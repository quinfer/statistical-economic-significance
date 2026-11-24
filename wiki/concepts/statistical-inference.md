# Statistical inference and p-values

**Illustration.** Two studies each estimate a reduction of 0.10 percentage points in the one-year default rate among eligible borrowers. In the first study the standard error is 0.02 percentage points. In the second it is 0.10. Which study gives stronger evidence against zero, and what has changed about the estimated size of the effect?

Assume each study identifies the target effect and gives an unbiased normal estimate with known standard error. For a test of zero, divide the estimate by its standard error. If the null holds, this test statistic has a standard normal distribution. The first estimate is five standard errors from zero and the second is one. The two-sided p-values are about 0.00000057 and 0.32. A shift in precision can therefore change the p-value substantially even when both studies report the same reduction. [Related worked example](../../QUICKSTART.md#check-one-result-by-hand)

## What probability are you calculating?

**Project interpretation.** Specify the null, the model and what counts as an outcome at least as extreme as the one you observed. Here the calculation asks how often the test statistic would be at least as far from zero in either direction if the null and model held. A posterior probability would reverse the direction of the conditioning and require a probability model for the unknown effect. The nominal level, such as 5%, concerns how often a test rejects under the null in repeated use under its assumptions. It gives no case-specific probability that a rejection was a mistake. [Confidence intervals](intervals.md)

**Open question.** Suppose the lender requires a reduction of one percentage point to call the programme worthwhile. Which of these p-values bears directly on that benchmark? Write down the hypothesis and the estimate and interval you would report to answer the economic question. Statistical inference also includes estimation, confidence procedures and Bayesian updating. A policy choice additionally needs an account of consequences. [Economic significance and inference](../claims/C001-independence.md) · [Competing threshold proposals](../claims/C005-threshold-reforms.md)

## Evidence and further reading

- **Source claim.** The ASA statement and Greenland et al. explain how to interpret p-values under model assumptions. The ASA note draws on selected passages, with a full reading of the six principles still pending. [ASA statement](../papers/wasserstein-lazar-2016.md) · [Greenland et al.](../papers/greenland-et-al-2016.md)
- **Source claim.** Imbens distinguishes tasks for reporting statistical uncertainty in applied economics. The project consulted the abstract. [Imbens](../papers/imbens-2021.md)

[Wiki home](../index.md)
