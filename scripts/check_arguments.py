#!/usr/bin/env python3
"""Deterministic mathematical illustrations, not simulations or empirical findings.

Uses known-variance normal models, fixed margins and a specified normal prior.
No random draws: there is no seed or Monte Carlo error. Output is generated for
source-criticism and the synthesis; it is not a training deck.
"""
import json
import math
from pathlib import Path
from statistics import NormalDist

N = NormalDist()
ALPHA = .05
Z = N.inv_cdf(1 - ALPHA / 2)

def power(noncentrality):
    return N.cdf(-Z - noncentrality) + 1 - N.cdf(Z - noncentrality)

def case(estimate, se, margin):
    ci95 = [estimate - Z * se, estimate + Z * se]
    q = N.inv_cdf(1 - ALPHA)
    ci90 = [estimate - q * se, estimate + q * se]
    return dict(estimate=estimate, se=se, margin=margin,
                p_zero_two_sided=2*N.cdf(-abs(estimate/se)),
                ci95=ci95, ci90=ci90,
                equivalent_tost_05=ci90[0]>-margin and ci90[1]<margin,
                positive_beyond_margin_onesided_05=ci90[0]>margin)

cases = {
    'small_precise': case(.1, .02, 1),
    'large_imprecise': case(2, 2, 1),
    'precise_zero': case(0, .001, .01),
    # A two-sided .05 zero-null test rejects, but the meaningful-margin test fails.
    'positive_but_not_established_above_margin': case(1.1, .2, 1),
}
# Data: unbiased normal estimate in pounds per person, known se; proper prior.
x, se, prior_mean, prior_sd = 400., 500., 0., 1000.
post_var = 1/(1/prior_sd**2+1/se**2)
post_mean = post_var*(prior_mean/prior_sd**2+x/se**2)
decision = dict(estimate=x,se=se,prior_mean=prior_mean,prior_sd=prior_sd,
    posterior_mean=post_mean,posterior_sd=math.sqrt(post_var),
    p_zero_two_sided=2*N.cdf(-abs(x/se)),
    expected_net_at_cost_100=post_mean-100,
    expected_net_at_cost_500=post_mean-500)
# An equivalence failure can be frequent when the true effect is exactly zero.
# For known se=1 and margin=.1, the 90% CI cannot fit within [-.1,.1]
# for ANY observed estimate. ETFR is therefore 1, but no zero-null is false.
equivalence_counterexample = dict(theta=0,se=1,margin=.1,
    ci90_halfwidth=N.inv_cdf(.95),equivalence_failure_probability=1.)
assert math.isclose(power(0), .05, abs_tol=1e-12)
assert cases['small_precise']['p_zero_two_sided'] < .05
assert cases['small_precise']['equivalent_tost_05']
assert cases['precise_zero']['p_zero_two_sided'] == 1
assert cases['precise_zero']['equivalent_tost_05']
assert cases['large_imprecise']['ci95'][0] < 0 < cases['large_imprecise']['ci95'][1]
assert not cases['positive_but_not_established_above_margin']['positive_beyond_margin_onesided_05']
assert decision['p_zero_two_sided'] > .05
assert decision['expected_net_at_cost_100'] > 0 > decision['expected_net_at_cost_500']
assert equivalence_counterexample['ci90_halfwidth'] > equivalence_counterexample['margin']
output = dict(label='Synthetic deterministic illustrations; no empirical observations',
    assumptions='Known-variance normal likelihood; fixed thresholds; decision example uses stated proper prior and linear risk-neutral utility; no selection or identification failure',
    alpha=ALPHA,normal_critical_value=Z,
    power_by_noncentrality={str(d):power(d) for d in [1,.1,.01,0]},
    cases=cases,decision=decision,equivalence_counterexample=equivalence_counterexample)
target=Path(__file__).resolve().parents[1]/'synthesis/analytical-checks.json'
target.write_text(json.dumps(output,indent=2)+'\n')
print(f'PASS: analytical boundary checks; wrote {target.relative_to(target.parents[1])}')
