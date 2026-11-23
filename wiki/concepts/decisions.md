# Decisions under uncertainty

**Project framework.** A decision requires a feasible action set and an evaluation of consequences. Bayesian expected utility uses a posterior and preferences to choose an action conditional on data. A data-dependent decision rule can instead be evaluated before the data are observed: its expected regret at a state is the gap between the best welfare attainable knowing that state and its welfare averaged over the state's sampling distribution. A minimax-regret rule minimises the maximum expected regret across feasible states. State the sampling model and benchmark. Choosing a realised action and evaluating a statistical rule are distinct tasks.

**Source trail:** [Manski 2019](../papers/manski-2019-treatment-choice.md) directly contrasts treatment choice with hypothesis testing; [Manski 2021](../papers/manski-2021-econometrics-decisions.md) broadens model-based evaluation. [Kandel–Stambaugh](../papers/kandel-stambaugh-1996-asset-allocation.md) provides an investment application at abstract-level reading. [Wald](../papers/wald-1950-decision-functions.md) remains unread.

**Open questions:** whose welfare or loss counts; whether probabilities are credible; whether action is reversible; how learning changes the choice; and whether a preferred action is robust to uncertain costs. A rational choice does not certify a point estimate as accurate. Conversely, an uncertain magnitude need not imply inaction if one action is preferable across the relevant uncertainty set.

[C002](../claims/C002-action-without-rejection.md) · [C001](../claims/C001-independence.md) · [Finance](finance.md) · [Wiki home](../index.md).

## Contemporary qualification

[Aradillas Fernández et al. 2026](../papers/aradillas-fernandez-etal-2026-robust-bayes.md), under its particular prior class and partial-identification setting, distinguishes minimax prior risk from worst posterior regret. Ex ante and ex post robust Bayes rules can disagree; randomisation can be optimal. These are source claims under restrictive assumptions, not a universal prescription. **Project implication:** state when a rule is evaluated, how priors are restricted, what can be identified and which losses are being minimised.

The [checked normal-prior example](../evidence/mathematical-checks.md) demonstrates action without rejection under explicit assumptions. It does not establish the underlying population effect or override other legitimate objectives. [Synthesis](../../synthesis/critical-synthesis.md).

## Documentary examples that sharpen the distinction

The [Woodbury–Spiegelman audit](../evidence/aer-darby-woodbury.md) distinguishes an estimated trial benefit–cost ratio from break-even, subgroup evidence and a policy with different take-up. The [Matrixx primary-opinion check](../evidence/matrixx-2011-lecture-audit.md) distinguishes contextual materiality and adequate pleading from a merits finding of causation. Neither example establishes that uncertainty can be discarded; both identify a decision or evidential question that a zero-null threshold alone cannot answer.
