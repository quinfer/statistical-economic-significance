# Annotated reading pathways

This guide maps the **35-work verified core** to the six modules in the [curriculum](../CURRICULUM.md). It is a teaching selection and ordering, not a new bibliography or an exhaustive review. The [generated catalogue](../sources/literature-map.md) and [registry](../sources/registry.json) remain authoritative for source identity, versions and reading coverage. Each linked paper note supplies primary-source URLs and the evidence trail.

**Project interpretation.** The prompts below suggest what to examine and compare. They are not additional empirical findings. Attributed claims, exact consulted locators and their limits are recorded in the linked notes. Reading a note is not a substitute for reading its source, and a result reported by an author is not independently established by its inclusion here.

## A first learning sequence

Begin with the named notes and inspect their consulted passages where access permits. Use the other entries in each module to test your initial interpretation; completing this sequence does not complete the corpus review.

1. **Magnitude, evidence, action:** Wasserstein–Lazar (2016), then Imbens (2021). Write three different questions that the phrase *economic significance* might conceal.
2. **Uncertainty and equivalence:** Greenland and colleagues (2016), then Lakens (2017). Explain how a finding can be distinguishable from zero yet compatible with practical negligibility.
3. **Power and selection:** Gelman–Carlin (2014), then Lakens (2022). State the external effect-size assumptions needed for an informative design calculation.
4. **The historical dispute:** read all three 2008 exchange notes in order, then the bounded book and AER audit notes. Separate arguments about practice from arguments about inference.
5. **Finance and identification:** compare Harvey–Liu–Zhu (2016) with Jensen–Kelly–Pedersen (2023), then Deaton–Cartwright (2018). Identify which definitions or assumptions could reconcile apparently conflicting conclusions.
6. **Decisions:** compare Kandel–Stambaugh (1996), Manski (2019) and the 2026 robust Bayes article. Specify the choice criterion before recommending an action.

The coverage column describes **the project's existing reading**, not how much you are expected to read. `selected_sections_read` can mean a bounded selection of full text or indexed passages; the note states which. `abstract_read` and `metadata_only` entries identify substantial remaining reading work. All statuses below reflect the registry checked on 24 October 2026; this guide does not certify later versions or new access.

## 1. Magnitude, evidence and action

Use the [concept note](../wiki/concepts/economic-significance.md), [competing positions](../wiki/disagreements/methodological-positions.md) and [module exercise](../exercises/01-magnitude-evidence-action.md).

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Wasserstein and Lazar (2016)](../wiki/papers/wasserstein-lazar-2016.md), *The ASA Statement on p-Values* | `selected_sections_read`; published statement and contextual editorial. Indexed passages only; direct full-page access was blocked. | Principle 6 and contextual sections 4–5: what does a p-value leave unspecified about importance and scientific reasoning? Do not infer that every subsequent reform proposal is ASA policy. |
| [Imbens (2021)](../wiki/papers/imbens-2021.md), *Statistical Significance, p-Values, and the Reporting of Uncertainty* | `abstract_read`; published article. Detailed examples remain unread. | The abstract's distinction between decision problems and questions naturally addressed by a null test. What would justify retaining a test in your application? |
| [Cohen (1994)](../wiki/papers/cohen-1994.md), *The Earth Is Round (p < .05)* | `abstract_read`; published article, conservatively classified after extraction failed. | The abstract's proposed changes to practice. Separate a criticism of dichotomous interpretation from a claim that sampling uncertainty is irrelevant. Do not reconstruct unread arguments from the title. |
| [Wasserstein, Schirm and Lazar (2019)](../wiki/papers/wasserstein-schirm-lazar-2019.md), *Moving to a World Beyond “p < 0.05”* | `selected_sections_read`; editorial, pp. 1–4 inspected. | The status notice on p. 1 and sections 2, 3.1–3.2: distinguish the editors' own proposal from the official 2016 statement. Would moving a binary rule to an interval boundary resolve their objection? |
| [Benjamin and colleagues (2018)](../wiki/papers/benjamin-et-al-2018.md), *Redefine statistical significance* | `abstract_read`; published Comment. Numerical and Bayes-factor arguments are not audited. | The abstract's proposal to change the default threshold for new discoveries. Formulate its strongest defence and identify which costs or power consequences require further reading. |
| [Amrhein, Greenland and McShane (2019)](../wiki/papers/amrhein-greenland-mcshane-2019.md), *Scientists rise up against statistical significance* | `selected_sections_read`; published Comment, selected passages pp. 305–307. | The discussion of practical implications and interval limits on pp. 306–307. Distinguish ending categorical claims from banning p-values; retain the stated exception for specialised decision applications. |
| [McShane and colleagues (2019)](../wiki/papers/mcshane-etal-2019-abandon.md), *Abandon Statistical Significance* | `selected_sections_read`; final article, opening pp. 235–236. | Which other evidence would accompany continuously interpreted statistical information? Treat implementation benefits as a proposal to assess, not a demonstrated outcome of reform. |

