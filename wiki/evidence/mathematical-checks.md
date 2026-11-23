# Mathematical checks and counterexamples

**Project derivations and synthetic illustrations.** These are deterministic calculations, not findings about real studies and not Monte Carlo simulations. No random seed or simulation error is applicable. Reproduce with `python3 scripts/check_arguments.py`; inspect [code](../../scripts/check_arguments.py) and [generated values](../../synthesis/analytical-checks.json). These checks do not advance the slide gate.

## Power near a null

For a two-sided known-variance normal test of size α, let Z have distribution N(λ,1), with rejection when |Z| > c, where c = Φ⁻¹(1−α/2). Then

`power(λ) = Φ(−c−λ) + 1−Φ(c−λ)`.

As λ tends to zero, power tends to α, not zero. At α=.05 the powers for λ=1,.1,.01,0 are approximately .170075, .051146, .050011 and .05. This corrects the fixed-size limit stated on p. 14 of [Sound and fury](../papers/hoover-siegler-2008-sound.md); it preserves the warning that power against nearby alternatives is low. A finite-sample t test also needs its appropriate degrees-of-freedom cutoff, not automatically 1.96.

## An unstable coefficient does not make its standardised statistic deterministic

For a Gaussian linear regression with fixed residualised regressor sum of squares Sxx and known error standard deviation σ,

`β̂ = β + σZ/√Sxx`, so `β̂/se(β̂) = β√Sxx/σ + Z`, with Z∼N(0,1).

As positive Sxx tends to zero, noncentrality tends to zero but variance of this standardised statistic remains one. With estimated σ, the corresponding statement involves a central t distribution. At exact collinearity the coefficient is unidentified. This qualifies p. 17 of the same paper: instability of a raw coefficient remains a valid concern even though a statistic need not be near zero in every realisation.

## Four magnitude examples

Assume β̂∼N(β,s²), known s, fixed units and a justified negligible region (−δ,δ). Normal 95% intervals are shown; a level-.05 TOST equivalence declaration uses a 90% interval strictly inside the margins. Interval endpoints use repeated-sampling coverage, not a posterior probability for fixed β. The chosen δ values are illustrative assumptions, not empirically validated economic standards.

| Illustration | β̂ | s | δ | 95% interval | Inference |
|---|---:|---:|---:|---|---|
| Small and precise | .1 | .02 | 1 | [.0608,.1392] | Reject zero; establish equivalence under this margin |
| Large and imprecise | 2 | 2 | 1 | [−1.9199,5.9199] | Neither a positive important effect nor negligibility established |
| Precisely near zero | 0 | .001 | .01 | [−.001960,.001960] | p=1; establish equivalence |
| Positive but uncertain relative to δ | 1.1 | .2 | 1 | [.7080,1.4920] | Reject zero but fail the one-sided meaningful-effect test |

The first case refutes sufficiency of zero-null rejection for importance; it does not refute necessity. The third shows that non-rejection need not mean an economically uninformative estimate. The second rebuts treating a large estimate as established magnitude. None removes identification or model adequacy from consideration.

## A genuine nested-test implication

Under a compatible one-sided normal testing procedure at the same α, an importance claim established by a lower bound L > δ > 0 entails L > 0. Thus rejecting H₀:β≤δ implies rejecting H₀:β≤0. It is wrong to claim that zero-null rejection can never be necessary under any definition of established importance. This is a restricted logical implication within a chosen procedure; it is not a universal rule for action or a requirement to run two separate tests. Do not mix a one-sided and a two-sided cutoff when asserting it.

## Action without zero-null rejection

An expressly synthetic policy estimate is £400 per person with known normal standard error £500. Assume an unbiased likelihood, no identification failure, a proper prior β∼N(0,1000²), and one risk-neutral decision between adopting and retaining a zero-payoff status quo. Payoff from adoption is β−c; c is a known per-person cost. No learning, capacity constraints, distributional weights or option to delay are included.

The posterior mean is £320 and standard deviation £447.21. The frequentist two-sided zero-null p-value is .4237. At c=£100, posterior expected net benefit is £220, so this criterion favours adoption. At c=£500, it is −£180, so it favours the status quo with identical statistical evidence. A tighter prior, nonlinear losses or uncertain costs can change the decision. This proves possibility under specified assumptions, not that any actual policy should be adopted.

## Equivalence failures do not reveal false zero nulls

Suppose every true effect is exactly zero, s=1, and the prespecified equivalence margin is δ=.1. The normal 90% interval has half-width 1.64485; no realised estimate can place that interval inside (−.1,.1). Every equivalence test fails, including among estimates that do not reject zero. Yet none of those zero nulls is false. Type II error concerns non-rejection under an alternative and is not a realised frequency of false null claims in this constructed corpus.

This counterexample targets the strong interpretation of an equivalence-testing failure rate, not the utility of equivalence testing. See the [Fitzgerald audit](../disagreements/equivalence-audit.md).

[Critical synthesis](../../synthesis/critical-synthesis.md) · [Matched exchange](../disagreements/2008-exchange.md).
