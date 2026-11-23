# Close reading: McCloskey and Ziliak (2008), reply

**Status:** complete reading of this article; source-fidelity notes and provisional critical analysis. This is not independent verification of its historical, empirical or causal assertions, review of the entire exchange, or approval of the synthesis or slide gate.

**Citation:** McCloskey, Deirdre N., and Stephen T. Ziliak. 2008. “Signifying nothing: reply to Hoover and Siegler.” *Journal of Economic Methodology* 15(1): 39–55. DOI: 10.1080/13501780801913413.

## Reading and provenance record

- Reader: `inference_sources`; access and reading date: 2026-10-24.
- Primary document: [author/institution-hosted published PDF](https://bpb-us-e1.wpmucdn.com/blogs.roosevelt.edu/dist/b/153/files/2019/04/Signifying-nothing-reply-to-Hoover-and-Siegler-2a8q87a.pdf).
- Local temporary copy: `/tmp/significance-2008-reply.pdf`; SHA-256: `8ecdd0c2cbee257412483caba2b4e204f6340333959a152d05f5fd43d00d8614`.
- The PDF has a publisher download cover and 17 article pages. Cover and every extracted article page were read, including all seven notes and the complete reference list. `pypdf` extracted non-empty text from every page. Reading was sequential, in groups ending at printed pp. 43,48,53,55; none of those tool outputs was truncated. Printed pagination was checked in the extracted headers/footers. Rendered printed pp. 43,50,52 were additionally inspected visually to check the most consequential passages against extraction.
- Coverage: printed pp. 39–52 contain the abstract and argument; p. 53 concludes the argument, contains notes 1–7 and starts references; pp. 54–55 finish references. All were read. No appendix, table or external supplement forms part of this PDF. Sources cited inside the article were not thereby read.
- Secondary [author HTML](https://www.deirdremccloskey.com/articles/stats/sig.php) was consulted for its header, abstract and opening passages, not treated as the controlling text. Its header gives 39–57, whereas the published PDF establishes 39–55. Wording also differs in places; do not transfer unpaginated HTML wording into a quotation attributed to the published PDF without checking.
- Initial shell download failed because sandbox DNS resolution was unavailable; the authorised escalated public download succeeded. Web PDF screenshots returned cache misses; local `pdfplumber` rendering succeeded. Neither failure indicates source inaccessibility or paywall status.
- The public PDF remains in `/tmp` for checking, not in the repository. Recommended registry depth: `full_text_read`, explicitly scoped to this reply alone.

## Compact evidence ledger

Every entry below is an **attributed source claim**, not a project endorsement. Locators are printed pages.

| ID | Pages | Attributed position or concession |
|---|---|---|
| R01 | 39,41 | Rejects thresholds as necessary or sufficient for importance. |
| R02 | 41–43 | Prioritises non-sampling error and context-dependent accuracy. |
| R03 | 43 | Allows considered p levels with power in relevant cases. |
| R04 | 43 | Also separates sampling precision categorically from effect magnitude. |
| R05 | 45 | Acknowledges survey omissions and index-weighting difficulties. |
| R06 | 45–46 | Defends coding access arrangements; declines detailed reconstruction. |
| R07 | 46–48 | Challenges significance-led specification, not every reporting of magnitudes. |
| R08 | 49 | Defends immediate action under imperfect information. |
| R09 | 49–50 | Questions superpopulation reasoning; labels a realised time-series sample size one. |
| R10 | 50 | Intervals encourage magnitude assessment but cannot supply judgement. |
| R11 | 51–52 | Concedes overstatement about physicists; extrapolations remain hypothetical. |
| R12 | 52 | Rejects exclusively monetary losses; invokes scientific judgement. |
| R13 | 39,49,52–53 | Makes contested historical and practical-harm assertions. |
| R14 | 50–52 | Challenges unnormalised search counts using illustrative denominators. |

## Project interpretation: strongest defensible reconstruction

The useful distinction is between a statistical quantity and a justified criterion for using that quantity. A measurement error of a given size can be adequate for one task and inadequate for another; demonstrating that a number is unusual under a model cannot by itself determine welfare, usefulness or the cost of a mistaken action. That argument challenges automatic relevance filters and automatic decision rules. It does not require abandoning probability models or pretending that estimates have no uncertainty. Use R01–R03, R07–R08 and R12 as the source anchors for this reconstruction.

Two caricatures should therefore be avoided: an exclusively monetary theory of scientific importance, and an unqualified refusal ever to calculate a p-value or power. Conversely, a charitable reconstruction must not silently replace every strong assertion with the weaker proposition that context matters. R04 and R09 identify passages where the article's actual methodological commitments require further challenge. Its polemical descriptions of opponents are evidence about the reply's stance, not reliable substitutes for reading those opponents directly.

## Project analysis: precise points requiring adjudication

1. **Magnitude as a statistic versus magnitude as an unknown target.** Consider an illustrative normal observation model, `estimate | theta ~ Normal(theta, s^2)`. Holding the estimate fixed while changing `s` changes the likelihood over the unknown magnitude `theta`. It does not change the numerical size of the estimate. This supplies a clean way to test a categorical separation of precision from magnitude without presuming that a .05 threshold is required. The reply should be assessed against both meanings, not defended or dismissed through an ambiguous use of “size”. Relevant ledger entries: R02–R04.

2. **Adequacy of uncertainty versus information about uncertainty.** A normative standard may be required to decide whether uncertainty is tolerable. That does not entail that a model-based uncertainty measure contains no information before the standard is selected. Separate an assessment of the sampling distribution from a decision about an acceptable risk. Ask whether the disputants are answering these different questions when they disagree over accuracy. Relevant entries: R02–R03.

3. **One realised path versus one informative observation.** A time series is one realisation of a stochastic process, but it can contain information across time under stated dependence, stationarity or other process assumptions. Likewise, a descriptive census target differs from a causal or superpopulation target. Neither treating all observations as independent nor declaring every process realisation to have only one informative observation follows automatically. The synthesis must specify estimand and stochastic model before resolving this dispute. Relevant entry: R09.

4. **Specification selection requires a narrower causal argument.** Dropping a genuinely irrelevant regressor from an otherwise appropriate conditional-mean model does not inherently bias the retained coefficients. Dropping a relevant confounder can. Selection also affects uncertainty estimation. Any universal claim that significance-based selection necessarily yields biased and inconsistent estimates needs to distinguish these cases, rather than substitute economic importance for identification. Relevant entry: R07, especially p. 48.

5. **Scientific judgement is not yet an operational loss function.** Requiring a reasoned standard is persuasive at a broad level; a decision-theoretic implementation still needs actions, states, consequences and an evaluation rule. Consensus, persuasion and personal utility need not coincide. The strongest challenge is whether scientific audiences can justify common evidential standards while downstream users have different losses. Relevant entries: R08 and R12; compare the other two papers directly before attributing a response.

6. **Survey disagreement needs an independent audit.** An omitted-universe correction, an index-number dispute, disagreement about article scoring and disagreement about access to the coding trail are distinct issues. None can be resolved by the number of supporting anecdotes, the willingness to meet, or the absence of a fresh replication. A reproducible audit needs the inclusion list, item definitions, article-level decisions, locators, disagreement resolution and sensitivity to weights. Relevant entries: R05–R07. Retain both parties' accounts as attributed until documentary evidence is reconciled.

7. **Search-hit denominators and field comparisons are not measured prevalence by themselves.** A search record, an article and an estimated coefficient are different counting units. A claim about reporting rates needs an observed denominator and a reproducible search-and-classification protocol; an imagined number of coefficients cannot establish an empirical lower bound without additional assumptions. Treat the arithmetic as an argument to investigate, not a verified prevalence estimate. Relevant entries: R11 and R14.

8. **Historical and harm claims require their own evidence chain.** Check Fisher's original texts, the cited Gosset–Pearson letter and contemporary sources before declaring the historical dispute settled. Trace the schizophrenia discussion to Cohen (1994) before calling it documented clinical harm: a hypothetical diagnostic illustration cannot establish realised harm. Similarly, interpretation of the employment experiment requires its design, estimates, losses and decision context. Reading an accusation does not verify it. Relevant entries: R13 and the application discussed on p. 47.

## Integration instructions and open work

Update the paper note's reading status and provenance while retaining the distinction between textual comprehension and independent validation. Add R03 as an explicit concession; preserve R04 and R09 as real disagreements; use R10 to prevent a false interval-versus-test polarity and R12 to prevent monetary reductionism. The statement “they admit” within this reply must remain an attribution until checked against Hoover and Siegler's own wording.

The next deliverable should be a matched proposition matrix across the initial critique, reply and rejoinder: proposition, exact locator in each, agreement, difference in target, unresolved factual allegation and evidence needed. This note supplies only the reply column. It cannot establish the accuracy of either side's empirical-practice claims, claims about historical actors, or proposed consequences for the wider profession. It does not advance the slide review gate.

[Matched exchange](../disagreements/2008-exchange.md) · [Paper index](../papers/index.md) · [Critical synthesis](../../synthesis/critical-synthesis.md).

## Later evidence

The access/audit limits above describe this exchange-only reading pass. A subsequent [book reading](cult-2008-reading.md), [coding audit](aer-coding-audit.md) and case ledgers for [Darby/Woodbury–Spiegelman](aer-darby-woodbury.md) and [three further cases](aer-macro-finance-addiction.md) now provide bounded independent documentary checks. They do not amount to complete recoding, empirical replication or verification of historical/medical harms.
