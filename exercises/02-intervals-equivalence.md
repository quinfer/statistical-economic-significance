# 02. Intervals and equivalence

When could you tell the lender that an effect is small enough to ignore? Start from your claim map in [exercise 01](01-magnitude-evidence-action.md). Here you will decide what each interval supports about zero and about an economically negligible range.

Read the chapter’s examples before comparing the four studies. Return to its discussion of margins when you change the research question in task 3. [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [§4, Setting a margin worth testing](../synthesis/critical-synthesis.md#setting-a-margin-worth-testing) · [Intervals](../wiki/concepts/intervals.md) · [Equivalence](../wiki/concepts/equivalence.md) · [Lakens 2017 and reading limits](../wiki/papers/lakens-2017-equivalence.md) · [Claim C003](../wiki/claims/C003-equivalence.md)

## Problem and assumptions

**Illustration:** use the same hypothetical borrower population and one-year default-reduction estimand as exercise 01, measured in percentage points. Assume β̂ ∼ N(β, s²), known s, no selection or identification failure, and fixed negligible bounds (−δ, δ). Each row is a separate prespecified research question; the margins are not chosen after seeing its result. Use α = .05 throughout.

| Case | β̂ (pp) | s (pp) | δ (pp) |
|---|---:|---:|---:|
| A | 0.1 | 0.02 | 1 |
| B | 2 | 2 | 1 |
| C | 0 | 0.001 | 0.01 |
| D | 1.1 | 0.2 | 1 |

A and B carry over from Exercise 1. Its case C, the 1.1 pp estimate, is case D here. This exercise uses C for the precise zero estimate added to complete the four possible test outcomes.

For two one-sided tests (TOST), test both H₀L: β ≤ −δ and H₀U: β ≥ δ. Declare equivalence only if both reject at .05. The compatible normal 90% interval must lie strictly inside the fixed bounds. This is a repeated-sampling procedure, not a posterior probability that β lies within the bounds.

## Tasks

1. **Make two predictions for each case.** Does the study reject zero? Does it establish equivalence at the stated margin? Then compute each zero-null p-value, 95% interval, 90% interval and TOST p-value. Classify all four combinations and explain which hypothesis each test addresses.
2. **Compare B with C.** Which study supports negligibility, and how can C be informative with a zero-null p-value of exactly one? Point to the relevant interval and margin in each case.
3. **Change the question.** For A, set δ = 0.05 pp and recalculate. Explain what you are now asking the study to establish. What would change about the inference if you selected that margin after inspecting the estimates?
4. **Check what the design allows.** Set the true β = 0, s = 1 pp and δ = 0.1 pp. Show that the 90% interval is too wide to fit inside the bounds for any estimate. What would a 100% equivalence failure rate mean in this example?
5. **Compare with break-even.** Value each percentage-point reduction at V > 0 pounds per borrower and set the fixed adoption cost at c pounds per borrower over the same horizon. With linear benefits, the positive net-benefit threshold is β > c/V. Explain whether ruling out positive viability would require ruling out a large harmful effect.

```python
from implementations.normal_model import interval, tost_p, two_sided_p

for estimate, se, margin in [(0.1, 0.02, 1), (2, 2, 1),
                             (0, 0.001, 0.01), (1.1, 0.2, 1)]:
    print(estimate, two_sided_p(estimate, se),
          interval(estimate, se), interval(estimate, se, level=0.90),
          tost_p(estimate, se, margin))
```

**Submit:** the results table and a 400-word report. Include a substantive justification you would require before using a real margin and a sensitivity analysis that does not conceal the originally specified question.

<details>
<summary>Worked solution and discussion</summary>

**Illustration.** Read the 95% interval against zero. For equivalence at the 5% level use the two compatible one-sided tests, or check whether both endpoints of the 90% interval lie strictly between −δ and δ. Compare B and C first. Both 95% intervals contain zero, and only C’s 90% interval fits inside its negligible region.

| Case | Two-sided p-value against zero | 95% interval (pp) | 90% interval (pp) | TOST p-value | Result |
|---|---:|---|---|---:|---|
| A | 5.73 × 10⁻⁷ | [0.0608, 0.1392] | [0.0671, 0.1329] | < .0001 | Reject zero and establish equivalence |
| B | 0.3173 | [−1.9199, 5.9199] | [−1.2897, 5.2897] | 0.6915 | Neither conclusion established |
| C | 1 | [−0.001960, 0.001960] | [−0.001645, 0.001645] | < .0001 | Establish equivalence only |
| D | 3.80 × 10⁻⁸ | [0.7080, 1.4920] | [0.7710, 1.4290] | 0.6915 | Reject zero only |

Very small positive p-values can display as zero at machine precision. Report A and C’s TOST results as below .0001. [§2, Why the two tests can give different answers](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark)

For A with δ = 0.05 pp, the 90% interval stays at [0.0671, 0.1329] pp and falls outside the narrower bounds. The upper one-sided test gives the larger p-value, about 0.9938, so the TOST result no longer supports equivalence. The smaller margin asks for a more demanding notion of negligibility. A wide fixed margin can be economically unhelpful while retaining calibration for its stated null. Selecting a margin after seeing results raises a separate error-control question.

In task 4 the interval half-width is 1.64485 pp, exceeding the entire permissible half-width 0.1 pp. No possible centre fixes this. The true effect is zero by construction, so failed equivalence does not reveal a nonzero effect or an economically large effect. It can reflect insufficient precision relative to the margin. See the [mathematical counterexample](../wiki/evidence/mathematical-checks.md) and [critical equivalence audit](../wiki/disagreements/equivalence-audit.md).

For task 5, an effect below c/V yields negative net benefit under the stated valuation and cost. Very harmful effects are also below that threshold. A symmetric equivalence claim would additionally have to rule out effects at or below its lower margin. Defend your choice of question and margin before choosing the test. [§4, Setting a margin worth testing](../synthesis/critical-synthesis.md#setting-a-margin-worth-testing)

</details>

[Exercise index](README.md) · [Next: power and selection](03-power-selection.md)