**Discussion:** What would a defender of calibrated testing accept in the reform arguments, and what would remain disputed? Record the answer against [C005: threshold reforms](../wiki/claims/C005-threshold-reforms.md).

## 2. Uncertainty, intervals and equivalence

Use the [intervals](../wiki/concepts/intervals.md) and [equivalence](../wiki/concepts/equivalence.md) notes, the [equivalence audit](../wiki/disagreements/equivalence-audit.md) and the [module exercise](../exercises/02-intervals-equivalence.md).

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Greenland and colleagues (2016)](../wiki/papers/greenland-et-al-2016.md), *Statistical tests, P values, confidence intervals, and power* | `selected_sections_read`; published open-access essay. | “Moving from tests to estimates” and misconceptions 19–25: separate procedure coverage, parameter probability and the practical meaning of interval limits. State the model and selection assumptions that remain. |
| [Morey and colleagues (2016)](../wiki/papers/morey-et-al-2016-intervals.md), *The fallacy of placing confidence in confidence intervals* | `selected_sections_read`; abstract and introduction only. Online 2015, issue year 2016. | The introductory objection to common interpretations of realised intervals. Which claim follows from coverage alone? The detailed counterexamples and proposed alternatives still require reading. |
| [Neyman (1937)](../wiki/papers/neyman-1937-estimation.md), *Outline of a Theory of Statistical Estimation…* | `metadata_only`; published article identity verified, no substantive theoretical section read. | A historical reading assignment: obtain the confidence-interval section and reconstruct its probability statement. This project's record currently supports bibliographic identity, not an attributed theoretical result. |
| [Schuirmann (1987)](../wiki/papers/schuirmann-1987-tost.md), comparison of TOST and the power approach | `abstract_read`; published article. Proofs and examples not audited. | The abstract's relation between two one-sided tests and a 1−2α interval. Identify assumptions before using that relation; bioavailability limits do not supply economic margins. |
| [Lakens (2017)](../wiki/papers/lakens-2017-equivalence.md), *Equivalence Tests: A Practical Primer* | `selected_sections_read`; published repository copy, introduction, “Testing for Equivalence” and Figure 1 discussion. | Figure 1's four combinations of difference and equivalence conclusions. Give each an interpretation in annual pounds per person, with an independently justified margin. Source formulas and software have not yet been independently audited. |
| [Lakens, Scheel and Isager (2018)](../wiki/papers/lakens-scheel-isager-2018.md), *Equivalence Testing for Psychological Research* | `selected_sections_read`; indexed discussion and margin-justification sections of the published article. | The “Subjective justification” discussion: what changes if the bounds are chosen after seeing the estimates? Distinguish prespecification from a persuasive substantive justification. |
| [Fitzgerald (2025)](../wiki/papers/fitzgerald-2025-equivalence.md), *The Need for Equivalence Testing in Economics* | `selected_sections_read`; author-hosted working paper dated 8 December 2025. Author-linked v2 DOI is verified, but an exact deposit match is not. | Compare p. 22 on failed equivalence with p. 34 on generic audit margins. Does an inadequately supported null claim establish that the true effect is large? Do not describe this working paper as a verified journal publication or its reanalysis as this project's replication. |

