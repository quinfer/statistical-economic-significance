# A learning pathway through significance

An economic argument needs a quantity that matters, evidence about that quantity and a reason for choosing an action. Those requirements overlap, but none supplies the others automatically. This pathway uses calculations, source criticism and decision memos to make their relationships explicit.

Work through the six modules in order on a first pass. Each produces something you can discuss or revise: a claim map, an interval table, a design analysis, an audit ledger, an application assessment and a decision memo. The pathway is self-paced and provisional; it does not claim assessed learning outcomes or a completed empirical replication. Slides remain on hold under the [review gate](reviews/review-gate.md).

## Preparation and entry routes

Begin with the [quick start](QUICKSTART.md). Familiarity with estimates, standard errors, probability and one economic or financial application is enough to begin. Later modules introduce selection, identification and decision criteria; follow the linked concept notes when those terms are unfamiliar.

- **Economics and finance route:** keep one application throughout. Define its estimand and economic threshold first, then use the calculations to test how much your conclusion depends on precision and assumptions.
- **Statistics and programming route:** begin with the normal-model calculations, then translate every input and output into natural units. Ask which population, horizon and action the calculation could inform.

Neither route permits skipping source criticism. A correct calculation applied to the wrong target or an inaccurately reported paper does not support the intended conclusion.

## Module 1: Magnitude, evidence and action

**Question:** what exactly are you claiming when you call a result economically significant?

Read [economic significance](wiki/concepts/economic-significance.md), [C001: independence](wiki/claims/C001-independence.md) and the paper note for the [ASA statement](wiki/papers/wasserstein-lazar-2016.md). Use the paper note's locator and access record for any statement attributed to the ASA.

**Work:** complete [Exercise 1](exercises/01-magnitude-evidence-action.md). For a policy or finance question, distinguish a meaningful benchmark, a description of what was observed, a claim about an unknown effect and a choice of action. Specify units, population, horizon, aggregation and whose gains or losses count. Construct two contexts in which the same estimated effect would have different importance.

**Deliverable:** a one-page claim map with those four kinds of statement and the additional premises each requires. Mark invented examples as **Illustration** and your arguments as **Project interpretation**.

**Before moving on:** you can explain why statistical significance does not set an economic threshold, why a large estimate may be uncertain, and why acting is different from certifying a population effect. You can identify a descriptive finite-population question for which sampling extrapolation is unnecessary, while preserving measurement concerns.

## Module 2: Intervals, meaningful thresholds and equivalence

**Question:** what evidence would distinguish a negligible effect from an imprecisely estimated one?

