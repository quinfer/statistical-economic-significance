# 06. A decision before certainty

**Aim:** give a defensible recommendation under explicit uncertainty and preferences while keeping it separate from a claim that an economically important effect has been established. Prerequisites: exercises 01–05 and basic conditional probability.

Read [decisions under uncertainty](../wiki/concepts/decisions.md), [C002](../wiki/claims/C002-action-without-rejection.md), [C010](../wiki/claims/C010-uncertainty-and-choice.md) and section 5 of the [working synthesis](../synthesis/critical-synthesis.md). The [Manski 2019 note](../wiki/papers/manski-2019-treatment-choice.md) supplies a source trail for the distinction between treatment choice and testing; this exercise is the project's own normal-prior illustration, not a replication of that paper.

## Problem and assumptions

**Illustration:** a hypothetical programme's unknown average gross benefit β is measured in **pounds per eligible person over one year** in a fixed target population. The unbiased estimate is £400 with known normal standard error £500: β̂ ∼ N(β, 500²). Assume valid identification, no selection or extrapolation failure, and a proper prior β ∼ N(0, 1000²).

Choose once between adoption and a status quo with zero payoff. Adoption payoff per person is β − c, with known cost c. The baseline criterion maximises posterior expected payoff using linear risk-neutral utility. There are no distributional weights, capacity constraints, option to delay, future learning or uncertain costs. These exclusions are modelling assumptions, not recommendations to ignore such issues in practice.

For prior mean m₀ and prior variance v₀, posterior variance is

`v₁ = 1 / (1/v₀ + 1/s²)`,

and posterior mean is

`m₁ = v₁ × (m₀/v₀ + β̂/s²)`.

## Tasks

1. Calculate the posterior mean and standard deviation, the frequentist two-sided zero-null p-value and the posterior expected net benefit at c = £100. State the preferred action under the baseline criterion. What proposition has this calculation established, and what has it not established?
2. Keep the same likelihood and prior but set c = £500. Explain why the preferred action can change although the zero-null p-value does not.
3. Return to c = £100 and replace the prior by N(0, 100²), keeping it proper. Recalculate. Present the strongest substantive justification that a decision-maker would need for each prior, and explain why selecting a prior to obtain a preferred recommendation is unpersuasive.
4. For both priors at c = £100, compute Pr(β > c | data). Compare maximising expected net benefit with a separate rule requiring this probability to exceed .95. Why do these criteria differ? Do not label either rule uniquely rational without an objective that justifies it.
5. Consider an alternative payoff `β − c − k × max(c − β, 0)`, with k > 0: shortfalls below break-even receive an extra penalty. Explain how this changes the decision problem. You may derive the expectation as an extension, but a different decision under a changed payoff does not contradict the baseline calculation.
6. Write the decision memo below. Include one objection from the strongest inferential position and one from the strongest contextualist position. Say what further evidence or stakeholder judgement could change your recommendation, and which uncertainty more data might fail to resolve.

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
<summary>Self-check and discussion guide</summary>

**Illustration — calculated results:** the baseline posterior mean is £320 and standard deviation approximately £447.21. The frequentist two-sided p-value is approximately .4237. At c = £100, expected net benefit is £220, so baseline expected payoff favours adoption. At c = £500, expected net benefit is −£180, so it favours the status quo. Neither action proves the true effect is positive, negligible or economically large.

With prior standard deviation £100, posterior mean is approximately £15.38 and standard deviation £98.06. Expected net benefit at c = £100 becomes −£84.62, favouring the status quo. The likelihood and its zero-null p-value are unchanged. Under the wider and tighter priors, posterior probabilities of positive net benefit are approximately .6886 and .1941 respectively. A .95 probability rule favours neither adoption case; it is a different criterion, and the fixed threshold requires justification.

For the optional asymmetric-loss extension, let μ and σ be the posterior mean and standard deviation, d = (c − μ)/σ, and φ/Φ the standard normal density/distribution functions. Expected shortfall below break-even is `(c − μ)Φ(d) + σφ(d)`. Expected adoption payoff becomes `μ − c − k × expected_shortfall`. This formula makes the additional penalty explicit. It should not be mistaken for a universal welfare function or an empirical estimate of stakeholder preferences.

**Project interpretation:** the example refutes a universal requirement to reject zero before acting under every defensible criterion. It does not refute the need for reliable evidence about unknown effects. “Adopt under these assumptions” and “the population effect is established as important” remain distinct. A good memo also recognises that a prior, loss function and causal target can be disputed even when all arithmetic is correct. [C011](../wiki/claims/C011-nested-meaningful-tests.md) preserves the narrower case in which a meaningful-effect evidential criterion logically entails rejection of zero.

</details>

[Exercise index](README.md) · [Return to the critical synthesis](../synthesis/critical-synthesis.md) · [Review gate](../reviews/review-gate.md)
