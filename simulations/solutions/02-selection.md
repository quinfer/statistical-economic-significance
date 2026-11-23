# Worked solution — selection bias

**Illustration and project derivation.** These calculations concern the DGP in [Lab 2](../labs/02-selection.md), not observed finance data. They do not extend the reading claims in the linked source notes. The [implementation](../selection.py), [reference output](../results/reference.json) and [generated summary](../results/summary.md) expose inputs, seeds, denominators and Monte Carlo uncertainty. No slides are authorised.

## 1. The conditional population

Let `X ~ N(θ,s²)`, `c = zs`, `z = Φ⁻¹(1−α/2)`, and `A = {|X|>c}`. Write `a=(−c−θ)/s`, `b=(c−θ)/s`, `L=Φ(a)` and `U=1−Φ(b)`. Then

`P(A) = L + U`.

This is size α at θ = 0 and power at a specified alternative. For θ > 0, Type S is `L/(L+U)`; for θ < 0, it is `U/(L+U)`. There is no true sign to be wrong about at θ = 0, so do not report zero Type S there.

Using `∫ᵦ∞ tφ(t)dt=φ(b)` and `∫₋∞ᵃ tφ(t)dt=−φ(a)`, the unnormalised first selected moment is

`E[X 1(A)] = θ(L+U) + s[φ(b)−φ(a)]`.

Thus

`E(X−θ | A) = s[φ(b)−φ(a)]/(L+U)`.

For a weak positive effect, this is positive; for its negative counterpart it reverses sign. At θ = 0 it is zero by symmetry, even though every selected estimate has absolute magnitude greater than c. A claim that selection always increases the signed mean would therefore be false.

The absolute first moment is

`E[|X| 1(A)] = θ(U−L) + s[φ(b)+φ(a)]`.

Divide by P(A) to obtain the selected absolute mean, then by |θ| for expected Type M when θ ≠ 0. Type M is an expected ratio under a stipulated true effect; it is not a correction factor reliably recoverable from one observed significant X. At θ = 0, use the absolute mean in bp instead of dividing by zero. High noise relative to a small nonzero effect makes this ratio large partly because the denominator is small.

## 2. Reference execution

The following are **computed simulation results**, rounded from the default 50,000 repetitions and base seed 20261123. Read the JSON for unrounded values, derived seeds, MCSEs and Wilson intervals. Different seeds should change the estimates within ordinary Monte Carlo variation; opposite-sign scenarios use separate streams, so their realised outputs need not be exact negatives.

| Scenario θ (bp/month) | Selected K | Rejection estimate (MCSE) | Conditional Type S | Conditional Type M | Selected signed bias, bp (MCSE) |
|---|---:|---:|---:|---:|---:|
| 0 | 2,489 | .04978 (.000973) | Undefined | Undefined | .587 (.474) |
| 1 | 2,597 | .05194 (.000992) | .38583 | 23.3389 | 4.526 (.450) |
| 30 | 42,442 | .84884 (.001602) | 0 observed | 1.08964 | 2.689 (.0389) |
| −1 | 2,633 | .05266 (.000999) | .39233 | 23.4543 | −4.208 (.451) |

For θ = 1, the Type S MCSE is about .00955; Type M MCSE is about .0671. Their denominator is 2,597, not 50,000. At θ = 0, the selected absolute mean is 23.395 bp (MCSE .0672), despite the exact zero signed mean. The random selected signed bias .587 bp is consistent with ordinary Monte Carlo fluctuation; it is not evidence that the symmetric DGP has a positive conditional mean.

At θ = 30, zero wrong-sign events were observed. The exact wrong-sign probability is positive, and the Wilson upper bound is positive. Plug-in MCSE zero does not turn the simulation into a proof of zero risk. Simulation is especially inefficient for resolving such a rare event; the known analytic benchmark is more informative in this model.

## 3. Independent holdout and paired comparisons

