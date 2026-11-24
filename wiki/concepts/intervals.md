# Confidence intervals

**Illustration.** A lender regards a reduction of one percentage point in eligible borrowers’ one-year default rate as worthwhile. An estimate of 1.1 percentage points gives a 95% confidence interval of 0.71 to 1.49 when the standard error is 0.20 percentage points. What restrictions does this interval place on a claim that the lender’s benchmark has been met?

Assume the study identifies the effect and the estimate is unbiased and normally distributed with known standard error. The interval excludes zero and contains effects on both sides of the benchmark. Hold the estimate fixed and reduce the standard error to 0.04 percentage points. The interval, calculated as the estimate plus or minus 1.96 standard errors, narrows to about 1.02 to 1.18 percentage points. Under the same assumptions, even its lower bound exceeds the benchmark. [Worked interval comparisons](../../exercises/02-intervals-equivalence.md)

## What does 95% describe?

**Project interpretation.** Imagine repeating the study under the same assumptions and constructing an interval each time. The endpoints vary from study to study. The underlying effect stays fixed. Before sampling, this procedure has a 95% probability of producing an interval that covers that effect. A 95% Bayesian credible interval instead assigns 95% of the posterior probability to its range under a prior and likelihood. [Statistical inference](statistical-inference.md)

For a compatible family of two-sided tests, a confidence interval can be built from the candidate values those tests retain. Reporting the range makes it easy to compare several economic benchmarks at once. Choosing an interval or a test depends on the question. Both rely on the design and model, including how results were selected. [Do intervals solve the problem?](../claims/C007-intervals.md) · [Equivalence](equivalence.md)

**Open question.** If both studies estimated the effect for a different group of borrowers, what evidence would you need before applying either interval to the lender’s target group? [Identification and transportability](identification.md)

## Evidence and further reading

- **Source claim.** Greenland et al. discuss how to interpret confidence intervals. Morey et al. challenge interpretations of a realised interval as a probability statement about its parameter or a ranking of plausible values. The Morey note draws on the abstract and introduction. [Greenland et al.](../papers/greenland-et-al-2016.md) · [Morey et al.](../papers/morey-et-al-2016-intervals.md)
- **Reading limit.** Neyman’s foundational reference is bibliographically verified and awaits substantive reading. [Neyman](../papers/neyman-1937-estimation.md)

[Wiki home](../index.md)
