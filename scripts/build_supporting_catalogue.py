#!/usr/bin/env python3
"""Build the separately scoped audit bibliography; never expand the core corpus."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "sources/aer-audit"


def build():
    rows = json.loads((DIRECTORY / "supporting-registry.json").read_text())["sources"]
    entries = []
    lines = ["# Supporting audit materials", "",
             "These version and case records support a bounded documentary audit. They are **outside the 35-work core**; drafts and finals do not count as independent contributions. Identity checks and reading depths remain separate. The supplied lecture's identity is verified from the document, not from a second public copy.", "",
             "[Registry](supporting-registry.json) · [BibTeX](supporting-references.bib) · [Coding provenance](coding-manifest.json) · [Coding audit](../../wiki/evidence/aer-coding-audit.md)", "",
             "| Material | Version / type | Reading depth | Evidence note |",
             "|---|---|---|---|"]
    for r in rows:
        assert r["core_corpus"] is False
        fields = {"author": " and ".join(r.get("bibtex_authors", r["authors"])),
                  "title": "{" + r["title"] + "}", "year": str(r["year"])}
        kind = {"article": "article", "working_paper": "techreport"}.get(r["type"], "misc")
        fields[{"article": "journal", "working_paper": "institution"}.get(r["type"], "howpublished")] = r["venue"]
        for key, field in [("volume", "volume"), ("issue", "number"), ("pages", "pages"), ("doi", "doi")]:
            if r.get(key):
                fields[field] = str(r[key]).replace("–", "--")
        urls = [u["url"] for u in r["urls"] if u.get("consulted")]
        if urls:
            fields["url"] = urls[0]
        fields["note"] = "Supporting audit material, outside core corpus; " + r["version"]
        def escape(key, value):
            return value if key in {"doi", "url"} else value.replace("&", r"\&").replace("%", r"\%").replace("_", r"\_")
        entries.append("@" + kind + "{" + r["id"] + ",\n" + ",\n".join(
            f"  {k} = {{{escape(k, v)}}}" for k, v in fields.items()) + "\n}\n")
        lines.append(f"| {r['title']} ({r['year']}) | {r['type']} | `{r['reading_depth']}` | [Reading / limits]({r['evidence_note']}) |")
    (DIRECTORY / "supporting-references.bib").write_text("% Generated from supporting-registry.json; separate from core corpus.\n\n" + "\n".join(entries))
    (DIRECTORY / "supporting-materials.md").write_text("\n".join(lines) + "\n")
    return rows


if __name__ == "__main__":
    print(f"Built {len(build())} supporting version/material records; core unchanged.")
