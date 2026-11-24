# Statistical and Economic Significance

A learning repository for PhD students in economics and finance: distinguish **how large an effect is, what the evidence supports, and what action is justified**.

Start with the [quick start](QUICKSTART.md), follow the [six-module curriculum](CURRICULUM.md), and use the [annotated readings](papers/essential-readings.md) alongside the [exercises](exercises/README.md). The structure follows [Quantitative Finance Foundations](https://github.com/quinfer/quantitative-finance-foundations), adapted to a research-led methodological course.

## What you will learn

- Define an estimand and an economic benchmark, with units, population, horizon and costs.
- Interpret intervals, power and equivalence without treating non-rejection as evidence of negligibility.
- Reconstruct the strongest competing positions in the McCloskey–Ziliak and Hoover–Siegler exchange.
- Audit a disputed claim without confusing coding arithmetic with validation of the original judgement.
- Distinguish sampling uncertainty from identification, selection and implementation risks in finance.
- Defend a decision under stated priors and losses, including evidence that would change the conclusion.

## Choose your starting point

| Background | Start here | Focus |
|---|---|---|
| Economics or finance | [Quick start](QUICKSTART.md), modules 1–2 | Units, intervals and hand-checking calculations |
| Statistics or programming | [Learning map](resources/learning-map.md), modules 1 and 5 | Estimands, welfare, identification and costs |
| Researching the controversy | [2008 exchange](wiki/disagreements/2008-exchange.md), [AER audit](sources/aer-audit/README.md), [synthesis](synthesis/critical-synthesis.md) | Which proposition each criticism challenges |

## Six modules

| Module | Central question | Deliverable |
|---|---|---|
| 1. Magnitude, evidence, action | Which judgement are we making? | Estimand and benchmark sheet |
| 2. Intervals and equivalence | Which relevant alternatives remain compatible? | Four-case interpretation table |
| 3. Power and selection | What happens when noisy results are selected? | Design and selection critique |
| 4. Debate and AER audit | Can you trace and challenge the evidence? | Bounded source-audit memo |
| 5. Finance and identification | What survives costs and assumptions? | Alpha interpretation and robustness plan |
| 6. Decisions under uncertainty | Which action follows under which losses? | Adversarial decision memo |

The [curriculum](CURRICULUM.md) supplies prerequisites, readings, tasks and readiness checks. Extend modules 2–3 and 6 with the [three simulation labs](simulations/README.md), each with exercises, worked solutions and a reproducible reference run. There is no requirement to accept the project's tentative conclusion.

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
| [Book ledger](wiki/evidence/cult-2008-reading.md) | Pages read and evidence from *The Cult of Statistical Significance* |
| [AER audit](sources/aer-audit/README.md) | Evidence behind disputed claims about how published papers used significance tests |
| [Status and limits](STATUS.md) | Research coverage, outstanding evidence gaps and the closed slide gate |
| [Review gate](reviews/review-gate.md) | Review decisions and evidence needed before developing slides |

The organising question is: **under what conditions can economic importance be defined, empirically supported, or acted upon without conventional significance testing—and what uncertainty or identification arguments are still needed?** Conclusions remain open to challenge in either direction.

## Contribute and cite

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md). Corrections with locators, rival arguments and exercises that expose assumptions are welcome. AI assistance and review limits are recorded in [PROVENANCE.md](PROVENANCE.md).

Maintained by **Barry Quinn**. Cite the repository with its commit and access date using [CITATION.cff](CITATION.cff); cite underlying papers for substantive claims. Original writing is [CC BY 4.0](LICENSE); original software is [MIT licensed](LICENSE-CODE). Third-party works retain their own rights; their full texts are linked rather than redistributed.
