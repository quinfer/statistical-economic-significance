#!/usr/bin/env python3
"""Build bibliographic views; --init-notes creates missing notes only."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    "debate": ("The original economics debate", "economic-significance", "C004-practice-and-validity"),
    "inference": ("Interpretation and reform", "statistical-inference", "C005-threshold-reforms"),
    "intervals": ("Confidence intervals", "intervals", "C007-intervals"),
    "power": ("Power, precision and selection", "power-selection", "C006-noisy-magnitudes"),
    "equivalence": ("Meaningful thresholds and equivalence", "equivalence", "C003-equivalence"),
    "decision": ("Decisions under uncertainty", "decisions", "C002-action-without-rejection"),
    "identification": ("Identification and transportability", "identification", "C009-identification"),
    "finance": ("Finance and contested replication", "finance", "C008-finance-replication"),
}


def read_sources():
    return json.loads((ROOT / "sources/registry.json").read_text())["sources"]


def record_fingerprint(record):
    """Track the source snapshot underlying a note without overwriting analysis."""
    return hashlib.sha256(json.dumps(record, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def bib_escape(value):
    return str(value).replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")


def bib_entry(r):
    fields = {"author": " and ".join(r.get("bibtex_authors", r["authors"])), "title": "{" + r["title"] + "}", "year": r["year"]}
    venue_field = {"book": "publisher", "working_paper": "institution"}.get(r["type"], "journal")
    fields[venue_field] = r["venue"]
    for src, dst in [("volume", "volume"), ("issue", "number"), ("pages", "pages"), ("article_number", "eid"), ("doi", "doi")]:
        if r.get(src) and not (src == "pages" and r["type"] == "book"):
            fields[dst] = r[src].replace("–", "--")
    fields["url"] = next(u["url"] for u in r["urls"] if u["consulted"])
    notes = []
    if r.get("authors_abbreviated"):
        notes.append("Author list explicitly abbreviated; consult publisher for complete list")
    if r.get("bibliography_note"):
        notes.append(r["bibliography_note"])
    if notes:
        fields["note"] = "; ".join(notes)
    kind = {"book": "book", "working_paper": "techreport"}.get(r["type"], "article")
    # Identifiers must remain literal, notably a versioned OSF DOI containing '_'.
    return "@" + kind + "{" + r["id"] + ",\n" + ",\n".join(f"  {k} = {{{v if k in {'doi', 'url'} else bib_escape(v)}}}" for k, v in fields.items()) + "\n}\n"


def catalogue_text(rows):
    counts = Counter(r["reading_depth"] for r in rows)
    full_read = counts.get("full_text_read", 0)
    text = ["# Literature catalogue", "", "Generated from [registry.json](registry.json). **Target: 25–35 works; identity verification is not full-text review.**", "", f"Current records: **{len(rows)}**. Reading depths: " + "; ".join(f"{k}: {v}" for k, v in sorted(counts.items())) + ".", "", "All records have externally checked bibliographic identity. Primary full texts, abstracts, publisher descriptions and catalogue records provide different levels of support; the paper notes document these limits. " + f"Sources recorded as completely read: {full_read}. This label is distinct from critical-review approval.", "", "See [search log](search-log.md), [BibTeX](references.bib), [taxonomy](../planning/literature-taxonomy.md) and [review gate](../reviews/review-gate.md). An abbreviated author list is explicitly marked in the relevant record and BibTeX entry.", ""]
    for theme, (label, _, _) in THEMES.items():
        text += [f"## {label}", "", "| Paper | Year | Venue / type | Reading depth |", "|---|---:|---|---|"]
        for r in rows:
            if r["theme"] == theme:
                text.append(f"| [{r['title']}](../wiki/papers/{r['id']}.md) | {r['year']} | {r['venue']} / {r['type']} | `{r['reading_depth']}` |")
        text.append("")
    return "\n".join(text)


def paper_note(r):
    _, concept, claim = THEMES[r["theme"]]
    identity = "; ".join(r["authors"]) + f" ({r['year']}). *{r['title']}*. {r['venue']}"
    if r.get("volume"):
        identity += f", {r['volume']}" + (f"({r['issue']})" if r.get("issue") else "")
    if r.get("pages"):
        identity += ", " + r["pages"]
    if r.get("article_number"):
        identity += ", article " + r["article_number"]
    identity += "."
    urls = "\n".join(f"- [{u['role']}]({u['url']}) — {'consulted' if u['consulted'] else 'not successfully consulted'}; {u['locator']}" for u in r["urls"])
    doi = f"[DOI](https://doi.org/{r['doi']})" if r["doi"] else "DOI not verified; none supplied."
    return f"""<!-- registry-sha256: {record_fingerprint(r)} -->
# {r['title']}

{identity}

**Source ID:** `{r['id']}`

**Bibliographic status:** {r['bibliographic_status']}

**Reading depth:** `{r['reading_depth']}`

**Version:** {r['version']}

**Checked:** {r['verified_on']}, by {r['verifier']}

**Critical review:** {r['critical_review']}. {doi}

## Evidence consulted

{urls}

## Source claim

{r['source_claim']}

## Project interpretation

{r['project_relevance']}

## Limits and unresolved questions

{r['limitations']}

**Metadata notes:** {r['metadata_notes']}

**Next reading:** {r['next_reading']}

## Connections

[Concept](../concepts/{concept}.md) · [Claim to examine](../claims/{claim}.md) · [Competing positions](../disagreements/methodological-positions.md) · [Paper index](index.md) · [Registry](../../sources/registry.json)

The thematic links indicate relevance, not endorsement of every proposition in the linked notes.
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--init-notes", action="store_true")
    args = parser.parse_args()
    rows = read_sources()
    (ROOT / "sources/references.bib").write_text("% Generated from registry.json; verified fields only.\n% Reading and critical-review status are in the registry, not implied by a citation.\n\n" + "\n".join(bib_entry(r) for r in rows))
    (ROOT / "sources/literature-map.md").write_text(catalogue_text(rows))
    note_dir = ROOT / "wiki/papers"
    note_dir.mkdir(parents=True, exist_ok=True)
    index = ["# Paper notes", "", "Initial notes retain explicit source-access limits. A bibliographic record is not a claim of complete reading.", "", "[Wiki home](../index.md) · [Literature catalogue](../../sources/literature-map.md)", ""]
    for r in rows:
        path = note_dir / (r["id"] + ".md")
        if args.init_notes and not path.exists():
            path.write_text(paper_note(r))
        index.append(f"- [{r['title']} ({r['year']})]({r['id']}.md)")
    (note_dir / "index.md").write_text("\n".join(index) + "\n")
    if (ROOT / "sources/aer-audit/supporting-registry.json").exists():
        from build_supporting_catalogue import build
        print(f"Built {len(build())} separately scoped supporting records.")
    print(f"Built catalogue and BibTeX for {len(rows)} sources. Existing paper notes preserved.")


if __name__ == "__main__":
    main()