**Discussion:** Choose a margin before viewing the illustrative estimate, explain its units and consequences, and give a case where reasonable decision makers would disagree about it. Relate the result to [C003: negligibility](../wiki/claims/C003-equivalence.md).

## 3. Power, selection and noisy magnitudes

Use the [power and selection note](../wiki/concepts/power-selection.md), [C006: noisy magnitudes](../wiki/claims/C006-noisy-magnitudes.md) and the [module exercise](../exercises/03-power-selection.md).

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Gelman and Carlin (2014)](../wiki/papers/gelman-carlin-2014.md), *Beyond Power Calculations* | `selected_sections_read`; published article, selected design-analysis sections and discussion. | “Our Recommended Approach to Design Analysis”: identify the conditioning event in Type S and Type M quantities. Explain why a large selected estimate does not itself provide a credible design effect. Their computations and examples are not replicated here. |
| [Gelman and Stern (2006)](../wiki/papers/gelman-stern-2006.md), *The Difference Between “Significant” and “Not Significant”…* | `selected_sections_read`; author-hosted published article, pp. 328–329 and parts of examples. | Section 2's comparison of estimates: which contrast should be tested, and what covariance information would it require? Read the title as “not necessarily significant”, not a claim that the contrast can never be significant. |
| [Hoenig and Heisey (2001)](../wiki/papers/hoenig-heisey-2001-power.md), *The Abuse of Power* | `abstract_read`; published article, detailed variants unread. | The abstract's distinction between prospective power and post-experiment power used to interpret non-rejection. What extra information does reusing the observed estimate supply? Detailed derivations remain an assignment. |
| [Lakens (2022)](../wiki/papers/lakens-2022-sample-size.md), *Sample Size Justification* | `selected_sections_read`; published open-access article. | “Six Approaches to Justify Sample Sizes”, interesting effect sizes and value of information: compare power, precision and resource constraints for one feasible study. Avoid treating a detectable effect as automatically important. |

**Discussion:** Defend a design under a plausible range of effects, then identify a range under which its conclusions would be uninformative. Keep design calculations separate from claims about the true effect in an already completed study.

## 4. The 2008 exchange and the AER coding audit

Start with the [matched exchange](../wiki/disagreements/2008-exchange.md), then use the [audit exercise](../exercises/04-aer-source-audit.md). The exchange and the book have different reading histories: the rejoinder explicitly says the book was unavailable when the responses were written.

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Hoover and Siegler (2008), *Sound and fury*](../wiki/papers/hoover-siegler-2008-sound.md) | `full_text_read`; published article, pp. 1–37 including notes and references. | The loss-sensitive weak-signal discussion on p. 15 and corpus caveat in note 21. Present the strongest inference defence, then check the local mathematical objections in the evidence trail. Full reading does not validate all cited cases or historical claims. |
| [McCloskey and Ziliak (2008), *Signifying nothing*](../wiki/papers/mccloskey-ziliak-2008-reply.md) | `full_text_read`; published reply, pp. 39–55 including notes and references. | Use the linked reading ledger to locate substantive judgement, power and considered p levels. Which position is stronger than a blanket rejection of statistical reasoning? Original case classifications and harm claims need separate verification. |
| [Hoover and Siegler (2008), rejoinder](../wiki/papers/hoover-siegler-2008-rejoinder.md) | `full_text_read`; published rejoinder, pp. 57–68. | Compare p. 59's question about whose losses govern scientific evidence with pp. 60–61 on model-based inference. Inspect the project's objection to the p-value formulation on p. 58 as well. |
| [Ziliak and McCloskey (2008), *The Cult of Statistical Significance*](../wiki/papers/ziliak-mccloskey-2008-cult.md) | `selected_sections_read`; authorised preview of published book pp. 57–61, 74–85. Separate prepublication preface is not assumed identical. | Compare p. 60's balancing argument with the survey extension on p. 80 and Table 7.1. The book has **not** been fully read; these excerpts do not verify its historical or practical-harm claims. |
| [McCloskey and Ziliak (1996)](../wiki/papers/mccloskey-ziliak-1996.md), *The Standard Error of Regressions* | `selected_sections_read`; published JEL article, selected pp. 101–111 with visual checks. | Table 1 and the questionnaire: why are “discusses size” and “uses more than statistical significance decisively” different items? These are author classifications, not an independently established prevalence of misuse. |
| [Ziliak and McCloskey (2004)](../wiki/papers/ziliak-mccloskey-2004.md), *Size matters* | `selected_sections_read`; final JSE pp. 527–535, 540–542; selected separately paginated EJW material also read. | Final JSE Table 5, p. 542, alongside the [version check](../wiki/evidence/jse-2004-version-check.md). Distinguish reproducing an aggregate, resolving a table discrepancy and validating an individual code. |

