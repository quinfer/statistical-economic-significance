# 06. A decision before certainty

A committee asks whether to adopt a programme after seeing an uncertain estimate of its benefits. Write the recommendation you could make under an explicit decision rule and explain what would change it. Bring your work from exercises 01–05 and basic conditional probability.

The chapter builds the same decision problem in §5. Use §3 for the objections you will address in your memo. The numerical example is a project illustration. Manski’s treatment-choice argument supplies background for the distinction between a decision and a test. [§5, Action under uncertainty](../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty) · [§3, Competing arguments](../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) · [Decision concepts](../wiki/concepts/decisions.md) · [Claim C002](../wiki/claims/C002-action-without-rejection.md) · [Claim C010](../wiki/claims/C010-uncertainty-and-choice.md) · [Manski 2019](../wiki/papers/manski-2019-treatment-choice.md)

## Problem and assumptions

**Illustration:** a hypothetical programme's unknown average gross benefit β is measured in **pounds per eligible person over one year** in a fixed target population. The unbiased estimate is £400 with known normal standard error £500: β̂ ∼ N(β, 500²). Assume valid identification, no selection or extrapolation failure, and a proper prior β ∼ N(0, 1000²).

Choose once between adoption and a status quo with zero payoff. Adoption payoff per person is β − c, with known cost c. The baseline criterion maximises posterior expected payoff using linear risk-neutral utility. There are no distributional weights, capacity constraints, option to delay, future learning or uncertain costs. These exclusions are modelling assumptions, not recommendations to ignore such issues in practice.

For prior mean m₀ and prior variance v₀, posterior variance is

`v₁ = 1 / (1/v₀ + 1/s²)`,

and posterior mean is

`m₁ = v₁ × (m₀/v₀ + β̂/s²)`.

## Tasks

1. **Make a baseline recommendation.** At c = £100, calculate the posterior mean and standard deviation, the two-sided frequentist p-value against zero and the posterior expected net benefit. State the action under the baseline criterion and the evidential claim the data support.
2. **Change only cost.** Keep the likelihood and prior fixed and set c = £500. Identify the quantities that change and explain why the decision can reverse with the zero-null p-value held fixed.
3. **Change only the prior at the original cost.** Return to c = £100 and use the proper prior N(0, 100²). Recalculate. Give the strongest substantive defence of each prior and explain what would make one more credible to the committee before comparing recommendations.
4. **Compare decision criteria.** At c = £100 calculate Pr(β > c | data) under both priors. Compare the expected-net-benefit rule with a rule that requires this probability to exceed .95. Explain what each criterion values and what would justify using it.
5. **Penalise shortfalls.** Consider `β − c − k × max(c − β, 0)`, with k > 0. Explain how charging extra for outcomes below break-even changes the comparison. As an extension, derive the expected penalty. A change in the recommended action would now reflect a change in the payoff.
6. **Write for the committee.** Include one strong inferential objection and one strong contextual objection. State what further evidence or stakeholder judgement would change your recommendation and which uncertainty could persist with more observations.

```python
from implementations.normal_model import normal_cdf, normal_posterior, two_sided_p

print("Zero-null p-value:", two_sided_p(400, 500))
for prior_sd in [1000, 100]:
    mean, sd = normal_posterior(400, 500, prior_mean=0, prior_sd=prior_sd)
    probability_positive_net = normal_cdf((mean - 100) / sd)
    print(prior_sd, mean, sd, mean - 100, probability_positive_net)
```

## Memo and assessment

**Submit:** a 700-word memo and a reproducible calculation table. Address a hypothetical committee with responsibility for the stated target population. Lead with a conditional recommendation, then explain the economic criterion, evidence, prior/loss sensitivity, distributional omissions and what would reverse the recommendation. Separate the scientific report another decision-maker could reuse from the committee's own preferences. Label all numerical claims **Illustration**.

Use this rubric for self-assessment or peer discussion. Score each dimension 0 (missing or materially wrong), 1 (partly defensible) or 2 (clear and defensible); a high total cannot excuse a false citation or conflation of the action with proof of the effect.

| Dimension | Full-credit requirement |
|---|---|
| Target and units | Population, horizon, gross benefit, cost and status quo are explicit |
| Uncertainty | Likelihood, identification assumptions, prior and posterior are distinguished |
| Arithmetic | Posterior, expected net benefit and sensitivity results are reproducible |
| Decision criterion | Action follows from stated consequences/preferences, with alternatives acknowledged |
| Inferential discipline | No non-rejection-as-zero claim, and no recommendation-as-proof claim |
| Critical balance | Strong objections, source-reading limits and evidence that could change the judgement are recorded |

<details>
<summary>Worked solution and memo guidance</summary>

**Illustration.** With the baseline prior, combine its precision with the likelihood precision using the two formulas in the setup. The posterior mean is £320 and the posterior standard deviation is about £447.21. The two-sided p-value against zero is about .4237, calculated from the estimate and its sampling standard error. Under linear utility the expected adoption payoff is the posterior mean minus cost. Compare that payoff with zero for the status quo.

| Prior SD | Cost | Posterior expected net benefit | Choice under linear utility |
|---:|---:|---:|---|
| £1,000 | £100 | £220 | Adopt |
| £1,000 | £500 | −£180 | Keep the status quo |
| £100 | £100 | −£84.62 | Keep the status quo |

The tighter prior brings the posterior mean to approximately £15.38 and the posterior standard deviation to £98.06. The likelihood and its p-value stay fixed. At £100 use each posterior to find the area above break-even. The probabilities are about .6886 for the wider prior and .1941 for the tighter prior. Both fall below .95. A probability rule counts how often net benefit is positive under the posterior, while an expected-payoff rule also weights the sizes of gains and losses. Defend the criterion as well as the prior. [§5, Action under uncertainty](../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty)

For the optional asymmetric-loss extension, let μ and σ be the posterior mean and standard deviation, d = (c − μ)/σ, and φ/Φ the standard normal density/distribution functions. Expected shortfall below break-even is `(c − μ)Φ(d) + σφ(d)`. Expected adoption payoff becomes `μ − c − k × expected_shortfall`. This formula makes the additional penalty explicit. It should not be mistaken for a universal welfare function or an empirical estimate of stakeholder preferences.

**Project interpretation.** For your memo, give the committee a conditional recommendation and state where it relies on the prior, costs, loss and causal assumptions. The baseline adoption case demonstrates how a choice can be justified under stated conditions without rejecting zero. To establish the population effect as important you would need evidence about its magnitude relative to a benchmark. The chapter’s nested-test argument describes a narrower evidential criterion that entails zero-null rejection. [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Claim C011](../wiki/claims/C011-nested-meaningful-tests.md)

</details>

[Exercise index](README.md) · [Return to the critical synthesis](../synthesis/critical-synthesis.md) · [Review gate](../reviews/review-gate.md)
