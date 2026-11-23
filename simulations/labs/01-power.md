# Lab 1 — power, precision and meaningful effects

**Illustration: synthetic data, not a study of an actual programme.** This lab asks what repeated samples can tell us about zero effects, economically relevant magnitudes and an uncertainty model. Complete [intervals and equivalence](../../exercises/02-intervals-equivalence.md) and the [analytical power exercise](../../exercises/03-power-selection.md) first.

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

1. **Predict before running.** For each effect and n, calculate the true SE and predict zero rejection, interval coverage and equivalence. Identify a design where £20 is detectable and lies inside the chosen equivalence margin. Explain why those two descriptions are compatible.
2. **Audit simulation error.** Tabulate the simulated zero-rejection probability, its MCSE and Wilson interval, and the exact benchmark for all 11 scenarios. Count how many benchmark values lie outside their individual 95% intervals. Explain why requiring every such interval to contain its target would be an unsuitable correctness rule.
3. **Separate uncertainty from importance.** Compare `meaningful_n100` with `small_n100000`. Compare their zero-rejection rates with the rates of supporting a positive effect above £100. Write two conclusions that would be defensible after a single study and two that would not.
4. **Four outcomes.** Use `both_reject`, `neither_reject`, `zero_rejection` and `equivalence` to recover all four joint test outcomes. Explain why equivalence failure at n = 100 is uninformative about whether theta actually falls inside the margin. What does the boundary scenario test?
5. **Break calibration deliberately.** Compare the calibrated and understated-SE null scenarios at n = 2,500. Derive both their rejection and coverage probabilities. Explain why the stress case demonstrates the consequence of incorrect uncertainty without establishing a particular cause in real data.
6. **Separate R from n.** Repeat the run at R = 200,000 with the same seed. Compare Monte Carlo precision, then use the custom API below to change the equivalence margin from £100 to £50. Do not choose the margin after inspecting the output and call it preregistered. State what substantive evidence a real margin would need.

```python
from simulations.power import simulate_scenario

result = simulate_scenario(
    effect=20, sample_size=2500, margin=50,
    replications=50000, seed=20261123, scenario_id="margin50-small-n2500")
print(result["metrics"])
print(result["benchmarks"])
```

**Submit:** one operating-characteristics table with seed and R, the two analytic derivations, and a 500-word design memo. State the estimand, units, horizon, identification assumption, benchmark justification, uncertainty model and what would change your recommendation. You may propose rejecting this model for a real application. [Worked solutions](../solutions/01-power.md) are available after your first attempt.

## Evidence links and limits

**Source claim:** the selected sections of [Lakens (2017)](../../wiki/papers/lakens-2017-equivalence.md), including its Figure 1 discussion, distinguish non-rejection from equivalence and describe their four joint outcomes. [Lakens (2022)](../../wiki/papers/lakens-2022-sample-size.md), also selected-section coverage, distinguishes meaningful effects from merely detectable ones. The [Hoenig–Heisey note](../../wiki/papers/hoenig-heisey-2001-power.md) is abstract-only and supports only the recorded broad distinction between prospective and flawed post-experiment power reasoning.

**Project interpretation:** these calculations supply a transparent normal-model illustration. They do not replicate those sources' empirical examples, verify unread proofs or upgrade any reading depth. The repository's [book](../../wiki/evidence/cult-2008-reading.md) remains selected passages only, and the expanded 187-paper matrix remains unrecovered. Neither source gap is resolved by generating synthetic draws. [The slide gate stays closed](../../reviews/review-gate.md).

[Lab index](../README.md) · [Worked solutions](../solutions/01-power.md)
