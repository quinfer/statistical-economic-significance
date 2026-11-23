# Worked solution — Decisions under uncertainty

**Illustration: all numbers below belong to the declared synthetic model.** These are mathematical derivations and interpretation checks for [Lab 3](../labs/03-decisions.md), not empirical programme findings or a claim of complete primary-source reading.

## 1. Derive the decision thresholds

For prior `θ∼N(m₀,τ₀²)` and known sampling SE s, the posterior mean is

`m(Y)=wY+(1−w)m₀`, where `w=τ₀²/(τ₀²+s²)`.

Expected adoption payoff is `m(Y)−c`, so the risk-neutral Bayes rule adopts iff

`Y > [c−(1−w)m₀]/w`.

At s=£500, the baseline prior has w=.8: its cutoffs are £125 for cost £100 and £625 for cost £500. The tight prior has w=1/26: corresponding cutoffs are £2600 and £13,000. The plug-in cutoffs equal the costs. The positive significance cutoff is `Φ⁻¹(.975)×500 ≈ £979.98`, independent of cost. The cost-confidence cutoff is `c+Φ⁻¹(.95)×500`, approximately £922.43 or £1322.43 for the two costs.

For the cost-confidence rule, at the boundary θ=c the false-adoption probability is `Pr(Z>Φ⁻¹(.95))=.05`. For θ<c, the required standardised deviation is larger, so the probability is at most .05. This is calibrated control of an evidential error under the model, not a claim that the rule maximises expected welfare. Under a distribution of θ, the proportion of all replications adopting a harmful programme is a different quantity from the conditional error bound at each θ≤c.

At Y=£400, the baseline posterior mean is £320: adopt at cost £100 and retain the status quo at cost £500. The tight-prior mean is approximately £15.38, so it recommends the status quo at either cost. The two-sided zero-null p-value remains approximately .4237. These recommendations follow from stipulated priors, costs and utility; none certifies the population effect as positive or economically important.

The strict `>` tie rule chooses the status quo at exact zero net posterior benefit. Both actions have equal posterior expected utility there, and exact ties have probability zero under the continuous model.

## 2. Exact performance benchmarks

Let the evaluation distribution be `θ∼N(μ,τ²)` and `Y=θ+ε`, with independent `ε∼N(0,s²)`. The evaluation distribution need not equal either policy's assumed prior. Set `v=sqrt(τ²+s²)` and `a=(t−μ)/v` for an adoption threshold t. Then

`Pr(adopt)=Φ(−a)`

and

`E[U]=(μ−c)Φ(−a)+(τ²/v)φ(a)`.

To derive the second term, use `E[θ|Y]=μ+(τ²/v²)(Y−μ)` and `E[(Y−μ)1{Y>t}]=vφ(a)`. At a fixed state, τ=0, so expected utility reduces to `(μ−c)Pr(adopt)`. Always adopts with expected utility μ−c; never has zero expected utility.

The oracle expectation for τ>0 is

`E[max(θ−c,0)]=(μ−c)Φ((μ−c)/τ)+τφ((μ−c)/τ)`;

at a fixed state it is simply `max(μ−c,0)`. Subtract a rule's expected utility to obtain its expected oracle regret. These expressions are implemented independently of the simulation loop in [decisions.py](../decisions.py).

**Calculated analytical benchmarks, pounds per person:**

| Evaluation | Baseline Bayes utility | Positive-significance utility | Plug-in utility | Never utility |
|---|---:|---:|---:|---:|
| Matched prior, cost £100 | 309.053 | 223.972 | 308.964 | 0 |
| Matched prior, cost £500 | 161.171 | 147.823 | 159.188 | 0 |
| Mismatched negative distribution | −74.893 | −2.348 | −79.998 | 0 |
| Fixed θ=0 | −40.129 | −2.500 | −42.074 | 0 |
| Fixed θ=400 | 212.652 | 36.910 | 217.724 | 0 |
| Fixed θ=1200 | 1082.645 | 737.049 | 1084.706 | 0 |

Compare these rounded expectations with the estimates **and MCSEs** in the generated [reference report](../results/summary.md); the full [JSON](../results/reference.json) contains all seven rules, including the cost-confidence comparator, paired differences and exact benchmarks. The simulated mean need not equal its expectation or rank very close rules correctly in one finite run. At matched-prior cost £100, the baseline–plug-in expected utility difference is only about £0.089; reporting a precise ranking from unrelated unpaired standard errors would be misleading.

## 3. Why pairing matters

For replication r, compute `Dᵣ=U_other,r−U_bayes,r` before summarising. Its MCSE is `sd(D)/sqrt(R)`. It includes the covariance induced by shared states and observations. In general it is not `sqrt(MCSE_other²+MCSE_bayes²)`, which assumes independence.

