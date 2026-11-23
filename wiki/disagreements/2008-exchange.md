# The 2008 exchange: claims, concessions and unresolved disagreements

**Status:** integrated close-reading ledger and provisional project critique, 24 October 2026. This is not an independent audit of the original AER papers, a settled synthesis or approval of the slide gate.

The evidence comes from [Hoover and Siegler's initial article](../papers/hoover-siegler-2008-sound.md) (**S**, pp. 1–37), [McCloskey and Ziliak's reply](../papers/mccloskey-ziliak-2008-reply.md) (**R**, pp. 39–55), and [Hoover and Siegler's rejoinder](../papers/hoover-siegler-2008-rejoinder.md) (**J**, pp. 57–68). Complete readings were supplied respectively by `debate_sources`, `inference_sources` and the root researcher. All locators below use printed pagination. Reading these articles does not establish the accuracy of their descriptions of other research.

**Source claim:** J, p. 65, states that the book was unavailable when the article and rejoinder were written. The exchange therefore must not be presented as a full review of [*The Cult of Statistical Significance*](../papers/ziliak-mccloskey-2008-cult.md). That book requires its own reading and evidence trail.

## Matched evidence ledger

The table records **attributed source claims**, including concessions. It does not endorse either side's account of the other.

| Question | Initial article: S | Reply: R | Rejoinder: J |
|---|---|---|---|
| What does significance establish? | Importance and measurement precision differ; both matter (p. 2). | Rejects thresholds as necessary or sufficient for importance (pp. 39, 41). | Distinguishes testing's usefulness from substantive importance (pp. 57–59). |
| Can weak evidence justify action? | Asymmetric losses can justify responding to weak signals (p. 15). | Defends action under imperfect information; allows considered p-levels and power (pp. 43, 49). | Accepts contextual losses but asks whose losses govern science (p. 59). |
| Must science specify losses? | Questions a universal practical loss-function requirement (pp. 18–19). | Invokes scientific judgement; rejects exclusively monetary losses (p. 52). | Distinguishes shared understanding from contextual uses of knowledge (pp. 59, 67). |
| Do intervals resolve the dispute? | Emphasises test–interval correspondence (p. 20). | Intervals encourage magnitude assessment but cannot supply judgement (p. 50). | Mathematical correspondence challenges categorical rejection of tests (pp. 60–61). |
| What population does a time series represent? | Defends conditional, model-based hypothetical populations (pp. 20–23). | Questions that reasoning; describes one realised path as N = 1 (pp. 49–50). | Defends probabilistic modelling and counterfactual reasoning (p. 60). |
| What justifies specification choices? | Defends diagnostics and qualified specification search (pp. 24–26). | Challenges significance-led selection and its consequences (pp. 46–48). | Treats model adequacy as a necessary concern (p. 60). |
| Do the audits establish widespread confusion? | Disputes selection and scoring; omissions need not change results (pp. 5–7; n. 3, pp. 31–32). | Acknowledges omissions and weighting difficulties; defends access arrangements (pp. 45–46). | Challenges construct validity, weighting, calibration and coding transparency (pp. 65–66). |
| What do cross-field comparisons show? | Offers keyword searches and physical-science examples (pp. 27–30). | Concedes overstatement about physicists; disputes search denominators (pp. 50–52). | Challenges that response and its evidential implications (pp. 61–62). |

## Project interpretation: where agreement ends

**Magnitude, uncertainty and decisions.** A useful reading separates the numerical magnitude of an estimate, the unknown effect it estimates, and the consequences of acting. Changing an estimate's standard error does not change its displayed numerical value, but it changes what that estimate supports about an unknown parameter. Defining an economically relevant benchmark can precede statistical analysis; establishing that an unknown effect exceeds it needs evidence. A rational decision additionally requires actions, consequences and an evaluation rule. These are the distinct propositions in [C001](../claims/C001-independence.md), [economic significance](../concepts/economic-significance.md) and [decisions](../concepts/decisions.md).

The concessions in the ledger prevent a simple opposition between advocates of judgement and advocates of mechanical rules. Yet charitable reconstruction must not erase stronger assertions. R's categorical separation of sampling precision and magnitude on p. 43 deserves examination; S's language on p. 25 risks making significance a prerequisite for interpreting magnitude. Neither formulation should replace the more careful distinction between descriptive size and uncertainty about a target. [C006](../claims/C006-noisy-magnitudes.md) retains that distinction.

**Action and general knowledge.** Evidence reusable by people with different objectives need not encode one person's utility function. Conversely, disagreement about a universal scientific loss function does not discredit explicit losses for particular investment or treatment choices. A shared evidential standard and a locally optimal action answer different questions. The important unresolved issue is how to connect them without assuming that either consensus or private utility determines scientific truth. [C002](../claims/C002-action-without-rejection.md) concerns the possibility of justified action without conventional rejection, not a recommendation always to act on uncertain estimates.

**Intervals and communication.** Matched tests and confidence sets can carry equivalent mathematical information while encouraging different comparisons. An interval assessed against an economically meaningful region can foreground questions that a significance badge obscures. An interval assessed only for exclusion of zero can reproduce the same binary habit. Formal correspondence therefore neither proves nor disproves a communicative advantage. That advantage is an empirical proposition requiring evidence, as distinct from the logical limits of interval interpretation. See [C007](../claims/C007-intervals.md) and [intervals](../concepts/intervals.md).

**Model-based inference and specification.** One realised stochastic path need not contain only one informative observation. Its information depends on dependence, stability, measurement and identification assumptions. Equally, calling observations a sample does not establish transportability or validate a causal interpretation. Residual diagnostics can reveal problems without proving every remaining assumption. Dropping a relevant confounder and dropping an irrelevant predictor have different consequences; neither an unconditional defence nor an unconditional condemnation of selection is adequate. The relevant conditions belong in [statistical inference](../concepts/statistical-inference.md) and [C009](../claims/C009-identification.md).

## Project critique: technical claims also require checking

Several local formulations should not become teaching rules. The complete reading visually confirmed S's p. 14 statement that power approaches zero near the null. For a continuous two-sided normal test with fixed size alpha, power instead tends to alpha as the alternative approaches the null. S's p. 17 description of a near-zero t-statistic under vanishing regressor variation also needs correction: the noncentrality tends to zero, while the standardised statistic remains random under the stated-style Gaussian model. These corrections preserve the valid warning that an unstable point estimate need not reveal the true magnitude.

A separate issue is J's p. 58 parenthetical identification of a p-value with the probability of a Type-I error. The observed p-value, a procedure's pre-specified error rate alpha, and a posterior probability of a hypothesis are distinct quantities. Use the [ASA statement](../papers/wasserstein-lazar-2016.md) as a definitional check. Finding these mistakes does not establish that every argument in the exchange fails; overlooking them because a paper supplies a useful counterposition would equally undermine balance.

For R's p. 48 selection argument, the question is which variable is removed, under what model, and how selection affects subsequent inference. For the subgroup discussion in S, pp. 9–10, significance in one group alone cannot establish a between-group difference. The [bounded case audit](../evidence/aer-darby-woodbury.md) now applies these checks to selected original or explicitly identified draft sections, without a full-study verdict.

## Evidence needed before adjudication

The empirical disagreement in [C004](../claims/C004-practice-and-validity.md) remains open. An audit needs a reproducible article universe; explicit definitions of each scoring item; passage-level mappings; independent raters and calibration; and sensitivity to weights, dependence among items and exclusions. Correcting an omission list does not by itself overturn an audit. Conversely, finding defects in an audit does not establish good practice throughout a profession.

The five AER cases discussed in S, pp. 8–13, now have matched [case ledgers](../evidence/aer-macro-finance-addiction.md), with subsequently supplied [final Darby](../evidence/darby-final-followup.md) and [final Bernheim–Wantz](../evidence/bernheim-wantz-final-followup.md) texts now checked directly. These strengthen specific contextual corrections without establishing the underlying economic mechanisms. Purposively chosen counterexamples may challenge universal accusations without estimating prevalence. Counts of search hits, articles and coefficients are different quantities: plausible invented denominators cannot establish observed reporting rates. S's n. 21, p. 34, itself discloses a corpus mismatch in its interval comparison.

Historical assertions about Fisher and Gosset, the aspirin example, and claims of practical harm require separate primary-source trails. They remain attributed allegations. The next review should identify which disagreements concern facts, which concern statistical conditions, and which concern the purposes of inquiry. Complete readings improve that review's foundation; they do not clear the [review gate](../../reviews/review-gate.md).

[Competing positions](methodological-positions.md) · [Synthesis framework](../../synthesis/argument-framework.md) · [Wiki home](../index.md).

## Subsequent documentary audit

The [coding audit](../evidence/aer-coding-audit.md) reproduces earlier arithmetic while identifying unresolved table, score and omission discrepancies on both sides. The [book ledger](../evidence/cult-2008-reading.md) records the expanded 187-paper survey and qualifies the methodological interpretation. The [revised synthesis](../../synthesis/critical-synthesis.md) separates accurate description, justified method and true conclusion. No corrected population misuse rate or full-book verdict follows.
