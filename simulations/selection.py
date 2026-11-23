"""Synthetic significance and search selection; no empirical market observations.

The estimator is normal with known SE. Conditional risks concern the specified
filter and effect, rather than a universal model of publication or factor search.
"""
from math import exp, isfinite, pi, sqrt
from statistics import NormalDist

from implementations.normal_model import normal_cdf
from simulations.common import mean_summary, rate_summary, rng_for, validate_run

_NORMAL = NormalDist()


def _validate(effect, se, alpha):
    if not isfinite(effect):
        raise ValueError("effect must be finite")
    if not isfinite(se) or se <= 0:
        raise ValueError("se must be positive and finite")
    if not isfinite(alpha) or not 0 < alpha < 1:
        raise ValueError("alpha must lie strictly between zero and one")


def selection_benchmarks(effect, se, alpha=.05):
    """Exact normal-tail moments for selection on abs(estimate/se) > z.

    Type S and Type M are undefined at a zero true effect. If selection has
    numerically zero probability, all conditional benchmarks are undefined.
    """
    _validate(effect, se, alpha)
    z = -_NORMAL.inv_cdf(alpha / 2)
    a, b = -z - effect / se, z - effect / se
    lower, upper = normal_cdf(a), normal_cdf(-b)
    probability = lower + upper
    result = dict(rejection_rate=probability, unconditional_bias=0.,
                  selected_holdout_bias=0.)
    if probability == 0:
        result.update(selected_bias=None, selected_absolute_mean=None,
                      selected_type_s=None, selected_type_m=None,
                      selected_discovery_minus_holdout=None)
        return result
    phi_a = exp(-a * a / 2) / sqrt(2 * pi)
    phi_b = exp(-b * b / 2) / sqrt(2 * pi)
    bias = se * (phi_b - phi_a) / probability
    absolute_mean = (effect * (upper - lower) + se * (phi_b + phi_a)) / probability
    result.update(
        selected_bias=bias,
        selected_absolute_mean=absolute_mean,
        selected_type_s=(lower if effect > 0 else upper) / probability if effect else None,
        selected_type_m=absolute_mean / abs(effect) if effect else None,
        selected_discovery_minus_holdout=bias,
    )
    return result


def summarise_selection(discovery, holdout, effect, se, alpha=.05):
    """Summarise paired discovery/independent-holdout estimates.

    Inputs are equal-length lists. The holdout is observed for every simulated
    study, but conditional summaries retain only studies passing discovery's
    filter. Empty groups and undefined zero-effect ratios are explicit nulls.
    """
    _validate(effect, se, alpha)
    if len(discovery) != len(holdout):
        raise ValueError("discovery and holdout must have equal lengths")
    if not all(isfinite(x) for x in discovery + holdout):
        raise ValueError("all estimates must be finite")
    cutoff = -_NORMAL.inv_cdf(alpha / 2) * se
    pairs = [(x, y) for x, y in zip(discovery, holdout) if abs(x) > cutoff]
    selected = len(pairs)
    metrics = dict(
        rejection_rate=rate_summary(selected, len(discovery)),
        unconditional_bias=mean_summary([x - effect for x in discovery]),
        selected_bias=mean_summary([x - effect for x, _ in pairs]),
        selected_absolute_mean=mean_summary([abs(x) for x, _ in pairs]),
        selected_holdout_bias=mean_summary([y - effect for _, y in pairs]),
        selected_discovery_minus_holdout=mean_summary([x - y for x, y in pairs]),
        selected_type_s=rate_summary(sum(x * effect < 0 for x, _ in pairs), selected)
                        if effect else rate_summary(0, 0),
        selected_type_m=mean_summary([abs(x) / abs(effect) for x, _ in pairs])
                        if effect else mean_summary([]),
    )
    return metrics, selected


