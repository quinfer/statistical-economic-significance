import math
import unittest
from simulations.common import mean_summary, rate_summary, rng_for, validate_run


class MonteCarloBookkeepingTests(unittest.TestCase):
    def test_mean_standard_error_and_pairing(self):
        result = mean_summary([1., 2., 3.])
        self.assertEqual(result['estimate'], 2.)
        self.assertAlmostEqual(result['mcse'], 1 / math.sqrt(3))
        a, b = [11., 21., 31.], [10., 20., 30.]
        paired = mean_summary([x-y for x, y in zip(a, b)])
        self.assertEqual(paired['estimate'], 1.)
        self.assertEqual(paired['mcse'], 0.)

    def test_empty_and_boundary_semantics(self):
        self.assertIsNone(mean_summary([])['estimate'])
        self.assertIsNone(mean_summary([1.])['mcse'])
        self.assertIsNone(rate_summary(0, 0)['wilson95'])
        self.assertGreater(rate_summary(0, 100)['wilson95'][1], 0.)
        self.assertLess(rate_summary(100, 100)['wilson95'][0], 1.)
        self.assertEqual(rate_summary(0, 50000)['wilson95'][0], 0.)
        self.assertEqual(rate_summary(50000, 50000)['wilson95'][1], 1.)
        self.assertAlmostEqual(rate_summary(50, 100)['mcse'], .05)

    def test_streams_are_reproducible_and_order_independent(self):
        a, sa = rng_for(42, 'power:example')
        b, sb = rng_for(42, 'power:example')
        c, sc = rng_for(42, 'decisions:example')
        self.assertEqual(sa, sb)
        self.assertNotEqual(sa, sc)
        self.assertEqual([a.random() for _ in range(10)], [b.random() for _ in range(10)])
        self.assertNotEqual(sc, rng_for(43, 'decisions:example')[1])

    def test_invalid_inputs(self):
        for n, seed in [(1, 42), (True, 42), (3.5, 42), (10, -1), (10, True)]:
            with self.assertRaises(ValueError):
                validate_run(n, seed)
        for successes, n in [(-1, 10), (11, 10), (1.5, 10), (0, -1)]:
            with self.assertRaises(ValueError):
                rate_summary(successes, n)
        with self.assertRaises(ValueError):
            mean_summary([math.nan])
