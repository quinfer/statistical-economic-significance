# Reproducible worked examples

These are **synthetic illustrations**, using an unbiased normal estimate with known standard error. They explain distinctions; they are not findings about a policy, a market or the AER survey. Python 3.10 or later is sufficient; no packages need installing.

From the repository root:

```sh
python3 implementations/worked_examples.py
python3 -m unittest discover -s tests -v
```

The first command prints labelled JSON to the terminal without changing files. It covers magnitude versus precision, confidence intervals, equivalence, analytical power, a monthly alpha net of known costs, and a decision under a proper normal prior. It uses no random draws, so no seed or Monte Carlo error applies.

| Calculation | Assumptions and limits |
|---|---|
| Zero-null p-value and interval | Known-SE normal sampling model; conditional on identification and the specified analysis |
| TOST equivalence | Positive, symmetric margin fixed before seeing the estimate; two one-sided tests at the same alpha |
| Power | A specified true effect and known SE; this is a design calculation, not the probability that a hypothesis is true |
| Finance | Monthly basis points; fixed factor interpretation and known implementation cost; no multiple search or serial dependence correction |
| Posterior decision | Proper normal prior, pounds per person, known cost, risk-neutral linear utility and status quo normalised to zero |

For `tost_p`, use `p < .05` to match strict containment of the 90% interval in the margins. Other conventions at exact equality make no probability difference in a continuous model, but should be reported consistently. Confidence coverage concerns repeated sampling under the model; posterior probabilities require the stated prior and likelihood.

[normal_model.py](normal_model.py) contains small, inspectable functions; [worked_examples.py](worked_examples.py) sets their units and assumptions. The [tests](../tests/test_normal_model.py) check known values, symmetry, equivariance to unit changes, interval/TOST agreement and invalid inputs. The older [synthesis calculations](../scripts/check_arguments.py) provide a separately implemented cross-check on the shared examples.

Start with the [exercises](../exercises/README.md). Future Monte Carlo work has a separate [design backlog](../simulations/README.md). The [slide gate](../reviews/review-gate.md) is closed.
