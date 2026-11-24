# 03. Power and selection

Suppose the lender wants to detect a small reduction in defaults, and the study will only be reported if its test rejects zero. Work out what the design can detect before deciding what to make of the reported estimates. This exercise builds on exercises 01–02 and uses the standard normal distribution.

The chapter discusses selection in its treatment of intervals and checks the limit of power near zero in the 2008 exchange. Use the paper notes when distinguishing a design analysis at externally justified effects from “observed power” reusing the same estimate. [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [§3, Competing arguments](../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) · [Power and selection](../wiki/concepts/power-selection.md) · [Gelman and Carlin](../wiki/papers/gelman-carlin-2014.md) · [Hoenig and Heisey](../wiki/papers/hoenig-heisey-2001-power.md) · [Claim C006](../wiki/claims/C006-noisy-magnitudes.md)

## Problem and assumptions

**Illustration:** β is a one-year default-probability reduction in percentage points in the hypothetical target population. At each candidate design, β̂ ∼ N(β, s²), with known s and valid identification. A two-sided test rejects β = 0 when |β̂/s| > z₀.₉₇₅. Its design-stage power at specified true effect β is

`Φ(−z₀.₉₇₅ − β/s) + 1 − Φ(z₀.₉₇₅ − β/s)`.

Assume β is specified independently of the eventual estimate. No observations are generated. Every calculation below is analytical; there is no seed or Monte Carlo uncertainty.

## Tasks

1. **Approach zero with the design fixed.** At s = 1 pp, calculate rejection probabilities for true β = 1, 0.1, 0.01 and 0 pp. Predict the limit as β approaches zero and name the rejection probability at the exact null.
2. **Change precision with the effect fixed.** At a substantively motivated effect of 0.1 pp, compare s = 1 pp with s = 0.02 pp. State what the comparison establishes about detection and what separate arguments you would need about importance and identification.
3. **Translate precision into sample size.** Suppose independent sampling justifies s ∝ 1/√n. What sample-size multiplier reduces s from 1 to 0.02? Explain when clustering, dependence or changes in measurement could make that extrapolation unreliable.
4. **Apply the reporting screen.** At s = 1, a two-sided .05 publication filter retains only estimates satisfying |β̂| > 1.95996 pp. When true β = 0.1 pp, write a lower bound for |β̂|/|β| among retained estimates. Inspect both tails for wrong signs. Say what further calculation would give an expected exaggeration ratio or a sign-error probability.
5. **Evaluate a reliability claim.** A researcher plugs a large significant estimate into the power formula and calls it “the study’s achieved reliability”. Trace how the input and the reported test statistic are related. Propose a design analysis over plausible effects and say what evidence would justify that range.
6. **Stress-test your recommendation.** Consider more observations, preregistration and a different threshold. For each, identify the problem it addresses and one that it leaves unresolved.

```python
from implementations.normal_model import power_two_sided

for effect in [1, 0.1, 0.01, 0]:
    print(effect, power_two_sided(effect, se=1))
print("Precise design:", power_two_sided(0.1, se=0.02))
```

**Submit:** a power table, the selection-bound derivation and a 400-word design note. Give units, plausible alternatives, target precision or power, and a separate account of identification. Do not describe this exercise as a simulation or evidence about the actual publication process.

<details>
<summary>Worked solution and discussion</summary>

**Illustration.** At s = 1 the rejection probabilities are approximately 0.170075, 0.051146, 0.050011 and 0.05. As the true effect approaches zero, the standardised sampling distribution approaches the null distribution. The fixed rejection region still takes probability α = .05 at the null, the test’s size. At β = 0.1 and s = 0.02 power is approximately 0.998817. Under the stipulated scaling law a fiftyfold reduction in s requires squaring that factor, giving a sample-size multiplier of (1/0.02)² = 2,500. This ratio applies to the two hypothetical designs. [§3, Technical claims about power](../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) · [Mathematical evidence note](../wiki/evidence/mathematical-checks.md)

Among selected estimates at s = 1 and true β = 0.1, divide the minimum absolute estimate that clears the screen by 0.1. The ratio exceeds 1.95996/0.1 ≈ 19.60. To find expected Type M, average the absolute ratio over both retained tails. To find Type S for this positive true effect, divide the probability in the retained lower tail by the total probability of selection. The bound itself follows from the screen. Extending it to a literature would need evidence about how estimates are selected and what effects and precisions are plausible.

Substituting β̂ into the power formula reuses the test statistic, so the resulting number is already determined by the study’s result. For a prospective design, justify plausible inputs from relevant evidence and compare power across that range. If the sample size is infeasible, discuss which precision you can achieve. Even a much larger sample can leave bias or non-identification intact. To see the effect of selection across repeated studies, follow the lab after completing this calculation. [Selection lab](../simulations/labs/02-selection.md)

</details>

[Exercise index](README.md) · [Finish Module 3 with the simulation labs](../CURRICULUM.md#module-3-power-selection-and-noisy-magnitudes) · [Next core exercise: finance and identification](05-finance-identification.md) · [Optional AER source audit](04-aer-source-audit.md)
