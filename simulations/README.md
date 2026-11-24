# Simulation labs: power, selection and decisions

**Illustration: every simulated observation is synthetic.** These labs explore consequences of explicit models; they do not estimate actual policy effects, validate the AER survey codes or reproduce a paper's empirical results. The [slide gate](../reviews/review-gate.md) remains **closed**.

Each lab pairs a reproducible experiment with questions, a concrete submission and a separate worked solution. Try the exercises before opening the solutions.

| Lab | What you will compare | Chapter reading | Worked solution |
|---|---|---|---|
| [1. Power and precision](labs/01-power.md) | How sample size, effect size and reporting the wrong standard error affect tests and intervals | [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) | [Power solution](solutions/01-power.md) |
| [2. Selection bias](labs/02-selection.md) | All estimates, significant estimates, independent holdouts and a search across null candidates | [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) and [§4, Comparing analyses](../synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data) | [Selection solution](solutions/02-selection.md) |
| [3. Decisions under uncertainty](labs/03-decisions.md) | Decision rules under different costs and priors, with average and state-specific regret | [§5, Action under uncertainty](../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty) | [Decision solution](solutions/03-decisions.md) |

## Run a lab

Python 3.10 or later, using only its standard library. From the repository root:

```sh
python3 simulations/run_labs.py --lab power --replications 50000 --seed 20261123 --output-dir scratch/power
python3 simulations/run_labs.py --lab selection --replications 50000 --seed 20261123 --output-dir scratch/selection
python3 simulations/run_labs.py --lab decisions --replications 50000 --seed 20261123 --output-dir scratch/decisions
```

Or run all three together:

```sh
python3 simulations/run_labs.py --lab all --replications 50000 --seed 20261123 --output-dir scratch/simulation-labs
```

Each command writes three files in the specified folder, replacing an earlier generated report there:

- `reference.json`: full design, parameters, base and derived seeds, Python version, code hashes, numerical results and analytic benchmarks.
- `metrics.csv`: one row per metric, including its denominator, Monte Carlo standard error and a Wilson interval for rates.
- `summary.md`: readable tables with scenario parameters and the same results.

The default configuration is committed in [reference.json](results/reference.json), [metrics.csv](results/metrics.csv) and the [results summary](results/summary.md). These are computed outputs, not targets to tune the simulation towards. Personal experiments belong in ignored `scratch/` directories.

## Find a result you need

Open your run’s `summary.md` and expand the scenario named in the task. To compare scenarios, filter `metrics.csv` by its `lab`, `scenario` and `metric` columns. Read the estimate alongside its MCSE and analytic benchmark where one is available. The output column `n` counts the replications used **for that metric**. For a rate over all repetitions it is R; for a conditional result it counts the selected cases. To find the simulated study’s sample size in Lab 1, use `sample_size` in the scenario parameters. Those parameters are in the summary and `reference.json`.

## Reproduce and validate

```sh
python3 simulations/run_labs.py --check-reference
python3 scripts/check_all.py
```

The reference check reruns the stored seed, replication count and scenarios, verifies the implementation hashes and compares numerical results with small floating-point tolerances. It also checks that the CSV and Markdown reflect the stored JSON. It does not rewrite the reference. The full repository check includes independent analytic benchmarks and tests of conditional denominators, undefined quantities and paired comparisons.

Random streams are derived from the base seed and a stable scenario label using SHA-256, so running one lab does not consume another lab's stream. Repeated runs in the recorded Python environment reproduce the random stream. Small floating-point differences across operating systems are tolerated; random-library changes across future Python versions may require a recorded version or a deliberately reviewed reference update. Do not regenerate outputs merely to silence a failed check.

To update the reference after reviewing a design or code change:

```sh
python3 simulations/run_labs.py --lab all --replications 50000 --seed 20261123 --output-dir simulations/results
```

Inspect the changed designs and numbers, rerun the checks and record why the change was made. An extra seed run checks sensitivity to simulation noise; it must not become a search for a preferred result.

## Read uncertainty correctly

The **study standard error** describes variability of an estimator across hypothetical studies. The **Monte Carlo standard error (MCSE)** describes how accurately a finite simulation estimates a probability or expectation under its chosen model. Increasing the number of simulated replications reduces the latter; it does not improve the design, sample size or identification in each simulated study.

For independent replication-level values, mean MCSE is sample SD divided by the square root of the number of values. Rate MCSE is `sqrt(p_hat * (1 - p_hat) / n)`. Wilson 95% Monte Carlo intervals remain informative when the observed rate is zero or one, where the plug-in MCSE is zero. Mean ± 1.96 MCSE is a large-replication approximation, not a guarantee for tiny or heavy-tailed selected samples.

Conditional results use the **selected count**. If no observations meet the selection rule, the result is undefined (`null`), not zero. Type M and Type S relative to a true sign are undefined at a true effect of zero. Decision-rule differences use the same simulated states and observations: subtract utilities within each replication before computing MCSE. Independently adding standard errors would discard that pairing.

## Assumptions and source limits

The lab sheets state the estimand, units, target population and horizon; data-generating process; estimator; uncertainty model; fixed thresholds; seed; replication count; and inferential error criterion or explicit loss/utility. Margins, costs and priors are teaching choices, not quantities established by the literature.

The primary evidence trail remains the [annotated readings](../papers/essential-readings.md), [power/selection concept](../wiki/concepts/power-selection.md), [decision concept](../wiki/concepts/decisions.md) and their paper notes. Their existing reading depths still apply. No new reference or additional source reading is claimed by these labs. Book coverage remains selected pp. 57–61 and 74–85; the expanded 187-paper matrix remains unrecovered. Wald remains metadata-only, and an abstract-only source cannot support an unread derivation. The mathematical derivations here are project illustrations with inspectable code.

The labs are deliberately bounded: known-SE normal models, a simple independent search, and risk-neutral binary decisions. They do not implement clustered panels, serially correlated market returns, realistic trading costs, endogenous selection, partial-identification bounds or minimax-regret optimisation. Follow [identification](../wiki/concepts/identification.md) and [uncertainty beyond sampling](../wiki/concepts/uncertainty-beyond-sampling.md) before translating an illustration into an empirical claim.

See the [simulation review](../reviews/2026-11-23-simulation-review.md). Successful computation is not scholarly approval, classroom validation or permission to generate slides.
