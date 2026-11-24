# Statistical and Economic Significance

A PhD self-study resource in applied statistics and econometrics for economics and finance. Start with a practical question. If an estimated effect clears an economic benchmark, what would you need before reporting that the true effect is worthwhile or recommending action?

## Start here

1. **Work through one result.** Check a lender’s confidence interval, change one input and explain which conclusion changes. [Quick start](QUICKSTART.md)
2. **Follow the five modules.** Each takes you from a chapter section to a concept or source in the wiki and then to a calculation or argument of your own. [Curriculum](CURRICULUM.md)
3. **Check your reasoning.** Attempt the task before opening its worked solution. Compare the assumptions and interpretation as well as the arithmetic. [Exercises](exercises/README.md) · [Simulation labs and solutions](simulations/README.md)

The [critical synthesis chapter](synthesis/critical-synthesis.md) develops the argument from defining a worthwhile effect to choosing an action under uncertainty. Use the [wiki](wiki/index.md) when you need to unpack a method or trace a claim to the passages consulted in a paper note. The [annotated readings](papers/essential-readings.md) and [learning map](resources/learning-map.md) help you find more material for a particular question.

## What you will do

| Module | What you will practise |
|---|---|
| [1. Magnitude, evidence and action](CURRICULUM.md#module-1-magnitude-evidence-and-action) | State what you want to estimate, what would count as a worthwhile effect, and what evidence a decision would need. |
| [2. Intervals and equivalence](CURRICULUM.md#module-2-intervals-meaningful-thresholds-and-equivalence) | Explain when an interval supports negligibility and when the estimate is too imprecise to decide. |
| [3. Power and selection](CURRICULUM.md#module-3-power-selection-and-noisy-magnitudes) | Compare what a design can detect with what a reader sees after results pass a reporting screen. |
| [4. Finance and identification](CURRICULUM.md#module-4-finance-identification-and-analysis-choices) | Work from gross alpha to net alpha, and assess assumptions that precision alone leaves unresolved. |
| [5. Decisions under uncertainty](CURRICULUM.md#module-5-decisions-under-uncertainty-and-the-capstone) | Write a decision memo and specify which evidence, priors or costs would change your recommendation. |

## Use the calculations

Begin by hand, or run the [deterministic worked examples](implementations/README.md) with Python 3.10 or later and its standard library. When you reach Module 3, use the seeded simulations to compare probabilities and expectations with their exact benchmarks. The calculations use synthetic inputs under stated models. The labs report Monte Carlo error for the simulated results. [Setup and first run](QUICKSTART.md#get-the-repository-and-run-the-examples) · [Simulation guide](simulations/README.md)

## Follow a claim to its evidence

The wiki labels attributed statements **Source claim** and the project’s reasoning **Project interpretation**. It also marks synthetic examples as **Illustration** and unresolved judgements as **Open question**. Check the paper note for the version, locator and reading depth. [Source catalogue](sources/literature-map.md) · [BibTeX](sources/references.bib) · [Targeted 2024–2026 update](sources/update-2024-2026.md)

The 2008 exchange is an optional case study in evaluating methodological disagreements. It pairs McCloskey and Ziliak’s critique with Hoover and Siegler’s response and gives you a way to audit one disputed claim. [Optional case study](CURRICULUM.md#optional-case-study-the-2008-debate)

The **slide gate is closed**. The project status records the remaining research and review work. [Status and limits](STATUS.md) · [Review gate](reviews/review-gate.md)

## Contribute and cite

Barry Quinn maintains this repository. The self-study structure draws on Quantitative Finance Foundations. Corrections with locators, rival interpretations and exercises that test assumptions are welcome. [Quantitative Finance Foundations](https://github.com/quinfer/quantitative-finance-foundations) · [Contributing guide](CONTRIBUTING.md) · [Research standards](AGENTS.md) · [Provenance](PROVENANCE.md)

Cite the repository with its commit and access date, and cite the original papers for substantive source claims. Original writing is CC BY 4.0 and original software is MIT licensed. Third-party works retain their own rights. [Citation details](CITATION.cff) · [Writing licence](LICENSE) · [Code licence](LICENSE-CODE)
