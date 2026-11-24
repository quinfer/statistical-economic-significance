# Equivalence and meaningful margins

**Illustration.** Two studies estimate that a lending programme changes eligible borrowers’ one-year default rate by zero percentage points. Before either study, the lender specifies that changes strictly between −1 and +1 percentage points would be negligible. Assume unbiased normal estimates with known standard errors and valid identification. The standard errors are 0.20 and 1.00 percentage points. Both two-sided tests against zero give a p-value of one. Can both studies support calling the effect negligible?

At the 5% level, the standard two one-sided tests procedure compares the 90% confidence interval with the lender’s bounds. For the more precise study that interval runs from about −0.33 to +0.33 percentage points, wholly inside the negligible range. For the other study it extends from about −1.64 to +1.64. The first supports practical equivalence for the stated margin. The second leaves room for meaningful effects and for negligible ones. [Work through four cases](../../exercises/02-intervals-equivalence.md)

## What are the two tests doing?

**Project interpretation.** The first test takes effects at or below the lower bound as its null. The second takes effects at or above the upper bound as its null. Both must reject at the chosen level, α. In the standard continuous construction with compatible tests, their respective limits form a two-sided confidence interval with coverage 100(1−2α)%. At α = 0.05 that is a 90% interval. Its coverage refers to the procedure over repeated samples. Other equivalence procedures can use a different construction. [Confidence intervals](intervals.md) · [What can a non-significant result tell us?](../claims/C003-equivalence.md)

Defend the margin in units that matter to the application. A wider fixed margin answers a different economic question and can still give a calibrated test for that margin. Choosing a margin after seeing the results can change the error rate of the procedure actually used. Report sensitivity to other defensible margins so readers can judge what depends on that choice. [Economic significance](economic-significance.md)

**Open question.** If the lender only asks whether the reduction is large enough to cover its costs, formulate the one-sided threshold it needs to assess. How does that question differ from asking whether the effect falls within a symmetric negligible range? [Meaningful-effect tests](../claims/C011-nested-meaningful-tests.md) · [Critical synthesis](../../synthesis/critical-synthesis.md)

## Evidence and further reading

- **Source claim.** Schuirmann’s abstract relates two one-sided tests to the corresponding interval in bioequivalence. The Lakens tutorial develops the procedure, and the later tutorial discusses setting bounds in advance. [Schuirmann](../papers/schuirmann-1987-tost.md) · [Lakens](../papers/lakens-2017-equivalence.md) · [Lakens, Scheel and Isager](../papers/lakens-scheel-isager-2018.md)
- **Project interpretation.** The audit of Fitzgerald’s 2025 working paper asks which economic consequences would justify generic standardised margins and what safeguards make an elicitation independent of results. Recruiting independent respondents is one part of that design. The project consulted selected sections, with calculations and applications awaiting replication. [Fitzgerald](../papers/fitzgerald-2025-equivalence.md) · [Critical audit](../disagreements/equivalence-audit.md)

[Wiki home](../index.md)
