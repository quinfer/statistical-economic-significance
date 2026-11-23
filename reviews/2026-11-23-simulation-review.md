# Simulation lab review — 23 November 2026

**Decision: retain the three bounded, reproducible learning labs. The slide gate remains CLOSED and NOT PASSED.** The user requested labs, exercises and worked solutions, while expressly retaining source limitations and the slide hold. This is an implementation and teaching-content review, not human scholarly approval or an empirical replication.

## Material and reviewers

Three separately assigned AI agents developed the power, selection and decision labs. Each supplied code, an exercise sheet, a worked solution and tests. The parent agent integrated shared random streams, Monte Carlo summaries, output provenance, reference checks and the learning/wiki navigation, and reviewed the model equations and reference results.

The power agent then independently reviewed the common runner and the selection/decision implementations and prose. It checked selected normal-tail moments, decision expected utilities and second moments by numerical integration separate from the simulation loops. The selection agent independently reviewed the power formulas and boundary cases, decision derivations, source-depth wording and displayed analytical utilities. These reviews used the existing source notes; no new primary-source reading is claimed.

## Scope of the implemented experiments

| Lab | Reference design | Analytic checks and counterexamples |
|---|---|---|
| Power | 11 effect/sample-size, boundary and SE-misspecification scenarios | Test size/power, 95% coverage, TOST, joint classifications and positive meaningful-effect tests; precise negligible effects, uncertain consequential effects and understated SE |
| Selection | Four fixed-effect scenarios and one 20-candidate all-null search | Normal tail moments, Type S/M, null symmetry, independent holdout, family error and Bonferroni; strong effects and zero signed bias qualify blanket selection claims |
| Decisions | Six evaluation distributions, seven rules sharing each simulated state/estimate | Threshold utility, adoption, oracle regret and paired differences; matching-prior average optimum, prior mismatch and fixed-state ranking reversals |

The committed reference uses base seed **20261123** and **50,000 replications per scenario**. Python runtime, stable scenario seeds, code hashes, full design assumptions, unrounded metrics and analytic benchmarks are in [reference.json](../simulations/results/reference.json). CSV and Markdown views are generated from that record. No code or data from a cited empirical study is represented as replicated.

## Objections and resolutions

| Issue | Resolution |
|---|---|
| A cost-blind significance gate could make the decision comparison too narrow | Retained it as an explicitly labelled mechanical comparator and added a cost-aware one-sided confidence-bound rule. Its false-adoption probability is .05 at the break-even boundary under the stated normal model; its objective differs from expected-utility maximisation |
| Empty selected groups or zero true effects could produce misleading zero risks | Conditional empty groups are null; Type S/M at theta=0 are undefined; selected counts remain explicit |
| Zero observed rare events give a zero plug-in MCSE | Rates include Wilson intervals and exact benchmarks; mean tests use exact utility variance where rare-event sample variance is zero; worked solutions explain the limitation |
| Policy outcomes are dependent within replication | Utility and regret differences are computed within each replication before computing their MCSEs; tests check opposite signs and equal MCSEs |
| Floating-point Wilson endpoints could exclude an exact 0 or 1 by one rounding bit | Set the mathematically exact boundary endpoints explicitly and added regression checks before regenerating reference outputs |
| Individual 95% Monte Carlo intervals do not simultaneously cover a whole table | Power solution reports the two actual zero-rejection interval misses in the default run; neither seeds nor results were selected to remove them |
| Synthetic results could be confused with source findings or source access | Added an explicit [simulation evidence boundary](../wiki/evidence/simulation-labs.md); registries and paper reading-depth fingerprints remain unchanged |

## Verification and remaining limitations

The checks cover normal-model analytic agreement, seed reproduction, distinct scenario streams, selected denominators, undefined cases, paired comparisons, boundary calibration, invalid inputs and generated-report consistency. Tests also reject changed numerical reference values and stale Markdown views. The reference check reruns all 22 scenarios, checks implementation hashes and tolerates small platform floating-point differences while retaining the recorded runtime.

The source corpus remains 35 core works and 11 supporting/version records. Book coverage remains selected pp. 57–61 and 74–85; the expanded 187-paper matrix is still unrecovered. Existing abstract-only and metadata-only records remain so. No source PDFs, source full-text extracts or slide artefacts were added.

These labs do not establish classroom effectiveness, realistic financial return dependence, empirical identification, correct priors or social losses. They do not implement minimax-regret optimisation, robust Bayes or partial identification. Known-SE normal assumptions, independent search and risk-neutral binary decisions are deliberate simplifications; changing them requires a new design and validation. Review completion does not authorise slides.
