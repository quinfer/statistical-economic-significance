# Lab 2 — selection changes the population of reported estimates

**Illustration.** All estimates are synthetic. This lab studies a stipulated reporting rule and search design; it does not estimate actual publication bias, the reliability of a real factor, or the economic value of a trading strategy. The [slide gate](../../reviews/review-gate.md) stays closed.

**Learning objectives:** distinguish unconditional estimation bias from bias after selection; interpret conditional Type S and Type M quantities; expose the denominator of a Monte Carlo estimate; and compare a selected discovery estimate with genuinely independent follow-up evidence. Prerequisites: [power and selection exercise](../../exercises/03-power-selection.md), normal tails and the [simulation guide](../README.md).

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

1. **Prediction before execution.** For each nonzero θ, predict the direction of selected signed bias, relative exaggeration and Type S risk. For θ = 0, distinguish a zero signed conditional mean from a large conditional absolute mean. Explain which predictions use symmetry.
2. **Quantify the filter.** Produce a table with R, K, estimated rejection probability, MCSE, Type S, Type M, selected bias and independent-holdout bias. Include the exact benchmarks. State the units for every column; Type S and Type M are dimensionless.
3. **Derive, then compare.** With `c = 10z₀.₉₇₅`, derive `P(A)` and `E(X | A)` from upper and lower normal tails. Derive `E(|X| | A)` and hence the Type M benchmark. Why is using the realised X as the putative true θ a different exercise?
4. **Replicate independently.** Compare `selected_bias` with `selected_holdout_bias` and their paired difference. Explain why independent holdout estimates return towards θ in expectation while a genuine nonzero effect need not disappear. Does an individual unsuccessful holdout prove θ = 0?
5. **Search a family.** Derive the family rejection probability under independence for 20 null candidates. Compare it with Bonferroni's exact family probability in this independent design. Explain why FWER is not a posterior probability that an arbitrary empirical claim is false. Distinguish signed winner means from absolute winner means.
6. **Monte Carlo stress test.** Repeat with 500, 5,000 and 50,000 repetitions and at least three prespecified seeds. Compare estimated MCSE with the expected square-root scaling; report rather than hide any 95% interval that misses its benchmark. Inspect a zero-event Type S result in the strong-effect regime. Use a Wilson bound instead of treating MCSE = 0 as certainty.
7. **Challenge the design.** Change the number of candidates in a separately saved copy, or add a scientifically justified correlated-error DGP. State which independence benchmark stops applying. Explain why correlated candidates, heterogeneous true effects and changing markets require new assumptions. Do not describe an unimplemented extension as a result.
8. **Methodological disagreement.** Write the strongest inference from this experiment and the strongest caution against that inference. Use the [finance disagreement trail](../../wiki/concepts/finance.md) to identify why an optimistic empirical replication study and a pessimistic search critique need not be direct contradictions.

**Submit:** commands and environment/commit information, your labelled results table, two tail-moment derivations, a repeated-seed check, and a 500-word interpretation separating the synthetic result, the source positions and the limits of generalisation. Use [worked solutions](../solutions/02-selection.md) after completing the prediction and derivation tasks.

## Sources and explicit limitations

**Source claim:** the existing [Gelman–Carlin note](../../wiki/papers/gelman-carlin-2014.md), based on its named selected sections, records conditional sign/magnitude design analysis using externally justified effects. This lab independently derives normal-model illustrations; it does not claim to reproduce that paper's software or empirical examples, and does not upgrade the note to full-text reading.

**Project interpretation:** selection is one mechanism that can separate a reported magnitude from its population target. This does not establish that all significant results are exaggerated, all selection creates a positive signed bias, or all finance results fail to replicate. [Harvey–Liu–Zhu](../../wiki/papers/harvey-liu-zhu-2016-cross-section.md) and [McLean–Pontiff](../../wiki/papers/mclean-pontiff-2016-predictability.md) have abstract-only coverage here; [Jensen–Kelly–Pedersen](../../wiki/papers/jensen-kelly-pedersen-2023-replication.md) has selected-section coverage. Their designs, models and empirical magnitudes are not replicated by these artificial normal draws. See [C006](../../wiki/claims/C006-noisy-magnitudes.md) and [C008](../../wiki/claims/C008-finance-replication.md).
