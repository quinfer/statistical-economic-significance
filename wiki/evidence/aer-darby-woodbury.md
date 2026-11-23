# AER case audit: Darby and Woodbury–Spiegelman

**Status:** bounded primary-source audit, 24 October 2026, by the `inference_sources` research agent. This is neither a replication nor a human review approval. These are supporting materials outside the 35-source core. The slide gate remains closed.

**Project interpretation:** These cases do not establish a clean victory for either side. Woodbury and Spiegelman plainly discuss economics and policy contingencies; their categorical subgroup wording remains vulnerable. Darby's published article is now directly read: it combines statistical model selection with substantive coefficient calculations. The [final-version follow-up](darby-final-followup.md) supersedes the earlier access limit while preserving unresolved selection and identification questions.

## Sources and actual reading coverage

| Material | Verified identity and consulted version | Reading coverage |
|---|---|---|
| Michael R. Darby (1984), “The U.S. Productivity Slowdown: A Case of Statistical Myopia” | *American Economic Review* 74(3):301–322; [JSTOR issue record](https://www.jstor.org/stable/i304558), [NBER publication cross-reference](https://www.nber.org/papers/w1018). Published DOI not verified. | **Full text read after user-supplied JSTOR download:** printed pp. 301–322 including footnotes, appendix and references; selected visual checks. Independent visual checks of pp. 310–311 and 315 by root and debate_sources. See [exact coverage](darby-final-followup.md). No empirical replication. |
| Darby (1982), same title | [NBER Working Paper 1018](https://www.nber.org/system/files/working_papers/w1018/w1018.pdf), November 1982; manuscript dated 15 October 1982; DOI 10.3386/w1018. | **Selected sections read:** cover/abstract, printed p. 1, pp. 15–22, p. 26, notes on pp. 38–39, Tables 6–7 on pp. 45–46. Visually checked p. 17 and Table 6. This is a draft, not the 1984 article. |
| Stephen A. Woodbury and Robert G. Spiegelman (1987), “Bonuses to Workers and Employers to Reduce Unemployment: Randomized Trials in Illinois” | *American Economic Review* 77(4):513–530; [Upjohn institutional record](https://research.upjohn.org/jrnlarticles/126/); published text in [Woodbury's public author upload](https://www.researchgate.net/publication/4980344_Bonuses_to_Workers_and_Employers_to_Reduce_Unemployment_Randomized_Trials_in_Illinois). DOI not verified. | **Selected sections read:** abstract, p. 515 sample design/size, pp. 523–524 subgroup discussion, Table 7 p. 525 including notes, Table 8 p. 526 and accompanying discussion, benefit–cost section pp. 527–528 and conclusion pp. 528–529. Reading used extracted published text with printed headers, not a downloaded PDF or complete paper. Table 6 was not recovered reliably. |

The ResearchGate header says February 1987; its reproduced journal cover and the institutional citation identify the September 1987 issue. The journal imprint controls. Download failures are recorded below rather than concealed by a full-text-reading label.

Comparison texts: [McCloskey–Ziliak 1996](../papers/mccloskey-ziliak-1996.md), printed pp. 104, 107–108, read directly from the published scan and visually checked; [Hoover–Siegler 2008](../papers/hoover-siegler-2008-sound.md), pp. 8–10 and note 6 p. 32; [McCloskey–Ziliak's reply](../papers/mccloskey-ziliak-2008-reply.md), pp. 46–48. The latter exchange was previously read in full. See also the [2008 disagreement record](../disagreements/2008-exchange.md).

## Darby: model selection and substantive interpretation are separate questions

**Source claims.** MZ 1996 p. 104 criticises Darby's coefficient reasoning and ambiguous use of significance, while acknowledging that his findings do not turn on regressions. H&S pp. 8 and 32 instead describes substantive growth calculations following a test-based specification exercise and a robustness comparison. MZ 2008 pp. 46–47 challenges that exercise itself.

**Direct draft evidence.** Darby 1982 pp. 17–18 uses Table 6's tests to exclude oil-price terms, then converts a price-control coefficient into annual growth adjustments. Equation (14) nevertheless retains regressors with small t statistics. Page 26 compares a second coefficient and supplies an economic explanation for its difference. Page 21 distinguishes explaining changes in growth from assessing influences on its trend level.

**Project interpretation — what favours H&S.** In the accessible draft, regression magnitudes actually enter the economic argument. Calling the entire exercise indifferent to magnitude would miss the calculation. Moreover, retention of statistically weak controls means it is not a universal algorithm deleting every insignificant coefficient. A specification decision can pursue identification, parsimony or prediction without asserting that an omitted variable has no economic consequence anywhere. The relevant causal and measurement rationale should be assessed directly.

**Project interpretation — what favours MZ.** Calculating magnitudes after selecting a model does not automatically validate selection or the uncertainty subsequently attached to those magnitudes. Dropping a term because a zero restriction was not rejected does not establish that its contribution lies inside an economically negligible region. The substantive target would need a threshold in productivity-growth units and uncertainty about its contribution, including model uncertainty. This is a defensible criticism of an inferential step; it is stronger than alleging that Darby never reasons economically.

The draft's oil-price conclusion moves from weak tests towards a substantive-sounding absence claim. Its later warning about trend-level influences qualifies the overall interpretation but does not itself establish negligible short-run oil effects. Conversely, the mere use of F tests does not prove that the resulting estimates are biased or inconsistent. Those properties require assumptions about the data-generating process, omitted variables, selection rule and asymptotic framework.

**Final-version check.** The [supplied published article](darby-final-followup.md) now verifies the contested passages directly. Final equation (12), p. 311, retains contemporaneous employment growth with t = 0.31 while Table 6's restrictions exclude oil-price terms. Multiplying the price-control coefficient 0.04691 by 0.7857 gives approximately 0.0369 log points of estimated 1973 overstatement; the article applies annual growth adjustments of approximately −0.46 and +0.61 percentage points to 1965–1973 and 1973–1979 respectively. These are model-based calculations, not verified true corrections. Page 310, n. 24, also explains that the draft's layoff variable lost data coverage after 1981: the version change must not be attributed solely to statistical insignificance.

Final p. 315 compares 0.04691 with 0.0312 and explains the approximately 0.016 difference economically despite reporting that it is not statistically significant. This verifies the substance of Hoover–Siegler's magnitude defence. Their confidence-interval-containment explanation in n. 6 remains a reconstruction, not a reported covariance-aware test in Darby. Darby's n. 39 tests equality across control/decontrol periods within regressions, not equality between the coefficients in equations (12) and (16). Neither a non-rejection nor one estimate lying within another's interval establishes equivalence. Final p. 317 also distinguishes not explaining variation from being economically unimportant.

The draft's equation (14) and horizon ending in 1978 are now demonstrably different from final equation (12) and its 1979 horizon. Their numerical details are kept version-specific. Direct final reading strengthens the rejection of blanket magnitude-neglect or universal insignificant-variable deletion allegations, while leaving the particular oil-price restriction and subsequent uncertainty assessment open to criticism.

## Woodbury–Spiegelman: economic analysis with an overstrong subgroup claim

**Source evidence, compact ledger.** The author-uploaded published text reports the following Employer Experiment benefit–cost estimates (Table 7, p. 525; extracted text, not visually verified; standard errors use a Taylor approximation):

| Population | Ratio | Standard error |
|---|---:|---:|
| Overall | 4.29 | 2.90 |
| White women | 7.07 | 2.95 |
| Black women | 24.65 | 34.06 |

Page 515 ties sample size to a policy-relevant response. Page 527 tests ratios against zero, says the treatment “affected only white women”, and calls for further understanding. Pages 527–529 discuss displacement and changing take-up: with complete take-up but unchanged benefit reductions, the overall Employer ratio would be 0.53. Table 8 p. 526 suppresses decompositions for insignificant bonus-receipt differences. These are the authors' calculations and claims, not replicated findings.

**Project interpretation — the strongest defence.** The cost calculations, scale-up scenario and distinction between state savings and net social benefits contradict a reading that the authors simply ignored economic considerations. Uncertain external validity and possible changes in programme participation are economically pertinent reasons to qualify a recommendation. The conditional scenario also shows why a favourable trial point estimate is not an automatic forecast for permanent policy. It is a scenario, however, not evidence that complete take-up would actually occur. H&S is persuasive about the presence of substantive economic reasoning; its categorical dismissal of any logical problem goes too far.

**Project interpretation — the strongest criticism.** A rejection within one subgroup and non-rejections elsewhere do not establish that the treatment works exclusively in the first subgroup. This applies to the original wording and to H&S p. 9 when differences in significance are used to support distinct underlying populations. A contrast of treatment effects, with its joint uncertainty, addresses heterogeneity. Establishing that only one subgroup benefits additionally requires evidence that effects elsewhere are absent or negligibly small. Differences in actual bonus receipt or take-up are informative mechanisms but are not identical to differences in causal effects on unemployment or state savings. Because Table 6 was not recovered reliably and the separate detailed report was not read, this audit does not claim that no relevant contrast was ever examined.

The suppressed decompositions provide a more specific example of significance filtering than a global claim of economic illiteracy. Whether their omission materially changes an economic conclusion remains to be established; a small, uncertain contrast might still be worth displaying alongside its uncertainty.

**Project interpretation — the decision criterion.** Testing whether a benefit–cost ratio differs from zero is not testing fiscal break-even. If the measured benefits and costs were complete, break-even would be one; with omitted administration costs or spillovers, even that calculation needs adjustment. Nor must a rational decision-maker demand rejection of either null. Expected utility or another explicit criterion can favour action under considerable uncertainty, depending on the consequences of action and delay. A large estimate alone does not supply that criterion or a posterior distribution.

MZ 1996 pp. 107–108 reasonably insists that the noisy overall estimate deserves discussion, but infers a categorical judgement of policy uselessness that the surrounding economic discussion does not support. MZ 2008 p. 47 focuses on Black women; that subgroup must not be confused with the overall 4.29 estimate. Its own ratio is much less precise, as the ledger shows. Saying a subsidy *would* save a specified amount requires a stronger empirical claim than reporting an estimated ratio. Neither the original paper nor this audit establishes that a particular policy decision caused foregone employment; that would require a separate history and counterfactual analysis.

## Access log and remaining tests

All attempts below occurred on 24 October 2026:

- Published PDFs at `https://www.jstor.org/stable/pdf/1804009.pdf` and `https://www.jstor.org/stable/pdf/1814528.pdf` returned HTTP-success **Client Challenge HTML**, not PDF files. The Darby stable landing page yielded no article text; its issue contents verified metadata.
- Upjohn's record was retrieved and its full-text link points to JSTOR 1814528, rather than providing a locally hosted PDF.
- Woodbury's ResearchGate page was readable through web extraction and identifies the material as author-uploaded. Direct page download and the linked PDF returned 403; the web PDF-opening attempts failed/cache-missed. The extracted text therefore remains the basis of the bounded published-source reading, with no visual verification of Tables 6–7.
- The NBER landing page initially failed through the web opener (403), but public terminal retrieval of the landing page and PDF succeeded. Metadata and the draft's version/date were checked directly.
- The cited UCLA 1983 working-paper URL `http://www.econ.ucla.edu/workingpapers/wp304.pdf` returned 404. No 1983-text reading is claimed.
- Hoover's public McCloskey source-directory index was unavailable through the web opener but retrieved through the terminal. It contained debate/survey files, not either original AER article.

**Open questions.** Audit Darby’s identification, selection uncertainty and economically relevant oil-effect bounds; visually verify the published Woodbury tables, recover Table 6, and examine any reported interaction or equality tests in the detailed experiment report. A later numerical audit should specify the estimand, account for ratio-denominator uncertainty and distinguish trial assignment effects from a scaled programme. No new survey scores, population misuse rate or empirical replication follows from these two targeted cases.

Links: [economic significance](../concepts/economic-significance.md), [power and selection](../concepts/power-selection.md), [decisions](../concepts/decisions.md).

**Access update:** The earlier failures above describe the public-search phase. The user subsequently downloaded the final Darby article through JSTOR; its identity, checksum and complete reading coverage are recorded in the [final follow-up](darby-final-followup.md). The original search failures are retained as history, not current access limits.