Since Y is independent of X with the same fixed mean θ, conditioning on A leaves `E(Y | A)=θ`. Therefore

`E(Y−θ | A)=0`, and `E(X−Y | A)=E(X−θ | A)`.

For the weak positive regime, the reference selected holdout bias is .271 bp (MCSE .198); the paired discovery-minus-holdout mean is 4.256 bp (MCSE .488). For the strong positive regime, the holdout bias is −.0225 bp (MCSE .0482), while the target effect remains 30 bp. These outcomes show why a smaller holdout estimate can coexist with a real effect. A single non-significant holdout does not establish zero or equivalence.

Compute the variance of paired differences from `X_i−Y_i` for the selected i. Do not add the MCSEs. If an alternative design reused data, used a holdout to select among models, or allowed θ to change, the independence argument would need revision. No simulation here identifies adaptation after publication.

## 4. Searching 20 independent null candidates

Each unadjusted test has null rejection probability α. Under independence, no candidate rejects with probability `(1−α)^20`, hence

`FWER = 1−(1−.05)^20 ≈ .641514`.

With a Bonferroni cutoff, each test has size α/20 and the exact family probability in this independent design is

`1−(1−.05/20)^20 ≈ .048830`.

Bonferroni's general bound is at most α even without independence when the individual tests are valid; the displayed equality requires the independent DGP. This lab compares family false positives, not power under alternatives; a welfare or discovery-efficiency recommendation would require additional cases and losses.

The reference unadjusted rate is .64118 (MCSE .002145); Bonferroni's is .04904 (MCSE .000966). Among the 32,059 published family winners, mean absolute discovery alpha is 24.260 bp and mean absolute independent holdout alpha is 7.999 bp. The paired absolute difference is 16.261 bp (MCSE .0397). The holdout absolute mean has exact benchmark `s√(2/π) ≈ 7.979 bp`, because a zero-mean normal observation still has nonzero absolute magnitude.

The selected winner's signed mean is approximately −.066 bp (MCSE .137), with exact expectation zero. Large absolute values and a near-zero signed mean can coexist. In this artificial all-null population, every published claim of a nonzero effect is false; the family rejection frequency still means the probability that a family produces at least one such rejection. It is not a posterior probability for a claim drawn from a different population containing true effects.

## 5. Repetitions, denominators and challenges

MCSE usually shrinks approximately in proportion to `1/√R`. Ten times more repetitions gives roughly `1/√10` of the error, holding the DGP and conditional selection probability fixed. Realised K fluctuates, so conditional errors do not scale exactly. A 95% Monte Carlo interval is allowed to miss its benchmark; repeated-seed results should report misses rather than delete them. Very small K undermines normal approximations for conditional means.

A valid extension specifies the new joint distribution before simulating. Correlation changes the exact family formula. Heterogeneous true effects change which candidate wins and what its holdout mean should be. Regime shifts can change follow-up targets. These are different mechanisms, not automatic interpretations of this baseline.

**Project interpretation:** unbiased estimation before selection does not guarantee reliable magnitudes after selection. The opposing caution is just as important: selection effects depend on true effects, noise and the precise filter, and the strong-effect case has much smaller relative exaggeration than the weak-effect case. Nothing here estimates profession-wide misuse, validates the AER coding, or settles the empirical finance replication debate.

The [Gelman–Carlin note](../../wiki/papers/gelman-carlin-2014.md) has selected-section coverage. [Harvey–Liu–Zhu](../../wiki/papers/harvey-liu-zhu-2016-cross-section.md) and [McLean–Pontiff](../../wiki/papers/mclean-pontiff-2016-predictability.md) are abstract-only here; [Jensen–Kelly–Pedersen](../../wiki/papers/jensen-kelly-pedersen-2023-replication.md) is selected sections. These source limitations remain unchanged. An intellectually defensible discussion compares their targets and assumptions without filling unread sections from memory.
