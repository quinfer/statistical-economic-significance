import math
import unittest

from implementations.normal_model import normal_posterior
from simulations.decisions import (
    POLICIES, analytical_policy, bayes_cutoff, oracle_expected_utility, policy_actions, run,
)


class DecisionSimulationTests(unittest.TestCase):
    def test_bayes_threshold_matches_posterior_action(self):
        for cost in (100., 500.):
            for sd in (100., 1000.):
                cutoff = bayes_cutoff(cost, 500., prior_sd=sd)
                for estimate in (cutoff - 1., cutoff + 1.):
                    mean, _ = normal_posterior(estimate, 500., prior_sd=sd)
                    self.assertEqual(estimate > cutoff, mean > cost)
        self.assertAlmostEqual(bayes_cutoff(100., 500.), 125.)
        self.assertAlmostEqual(bayes_cutoff(100., 500., prior_sd=100.), 2600.)
        actions = policy_actions(400., 100., 500.)
        self.assertTrue(actions['bayes'])
        self.assertFalse(actions['positive_significance'])

    def test_cost_confidence_controls_false_adoption_at_break_even(self):
        for cost in (100., 500.):
            boundary = analytical_policy(cost, 0., cost, 500., 'cost_confidence')
            below = analytical_policy(cost - 500., 0., cost, 500., 'cost_confidence')
            self.assertAlmostEqual(boundary['adoption'], .05)
            self.assertLess(below['adoption'], .05)

    def test_analytic_optimality_has_a_scope(self):
        for cost in (100., 500.):
            baseline = analytical_policy(0., 1000., cost, 500., 'bayes')['utility']
            for policy in POLICIES:
                self.assertGreaterEqual(baseline + 1e-10,
                                        analytical_policy(0., 1000., cost, 500., policy)['utility'])
        # Correct-prior average optimality does not imply pointwise dominance.
        self.assertGreater(analytical_policy(400., 0., 100., 500., 'plugin')['utility'],
                           analytical_policy(400., 0., 100., 500., 'bayes')['utility'])
        self.assertGreater(analytical_policy(-250., 100., 100., 500., 'never')['utility'],
                           analytical_policy(-250., 100., 100., 500., 'bayes')['utility'])
        self.assertAlmostEqual(oracle_expected_utility(0., 1000., 0.), 1000 / math.sqrt(2 * math.pi))

    def test_monte_carlo_matches_exact_benchmarks_and_paired_identities(self):
        report = run(replications=12000, seed=173)
        for scenario in report['scenarios']:
            metrics = scenario['metrics']
            for key, target in scenario['benchmarks'].items():
                observed = metrics[key]
                # A declared fixed-seed stochastic check with generous MC tolerance.
                # For a rare-event utility with no observed adoptions, the sample
                # MCSE is zero. Use the exact utility variance as an independent
                # reference instead of pretending the DGP variance is zero.
                reference_mcse = observed['mcse']
                name = key.removesuffix('_utility')
                if key.endswith('_utility') and name in POLICIES:
                    p = scenario['parameters']
                    exact = analytical_policy(p['theta_mean'], p['theta_sd'], p['cost'], p['se'], name)
                    reference_mcse = max(reference_mcse, exact['utility_sd'] / math.sqrt(observed['n']))
                name = key.removesuffix('_regret')
                if key.endswith('_regret') and name in POLICIES and scenario['parameters']['theta_sd'] == 0:
                    p = scenario['parameters']
                    exact = analytical_policy(p['theta_mean'], p['theta_sd'], p['cost'], p['se'], name)
                    # At a fixed state the oracle is constant: regret and utility
                    # therefore have the same variance.
                    reference_mcse = max(reference_mcse, exact['utility_sd'] / math.sqrt(observed['n']))
                tolerance = 7 * reference_mcse + (1e-8 if 'adoption' not in key else .001)
                self.assertLessEqual(abs(observed['estimate'] - target), tolerance,
                                     f"{scenario['id']}:{key}")
            for policy in POLICIES:
                utility = metrics[f'{policy}_utility']['estimate']
                regret = metrics[f'{policy}_regret']['estimate']
                self.assertGreaterEqual(regret, -1e-12)
                self.assertAlmostEqual(utility + regret, metrics['oracle_utility']['estimate'], places=8)
                if policy != 'bayes':
                    du = metrics[f'{policy}_minus_bayes_utility']
                    dr = metrics[f'{policy}_minus_bayes_regret']
                    self.assertAlmostEqual(du['estimate'], -dr['estimate'])
                    self.assertAlmostEqual(du['mcse'], dr['mcse'])
                    self.assertAlmostEqual(du['estimate'], utility - metrics['bayes_utility']['estimate'])

    def test_invalid_replication_counts(self):
        for count in (0, 1, -3, True, 10.5):
            with self.assertRaises(ValueError):
                run(replications=count)


if __name__ == '__main__':
    unittest.main()
