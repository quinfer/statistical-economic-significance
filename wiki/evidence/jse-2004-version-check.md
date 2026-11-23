# Final 2004 publication: a version-specific table check

**Status:** selected published pages directly read, 24 October 2026; reader `root`, independent table verifier `decision_finance_sources`. This follow-up narrows a version gap in the [2004 paper note](../papers/ziliak-mccloskey-2004.md) and [coding audit](aer-coding-audit.md). It does not recover the [expanded 187-paper matrix](expanded-matrix-followup.md).

## Source and actual coverage

The author's articles index supplied [Article_190.pdf](https://www.deirdremccloskey.com/docs/pdf/Article_190.pdf). The first page identifies Ziliak and McCloskey, *The Journal of Socio-Economics* **33 (2004), 527–546**, DOI **10.1016/j.socec.2004.09.024**. This is a 20-page image-only published scan, distinct from the separately paginated *Econ Journal Watch* version. Its SHA-256 is `ec4f1d738f03f246dd715ccd33f289f3ef7961e4e44352b0299f5c86d9add153`. The [manifest](../../sources/aer-audit/coding-manifest.json) records retrieval provenance. No scan or extracted article text is committed.

Root visually read printed **pp. 527–535 and 540–542**, including Tables 1–3 and 5 and the associated prose. Pages 536–539 and 543–546 remain unread in this version. Historical citations, cross-disciplinary assertions and practical-harm claims in the read pages were not independently verified. Both readers also visually checked pp. 534–535 for the Bernheim–Wantz quotation and table allegation. The second reader visually checked pp. 529, 532 and 542, rechecked EJW p. 336, and independently recomputed the relevant matrix totals.

## What the final pages establish

**Source observations and reproducible comparisons.** Table 1's source note, p. 529, expressly uses **137** 1990s papers. This is not the book's later sample.

| Item | Final JSE observation | Earlier comparison | Consequence |
|---|---|---|---|
| 1980s Q7 | Table 1, p. 529: **47.3%**; Table 3, p. 532: change of −10.8 points to 36.5% | EJW Table 1, p. 336, prints **13.2%**; the 1996 original reports 47.3% | The EJW discrepancy is absent from final JSE. Do not attribute that number to every version. |
| 1990s Q14 | Tables 1 and 3, pp. 529, 532: **25.5%** | Matrix: **39/137 = 28.5%**, rounded | The matrix/table mismatch persists in final JSE. |
| 1990s Q15 | Same tables: **28.5%** | Matrix: **35/137 = 25.5%**, rounded | The apparent exchange persists; its origin in coding, column labels or table production remains unknown. |
| Q7 × Q16 | Table 5, p. 542: cells **80, 7, 32, 18** in row order; total **137** | The matrix and EJW Table 5 agree | The same aggregate is reproduced in both publications; this is not independent recoding. |

**Source claim.** The simulation criterion explicitly excludes a later simulation whose coefficients were admitted solely by statistical significance (pp. 532–533). This qualification matters when assessing claims that the presence of a magnitude or simulation overturns a negative code. The source also asserts deterioration using its preferred criteria while acknowledging improvements (pp. 531–533).

**Project interpretation.** The retrieved final version strengthens one bounded correction and limits another: Q14/Q15 remain unresolved, whereas the 1980s Q7 error is confined to the checked EJW table. Neither observation validates the coding instrument, identifies the erroneous stage, nor estimates the prevalence of methodological confusion. A version comparison is therefore substantive evidence work, not merely bibliographic housekeeping.

Page 528 also repeats the conditional claim that roughly 70% of the 70% confused 1980s papers failed to report magnitudes. Its tension with Q12's 80.2% positive figure is the same **conditional** issue identified in the [book ledger](cult-2008-reading.md): it becomes a numerical contradiction only if the event definition and paper universe coincide. We retain the tension rather than inventing corrected counts.

## Additional quotation-context check

**Source comparison.** Final JSE p. 534 quotes Bernheim–Wantz’s non-significance remark while omitting its Table 1 qualifier and adding an interpolation about four regressions. The original final p. 543 distinguishes Table 1 from Table 2, immediately discusses economic and statistical effects, and draws a substantive theoretical inference from the latter results. Thus the extracted quotation is incomplete context; equally, Hoover–Siegler’s defence that no inference is drawn should be limited to the isolated Table 1 remark. Page 535’s allegation about the p. 547 table is also checked against the final original in the [Bernheim–Wantz follow-up](bernheim-wantz-final-followup.md). No intention to mislead is inferred.

## Effect on the synthesis

The [critical synthesis](../../synthesis/critical-synthesis.md) now attributes each discrepancy to the publication in which it was actually observed. Its broader distinction between defining importance, establishing an uncertain effect and choosing an action is unchanged. No new survey score, revised misuse rate, complete-version equivalence or full-article reading is claimed. The [slide gate](../../reviews/review-gate.md) remains closed.
