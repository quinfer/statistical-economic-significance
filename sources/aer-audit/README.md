# Supporting sources and reproducible AER audit

The core corpus remains **35 works**. This directory contains factual transcriptions, original audit code and separate supporting/version records; no full copyrighted articles, book pages or lecture file are committed.

Start with the [coding narrative](../../wiki/evidence/aer-coding-audit.md), [book reading](../../wiki/evidence/cult-2008-reading.md), [case audits](../../wiki/evidence/aer-darby-woodbury.md) and [supporting-source catalogue](supporting-materials.md). The second case ledger covers [monetary transmission, dividends and addiction](../../wiki/evidence/aer-macro-finance-addiction.md).

The latest pass directly checks [final Darby](../../wiki/evidence/darby-final-followup.md) and [final Bernheim–Wantz](../../wiki/evidence/bernheim-wantz-final-followup.md), supplied by the user, and a newly retrieved [final JSE scan](../../wiki/evidence/jse-2004-version-check.md). The [expanded-matrix search](../../wiki/evidence/expanded-matrix-followup.md) remains unsuccessful within its documented scope. See the [latest review](../../reviews/2026-10-24-final-source-review.md).

| File | Function |
|---|---|
| `final-paper-access-log.json` / `expanded-search-log.json` | Follow-up queries, response outcomes, checksums and later user-supplied final sources |
| `coding-manifest.json` / `coding-access-log.json` | Exact URLs, versions, coverage, checksums and access failures |
| `coding-questionnaire.csv` | Paraphrased item dictionary, locators and published percentages |
| `coding-1980s-author-scores.csv` | 281 author–paper totals; not 281 independent papers or an item matrix |
| `coding-1990s-paper-scores.csv` | Original 137-paper, 19-item matrix; not the expanded book sample |
| `coding-omissions.csv` / `coding-selected-cases.csv` | Reported omission metadata and selected case mappings |
| `coding-audit.py` / `coding-audit-results.json` | Reproducible arithmetic diagnostics, not replacement scholarly scores |
| `supporting-registry.json` | Application articles, separately identified drafts, EJW publication version, lecture and court sources |
| `supporting-references.bib` / `supporting-materials.md` | Generated from the supporting registry, separate from core bibliography |

Run `python3 sources/aer-audit/coding-audit.py` from the repository root to reproduce arithmetic. Add `--raw-dir /tmp` while this session's downloaded sources remain there to verify checksums and reparse the original HTML against the factual CSVs. Temporary source paths are retrieval provenance, not durable repository dependencies. Re-download only from the exact manifest URLs when needed; a changed checksum requires a version check.

Run `python3 scripts/build_catalogue.py` to rebuild both core and supporting bibliographic views. Run `python3 scripts/check_integrity.py` for links, identifiers, bibliographic structure and the closed slide gate. These checks do not establish that the article codes are correct, that the census is complete, or that any practical-harm claim is true.
