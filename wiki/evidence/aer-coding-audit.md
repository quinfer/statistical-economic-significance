# AER survey coding: provenance and bounded arithmetic audit

**Status:** original research audit, 24 October 2026; verifier `debate_sources`. This is an audit of the retrieved materials for the original 1980s and 1990s surveys, not a replication of all article classifications. It does not open the slide gate.

**Project finding.** The supplied 137-paper matrix reproduces the arithmetic behind the 2004 headline of approximately 82% adverse classifications on question 16, and its question 7 × question 16 cross-tabulation. It also contains discrepancies with published item percentages. The 1980s author totals have unresolved inconsistencies, and Hoover–Siegler's omissions list contradicts their reproduced score list in one identifiable case. These results qualify both sides' numerical evidence; none establishes how many economists actually confused statistical and economic significance.

Related: [1996 survey](../papers/mccloskey-ziliak-1996.md), [2004 survey](../papers/ziliak-mccloskey-2004.md), [Sound and fury](../papers/hoover-siegler-2008-sound.md), [2008 exchange](../disagreements/2008-exchange.md), [practice versus validity](../claims/C004-practice-and-validity.md).

## Materials, versions and actual coverage

The [audit manifest](../../sources/aer-audit/coding-manifest.json) records exact URLs, versions, access date, downloaded-file SHA-256 checksums, temporary paths and reading coverage. The [access log](../../sources/aer-audit/coding-access-log.json) records failures and workarounds. Supporting materials are outside the 35-source core. No article PDFs or complete source HTML are redistributed.

**Source provenance.** Hoover's [rankings page](https://public.econ.duke.edu/~kdh9/Source%20Materials/McCloskey/Rankings.htm) attributes its survey tables to Stephen Ziliak through personal communication. These are author-hosted reproductions of transmitted scores, not independent recodings. The 1980s workbook has **281 author–paper entries**, with coauthors entered separately, and only yes/no totals. The 1990s workbook has **137 paper entries**, with all coauthors in one entry and 19 binary item columns. The alphabetical and ranked sheets within each workbook contain identical substantive records after reordering. This checks transcription consistency, not independent reliability.

