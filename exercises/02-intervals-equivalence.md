# 02. Intervals and equivalence

**Aim:** distinguish evidence of a nonzero effect, evidence of practical equivalence and insufficient precision. Prerequisite: [exercise 01](01-magnitude-evidence-action.md).

Read [intervals](../wiki/concepts/intervals.md), [equivalence](../wiki/concepts/equivalence.md), [Lakens 2017](../wiki/papers/lakens-2017-equivalence.md) and [C003](../wiki/claims/C003-equivalence.md). Keep the source notes' reading limits in view.

## Problem and assumptions

**Illustration:** use the same hypothetical borrower population and one-year default-reduction estimand as exercise 01, measured in percentage points. Assume β̂ ∼ N(β, s²), known s, no selection or identification failure, and fixed negligible bounds (−δ, δ). Each row is a separate prespecified research question; the margins are not chosen after seeing its result. Use α = .05 throughout.

| Case | β̂ (pp) | s (pp) | δ (pp) |
|---|---:|---:|---:|
| A | 0.1 | 0.02 | 1 |
| B | 2 | 2 | 1 |
| C | 0 | 0.001 | 0.01 |
| D | 1.1 | 0.2 | 1 |

For two one-sided tests (TOST), test both H₀L: β ≤ −δ and H₀U: β ≥ δ. Declare equivalence only if both reject at .05. The compatible normal 90% interval must lie strictly inside the fixed bounds. This is a repeated-sampling procedure, not a posterior probability that β lies within the bounds.

## Tasks

1. Compute each zero-null p-value, 95% interval, 90% interval and TOST p-value. Classify the pair of decisions: reject zero or not; establish equivalence or not. Include all four possible combinations and explain why none is logically contradictory.
2. Explain why case C is informative although its zero-null p-value is exactly one, and why case B's non-rejection does not establish negligibility.
3. In case A, change the **research question** to δ = 0.05 pp. Recalculate and explain which substantive claim has changed. Would choosing that margin only after seeing the data create an additional problem?
4. Construct a failure-of-equivalence example with true β = 0, s = 1 pp and δ = 0.1 pp. Show that the 90% interval cannot fit inside the bounds for any estimate. Does universal failure of equivalence demonstrate that any true effect is nonzero or important?
5. Contrast symmetric equivalence with a one-sided viability question: if each percentage-point reduction is valued at V pounds per borrower and adoption costs c pounds, the positive net-benefit threshold is β > c/V. Explain why ruling out positive viability need not require ruling out a large harmful effect.

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
<summary>Self-check and discussion guide</summary>

**Illustration — calculated results:** the 90% intervals are A [0.0671, 0.1329], B [−1.2897, 5.2897], C [−0.001645, 0.001645] and D [0.7710, 1.4290], all in pp. A both rejects zero and establishes equivalence; B does neither; C establishes equivalence without rejecting zero; D rejects zero without establishing equivalence. TOST p-values for B and D are about 0.6915; for A and C they are below .0001, not mathematically zero.

For A with δ = 0.05 pp, the observed interval no longer lies inside the bounds. A narrow margin concerns a more demanding notion of negligibility. A wide fixed margin can be economically unhelpful while retaining calibration for its stated null; result-dependent margin selection is a separate inferential concern.

In task 4 the interval half-width is 1.64485 pp, exceeding the entire permissible half-width 0.1 pp. No possible centre fixes this. The true effect is zero by construction, so failed equivalence does not reveal a nonzero effect or an economically large effect. It can reflect insufficient precision relative to the margin. See the [mathematical counterexample](../wiki/evidence/mathematical-checks.md) and [critical equivalence audit](../wiki/disagreements/equivalence-audit.md).

A frequentist 90% interval is used here because it implements two compatible one-sided .05 tests. It is not an invitation to choose a lower confidence level until a desired conclusion appears. The one-sided net-benefit threshold and a symmetric negligible region express different economic questions.

</details>

[Exercise index](README.md) · [Next: power and selection](03-power-selection.md)
