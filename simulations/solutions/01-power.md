# Worked solutions — power and precision

**Illustration.** Start with the £20 effect and the £100 margin. Ask how often a repeated study rejects zero, then how often it supports a negligible effect. The exact probabilities come from the stipulated normal model. The estimates in the reference run also depend on the seed and replication count. Use `benchmarks` for the exact values and `metrics` for the realised values. [Chapter §2, Evidence about the benchmark](../../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Reference JSON](../results/reference.json) · [Reference summary](../results/summary.md)

## 1. Start from the estimand and sampling distribution

The quantity of interest is the mean one-year policy effect in pounds per eligible person. Write `s = sigma/√n` for the true sampling SE and `r` for the reported SE. With sigma = £1,000, sample sizes 100, 2,500 and 100,000 give s = £100, £20 and approximately £3.1623 per person per year. Start with r = s, as in the main grid. Vary n while holding the effect and prespecified margin fixed.

Let `c = z(.975)*r` and let Φ denote the standard normal CDF. Zero-null rejection occurs in the two tails. Therefore

`P(reject zero | theta) = Φ((−c−theta)/s) + Φ((theta−c)/s)`.

At theta = 0 and r = s, this is .05 for every n. This is the test’s size, the rejection probability with the null held true. At a fixed nonzero theta in the calibrated grid, shrinking s increases the rejection probability. Keep theta as an input when interpreting the reference run. The simulation estimates a probability conditional on that input. [Chapter §3, Technical claims about power](../../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree)

## 2. Monte Carlo uncertainty is a separate layer

Each repeated study contributes an indicator, so at a fixed design the event count is binomial `(R,p)`. Its rate has variance `p(1−p)/R`, estimated by plugging in the realised rate. For example, a probability near .05 at R = 50,000 has MCSE about .000975, or 0.0975 percentage points. Measure that error in the estimated rate. For precision of the effect estimate from a single study, go back to the sampling SE in pounds per person per year.

An individual 95% Wilson interval is not a simultaneous guarantee for a table of many probabilities. Some targets can fall outside their intervals even when the generator is correct. Metrics within a scenario are also dependent, so the chance of at least one miss should not be computed as if every reported interval were independent. Automated tests use more conservative tolerances against exact probabilities; statistical checks still supplement, rather than replace, code inspection.

When zero or R events occur, the plug-in MCSE is zero but the Wilson interval has positive width. Here exact normal probabilities can resolve whether the event is impossible or simply rare. At n = 100, equivalence is structurally impossible with the stipulated margin and SE; a nearly zero false-equivalence probability for a large effect is a different case.

## 3. Zero, negligibility and a positive meaningful effect

Put the 90% interval inside the equivalence region by moving each margin inwards by the interval’s half-width. Let `q = z(.95)*r` and delta = £100. The equivalence rejection region is

`−delta + q < Xbar < delta − q`.

It is empty if `q ≥ delta`. Otherwise its probability is

`Φ((delta−q−theta)/s) − Φ((−delta+q−theta)/s)`.

This is TOST at alpha = .05 because each one-sided test uses z(.95), yielding a 90% two-sided interval. A 95% interval is still used for the separate coverage metric. At n = 100, q is approximately £164.49, so no estimate can have its 90% interval wholly inside ±£100. Equivalence failure in that design cannot distinguish theta = £0 from theta = £200.

For `small_n100000`, a true £20 effect is both highly detectable against zero and safely inside the chosen ±£100 region. That is no contradiction: the null hypotheses differ. For `meaningful_n100`, a true £200 effect has substantial sampling uncertainty. Its point estimate and zero-test outcome alone cannot certify a positive effect beyond £100.

The latter claim has its own one-sided test:

`P(support theta > delta | theta) = Φ((theta−delta−q)/s)`.

This probability is less than the zero-rejection probability in the positive-effect examples. In the reference run, `meaningful_n100` rejects zero in 0.51676 of replications and supports an effect above £100 in 0.26008. For `small_n100000` these frequencies are 1 and 0, with analytic benchmarks close to those limits. Those rates describe the designs. For a single study, you could say that a 90% interval wholly within ±£100 supports equivalence at the 5% level, or that a one-sided 95% lower bound above £100 supports an effect above that benchmark. Give the actual interval and assumptions in either case. “The coefficient was significant, so the programme is worthwhile” ignores the benchmark and costs. “It was non-significant, so it is negligible” ignores the relevant alternatives.

