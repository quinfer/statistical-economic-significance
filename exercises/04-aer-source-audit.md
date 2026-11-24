# 04. Audit a claim about research practice

Suppose a reader cites the survey’s headline as evidence that economists ignored effect sizes. Find the exact version and question behind the number. Then check two papers to see how much the coding summaries can tell you about what the researchers actually did.

Begin with the chapter’s account of versions, codes and disputed cases. Work from the factual transcriptions and reading records in this repository, which are sufficient for the tasks. [Chapter appendix, Auditing claims about research practice](../synthesis/critical-synthesis.md#appendix-auditing-claims-about-research-practice) · [AER audit guide](../sources/aer-audit/README.md) · [Coding narrative](../wiki/evidence/aer-coding-audit.md) · [2008 exchange](../wiki/disagreements/2008-exchange.md)

## Problem and scope

**Source claim:** the book reports an expanded 1990s corpus of 187 papers after adding 50 omissions, with an affirmative Q16 rate of 20.9% (printed pp. 80–81; [book note](../wiki/papers/ziliak-mccloskey-2008-cult.md) and [direct-reading ledger](../wiki/evidence/cult-2008-reading.md)). The repository's retrieved item matrix instead contains the earlier 137 papers. Its provenance is documented in the [manifest](../sources/aer-audit/coding-manifest.json). Your task is to decide which propositions the available records can actually test.

The unit of the 1990s matrix is an article, with 19 binary items. The 1980s totals file contains author–paper rows; coauthored papers can recur. Neither file is a random sample newly drawn for this exercise. You are reproducing a bounded historical audit, not estimating a new prevalence of misuse.

## Tasks

1. Run the audit from the repository root:

   ```sh
   python3 sources/aer-audit/coding-audit.py
   ```

   The default run needs only committed CSVs and computes arithmetic diagnostics. `--raw-dir` is optional and requires separately retrieved historical source files; a default run does not repeat the earlier raw-source checksum and transcription checks.

2. **Reproduce the counts independently.** Calculate the Q16 adverse count and proportion, the Q7 × Q16 cross-tabulation and Q9’s affirmative rate over all 137 rows and conditional on Q8 = 1. Explain what each denominator counts and what the questionnaire means by an adverse response. [Question dictionary](../sources/aer-audit/coding-questionnaire.csv) · [137-row matrix](../sources/aer-audit/coding-1990s-paper-scores.csv)
3. **Name the version where each discrepancy occurs.** Compare matrix Q14/Q15 percentages with the final JSE tables. Record where they differ and what you would need to explain the difference. Check the final JSE and EJW 1980s Q7 entries separately. [Final JSE version check](../wiki/evidence/jse-2004-version-check.md)
4. **Check what a row represents.** For the 1980s row-total anomaly and the omission-list overlap, write one warranted statement and one that would overreach. Take account of author–paper rows and the limits of the eligibility evidence.
5. **Build a two-case ledger.** For Darby and Bernheim–Wantz, identify the exact allegation, published version and printed locator, evidence bearing on the allegation, a narrower concern and what would require replication. Give one correction to the critique and one qualification of the defence. Check that any DOI you give corresponds to the version you use. [Final Darby reading](../wiki/evidence/darby-final-followup.md) · [Final Bernheim–Wantz reading](../wiki/evidence/bernheim-wantz-final-followup.md) · [Supporting catalogue](../sources/aer-audit/supporting-materials.md)
6. **Test a proposed reconstruction.** Could subtracting earlier counts from rounded book percentages recover the 50 added papers’ codes? Explain the mathematical non-uniqueness and the unverified assumptions about versions. Specify what you would seek in a follow-up. [Expanded-matrix search](../wiki/evidence/expanded-matrix-followup.md)

**Submit:** a reproduction table, a two-case evidence ledger and a 500-word assessment of what remains unresolved. Label your ledger's documentary claims as based on the repository's existing reading record unless you actually obtain and consult the primary passages yourself. A primary-source reading, a note-based exercise and an empirical replication are different accomplishments.

<details>
<summary>Worked audit and discussion</summary>

**Project reproduction.** Start with the earlier 137-paper matrix. Count 25 affirmative Q16 codes and 112 adverse codes, giving 112/137 ≈ 81.7518%. Keep the row and column labels on the joint table so the order of the four counts is visible.

| Q7 | Q16 = 0 | Q16 = 1 |
|---|---:|---:|
| 0 | 80 | 7 |
| 1 | 32 | 18 |

All five affirmative Q9 responses occur in the eleven rows with Q8 = 1. Report 5/137 ≈ 3.65% for all coded papers or 5/11 ≈ 45.45% for the papers that met the preceding criterion. Name the denominator when reporting the result. [Chapter appendix, What do the scores and percentages tell you?](../synthesis/critical-synthesis.md#what-do-the-scores-and-percentages-tell-you)

The matrix gives Q14 = 39/137 ≈ 28.5% and Q15 = 35/137 ≈ 25.5%; the checked final JSE tables reverse these values. The 1980s Q7 value is 47.3% in the checked final JSE version, while the checked EJW table gives 13.2%. The [version ledger](../wiki/evidence/jse-2004-version-check.md) supports reporting those specific observations, not a reconstructed explanation.

There are 281 author–paper rows, of which 42 total 20 responses despite 19 items. This is an unexplained record inconsistency, not 42 proven independent miscoded papers. The omission list has 82 rows against the rejoinder's stated 81; Simon appears in both an omission and a scored list. The [coding audit](../wiki/evidence/aer-coding-audit.md) records the provenance and limits. The discrepancy does not show that all omissions were fictitious.

**Project interpretation of the documented readings.** For Darby, use final pp. 311–312 to show how he translates a coefficient into growth magnitudes and p. 315 for his economic interpretation of a difference. These passages correct a blanket description of magnitude neglect. To judge the exclusion of the oil term and the reading of non-rejection as absence, examine the selection step. The defence uses interval containment, so a covariance-aware cross-equation test would require further evidence. [Darby ledger](../wiki/evidence/darby-final-followup.md)

Bernheim–Wantz final pp. 543–544 interpret magnitudes; p. 547 Table 4 contains magnitude estimates, and footnote 17 reports direct tests of differences. The star labels an alternative comparison, not a significance tier. Thus a critique based solely on missing magnitudes or separate significance labels misdescribes the checked final passages. Within-regime non-rejection still does not establish practical equivalence, and no causal identification claim has been replicated. See the [Bernheim–Wantz ledger](../wiki/evidence/bernheim-wantz-final-followup.md).

To see the reconstruction problem, imagine two surveys with identical column totals and different papers scoring yes. The totals match while the joint coding patterns differ. Subtracting older totals would also assume unchanged codes, eligibility, applicability and denominators for retained papers. A follow-up needs a versioned 187-paper roster and matrix, the 50-paper crosswalk, coding rules, passage-level reasons and independent coding checks. Retrieval remains incomplete. The case checks can correct particular descriptions, while a corpus-wide rate would need a defensible article universe and coding design. [Chapter appendix, Reading the original papers](../synthesis/critical-synthesis.md#what-changes-when-you-read-the-original-papers)

</details>

[Exercise index](README.md) · [Next: finance and identification](05-finance-identification.md)
