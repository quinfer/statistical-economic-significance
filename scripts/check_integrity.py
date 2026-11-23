#!/usr/bin/env python3
"""Check local research structure, not citation truth or review adequacy."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse
from build_catalogue import record_fingerprint

ROOT = Path(__file__).resolve().parents[1]
rows = json.loads((ROOT / "sources/registry.json").read_text())["sources"]
errors = []
depths = {"metadata_only", "publisher_description", "abstract_read", "selected_sections_read", "full_text_read"}
required = {"id", "authors", "year", "title", "type", "venue", "theme", "reading_depth", "version", "urls", "source_claim", "project_relevance", "limitations", "metadata_notes", "next_reading", "verifier", "verified_on", "bibliographic_status", "critical_review"}
ids, dois = set(), set()
for r in rows:
    sid = r.get("id", "MISSING")
    if missing := required - set(r):
        errors.append(f"{sid}: missing fields {sorted(missing)}")
    if sid in ids:
        errors.append(f"Duplicate source ID: {sid}")
    ids.add(sid)
    if r["reading_depth"] not in depths:
        errors.append(f"{sid}: invalid reading depth")
    if r["bibliographic_status"] != "verified_identity":
        errors.append(f"{sid}: unverified source in selected corpus")
    if not any(u.get("consulted") and u.get("locator") for u in r["urls"]):
        errors.append(f"{sid}: no consulted source locator")
    for u in r["urls"]:
        if urlparse(u["url"]).scheme not in {"http", "https"}:
            errors.append(f"{sid}: invalid external URL")
    if d := r.get("doi", "").lower():
        if d in dois:
            errors.append(f"Duplicate DOI: {d}")
        dois.add(d)
        if not re.fullmatch(r"10\.\d{4,9}/\S+", d):
            errors.append(f"{sid}: invalid DOI syntax")
    note = ROOT / "wiki/papers" / f"{sid}.md"
    if not note.exists():
        errors.append(f"Missing note: {sid}")
    elif sid not in note.read_text():
        errors.append(f"Missing source ID in note: {sid}")
    elif f"<!-- registry-sha256: {record_fingerprint(r)} -->" not in note.read_text():
        errors.append(f"{sid}: stale registry snapshot in note; reconcile source-derived content before updating its fingerprint")
    if "others" in r["authors"] and not r.get("authors_abbreviated"):
        errors.append(f"{sid}: abbreviated authors not flagged")

if not 25 <= len(rows) <= 35:
    errors.append(f"Corpus outside requested 25–35 range: {len(rows)}")

bib = (ROOT / "sources/references.bib").read_text()
bib_ids = re.findall(r"@\w+\{([^,]+),", bib)
if set(bib_ids) != ids or len(bib_ids) != len(ids):
    errors.append("BibTeX entries do not match registry IDs")

support_path = ROOT / "sources/aer-audit/supporting-registry.json"
if support_path.exists():
    supporting = json.loads(support_path.read_text())["sources"]
    support_ids = [r["id"] for r in supporting]
    if len(set(support_ids)) != len(support_ids) or set(support_ids) & ids:
        errors.append("Duplicate supporting IDs or overlap with core IDs")
    for r in supporting:
        if r.get("core_corpus") is not False or r.get("reading_depth") not in depths:
            errors.append(f"{r['id']}: invalid supporting scope/depth")
        if r.get("bibliographic_status") not in {"verified_identity", "verified_supplied_document_identity"}:
            errors.append(f"{r['id']}: missing supporting identity verification")
        if not (support_path.parent / r["evidence_note"]).exists():
            errors.append(f"{r['id']}: missing supporting evidence note")
        if not r.get("urls") and not r.get("source_location"):
            errors.append(f"{r['id']}: missing source location")
    support_bib = (support_path.parent / "supporting-references.bib").read_text()
    support_keys = re.findall(r"@\w+\{([^,]+),", support_bib)
    if set(support_keys) != set(support_ids) or len(support_keys) != len(support_ids):
        errors.append("Supporting BibTeX entries do not match supporting registry")

for path in ROOT.rglob("*.md"):
    if ".git" in path.parts or "scratch" in path.parts:
        continue
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        target = target.split("#", 1)[0].strip("<>")
        if not target or urlparse(target).scheme:
            continue
        if not (path.parent / unquote(target)).exists():
            errors.append(f"Broken local link in {path.relative_to(ROOT)}: {target}")

gate = (ROOT / "reviews/review-gate.md").read_text()
gate_states = re.findall(r"^\*\*Status: (NOT PASSED|PASSED)\.\*\*", gate, re.MULTILINE)
if len(gate_states) != 1:
    errors.append("Missing or ambiguous review-gate status; unknown status remains blocked")
if gate_states != ["PASSED"]:
    for pattern in ("*.qmd", "*.pptx"):
        if list((ROOT / "training").rglob(pattern)):
            errors.append("Training artifact exists while critical-review gate is not passed")

if errors:
    print("INTEGRITY CHECK FAILED\n" + "\n".join(errors))
    raise SystemExit(1)
print(f"PASS: {len(rows)} source records, matching BibTeX, paper notes and local Markdown links; review gate respected.")
print("This check does not establish source fidelity, scientific validity or review approval.")
