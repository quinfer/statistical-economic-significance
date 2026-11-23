import math
import unittest

from simulations.selection import run, selection_benchmarks, summarise_selection


class SelectionSimulationTests(unittest.TestCase):
    def assert_mc_close(self, summary, target):
        self.assertIsNotNone(summary['mcse'])
        # A rare event may be absent, giving plug-in MCSE zero even though
        # its true probability is positive. Use the known Bernoulli variance
        # for rate validation; the output separately supplies Wilson bounds.
        error = math.sqrt(target * (1-target) / summary['n']) if 'successes' in summary else summary['mcse']
        self.assertLessEqual(abs(summary['estimate'] - target), 6 * error + 1e-12)

    def test_exact_tail_benchmarks_and_sign_symmetry(self):
        null = selection_benchmarks(0., 10.)
        self.assertAlmostEqual(null['rejection_rate'], .05)
        self.assertAlmostEqual(null['selected_bias'], 0.)
        self.assertIsNone(null['selected_type_s'])
        self.assertIsNone(null['selected_type_m'])
        self.assertGreater(null['selected_absolute_mean'], 1.96 * 10)
        positive, negative = selection_benchmarks(1., 10.), selection_benchmarks(-1., 10.)
        self.assertAlmostEqual(positive['selected_bias'], -negative['selected_bias'])
        for key in ['rejection_rate', 'selected_type_s', 'selected_type_m']:
            self.assertAlmostEqual(positive[key], negative[key])

    def test_empty_selection_and_zero_effect_are_not_zero_risk(self):
        empty, count = summarise_selection([0., 1.], [2., -2.], 1., 10.)
        self.assertEqual(count, 0)
        self.assertEqual(empty['rejection_rate']['estimate'], 0.)
        for key in ['selected_bias', 'selected_type_s', 'selected_type_m', 'selected_holdout_bias']:
            self.assertIsNone(empty[key]['estimate'])
            self.assertIsNone(empty[key]['mcse'])
        null, count = summarise_selection([-30., -1., 0., 1., 30.], [0.] * 5, 0., 10.)
        self.assertEqual(count, 2)
        self.assertEqual(null['selected_bias']['estimate'], 0.)
        self.assertEqual(null['selected_absolute_mean']['estimate'], 30.)
        self.assertIsNone(null['selected_type_s']['estimate'])
        self.assertIsNone(null['selected_type_m']['estimate'])

    def test_simulated_rates_and_moments_match_analytic_benchmarks(self):
        result = run(replications=30000, seed=1847)
        for scenario in result['scenarios']:
            for metric, expected in scenario['benchmarks'].items():
                if expected is not None:
                    self.assert_mc_close(scenario['metrics'][metric], expected)

    def test_seed_reproducibility_and_validation(self):
        self.assertEqual(run(200, 82), run(200, 82))
        self.assertNotEqual(run(200, 82), run(200, 83))
        for invalid in [0, -1, 1, 2.5, True]:
            with self.assertRaises(ValueError):
                run(invalid)
        for se in [0., -1., math.inf]:
            with self.assertRaises(ValueError):
                selection_benchmarks(1., se)
        with self.assertRaises(ValueError):
            summarise_selection([1.], [], 1., 10.)
