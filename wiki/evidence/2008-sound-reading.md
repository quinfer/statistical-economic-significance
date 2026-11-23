# Close reading: Hoover and Siegler (2008), Sound and fury

**Source ID:** `hoover-siegler-2008-sound`
**Reader:** `debate_sources`
**Date:** 24 October 2026
**Status:** Complete-article reading; independent source-audit and methodological review remain pending. The slide gate remains CLOSED.

Hoover, Kevin D., and Mark V. Siegler. 2008. Sound and fury: McCloskey and significance testing in economics. *Journal of Economic Methodology* 15(1): 1–37. DOI: [10.1080/13501780801913298](https://doi.org/10.1080/13501780801913298).

[Consulted published article on the author's Duke website](https://public.econ.duke.edu/~kdh9/Source%20Materials/Research/%24Sound%20and%20Fury%20Published%20Version.pdf).

## Access and actual coverage

The publicly available author-hosted PDF was downloaded to temporary storage for private research after a network escalation succeeded. Initial sandboxed retrieval failed because the host could not be resolved; this was not a paywall finding. Neither the PDF nor its complete extracted text should be committed to the repository.

All printed pages 1–37 were read from locally extracted text: main text and acknowledgements on pp. 1–31; all 25 endnotes on pp. 31–34; references on pp. 34–37. Tables 1, 2 and 3 were read. The file has a publisher cover followed by 37 numbered article pages. The association between PDF index and printed pagination was checked against page headers/footers; printed locators below are not inferred solely from viewer position.

`pypdf` reported malformed object-pointer warnings, but returned text for all 38 PDF pages. Extraction corrupted some mathematical symbols and superscripts, broke ligatures and occasionally moved table material ahead of or behind surrounding paragraphs. Selected page images were therefore inspected: printed pp. 3, 13, 14, 17, 25, 26, 27, 29, 31, 33 and 34. These resolve the principal equations, tables, technical formulations and caveats used below. For example, p. 13's modulus is square-root-of-two times the standard deviation; p. 25 uses Omega for its set notation; p. 34 n. 19 has a negative exponent that text extraction lost. There are no known unread article sections. Not every page was visually inspected, and reading the references does not mean reading the cited works.

No original AER case paper, original survey coding sheet, omitted-paper list, historical statistical text, medical trial or specification-search simulation was independently audited in this assignment. The earlier working-paper version and its omitted textbook discussion were not read. Accordingly, `full_text_read` records coverage of this article only, not the truth of its empirical allegations or the completeness of the wider evidence trail.

## Compact evidence ledger

Each entry is a **Source claim** attributed to Hoover and Siegler, not an adjudicated finding. The brief propositions are deliberately separated from our analysis.

| ID | Printed locator | Source claim | Kind |
|---|---|---|---|
| S01 | p. 2 | Importance differs from precision; both matter. | Conceptual concession |
| S02 | pp. 5–7 | Survey selection, weighting and interpretive reproducibility are disputed. | Empirical/methodological objection |
| S03 | pp. 8–13 | Five selected case readings challenge accusations of confusion. | Empirical allegation |
| S04 | pp. 14–15 | Testing depends on a statistical model. | Inferential condition |
| S05 | p. 15 | Asymmetric losses can justify responding to weak signals. | Decision concession |
| S06 | pp. 16–17 | More data need not preserve the initial estimate. | Statistical argument |
| S07 | pp. 18–19 | Scientific understanding need not share one practical loss function. | Philosophical argument |
| S08 | p. 20 | Test–interval equivalence challenges a blanket rejection of tests. | Logical argument |
| S09 | pp. 20–23 | Generalisation can involve hypothetical populations, subject to modelling conditions. | Inferential argument |
| S10 | pp. 24–26 | Specification testing and qualified search can improve measurement. | Methodological defence |
| S11 | pp. 27–30 | Physical-science examples counter claims that testing is absent. | Empirical allegation |
| S12 | pp. 30–31 | Tests contribute to cumulative evidence; other errors can dominate. | Scope concession |
| S13 | pp. 31–32, n. 3 | Omitted papers need not change survey results. | Empirical caveat |
| S14 | p. 34, n. 21 | Confidence-interval search counts use a different article universe. | Comparability caveat |

## Project interpretation: what survives a strong challenge

S01, S05 and S12 make an indiscriminate defence of the five-per-cent convention an inadequate representation of this paper. The most defensible reconstruction is that assessing a noisy estimate requires attention to its uncertainty and the model generating it. That is weaker than requiring rejection of a zero null before an empirical magnitude may be discussed, or before action is rational. Our synthesis should preserve this separation even where the paper's rhetoric is less careful.

S06 can be retained without committing to a particular significance rule. An estimate with large sampling variability is not made accurate by attaching an important economic interpretation to its numerical value. Equally, uncertainty assessment need not take the form of a binary zero-null decision. A credible counterposition should combine effects, uncertainty and an explicit inferential or decision objective.

S07 raises a genuine question about the audience for scientific evidence. Evidence intended for multiple decision-makers need not encode one person's utilities. However, the infeasibility of a single universal loss function does not show that local decisions about treatment, investment or research design cannot benefit from explicit losses. Neither side receives a general victory from that distinction alone.

## Project mathematical checks and tensions

These are our mathematical analyses, not additional findings attributed to the article. They were triggered by the indicated passages and do not adjudicate the underlying AER cases.

### Fixed-size power near the null: p. 14

The printed phrase **“power approaches zero”** was visually confirmed. For a two-sided normal test with fixed size alpha, statistic Z distributed as N(delta, 1), and cutoff c = Phi-inverse(1 − alpha/2),

`power(delta) = 1 − Phi(c − delta) + Phi(−c − delta)`.

Consequently, power approaches alpha as delta approaches zero. At alpha = .05, deterministic evaluation gives approximately .170075 at delta = 1, .051146 at .1, .050011 at .01, and .050000 at zero. Type-II error correspondingly approaches .95, not one. This is a local technical error in the general formulation, not a refutation of the broader point that power against nearby alternatives is weak. No random simulation or empirical data were used in this calculation.

The same page's use of 1.96 in its discussion of a t-statistic also needs a qualification: 1.96 is the two-sided standard-normal five-per-cent cutoff, while a finite-degrees-of-freedom Student-t cutoff differs. Normal errors alone do not make 1.96 exact when variance is estimated. This is a secondary expository issue.

### Small regressor variation: p. 17

The page's **“t-statistic near zero”** wording was visually confirmed. Under a correctly specified Gaussian linear model with fixed residualised regressor sum of squares Sxx and known sigma, we can write

`beta_hat = beta + sigma Z / sqrt(Sxx)`;

`se(beta_hat) = sigma / sqrt(Sxx)`;

`beta_hat / se(beta_hat) = beta sqrt(Sxx) / sigma + Z`, where Z is N(0, 1).

As Sxx tends to zero with beta fixed, the noncentrality tends to zero, but the statistic remains random; it does not converge deterministically to zero. With estimated sigma the corresponding finite-sample statement involves a central t distribution. The substantive warning about an unstable raw coefficient survives this correction. At exact collinearity the coefficient is unidentified; calling its standard error infinite is a limiting intuition, not a literal output of an identified regression.

### Precision is different from distance from zero: p. 25

The language near the end of the penultimate paragraph risks turning significance into a prerequisite for interpreting economic magnitude. Consider our expressly synthetic numerical illustration: estimate zero, standard error .001, approximately normal sampling model, and an economically negligible region of [−.01, .01]. The 95% interval [−.00196, .00196] is narrow relative to that region even though the zero-null p-value is one. A failure to reject zero therefore does not invariably imply economically uninformative imprecision. Meaningfulness depends on the estimand, units, calibrated interval and justified margin. This example is a logical illustration, not evidence about markets, policies or any paper's empirical results.

### Heterogeneity and the case discussion: pp. 9–10

One subgroup crossing a significance threshold while another does not is insufficient to establish a difference between groups. A direct contrast requires its own uncertainty calculation, including covariance where relevant. Applying that check to the Woodbury–Spiegelman discussion is necessary, but no verdict about the original trial follows here: its estimates, covariance structure and original arguments have not been audited. Keep this question separate from whether the original authors appreciated economic magnitudes.

### Formal duality and communication: p. 20

Matched confidence sets and tests can encode the same mathematical information without eliciting the same reasoning from readers. A claim of formal equivalence does not settle whether presenting intervals against meaningful economic margins improves interpretation. Conversely, converting a test into an interval and then inspecting only whether zero is excluded simply recreates the original threshold. Any teaching recommendation should specify which comparison the interval is intended to support.

### Specification and search: pp. 23–26

Diagnostics can reveal departures from a model without proving that its remaining assumptions hold. A model-selection consistency result requires its precise candidate-set, identification, test, sample-size and critical-value conditions; successful recovery under an assumed data-generating process does not establish reliable selection when every candidate model is wrong. The original White result and cited Monte Carlo studies must be read before making claims about particular algorithms. Policy coefficient interpretation additionally requires identification assumptions that a well-behaved residual distribution does not supply.

## Empirical audit queue: disputes must remain open

The following are document targets identified from the article, not newly verified or read sources. The printed locators point to Hoover and Siegler's discussion, not the underlying original paper.

| Audit target | Locator | Question for independent audit |
|---|---|---|
| Survey universe and omitted-paper lists | pp. 5–7; n. 3, pp. 31–32 | Can a pre-specified eligibility rule reproduce each universe, and what changes after recoding? |
| Survey score-to-passage mapping | pp. 6–7 | Are classifications recoverable with calibrated independent raters? |
| Darby (1984) | p. 8; n. 6, p. 32 | Which claims depend on magnitudes, specification tests or both? |
| Woodbury and Spiegelman (1987) | pp. 8–10 | Are efficacy, heterogeneity, benefits and uncertainty treated distinctly? |
| Bernanke and Blinder (1992) | p. 10 | Are predictive distribution questions distinguished from economic and causal interpretation? |
| Bernheim and Wantz (1995) | p. 11 | Are sign, timing and magnitude claims characterised accurately by both sides? |
| Becker, Grossman and Murphy (1994) | pp. 11–13; nn. 8–9, p. 32 | What evidence bears on model discrimination, elasticities and substantive plausibility? |
| Aspirin trial and cited secondary accounts | p. 16; n. 12, p. 33 | What outcome and stopping rule did the original trial actually report? |
| Confidence-interval searches | p. 20; n. 21, p. 34 | Do counts measure actual use, and are denominators comparable? |
| Physical-science searches and examples | pp. 27–30; Tables 2–3 | Do keyword hits indicate proper testing, and what can an unsystematic example set establish? |
| Historical accounts of Edgeworth and Fisher | pp. 13–14; nn. 10–11, pp. 32–33 | Do original texts support the disputed historical characterisations? |

Our interpretation: counterexamples can defeat universal accusations but cannot estimate the prevalence of good or bad practice. An audit of five purposively chosen examples and a representative population estimate answer different questions. Likewise, doubts about survey validity do not establish that the opposite prevalence claim is true. The article's own empirical case therefore needs the same traceability demanded of its opponents.

## Further integrity observations and next step

The printed text of n. 23 on p. 34 places papers dated 1983 and 1985 in discussion of the 1990s survey. This is an apparent internal decade error, visually confirmed, that should be checked against the linked omission list before reuse. Do not silently repair it or infer misconduct. Reference-list entries and historical citations were read but not independently validated.

Next integrate this note with close readings of the reply and rejoinder, then build a claim-by-claim disagreement matrix. Retain the three distinct tracks: logical validity, normative decision criteria, and observed scholarly practice. The successful full reading changes coverage status; it does not close any unresolved dispute or approve slide production.

[Matched exchange](../disagreements/2008-exchange.md) · [Paper index](../papers/index.md) · [Critical synthesis](../../synthesis/critical-synthesis.md).

## Later evidence

The access/audit limits above describe this exchange-only reading pass. A subsequent [book reading](cult-2008-reading.md), [coding audit](aer-coding-audit.md) and case ledgers for [Darby/Woodbury–Spiegelman](aer-darby-woodbury.md) and [three further cases](aer-macro-finance-addiction.md) now provide bounded independent documentary checks. They do not amount to complete recoding, empirical replication or verification of historical/medical harms.
