"""Monte Carlo bookkeeping shared by the three synthetic teaching labs."""
import hashlib
import math
import random
from statistics import NormalDist


def validate_run(replications, seed):
    if isinstance(replications, bool) or not isinstance(replications, int) or replications < 2:
        raise ValueError("replications must be an integer of at least 2")
    if isinstance(seed, bool) or not isinstance(seed, int) or seed < 0:
        raise ValueError("seed must be a non-negative integer")


def rng_for(seed, label):
    """Stable, order-independent stream per named scenario; not Python's hash()."""
    validate_run(2, seed)
    if not isinstance(label, str) or not label:
        raise ValueError("a non-empty scenario label is required")
    digest = hashlib.sha256(f"significance-labs-v1:{seed}:{label}".encode()).digest()
    derived_seed = int.from_bytes(digest[:8], "big")
    return random.Random(derived_seed), derived_seed


def mean_summary(values):
    """Mean and sample-SD/sqrt(n) MCSE for independent replication-level values.

    For paired policy differences, subtract within replication BEFORE calling.
    Null output for an empty conditional group is not an estimate of zero.
    """
    values = list(values)
    n = len(values)
    if not all(math.isfinite(x) for x in values):
        raise ValueError("replication values must be finite")
    if not n:
        return dict(estimate=None, mcse=None, n=0)
    mean = math.fsum(values) / n
    mcse = (math.sqrt(math.fsum((x-mean)**2 for x in values) / (n*(n-1)))
            if n > 1 else None)
    return dict(estimate=mean, mcse=mcse, n=n)


def rate_summary(successes, n):
    """Binomial plug-in MCSE and Wilson 95% Monte Carlo interval.

    A zero empirical MCSE at an all-zero/all-one boundary is not certainty;
    use the non-degenerate Wilson interval, and increase replications as needed.
    """
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (successes, n)):
        raise ValueError("successes and n must be integer counts")
    if not 0 <= successes <= n:
        raise ValueError("require 0 <= successes <= n")
    if not n:
        return dict(estimate=None, mcse=None, n=0, successes=0, wilson95=None)
    p = successes / n
    z = NormalDist().inv_cdf(.975)
    denominator = 1 + z*z/n
    centre = (p + z*z/(2*n)) / denominator
    half = z * math.sqrt(p*(1-p)/n + z*z/(4*n*n)) / denominator
    lower = 0. if successes == 0 else max(0., centre-half)
    upper = 1. if successes == n else min(1., centre+half)
    return dict(estimate=p, mcse=math.sqrt(p*(1-p)/n), n=n, successes=successes,
                wilson95=[lower, upper])
