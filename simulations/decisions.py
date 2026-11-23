"""Synthetic policy evaluation under a known-SE normal observation model.

Each replication is a new decision problem. Utility and regret use the simulated
population mean, not a draw of individual outcomes. No empirical claims are made.
"""
from math import exp, isfinite, pi, sqrt
from statistics import NormalDist

from implementations.normal_model import normal_cdf, normal_posterior
from simulations.common import mean_summary, rate_summary, rng_for, validate_run

POLICIES = ("bayes", "skeptical_bayes", "positive_significance", "cost_confidence",
            "plugin", "always", "never")
ALPHA = .05
BASE_PRIOR_MEAN = 0.
BASE_PRIOR_SD = 1000.
SKEPTICAL_PRIOR_SD = 100.


def _positive(value, name):
    if not isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be positive and finite")


def bayes_cutoff(cost, se, prior_mean=BASE_PRIOR_MEAN, prior_sd=BASE_PRIOR_SD):
    """Adopt iff estimate exceeds this cutoff under linear expected utility."""
    _positive(se, "se")
    _positive(prior_sd, "prior_sd")
    if not isfinite(cost) or not isfinite(prior_mean):
        raise ValueError("cost and prior mean must be finite")
    weight = prior_sd ** 2 / (prior_sd ** 2 + se ** 2)
    return (cost - (1 - weight) * prior_mean) / weight


def policy_cutoffs(cost, se):
    """The finite thresholds; always/never do not need a numerical threshold."""
    return {
        "bayes": bayes_cutoff(cost, se),
        "skeptical_bayes": bayes_cutoff(cost, se, prior_sd=SKEPTICAL_PRIOR_SD),
        "positive_significance": -NormalDist().inv_cdf(ALPHA / 2) * se,
        "cost_confidence": cost - NormalDist().inv_cdf(ALPHA) * se,
        "plugin": cost,
    }


def policy_actions(estimate, cost, se):
    """Return all seven actions; zero posterior net benefit favours the status quo."""
    if not isfinite(estimate):
        raise ValueError("estimate must be finite")
    cuts = policy_cutoffs(cost, se)
    return {**{name: estimate > cut for name, cut in cuts.items()},
            "always": True, "never": False}


def _density(z):
    return exp(-z * z / 2) / sqrt(2 * pi)


def oracle_expected_utility(theta_mean, theta_sd, cost):
    """E[max(theta-cost, 0)] for normal theta, including a fixed state."""
    if not all(isfinite(x) for x in (theta_mean, theta_sd, cost)) or theta_sd < 0:
        raise ValueError("normal-state parameters must be finite and SD non-negative")
    if theta_sd == 0:
        return max(theta_mean - cost, 0.)
    z = (theta_mean - cost) / theta_sd
    return (theta_mean - cost) * normal_cdf(z) + theta_sd * _density(z)


def analytical_policy(theta_mean, theta_sd, cost, se, policy):
    """Exact adoption, utility and regret for each threshold rule.

    If Y=theta+noise, Cov(theta,Y)=theta_sd**2. Thus threshold utility is
    (theta_mean-cost)*Pr(Y>t) + Cov(theta,Y)/sd(Y)*phi((t-E[Y])/sd(Y)).
    This is evaluation under the supplied DGP, which need not match a policy prior.
    """
    _positive(se, "se")
    oracle = oracle_expected_utility(theta_mean, theta_sd, cost)
    if policy not in POLICIES:
        raise ValueError(f"Unknown policy: {policy}")
    if policy == "always":
        adoption, utility = 1., theta_mean - cost
        second_moment = theta_sd ** 2 + utility ** 2
    elif policy == "never":
        adoption, utility = 0., 0.
        second_moment = 0.
    else:
        threshold = policy_cutoffs(cost, se)[policy]
        marginal_sd = sqrt(theta_sd ** 2 + se ** 2)
        z = (threshold - theta_mean) / marginal_sd
        adoption = normal_cdf(-z)
        utility = ((theta_mean - cost) * adoption
                   + theta_sd ** 2 / marginal_sd * _density(z))
        slope = theta_sd ** 2 / marginal_sd
        conditional_variance = theta_sd ** 2 - slope ** 2
        second_moment = (((theta_mean - cost) ** 2 + conditional_variance) * adoption
                         + 2 * (theta_mean - cost) * slope * _density(z)
                         + slope ** 2 * (adoption + z * _density(z)))
    return {"adoption": adoption, "utility": utility, "regret": oracle - utility,
            "utility_sd": sqrt(max(second_moment - utility ** 2, 0.))}


