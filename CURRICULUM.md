# A learning pathway through significance

Work through the five modules in order. You will start by specifying an effect and what size would matter, then examine what a study can establish, and finish by advising someone who must decide under uncertainty. Keep one application in mind throughout so you can see which parts of your argument change as you change the design, the assumptions or the decision.

## How to work through a module

Begin with the first-session calculation and evidence trail. You need familiarity with estimates, standard errors and basic probability. The exercises can be worked by hand. For the executable examples and labs, use Python 3.10 or later and its standard library. [Quick start](QUICKSTART.md)

1. **Read the assigned chapter section.** Stop at the opening example and write what you think the researcher needs to establish. Then read the reasoning and note an assumption on which the answer depends. [Critical synthesis chapter](synthesis/critical-synthesis.md)
2. **Use the wiki to resolve a question.** Start with the concept note for the module. When you want to test a claim, follow the claim or paper note to its version, passage and reading depth. Record which material you actually consulted. [Research wiki](wiki/index.md) · [Learning map](resources/learning-map.md)
3. **Attempt the exercise and then check it.** Make a prediction, record the inputs and units, and work through the calculation or argument before opening the worked solution. Keep one explanation you changed after checking it. When a module assigns a lab, compare the simulation with its exact benchmark and use the separate solution to check the interpretation. [Exercises and worked solutions](exercises/README.md) · [Simulation labs](simulations/README.md)

If your background is in economics or finance, begin with a policy or investment question that gives you units, a population and a horizon. If your background is in statistics or computer science, begin with the calculation and explain what each input means in the application. Both routes lead through the same exercises.

## Module 1: Magnitude, evidence and action

