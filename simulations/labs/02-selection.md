# Lab 2 — selection changes the population of reported estimates

**Illustration.** An estimate can be unbiased across all studies and look very different among those that pass a reporting screen. Predict what the screen will do to the signs and magnitudes in this synthetic experiment. Then compare reported discoveries with fresh holdout estimates. The reporting rule and search design are stipulated for the lab. [Chapter §2, Evidence about the benchmark](../../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Slide gate](../../reviews/review-gate.md)

Use the selected count whenever you report a conditional sign or magnitude result. You will need the normal tails and the distinction between study precision and Monte Carlo precision. [Power and selection exercise](../../exercises/03-power-selection.md) · [Simulation guide](../README.md)

## Run and record

From the repository root, with Python 3.10 or later:

```sh
python3 simulations/run_labs.py --lab selection --replications 50000 --seed 20261123 --output-dir scratch/selection
```

The [implementation](../selection.py) uses only the standard library. Save the command, Python version, Git commit and generated files with your submission. The base seed is `20261123`; each named scenario receives its own SHA-256-derived seed, recorded in the output. The [reference results](../results/reference.json) and [summary](../results/summary.md) use 50,000 repetitions. Tiny floating-point differences across platforms need not change the statistical lesson.

## Data-generating process and target

The estimand θ is a hypothetical candidate's population **monthly gross factor-model alpha**, in basis points (bp), under a fixed model and unchanged trading regime. No individual assets or returns are simulated. Instead, generate the estimator directly: independently for each repeated study,

`X ~ N(θ, 10²)` and `Y ~ N(θ, 10²)`, with X and Y independent.

X is the discovery estimate and Y is an independent holdout estimate. Its known sampling SE is 10 bp, not the Monte Carlo SE of a summary across studies. This direct-estimator DGP assumes identification, a correct normal sampling model and known variance. It omits serial dependence, factor misspecification, costs, capacity, adaptation and changing true effects. It therefore cannot establish investor welfare.

The fixed reporting event is `A = {|X/10| > z₀.₉₇₅}`: two-sided rejection of θ = 0 at .05. Four single-candidate regimes use θ = 0, 1, 30 and −1 bp. These effects are chosen before the simulated data; they are not re-estimated from a selected result. Repetition means a new independent study of the same stipulated candidate, not more observations for the original estimate.

A fifth regime generates **20 independent null candidates** per repetition, all with θ = 0 and SE = 10. Select the largest absolute discovery statistic and report it only if it exceeds the unadjusted .05 cutoff. The chosen candidate gets a new independent holdout. Also record whether the family maximum exceeds the Bonferroni cutoff with per-test size .05/20. Sampling just the chosen candidate's holdout is valid here because every candidate has the same null distribution and the entire holdout experiment is independent of discovery.

**Error criterion.** The lab evaluates inferential error and estimator distortion; it specifies no utility or welfare loss. Type S is the probability of the wrong sign conditional on A, for nonzero θ. Type M is `E(|X|/|θ| | A)`, also for nonzero θ. Signed bias is `E(X−θ | A)`, a different quantity. At θ = 0, neither a true sign nor a relative magnitude denominator exists, so Type S and Type M are **undefined**, represented as JSON `null`.

## Monte Carlo uncertainty

For rejection frequencies, the denominator is all repetitions R. For conditional quantities it is the selected count K. Rate MCSE is `sqrt(p̂(1−p̂)/K)` or its R-denominator counterpart; mean MCSE is the sample SD of the relevant replication-level outcomes divided by √K. The output includes K through the summary's `n` and as `selected_count`.

A zero observed event count gives plug-in MCSE zero, but is not evidence that the true probability is exactly zero. Consult the Wilson 95% Monte Carlo interval and increase repetitions for rare events. Mean ± 1.96 MCSE is only an approximate Monte Carlo interval, especially with small K. These intervals concern the simulation's probabilities or expectations under the specified DGP, **not θ in an empirical study**. If K = 0, conditional output is unavailable rather than zero. The discovery-minus-holdout MCSE uses within-study paired differences.

## Exercises

1. **Predict before running.** For each nonzero θ, predict signed bias, relative exaggeration and Type S risk after the screen. At θ = 0, decide whether symmetry implies anything about the signed and absolute means separately.
2. **Show the denominators.** Tabulate R, K, estimated rejection probability, MCSE, Type S, Type M, selected bias and independent-holdout bias beside the exact benchmarks. Label the units, including which quantities are dimensionless.
3. **Work from both tails.** With `c = 10z₀.₉₇₅`, derive `P(A)`, `E(X | A)` and `E(|X| | A)`. Use the last quantity to get the Type M benchmark. Explain what changes if you use the selected X in place of the stipulated θ.
4. **Use the independent holdout.** Compare `selected_bias`, `selected_holdout_bias` and the paired difference. Explain why the holdout returns to θ in expectation and what one unsuccessful holdout would allow you to say about θ.
5. **Search 20 candidates.** Start from the probability that none of the independent null candidates rejects. Derive the family rejection probability at the unadjusted and Bonferroni cutoffs. Describe what population that probability refers to, and compare the signed and absolute winner means.
6. **Vary simulation precision.** Use 500, 5,000 and 50,000 repetitions and at least three seeds chosen in advance. Compare MCSE with the expected square-root scaling and record all 95% intervals that miss the benchmark. For a zero-event Type S result in the strong-effect regime, inspect the Wilson bound.
7. **Challenge the design.** In a separately saved copy, change the candidate count or add a justified correlated-error model. Name the benchmark you would revise. Explain what additional assumptions would be needed for heterogeneous effects or changing markets. Mark any unimplemented extensions as proposals.
8. **Compare the empirical questions.** Write the strongest inference this simulation permits and the strongest caution about transferring it to finance. Identify which features of an empirical replication study you would check before comparing it with a search critique. [Finance disagreement trail](../../wiki/concepts/finance.md) · [Chapter §4, Comparing analyses of the same data](../../synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data)

**Submit:** commands and environment/commit information, your labelled results table, two tail-moment derivations, a repeated-seed check, and a 500-word interpretation separating the synthetic result, the source positions and the limits of generalisation. Use [worked solutions](../solutions/02-selection.md) after completing the prediction and derivation tasks.

## Sources and explicit limitations

**Source claim:** the existing [Gelman–Carlin note](../../wiki/papers/gelman-carlin-2014.md), based on its named selected sections, records conditional sign/magnitude design analysis using externally justified effects. This lab independently derives normal-model illustrations; it does not claim to reproduce that paper's software or empirical examples, and does not upgrade the note to full-text reading.

**Project interpretation:** selection is one mechanism that can separate a reported magnitude from its population target. This does not establish that all significant results are exaggerated, all selection creates a positive signed bias, or all finance results fail to replicate. [Harvey–Liu–Zhu](../../wiki/papers/harvey-liu-zhu-2016-cross-section.md) and [McLean–Pontiff](../../wiki/papers/mclean-pontiff-2016-predictability.md) have abstract-only coverage here; [Jensen–Kelly–Pedersen](../../wiki/papers/jensen-kelly-pedersen-2023-replication.md) has selected-section coverage. Their designs, models and empirical magnitudes are not replicated by these artificial normal draws. See [C006](../../wiki/claims/C006-noisy-magnitudes.md) and [C008](../../wiki/claims/C008-finance-replication.md).
