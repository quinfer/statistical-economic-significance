# Uncertainty beyond sampling

**Illustration.** Two analysts use the same monthly returns to assess a hypothetical strategy. One adjusts for the market. The other also adjusts for size and value factors. Both report tight standard errors, but they disagree about whether the strategy earns a positive alpha. Before deciding which result to report, ask what payoff each model is trying to measure.

## What would resolve the disagreement?

**Project interpretation.** A sampling standard error describes how an estimate varies when the sampling process repeats under the stated model and analysis. In the strategy example, a longer return history might narrow both standard errors while the two intercepts remain different. Adjusting for different risks can change what counts as a return unexplained by the model. Compare the assumptions and the targets before combining or ranking the estimates. [Finance applications](finance.md)

| Issue | Question to ask | What to inspect |
|---|---|---|
| Sampling | How much would the estimate vary in repeated samples? | The sampling process, such as dependence across months |
| Analysis choices | How sensitive is the estimate to defensible choices? | The analysis steps and the quantity each version estimates |
| Identification | Which effects are consistent with the data and assumptions? | The assumptions linking observable returns to the effect or payoff of interest |
| Transportability | Would the result carry over to the proposed trading regime? | Differences in markets, investors, scale and implementation |
| Values and costs | Which gains and risks matter to the investor? | Trading costs, constraints and the investor’s preferences |

Some of these questions concern different targets or disagreements about objectives. Adding variances as if the sources were independent would require a model that justifies treating them as random and independent. Agreement across specifications can be useful once you justify the range of specifications and show that their assumptions bear on the claim. Causal identification still needs its own argument. [Identification](identification.md) · [Uncertainty and choice](../claims/C010-uncertainty-and-choice.md)

**Open question.** Give one reason to use each factor model in the example. Which conclusion could both support? Which would still depend on trading costs even if the estimates agreed? [Critical synthesis](../../synthesis/critical-synthesis.md)

## Evidence and further reading

- **Source claim.** Menkveld et al. examine analyst variation on common data. The project consulted selected sections. [Menkveld et al.](../papers/menkveld-etal-2024-nonstandard-errors.md)
- **Source claim.** Aradillas Fernández et al. consider partial identification and decisions with multiple priors in the framework and conclusion consulted here. Selected passages in Deaton and Cartwright motivate checking whether a study result applies elsewhere. Each source addresses a specific part of the diagnosis. [Aradillas Fernández et al.](../papers/aradillas-fernandez-etal-2026-robust-bayes.md) · [Deaton and Cartwright](../papers/deaton-cartwright-2018-rcts.md)

[Wiki home](../index.md)
