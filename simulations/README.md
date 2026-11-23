# Simulation design backlog

No Monte Carlo simulations have been implemented. The [learning examples](../implementations/README.md) use deterministic analytical calculations with synthetic inputs. No numerical output here is an empirical finding. Implement random simulations after their arguments and teaching scope have been reviewed.

Planned experiments will vary effect magnitude, precision, selection and decision costs independently. Every exercise must state a synthetic data-generating process, units, estimand, estimator, uncertainty method, random seed, number of replications and Monte Carlo error. Store source code and outputs separately; never label an illustrative calibration as an estimated economic fact.

The [training brief](../training/README.md) describes intended exercises. Numerical checks must include analytic benchmarks where available, behaviour under a true null and a non-negligible effect, and sensitivity to violated assumptions. Review clustering, serial dependence and multiple testing before applying iid examples to economics or finance.

## Research checks already available

The [argument-check script](../scripts/check_arguments.py) evaluates closed-form synthetic normal examples for the working synthesis. The [learning implementation](../implementations/README.md) now makes those distinctions explorable through six exercise sheets. Both use no random draws, so seed and Monte Carlo error do not apply. Monte Carlo simulation and slide development remain deferred.
