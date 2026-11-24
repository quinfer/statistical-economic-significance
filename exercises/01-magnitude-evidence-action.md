# 01. Magnitude, evidence and action

You are reviewing three estimates for a lender. One is small and precise, one is large and imprecise, and one falls just above the lender’s benchmark. Before running a test, write down what you would need to know to recommend adoption. You’ll use estimates, standard errors and confidence intervals to separate that decision from what each study establishes.

Use the chapter’s distinctions in [§1, Which claim are you trying to establish?](../synthesis/critical-synthesis.md#1-which-claim-are-you-trying-to-establish) and [§2, What do the data tell you about the benchmark?](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark). If you draw on the debate, check each side’s concessions and the passages cited. [§3, Competing arguments](../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) · [Economic significance](../wiki/concepts/economic-significance.md) · [Claim C001](../wiki/claims/C001-independence.md) · [Matched 2008 exchange](../wiki/disagreements/2008-exchange.md)

## Problem and assumptions

**Illustration:** a programme targets the average one-year reduction in the probability of default among eligible borrowers at one hypothetical lender. Write this effect as β, in **percentage points**, with positive values denoting a reduction. Assume an unbiased estimate with known standard error, β̂ ∼ N(β, s²), a valid identification argument for this target population, no selection and no uncertainty beyond the stated likelihood. These are stipulated teaching assumptions, not facts about an actual intervention.

Before examining results, the lender regards effects strictly between −1 and +1 percentage points as negligible for a specified research question. This symmetric margin is an assumption to interrogate, not a default economic standard or a complete adoption rule.

| Case | Estimate β̂ | Known standard error s | Negligible region |
|---|---:|---:|---|
| A: small and precise | 0.1 pp | 0.02 pp | (−1, 1) pp |
| B: large and imprecise | 2 pp | 2 pp | (−1, 1) pp |
| C: above the margin as a point estimate | 1.1 pp | 0.2 pp | (−1, 1) pp |

## Tasks

1. **Write the four claims.** Begin “A reduction would matter if…”, “The records show…”, “The evidence supports…” and “The lender should adopt if…”. For the second sentence, name something the lender could tally directly from complete records, such as the number of defaults last year. State what you would need to check about those records. For the last sentence, list the costs and consequences of adoption, including the consequences of defaults.
2. **Calculate, then interpret.** Find the two-sided zero-null p-value and 95% confidence interval for each case. Explain 95% coverage by describing what would happen if you repeated the study with β held fixed.
3. **Check three proposed interpretations.** A colleague says A’s effect is important because it rejects zero, B establishes importance because the estimate is large, and C establishes β > 1 because its estimate exceeds 1. For each claim, identify the step that needs more evidence.
4. **Check the narrower implication.** For C, calculate the one-sided 95% lower confidence bound, β̂ − 1.64485s. In a compatible procedure, if the lower bound L exceeds a positive threshold δ, what follows about L relative to zero? Explain why the same bound is enough for the two comparisons and why an adoption decision raises a further question.
5. **Challenge one stipulation.** Say what would change if the lender cared about long-term effects, or if severe losses among a subgroup made the average-based negligible region inappropriate.

From the repository root:

```python
from implementations.normal_model import interval, two_sided_p

for estimate, se in [(0.1, 0.02), (2, 2), (1.1, 0.2)]:
    print(estimate, two_sided_p(estimate, se), interval(estimate, se))
```

**Submit:** a one-page claim map, the calculated table and a 300-word argument distinguishing insufficiency from non-necessity. Include one condition under which your conclusion would change.

<details>
<summary>Worked solution and discussion</summary>

**Illustration.** Divide each estimate by its standard error for the two-sided normal test. For the 95% interval, go 1.96 standard errors either side of the estimate. Under the model, 95% of intervals constructed this way over repeated samples would cover the fixed target effect.

| Case | Two-sided p-value against zero | 95% interval (pp) | What you can say about the benchmark |
|---|---:|---|---|
| A | 5.73 × 10⁻⁷ | [0.0608, 0.1392] | The interval excludes zero and lies inside the negligible region. Zero-null rejection is insufficient to establish importance. |
| B | 0.3173 | [−1.9199, 5.9199] | The range includes negative, negligible and large positive effects. The point estimate is above the benchmark and the interval crosses it. |
| C | 3.80 × 10⁻⁸ | [0.7080, 1.4920] | The two-sided zero test rejects and the point estimate clears the threshold. C’s one-sided 95% lower bound is about 0.7710 pp, below the 1 pp threshold. |

Case A tells you about sufficiency. To assess necessity for a specific evidence standard, consider L > δ > 0. This implies L > 0 at the same error level within the compatible one-sided procedure. Keep the tail fixed when making that comparison. If the question instead asks about an exactly observed accounting total, you may be able to answer it descriptively without sampling extrapolation. [§2, Benchmark and nested tests](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark)

A reduction of one percentage point would matter if its consequences at the lender’s scale justify that benchmark. The lender could describe last year’s number of defaults after checking which borrowers the records cover and how defaults were defined. The evidence in A supports a positive but negligible reduction under the stipulated margin. The lender should adopt if expected benefits exceed implementation costs under a defensible decision criterion. To justify that last sentence, say how much averting defaults is worth, whose losses count and what risks the lender faces. A different horizon or borrower mix can require an argument for a different causal target. [§1, The four claims](../synthesis/critical-synthesis.md#1-which-claim-are-you-trying-to-establish) · [§5, Action under uncertainty](../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty) · [Claim C011](../wiki/claims/C011-nested-meaningful-tests.md) · [Checked derivations](../wiki/evidence/mathematical-checks.md)

</details>

[Exercise index](README.md) · [Next: intervals and equivalence](02-intervals-equivalence.md)
