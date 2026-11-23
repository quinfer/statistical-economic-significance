"""Mathematical checks for public teaching calculations, not empirical validation."""
import math
import unittest
from implementations.normal_model import (
    interval, normal_cdf, normal_posterior, power_two_sided, tost_p, two_sided_p,
)


class NormalModelTests(unittest.TestCase):
    def test_reference_values_and_tails(self):
        self.assertEqual(two_sided_p(0., 1.), 1.)
        self.assertAlmostEqual(two_sided_p(1.959963984540054, 1.), .05)
        self.assertAlmostEqual(normal_cdf(0.), .5)
        self.assertGreater(two_sided_p(10., 1.), 0.)
        self.assertEqual(normal_cdf(-math.inf), 0.)
        self.assertEqual(normal_cdf(math.inf), 1.)

    def test_intervals_and_unit_changes(self):
        lo, hi = interval(0., 1.)
        self.assertAlmostEqual(hi, 1.959963984540054)
        self.assertAlmostEqual(lo, -hi)
        self.assertAlmostEqual(two_sided_p(2., 3.), two_sided_p(200., 300.))
        for a, b in zip(interval(2., 3.), interval(200., 300.)):
            self.assertAlmostEqual(a * 100, b)
        self.assertAlmostEqual(tost_p(2., 3., 4.), tost_p(200., 300., 400.))

    def test_power_size_symmetry_and_order(self):
        self.assertAlmostEqual(power_two_sided(0., 1.), .05)
        self.assertAlmostEqual(power_two_sided(2., 1.), power_two_sided(-2., 1.))
        self.assertLess(power_two_sided(1., 1.), power_two_sided(2., 1.))
        self.assertGreater(power_two_sided(10., 1.), .999999)

    def test_equivalence_is_interval_containment(self):
        for alpha in (.01, .05, .1):
            for estimate in (-3., -.3, 0., .3, 3.):
                for se in (.02, .2, 2.):
                    lo, hi = interval(estimate, se, 1 - 2 * alpha)
                    self.assertEqual(tost_p(estimate, se, 1.) < alpha,
                                     lo > -1. and hi < 1.)
        self.assertLess(two_sided_p(.1, .02), .05)
        self.assertLess(tost_p(.1, .02, 1.), .05)
        self.assertGreater(tost_p(0., 1., .1), .05)

    def test_proper_prior_and_decision_sensitivity(self):
        mean, sd = normal_posterior(400., 500., prior_sd=1000.)
        self.assertAlmostEqual(mean, 320.)
        self.assertAlmostEqual(sd, math.sqrt(200000.))
        tight_mean, tight_sd = normal_posterior(400., 500., prior_sd=100.)
        self.assertAlmostEqual(tight_mean, 400 / 26)
        self.assertAlmostEqual(tight_sd, math.sqrt(250000 / 26))
        self.assertGreater(mean - 100., 0.)
        self.assertLess(tight_mean - 100., 0.)
        self.assertLess(mean - 500., 0.)

    def test_invalid_inputs(self):
        for se in (0., -1., math.nan, math.inf):
            for fn in (two_sided_p, interval, power_two_sided):
                with self.assertRaises(ValueError):
                    fn(1., se)
        for bad in (0., 1., -1., math.nan):
            with self.assertRaises(ValueError):
                interval(1., 1., bad)
            with self.assertRaises(ValueError):
                power_two_sided(1., 1., bad)
        for bad in (0., -1., math.inf):
            with self.assertRaises(ValueError):
                tost_p(1., 1., bad)
            with self.assertRaises(ValueError):
                normal_posterior(1., 1., prior_sd=bad)
        with self.assertRaises(ValueError):
            two_sided_p(math.nan, 1.)


if __name__ == "__main__":
    unittest.main()
