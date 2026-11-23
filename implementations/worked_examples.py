#!/usr/bin/env python3
"""Print synthetic, deterministic examples as JSON; no files are modified."""
import json

try:
    from .normal_model import interval, normal_posterior, power_two_sided, tost_p, two_sided_p
except ImportError:  # Direct invocation from the repository root.
    from normal_model import interval, normal_posterior, power_two_sided, tost_p, two_sided_p


def results():
    cases = {}
    for name, estimate, se, margin in [
        ("small_precise", .1, .02, 1.),
        ("large_imprecise", 2., 2., 1.),
        ("precise_zero", 0., .001, .01),
        ("positive_but_not_above_margin", 1.1, .2, 1.),
    ]:
        cases[name] = dict(estimate=estimate, se=se, units="abstract effect units",
                           margin=margin, p_zero=two_sided_p(estimate, se),
                           ci95=interval(estimate, se), ci90=interval(estimate, se, .9),
                           p_tost=tost_p(estimate, se, margin))
    decisions = []
    for prior_sd in (1000., 100.):
        mean, sd = normal_posterior(400., 500., prior_sd=prior_sd)
        for cost in (100., 500.):
            net = mean - cost
            decisions.append(dict(prior_mean=0., prior_sd=prior_sd, posterior_mean=mean,
                                  posterior_sd=sd, cost=cost, expected_net=net,
                                  action="adopt" if net > 0 else "status quo"))
    gross = interval(20., 15.)
    return dict(
        label="ILLUSTRATIONS: synthetic inputs, deterministic calculations, no empirical data",
        model="Unbiased normal estimate with known SE, fixed comparisons and justified identification assumed",
        reproducibility="No random draws, seed or Monte Carlo error; floating-point arithmetic. Extremely small p-values can underflow to displayed 0.0, not mathematical zero.",
        cases=cases,
        power=dict(alpha=.05, se=1., units="abstract effect units",
                   by_effect={str(x): power_two_sided(x, 1.) for x in (0., .1, 1., 2., 3.)}),
        finance=dict(units="basis points per month", gross_alpha=20., se=15.,
                     ci95_gross=gross, p_zero_gross=two_sided_p(20., 15.),
                     ci95_net_by_known_cost={str(c): [x-c for x in gross] for c in (10., 25.)},
                     limits="No search, serial dependence, factor uncertainty, capacity or cost uncertainty modelled"),
        decision=dict(units="pounds per person", estimate=400., se=500.,
                      p_zero=two_sided_p(400., 500.),
                      utility="Risk-neutral linear benefit theta minus known cost; status quo utility zero",
                      cases=decisions))


if __name__ == "__main__":
    print(json.dumps(results(), indent=2, allow_nan=False))
