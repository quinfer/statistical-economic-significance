"""Synthetic known-SE normal power, coverage and equivalence experiments.

The direct normal draws have the same distribution as sample means of n iid
N(theta, sigma**2) effect measurements. No policy or market data are used.
"""
import math
from statistics import NormalDist

from implementations.normal_model import normal_cdf
from simulations.common import mean_summary, rate_summary, rng_for


def _integer(value, name, minimum):
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")


def _positive(value, name):
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be finite and positive")


def _normal_between(lower, upper, effect, se):
    if lower >= upper:
        return 0.
    return max(0., normal_cdf((upper - effect) / se)
               - normal_cdf((lower - effect) / se))


def exact_benchmarks(effect, true_se, reported_se, margin=100., alpha=.05):
    """Exact repeated-sampling probabilities under the declared normal DGP."""
    if not math.isfinite(effect):
        raise ValueError("effect must be finite")
    for value, name in ((true_se, "true_se"), (reported_se, "reported_se"),
                        (margin, "margin")):
        _positive(value, name)
    if not math.isfinite(alpha) or not 0 < alpha < .5:
        raise ValueError("alpha must be strictly between 0 and 0.5")
    normal = NormalDist()
    critical = -normal.inv_cdf(alpha / 2) * reported_se
    coverage_halfwidth = -normal.inv_cdf(.025) * reported_se
    equivalence_halfwidth = -normal.inv_cdf(alpha) * reported_se
    lower, upper = -margin + equivalence_halfwidth, margin - equivalence_halfwidth
    reject = (normal_cdf((-critical - effect) / true_se)
              + normal_cdf((effect - critical) / true_se))
    equivalent = _normal_between(lower, upper, effect, true_se)
    both = (_normal_between(lower, min(upper, -critical), effect, true_se)
            + _normal_between(max(lower, critical), upper, effect, true_se))
    return {
        "estimate_mean": effect,
        "zero_rejection": reject,
        "coverage95": _normal_between(-coverage_halfwidth, coverage_halfwidth, 0., true_se),
        "equivalence": equivalent,
        "both_reject": both,
        "neither_reject": max(0., 1 - reject - equivalent + both),
        "positive_beyond_margin": normal_cdf(
            (effect - margin - equivalence_halfwidth) / true_se),
    }


def simulate_scenario(effect, sample_size, *, sigma=1000., margin=100., alpha=.05,
                      reported_se_ratio=1., replications=50000, seed=20261123,
                      scenario_id="custom"):
    """Run one repeated-study design. All monetary inputs are pounds/person/year.

    `reported_se_ratio` changes the inference rule, not the sampling DGP.
    Stable scenario labels determine independent streams in the default suite.
    Reusing a label and seed permits common-random-number sensitivity comparisons.
    """
    _integer(sample_size, "sample_size", 1)
    _integer(replications, "replications", 2)
    if isinstance(seed, bool) or not isinstance(seed, int):
        raise ValueError("seed must be an integer")
    for value, name in ((sigma, "sigma"), (reported_se_ratio, "reported_se_ratio")):
        _positive(value, name)
    true_se = sigma / math.sqrt(sample_size)
    reported_se = true_se * reported_se_ratio
    benchmarks = exact_benchmarks(effect, true_se, reported_se, margin, alpha)
    rng, derived_seed = rng_for(seed, f"power:{scenario_id}")
    normal = NormalDist()
    critical = -normal.inv_cdf(alpha / 2) * reported_se
    coverage_halfwidth = -normal.inv_cdf(.025) * reported_se
    equivalence_halfwidth = -normal.inv_cdf(alpha) * reported_se
    counts = {key: 0 for key in benchmarks if key != "estimate_mean"}
    estimates = []
    for _ in range(replications):
        estimate = rng.gauss(effect, true_se)
        estimates.append(estimate)
        rejected = abs(estimate) > critical
        equivalent = (-margin < estimate - equivalence_halfwidth
                      and estimate + equivalence_halfwidth < margin)
        counts["zero_rejection"] += rejected
        counts["coverage95"] += abs(estimate - effect) <= coverage_halfwidth
        counts["equivalence"] += equivalent
        counts["both_reject"] += rejected and equivalent
        counts["neither_reject"] += not rejected and not equivalent
        counts["positive_beyond_margin"] += estimate - equivalence_halfwidth > margin
    metrics = {key: rate_summary(value, replications) for key, value in counts.items()}
    metrics["estimate_mean"] = mean_summary(estimates)
    return {
        "id": scenario_id,
        "parameters": {"effect": effect, "sample_size": sample_size, "sigma": sigma,
                       "true_se": true_se, "reported_se": reported_se,
                       "reported_se_ratio": reported_se_ratio, "margin": margin,
                       "alpha": alpha, "units": "pounds per person per year"},
        "derived_seed": derived_seed,
        "metrics": metrics,
        "benchmarks": benchmarks,
    }


def run(replications=50000, seed=20261123):
    """A balanced design grid plus a boundary and an SE-misspecification case."""
    specifications = [
        (f"{name}_n{n}", effect, n, 1.)
        for name, effect in (("null", 0.), ("small", 20.), ("meaningful", 200.))
        for n in (100, 2500, 100000)
    ]
    specifications.extend([
        ("equivalence_boundary_n2500", 100., 2500, 1.),
        ("understated_se_null_n2500", 0., 2500, .5),
    ])
    scenarios = [simulate_scenario(effect, n, reported_se_ratio=ratio,
                                  replications=replications, seed=seed,
                                  scenario_id=name)
                 for name, effect, n, ratio in specifications]
    return {
        "lab": "power",
        "design": {
            "label": "ILLUSTRATION: synthetic normal effect measurements; no empirical data",
            "estimand": "Fixed hypothetical mean one-year policy effect in an eligible target population",
            "units": "pounds per person per year",
            "dgp": "Yi iid N(theta, 1000^2); draw Xbar directly from N(theta, 1000^2/n)",
            "estimator": "Unbiased sample mean Xbar; no fitted nuisance parameters",
            "uncertainty_model": "Known-SE normal inference; report sigma/sqrt(n) except explicit ratio-0.5 stress case",
            "identification": "Effect measurements assumed unbiased for the target; confounding, spillovers and transport problems absent by design",
            "alpha": .05,
            "equivalence_margin": 100.,
            "margin_basis": "Fixed teaching assumption before simulation, not an estimated welfare threshold",
            "decision_criterion": "No adoption decision or utility loss; compare zero-null, equivalence and positive-above-margin classifications",
            "error_events": "False zero rejection under theta=0; false equivalence under |theta|>=100; interval noncoverage",
            "seed": seed,
            "replications_per_scenario": replications,
            "monte_carlo": "Independent repeated studies within each scenario. Rates have binomial MCSE and Wilson intervals; mean has sample-SD/sqrt(R) MCSE. These are not the study's sampling SE or confidence interval.",
            "limitations": "No real policy calibration, estimated variances, clustering, serial dependence, selective reporting or causal identification test. SE stress changes only reported uncertainty; it does not generate dependent raw data.",
        },
        "scenarios": scenarios,
    }
