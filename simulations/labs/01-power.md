# Lab 1 — power, precision and meaningful effects

**Illustration.** A precisely estimated £20 effect may be detectable and still lie inside a prespecified negligible region. A much larger true effect may be harder to establish as worthwhile in a smaller study. Predict which designs show those patterns, then check your predictions with synthetic repeated studies. Complete the two analytical exercises first. [Intervals and equivalence](../../exercises/02-intervals-equivalence.md) · [Analytical power exercise](../../exercises/03-power-selection.md) · [Chapter §2, Evidence about the benchmark](../../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark)

## Design before computation

The hypothetical target is the mean one-year policy effect in an eligible population, in **pounds per person per year**. Treat an effect measurement as `Yi ~ N(theta, 1000²)`, independently across people. The estimator is the sample mean. Instead of generating every individual, the program draws its exact distribution, `Xbar ~ N(theta, 1000²/n)`. This reduces computation without changing the stipulated sampling experiment. It does not simulate a complete causal study: unbiased effect measurement and identification are assumed.

The main grid crosses true effects £0, £20 and £200 with sample sizes 100, 2,500 and 100,000. The prespecified **teaching** equivalence margin is ±£100. It is not a measured welfare threshold. Reported SE equals £1,000/√n in the main grid. A boundary case uses theta = £100; a stress case reports half the true SE at theta = £0 and n = 2,500. The latter is a controlled uncertainty error, not a simulation of raw clustered or serially dependent observations.

| Quantity | Rule |
|---|---|
| Zero-null rejection | Reject `theta = 0` if `abs(Xbar/reported_SE) > z(.975)` |
| 95% interval coverage | Whether `Xbar ± z(.975)*reported_SE` contains the fixed true theta |
| Equivalence | Reject `theta ≤ −100 or theta ≥ 100` if the 90% interval lies strictly inside ±£100 |
| Positive beyond margin | Reject `theta ≤ 100` if the one-sided 95% lower bound exceeds £100 |
| Both / neither | Joint zero-test and equivalence-test classifications, not alternative estimands |

There is **no adoption decision or welfare loss function in this lab**. The error events are false zero-null rejection, false equivalence and interval noncoverage. Their economic costs are deliberately left unspecified; Lab 3 supplies an explicit decision problem.

## Reproduce the run

From the repository root, using Python 3.10 or later:

```sh
python3 simulations/run_labs.py --lab power --replications 50000 --seed 20261123 --output-dir scratch/power
```

Each scenario records its parameters, base seed, derived stream seed and 50,000 independent repeated studies. Scenario streams are derived from stable labels, so adding or reordering a scenario does not change another's random draws. The [code](../power.py), [reference JSON](../results/reference.json) and [reference summary](../results/summary.md) make the calculation inspectable. Reproduction with the same seed and runtime should agree; last-bit floating-point differences across platforms are not substantive differences.

For a simulated event rate `p_hat`, its plug-in Monte Carlo standard error is `sqrt(p_hat*(1−p_hat)/R)`. The reported Wilson interval concerns the **simulation event probability**, not theta. Zero observed events give a zero plug-in MCSE but do not establish a zero probability; inspect the Wilson upper bound and the exact benchmark. For an average estimated effect, MCSE is the standard deviation across repeated estimates divided by √R. Neither MCSE is the individual study's SE. Multiplying R by four reduces Monte Carlo noise by about half; increasing n changes the study design.

## Exercises

1. **Make predictions for the design.** Calculate the true SE for each n. For each effect and design, predict zero rejection, coverage and equivalence. Find where £20 should be detectable and still lie inside the chosen equivalence margin. Explain both judgements.
2. **Check the simulation against exact probabilities.** In `scratch/power/metrics.csv`, filter for `zero_rejection`. For all 11 scenarios, report the estimate, MCSE, Wilson interval and exact benchmark. Count the benchmarks outside their individual 95% intervals. What pattern of misses would prompt you to look at your simulation code? [Find a result in the output](../README.md#find-a-result-you-need)
3. **Compare the two targets.** For `meaningful_n100` and `small_n100000`, compare the rate of rejecting zero with the rate of supporting an effect above £100. Write two warranted interpretations of a single study and two that overreach.
4. **Reconstruct the four outcomes.** Use `both_reject`, `neither_reject`, `zero_rejection` and `equivalence`. At n = 100 check how wide the 90% interval is relative to the margin. Then explain what the boundary scenario tests.
5. **Change the reported uncertainty.** At n = 2,500 compare the calibrated and understated-SE null scenarios. Derive rejection and coverage in both. Explain what the stress case shows, and what you would have to investigate to diagnose an incorrect SE in real data.
6. **Vary repetitions and the margin separately.** Repeat at R = 200,000 with the same seed and compare Monte Carlo precision. Then use the code below to compare £100 with a £50 equivalence margin. Record that comparison as a sensitivity exercise and say what evidence would justify a margin specified in advance. [Chapter §4, Setting a margin worth testing](../../synthesis/critical-synthesis.md#setting-a-margin-worth-testing)

```python
from simulations.power import simulate_scenario

result = simulate_scenario(
    effect=20, sample_size=2500, margin=50,
    replications=50000, seed=20261123, scenario_id="margin50-small-n2500")
print(result["metrics"])
print(result["benchmarks"])
```

**Submit:** one operating-characteristics table with seed and R, the rejection and coverage derivations from task 5, and a 500-word design memo. State the estimand, units, horizon, identification assumption, benchmark justification, uncertainty model and what would change your recommendation. You may propose rejecting this model for a real application. [Worked solutions](../solutions/01-power.md) are available after your first attempt.

## Evidence links and limits

**Source claim:** the selected sections of [Lakens (2017)](../../wiki/papers/lakens-2017-equivalence.md), including its Figure 1 discussion, distinguish non-rejection from equivalence and describe their four joint outcomes. [Lakens (2022)](../../wiki/papers/lakens-2022-sample-size.md), also selected-section coverage, distinguishes meaningful effects from merely detectable ones. The [Hoenig–Heisey note](../../wiki/papers/hoenig-heisey-2001-power.md) is abstract-only and supports only the recorded broad distinction between prospective and flawed post-experiment power reasoning.

**Project interpretation:** these calculations supply a transparent normal-model illustration. They do not replicate those sources' empirical examples, verify unread proofs or upgrade any reading depth. The repository's [book](../../wiki/evidence/cult-2008-reading.md) remains selected passages only, and the expanded 187-paper matrix remains unrecovered. Neither source gap is resolved by generating synthetic draws. [The slide gate stays closed](../../reviews/review-gate.md).

[Lab index](../README.md) · [Worked solutions](../solutions/01-power.md)
