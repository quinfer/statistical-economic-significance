# 03. Power and selection

**Aim:** reason about design-stage power and selected estimates without confusing either with the probability that a reported result is true. Prerequisite: exercises 01–02 and the standard normal distribution.

Read [power and selection](../wiki/concepts/power-selection.md), [Gelman–Carlin](../wiki/papers/gelman-carlin-2014.md), [Hoenig–Heisey](../wiki/papers/hoenig-heisey-2001-power.md) and [C006](../wiki/claims/C006-noisy-magnitudes.md). The source notes distinguish externally justified plausible effects from same-data “observed power”.

## Problem and assumptions

**Illustration:** β is a one-year default-probability reduction in percentage points in the hypothetical target population. At each candidate design, β̂ ∼ N(β, s²), with known s and valid identification. A two-sided test rejects β = 0 when |β̂/s| > z₀.₉₇₅. Its design-stage power at specified true effect β is

`Φ(−z₀.₉₇₅ − β/s) + 1 − Φ(z₀.₉₇₅ − β/s)`.

Assume β is specified independently of the eventual estimate. No observations are generated. Every calculation below is analytical; there is no seed or Monte Carlo uncertainty.

## Tasks

1. At s = 1 pp, calculate rejection probabilities for true β = 1, 0.1, 0.01 and 0 pp. What is the limit as β approaches zero? Is rejection probability at the exact null customarily called power against an alternative?
2. For a substantively motivated true effect of 0.1 pp, compare s = 1 pp with s = 0.02 pp. Explain why a power calculation alone cannot establish that 0.1 pp matters or that the identification assumptions hold.
3. Suppose an independent-sampling design justifies s ∝ 1/√n. What sample-size multiplier would reduce s from 1 to 0.02? State why this extrapolation could fail with clustering, dependence or different measurement quality.
4. At s = 1, a two-sided .05 publication filter retains only estimates satisfying |β̂| > 1.95996 pp. If true β = 0.1 pp, what lower bound does this place on |β̂|/|β| among retained estimates? Can some retained estimates have the wrong sign? Distinguish the deterministic selection bound from an expected exaggeration ratio or a calculated sign-error probability.
5. A researcher substitutes a large significant estimate into the power formula and calls the resulting number “the study's achieved reliability”. Explain the problem. Propose a design analysis over plausible effects chosen from substantive knowledge, and record what evidence could justify that range.
6. Present the strongest caution against your own proposed solution. More observations, preregistration and a different threshold address different problems; identify at least one problem each leaves unresolved.

```python
from implementations.normal_model import power_two_sided

for effect in [1, 0.1, 0.01, 0]:
    print(effect, power_two_sided(effect, se=1))
print("Precise design:", power_two_sided(0.1, se=0.02))
```

**Submit:** a power table, the selection-bound derivation and a 400-word design note. Give units, plausible alternatives, target precision or power, and a separate account of identification. Do not describe this exercise as a simulation or evidence about the actual publication process.

<details>
<summary>Self-check and discussion guide</summary>

**Illustration — calculated results:** rejection probabilities at s = 1 are approximately 0.170075, 0.051146, 0.050011 and 0.05. The limit is α = .05, not zero; at the null this is the test's size. At β = 0.1 and s = 0.02, power is approximately 0.998817. The stipulated sample-size multiplier is (1/0.02)² = 2,500, not 50. It is a ratio, not a claim that a particular real study needs 2,500 observations.

Among selected estimates at s = 1 and true β = 0.1, the absolute ratio exceeds 1.95996/0.1 ≈ 19.60. The lower tail is also retained, so wrong-sign estimates are possible. This bound is not an expected Type M error and does not give a Type S error probability. Nor does it establish the distortion in a real literature, where selection and true effects may differ.

Substituting β̂ for a substantively plausible alternative reuses the result in a quantity determined by its test statistic. It does not create independent evidence of reliability or reveal the true β. A good answer uses a defensible range of effects, allows the preferred design to be infeasible and explains why bias or non-identification can persist as sampling error shrinks.

The [mathematical evidence note](../wiki/evidence/mathematical-checks.md) checks the limiting power statement within the debate. Correcting that local statement does not invalidate every argument made by its authors.

</details>

[Exercise index](README.md) · [Next: AER source audit](04-aer-source-audit.md)
