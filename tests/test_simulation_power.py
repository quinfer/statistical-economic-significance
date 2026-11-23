"""Check simulated operating characteristics against exact normal probabilities."""
import math
import unittest

from simulations.power import exact_benchmarks, run, simulate_scenario


class PowerLabTests(unittest.TestCase):
    def test_simulated_probabilities_and_means_match_analytic_targets(self):
        report = run(replications=12000, seed=34019)
        for scenario in report["scenarios"]:
            for metric, target in scenario["benchmarks"].items():
                with self.subTest(scenario=scenario["id"], metric=metric):
                    summary = scenario["metrics"][metric]
                    if metric == "estimate_mean":
                        mcse = scenario["parameters"]["true_se"] / math.sqrt(summary["n"])
                        tolerance = 6 * mcse
                    else:
                        # Use the exact Bernoulli variance, including when no rare
                        # events occurred and the plug-in reported MCSE is zero.
                        mcse = math.sqrt(target * (1 - target) / summary["n"])
                        tolerance = 6 * mcse + 1 / summary["n"]
                    self.assertLessEqual(abs(summary["estimate"] - target), tolerance)

    def test_reference_operating_characteristics(self):
        correct = exact_benchmarks(0., 20., 20.)
        self.assertAlmostEqual(correct["zero_rejection"], .05)
        self.assertAlmostEqual(correct["coverage95"], .95)
        # A wide 90% interval cannot ever fit in +/-100 when SE=100.
        self.assertEqual(exact_benchmarks(0., 100., 100.)["equivalence"], 0.)
        understated = exact_benchmarks(0., 20., 10.)
        self.assertGreater(understated["zero_rejection"], .3)
        self.assertLess(understated["coverage95"], .7)
        # Coverage remains 95% when the testing threshold changes.
        self.assertAlmostEqual(exact_benchmarks(0., 20., 20., alpha=.01)["coverage95"], .95)

    def test_seed_reproduces_run_and_streams_are_distinct(self):
        first = run(replications=40, seed=7)
        self.assertEqual(first, run(replications=40, seed=7))
        seeds = [s["derived_seed"] for s in first["scenarios"]]
        self.assertEqual(len(seeds), len(set(seeds)))
        self.assertNotEqual(first, run(replications=40, seed=8))

    def test_invalid_designs_fail(self):
        for kwargs in ({"replications": 0}, {"replications": 1}, {"replications": True},
                       {"sigma": 0}, {"reported_se_ratio": .0}, {"margin": -1},
                       {"alpha": .5}, {"seed": 1.5}, {"effect": math.nan},
                       {"sample_size": 0}):
            args = {"effect": 0., "sample_size": 100, "replications": 10}
            args.update(kwargs)
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                simulate_scenario(**args)


if __name__ == "__main__":
    unittest.main()
