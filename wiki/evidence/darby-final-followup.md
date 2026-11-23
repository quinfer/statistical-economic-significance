# Darby (1984): published-text reading after retrieval follow-up

**Status:** final article read on 24 October 2026 by `inference_sources`, after the initial search failed and the user supplied a JSTOR download. This supersedes the final-article access gap in the earlier [Darby–Woodbury ledger](aer-darby-woodbury.md). It does not replicate Darby's empirical results or recode the AER survey. These supporting materials remain outside the 35-source core. **The slide gate remains closed; this is agent research, not human review approval.**

**Project assessment.** The published text confirms H&S's principal defence: Darby translates estimated coefficients into productivity-growth magnitudes and discusses their economic meaning. It also confirms the narrower basis of MZ's objection: oil-price terms are excluded after tests of zero restrictions, without a demonstrated economically negligible region. These conclusions address different steps of the argument. Neither warrants a wholesale acquittal or condemnation of the paper.

## Identity, provenance and actual coverage

Michael R. Darby, “The U.S. Productivity Slowdown: A Case of Statistical Myopia,” *American Economic Review* 74(3), June 1984, pp. 301–322. Identity is corroborated by the [JSTOR issue contents](https://www.jstor.org/stable/i304558), [NBER publication cross-reference](https://www.nber.org/papers/w1018), author's [official UCLA CV](https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/strategy/MICHAEL%20R.%20DARBY%20CV.pdf), p. 20, publication 32, and the supplied journal scan. The article DOI remains unverified; the working-paper DOI `10.3386/w1018` must not be assigned to it.

The supplied file, `supplied-document:Darby-USProductivitySlowdown-1984.pdf`, is 1,229,008 bytes, with SHA-256 `eb0978c229c4562c6b2ab0f46c39a91ad46967218046289575c868f9b6053c7d`. Its 23 PDF pages comprise a JSTOR cover and the complete printed pp. 301–322. The cover identifies [stable article 1804009](https://www.jstor.org/stable/1804009); journal headers, title, author and continuous printed pagination match. The download footer dates the supplied copy to 24 October 2026. This is the published article, not the NBER draft.

**Reading depth: `full_text_read`.** All extracted text of printed pp. 301–322 was read, including footnotes, data appendix and references. Printed pp. 301, 307, 310–312 and 315–316 were also rendered and visually checked: the title/identity, all three figures, disputed equations, Table 6 and Table 7. The appendix was read but its data cells were not independently transcribed, reconstructed or replicated. Complete-text reading is not a claim that every visual element or numerical input was independently audited. Temporary page extractions are in `/tmp/darby-final-text/`; no article text or PDF is added to the repository.

Comparison sources are [MZ 1996](../papers/mccloskey-ziliak-1996.md), p. 104; [H&S 2008](../papers/hoover-siegler-2008-sound.md), p. 8 and note 6 p. 32; and [MZ's 2008 reply](../papers/mccloskey-ziliak-2008-reply.md), pp. 46–47. See the [2008 exchange](../disagreements/2008-exchange.md). The NBER 1982 draft retains its earlier **selected-sections** reading label.

## Evidence ledger: what the final text changes

| Printed location | Verified source observation | Project interpretation |
|---|---|---|
| 310, equation (9), definitions and note 24 | The target is an effect beyond temporary unemployment/employment effects. Quarterly analysis substitutes a post-1965 time-shift assumption for the demographic adjustments. Darby says BLS stopped collecting the layoff series in 1981; he also reports its weak t statistic and limited effect on other estimates. | Do not mistake the conditional direct-effect target for all possible economic consequences. The draft's layoff term disappearing is not evidence of significance-only deletion: an explicit data-availability reason is present. Neither the time-shift proxy nor the conditional interpretation is thereby validated. |
| 311, Table 6 and equation (12) | Unrestricted price-control coefficient .04104 (t 2.69); after all oil terms are set to zero, .04691 (t 3.77). Unrestricted oil joint tests give F(4,122)=.42 and F(3,122)=.49. Final equation retains current employment-growth coefficient .027 (t .31). | Test-based oil exclusion is observable. Retention of a weak control disproves a universal deletion rule, but does not answer MZ's specific objection to the oil restriction. Selection need not automatically produce bias or inconsistency; that requires a specified statistical model and selection procedure. |
| 311–312, calculation after equation (12), Table 7 | Average control index .7857 is multiplied by .04691, giving .0369 rounded log-productivity overstatement. Dividing across the two periods yields corrections of −.46 and +.61 in annual growth units. Adjusted hourly rates are 1.88 and 1.33; employee rates 1.67 and 1.33. | H&S's magnitude defence is directly verified. These are approximately percentage-point adjustments to annual log growth, not relative percentage reductions. This part of Darby's conclusion depends materially on the estimated coefficient, contrary to an unqualified claim that his findings do not turn on regressions. It does not show that the selected model or resulting substantive conclusion is correct. |
| 312, text and note 31 | Darby distinguishes price controls' possible real employment effects from the reporting effect captured conditional on labour-market movements. | The estimand distinction strengthens the case against treating a variable's exclusion as a judgement about its importance everywhere. It does not demonstrate that the remaining conditional oil effect is economically negligible. |
| 314, equations (14)–(15) and following discussion | The price-control coefficient for nominal GNP is .0012 (t .07). The discussion proceeds from lack of a significant nominal impact to an asserted absence of a nominal-spending effect. | This supplies a concrete, narrower non-rejection-as-absence concern beyond ambiguous terminology. A small point estimate and weak t statistic alone cannot establish practical equivalence. The economic theory and other evidence may contribute, but do not turn this test into an equivalence demonstration. |
| 315, equation (16) and note 39 | The manufacturing-production comparison yields .0312 (t 2.62), about .016 below equation (12)'s estimate. Darby discusses the difference despite calling it statistically insignificant and attributes it to the index's mix of physical-unit and deflated series. Note 39 reports control-versus-decontrol equality tests within regressions. | The economic explanation strengthens H&S's broad defence, but its note 6 confidence-interval reconstruction is not a reported calibrated cross-equation test. Note 39 is not a test of the difference between equations (12) and (16). |
| 316–317, conclusions | The oil conclusion remains strong. Darby also explicitly distinguishes factors' failure to explain variation from their possible importance for trend growth, and calls for further work on demographic adjustments and measurement. | Preserve both passages. The warning limits a global accusation that Darby equates every non-significant result with universal unimportance; it does not prove the narrower oil conclusion or remove selection uncertainty. |

**Source-fidelity cautions.** The visual Table 6 places one-tailed 10% markings on current-oil coefficients in rows 4 and 5, while the prose refers to rows 5 and 6; row 6 restricts all these terms to zero. This appears to be an internal cross-reference error, not an extraction error or evidence of a different empirical result. Table 7's caption ends in 1978, but its rows, adjustment denominator and surrounding discussion use 1979. The latter are the basis of the reported six-year adjustment. These inconsistencies should be preserved rather than silently repaired.

## What follows for the dispute

**Project interpretation — the strongest H&S position.** MZ 1996 p. 104's description is too broad if read as denying substantive coefficient reasoning. Darby's published pp. 311–312 and 315 provide direct counterevidence. The demographic construction and comparisons earlier in the paper also make economic assumptions and evaluate magnitudes; the paper is not an exercise in significance labels alone. However, H&S's p. 8 assertion that there is nowhere any confusion is stronger than this audit warrants, especially given pp. 311 and 314's absence language.

**Project interpretation — the strongest MZ position.** Their reply pp. 46–47 directly attacks using significance as a specification filter. That objection is not answered merely by finding a later magnitude calculation. The valuable remaining question is whether excluding oil-price terms preserves economically plausible productivity contributions and properly reflects selection uncertainty. The retained employment term rebuts a *universal* reading of the reply's polemical deletion language; it does not erase the documented oil restrictions or imply that MZ literally lists every retained regressor.

**Project interpretation — the p. 315 comparison.** The published coefficient gap is .04691 − .0312 = .01571. A proper uncertainty statement about a difference requires the covariance of the two estimates as well as their individual variances. These equations also have different outcomes, covariates and estimation periods, so substantive comparability needs attention before testing equality. Confidence-interval containment is not itself a calibrated difference test, and failure to reject equality is not practical equivalence. Darby supplies an economic reason for a smaller second coefficient; the passage does not supply a complete cross-equation uncertainty calculation. H&S note 6's interpretation must therefore remain an interpretation, not a claim that the article reports such a calculation.

## Draft/final differences now directly verified

| Feature | NBER November 1982 draft | Published June 1984 article |
|---|---|---|
| Selected productivity regression | Equation (14), printed p. 17 | Equation (12), p. 311 |
| Productivity sample | 1949:I–1980:IV | 1950:II–1983:I |
| Price-control coefficient and t | .04397; 3.41 | .04691; 3.77 |
| Current employment coefficient and t | .018; .20 | .027; .31 |
| Layoff variable | Retained, t −.24 | Removed; data collection ceased in 1981, p. 310 n24 |
| Later comparison coefficient and t | Equation (18), p. 26: .0355; 3.05 | Equation (16), p. 315: .0312; 2.62 |
| Later comparison sample | 1948:II–1980:III | 1948:II–1983:I |
| Growth comparison endpoint | 1978 | 1979 in final calculation and Table 7 rows |

These differences prevent interchangeable quotations or equation numbers. The comparison verifies text, not the effect of each revision on the underlying estimates. Both versions retain the central combination of test-based restrictions and substantive coefficient interpretation.

## Retrieval chronology and remaining boundaries

The initial targeted search on 24 October did **not** recover a final article. The user then supplied the published JSTOR file, which was checked and read as described above. Earlier failures remain accurate accounts of those routes; they are superseded as an overall access conclusion. Root's ordinary-browser activity is outside this agent's access claims.

The author's CV identifies a reprint in Edward N. Wolff (ed.), *The Economics of Productivity*, volume II, Edward Elgar, 1997, ISBN 1858984203. The [volume-II catalogue](https://books.google.co.uk/books?id=EBAPAQAAMAAJ) was retrieved, but the reprint text and pagination remain unread. The CV's p. 11 dates NBER 1018 July 1984 and cross-refers publication 33, while the final entry is 32. Its [NBER alias](https://papers.nber.org/papers/w1018.pdf) served the same November 1982 draft already read. RePEc explicitly borrows its abstract from another version; the actual OpenAlex result `W1760003876` groups draft and final locations. None of these metadata labels substitutes for the final-file check.

| Route and exact attempted URL | Outcome in this pass |
|---|---|
| [JSTOR stable article](https://www.jstor.org/stable/1804009) and [PDF](https://www.jstor.org/stable/pdf/1804009.pdf) | Web extraction gave no usable article text; PDF opener reported inaccessible. The earlier terminal attempt returned challenge HTML, not PDF. Root's separate ordinary-browser check is outside this agent's access claims. |
| [UCLA current faculty page](https://www.anderson.ucla.edu/faculty-and-research/strategy/faculty/darby) | Readable; linked the CV. Selected publication list supplied no final-paper download. The attempted older `global-economics-and-management/faculty/darby` path was inaccessible. |
| [UCLA CV PDF](https://www.anderson.ucla.edu/sites/default/files/documents/areas/fac/strategy/MICHAEL%20R.%20DARBY%20CV.pdf) | Public download succeeded; dated 8 December 2015; 36 PDF pages. Selected bibliographic entries read. |
| [NBER alias](https://papers.nber.org/papers/w1018.pdf) | Public download succeeded, 58 PDF pages; byte-identical to the previously retrieved 1982 draft. |
| [UCLA wp304](https://www.econ.ucla.edu/workingpapers/wp304.pdf), [wp266](https://www.econ.ucla.edu/workingpapers/wp266.pdf) | Both inaccessible through web opener; terminal HTTPS wp304 connection timed out after about 75 seconds, HTTP code 000. Earlier HTTP wp304 attempt was 404. These are working-paper routes, not verified final-paper files. |
| [Elgar ISBN route](https://www.e-elgar.com/shop/isbn/9781858984209) | Web inaccessible; terminal HTTP 403. A conventional `/shop/gb/the-economics-of-productivity-9781858984209.html` route was also inaccessible through web opener. No purchase or login attempted. |
| [Google Books ISBN route](https://books.google.com/books?vid=ISBN1858984203) | Web opener failed, but public terminal retrieval succeeded and redirected to the UK catalogue. It identified volume I, `RA8PAQAAMAAJ`, and linked volume II, `EBAPAQAAMAAJ`; the latter catalogue was also retrieved. Only catalogue/snippet-view information, not the Darby article, was read. |
| [SSRN 304758](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=304758) | OpenAlex discovery link; web inaccessible and terminal HTTP 403. Version/content not inspected. |
| [Internet Archive catalogue query](https://archive.org/advancedsearch.php?q=title%3A%22American%20Economic%20Review%22%20AND%20year%3A1984&output=json&rows=50) | HTTP 200; returned one table-of-contents item, `sim_american-economic-review_1984_74_contents`. No final article text retrieved. |

Failure here means failure of the recorded route, not proof that no legitimate copy exists or that a library subscription cannot supply it. No credentials, purchases, access-control workarounds or messages to outside people were used.


## Search record and file integrity

The exact 27 web queries, two API queries, attempted URLs, outcomes, reading update and proposed supporting-registry changes are preserved in [permanent final-paper access log](../../sources/aer-audit/final-paper-access-log.json). This was a targeted retrieval pass, not an exhaustive systematic search. The initial temporary artefacts have these checksums:

| Temporary artefact | SHA-256 | What the checksum establishes |
|---|---|---|
| `/tmp/darby-final-cv.pdf` | `756ad9a93dcce63e51a43c31e757201d46ad864791a728bc6472d8b677cc0c34` | Retrieved 36-page CV, not final article |
| `/tmp/darby-final-nber-alias.pdf` | `b1b79c875f0d9e20789b28996bcba74edd9c7849c78445c4cc7dc1d6258e8829` | Same 1982 manuscript as earlier retrieval |
| `/tmp/darby-final-openalex.json` | `ea7095de6b6ad34f4b33ba72a941991c993a34a1938efb0a2acfadeef519564c` | Actual discovery response, not proof of version equivalence |
| `/tmp/darby-final-googlebooks-vol2.html` | `515c52d16d176097f4654627bc0719024dc810cffb40f8050c0497c898a805ab` | Retrieved catalogue HTML, not article pages |


The final article's checksum and actual coverage appear above. No access-control workaround or contact with external people was used. The copyrighted article remains in the user's Downloads; original analysis, bibliographic records and links belong in Git.

**Open questions.** A substantive replication would require the data construction, covariance-aware comparisons, economically justified oil-effect bounds and sensitivity to specification selection. No corrected survey misuse rate, empirical truth about the productivity slowdown, or recommendation to discard calibrated inference follows from this reading. The earlier final-text access gap is resolved; these methodological and replication questions remain open.