The application papers are **supporting sources**, not extra core works. Follow the [final Darby audit](../wiki/evidence/darby-final-followup.md) and [final Bernheim–Wantz audit](../wiki/evidence/bernheim-wantz-final-followup.md) to their separate source records. Darby's final article has complete-text reading; Bernheim–Wantz has selected empirical and concluding coverage, with theory pages still unread. Neither exercise replicates the underlying data analysis.

Keep three objects distinct in the [coding audit](../wiki/evidence/aer-coding-audit.md): the original **137-paper** 1990s matrix, the book's expanded **187-paper** survey, and **author–paper** totals with coauthors repeated. The [expanded-matrix search](../wiki/evidence/expanded-matrix-followup.md) did not recover the 187-paper matrix. A checked denominator or arithmetic total cannot establish whether a disputed code is justified.

**Discussion:** Produce two memos about one case: the strongest defensible coding criticism and the strongest defensible response. End with what the surviving evidence can and cannot settle about profession-wide practice.

## 5. Finance, identification and competing replication diagnoses

Use the [finance](../wiki/concepts/finance.md), [identification](../wiki/concepts/identification.md) and [uncertainty beyond sampling](../wiki/concepts/uncertainty-beyond-sampling.md) notes with the [module exercise](../exercises/05-finance-identification.md).

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Harvey, Liu and Zhu (2016)](../wiki/papers/harvey-liu-zhu-2016-cross-section.md), *… and the Cross-Section of Expected Returns* | `abstract_read`; published article. | The abstract's multiple-search argument. Specify the research family and selection process before treating any proposed hurdle as transferable to your study. Detailed calculations have not been assessed here. |
| [McLean and Pontiff (2016)](../wiki/papers/mclean-pontiff-2016-predictability.md), *Does Academic Research Destroy Stock Return Predictability?* | `abstract_read`; published article. | Separate out-of-sample and post-publication comparisons in the abstract. Which observations could distinguish statistical selection from investors learning? No quantitative decay estimates are verified in this resource. |
| [Harvey and Liu (2020)](../wiki/papers/harvey-liu-2020-false-missed.md), *False (and Missed) Discoveries in Financial Economics* | `selected_sections_read`; final article, opening pp. 2503–2505. | The opening discussion of false versus missed discoveries and their costs. Identify the chosen definition of manager skill; the double-bootstrap implementation is not independently audited. |
| [Jensen, Kelly and Pedersen (2023)](../wiki/papers/jensen-kelly-pedersen-2023-replication.md), *Is There a Replication Crisis in Finance?* | `selected_sections_read`; published article, selected model and replication discussion. | Compare replication definitions, risk adjustment, sample construction and the hierarchical model with the earlier critique. A more favourable diagnosis is conditional on these choices; the complete implementation and supplements remain unreviewed. |
| [Menkveld and colleagues (2024)](../wiki/papers/menkveld-etal-2024-nonstandard-errors.md), *Nonstandard Errors* | `selected_sections_read`; published article, selected sections I.A, I.C, II.D and III. | Section II.D and the discussion of analyst dispersion: what varies when analysts receive the same data? Dispersion alone does not identify bias or supply a quantity to add mechanically to a sampling standard error. |
| [Deaton and Cartwright (2018)](../wiki/papers/deaton-cartwright-2018-rcts.md), *Understanding and misunderstanding randomized controlled trials* | `selected_sections_read`; selected indexed passages from the published article, sections 1–3. | Separate unbiasedness, precision and extrapolation. Which extra assumptions connect a study's estimate to a target policy population? The authors' criticism is not a general rejection of randomised trials. |

