# 04. Audit a claim about research practice

**Aim:** separate reproducible arithmetic, provenance, interpretation of a passage and validity of a research-practice measure. Prerequisites: basic proportions and a willingness to retain unresolved disagreements.

Start with the [AER audit guide](../sources/aer-audit/README.md), [coding narrative](../wiki/evidence/aer-coding-audit.md) and [2008 exchange](../wiki/disagreements/2008-exchange.md). The exercise uses factual transcriptions and original project notes already in the repository. It does not require access to copyrighted article files or temporary downloads.

## Problem and scope

**Source claim:** the book reports an expanded 1990s corpus of 187 papers after adding 50 omissions, with an affirmative Q16 rate of 20.9% (printed pp. 80–81; [book note](../wiki/papers/ziliak-mccloskey-2008-cult.md) and [direct-reading ledger](../wiki/evidence/cult-2008-reading.md)). The repository's retrieved item matrix instead contains the earlier 137 papers. Its provenance is documented in the [manifest](../sources/aer-audit/coding-manifest.json). Your task is to decide which propositions the available records can actually test.

The unit of the 1990s matrix is an article, with 19 binary items. The 1980s totals file contains author–paper rows; coauthored papers can recur. Neither file is a random sample newly drawn for this exercise. You are reproducing a bounded historical audit, not estimating a new prevalence of misuse.

## Tasks

1. Run the audit from the repository root:

   ```sh
   python3 sources/aer-audit/coding-audit.py
   ```

   The default run needs only committed CSVs and computes arithmetic diagnostics. `--raw-dir` is optional and requires separately retrieved historical source files; a default run does not repeat the earlier raw-source checksum and transcription checks.

2. Using the [question dictionary](../sources/aer-audit/coding-questionnaire.csv) and [137-row matrix](../sources/aer-audit/coding-1990s-paper-scores.csv), independently calculate the Q16 adverse count/proportion, the Q7 × Q16 cross-tabulation, and Q9's affirmative rate both over all 137 rows and conditional on Q8 = 1. Explain which question each denominator answers. Do not automatically translate every adverse item into “no magnitude reasoning”.
3. Compare matrix Q14/Q15 percentages with the [final JSE version check](../wiki/evidence/jse-2004-version-check.md). Record the observed discrepancy without inventing its cause. Explain why the final JSE and EJW 1980s Q7 entries must be distinguished.
4. Inspect the 1980s row-total anomaly and the omission-list overlap. For each, write one warranted conclusion and one conclusion that would overreach. Do not count author rows as independent miscoded papers or assume every listed omission satisfies a verified eligibility rule.
5. Build a two-case ledger using [final Darby](../wiki/evidence/darby-final-followup.md) and [final Bernheim–Wantz](../wiki/evidence/bernheim-wantz-final-followup.md). For each, give the exact disputed allegation, published version and printed locator, evidence bearing on it, a narrower surviving concern, and what would require replication. Include one correction to the original critique and one qualification of the defence. Consult the linked [supporting catalogue](../sources/aer-audit/supporting-materials.md); do not assign a working-paper DOI to the final article.
6. Read the [expanded-matrix search](../wiki/evidence/expanded-matrix-followup.md). Can you subtract earlier counts from rounded book percentages and recover the 50 added papers' codes? Explain both the mathematical non-uniqueness and the unverified version assumptions. Specify the records needed for a proper follow-up.

**Submit:** a reproduction table, a two-case evidence ledger and a 500-word assessment of what remains unresolved. Label your ledger's documentary claims as based on the repository's existing reading record unless you actually obtain and consult the primary passages yourself. A primary-source reading, a note-based exercise and an empirical replication are different accomplishments.

<details>
<summary>Self-check and discussion guide</summary>

**Project reproduction:** Q16 has 25 affirmative codes and 112 adverse codes: 112/137 ≈ 81.7518%. The Q7 × Q16 cells are (0,0): 80; (0,1): 7; (1,0): 32; (1,1): 18. Q9 has five affirmative codes: 5/137 ≈ 3.65%, or 5/11 ≈ 45.45% conditional on Q8 = 1. All five Q9 positives fall within those eleven rows. Check the instrument's conditional meaning before interpreting either denominator.

The matrix gives Q14 = 39/137 ≈ 28.5% and Q15 = 35/137 ≈ 25.5%; the checked final JSE tables reverse these values. The 1980s Q7 value is 47.3% in the checked final JSE version, while the checked EJW table gives 13.2%. The [version ledger](../wiki/evidence/jse-2004-version-check.md) supports reporting those specific observations, not a reconstructed explanation.

There are 281 author–paper rows, of which 42 total 20 responses despite 19 items. This is an unexplained record inconsistency, not 42 proven independent miscoded papers. The omission list has 82 rows against the rejoinder's stated 81; Simon appears in both an omission and a scored list. The [coding audit](../wiki/evidence/aer-coding-audit.md) records the provenance and limits. The discrepancy does not show that all omissions were fictitious.

**Project interpretation of the documented source readings:** Darby's final pp. 311–312 translate a coefficient into growth magnitudes, and p. 315 discusses an economically interpretable difference. This contradicts a blanket absence-of-magnitude description. Oil-term exclusion and non-rejection-as-absence still require scrutiny; the existence of later magnitude calculations does not validate selection. The defence's interval-containment argument is not a reported covariance-aware cross-equation test. See the [Darby ledger](../wiki/evidence/darby-final-followup.md).

Bernheim–Wantz final pp. 543–544 interpret magnitudes; p. 547 Table 4 contains magnitude estimates, and footnote 17 reports direct tests of differences. The star labels an alternative comparison, not a significance tier. Thus a critique based solely on missing magnitudes or separate significance labels misdescribes the checked final passages. Within-regime non-rejection still does not establish practical equivalence, and no causal identification claim has been replicated. See the [Bernheim–Wantz ledger](../wiki/evidence/bernheim-wantz-final-followup.md).

Rounded column percentages cannot identify individual rows or joint coding patterns. Subtracting older totals would additionally assume unchanged codes, eligibility, applicability and denominators for retained papers. Required follow-up includes a versioned 187-paper roster/matrix, the 50-paper crosswalk, coding rules, item-to-passage rationales and independent coding checks. Failed retrieval is not proof that the records never existed. These selected cases do not supply a corrected corpus-wide misuse rate.

</details>

[Exercise index](README.md) · [Next: finance and identification](05-finance-identification.md)
