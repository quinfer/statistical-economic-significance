# Start with one result

A lender estimates that a programme reduces defaults. How would you tell whether the reduction is large enough to matter, whether the study supports that claim, and whether the lender should adopt the programme?

By the end of this session, keep one page with your checked calculation, three sentences answering those questions and one evidence trail. Estimates, standard errors and basic probability are enough to begin. You can work in your browser and calculate by hand.

## Your first study session

1. **Read the opening lending case and §1.** In your own words, say what the lender wants to learn and what an economic benchmark is for. If you come from economics or finance, start by naming the population, horizon and costs. If you come from statistics or computer science, translate the estimate and standard error into percentage points for these borrowers. [Chapter opening](synthesis/critical-synthesis.md) · [§1, Which claim are you trying to establish?](synthesis/critical-synthesis.md#1-which-claim-are-you-trying-to-establish) · [Economic significance concept note](wiki/concepts/economic-significance.md)
2. **Check a result by hand.** Work through the smaller-effect example below. Hold the estimate and the benchmark fixed, change the standard error and predict which inference will change. [Check one result by hand](#check-one-result-by-hand)
3. **Follow one claim into the wiki.** Trace what a p-value can tell you from the concept note to the ASA statement note. Write down one attributed source claim, the passages the project consulted and the recorded reading depth. If you work from the note, say so. If you consult the article, record the version and locator you used. [Statistical inference and p-values](wiki/concepts/statistical-inference.md) · [ASA statement note](wiki/papers/wasserstein-lazar-2016.md)
4. **Try the claim-map prompt in Exercise 1.** Write your three sentences before looking at the worked solution. Keep one sentence you revised and explain why. Return to the rest of the exercise in Module 1. [Exercise 1](exercises/01-magnitude-evidence-action.md)

## Check one result by hand

**Illustration.** Return to the same hypothetical lending question with a different estimate. The target is the average reduction in the one-year default rate among eligible borrowers. Positive values mean fewer defaults. The lender sets −1 and +1 percentage points as the limits of a negligible effect before seeing the results.

Assume the study identifies that average effect and gives an unbiased, normally distributed estimate with a known standard error. The estimate is 0.10 percentage points and its standard error is 0.02 percentage points. Look at the interval. Does it exclude zero? How far are its endpoints from the lender’s limits?

```text
0.10 ± 1.96 × 0.02 = [0.0608, 0.1392] percentage points
```

The 95% interval excludes zero, so the two-sided 5% test rejects a zero effect. To test practical equivalence at 5%, use a one-sided test at each limit. In this model the two tests use the endpoints of the central 90% interval, [0.0671, 0.1329] percentage points. Both endpoints lie strictly inside the limits. You therefore have evidence of a nonzero effect and evidence of equivalence under the stipulated margin.

Hold the estimate and the limits fixed. Raise the standard error to 0.10 percentage points. Predict which conclusion changes, then calculate both intervals.

<details>
<summary>Check your reasoning</summary>

The 95% interval widens to [−0.0960, 0.2960] percentage points and includes zero, so the two-sided 5% test no longer rejects zero. The 90% interval widens to [−0.0645, 0.2645] percentage points and still fits inside the fixed limits. The equivalence test still supports negligibility on that margin. The study is less precise, and the two questions still use different thresholds.

</details>

Write three sentences. Explain what would make the one-percentage-point margin defensible. Say what each version of the study supports about the magnitude of the reduction. Then name the programme costs and losses from default that you would need to value before recommending adoption. Check your answers against the chapter’s examples and the reproducible derivations. [Chapter §2, Evidence about the benchmark](synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Checked mathematical examples](wiki/evidence/mathematical-checks.md)

## Get the repository and run the examples

Use Python 3.10 or later and its standard library. The examples contain all the inputs they need. From a terminal:

```sh
git clone https://github.com/statistical-science-in-finance/statistical-economic-significance.git
cd statistical-economic-significance
python3 implementations/worked_examples.py
python3 scripts/check_integrity.py
```

If you already have a checkout, run the two Python commands from the top-level directory. In the worked output, look for the small, precise case and compare its 95% and 90% intervals with your notes. The code labels the effect units generically. For the lender, read the endpoints in percentage points. The integrity script checks the repository’s records and links. Assess the evidence for a citation or argument by following it to its source. [Implemented examples](implementations/README.md)

To run a Python snippet from an exercise, start `python3` from the top-level directory and paste the code at the Python prompt. Leave a blank line after an indented loop to run it. Use `exit()` to return to the terminal for commands such as the simulation runs below.

## Continue with the modules

Start with [Module 1](CURRICULUM.md#module-1-magnitude-evidence-and-action), then work through the [curriculum](CURRICULUM.md) in order. In Module 2, use the [interval and equivalence exercise](exercises/02-intervals-equivalence.md) to compare all four combinations of test outcomes. When a question needs more explanation, look it up in the [wiki](wiki/index.md) or follow its evidence route in the [learning map](resources/learning-map.md). The [exercise index](exercises/README.md) links each task to its chapter reading. For a reading group on contested claims, try the [optional debate case](CURRICULUM.md#optional-case-study-the-2008-debate).

When you reach Module 3, try the power lab. It uses random replications under a stated synthetic model and complements the deterministic calculations above. [Lab 1, Power and precision](simulations/labs/01-power.md) · [All simulation labs](simulations/README.md)

```sh
python3 simulations/run_labs.py --lab power --replications 50000 --seed 20261123 --output-dir scratch/power
```

Open `scratch/power/summary.md` and compare the estimated rates with their exact benchmarks and Monte Carlo standard errors. Varying the number of replications changes the precision of a simulated rate. Varying the sample size changes the study being simulated. Keep your own notes and experiment outputs in the ignored `scratch/` directory or outside the repository.

The [slide gate is closed](reviews/review-gate.md).
