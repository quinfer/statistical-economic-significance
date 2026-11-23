# Critical synthesis: argument framework

**Status: pre-synthesis framework, awaiting deeper reading and critical review.** No final verdict is asserted. The [positions map](../wiki/disagreements/methodological-positions.md) and [claim records](../wiki/index.md) specify initial evidence trails.

## Disaggregate the central question

| Question | What an answer requires | What does not follow automatically |
|---|---|---|
| What magnitude would matter? | Units, target population, horizon, relevant alternatives, costs and normative criteria | The population effect has that magnitude |
| What magnitude does the evidence support? | Estimation and identification arguments with appropriate treatment of uncertainty and selection | A particular action is preferred |
| What should an actor do? | Feasible actions, consequences, information and a defensible decision criterion | A causal proposition or point estimate has been established |

This is a **project framework**, motivated by [C001](../wiki/claims/C001-independence.md) and [C002](../wiki/claims/C002-action-without-rejection.md). It must not be used to stipulate away disagreements over what “established” or “inference” means.

## Competing hypotheses

**H1a: conventional statistical significance is necessary for economic significance.** Test necessity separately for defining a meaningful magnitude, supporting a population-effect claim and choosing an action. A decision without rejection can challenge a prerequisite for action; it does not by itself establish the underlying population magnitude.

**H1b: conventional statistical significance is sufficient for economic significance.** A precisely estimated but negligible effect is a counterexample to sufficiency. It is not a counterexample to necessity. Both hypotheses require an explicit meaning of economic significance.

**H2: substantive magnitude can replace inferential reasoning.** Test this against noisy estimates, selection, wrong signs, uncertainty around costs, and identification failures. A defensible version may concern defining a benchmark or describing an observed accounting total, rather than an unknown population or causal effect.

**H3: significance testing is dispensable in many decisions, while uncertainty and identification remain relevant.** This is a promising working position, not the predetermined answer. Probe its limits: robust dominance may make a decision insensitive to some uncertainty, and an exactly observed finite-population total may not require sampling inference for that descriptive target. Measurement uncertainty, extrapolation and counterfactual claims can reintroduce other problems.

**H4: no single replacement is best across discovery, estimation, communication and action.** Assess whether this becomes an empty pluralism. Specify task-dependent standards and costs rather than merely recommending every method.

## Formal distinction to develop later

Let theta denote an economic effect, delta a meaningful magnitude threshold, D the data, and a an action. Comparing an estimate with delta, evaluating evidence about theta > delta, and choosing an action to maximise posterior expected utility are different operations. For a data-dependent decision rule, expected regret at a state compares its expected welfare, averaged over the sampling distribution of D at that state, with the best welfare achievable if the state were known. A minimax-regret criterion chooses the rule minimising the maximum expected regret across feasible states. Distinguish this ex ante evaluation of a rule from choosing an action after observing D. Neither criterion generally reduces to testing theta = 0 at .05. This paragraph is **project mathematical framing**, not a quotation from unread Wald chapters.

The review should also ask whether delta is fixed, uncertain, context-dependent or an inadequate summary of heterogeneous welfare. An inference about an average coefficient may not answer the economically relevant distributional question.

## Proof obligations before a conclusion

1. Read the matched 2008 exchange and distinguish concessions from alleged positions. Do not infer the book's detailed argument from its title or publisher description.
2. Audit claims about empirical practice separately from claims about testing's logical utility.
3. Compare interval and testing proposals under explicit assumptions, including equivalence margins and multiple testing.
4. Evaluate at least one decision example where action is warranted without conventional significance, and one where a large estimate is too uncertain or poorly identified to support the magnitude claim.
5. Compare competing finance replication designs and specify what would change the interpretation.
6. Address counterexamples and the 2024–2026 coverage gap; record unresolved disagreements in the final synthesis.

The current evidence supports taking these distinctions seriously. It does not establish the causal effects of statistical practices on jobs, justice, welfare or realised investment performance.

[Roadmap](../planning/roadmap.md) · [Review gate](../reviews/review-gate.md) · [Training plan](../training/README.md).

## Subsequent development

This file preserves the initial hypotheses. The [substantive synthesis](critical-synthesis.md) now implements the matched exchange, targeted 2024–2026 update and deterministic counterexamples. It narrows the independence claim, rejects a universal rejection prerequisite for action, and adds a compatible nested-test case where meaningful-effect certification entails zero-null rejection. Direct book excerpts and a bounded original AER audit are now incorporated, with full-book reading, complete recoding, underlying replications and several recent proofs still open; the slide gate remains closed.