Each regret difference is exactly `−Dᵣ`, because both rules use the same oracle payoff. Their estimated differences therefore have opposite signs and identical MCSEs. Likewise, mean utility plus mean regret must equal mean oracle utility for every rule. Negative individual regret would signal a coding or benchmark error under this two-action model.

Adoption-rate intervals concern repeated independent simulation replications. A nominal 95% Monte Carlo interval is an approximate uncertainty statement about a model performance probability, not a guarantee or an empirical interval for θ. If the tight-prior rule never adopts in a finite run, its observed utility MCSE may be zero even though its analytical expected utility is nonzero. The rate's Wilson interval and the exact benchmark expose that limitation. The tests use an exact utility-variance reference when an unobserved rare tail makes the sample MCSE vanish.

## 4. Optimality and its limits

Under the matching prior and correct likelihood, selecting the action with larger posterior expected utility maximises prior-predictive expected utility. This is a mathematical consequence of pointwise conditional optimisation followed by averaging. It is a useful correctness check; it is not empirical confirmation that the prior or utility is suitable.

The negative-mismatch case reverses comparisons: in this synthetic evaluation distribution, the baseline prior leads to too many costly adoptions, and never acting has greater average utility. The fixed θ=0 case also rewards inaction. At fixed positive θ=400 or 1200, the plug-in rule has greater expected utility than the baseline Bayes rule because it adopts more often when adoption is truly beneficial. A rule's prior-average optimum does not imply dominance at every state. Always adopting knows neither the state nor its sign; its success at a favourable fixed state is not a general prescription.

At cost £100, baseline Bayes adoption can occur for `125<Y≤979.98`, without rejection of the two-sided zero null. The report records this joint event as a fraction of **all replications**, not as a conditional fraction of adoptions. That frequency describes a rule under the DGP. It does not prove a nonzero, large or causal population effect.

The positive-significance rule is one explicit cost-blind comparator. The cost-confidence rule supplies a cost-aware frequentist alternative with a stated false-adoption guarantee, although that guarantee may sacrifice beneficial adoptions and does not solve expected-utility optimisation. Defending calibrated inference does not commit a statistician to the cost-blind rule. Conversely, replacing either with a prior-dependent rule does not remove the need to defend identification, calibration, costs and preferences. Comparing their average utilities evaluates them under this lab's welfare criterion; it does not show that their distinct objectives are interchangeable.

## Reference-run paired comparisons

**Computed illustration:** base seed 20261123, 50,000 replications per scenario. Utilities are pounds per person over one year. These Monte Carlo values differ from the exact expectations above.

| Evaluation | Baseline Bayes mean utility (MCSE) | Plug-in minus Bayes mean utility (paired MCSE) |
|---|---:|---:|
| `matched_prior_cost100` | 303.403 (2.547) | -0.299 (0.191) |
| `matched_prior_cost500` | 159.897 (1.901) | -2.601 (0.415) |
| `mismatched_prior_negative` | -74.705 (0.647) | -5.209 (0.193) |
| `fixed_zero` | -40.058 (0.219) | -1.916 (0.061) |
| `fixed_moderate_benefit` | 212.220 (0.610) | 5.400 (0.178) |
| `fixed_large_benefit` | 1082.224 (0.620) | 2.112 (0.215) |

At matched-prior cost £100, the paired difference is small relative to its simulation error. Its finite-run estimate does not overturn the analytical ordering. At fixed positive states the sign reverses, as predicted. The full JSON includes cost-confidence, tight-prior, always/never and cost-blind significance rules; report their separate objectives before treating a utility ranking as a methodological verdict.

## 5. Replication and extension answers

A fresh seed changes Monte Carlo estimates while leaving analytic expectations fixed. Increasing from 10,000 to 50,000 replications typically reduces mean MCSE by about `sqrt(5)`, subject to realised variance and rare-event counts. It does not add data on an actual programme, validate a prior, fix an incorrect sampling model or choose a legitimate welfare function.

For uncertain cost C, expected adoption payoff becomes `E[θ−C|data]` under linear utility; joint modelling is needed when costs and benefits share information. An asymmetric downside penalty could instead use `U(1,θ)=θ−c−k max(c−θ,0)` with k>0. The former baseline Bayes cutoff no longer automatically solves the latter problem. State k's interpretation and stakeholder justification, derive the posterior expected penalty, and only then compare rules under a consistently revised oracle and evaluation criterion.

**Source limits remain unchanged.** Consult the [lab's source boundary](../labs/03-decisions.md#evidence-boundaries): Manski 2019 is a selected-passage reading, Manski 2021 and Kandel–Stambaugh are abstract-only, and Wald is metadata-only. This solution neither replicates those works nor claims to prove a universal ranking of inferential approaches. The [slide gate](../../reviews/review-gate.md) is closed.

[Lab questions](../labs/03-decisions.md) · [Simulation index](../README.md)
