import math
import unittest
from scripts.numeric_snapshot import assert_equivalent


class SnapshotTests(unittest.TestCase):
    def test_last_bit_variation_is_accepted(self):
        assert_equivalent({'critical': 1.9599639845400534, 'flags': [True]},
                          {'critical': 1.9599639845400536, 'flags': [True]})

    def test_meaningful_changes_fail(self):
        for actual, expected in [(.05, .06), (True, 1), ({'x': 1}, {'y': 1}),
                                 ([1], [1, 2]), (math.nan, math.nan),
                                 (math.inf, math.inf), ('source', 'illustration')]:
            with self.assertRaises(AssertionError):
                assert_equivalent(actual, expected)
