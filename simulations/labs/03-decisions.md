# Lab 3 — Decisions under uncertainty

**Illustration.** Two decision rules can recommend different actions from the same estimate. Which rule would you choose before the data arrive, and would you still choose it if the distribution of programme benefits changed? Compare rules under the synthetic model below after completing the individual decision problem. You will use the normal distribution, expectation and Monte Carlo standard errors. [Exercise 06](../../exercises/06-decision-memo.md) · [Chapter §5, Action under uncertainty](../../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty)

## Question and design

A hypothetical programme has unknown average gross benefit θ in **pounds per eligible person over one year**, in a fixed target population. The estimate satisfies `Y | θ ∼ N(θ, 500²)`. It is unbiased, its sampling standard error is known, and identification and transport to this population are assumed valid. Each replication represents a new decision problem, not an additional observation on one programme.

Choose once between adoption and a status quo. Per-person utility is `U(a,θ)=a(θ−c)` for `a∈{0,1}`, with known cost c and status quo payoff zero. Utility is linear and risk-neutral. Individual outcome variation, distributional weights, uncertain costs, capacity, delay and future learning are excluded. The random θ in prior-predictive scenarios represents variation across hypothetical programme means; it is **not** a distribution of individual treatment effects.

Compare seven pre-specified rules on the **same θ and Y in each replication**:

| Rule | Adopt when |
|---|---|
| `bayes` | Posterior mean exceeds cost under the proper prior `θ∼N(0,1000²)` |
| `skeptical_bayes` | Posterior mean exceeds cost under the proper prior `θ∼N(0,100²)` |
| `positive_significance` | Y is positive and the two-sided known-SE test of θ=0 has p<.05 |
| `cost_confidence` | The one-sided 95% lower confidence bound `Y−Φ⁻¹(.95)×500` exceeds cost |
| `plugin` | Y exceeds cost |
| `always` | Every time |
| `never` | Never |

The positive-significance comparator deliberately uses a cost-blind zero-null gate; it is not a claim that all inferential practice recommends this rule. The cost-confidence rule instead limits the probability of false adoption to .05 for every `θ≤c` under the stated sampling model. It uses a calibrated evidential criterion about net benefit, rather than maximising posterior expected utility. Neither rule represents every frequentist method. The evaluation charges every rule the same cost. The always/never rules are useful benchmarks, not recommended policies. Each Bayes rule is optimal for its own stated posterior expected-utility problem; evaluation need not use its prior as the data-generating distribution.

The scenarios are fixed in advance:

| Scenario | Evaluation distribution of θ | Cost |
|---|---|---:|
| `matched_prior_cost100` | N(0,1000²), matching the baseline prior | £100 |
| `matched_prior_cost500` | N(0,1000²), matching the baseline prior | £500 |
| `mismatched_prior_negative` | N(−250,100²), matching neither assumed prior | £100 |
| `fixed_zero` | θ=0 in every replication | £100 |
| `fixed_moderate_benefit` | θ=400 in every replication | £100 |
| `fixed_large_benefit` | θ=1200 in every replication | £100 |

The evaluator knows the simulated θ; the decision rules receive only Y, known SE, cost and their own fixed prior. An oracle knowing θ earns `max(θ−c,0)`. **Oracle regret** is this payoff minus the rule's payoff and is non-negative in every replication. Averaging over a stipulated prior distribution and evaluating at a fixed θ are different performance questions; neither supplies minimax regret over all possible states.

## Reproduce

From the repository root, with Python 3.10 or later and no third-party packages:

```sh
python3 simulations/run_labs.py --lab decisions --replications 50000 --seed 20261123 --output-dir scratch/decisions
```

The [implementation](../decisions.py) records scenario parameters and independently derived seeds. The committed [reference results](../results/reference.json) and [summary](../results/summary.md) use the declared reference run. Repeating a seed on the recorded environment reproduces the draws; small platform-level floating-point differences may occur.

For a mean utility, regret or **paired difference**, MCSE is the replication-level sample standard deviation divided by √R. For an adoption rate it is `sqrt(p̂(1−p̂)/R)`; the report also gives a Wilson 95% Monte Carlo interval. These describe simulation error in estimating a fixed model performance measure. They are not confidence intervals for an actual programme's θ. A zero observed MCSE after no rare adoptions is not proof of zero underlying risk; inspect the count, Wilson interval and analytic benchmark.

## Tasks

1. **Find the cutoffs.** Derive each finite threshold. At Y=£400, compare the baseline and tight-prior actions at costs £100 and £500. Prove the cost-confidence rule’s false-adoption bound at θ≤c and identify the event the bound controls.
2. **Predict the ranking before running.** Under the matched prior, say which rule should maximise average utility and why. Compare the simulated means with exact benchmarks and use the paired MCSE to explain any apparent reversal among close rules.
3. **Check the pairing.** For each rule verify `mean utility + mean regret = mean oracle payoff`. Compare `other_minus_bayes_utility` and `other_minus_bayes_regret`. Explain what you would miss by computing uncertainty from separate MCSEs as though the rules had seen independent samples.
4. **Distinguish the two decisions.** Find an adoption without rejection of zero. Name what the frequency of that event measures, and distinguish the action taken after observing data from the performance of the rule over repeated decisions.
5. **Change the evaluation.** Compare the mismatch and all three fixed-state scenarios. Which conclusions about baseline Bayes survive? Explain what information the oracle uses that a feasible rule lacks, and what the average result under one prior tells you about any individual state.
6. **Measure simulation noise.** Repeat with seed 20261124 and with 10,000 versus 50,000 replications. Which sources of uncertainty does R change? Explain rare-event zeros using their counts and the benchmark.
7. **Change the decision problem.** Propose uncertain costs or asymmetric losses. Write the revised utility and justify the extra assumptions before changing code. Explain the substantive purpose of any new prior or scenario you propose. [Chapter §6, What would change the conclusion?](../../synthesis/critical-synthesis.md#6-what-would-change-the-conclusion)

**Submit:** a 700-word decision-method memo, exact commands, result tables including MCSEs and denominators, and one strong objection to your preferred rule. Explain what empirical evidence and stakeholder judgement would be needed to apply it. The [worked solution](../solutions/03-decisions.md) supplies derivations and interpretation checks.

## Evidence boundaries

**Source trail:** the [Manski 2019 note](../../wiki/papers/manski-2019-treatment-choice.md) records selected indexed section 3 passages on consequences and regret; full text was not read. [Manski 2021](../../wiki/papers/manski-2021-econometrics-decisions.md) and [Kandel–Stambaugh](../../wiki/papers/kandel-stambaugh-1996-asset-allocation.md) remain abstract-level readings. [Wald](../../wiki/papers/wald-1950-decision-functions.md) is metadata-only and cannot support a detailed attributed claim here. These normal-model calculations are original project illustrations, not replications or transcriptions of those papers.

**Project interpretation:** the [decision concept](../../wiki/concepts/decisions.md), [C002](../../wiki/claims/C002-action-without-rejection.md) and [C010](../../wiki/claims/C010-uncertainty-and-choice.md) distinguish action, evidence and competing objectives. This lab does not model the source papers' complete methods, robust Bayes, partial identification or empirical investment performance. Book access and disputed AER coding limitations remain as recorded in [STATUS](../../STATUS.md). The [slide gate](../../reviews/review-gate.md) stays closed.

[Simulation index](../README.md) · [Worked solution](../solutions/03-decisions.md)