## 4. Reconstruct the four cells

Let Z be the zero-test rejection rate, E the equivalence rate and B their joint rate. Then:

| Outcome | Probability |
|---|---|
| Both reject | B |
| Only zero rejects | Z − B |
| Only equivalence rejects | E − B |
| Neither rejects | 1 − Z − E + B |

All four sum to one. The code also records the last quantity directly as `neither_reject`; this gives an arithmetic cross-check. “Only equivalence” is compatible with a precisely estimated negligible effect; “neither” can mean that both relevant distinctions remain unresolved. Neither classification is a posterior probability about theta.

At theta = delta, the equivalence null is true. For correct SE and this continuous TOST construction, the false-equivalence probability cannot exceed alpha. The boundary scenario checks that particular operating property; it does not show that a £100 margin is substantively justified.

## 5. Understate the SE

Under theta = 0, define `k = r/s`. The zero-rejection probability becomes

`2*Φ(−z(.975)*k)`.

The 95% interval coverage becomes

`2*Φ(z(.975)*k) − 1`.

At k = 1 these are .05 and .95. At k = .5 they are approximately .327 and .673. More replications reveal these miscalibrated operating characteristics more precisely; they do not repair them. This stress case does not identify the reason for a bad SE in an actual study. Dependence, misspecification, estimated variance and selection require their own models and diagnostics.

## 6. Change a design, not a conclusion by decree

Increasing R from 50,000 to 200,000 approximately halves MCSE and keeps the exact benchmark fixed. Increasing n affects s and therefore the study probabilities themselves. For the margin sensitivity run hold r = £20 and theta = £20 fixed. Inserting delta = £50 into the equivalence formula gives probability 0.4106, compared with 0.9907 at £100. The same true effect lies inside both margins. The smaller margin leaves less room for the entire interval to fit. [Chapter §4, Setting a margin worth testing](../../synthesis/critical-synthesis.md#setting-a-margin-worth-testing)

An adequate memo would justify a real margin using units, opportunity costs, population, distributional consequences and horizon, then assess sensitivity. It would distinguish these normative and measurement choices from power. It would also allow the conclusion that the desired precision is infeasible, or that more data are less valuable than better identification. Choosing a margin to fit the observed interval cannot retrospectively create a prespecified claim.

## Reference-run check

**Computed illustration:** 50,000 replications per scenario, base seed 20261123. Zero-rejection rates and MCSEs below are proportions, not percentages. The full report also contains coverage, equivalence, meaningful-effect and joint classifications.

| Scenario | Zero rejection | MCSE | Exact benchmark |
|---|---:|---:|---:|
| `null_n100` | 0.04934 | 0.000968561 | 0.05 |
| `null_n2500` | 0.04798 | 0.000955802 | 0.05 |
| `null_n100000` | 0.04894 | 0.00096483 | 0.05 |
| `small_n100` | 0.057 | 0.00103683 | 0.0545947 |
| `small_n2500` | 0.1672 | 0.0016688 | 0.170075 |
| `small_n100000` | 1 | 0 | 0.999994 |
| `meaningful_n100` | 0.51676 | 0.00223481 | 0.516005 |
| `meaningful_n2500` | 1 | 0 | 1 |
| `meaningful_n100000` | 1 | 0 | 1 |
| `equivalence_boundary_n2500` | 0.99876 | 0.000157382 | 0.998817 |
| `understated_se_null_n2500` | 0.32868 | 0.00210071 | 0.327095 |

In this run, **2 of the 11** zero-rejection Wilson intervals miss their benchmark: `null_n2500`, `small_n100`. They are retained in the report. This is compatible with finite Monte Carlo variation; these intervals are not simultaneous coverage guarantees. A displayed rate of 1 and MCSE of 0 must still be read beside its Wilson interval and exact benchmark.

## Source boundary

These are project derivations checked against their implementation. The [lab's evidence links](../labs/01-power.md#evidence-links-and-limits) retain selected-section and abstract-only source limits. The exercise supplies no additional evidence about real policy effects, disputed AER codes or unread book chapters, and does not authorise slides.

[Lab questions](../labs/01-power.md) · [Lab index](../README.md)
