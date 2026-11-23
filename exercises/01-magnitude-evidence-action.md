# 01. Magnitude, evidence and action

**Aim:** distinguish a benchmark, an inference about an unknown effect and a choice under uncertainty. Prerequisites: estimates, standard errors and the meaning of a confidence interval.

Read the [economic-significance note](../wiki/concepts/economic-significance.md), [C001: independence](../wiki/claims/C001-independence.md) and sections 1–3 of the [working synthesis](../synthesis/critical-synthesis.md). The [matched 2008 exchange](../wiki/disagreements/2008-exchange.md) supplies the competing positions and locators; do not treat either side as defending an unrestricted slogan.

## Problem and assumptions

**Illustration:** a programme targets the average one-year reduction in the probability of default among eligible borrowers at one hypothetical lender. Write this effect as β, in **percentage points**, with positive values denoting a reduction. Assume an unbiased estimate with known standard error, β̂ ∼ N(β, s²), a valid identification argument for this target population, no selection and no uncertainty beyond the stated likelihood. These are stipulated teaching assumptions, not facts about an actual intervention.

Before examining results, the lender regards effects strictly between −1 and +1 percentage points as negligible for a specified research question. This symmetric margin is an assumption to interrogate, not a default economic standard or a complete adoption rule.

| Case | Estimate β̂ | Known standard error s | Negligible region |
|---|---:|---:|---|
| A: small and precise | 0.1 pp | 0.02 pp | (−1, 1) pp |
| B: large and imprecise | 2 pp | 2 pp | (−1, 1) pp |
| C: above the margin as a point estimate | 1.1 pp | 0.2 pp | (−1, 1) pp |

## Tasks

1. Write three distinct sentences beginning “A reduction would matter if…”, “The evidence supports…” and “The lender should adopt if…”. Identify the additional inputs needed for the third sentence, including costs and consequences of defaults.
2. Compute the two-sided zero-null p-value and 95% confidence interval for each case. Explain the coverage statement without assigning a frequentist probability to the fixed β inside the realised interval.
3. Evaluate: “A rejects zero, so its effect is important”; “B has a large estimate, so it establishes importance”; “C's estimate exceeds 1, so it establishes β > 1.” State exactly which implication fails in each.
4. For C, calculate the one-sided 95% lower confidence bound, β̂ − 1.64485s. Then consider a generic compatible test: if its lower bound L exceeds a positive meaningful threshold δ, must L also exceed zero? Explain why this restricted implication neither requires two separate tests nor establishes a universal testing prerequisite for action.
5. Challenge one stipulation. For example, distinguish a one-year average from long-term effects, or explain how severe losses among a subgroup could make an average-based negligible region inadequate.

From the repository root:

```python
from implementations.normal_model import interval, two_sided_p

for estimate, se in [(0.1, 0.02), (2, 2), (1.1, 0.2)]:
    print(estimate, two_sided_p(estimate, se), interval(estimate, se))
```

**Submit:** a one-page claim map, the calculated table and a 300-word argument distinguishing insufficiency from non-necessity. Include one condition under which your conclusion would change.

<details>
<summary>Self-check and discussion guide</summary>

**Illustration — calculated results:** A has p ≈ 5.73 × 10⁻⁷ and 95% interval [0.0608, 0.1392] pp. B has p ≈ 0.3173 and [−1.9199, 5.9199] pp. C has p ≈ 3.80 × 10⁻⁸ and [0.7080, 1.4920] pp. C's one-sided 95% lower bound is about 0.7710 pp, below the 1 pp threshold.

A rebuts the sufficiency of zero-null rejection for importance under the stipulated margin. It does not rebut necessity. B does not establish a positive effect exceeding 1 pp; negative, negligible and large positive effects remain within its interval. C shows that rejecting zero and comparing the point estimate with δ do not establish the same proposition as a calibrated meaningful-effect test.

The implication L > δ > 0 ⇒ L > 0 is valid within a compatible one-sided procedure at a common error level. Do not silently substitute a two-sided zero-null cutoff. It is an implication between evidential criteria, not a proof that every rational action requires rejection. An exactly observed accounting total can also answer a different, purely descriptive question without sampling extrapolation.

A strong answer specifies what would make 1 pp matter economically, separates the assumed causal target from the observation model, and leaves adoption unresolved until consequences and a decision criterion are supplied. See [C011](../wiki/claims/C011-nested-meaningful-tests.md) and the [checked derivations](../wiki/evidence/mathematical-checks.md).

</details>

[Exercise index](README.md) · [Next: intervals and equivalence](02-intervals-equivalence.md)
