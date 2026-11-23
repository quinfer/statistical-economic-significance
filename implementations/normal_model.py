"""Deterministic teaching calculations for an unbiased, known-SE normal estimate.

These functions do not establish identification, model fit or economic importance.
Inputs must use the same units. No random draws or third-party packages are used.
"""
from math import erfc, isfinite, sqrt
from statistics import NormalDist

_NORMAL = NormalDist()


def _finite(value, name):
    if not isfinite(value):
        raise ValueError(f"{name} must be finite")
    return value


def _positive(value, name):
    _finite(value, name)
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return value


def _probability(value, name):
    _finite(value, name)
    if not 0 < value < 1:
        raise ValueError(f"{name} must be strictly between 0 and 1")
    return value


def normal_cdf(z):
    """Standard normal cumulative probability; infinite limits are supported."""
    if z != z:
        raise ValueError("z must not be NaN")
    return erfc(-z / sqrt(2)) / 2


def two_sided_p(estimate, se):
    """Two-sided p-value for H0: theta = 0, with known standard error."""
    _finite(estimate, "estimate")
    _positive(se, "se")
    return 2 * normal_cdf(-abs(estimate / se))


def interval(estimate, se, level=.95):
    """Equal-tailed normal confidence interval; coverage is model-conditional."""
    _finite(estimate, "estimate")
    _positive(se, "se")
    _probability(level, "level")
    # Lower-tail quantile avoids rounding 1 - a tiny tail probability to one.
    halfwidth = -_NORMAL.inv_cdf((1 - level) / 2) * se
    return estimate - halfwidth, estimate + halfwidth


def power_two_sided(effect, se, alpha=.05):
    """Pr(reject H0: theta=0 | theta=effect), at fixed se and size alpha."""
    _finite(effect, "effect")
    _positive(se, "se")
    _probability(alpha, "alpha")
    critical = -_NORMAL.inv_cdf(alpha / 2)
    shift = effect / se
    return min(1., normal_cdf(-critical - shift) + normal_cdf(shift - critical))


def tost_p(estimate, se, margin):
    """TOST p-value for H0: theta <= -margin OR theta >= margin.

    Reject at p < alpha to support -margin < theta < margin. Equivalently,
    the 100*(1-2*alpha)% interval must lie strictly inside the fixed margins.
    The margin must be justified independently of the observed estimate.
    """
    _finite(estimate, "estimate")
    _positive(se, "se")
    _positive(margin, "margin")
    return max(normal_cdf(-(estimate + margin) / se),
               normal_cdf((estimate - margin) / se))


def normal_posterior(estimate, se, prior_mean=0., prior_sd=1000.):
    """Return (mean, sd) under a proper N(prior_mean, prior_sd**2) prior.

    Likelihood: estimate | theta ~ N(theta, se**2), with se known. The default
    prior scale belongs to the pounds example; set it explicitly in other units.
    """
    _finite(estimate, "estimate")
    _finite(prior_mean, "prior_mean")
    _positive(se, "se")
    _positive(prior_sd, "prior_sd")
    # Ratios avoid squaring a potentially large standard deviation.
    if prior_sd >= se:
        ratio = se / prior_sd
        weight = 1 / (1 + ratio * ratio)
        post_sd = se / sqrt(1 + ratio * ratio)
    else:
        ratio = prior_sd / se
        weight = ratio * ratio / (1 + ratio * ratio)
        post_sd = prior_sd / sqrt(1 + ratio * ratio)
    return weight * estimate + (1 - weight) * prior_mean, post_sd