A lender wants to know whether a reduction in defaults would matter. Write down what size would matter before looking at the result. Then ask what it would take to establish that size, and what additional information would justify adoption. [Chapter §1, Which claim are you trying to establish?](synthesis/critical-synthesis.md#1-which-claim-are-you-trying-to-establish)

Use the concept and claim notes to distinguish the target quantity you want to learn about, or *estimand*, from the estimate the study produces. As a first evidence trail, follow the ASA statement note and describe what the passages consulted support about interpreting a p-value. [Economic significance](wiki/concepts/economic-significance.md) · [Claim C001](wiki/claims/C001-independence.md) · [ASA statement note](wiki/papers/wasserstein-lazar-2016.md)

**Your work.** Complete Exercise 1. Add an observed-data claim to the three sentences you wrote in the quick start. Your claim map should now distinguish a worthwhile benchmark, what was observed, an unknown effect and a choice of action. For an application of your own, state units, population, horizon, aggregation and whose gains or losses count. Give two settings where the same estimate would have different economic importance. Keep the one-page map, calculation table and short argument specified in the exercise. [Exercise 1 and worked solution](exercises/01-magnitude-evidence-action.md)

**Check before moving on.** Explain why a large estimate can leave the effect uncertain. Give an example of a fully observed quantity you could describe without sampling extrapolation, and say what you would still need to check about its measurement.

## Module 2: Intervals, meaningful thresholds and equivalence

What evidence would distinguish a negligible effect from an imprecisely estimated one? Compare the intervals in the chapter with both zero and the proposed limits for a negligible effect. Then ask what makes those limits defensible. [Chapter §2, Evidence about the benchmark](synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Chapter §4, Setting a margin worth testing](synthesis/critical-synthesis.md#setting-a-margin-worth-testing)

If the two comparisons look inconsistent, revisit what each hypothesis asks and how the confidence levels relate to the tests. The audit of Fitzgerald’s working paper is a more advanced follow-up. Check which parts were read and what would require replication. [Intervals](wiki/concepts/intervals.md) · [Equivalence](wiki/concepts/equivalence.md) · [Lakens’s tutorial note](wiki/papers/lakens-2017-equivalence.md) · [Claim C011](wiki/claims/C011-nested-meaningful-tests.md) · [Equivalence audit](wiki/disagreements/equivalence-audit.md)

**Your work.** Complete Exercise 2 and produce its four-case table and short interpretation. Report the interval levels, the comparison with zero and the equivalence margin in natural units. Change the margin for a fixed estimate, then use the quick-start example to change the standard error at a fixed margin. In each case explain which scientific question or which piece of evidence has changed. [Exercise 2 and worked solution](exercises/02-intervals-equivalence.md) · [Quick-start comparison](QUICKSTART.md#check-one-result-by-hand)

**Check before moving on.** Explain coverage under repeated sampling, why the compatible 5% two one-sided tests use a 90% interval, and how equivalence can fail when the true effect is zero. Describe the specific one-sided procedure in which a lower bound above a positive benchmark also rules out zero.

## Module 3: Power, selection and noisy magnitudes

Suppose only results that reject zero are reported. Before looking at the selected estimates, ask how often the design would reject for a plausible effect and which estimates pass the screen. Read the chapter’s example about precision and its discussion of the power limit near the null. [Chapter §2, Evidence about the benchmark](synthesis/critical-synthesis.md#2-what-do-the-data-tell-you-about-the-benchmark) · [Chapter §3, Competing arguments](synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree)

Use the wiki to distinguish the unconditional behaviour of the estimator from the behaviour of reported results. Gelman and Carlin’s note documents design analysis at externally justified effects. The Hoenig and Heisey note records abstract-level coverage. Check the locators and reading limits when you compare their questions. [Power and selection](wiki/concepts/power-selection.md) · [Gelman and Carlin](wiki/papers/gelman-carlin-2014.md) · [Hoenig and Heisey](wiki/papers/hoenig-heisey-2001-power.md)

**Your work.** Complete Exercise 3. In your design note, state the estimand, plausible true effects, standard errors and selection rule. Use the power table and selection bound to explain the risks of false discoveries, missed useful effects, wrong signs and exaggerated magnitudes. Say what using the observed estimate as a power input can tell you and what requires separate evidence. [Exercise 3 and worked solution](exercises/03-power-selection.md)

Then complete the power and selection labs. Compare simulated rates and conditional summaries with their exact benchmarks. Record the data-generating process, seed, repetitions, denominator and Monte Carlo standard error for each reported result. Explain what using an independent holdout changes. Compare the tables and critiques you drafted with the worked lab solutions. [Lab 1, Power](simulations/labs/01-power.md) · [Power solution](simulations/solutions/01-power.md) · [Lab 2, Selection](simulations/labs/02-selection.md) · [Selection solution](simulations/solutions/02-selection.md)

**Check before moving on.** Point to the true effect that a power calculation assumes. Identify which studies enter a conditional sign or magnitude calculation. Explain why increasing the study sample size changes a different quantity from increasing simulation replications.

## Module 4: Finance, identification and analysis choices

A portfolio has a positive estimated gross alpha. What would you need before making a claim about returns after implementation costs? Use the chapter’s gross-to-net example and ask what changes when you compare analysts using the same data. [Chapter §4, Comparing analyses of the same data](synthesis/critical-synthesis.md#comparing-analyses-of-the-same-data)

Trace one contrast in the finance replication notes to the papers and check whether the studies share the same targets, samples and procedures. Use the Menkveld et al. note to ask what variation over analysis choices can establish, and what further assumptions would connect it to bias. [Finance](wiki/concepts/finance.md) · [Identification](wiki/concepts/identification.md) · [Uncertainty beyond sampling](wiki/concepts/uncertainty-beyond-sampling.md) · [Claim C008](wiki/claims/C008-finance-replication.md) · [Menkveld et al.](wiki/papers/menkveld-etal-2024-nonstandard-errors.md)

**Your work.** Complete Exercise 5. Keep a gross/net results table with an explicit sensitivity analysis and an interpretation that names the target at each step. In finance, explain the role of risk adjustment, costs, implementation constraints and investor utility. If you adapt the reasoning to policy, distinguish the observed association, the causal effect, the target population and welfare. Retain one evidence-based comparison between papers and record the source-reading limits. [Exercise 5 and worked solution](exercises/05-finance-identification.md)

**Check before moving on.** Identify an assumption that a narrow standard error leaves untested. Explain what a reproducible calculation establishes and what would need independent empirical replication or evidence from a different setting.

## Module 5: Decisions under uncertainty and the capstone

A committee must choose whether to adopt a programme with an uncertain benefit. Read the chapter’s decision example with costs of £100 and £500. Predict whether the recommendation will change, holding the study and the prior fixed. [Chapter §5, Action under uncertainty](synthesis/critical-synthesis.md#5-what-can-justify-an-action-under-uncertainty)

Use the decision concept to distinguish choosing after you see the data from evaluating a rule before the data arrive. The Manski note gives a trail on treatment choice, and the robust Bayes note gives a further challenge within its recorded selected-section scope. [Decisions under uncertainty](wiki/concepts/decisions.md) · [Claim C002](wiki/claims/C002-action-without-rejection.md) · [Manski on treatment choice](wiki/papers/manski-2019-treatment-choice.md) · [Robust Bayes note](wiki/papers/aradillas-fernandez-etal-2026-robust-bayes.md)

**Your work.** Complete Exercise 6. Start your memo with a recommendation conditional on the feasible actions, uncertainty, consequences and decision criterion. Report what the study establishes separately. Show how changing a prior, cost or loss changes the calculation. If you discuss minimax regret or a different uncertainty set, state what it would evaluate and which additional assumptions it needs. [Exercise 6 and worked solution](exercises/06-decision-memo.md)

Use your Exercise 6 memo as the capstone. In Lab 3, prepare the separate comparison of decision rules under matched and mismatched priors and fixed states. Report paired utility differences with Monte Carlo standard errors. Bring one finding from that comparison back into a short appendix to the capstone memo. Explain which part of the chapter’s argument you would retain, narrow or revise. [Lab 3, Decisions](simulations/labs/03-decisions.md) · [Decision solution](simulations/solutions/03-decisions.md) · [Chapter §6, What would change the conclusion?](synthesis/critical-synthesis.md#6-what-would-change-the-conclusion)

**Check your memo.** Name the criterion that justifies the action and distinguish it from evidence of a worthwhile effect. Explain why a rule that works best on average under its prior can perform worse at particular states. Give the strongest objection to your choice and say what evidence or stakeholder judgement could change it.

## Optional case study: The 2008 debate

Choose one proposition and ask whether it concerns observed research practice, valid inference or a decision. Read the relevant part of the chapter, then use the matched exchange ledger to locate a strong argument and a concession on each side. Say what evidence or assumptions could resolve the particular disagreement. [Chapter §3, Competing arguments](synthesis/critical-synthesis.md#3-where-do-the-competing-arguments-disagree) · [2008 exchange ledger](wiki/disagreements/2008-exchange.md)

For a reading group, begin with one disputed American Economic Review paper. If you do the full Exercise 4, build the two-case ledger for Darby and Bernheim–Wantz. In each case compare the passage, questionnaire item and scores available for that survey version. State your provisional judgement and what the evidence leaves open. Use the book and search ledgers to check the scope of the material consulted. [Chapter appendix, Auditing claims about research practice](synthesis/critical-synthesis.md#appendix-auditing-claims-about-research-practice) · [Exercise 4 and worked audit](exercises/04-aer-source-audit.md) · [Book reading ledger](wiki/evidence/cult-2008-reading.md) · [Expanded-data search](wiki/evidence/expanded-matrix-followup.md)

## Review your work

Ask a reader to trace one substantive statement to a source and one numerical statement to a calculation. Tell them which premise you think is most vulnerable. A defensible submission states its target, assumptions and limitations, gives the opposing view a fair reading and explains what evidence would change the conclusion. You can disagree with the chapter if you make that case. [Learning map](resources/learning-map.md) · [Research standards](AGENTS.md)

The slide gate is **closed** under the project’s review decision. [Review gate](reviews/review-gate.md)