The [published 1996 scan](https://www.bauer.uh.edu/jhess/documents/McCloskey%20and%20ziliak.pdf) was retrieved; its extracted text was empty. OCR supplied reading text, with the instrument's opening and Table 1 visually checked against printed pp. 101 and 105. Coverage here is pp. 101–106 and 109–111, not a complete article reading. The [author-hosted 2004 PDF](https://www.deirdremccloskey.com/docs/size.pdf) is the *Econ Journal Watch* publication, 1(2), pp. 331–358. Relevant survey prose and Tables 1–3 and 5 were read; p. 336 was visually checked. The first attempted institutional link to the *Journal of Socio-Economics* final returned HTTP 404. A subsequent author-index search recovered the final scan: printed pp. 527–535 and 540–542 were visually read, with an independent check of Tables 1, 3 and 5. The [version-check ledger](jse-2004-version-check.md) records this new evidence. Complete identity between versions is not assumed.

**Version boundary.** The 2008 book's revised 1990s survey concerns **187**, not 137, papers. The [direct book reading](cult-2008-reading.md) identifies this revision in chapter 7, p. 80, and Table 7.1, p. 81. This audit has not retrieved its expanded item matrix or the 50 additional papers' codes. A discrepancy in the 137-paper matrix must not automatically be attributed to the revised book table; conversely, a changed book percentage does not repair the provenance of the older matrix.

## What the instrument measures

**Source claim.** The 1996 paper, pp. 101–104, describes 19 questions, with yes, no and not-applicable responses; yes indicates the authors' preferred practice. Table 1, p. 105, uses different applicable denominators. [The item dictionary](../../sources/aer-audit/coding-questionnaire.csv) supplies operational paraphrases, original printed locators and numeric comparisons. It does not silently substitute a modern checklist for their instrument.

The questions cover sample size (1), reporting and interpretation (2–5), avoiding indiscriminate test-statistic reporting (6), significance's role at the first crucial passage (7), power (8–9), ranking by test statistics (10), signs versus magnitudes (11), magnitude discussion (12), quantitative scientific context (13), variable selection (14), argument after the principal test (15), treating tests as decisive (16), reasonableness simulations (17), conclusions (18), and ambiguous language (19). Original prose questions 7 and 16 are negatively phrased, while the tables/code labels orient yes towards good practice. Reading every literal prose question as if yes always retained its grammatical meaning would invert those items.

Question 9 is conditional. For 1990s, five papers receive Q9=1 and all five also receive Q8=1; 11 papers receive Q8=1. Thus 45.5% means **5/11**, while **5/137 = 3.65%** of all coded papers receive Q9=1. These answer different questions. The binary matrix assigns Q9=0 to all 126 papers with Q8=0, so the unweighted score loses both points for those entries; conditional reporting and score construction must be distinguished. The 1980s published Q9 denominator is 12, although Q8's 4.4% of 182 corresponds to eight papers under ordinary rounding. The original item-level data are needed to resolve that apparent conditional-denominator inconsistency.

Question 17 is also more demanding than the presence of a numerical simulation. The authors exclude a simulation whose coefficients are screened solely by statistical significance (1996 p. 104; EJW 2004 p. 337). Consequently, identifying a simulation or elasticity in an original article can rebut an absolute claim of no economic magnitude, while leaving the disputed selection-rule classification unresolved.

**Project interpretation.** A sum of these items combines several constructs. Reproducing that sum does not validate its weights or establish that every failure represents confusion between two kinds of significance. Conversely, finding magnitudes somewhere in a paper does not prove that significance was used appropriately at every selection or interpretation step. This is the distinction the individual case audits must preserve.

## Reproduced arithmetic and discrepancies

All 137 rows have 19 binary values; each reported total and percentage of positive items matches its row. The [matrix](../../sources/aer-audit/coding-1990s-paper-scores.csv) and [machine-readable results](../../sources/aer-audit/coding-audit-results.json) preserve the evidence.

| Check | Recalculation | Comparison and interpretation |
|---|---:|---|
| Q16 adverse classification | 112/137 = 81.75% | Reproduces rounded 82%; validity of the coding remains separate. |
| Q7 × Q16 | (0,0)=80; (0,1)=7; (1,0)=32; (1,1)=18 | Exactly reproduces EJW Table 5, p. 350, and final JSE Table 5, p. 542. |
| Q14, variable selection | 39/137 = 28.5% positive | EJW Table 1, p. 336, and final JSE Tables 1 and 3, pp. 529, 532, give 25.5%. |
| Q15, after the principal test | 35/137 = 25.5% positive | Both versions' tables give 28.5%; the two percentages appear exchanged relative to the matrix headers. |
| 1980s Q7 in comparative table | Original 1996 Table 1: 47.3% | EJW Table 1 prints 13.2%, despite its own p. 333 prose describing approximately 53% adverse classifications. Final JSE Table 1 prints 47.3%; this error is absent from that final table. |

All other 1990s Table 1 percentages match the matrix to one decimal when Q9 uses its conditional denominator. A Q14/Q15 exchange would leave each row's total unchanged; the present evidence cannot locate whether the error arose in table production, column labelling or an earlier coding stage.

The [1980s totals](../../sources/aer-audit/coding-1980s-author-scores.csv) include **42 author entries with yes + no = 20**, including Darby 1984 at 3 + 17. The instrument has 19 items. Entries below 19 can reflect legitimate not-applicable answers; exceeding 19 cannot be explained that way. Because coauthors repeat papers, these are not 42 independently established erroneous papers. The file has no reliable paper identifier or item codes, so collapsing entries solely by issue and score risks merging different articles. The claimed 182-paper totals and 1980s paper percentiles were not reconstructed.

A further diagnostic checks whether the visually transcribed 1996 Table 1 percentages can arise from an integer positive count divided by their printed applicable denominators and rounded to one decimal. Nine pairs fail that narrow check, including Q2: denominator 178 and 32.4%. The results file lists all pairs. This establishes an unresolved reporting inconsistency under that rounding convention, not the correct replacement counts. No aggregate prevalence was recalculated from the 281 author entries.

## Omissions: a source claim that itself needs auditing

**Source claim.** The [omissions list](https://public.econ.duke.edu/~kdh9/Source%20Materials/McCloskey/Omitted%20Papers.htm) marks 15 1980s and 56 1990s papers as using both regression and significance tests, plus five in each decade using tests without regression, and one 1990s paper using regression without tests. The [factual metadata transcription](../../sources/aer-audit/coding-omissions.csv) contains **82 records**, exactly 15 + 56 + 5 + 5 + 1. The narrower claimed set is 71. Eligibility labels remain Hoover–Siegler's claims, not independently established findings about all listed originals.

**Project finding.** *Sound and fury*, p. 5, enumerates those same quantities, while the rejoinder, p. 62, refers to 81 overlooked papers. More importantly, the omissions list's 1980s item 13 identifies Carol J. Simon's June 1989 article, whereas the 1980s alphabetical score sheet already includes **Simon, Carol J.; 1989(3); 9 yes, 10 no**, row 238. The ranked sheet agrees. The publisher's [June 1989 issue contents](https://www.jstor.org/stable/i304577) identifies her article as “The Effect of the 1933 Securities Act on Investor Information and the Performance of New Issues”, pp. 295–318, matching the author, issue and subject of the listed omission. This is a direct contradiction between the supplied lists. It could account numerically for 82 versus 81, but no retrieved explanation establishes that history; neither total is silently corrected.

The printed 8%/29% narrower omission rates can be approximately reproduced as 15/(182+15) and 56/(137+56), conditional on accepting the claimed eligibility and absence. The Simon overlap challenges that premise for one 1980s entry. Neither these rates nor the broader 20% figure is a corrected estimate of scientific misuse. Missing papers' classifications would have to be recovered before calculating that estimate. Hoover–Siegler themselves acknowledge that omissions need not change the conclusions (*Sound and fury*, n. 3, pp. 31–32).

## Five disputed cases mapped to available scores

These are mappings to the retrieved score tables; they do not adjudicate the original articles. The [case mapping CSV](../../sources/aer-audit/coding-selected-cases.csv) gives all positive and negative item numbers where available. Separate direct article audits cover [Darby and Woodbury–Spiegelman](aer-darby-woodbury.md) and [the macroeconomic, finance and addiction cases](aer-macro-finance-addiction.md).

| Article | Supplied score | What can be checked here |
|---|---:|---|
| Darby (1984) | 3 yes, 17 no | Confirms the inconsistent total noted by H&S, n. 5, p. 32; no original item codes retrieved. |
| Woodbury–Spiegelman (1987) | 7 yes, 12 no | Confirms total; no item-level coding retrieved. |
| Bernanke–Blinder (1992) | 8/19 | Q10=0, Q11=0, Q12=1, Q13=1, Q16=0, Q18=1. |
| Becker–Grossman–Murphy (1994) | 6/19 | Q10=0, Q11=0, Q12=1, Q13=0, Q16=0, Q18=1. |
| Bernheim–Wantz (1995) | 1/19 | Q3 alone is positive. |

Under H&S's stated cumulative definition—fraction scoring at most the case's score—the 1990s matrix gives Bernanke–Blinder 79/137 = 57.66% and Bernheim–Wantz 1/137 = 0.73%, consistent with their rounded 58th and 1st percentiles. Becker–Grossman–Murphy instead gives **46/137 = 33.58%**, not the reported 30th percentile (*Sound and fury*, n. 5, p. 32). This discrepancy does not alter its supplied six-item score.

## What remains unresolved

No original coder-by-coder sheets, inter-rater reliability study, contemporaneous passage-to-code rationales, complete 1980s item matrix, or expanded book matrix were retrieved. Their absence from this retrieval is not proof that no such records exist. The 82 omission candidates were not all independently read; the Simon check is a verified cross-list contradiction, not an exhaustive journal census. Numerical consistency supports faithful aggregation of given codes, not their construct validity. Numerical inconsistencies warrant correction and further provenance work, not the inference that the surveys contain no useful observations.

The [expanded-matrix follow-up](expanded-matrix-followup.md) records the subsequent author, publisher and archive search, including the final JSE discovery. It keeps the 137-paper arithmetic separate from the unresolved 187-paper reconstruction and article inclusion crosswalk.

Reproduce the CSV arithmetic with `python3 sources/aer-audit/coding-audit.py`. Add `--raw-dir /tmp` when the downloaded temporary files are available to verify checksums, reparse the HTML and compare both workbook orderings. The script does not fetch sources, adjudicate coding, or approve a review gate.
