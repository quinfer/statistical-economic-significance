# Exercises: evidence, importance and action

These six exercises turn the [learning route](../CURRICULUM.md) into a sequence of research products: a claim map, an interval report, a design analysis, a documentary audit, a finance interpretation and a decision memo. They can be completed individually or discussed in a PhD reading group. Attempt each task before opening its self-check.

| Exercise | Main question | Submission |
|---|---|---|
| [01. Magnitude, evidence and action](01-magnitude-evidence-action.md) | What exactly would “economically significant” mean here? | Claim map and a 300-word argument |
| [02. Intervals and equivalence](02-intervals-equivalence.md) | What does the evidence establish relative to a meaningful margin? | Results table and interpretation |
| [03. Power and selection](03-power-selection.md) | What can a design detect, and what changes after selection? | Power table and design note |
| [04. AER source audit](04-aer-source-audit.md) | Which claims survive arithmetic and passage-level scrutiny? | Reproduction table and evidence ledger |
| [05. Finance and identification](05-finance-identification.md) | Which estimated return is relevant to which decision? | Gross/net report and identification critique |
| [06. Decision memo](06-decision-memo.md) | Can a justified choice precede a decisive effect claim? | A reproducible policy memo with sensitivity analysis |

**Illustration:** every numerical policy or finance scenario in these exercises is synthetic. Normal-model calculations are deterministic, with no random draws, seed or Monte Carlo error. Their assumptions are stated in each sheet. The AER exercise instead reproduces arithmetic on documented historical coding artefacts; reproducing those counts does not validate the codes or the underlying papers.

Use Python 3.10 or later and the standard library from the repository root. The [worked examples](../implementations/worked_examples.py) and [normal-model functions](../implementations/normal_model.py) support the calculations; the [quick start](../QUICKSTART.md) explains the entry points. You may instead calculate by hand or in another language if you record the formulas, inputs and rounding. Keep personal responses in `scratch/`, which Git ignores, or outside the repository. Do not replace the research notes with exercise answers.

For each submission:

1. Separate the estimand, estimate, uncertainty model, identifying assumptions and decision criterion.
2. State units, population, horizon and any economic margin, cost or welfare weight.
3. Mark substantive statements **Source claim**, **Project interpretation**, **Illustration** or **Open question**. Link source claims to an existing paper note and a checked locator; report your own reading depth honestly.
4. Give the strongest objection to your preferred interpretation and identify evidence that would change it.

The self-checks establish arithmetic and the intended distinctions. They do not impose a single preference ordering or resolve the historical debate. A well-supported disagreement with the [working synthesis](../synthesis/critical-synthesis.md) is an acceptable outcome.

These are learning materials, not slides. The [slide gate remains closed](../reviews/review-gate.md), and completing the exercises does not alter it.

## Simulation extensions

After the deterministic exercises, use the [power lab](../simulations/labs/01-power.md), [selection lab](../simulations/labs/02-selection.md) and [decision lab](../simulations/labs/03-decisions.md). Each has a separate worked solution, a fixed-seed reference run and explicit Monte Carlo error. Their synthetic experiments extend the learning tasks; they do not validate the historical coding or upgrade any source's reading depth.
