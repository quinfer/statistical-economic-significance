# Start with one result

A small p-value does not say whether an effect would matter. A large estimate does not say how well its magnitude is known. Start by separating those two questions, then ask what a decision would require.

This repository combines a research wiki with a self-study pathway. The learning activities are proposed exercises, not a validated course. The [research review gate](reviews/review-gate.md) remains closed for slides.

## Choose an entry route

**Coming from economics or finance?** Start with a question you recognise: whether a policy benefit exceeds its cost, or whether a return predictor could improve an investment decision. Write down the target quantity, units, population and horizon. Use [Module 1](CURRICULUM.md#module-1-magnitude-evidence-and-action) to separate importance, evidence and action before adding statistical machinery.

**Coming from statistics or programming?** Start with the same question, but focus on what the numbers represent. A standardised coefficient, a percentage-point change, a gross return and a welfare gain answer different questions. Use [Module 1](CURRICULUM.md#module-1-magnitude-evidence-and-action) to translate a calculation into an economic claim before extending the code.

Both routes use the same five core modules. Use the [optional debate case study](CURRICULUM.md#optional-case-study-the-2008-debate) for a reading group on interpreting contested claims.

## What you need

| Preparation | Enough to begin | Learn or revisit as needed |
|---|---|---|
| Statistics | Estimates, standard errors and a normal distribution | Test inversion, power and conditional selection |
| Economics or finance | One question about benefits, costs or returns | Welfare, identification and implementability |
| Programming | Run a Python file and read its output | Functions, assertions and numerical checks |
| Research practice | Distinguish an author's statement from your interpretation | Trace evidence to specific passages and versions |

The initial calculations use Python 3.10 or later and its standard library. No downloaded dataset, paid package, account or notebook service is needed. Some primary readings require library access; the notes state what this project actually consulted.

## Get the repository and run the examples

```sh
git clone https://github.com/statistical-science-in-finance/statistical-economic-significance.git
cd statistical-economic-significance
python3 implementations/worked_examples.py
python3 scripts/check_integrity.py
```

If you already have a checkout, run the last two commands from its top-level directory. The worked examples are synthetic, model-conditional calculations. They are not estimates from an actual market or policy. The integrity check checks the repository's source records and links; it cannot certify that a citation is true or that an argument is sound.

## Check one result by hand

**Illustration.** A lender wants to know whether a new programme makes an economically meaningful difference to defaults. The target is the average reduction in the one-year default rate among eligible borrowers. Positive values mean fewer defaults. Before seeing the results, the lender sets −1 and +1 percentage points as the limits of a negligible effect for this exercise.

Suppose the study identifies that average effect and gives an unbiased, normally distributed estimate with a known standard error. The estimate is 0.10 percentage points and the standard error is 0.02 percentage points. Look at the 95% confidence interval. Does it exclude zero? How far do its endpoints lie from the lender's limits?

```text
0.10 ± 1.96 × 0.02 = [0.0608, 0.1392] percentage points
```

The 95% interval excludes zero, so the two-sided 5% test rejects a zero effect. To test practical equivalence at 5%, check each of the lender's limits with a one-sided test. Those tests use the two endpoints of the central 90% interval, [0.0671, 0.1329] percentage points. Both endpoints lie strictly inside the limits, so the data also support practical equivalence for this margin.

Now keep the estimate and the lender's limits fixed, and raise the standard error to 0.10 percentage points. Before you calculate, predict which conclusion changes. Then calculate both intervals and explain what the wider intervals tell you about the evidence.

<details>
<summary>Check your reasoning</summary>

The 95% interval widens to [−0.0960, 0.2960] percentage points and now includes zero. The 90% interval widens to [−0.0645, 0.2645] percentage points and still fits inside the fixed limits. The test against zero no longer rejects at 5%. The equivalence test still supports the conclusion that the effect is within the limits.

</details>

Write three sentences:

1. What would make the lender's margin of one percentage point defensible?
2. What does each version of the study tell you about the size of the effect?
3. What would you need to know about programme costs and losses from default before recommending a decision?

Try the [interval and equivalence exercise](exercises/02-intervals-equivalence.md) next, or see the [checked mathematical examples](wiki/evidence/mathematical-checks.md) for the assumptions behind these calculations.

## Your first study session

1. Read [economic significance](wiki/concepts/economic-significance.md) and complete [Exercise 1](exercises/01-magnitude-evidence-action.md).
2. Run the examples and check one interval by hand. Record the inputs, units and assumptions beside the output.
3. Follow one claim from a [concept note](wiki/index.md) to a paper note and then to its recorded source locator. Record the reading depth; a verified reference is not necessarily a fully read paper.
4. Write down one conclusion you would revise if the standard error, identification assumption or cost changed.

Keep your answers in your own notes. A useful first deliverable is one page containing the three-sentence interpretation, the checked calculation and one evidence trail.

Continue with the [curriculum](CURRICULUM.md), or use the [learning map](resources/learning-map.md) to find a particular concept or disagreement.

## Extend a calculation into a simulation

The [simulation labs](simulations/README.md) add power, selection bias and decision-rule comparisons, with separate worked solutions. Begin with:

```sh
python3 simulations/run_labs.py --lab power --replications 50000 --seed 20261123 --output-dir scratch/power
```

Open `scratch/power/summary.md` and compare each Monte Carlo estimate with its analytic benchmark and MCSE. Changing the number of replications improves simulation precision; it does not change the sample size of a simulated study. Use [Lab 1](simulations/labs/01-power.md) to make that distinction explicit.
