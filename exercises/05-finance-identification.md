# 05. From gross alpha to an economic claim

**Aim:** identify the estimand, units, costs and assumptions between an estimated return and a claim about economic value. Prerequisites: exercises 01–03.

Read [finance](../wiki/concepts/finance.md), [identification](../wiki/concepts/identification.md), [C008: finance replication](../wiki/claims/C008-finance-replication.md) and [C009](../wiki/claims/C009-identification.md). For the discussion task, use the existing notes on [Harvey–Liu–Zhu](../wiki/papers/harvey-liu-zhu-2016-cross-section.md), [McLean–Pontiff](../wiki/papers/mclean-pontiff-2016-predictability.md) and [Jensen–Kelly–Pedersen](../wiki/papers/jensen-kelly-pedersen-2023-replication.md), preserving their stated reading depths.

## Problem and assumptions

**Illustration:** a fixed, prespecified hypothetical portfolio has estimated **monthly gross factor-model alpha of 20 basis points**, with known normal standard error 15 bp. One basis point is 0.01 percentage points. The estimand α is the population intercept for that portfolio under the specified factor model and target trading regime, measured before implementation costs. Treat the model and its sampling approximation as valid initially; no factor search, portfolio selection, look-ahead bias or dependence misspecification is included in this baseline.

Implementation cost c is a known constant per month at the assumed scale: consider c = 10 bp and c = 25 bp. Net alpha is α − c. For this exercise costs enter additively, have no uncertainty and do not change the portfolio. There are no claims about an actual strategy, future returns or anyone's optimal portfolio. Investor welfare is not identified by an alpha alone.

## Tasks

1. Calculate gross and net point estimates and 95% confidence intervals for both cost cases. Derive why subtracting a known constant shifts the interval without changing its standard error. Compare the gross zero-null p-value with the two net zero-null p-values.
2. Repeat with SE = 2 bp and the same estimate/costs. Which evidence claims change? Explain why stronger gross significance can coexist with evidence of negative net alpha at a high cost.
3. Suppose cost were estimated rather than known. Write the variance of α̂ − ĉ, including covariance, and state what information is missing. Do not add standard errors or assume independence without justification.
4. Under the precise SE = 2 case and c = 10, introduce a model-bias sensitivity parameter b ∈ [0, 10] bp, fixed but unknown: α̂ estimates α + b. Construct the union of conditional 95% intervals for net α − c over this range. Explain why reducing sampling error alone has not removed the economic ambiguity, and distinguish this sensitivity interval from a posterior distribution over b.
5. Write one paragraph explaining why a factor-model intercept is not automatically a causal effect of deploying the portfolio, a capacity-adjusted payoff or an investor's utility gain. Identify a plausible design or measurement issue that would remain with arbitrarily many observations.
6. Compare the research questions and settings represented by the three finance paper notes. List what would have to match before you could treat a more optimistic replication result and a stronger discovery hurdle as direct empirical contradictions. Do not import findings from unread sections or infer an implementable trading strategy.

```python
from implementations.normal_model import interval, two_sided_p

for se in [15, 2]:
    for cost in [0, 10, 25]:
        net_estimate = 20 - cost
        print(se, cost, net_estimate,
              interval(net_estimate, se), two_sided_p(net_estimate, se))
```

**Submit:** a gross/net results table and a 500-word interpretation stating the target, factor model's role, horizon, scale, cost assumptions, uncertainty and missing decision inputs. Include an explicit sensitivity result and one evidence-based comparison of the paper notes.

<details>
<summary>Self-check and discussion guide</summary>

**Illustration — calculated results:** at SE = 15 bp the gross interval is [−9.40, 49.40] bp, with p ≈ .1824. At c = 10, net estimate is 10 bp, interval [−19.40, 39.40], p ≈ .5050. At c = 25, net estimate is −5 bp, interval [−34.40, 24.40], p ≈ .7389. None establishes zero net benefit or equivalence to zero.

At SE = 2 bp the gross interval is [16.08, 23.92]; the c = 10 net interval is [6.08, 13.92]; the c = 25 interval is [−8.92, −1.08] bp. Positive gross alpha and negative net alpha can both be precisely estimated. The relevant null and decision consequences have changed.

For an estimated cost, Var(α̂ − ĉ) = Var(α̂) + Var(ĉ) − 2Cov(α̂, ĉ). This expression alone does not establish the joint distribution or solve estimation bias. In task 4, the conditional net interval is [6.08 − b, 13.92 − b]; its union is approximately [−3.92, 13.92] bp. The sensitivity bound is assumed, not estimated or probabilistically weighted. With the stated normal model and true b inside the allowed set, taking this union is conservative for coverage; it is not an exact 95% probability statement about the realised interval or the bias.

Precision conditional on a factor model does not justify that model, recover an omitted trading cost or establish external validity at another scale. A strong discussion separates search/multiplicity, out-of-sample changes, publication-related changes, replication design and investor preferences. Use the [finance evidence trails](../wiki/concepts/finance.md) for attribution and the [synthesis](../synthesis/critical-synthesis.md) for the project's conditional interpretation.

</details>

[Exercise index](README.md) · [Next: decision memo](06-decision-memo.md)
