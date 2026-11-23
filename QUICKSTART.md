# Start with one result

A small p-value does not say whether an effect would matter. A large estimate does not say how well its magnitude is known. Start by separating those two questions, then ask what a decision would require.

This repository combines a research wiki with a self-study pathway. The learning activities are proposed exercises, not a validated course. The [research review gate](reviews/review-gate.md) remains closed for slides.

## Choose an entry route

**Coming from economics or finance?** Start with a question you recognise: whether a policy benefit exceeds its cost, or whether a return predictor could improve an investment decision. Write down the target quantity, units, population and horizon. Use [Module 1](CURRICULUM.md#module-1-magnitude-evidence-and-action) to separate importance, evidence and action before adding statistical machinery.

**Coming from statistics or programming?** Start with the same question, but focus on what the numbers represent. A standardised coefficient, a percentage-point change, a gross return and a welfare gain answer different questions. Use [Module 1](CURRICULUM.md#module-1-magnitude-evidence-and-action) to translate a calculation into an economic claim before extending the code.

Both routes use the same six modules. You can work through them alone or use the questions for a reading group.

## What you need

| Preparation | Enough to begin | Learn or revisit as needed |
|---|---|---|
| Statistics | Estimates, standard errors and a normal distribution | Test inversion, power and conditional selection |
| Economics or finance | One question about benefits, costs or returns | Welfare, identification and implementability |
| Programming | Run a Python file and read its output | Functions, assertions and numerical checks |
| Research practice | Distinguish an author's statement from your interpretation | Source versions, passage locators and coding audits |

The initial calculations use Python 3.10 or later and its standard library. No downloaded dataset, paid package, account or notebook service is needed. Some primary readings require library access; the notes state what this project actually consulted.

## Get the repository and run the examples

```sh
git clone https://github.com/quinfer/statistical-economic-significance.git
cd statistical-economic-significance
python3 implementations/worked_examples.py
python3 scripts/check_integrity.py
```

If you already have a checkout, run the last two commands from its top-level directory. The worked examples are synthetic, model-conditional calculations. They are not estimates from an actual market or policy. The integrity check checks the repository's source records and links; it cannot certify that a citation is true or that an argument is sound.

## Check one result by hand

**Illustration.** Suppose an estimate is 0.10 percentage points with a known standard error of 0.02 percentage points. Under the stated normal model, an approximate 95% confidence interval is:

```text
0.10 ± 1.96 × 0.02 = [0.0608, 0.1392] percentage points
```

The interval excludes zero. If a defensible negligibility region had been set at −1 to +1 percentage points, this same estimate could also support equivalence under the compatible TOST procedure. Standard TOST at 5% uses a 90% interval; calculate that interval separately rather than silently substituting 95%. The margin must be justified before it becomes an economic conclusion. The [interval and equivalence exercise](exercises/02-intervals-equivalence.md) develops the comparison, and the [checked mathematical examples](wiki/evidence/mathematical-checks.md) record the underlying assumptions.

Write three sentences:

1. What magnitude would matter, and to whom?
2. What does this estimate and uncertainty model support?
3. What additional information would you need before choosing an action?

Do not add a policy or trading recommendation to this deliberately incomplete example.

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
