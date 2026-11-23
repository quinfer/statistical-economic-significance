# Reference simulation results

**Illustration — synthetic data throughout.**

Base seed: `20261123`. Replications per scenario: **50,000**.
Recorded runtime: CPython 3.13.2.

The exact inputs, derived stream seeds, code hashes, assumptions and unrounded results are in `reference.json`; `metrics.csv` provides a flat comparison table. Values below are rounded to six significant figures.

MCSE measures simulation noise. It is not the study's standard error or uncertainty about the real world. Rate intervals are Wilson 95% Monte Carlo intervals; an observed rate of zero or one is not certainty. Conditional metrics use their selected counts. A dash means undefined or unavailable, not zero. For means, estimate ± 1.96 MCSE is only a large-replication approximation.

Run the exercises before consulting the worked solutions. These tables do not resolve the AER coding dispute, the book's unread chapters, or the appropriateness of any economic margin, prior or loss function.

## Power

<details><summary>null_n100</summary>

Parameters:

```json
{
  "effect": 0.0,
  "sample_size": 100,
  "sigma": 1000.0,
  "true_se": 100.0,
  "reported_se": 100.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `18310929093491590552`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.04934 | 0.000968561 | 50000 | 0.05 | [0.047476, 0.0512732] |
| `coverage95` | 0.95066 | 0.000968561 | 50000 | 0.95 | [0.948727, 0.952524] |
| `equivalence` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `both_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `neither_reject` | 0.95066 | 0.000968561 | 50000 | 0.95 | [0.948727, 0.952524] |
| `positive_beyond_margin` | 0.0039 | 0.00027874 | 50000 | 0.00408631 | [0.00339049, 0.00448574] |
| `estimate_mean` | 0.101598 | 0.445077 | 50000 | 0 | — |

</details>

<details><summary>null_n2500</summary>

Parameters:

```json
{
  "effect": 0.0,
  "sample_size": 2500,
  "sigma": 1000.0,
  "true_se": 20.0,
  "reported_se": 20.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `10295260146044363801`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.04798 | 0.000955802 | 50000 | 0.05 | [0.0461411, 0.0498883] |
| `coverage95` | 0.95202 | 0.000955802 | 50000 | 0.95 | [0.950112, 0.953859] |
| `equivalence` | 0.99916 | 0.00012956 | 50000 | 0.999207 | [0.998865, 0.999378] |
| `both_reject` | 0.04714 | 0.000947817 | 50000 | 0.0492068 | [0.0453168, 0.0490327] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0 | 0 | 50000 | 1.51759e-11 | [0, 7.68233e-05] |
| `estimate_mean` | 0.00851019 | 0.0891713 | 50000 | 0 | — |

</details>

<details><summary>null_n100000</summary>

Parameters:

```json
{
  "effect": 0.0,
  "sample_size": 100000,
  "sigma": 1000.0,
  "true_se": 3.162277660168379,
  "reported_se": 3.162277660168379,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `1740356453592281531`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.04894 | 0.00096483 | 50000 | 0.05 | [0.0470834, 0.0508659] |
| `coverage95` | 0.95106 | 0.00096483 | 50000 | 0.95 | [0.949134, 0.952917] |
| `equivalence` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `both_reject` | 0.04894 | 0.00096483 | 50000 | 0.05 | [0.0470834, 0.0508659] |
| `neither_reject` | 0 | 0 | 50000 | 1.38778e-17 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0 | 0 | 50000 | 5.67541e-243 | [0, 7.68233e-05] |
| `estimate_mean` | -0.00171762 | 0.0140887 | 50000 | 0 | — |

</details>

<details><summary>small_n100</summary>

Parameters:

```json
{
  "effect": 20.0,
  "sample_size": 100,
  "sigma": 1000.0,
  "true_se": 100.0,
  "reported_se": 100.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `10537739707590186358`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.057 | 0.00103683 | 50000 | 0.0545947 | [0.0550017, 0.0590664] |
| `coverage95` | 0.94792 | 0.000993657 | 50000 | 0.95 | [0.945938, 0.949833] |
| `equivalence` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `both_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `neither_reject` | 0.943 | 0.00103683 | 50000 | 0.945405 | [0.940934, 0.944998] |
| `positive_beyond_margin` | 0.00764 | 0.0003894 | 50000 | 0.00724555 | [0.00691371, 0.00844194] |
| `estimate_mean` | 20.1903 | 0.450801 | 50000 | 20 | — |

</details>

<details><summary>small_n2500</summary>

Parameters:

```json
{
  "effect": 20.0,
  "sample_size": 2500,
  "sigma": 1000.0,
  "true_se": 20.0,
  "reported_se": 20.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `11176249367673014772`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.1672 | 0.0016688 | 50000 | 0.170075 | [0.163955, 0.170496] |
| `coverage95` | 0.95058 | 0.000969306 | 50000 | 0.95 | [0.948645, 0.952445] |
| `equivalence` | 0.9901 | 0.000442764 | 50000 | 0.990736 | [0.989194, 0.990931] |
| `both_reject` | 0.1573 | 0.00162823 | 50000 | 0.160811 | [0.154135, 0.160518] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0 | 0 | 50000 | 8.26609e-09 | [0, 7.68233e-05] |
| `estimate_mean` | 19.9664 | 0.0893123 | 50000 | 20 | — |

</details>

<details><summary>small_n100000</summary>

Parameters:

```json
{
  "effect": 20.0,
  "sample_size": 100000,
  "sigma": 1000.0,
  "true_se": 3.162277660168379,
  "reported_se": 3.162277660168379,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `6312370178412820072`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 1 | 0 | 50000 | 0.999994 | [0.999923, 1] |
| `coverage95` | 0.94996 | 0.000975049 | 50000 | 0.95 | [0.948014, 0.951837] |
| `equivalence` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `both_reject` | 1 | 0 | 50000 | 0.999994 | [0.999923, 1] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0 | 0 | 50000 | 3.43815e-160 | [0, 7.68233e-05] |
| `estimate_mean` | 19.9982 | 0.0141276 | 50000 | 20 | — |

</details>

<details><summary>meaningful_n100</summary>

Parameters:

```json
{
  "effect": 200.0,
  "sample_size": 100,
  "sigma": 1000.0,
  "true_se": 100.0,
  "reported_se": 100.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `14445770654948747928`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.51676 | 0.00223481 | 50000 | 0.516005 | [0.512379, 0.521139] |
| `coverage95` | 0.94976 | 0.000976892 | 50000 | 0.95 | [0.947811, 0.95164] |
| `equivalence` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `both_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `neither_reject` | 0.48324 | 0.00223481 | 50000 | 0.483995 | [0.478861, 0.487621] |
| `positive_beyond_margin` | 0.26008 | 0.00196183 | 50000 | 0.259511 | [0.256253, 0.263943] |
| `estimate_mean` | 200.485 | 0.447362 | 50000 | 200 | — |

</details>

<details><summary>meaningful_n2500</summary>

Parameters:

```json
{
  "effect": 200.0,
  "sample_size": 2500,
  "sigma": 1000.0,
  "true_se": 20.0,
  "reported_se": 20.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `10962046624240084091`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `coverage95` | 0.95202 | 0.000955802 | 50000 | 0.95 | [0.950112, 0.953859] |
| `equivalence` | 0 | 0 | 50000 | 1.51759e-11 | [0, 7.68233e-05] |
| `both_reject` | 0 | 0 | 50000 | 1.51755e-11 | [0, 7.68233e-05] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0.99974 | 7.21017e-05 | 50000 | 0.999603 | [0.999555, 0.999848] |
| `estimate_mean` | 199.891 | 0.0888506 | 50000 | 200 | — |

</details>

<details><summary>meaningful_n100000</summary>

Parameters:

```json
{
  "effect": 200.0,
  "sample_size": 100000,
  "sigma": 1000.0,
  "true_se": 3.162277660168379,
  "reported_se": 3.162277660168379,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `1178898323086654494`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `coverage95` | 0.95214 | 0.000954667 | 50000 | 0.95 | [0.950234, 0.953977] |
| `equivalence` | 0 | 0 | 50000 | 5.67541e-243 | [0, 7.68233e-05] |
| `both_reject` | 0 | 0 | 50000 | 5.67541e-243 | [0, 7.68233e-05] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `estimate_mean` | 199.996 | 0.0140626 | 50000 | 200 | — |

</details>

<details><summary>equivalence_boundary_n2500</summary>

Parameters:

```json
{
  "effect": 100.0,
  "sample_size": 2500,
  "sigma": 1000.0,
  "true_se": 20.0,
  "reported_se": 20.0,
  "reported_se_ratio": 1.0,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `3104418070361059133`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.99876 | 0.000157382 | 50000 | 0.998817 | [0.998411, 0.999033] |
| `coverage95` | 0.9492 | 0.000982032 | 50000 | 0.95 | [0.947241, 0.95109] |
| `equivalence` | 0.04976 | 0.00097246 | 50000 | 0.05 | [0.0478884, 0.0517008] |
| `both_reject` | 0.04852 | 0.000960893 | 50000 | 0.0488173 | [0.0466711, 0.0504382] |
| `neither_reject` | 0 | 0 | 50000 | 8.32667e-17 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0.05188 | 0.000991851 | 50000 | 0.05 | [0.0499702, 0.0538586] |
| `estimate_mean` | 99.9523 | 0.0899202 | 50000 | 100 | — |

</details>

<details><summary>understated_se_null_n2500</summary>

Parameters:

```json
{
  "effect": 0.0,
  "sample_size": 2500,
  "sigma": 1000.0,
  "true_se": 20.0,
  "reported_se": 10.0,
  "reported_se_ratio": 0.5,
  "margin": 100.0,
  "alpha": 0.05,
  "units": "pounds per person per year"
}
```

Derived seed: `15972176078751255382`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `zero_rejection` | 0.32868 | 0.00210071 | 50000 | 0.327095 | [0.324576, 0.33281] |
| `coverage95` | 0.67132 | 0.00210071 | 50000 | 0.672905 | [0.66719, 0.675424] |
| `equivalence` | 0.99994 | 3.464e-05 | 50000 | 0.999971 | [0.999824, 0.99998] |
| `both_reject` | 0.32862 | 0.00210061 | 50000 | 0.327066 | [0.324516, 0.33275] |
| `neither_reject` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `positive_beyond_margin` | 0 | 0 | 50000 | 2.89996e-09 | [0, 7.68233e-05] |
| `estimate_mean` | 0.0313255 | 0.0899245 | 50000 | 0 | — |

</details>

## Selection

<details><summary>single_null</summary>

Parameters:

```json
{
  "true_effect": 0.0,
  "known_se": 10.0,
  "alpha": 0.05,
  "replications": 50000,
  "units": "basis points per month"
}
```

Derived seed: `4826860285458675641`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `rejection_rate` | 0.04978 | 0.000972645 | 50000 | 0.05 | [0.047908, 0.0517212] |
| `unconditional_bias` | 0.0545276 | 0.0448674 | 50000 | 0 | — |
| `selected_bias` | 0.586721 | 0.473658 | 2489 | 0 | — |
| `selected_absolute_mean` | 23.3945 | 0.0671739 | 2489 | 23.378 | — |
| `selected_holdout_bias` | 0.0778106 | 0.203251 | 2489 | 0 | — |
| `selected_discovery_minus_holdout` | 0.50891 | 0.511489 | 2489 | 0 | — |
| `selected_type_s` | — | — | 0 | — | — |
| `selected_type_m` | — | — | 0 | — | — |

</details>

<details><summary>single_weak_positive</summary>

Parameters:

```json
{
  "true_effect": 1.0,
  "known_se": 10.0,
  "alpha": 0.05,
  "replications": 50000,
  "units": "basis points per month"
}
```

Derived seed: `4331273051370576521`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `rejection_rate` | 0.05194 | 0.000992393 | 50000 | 0.0511463 | [0.0500291, 0.0539197] |
| `unconditional_bias` | 0.0951245 | 0.0448736 | 50000 | 0 | — |
| `selected_bias` | 4.52641 | 0.450063 | 2597 | 4.48557 | — |
| `selected_absolute_mean` | 23.3389 | 0.0670631 | 2597 | 23.4079 | — |
| `selected_holdout_bias` | 0.270712 | 0.197831 | 2597 | 0 | — |
| `selected_discovery_minus_holdout` | 4.2557 | 0.488292 | 2597 | 4.48557 | — |
| `selected_type_s` | 0.38583 | 0.00955226 | 2597 | 0.385189 | [0.367289, 0.404707] |
| `selected_type_m` | 23.3389 | 0.0670631 | 2597 | 23.4079 | — |

</details>

<details><summary>single_strong_positive</summary>

Parameters:

```json
{
  "true_effect": 30.0,
  "known_se": 10.0,
  "alpha": 0.05,
  "replications": 50000,
  "units": "basis points per month"
}
```

Derived seed: `16083122633950818294`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `rejection_rate` | 0.84884 | 0.00160194 | 50000 | 0.850839 | [0.845673, 0.851953] |
| `unconditional_bias` | -0.0790993 | 0.0448394 | 50000 | 0 | — |
| `selected_bias` | 2.68918 | 0.038869 | 42442 | 2.73009 | — |
| `selected_absolute_mean` | 32.6892 | 0.038869 | 42442 | 32.7301 | — |
| `selected_holdout_bias` | -0.022462 | 0.0482487 | 42442 | 0 | — |
| `selected_discovery_minus_holdout` | 2.71164 | 0.0620908 | 42442 | 2.73009 | — |
| `selected_type_s` | 0 | 0 | 42442 | 4.14334e-07 | [0, 9.05026e-05] |
| `selected_type_m` | 1.08964 | 0.00129563 | 42442 | 1.091 | — |

</details>

<details><summary>single_weak_negative</summary>

Parameters:

```json
{
  "true_effect": -1.0,
  "known_se": 10.0,
  "alpha": 0.05,
  "replications": 50000,
  "units": "basis points per month"
}
```

Derived seed: `17713973333053309097`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `rejection_rate` | 0.05266 | 0.000998869 | 50000 | 0.0511463 | [0.0507364, 0.0546523] |
| `unconditional_bias` | 0.00806043 | 0.0446988 | 50000 | 0 | — |
| `selected_bias` | -4.20755 | 0.450769 | 2633 | -4.48557 | — |
| `selected_absolute_mean` | 23.4543 | 0.0670138 | 2633 | 23.4079 | — |
| `selected_holdout_bias` | -0.109412 | 0.197034 | 2633 | 0 | — |
| `selected_discovery_minus_holdout` | -4.09813 | 0.490575 | 2633 | -4.48557 | — |
| `selected_type_s` | 0.392328 | 0.00951555 | 2633 | 0.385189 | [0.373848, 0.411122] |
| `selected_type_m` | 23.4543 | 0.0670138 | 2633 | 23.4079 | — |

</details>

<details><summary>twenty_independent_null_candidates</summary>

Parameters:

```json
{
  "true_effect": 0.0,
  "known_se": 10.0,
  "alpha": 0.05,
  "candidates": 20,
  "replications": 50000,
  "units": "basis points per month",
  "search": "Select maximum absolute discovery z; publish if unadjusted p < alpha"
}
```

Derived seed: `6101546078680289361`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `family_rejection_rate` | 0.64118 | 0.00214508 | 50000 | 0.641514 | [0.636965, 0.645373] |
| `bonferroni_family_rejection_rate` | 0.04904 | 0.000965765 | 50000 | 0.0488301 | [0.0471815, 0.0509678] |
| `winner_signed_mean` | -0.0602203 | 0.0991365 | 50000 | 0 | — |
| `winner_absolute_mean` | 21.661 | 0.0210708 | 50000 | — | — |
| `selected_winner_signed_mean` | -0.0661488 | 0.137074 | 32059 | 0 | — |
| `selected_winner_absolute_mean` | 24.2604 | 0.020737 | 32059 | — | — |
| `selected_holdout_signed_mean` | -0.0292245 | 0.0560066 | 32059 | 0 | — |
| `selected_holdout_absolute_mean` | 7.99928 | 0.0337748 | 32059 | 7.97885 | — |
| `selected_discovery_minus_holdout_absolute` | 16.2611 | 0.0396583 | 32059 | — | — |

</details>

## Decisions

<details><summary>matched_prior_cost100</summary>

Parameters:

```json
{
  "evaluation": "matched_prior_predictive",
  "theta_mean": 0.0,
  "theta_sd": 1000.0,
  "se": 500.0,
  "cost": 100.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 125.0,
    "skeptical_bayes": 2600.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 922.4268134757361,
    "plugin": 100.0
  }
}
```

Derived seed: `2850615676944286264`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 345.112 | 2.43922 | 50000 | 350.935 | — |
| `bayes_adoption_without_zero_rejection` | 0.26192 | 0.00196631 | 50000 | 0.265117 | [0.258085, 0.265792] |
| `bayes_adoption` | 0.45064 | 0.00222515 | 50000 | 0.45549 | [0.446283, 0.455005] |
| `bayes_utility` | 303.403 | 2.54667 | 50000 | 309.053 | — |
| `bayes_regret` | 41.7087 | 0.606462 | 50000 | 41.8827 | — |
| `skeptical_bayes_adoption` | 0.01018 | 0.000448918 | 50000 | 0.0100223 | [0.009337, 0.0110983] |
| `skeptical_bayes_utility` | 22.8611 | 1.03454 | 50000 | 22.8826 | — |
| `skeptical_bayes_regret` | 322.251 | 2.27469 | 50000 | 328.053 | — |
| `skeptical_bayes_minus_bayes_utility` | -280.542 | 2.38156 | 50000 | -286.17 | — |
| `skeptical_bayes_minus_bayes_regret` | 280.542 | 2.38156 | 50000 | 286.17 | — |
| `positive_significance_adoption` | 0.18872 | 0.00174988 | 50000 | 0.190373 | [0.185314, 0.192174] |
| `positive_significance_utility` | 219.925 | 2.35638 | 50000 | 223.972 | — |
| `positive_significance_regret` | 125.187 | 1.22753 | 50000 | 126.963 | — |
| `positive_significance_minus_bayes_utility` | -83.4781 | 1.29127 | 50000 | -85.0808 | — |
| `positive_significance_minus_bayes_regret` | 83.4781 | 1.29127 | 50000 | 85.0808 | — |
| `cost_confidence_adoption` | 0.20378 | 0.00180141 | 50000 | 0.204673 | [0.200272, 0.207333] |
| `cost_confidence_utility` | 230.116 | 2.37881 | 50000 | 233.421 | — |
| `cost_confidence_regret` | 114.996 | 1.1665 | 50000 | 117.514 | — |
| `cost_confidence_minus_bayes_utility` | -73.2875 | 1.22531 | 50000 | -75.6312 | — |
| `cost_confidence_minus_bayes_regret` | 73.2875 | 1.22531 | 50000 | 75.6312 | — |
| `plugin_adoption` | 0.45954 | 0.00222874 | 50000 | 0.464365 | [0.455175, 0.463911] |
| `plugin_utility` | 303.104 | 2.55456 | 50000 | 308.964 | — |
| `plugin_regret` | 42.008 | 0.610429 | 50000 | 41.9715 | — |
| `plugin_minus_bayes_utility` | -0.29934 | 0.191325 | 50000 | -0.0887872 | — |
| `plugin_minus_bayes_regret` | 0.29934 | 0.191325 | 50000 | 0.0887872 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | -110.208 | 4.4537 | 50000 | -100 | — |
| `always_regret` | 455.32 | 2.75682 | 50000 | 450.935 | — |
| `always_minus_bayes_utility` | -413.612 | 2.8862 | 50000 | -409.053 | — |
| `always_minus_bayes_regret` | 413.612 | 2.8862 | 50000 | 409.053 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 345.112 | 2.43922 | 50000 | 350.935 | — |
| `never_minus_bayes_utility` | -303.403 | 2.54667 | 50000 | -309.053 | — |
| `never_minus_bayes_regret` | 303.403 | 2.54667 | 50000 | 309.053 | — |

</details>

<details><summary>matched_prior_cost500</summary>

Parameters:

```json
{
  "evaluation": "matched_prior_predictive",
  "theta_mean": 0.0,
  "theta_sd": 1000.0,
  "se": 500.0,
  "cost": 500.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 625.0,
    "skeptical_bayes": 13000.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 1322.4268134757363,
    "plugin": 500.0
  }
}
```

Derived seed: `7894018033220693020`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 196.995 | 1.84454 | 50000 | 197.797 | — |
| `bayes_adoption_without_zero_rejection` | 0.09706 | 0.00132393 | 50000 | 0.097702 | [0.094496, 0.0996859] |
| `bayes_adoption` | 0.28626 | 0.00202146 | 50000 | 0.288075 | [0.282315, 0.290238] |
| `bayes_utility` | 159.897 | 1.90117 | 50000 | 161.171 | — |
| `bayes_regret` | 37.0989 | 0.574394 | 50000 | 36.6256 | — |
| `skeptical_bayes_adoption` | 0 | 0 | 50000 | 1.49266e-31 | [0, 7.68233e-05] |
| `skeptical_bayes_utility` | 0 | 0 | 50000 | 1.48905e-27 | — |
| `skeptical_bayes_regret` | 196.995 | 1.84454 | 50000 | 197.797 | — |
| `skeptical_bayes_minus_bayes_utility` | -159.897 | 1.90117 | 50000 | -161.171 | — |
| `skeptical_bayes_minus_bayes_regret` | 159.897 | 1.90117 | 50000 | 161.171 | — |
| `positive_significance_adoption` | 0.1892 | 0.00175159 | 50000 | 0.190373 | [0.185791, 0.192657] |
| `positive_significance_utility` | 147.15 | 1.80438 | 50000 | 147.823 | — |
| `positive_significance_regret` | 49.8457 | 0.710166 | 50000 | 49.9739 | — |
| `positive_significance_minus_bayes_utility` | -12.7467 | 0.658555 | 50000 | -13.3483 | — |
| `positive_significance_minus_bayes_regret` | 12.7467 | 0.658555 | 50000 | 13.3483 | — |
| `cost_confidence_adoption` | 0.11782 | 0.00144179 | 50000 | 0.118441 | [0.115023, 0.120675] |
| `cost_confidence_utility` | 117.156 | 1.69099 | 50000 | 118.057 | — |
| `cost_confidence_regret` | 79.8394 | 0.962932 | 50000 | 79.7391 | — |
| `cost_confidence_minus_bayes_utility` | -42.7405 | 0.977391 | 50000 | -43.1134 | — |
| `cost_confidence_minus_bayes_regret` | 42.7405 | 0.977391 | 50000 | 43.1134 | — |
| `plugin_adoption` | 0.32636 | 0.0020969 | 50000 | 0.32736 | [0.322264, 0.330483] |
| `plugin_utility` | 157.296 | 1.95024 | 50000 | 159.188 | — |
| `plugin_regret` | 39.6999 | 0.602898 | 50000 | 38.6083 | — |
| `plugin_minus_bayes_utility` | -2.60096 | 0.415159 | 50000 | -1.98267 | — |
| `plugin_minus_bayes_regret` | 2.60096 | 0.415159 | 50000 | 1.98267 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | -504.445 | 4.4843 | 50000 | -500 | — |
| `always_regret` | 701.441 | 3.34355 | 50000 | 697.797 | — |
| `always_minus_bayes_utility` | -664.342 | 3.49934 | 50000 | -661.171 | — |
| `always_minus_bayes_regret` | 664.342 | 3.49934 | 50000 | 661.171 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 196.995 | 1.84454 | 50000 | 197.797 | — |
| `never_minus_bayes_utility` | -159.897 | 1.90117 | 50000 | -161.171 | — |
| `never_minus_bayes_regret` | 159.897 | 1.90117 | 50000 | 161.171 | — |

</details>

<details><summary>mismatched_prior_negative</summary>

Parameters:

```json
{
  "evaluation": "mismatched_prior_predictive",
  "theta_mean": -250.0,
  "theta_sd": 100.0,
  "se": 500.0,
  "cost": 100.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 125.0,
    "skeptical_bayes": 2600.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 922.4268134757361,
    "plugin": 100.0
  }
}
```

Derived seed: `16531211227284977757`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 0.00397267 | 0.00176071 | 50000 | 0.00584809 | — |
| `bayes_adoption_without_zero_rejection` | 0.22232 | 0.00185954 | 50000 | 0.223109 | [0.218697, 0.225986] |
| `bayes_adoption` | 0.23034 | 0.00188299 | 50000 | 0.231037 | [0.22667, 0.234051] |
| `bayes_utility` | -74.7047 | 0.646666 | 50000 | -74.893 | — |
| `bayes_regret` | 74.7087 | 0.646655 | 50000 | 74.8988 | — |
| `skeptical_bayes_adoption` | 0 | 0 | 50000 | 1.13987e-08 | [0, 7.68233e-05] |
| `skeptical_bayes_utility` | 0 | 0 | 50000 | -2.7023e-06 | — |
| `skeptical_bayes_regret` | 0.00397267 | 0.00176071 | 50000 | 0.00585079 | — |
| `skeptical_bayes_minus_bayes_utility` | 74.7047 | 0.646666 | 50000 | 74.893 | — |
| `skeptical_bayes_minus_bayes_regret` | -74.7047 | 0.646666 | 50000 | -74.893 | — |
| `positive_significance_adoption` | 0.00802 | 0.00039889 | 50000 | 0.00792844 | [0.0072751, 0.00884049] |
| `positive_significance_utility` | -2.34092 | 0.123009 | 50000 | -2.34846 | — |
| `positive_significance_regret` | 2.3449 | 0.12302 | 50000 | 2.35431 | — |
| `positive_significance_minus_bayes_utility` | 72.3638 | 0.640173 | 50000 | 72.5445 | — |
| `positive_significance_minus_bayes_regret` | -72.3638 | 0.640173 | 50000 | -72.5445 | — |
| `cost_confidence_adoption` | 0.0112 | 0.000470629 | 50000 | 0.0107434 | [0.0103144, 0.0121607] |
| `cost_confidence_utility` | -3.3218 | 0.147026 | 50000 | -3.20379 | — |
| `cost_confidence_regret` | 3.32577 | 0.147035 | 50000 | 3.20964 | — |
| `cost_confidence_minus_bayes_utility` | 71.3829 | 0.637217 | 50000 | 71.6892 | — |
| `cost_confidence_minus_bayes_regret` | -71.3829 | 0.637217 | 50000 | -71.6892 | — |
| `plugin_adoption` | 0.24598 | 0.001926 | 50000 | 0.246228 | [0.242225, 0.249774] |
| `plugin_utility` | -79.9141 | 0.663217 | 50000 | -79.9982 | — |
| `plugin_regret` | 79.9181 | 0.663206 | 50000 | 80.004 | — |
| `plugin_minus_bayes_utility` | -5.20938 | 0.192995 | 50000 | -5.10518 | — |
| `plugin_minus_bayes_regret` | 5.20938 | 0.192995 | 50000 | 5.10518 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | -350.425 | 0.447957 | 50000 | -350 | — |
| `always_regret` | 350.429 | 0.447892 | 50000 | 350.006 | — |
| `always_minus_bayes_utility` | -275.72 | 0.778723 | 50000 | -275.107 | — |
| `always_minus_bayes_regret` | 275.72 | 0.778723 | 50000 | 275.107 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 0.00397267 | 0.00176071 | 50000 | 0.00584809 | — |
| `never_minus_bayes_utility` | 74.7047 | 0.646666 | 50000 | 74.893 | — |
| `never_minus_bayes_regret` | -74.7047 | 0.646666 | 50000 | -74.893 | — |

</details>

<details><summary>fixed_zero</summary>

Parameters:

```json
{
  "evaluation": "fixed_state",
  "theta_mean": 0.0,
  "theta_sd": 0.0,
  "se": 500.0,
  "cost": 100.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 125.0,
    "skeptical_bayes": 2600.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 922.4268134757361,
    "plugin": 100.0
  }
}
```

Derived seed: `7204598680875119766`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 0 | 0 | 50000 | 0 | — |
| `bayes_adoption_without_zero_rejection` | 0.37508 | 0.00216516 | 50000 | 0.376294 | [0.370846, 0.379333] |
| `bayes_adoption` | 0.40058 | 0.00219142 | 50000 | 0.401294 | [0.396293, 0.404883] |
| `bayes_utility` | -40.058 | 0.219144 | 50000 | -40.1294 | — |
| `bayes_regret` | 40.058 | 0.219144 | 50000 | 40.1294 | — |
| `skeptical_bayes_adoption` | 0 | 0 | 50000 | 9.96443e-08 | [0, 7.68233e-05] |
| `skeptical_bayes_utility` | 0 | 0 | 50000 | -9.96443e-06 | — |
| `skeptical_bayes_regret` | 0 | 0 | 50000 | 9.96443e-06 | — |
| `skeptical_bayes_minus_bayes_utility` | 40.058 | 0.219144 | 50000 | 40.1294 | — |
| `skeptical_bayes_minus_bayes_regret` | -40.058 | 0.219144 | 50000 | -40.1294 | — |
| `positive_significance_adoption` | 0.0255 | 0.000704979 | 50000 | 0.025 | [0.0241543, 0.0269186] |
| `positive_significance_utility` | -2.55 | 0.0704986 | 50000 | -2.5 | — |
| `positive_significance_regret` | 2.55 | 0.0704986 | 50000 | 2.5 | — |
| `positive_significance_minus_bayes_utility` | 37.508 | 0.216518 | 50000 | 37.6294 | — |
| `positive_significance_minus_bayes_regret` | -37.508 | 0.216518 | 50000 | -37.6294 | — |
| `cost_confidence_adoption` | 0.0327 | 0.00079537 | 50000 | 0.0325294 | [0.0311766, 0.0342952] |
| `cost_confidence_utility` | -3.27 | 0.0795378 | 50000 | -3.25294 | — |
| `cost_confidence_regret` | 3.27 | 0.0795378 | 50000 | 3.25294 | — |
| `cost_confidence_minus_bayes_utility` | 36.788 | 0.215661 | 50000 | 36.8764 | — |
| `cost_confidence_minus_bayes_regret` | -36.788 | 0.215661 | 50000 | -36.8764 | — |
| `plugin_adoption` | 0.41974 | 0.00220707 | 50000 | 0.42074 | [0.415421, 0.424072] |
| `plugin_utility` | -41.974 | 0.220709 | 50000 | -42.074 | — |
| `plugin_regret` | 41.974 | 0.220709 | 50000 | 42.074 | — |
| `plugin_minus_bayes_utility` | -1.916 | 0.0613079 | 50000 | -1.94466 | — |
| `plugin_minus_bayes_regret` | 1.916 | 0.0613079 | 50000 | 1.94466 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | -100 | 0 | 50000 | -100 | — |
| `always_regret` | 100 | 0 | 50000 | 100 | — |
| `always_minus_bayes_utility` | -59.942 | 0.219144 | 50000 | -59.8706 | — |
| `always_minus_bayes_regret` | 59.942 | 0.219144 | 50000 | 59.8706 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 0 | 0 | 50000 | 0 | — |
| `never_minus_bayes_utility` | 40.058 | 0.219144 | 50000 | 40.1294 | — |
| `never_minus_bayes_regret` | -40.058 | 0.219144 | 50000 | -40.1294 | — |

</details>

<details><summary>fixed_moderate_benefit</summary>

Parameters:

```json
{
  "evaluation": "fixed_state",
  "theta_mean": 400.0,
  "theta_sd": 0.0,
  "se": 500.0,
  "cost": 100.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 125.0,
    "skeptical_bayes": 2600.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 922.4268134757361,
    "plugin": 100.0
  }
}
```

Derived seed: `1034123117975583213`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 300 | 0 | 50000 | 300 | — |
| `bayes_adoption_without_zero_rejection` | 0.58442 | 0.00220397 | 50000 | 0.585809 | [0.580094, 0.588733] |
| `bayes_adoption` | 0.7074 | 0.00203463 | 50000 | 0.70884 | [0.703396, 0.711372] |
| `bayes_utility` | 212.22 | 0.610394 | 50000 | 212.652 | — |
| `bayes_regret` | 87.78 | 0.610394 | 50000 | 87.3479 | — |
| `skeptical_bayes_adoption` | 0 | 0 | 50000 | 5.41254e-06 | [0, 7.68233e-05] |
| `skeptical_bayes_utility` | 0 | 0 | 50000 | 0.00162376 | — |
| `skeptical_bayes_regret` | 300 | 0 | 50000 | 299.998 | — |
| `skeptical_bayes_minus_bayes_utility` | -212.22 | 0.610394 | 50000 | -212.65 | — |
| `skeptical_bayes_minus_bayes_regret` | 212.22 | 0.610394 | 50000 | 212.65 | — |
| `positive_significance_adoption` | 0.12298 | 0.00146871 | 50000 | 0.123032 | [0.12013, 0.125888] |
| `positive_significance_utility` | 36.894 | 0.440618 | 50000 | 36.9095 | — |
| `positive_significance_regret` | 263.106 | 0.440618 | 50000 | 263.09 | — |
| `positive_significance_minus_bayes_utility` | -175.326 | 0.661196 | 50000 | -175.743 | — |
| `positive_significance_minus_bayes_regret` | 175.326 | 0.661196 | 50000 | 175.743 | — |
| `cost_confidence_adoption` | 0.14884 | 0.00159177 | 50000 | 0.148045 | [0.145747, 0.151987] |
| `cost_confidence_utility` | 44.652 | 0.477536 | 50000 | 44.4136 | — |
| `cost_confidence_regret` | 255.348 | 0.477536 | 50000 | 255.586 | — |
| `cost_confidence_minus_bayes_utility` | -167.568 | 0.66621 | 50000 | -168.239 | — |
| `cost_confidence_minus_bayes_regret` | 167.568 | 0.66621 | 50000 | 168.239 | — |
| `plugin_adoption` | 0.7254 | 0.00199597 | 50000 | 0.725747 | [0.721471, 0.729295] |
| `plugin_utility` | 217.62 | 0.598797 | 50000 | 217.724 | — |
| `plugin_regret` | 82.38 | 0.598797 | 50000 | 82.2759 | — |
| `plugin_minus_bayes_utility` | 5.4 | 0.178374 | 50000 | 5.07197 | — |
| `plugin_minus_bayes_regret` | -5.4 | 0.178374 | 50000 | -5.07197 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | 300 | 0 | 50000 | 300 | — |
| `always_regret` | 0 | 0 | 50000 | 0 | — |
| `always_minus_bayes_utility` | 87.78 | 0.610394 | 50000 | 87.3479 | — |
| `always_minus_bayes_regret` | -87.78 | 0.610394 | 50000 | -87.3479 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 300 | 0 | 50000 | 300 | — |
| `never_minus_bayes_utility` | -212.22 | 0.610394 | 50000 | -212.652 | — |
| `never_minus_bayes_regret` | 212.22 | 0.610394 | 50000 | 212.652 | — |

</details>

<details><summary>fixed_large_benefit</summary>

Parameters:

```json
{
  "evaluation": "fixed_state",
  "theta_mean": 1200.0,
  "theta_sd": 0.0,
  "se": 500.0,
  "cost": 100.0,
  "alpha": 0.05,
  "policy_prior_mean": 0.0,
  "policy_prior_sd": 1000.0,
  "skeptical_prior_sd": 100.0,
  "policy_cutoffs": {
    "bayes": 125.0,
    "skeptical_bayes": 2600.0,
    "positive_significance": 979.9819922700269,
    "cost_confidence": 922.4268134757361,
    "plugin": 100.0
  }
}
```

Derived seed: `16129769607638190032`.

| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |
|---|---:|---:|---:|---:|---|
| `oracle_utility` | 1100 | 0 | 50000 | 1100 | — |
| `bayes_adoption_without_zero_rejection` | 0.31252 | 0.00207293 | 50000 | 0.314178 | [0.308472, 0.316597] |
| `bayes_adoption` | 0.98384 | 0.000563895 | 50000 | 0.984222 | [0.982697, 0.984909] |
| `bayes_utility` | 1082.22 | 0.62029 | 50000 | 1082.64 | — |
| `bayes_regret` | 17.776 | 0.62029 | 50000 | 17.3554 | — |
| `skeptical_bayes_adoption` | 0.00284 | 0.000237989 | 50000 | 0.00255513 | [0.0024102, 0.00334619] |
| `skeptical_bayes_utility` | 3.124 | 0.26179 | 50000 | 2.81064 | — |
| `skeptical_bayes_regret` | 1096.88 | 0.26179 | 50000 | 1097.19 | — |
| `skeptical_bayes_minus_bayes_utility` | -1079.1 | 0.67162 | 50000 | -1079.83 | — |
| `skeptical_bayes_minus_bayes_regret` | 1079.1 | 0.67162 | 50000 | 1079.83 | — |
| `positive_significance_adoption` | 0.67132 | 0.00210071 | 50000 | 0.670044 | [0.66719, 0.675424] |
| `positive_significance_utility` | 738.452 | 2.31081 | 50000 | 737.049 | — |
| `positive_significance_regret` | 361.548 | 2.31081 | 50000 | 362.951 | — |
| `positive_significance_minus_bayes_utility` | -343.772 | 2.28024 | 50000 | -345.596 | — |
| `positive_significance_minus_bayes_regret` | 343.772 | 2.28024 | 50000 | 345.596 | — |
| `cost_confidence_adoption` | 0.71172 | 0.00202571 | 50000 | 0.710603 | [0.707734, 0.715674] |
| `cost_confidence_utility` | 782.892 | 2.2283 | 50000 | 781.663 | — |
| `cost_confidence_regret` | 317.108 | 2.2283 | 50000 | 318.337 | — |
| `cost_confidence_minus_bayes_utility` | -299.332 | 2.18939 | 50000 | -300.982 | — |
| `cost_confidence_minus_bayes_regret` | 299.332 | 2.18939 | 50000 | 300.982 | — |
| `plugin_adoption` | 0.98576 | 0.000529853 | 50000 | 0.986097 | [0.984684, 0.986762] |
| `plugin_utility` | 1084.34 | 0.582844 | 50000 | 1084.71 | — |
| `plugin_regret` | 15.664 | 0.582844 | 50000 | 15.2938 | — |
| `plugin_minus_bayes_utility` | 2.112 | 0.21535 | 50000 | 2.06158 | — |
| `plugin_minus_bayes_regret` | -2.112 | 0.21535 | 50000 | -2.06158 | — |
| `always_adoption` | 1 | 0 | 50000 | 1 | [0.999923, 1] |
| `always_utility` | 1100 | 0 | 50000 | 1100 | — |
| `always_regret` | 0 | 0 | 50000 | 0 | — |
| `always_minus_bayes_utility` | 17.776 | 0.62029 | 50000 | 17.3554 | — |
| `always_minus_bayes_regret` | -17.776 | 0.62029 | 50000 | -17.3554 | — |
| `never_adoption` | 0 | 0 | 50000 | 0 | [0, 7.68233e-05] |
| `never_utility` | 0 | 0 | 50000 | 0 | — |
| `never_regret` | 1100 | 0 | 50000 | 1100 | — |
| `never_minus_bayes_utility` | -1082.22 | 0.62029 | 50000 | -1082.64 | — |
| `never_minus_bayes_regret` | 1082.22 | 0.62029 | 50000 | 1082.64 | — |

</details>

