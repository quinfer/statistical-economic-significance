"""Compare a numerical JSON snapshot without requiring platform-identical floats."""
import math


def assert_equivalent(actual, expected, path="$", rel_tol=1e-12, abs_tol=1e-15):
    """Require identical structure/text and close finite numbers; never blur booleans."""
    if isinstance(actual, bool) or isinstance(expected, bool):
        if type(actual) is not type(expected) or actual != expected:
            raise AssertionError(f"{path}: boolean mismatch")
    elif isinstance(actual, (int, float)) and isinstance(expected, (int, float)):
        if not (math.isfinite(actual) and math.isfinite(expected)
                and math.isclose(actual, expected, rel_tol=rel_tol, abs_tol=abs_tol)):
            raise AssertionError(f"{path}: numerical mismatch: {actual} versus {expected}")
    elif isinstance(actual, dict) and isinstance(expected, dict):
        if actual.keys() != expected.keys():
            raise AssertionError(f"{path}: object keys differ")
        for key in actual:
            assert_equivalent(actual[key], expected[key], f"{path}.{key}", rel_tol, abs_tol)
    elif isinstance(actual, list) and isinstance(expected, list):
        if len(actual) != len(expected):
            raise AssertionError(f"{path}: list lengths differ")
        for i, (a, e) in enumerate(zip(actual, expected)):
            assert_equivalent(a, e, f"{path}[{i}]", rel_tol, abs_tol)
    elif type(actual) is not type(expected) or actual != expected:
        raise AssertionError(f"{path}: value or type mismatch")
