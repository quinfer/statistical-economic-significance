# Exercises: evidence, importance and action

Use the exercises to put the chapter’s arguments to work. Read the linked section, make a prediction and attempt the tasks before opening the worked solution. The five core exercises follow the [learning route](../CURRICULUM.md) and work for self-study or a PhD reading group.

| Exercise | Read in the chapter | Submission |
|---|---|---|
| [Magnitude, evidence and action](01-magnitude-evidence-action.md) | [§1, Which claim are you trying to establish?](../synthesis/critical-synthesis.md#1-which-claim-are-you-trying-to-establish) | Claim map and a 300-word argument |
| [Intervals and equivalence](02-intervals-equivalence.md) | [§2, Evidence about the benchmark](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) | Results table and interpretation |
| [Power and selection](03-power-selection.md) | [§2, Estimates after selection](../synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) and [§3, Power near the null](../synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) | Power table and design note |
| [Finance and identification](05-finance-identification.md) | [§4, Comparing analyses of the same data](../synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data) | Gross/net report and identification critique |
| [Decision memo](06-decision-memo.md) | [§5, Action under uncertainty](../synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty) | A reproducible policy memo with sensitivity analysis |

**Illustration:** every numerical policy or finance scenario in the core exercises is synthetic. Normal-model calculations are deterministic, with their assumptions stated in each sheet.

The optional source audit takes you through one disputed classification and the arithmetic of the historical survey. [AER source audit](04-aer-source-audit.md) · [Chapter appendix](../synthesis/critical-synthesis.md#appendix-auditing-claims-about-research-practice)

Use Python 3.10 or later and the standard library from the repository root. The [worked examples](../implementations/worked_examples.py) and [normal-model functions](../implementations/normal_model.py) support the calculations; the [quick start](../QUICKSTART.md) explains the entry points. You may instead calculate by hand or in another language if you record the formulas, inputs and rounding. Keep personal responses in `scratch/`, which Git ignores, or outside the repository. Do not replace the research notes with exercise answers.

For each submission:

1. Separate the estimand, estimate, uncertainty model, identifying assumptions and decision criterion.
2. State units, population, horizon and any economic margin, cost or welfare weight.
3. Mark substantive statements **Source claim**, **Project interpretation**, **Illustration** or **Open question**. Link source claims to an existing paper note and a checked locator; report your own reading depth honestly.
4. Give the strongest objection to your preferred interpretation and identify evidence that would change it.

Use the worked solutions to check the arithmetic and the step from calculation to interpretation. In your own argument, say which assumptions you accept and where you would defend a different conclusion. [Critical synthesis chapter](../synthesis/critical-synthesis.md)

The [slide gate is closed](../reviews/review-gate.md).

## Simulation extensions

After the deterministic exercises, use the [power lab](../simulations/labs/01-power.md), [selection lab](../simulations/labs/02-selection.md) and [decision lab](../simulations/labs/03-decisions.md). Each has a separate worked solution, a fixed-seed reference run and explicit Monte Carlo error. Their synthetic experiments extend the learning tasks; they do not validate the historical coding or upgrade any source's reading depth.
