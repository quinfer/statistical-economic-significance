# Power, selection and magnitude errors

**Illustration.** You are designing a study of a programme’s effect on eligible borrowers’ one-year default rate. Suppose the true reduction is 0.50 percentage points. An unbiased normal estimate will have a known standard error of 0.40 percentage points. With a two-sided 5% test of zero, how often would you expect the study to reject? What will the estimates look like if you only see the studies that do reject?

The test rejects when the estimate is more than 1.96 standard errors from zero in either direction. Under the proposed design, the threshold is about 0.78 percentage points in absolute value. If the true reduction is 0.50, the test rejects about 24% of the time. Every selected estimate in this example has an absolute magnitude greater than the true magnitude, and a few selected estimates will be negative. The unselected estimator is unbiased by assumption. The selection rule changes which draws you see. [Exercise on power and selection](../../exercises/03-power-selection.md)

## What changes if the design gets more precise?

**Illustration, continued.** Cut the standard error to 0.20 percentage points while keeping the effect fixed. Power rises to about 71%, and the selection threshold falls to about 0.39 percentage points. A selected estimate can now be smaller in absolute value than the true effect.

**Project interpretation.** Power describes how often a test rejects at a specified true effect under a specified design. With greater precision in the example, smaller estimates can pass the screen, and rejection becomes more likely. Whether the design identifies the intended effect is a separate question. [Is a large estimate enough?](../claims/C006-noisy-magnitudes.md) · [Finance](finance.md)

**Open question.** Would you design the study around an effect of 0.50 percentage points? Explain where that number came from. Then sketch how you would estimate wrong-sign risk among significant results at two plausible values of the true effect. In the labs, the proposed true effects are inputs to the simulation. Their results describe the specified synthetic models. [Power and selection labs](../../simulations/README.md) · [Simulation evidence boundary](../evidence/simulation-labs.md)

## Evidence and further reading

- **Source claim.** Gelman and Carlin evaluate the chance of a wrong sign and the extent of magnitude exaggeration conditional on passing a significance screen. Their design analysis uses plausible effects justified independently of the focal estimate. [Gelman and Carlin](../papers/gelman-carlin-2014.md)
- **Source claim.** Hoenig and Heisey critique the interpretation of post-experiment power. Compare their objection to using the observed estimate as an input with Gelman and Carlin’s use of external inputs when assessing a design. Lakens connects sample-size justification to what the design should establish. [Hoenig and Heisey](../papers/hoenig-heisey-2001-power.md) · [Lakens on sample size](../papers/lakens-2022-sample-size.md)

[Wiki home](../index.md)
