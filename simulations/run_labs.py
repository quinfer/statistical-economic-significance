#!/usr/bin/env python3
"""Run synthetic simulation labs and write auditable JSON, CSV and Markdown."""
import argparse
import csv
import hashlib
import importlib
import io
import json
from pathlib import Path
import platform
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from simulations.common import validate_run
from scripts.numeric_snapshot import assert_equivalent

LABS = ("power", "selection", "decisions")
CODE_FILES = ["simulations/common.py", "simulations/run_labs.py",
              "implementations/normal_model.py"] + [f"simulations/{lab}.py" for lab in LABS]


def build_results(labs, replications, seed):
    validate_run(replications, seed)
    if not labs or any(lab not in LABS for lab in labs) or len(set(labs)) != len(labs):
        raise ValueError("choose distinct known labs")
    return {
        "schema_version": 1,
        "label": "ILLUSTRATIONS: simulated normal-model data, not empirical findings or literature replications",
        "seed": seed,
        "replications_per_scenario": replications,
        "random_streams": "random.Random with SHA256-derived integer seeds by scenario label; explicit normal draws",
        "environment": {"python": platform.python_version(), "implementation": platform.python_implementation()},
        "source_sha256": {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in CODE_FILES},
        "monte_carlo": {
            "mean_mcse": "Sample SD of independent replication-level values divided by sqrt(n)",
            "rate_mcse": "sqrt(p_hat*(1-p_hat)/n); Wilson 95% intervals also reported, including boundaries",
            "conditional_metrics": "n is the selected count, not the total number simulated; no selected values means null, not zero",
            "paired_metrics": "Subtract policies or discovery/holdout estimates within a replication before computing MCSE",
            "scope": "These errors quantify simulation noise under the chosen DGP, not empirical, identification or model uncertainty",
        },
        "labs": [importlib.import_module(f"simulations.{lab}").run(replications, seed) for lab in labs],
    }


def number(value):
    return "—" if value is None else f"{value:.6g}"


def summary_text(result):
    text = ["# Reference simulation results", "", "**Illustration — synthetic data throughout.**", "",
            f"Base seed: `{result['seed']}`. Replications per scenario: **{result['replications_per_scenario']:,}**.",
            f"Recorded runtime: {result['environment']['implementation']} {result['environment']['python']}.", "",
            "The exact inputs, derived stream seeds, code hashes, assumptions and unrounded results are in `reference.json`; `metrics.csv` provides a flat comparison table. Values below are rounded to six significant figures.", "",
            "MCSE measures simulation noise. It is not the study's standard error or uncertainty about the real world. Rate intervals are Wilson 95% Monte Carlo intervals; an observed rate of zero or one is not certainty. Conditional metrics use their selected counts. A dash means undefined or unavailable, not zero. For means, estimate ± 1.96 MCSE is only a large-replication approximation.", "",
            "Run the exercises before consulting the worked solutions. These tables do not resolve the AER coding dispute, the book's unread chapters, or the appropriateness of any economic margin, prior or loss function.", ""]
    for lab in result['labs']:
        text += [f"## {lab['lab'].capitalize()}", ""]
        for scenario in lab['scenarios']:
            text += [f"<details><summary>{scenario['id']}</summary>", "",
                     "Parameters:", "", "```json", json.dumps(scenario['parameters'], indent=2, allow_nan=False),
                     "```", "", f"Derived seed: `{scenario['derived_seed']}`.", "",
                     "| Metric | Estimate | MCSE | n | Analytic benchmark | Wilson 95% MC interval |",
                     "|---|---:|---:|---:|---:|---|"]
            for key, metric in scenario['metrics'].items():
                bounds = metric.get('wilson95')
                ci = f"[{number(bounds[0])}, {number(bounds[1])}]" if bounds else "—"
                text += [f"| `{key}` | {number(metric['estimate'])} | {number(metric['mcse'])} | {metric['n']} | {number(scenario['benchmarks'].get(key))} | {ci} |"]
            text += ["", "</details>", ""]
    return "\n".join(text) + "\n"


def csv_text(result):
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["lab", "scenario", "metric", "estimate", "mcse", "n", "successes",
                     "wilson95_low", "wilson95_high", "analytic_benchmark", "derived_seed"])
    for lab in result['labs']:
        for scenario in lab['scenarios']:
            for key, metric in scenario['metrics'].items():
                lo, hi = metric.get('wilson95') or (None, None)
                writer.writerow([lab['lab'], scenario['id'], key, metric['estimate'], metric['mcse'],
                                 metric['n'], metric.get('successes'), lo, hi,
                                 scenario['benchmarks'].get(key), scenario['derived_seed']])
    return stream.getvalue()


def write_results(result, directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    (directory / 'reference.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    (directory / 'metrics.csv').write_text(csv_text(result), encoding='utf-8')
    (directory / 'summary.md').write_text(summary_text(result), encoding='utf-8')


def check_reference(path):
    recorded = json.loads(path.read_text())
    regenerated = build_results([x['lab'] for x in recorded['labs']],
                                recorded['replications_per_scenario'], recorded['seed'])
    # Runtime versions may differ; numerical checks still run, and code hashes must match.
    regenerated['environment'] = recorded['environment']
    assert_equivalent(regenerated, recorded, rel_tol=1e-10, abs_tol=1e-12)
    # Check views against the stored numerical record, without platform round-trip drift.
    if (path.parent/'summary.md').read_text() != summary_text(recorded):
        raise AssertionError('summary.md is stale relative to the reference JSON')
    if (path.parent/'metrics.csv').read_text() != csv_text(recorded):
        raise AssertionError('metrics.csv is stale relative to the reference JSON')
    print('PASS: seeded reference reproduction, code hashes and generated views; no files changed.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lab', choices=('all',) + LABS, default='all')
    parser.add_argument('--replications', type=int, default=50000)
    parser.add_argument('--seed', type=int, default=20261123)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'scratch/simulation-labs')
    parser.add_argument('--check-reference', action='store_true',
                        help='Reproduce the committed reference configuration without changing files; other run options are ignored')
    args = parser.parse_args()
    if args.check_reference:
        check_reference(ROOT/'simulations/results/reference.json')
        return
    try:
        result = build_results(LABS if args.lab == 'all' else (args.lab,), args.replications, args.seed)
    except ValueError as error:
        parser.error(str(error))
    write_results(result, args.output_dir)
    print(f"Wrote {len(result['labs'])} synthetic labs to {args.output_dir}")
    print('reference.json, metrics.csv, summary.md; Monte Carlo error is reported, not empirical evidence.')


if __name__ == '__main__':
    main()
