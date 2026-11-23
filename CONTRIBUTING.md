# Contributing

Start with the [status](STATUS.md), [wiki index](wiki/index.md) and [research standards](AGENTS.md). Use British English. Corrections, rival arguments and exercises that reveal assumptions are welcome.

## Source corrections

Give the affected claim, a retrieved publisher/author/repository URL, exact version, locatable passage and proposed correction. Separate the author's claim from your interpretation. Report inaccessible material honestly. A verified DOI does not substantiate a detailed claim.

`sources/registry.json` is the bibliographic source of truth. Supporting applications and version comparisons belong in `sources/aer-audit/supporting-registry.json`, not the 25–35-work core. Keep reading depths accurate. After a registry edit, reconcile the note before updating its fingerprint and rebuilding the catalogue. Never refresh a fingerprint simply to silence an error. Preserve earlier failed-access records when access improves.

## Exercises and calculations

State the objective, estimand, units, population, horizon, uncertainty model, identification assumptions and economic criterion. Label synthetic inputs. Decisions require alternatives, costs, losses or utility, and any prior. Include a case that challenges the apparent lesson.

Random simulations need a data-generating process, seed, replication count and Monte Carlo error. Test against analytic benchmarks or independent implementations. Keep copyrighted full texts, credentials and personal machine paths out of Git.

## Checks and review

```sh
python3 scripts/build_catalogue.py
python3 scripts/check_all.py
git diff --check
git diff
```

Inspect generated-file changes. A focused pull request should explain the problem, evidence, change, checks and unresolved objections. Automated checks and AI reviews are not human scholarly approval.

**No slides may be generated while the [gate](reviews/review-gate.md) remains closed.** Learning exercises do not override the user's hold.

Contribute only material you can share under the applicable [writing](LICENSE) or [software](LICENSE-CODE) licence. Cited works retain their own rights. Prefer original summaries and links; quote briefly with checked locators. Record material AI assistance and review roles in [provenance](PROVENANCE.md).