def _scenario(sid, theta_mean, theta_sd, cost, evaluation, replications, seed):
    se = 500.
    rng, derived_seed = rng_for(seed, f"decisions/{sid}")
    cutoffs = policy_cutoffs(cost, se)
    utility = {name: [] for name in POLICIES}
    regret = {name: [] for name in POLICIES}
    adoption = {name: 0 for name in POLICIES}
    paired_utility = {name: [] for name in POLICIES if name != "bayes"}
    paired_regret = {name: [] for name in POLICIES if name != "bayes"}
    oracle_values = []
    without_rejection = 0
    for _ in range(replications):
        theta = rng.gauss(theta_mean, theta_sd) if theta_sd else theta_mean
        estimate = theta + rng.gauss(0., se)
        actions = {**{name: estimate > cut for name, cut in cutoffs.items()},
                   "always": True, "never": False}
        oracle = max(theta - cost, 0.)
        oracle_values.append(oracle)
        baseline = float(actions["bayes"]) * (theta - cost)
        without_rejection += actions["bayes"] and not actions["positive_significance"]
        for name, action in actions.items():
            value = float(action) * (theta - cost)
            loss = oracle - value
            utility[name].append(value)
            regret[name].append(loss)
            adoption[name] += action
            if name != "bayes":
                paired_utility[name].append(value - baseline)
                paired_regret[name].append(baseline - value)

    metrics = {"oracle_utility": mean_summary(oracle_values),
               "bayes_adoption_without_zero_rejection": rate_summary(without_rejection, replications)}
    oracle = oracle_expected_utility(theta_mean, theta_sd, cost)
    benchmarks = {"oracle_utility": oracle}
    exact = {name: analytical_policy(theta_mean, theta_sd, cost, se, name) for name in POLICIES}
    # All declared costs yield a positive Bayes cutoff. This is the interval
    # between that cutoff and the positive, two-sided-zero-null rejection cutoff.
    benchmarks["bayes_adoption_without_zero_rejection"] = max(
        0., exact["bayes"]["adoption"] - exact["positive_significance"]["adoption"])
    for name in POLICIES:
        metrics[f"{name}_adoption"] = rate_summary(adoption[name], replications)
        metrics[f"{name}_utility"] = mean_summary(utility[name])
        metrics[f"{name}_regret"] = mean_summary(regret[name])
        for quantity in ("adoption", "utility", "regret"):
            benchmarks[f"{name}_{quantity}"] = exact[name][quantity]
        if name != "bayes":
            metrics[f"{name}_minus_bayes_utility"] = mean_summary(paired_utility[name])
            metrics[f"{name}_minus_bayes_regret"] = mean_summary(paired_regret[name])
            benchmarks[f"{name}_minus_bayes_utility"] = exact[name]["utility"] - exact["bayes"]["utility"]
            benchmarks[f"{name}_minus_bayes_regret"] = exact[name]["regret"] - exact["bayes"]["regret"]
    return {
        "id": sid, "derived_seed": derived_seed,
        "parameters": {"evaluation": evaluation, "theta_mean": theta_mean, "theta_sd": theta_sd,
                       "se": se, "cost": cost, "alpha": ALPHA,
                       "policy_prior_mean": BASE_PRIOR_MEAN, "policy_prior_sd": BASE_PRIOR_SD,
                       "skeptical_prior_sd": SKEPTICAL_PRIOR_SD, "policy_cutoffs": cutoffs},
        "metrics": metrics, "benchmarks": benchmarks,
    }


def run(replications=50000, seed=20261123):
    """Evaluate declared scenarios; uses paired outcomes across policies in each one."""
    validate_run(replications, seed)
    scenarios = [
        ("matched_prior_cost100", 0., 1000., 100., "matched_prior_predictive"),
        ("matched_prior_cost500", 0., 1000., 500., "matched_prior_predictive"),
        ("mismatched_prior_negative", -250., 100., 100., "mismatched_prior_predictive"),
        ("fixed_zero", 0., 0., 100., "fixed_state"),
        ("fixed_moderate_benefit", 400., 0., 100., "fixed_state"),
        ("fixed_large_benefit", 1200., 0., 100., "fixed_state"),
    ]
    # Check agreement between the threshold derivation and the existing posterior.
    post_mean, _ = normal_posterior(400., 500., prior_mean=0., prior_sd=1000.)
    assert post_mean > 100. and policy_actions(400., 100., 500.)["bayes"]
    return {
        "lab": "decisions",
        "design": {
            "label": "Illustration: synthetic policy evaluation, not evidence about a real programme",
            "replications": replications, "seed": seed,
            "random_streams": "Stable SHA-256 derivation from base seed and named scenario; each derived seed is reported",
            "estimand": "Unknown average gross benefit theta in one fixed eligible population over one year",
            "units": "pounds per eligible person over one year; adoption probabilities are unitless",
            "dgp": "Theta is normal with scenario mean/SD, or fixed when SD=0; estimate|theta ~ N(theta,500^2)",
            "estimator": "Unbiased normal estimate with known SE=500; identification is assumed valid",
            "actions": "Adopt once or choose status quo; all policies face identical simulated states and estimates",
            "utility": "adopt*(theta-cost), linear risk-neutral per-person payoff; status quo payoff zero",
            "loss": "Oracle regret=max(theta-cost,0)-utility; oracle knows theta but policies do not",
            "priors": "Baseline N(0,1000^2), skeptical N(0,100^2); both proper and fixed before outcomes",
            "cost_confidence_rule": "Adopt iff the one-sided 95% lower confidence bound exceeds known cost; false adoption probability <=.05 for theta<=cost under the model",
            "evaluation": "Matched prior predictive, mismatched prior predictive and fixed-state sampling performance are distinguished",
            "paired_comparisons": "Other policy minus baseline Bayes on each shared replication; report sample SD of differences / sqrt(R)",
            "mc_error": "Mean MCSE is sample SD/sqrt(R); rate MCSE is sqrt(p_hat*(1-p_hat)/R), with Wilson 95% interval",
            "limitations": "No individual outcome noise, welfare weights, risk aversion, uncertain costs, partial identification, delay, learning or realistic programme data",
        },
        "scenarios": [_scenario(*row, replications, seed) for row in scenarios],
    }