Read [intervals](wiki/concepts/intervals.md), [equivalence](wiki/concepts/equivalence.md), [Lakens's tutorial note](wiki/papers/lakens-2017-equivalence.md) and [C011: meaningful-effect tests](wiki/claims/C011-nested-meaningful-tests.md). For a contemporary challenge, follow the [equivalence audit](wiki/disagreements/equivalence-audit.md) to the Fitzgerald working-paper note; its reading and replication limits remain relevant.

**Work:** complete [Exercise 2](exercises/02-intervals-equivalence.md). Compare a small precise estimate, a large imprecise estimate and an estimate near zero. Report an interval, a zero-null comparison and a justified equivalence margin separately. Change the margin while holding the estimate fixed, then change the standard error while holding the margin fixed. Explain which question each change alters.

**Deliverable:** an annotated table in natural units, with interval levels, hypotheses and margins stated. Include a paragraph on why failure to establish equivalence is not evidence that the effect lies outside the margin.

**Before moving on:** you can distinguish confidence coverage from posterior probability; state why conventional 5% TOST uses a compatible 90% interval; and explain the restricted implication from a lower bound above a positive meaningful threshold to a lower bound above zero. You do not treat that implication as a universal requirement for action.

## Module 3: Power, selection and noisy magnitudes

**Question:** when does selecting an impressive result make its estimated magnitude less trustworthy?

Read [power and selection](wiki/concepts/power-selection.md), the [Gelman–Carlin note](wiki/papers/gelman-carlin-2014.md) and the [Hoenig–Heisey note](wiki/papers/hoenig-heisey-2001-power.md). The latter currently has abstract-level support in this repository; do not attribute unread details to it.

**Work:** complete [Exercise 3](exercises/03-power-selection.md). Specify a plausible effect externally to the focal estimate, a sampling model and a selection rule. Compare unconditional accuracy with accuracy conditional on passing that rule. Consider both false discoveries and missed useful effects. Use the executable examples where applicable and keep analytical calculations separate from any extension using random draws.

**Deliverable:** a design-analysis note identifying the estimand, plausible alternatives, standard errors, selection condition and risks of sign or magnitude error. Explain why calculating power from the same observed estimate cannot independently resolve uncertainty about that estimate.

**Before moving on:** you can say which alternative a power number refers to and which population of results a conditional error measure describes. If you add a simulation, declare the data-generating process, seed, number of repetitions and Monte Carlo error. Do not call a deterministic calculation a simulation.

## Module 4: Read the disagreement and audit its evidence

**Question:** which propositions do the participants in the 2008 exchange actually dispute, and what would settle a coding disagreement?

Start with the [matched 2008 exchange ledger](wiki/disagreements/2008-exchange.md). Follow its passages to the three paper notes: [Hoover–Siegler's article](wiki/papers/hoover-siegler-2008-sound.md), [McCloskey–Ziliak's reply](wiki/papers/mccloskey-ziliak-2008-reply.md) and the [rejoinder](wiki/papers/hoover-siegler-2008-rejoinder.md). These are separate from the [book reading ledger](wiki/evidence/cult-2008-reading.md), which records selected excerpts and access limits.

**Work:** complete [Exercise 4](exercises/04-aer-source-audit.md). Reconstruct each side's strongest claim and concession before judging either. Select one disputed AER case and follow the version-specific evidence. Separate checking arithmetic, establishing source provenance and judging whether a questionnaire item measures the alleged practice.

**Deliverable:** a two-sided argument ledger plus a short audit record: proposition, source/version, locator, original code or claim, contrary evidence, your provisional judgement and what remains unresolved. Use the [coding audit](wiki/evidence/aer-coding-audit.md) and [expanded-matrix follow-up](wiki/evidence/expanded-matrix-followup.md) to mark the boundary of what can be reproduced.

**Before moving on:** you can distinguish the original 137-paper matrix from the expanded 187-paper survey, paper counts from author-paper rows, and arithmetic reproduction from coding validation. You can explain why finding a magnitude in a paper does not settle every selection or interpretation issue, and why a negative questionnaire answer does not always show an absence of magnitude reasoning.

## Module 5: Finance, identification and analysis choices

**Question:** when could a precise estimate still answer the wrong economic question?

Read [finance](wiki/concepts/finance.md), [identification](wiki/concepts/identification.md), [uncertainty beyond sampling](wiki/concepts/uncertainty-beyond-sampling.md) and [C008: finance replication](wiki/claims/C008-finance-replication.md). Follow the competing papers through their notes, checking reading depth before drawing conclusions. Use the [Menkveld et al. note](wiki/papers/menkveld-etal-2024-nonstandard-errors.md) to examine analysis choices without assuming that analyst dispersion automatically measures bias.

**Work:** complete [Exercise 5](exercises/05-finance-identification.md). Trace a proposed predictor or intervention from the estimated coefficient to an economically relevant target. For finance, distinguish gross returns, risk adjustment, costs, implementation constraints and investor utility. For policy, distinguish association, causal identification, target population and welfare. Identify where a narrow standard error leaves an important assumption untested.

**Deliverable:** an application assessment with an estimand table, a chain of identifying and implementation assumptions, and one sensitivity analysis. Compare two apparently conflicting research claims only after checking whether their samples, targets and procedures are comparable.

**Before moving on:** you can explain how a result can be precisely estimated yet poorly identified or difficult to transport. You can distinguish a reproducible calculation from an independently replicated empirical result and an implementable strategy from an attractive in-sample return.

## Module 6: Decisions under uncertainty and the capstone

**Question:** what can justify an action when the evidence has not established a materially positive effect?

Read [decisions under uncertainty](wiki/concepts/decisions.md), [C002: action without rejection](wiki/claims/C002-action-without-rejection.md), the [Manski treatment-choice note](wiki/papers/manski-2019-treatment-choice.md) and the [critical synthesis](synthesis/critical-synthesis.md). For further challenge, consult the [robust Bayes note](wiki/papers/aradillas-fernandez-etal-2026-robust-bayes.md) within its recorded selected-section scope.

**Work:** complete [Exercise 6](exercises/06-decision-memo.md). Specify feasible actions, uncertain states, consequences and a decision criterion. Use a synthetic normal-model example to compare a zero-null test with a decision based on posterior expected net benefit. Vary a cost or prior. Then discuss how a justified uncertainty set or a minimax-regret criterion could change the question; do not claim to implement a method you have only described.

**Deliverable:** a decision memo with a concise recommendation conditional on stated assumptions, the evidential claim kept separate, sensitivity analysis, the strongest objection, an evidence trail and a condition that would change your conclusion. Include a short appendix assessing whether the repository's synthesis should be retained, narrowed or revised.

**Before completing the pathway:** you can defend a rational action without presenting it as proof of an effect. You can also identify settings in which a meaningful-effect certification entails rejecting zero under a compatible procedure. You recognise that a loss function, prior or uncertainty set needs justification; choosing one does not make disagreement disappear.

## Review your work

Ask a reader to trace one substantive statement to a source and one numerical statement to a calculation. A good submission states the target, assumptions and limitations; represents an opposing view fairly; preserves unresolved evidence; and says what would change its conclusion. Agreement with the present synthesis is not a completion criterion.

Use the [learning map](resources/learning-map.md) to revisit gaps and the [research standards](AGENTS.md) before proposing an addition. Finishing these activities does not clear the slide gate or certify the literature review as complete.
