# Statistical and Economic Significance

A PhD learning resource on applied statistics and econometrics for economics and finance. Learn to distinguish **how large an effect is, what the evidence supports, and what action is justified**.

Start with the [quick start](QUICKSTART.md), follow the [five core modules](CURRICULUM.md), and use the [annotated readings](papers/essential-readings.md) alongside the [exercises](exercises/README.md). The structure follows [Quantitative Finance Foundations](https://github.com/quinfer/quantitative-finance-foundations), adapted for self-study in statistical methods.

## What you will learn

- Define an estimand and an economic benchmark, with units, population, horizon and costs.
- Interpret estimates, confidence intervals and hypothesis tests under their assumptions. Use equivalence tests when the question is practical negligibility.
- Evaluate what a design can detect and how selecting results affects estimated signs and magnitudes.
- Distinguish sampling uncertainty from identification, selection and implementation risks in finance.
- Defend a decision under stated priors and losses, including evidence that would change the conclusion.

## Choose your starting point

| Background | Start here | Focus |
|---|---|---|
| Economics or finance | [Quick start](QUICKSTART.md), modules 1–2 | Units, intervals and hand-checking calculations |
| Statistics or programming | [Learning map](resources/learning-map.md), modules 1 and 4 | Estimands, identification and costs |

## Five core modules

| Module | Central question | Deliverable |
|---|---|---|
| 1. Magnitude, evidence, action | Which judgement are we making? | Estimand and benchmark sheet |
| 2. Intervals and equivalence | Which relevant alternatives remain compatible? | Four-case interpretation table |
| 3. Power and selection | What happens when noisy results are selected? | Design and selection critique |
| 4. Finance and identification | What survives costs and assumptions? | Alpha interpretation and robustness plan |
| 5. Decisions under uncertainty | Which action follows under which losses? | Adversarial decision memo |

The [curriculum](CURRICULUM.md) supplies prerequisites, readings, tasks and readiness checks. The [three simulation labs](simulations/README.md) cover power, selection and decisions under uncertainty. Each has exercises, worked solutions and a reproducible reference run.

## Run the examples

Python 3.10 or later; no third-party packages are needed. From the repository root:

```sh
python3 implementations/worked_examples.py
python3 simulations/run_labs.py --lab all --replications 50000 --seed 20261123
python3 scripts/check_all.py
```

The [worked examples](implementations/README.md) use **synthetic inputs and deterministic normal-model calculations**. The [simulation labs](simulations/README.md) add random replications with fixed seeds, analytic benchmarks and reported Monte Carlo error. Neither is evidence about actual policies or markets. Every lab states its assumptions, target and limitations.

## Follow a claim to its evidence

The [wiki](wiki/index.md) connects paper notes, concepts, claims, disagreements and evidence ledgers. Notes distinguish **Source claim**, **Project interpretation**, **Open question** and **Illustration**. Attribution records what an author says; it does not settle whether the author is right.

| Resource | Purpose |
|---|---|
| [Source catalogue](sources/literature-map.md) and [BibTeX](sources/references.bib) | Verified identity, version and reading/access limits |
| [Critical synthesis](synthesis/critical-synthesis.md) | Empirical support versus action, with objections and counterexamples |
| [2024–2026 update](sources/update-2024-2026.md) | Targeted search recorded on 24 October 2026; not exhaustive coverage |
| [Optional case study](CURRICULUM.md#optional-case-study-the-2008-debate) | Compare McCloskey and Ziliak’s critique with Hoover and Siegler’s response and audit a disputed claim |
| [Status and limits](STATUS.md) | Research coverage, outstanding evidence gaps and the closed slide gate |
| [Review gate](reviews/review-gate.md) | Review decisions and evidence needed before developing slides |

The organising question is **how should an empirical researcher estimate and communicate an economically meaningful effect, and what evidence and assumptions justify acting on it?**

## Contribute and cite

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Corrections with locators, rival arguments and exercises that expose assumptions are welcome. AI assistance and review limits are recorded in [PROVENANCE.md](PROVENANCE.md).

Maintained by **Barry Quinn**. Cite the repository with its commit and access date using [CITATION.cff](CITATION.cff); cite underlying papers for substantive claims. Original writing is [CC BY 4.0](LICENSE); original software is [MIT licensed](LICENSE-CODE). Third-party works retain their own rights; their full texts are linked rather than redistributed.