def run(replications=50000, seed=20261123):
    """Run five independently seeded scenarios, returning JSON-safe summaries."""
    validate_run(replications, seed)
    se, alpha = 10., .05
    scenarios = []
    for name, effect in [("null", 0.), ("weak_positive", 1.),
                         ("strong_positive", 30.), ("weak_negative", -1.)]:
        scenario_id = "single_" + name
        rng, derived_seed = rng_for(seed, "selection:" + scenario_id)
        discovery, holdout = [], []
        for _ in range(replications):
            discovery.append(rng.gauss(effect, se))
            holdout.append(rng.gauss(effect, se))
        metrics, selected = summarise_selection(discovery, holdout, effect, se, alpha)
        scenarios.append(dict(
            id=scenario_id, derived_seed=derived_seed,
            parameters=dict(true_effect=effect, known_se=se, alpha=alpha,
                            replications=replications, units="basis points per month"),
            selected_count=selected, metrics=metrics,
            benchmarks=selection_benchmarks(effect, se, alpha),
        ))

    scenario_id = "twenty_independent_null_candidates"
    rng, derived_seed = rng_for(seed, "selection:" + scenario_id)
    candidates = 20
    cutoff = -_NORMAL.inv_cdf(alpha / 2) * se
    corrected_cutoff = -_NORMAL.inv_cdf(alpha / (2 * candidates)) * se
    winner, holdout = [], []
    corrected_rejections = 0
    for _ in range(replications):
        estimates = [rng.gauss(0., se) for _ in range(candidates)]
        selected = max(estimates, key=abs)
        winner.append(selected)
        # With independent, identically null candidates, sampling only the
        # chosen candidate's new holdout is equivalent to generating all 20.
        holdout.append(rng.gauss(0., se))
        corrected_rejections += abs(selected) > corrected_cutoff
    pairs = [(x, y) for x, y in zip(winner, holdout) if abs(x) > cutoff]
    number_selected = len(pairs)
    scenarios.append(dict(
        id=scenario_id, derived_seed=derived_seed, selected_count=number_selected,
        parameters=dict(true_effect=0., known_se=se, alpha=alpha, candidates=candidates,
                        replications=replications, units="basis points per month",
                        search="Select maximum absolute discovery z; publish if unadjusted p < alpha"),
        metrics=dict(
            family_rejection_rate=rate_summary(number_selected, replications),
            bonferroni_family_rejection_rate=rate_summary(corrected_rejections, replications),
            winner_signed_mean=mean_summary(winner),
            winner_absolute_mean=mean_summary([abs(x) for x in winner]),
            selected_winner_signed_mean=mean_summary([x for x, _ in pairs]),
            selected_winner_absolute_mean=mean_summary([abs(x) for x, _ in pairs]),
            selected_holdout_signed_mean=mean_summary([y for _, y in pairs]),
            selected_holdout_absolute_mean=mean_summary([abs(y) for _, y in pairs]),
            selected_discovery_minus_holdout_absolute=mean_summary([abs(x)-abs(y) for x, y in pairs]),
        ),
        benchmarks=dict(
            family_rejection_rate=1 - (1 - alpha) ** candidates,
            bonferroni_family_rejection_rate=1 - (1 - alpha / candidates) ** candidates,
            winner_signed_mean=0., selected_winner_signed_mean=0.,
            selected_holdout_signed_mean=0., selected_holdout_absolute_mean=se * sqrt(2 / pi),
        ),
    ))
    return dict(
        lab="selection", seed=seed, replications=replications,
        design=dict(
            label="ILLUSTRATION: synthetic normal estimates, not observed market returns",
            estimand="Population monthly gross factor-model alpha of a stipulated hypothetical candidate",
            population="Hypothetical repeated studies of fixed candidates in one unchanged trading regime",
            units="basis points per month; no annualisation or trading costs",
            dgp="Discovery X and independent holdout Y are N(theta, 10^2); fixed theta within each single-candidate scenario. Search has 20 independent theta=0 candidates per repetition.",
            estimator="Normal estimate of alpha with known standard error 10 bp",
            selection="Two-sided zero-null test at alpha=.05, retaining abs(X/10)>z_.975",
            error_criterion="Rejection, conditional sign error, conditional absolute exaggeration and estimation bias; no welfare loss or investment recommendation is specified",
            assumptions="Correct normal model; known SE; unchanged effect across discovery and holdout; independent studies and candidates; no factor misspecification, dependence, costs, market adaptation or optional stopping",
            monte_carlo="Rate MCSE=sqrt(p_hat*(1-p_hat)/denominator); mean MCSE=sample SD/sqrt(denominator); conditional denominators are selected-study counts. Wilson95 accompanies rates; not a confidence interval for an economic effect.",
            undefined="Type S and Type M are undefined at theta=0; every conditional metric is unavailable when no study is selected. JSON null is not zero. Small selected counts make asymptotic MCSE unreliable.",
            pairing="Discovery and holdout differences are summarised within study; their MCSE uses paired differences rather than adding independent group standard errors",
            source_limit="Conceptual motivation uses existing selected-section Gelman–Carlin notes. Finance notes have abstract/selected-section coverage. No new source reading or replication of their empirical findings is claimed.",
        ),
        scenarios=scenarios,
    )
