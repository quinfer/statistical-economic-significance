# 05. From gross alpha to an economic claim

An investment committee sees a gross alpha estimate of 20 basis points a month. A member asks whether the portfolio could earn enough after costs. Work through that question with two levels of precision, then check what happens when the factor model may be biased. This exercise builds on exercises 01–03.

Start with the chapter’s gross-to-net illustration and return to it when you assess whether two analyses answer the same question. [§4, Comparing analyses of the same data](../synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data) · [Finance](../wiki/concepts/finance.md) · [Identification](../wiki/concepts/identification.md) · [Claim C008](../wiki/claims/C008-finance-replication.md) · [Claim C009](../wiki/claims/C009-identification.md)

## Problem and assumptions

**Illustration:** a fixed, prespecified hypothetical portfolio has estimated **monthly gross factor-model alpha of 20 basis points**, with known normal standard error 15 bp. One basis point is 0.01 percentage points. The estimand α is the population intercept for that portfolio under the specified factor model and target trading regime, measured before implementation costs. Treat the model and its sampling approximation as valid initially; no factor search, portfolio selection, look-ahead bias or dependence misspecification is included in this baseline.

Implementation cost c is a known constant per month at the assumed scale: consider c = 10 bp and c = 25 bp. Net alpha is α − c. For this exercise costs enter additively, have no uncertainty and do not change the portfolio. There are no claims about an actual strategy, future returns or anyone's optimal portfolio. Investor welfare is not identified by an alpha alone.

## Tasks

1. **Translate gross to net.** Calculate the point estimates and 95% intervals for gross alpha and for net alpha at both costs. Show what subtracting a known constant does to the centre, endpoints and standard error. Compare the three p-values against zero, naming the target in each test.
2. **Hold costs and the estimate fixed.** Set SE = 2 bp and recalculate. Which evidence claims change? Explain how stronger evidence of positive gross alpha can coexist with evidence of negative net alpha at the higher cost.
3. **Allow cost to be estimated.** Write the variance of α̂ − ĉ and identify the information you would need about both estimates and their covariance.
4. **Allow for a biased model.** At SE = 2 bp and c = 10 bp, let the estimate target α + b, with fixed unknown b ∈ [0, 10] bp. Construct the union of conditional 95% intervals for net α − c. Explain what the union tells the committee and what you would need to assign posterior probabilities to values of b.
5. **Name the decision target.** Explain what would link a factor-model intercept to the causal effect of deploying a portfolio, to a payoff at a specified capacity, or to a gain in investor utility. Identify a design or measurement problem that could persist with arbitrarily many observations.
6. **Compare the studies’ questions.** Before treating a more optimistic replication result and a stronger discovery hurdle as contradictory, check the samples, targets and definitions of success you can establish from the notes. Attribute claims at the recorded reading depths. [Harvey, Liu and Zhu](../wiki/papers/harvey-liu-zhu-2016-cross-section.md) · [McLean and Pontiff](../wiki/papers/mclean-pontiff-2016-predictability.md) · [Jensen, Kelly and Pedersen](../wiki/papers/jensen-kelly-pedersen-2023-replication.md)

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
<summary>Worked solution and discussion</summary>

**Illustration.** Subtract the known cost from the gross estimate and both interval endpoints. The interval keeps the same width because the offset is constant across repeated samples. Retest against zero for the resulting target. All returns, costs, standard errors and intervals in the table are basis points per month.

| SE | Target | Estimate | 95% interval | Two-sided p-value against zero |
|---:|---|---:|---|---:|
| 15 | Gross | 20 | [−9.40, 49.40] | 0.1824 |
| 15 | Net, c = 10 | 10 | [−19.40, 39.40] | 0.5050 |
| 15 | Net, c = 25 | −5 | [−34.40, 24.40] | 0.7389 |
| 2 | Gross | 20 | [16.08, 23.92] | 1.52 × 10⁻²³ |
| 2 | Net, c = 10 | 10 | [6.08, 13.92] | 5.73 × 10⁻⁷ |
| 2 | Net, c = 25 | −5 | [−8.92, −1.08] | 0.0124 |

At SE = 15, the net intervals leave room for gains and losses. Equivalence would require a justified margin and evidence relative to it. At SE = 2, gross alpha is precisely estimated above zero and net alpha at c = 25 is precisely estimated below it. The two results concern different targets. [§4, Gross-to-net illustration](../synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data)

For an estimated cost, Var(α̂ − ĉ) = Var(α̂) + Var(ĉ) − 2Cov(α̂, ĉ). To use this, justify the covariance and determine what assumptions support inference about the difference. In task 4, subtract b from each endpoint to get [6.08 − b, 13.92 − b]. Across the allowed range, the lowest lower endpoint occurs at b = 10 and the highest upper endpoint at b = 0. The union is about [−3.92, 13.92] bp. It contains the conditional interval at the true b if that value is inside the stipulated range, giving conservative coverage under the stated model. The bound on b is a sensitivity assumption. A posterior would need a probability model for b.

For the committee, name the model and what its intercept measures. Explain which design assumptions, trading costs and capacity information would support a recommendation, even with a very small sampling error. When comparing the papers, distinguish search and multiplicity from out-of-sample or publication-related changes. Then check which replication designs and targets bear on the decision you are considering. [Finance evidence trails](../wiki/concepts/finance.md) · [§6, What would change the conclusion?](../synthesis/critical-synthesis.md#6-what-would-change-the-conclusion)

</details>

[Exercise index](README.md) · [Next: decision memo](06-decision-memo.md)