**Discussion:** A strategy can pass a statistical screen yet fail after costs or outside its estimation setting. Explain which question each reading helps address, and which questions require additional identification, market or decision evidence. Do not claim that this repository establishes a profitable strategy.

## 6. Decisions under uncertainty and the capstone

Use the [decisions note](../wiki/concepts/decisions.md), [C002: action without rejection](../wiki/claims/C002-action-without-rejection.md), [C010: uncertainty and choice](../wiki/claims/C010-uncertainty-and-choice.md) and [capstone exercise](../exercises/06-decision-memo.md).

| Reading | Existing coverage and version | One passage or distinction to inspect |
|---|---|---|
| [Kandel and Stambaugh (1996)](../wiki/papers/kandel-stambaugh-1996-asset-allocation.md), *On the Predictability of Stock Returns: An Asset-Allocation Perspective* | `abstract_read`; published article. | The abstract's distinction between conventional evidence strength and allocation under Bayesian learning. Specify prior beliefs, investor preferences and parameter uncertainty before proposing an application; this is not an inference-free result. |
| [Manski (2019)](../wiki/papers/manski-2019-treatment-choice.md), *Treatment Choice With Trial Data* | `selected_sections_read`; indexed abstract and section 3 passages of the published article. Direct full text was blocked. | Section 3's combination of error probabilities and welfare losses through regret. Identify the benchmark for regret. The exposition concerns medical trials; it is not an empirical economics finding. |
| [Manski (2021)](../wiki/papers/manski-2021-econometrics-decisions.md), *Econometrics for Decision Making* | `abstract_read`; published article superseding a 2019 draft. | The abstract's distinction between model space and feasible state space. What would fail if a decision were evaluated only under a convenient model? Methods and examples still require full reading. |
| [Aradillas Fernández and colleagues (2026)](../wiki/papers/aradillas-fernandez-etal-2026-robust-bayes.md), *Robust Bayes Treatment Choice with Partial Identification* | `selected_sections_read`; published FirstView article, 23 July 2026; final HTML controls, not earlier arXiv versions. | Sections 2.1–2.3, Assumption 1 and conclusion: compare ex ante and ex post criteria under the stated prior class and partial-identification model. Proofs are unread; do not generalise randomisation or optimality beyond the framework. |
| [Wald (1950)](../wiki/papers/wald-1950-decision-functions.md), *Statistical Decision Functions* | `metadata_only`; first-edition book identity verified. No book content read. | A historical extension assignment: obtain the book and locate a decision rule, loss function and risk definition. No theoretical proposition in this project is attributed to the unread book merely because it is foundational. |

**Capstone prompt:** Give an empirical assessment and an action recommendation separately. State uncertainty, identification assumptions, the feasible actions, consequences, criterion and sensitivity. Then construct a defensible rival recommendation. Explain whether disagreement concerns the evidence, the target population or the value assigned to outcomes.

## Continue the research

The [2024–2026 update](../sources/update-2024-2026.md) documents a targeted search, not exhaustive contemporary coverage. The [search log](../sources/search-log.md) preserves exclusions and unresolved candidates. Do not upgrade a source's reading depth after reading only this guide, and do not count an earlier draft as a new independent contribution.

Submit a reading memo with the exact consulted version and locator, a labelled source claim, your interpretation, the strongest objection and the remaining limit. Check it against the [critical synthesis](../synthesis/critical-synthesis.md) rather than treating that synthesis as a settled answer. The [review gate](../reviews/review-gate.md) remains closed for slides.
