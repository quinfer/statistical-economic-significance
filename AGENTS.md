# Research standards

## Purpose and scope

Develop a rigorous, balanced research knowledge base and PhD training resource on statistical versus economic significance in economics and finance. The project starts from the McCloskey–Ziliak debate but must not presume its conclusion. Use British English.

Work in four stages: verified literature; interconnected knowledge base; critical synthesis; Quarto reveal.js training. The initial scaffold is not a completed literature review. **Do not generate slides until the knowledge base and synthesis have been critically reviewed and the review decision is recorded in `reviews/review-gate.md`.** Planning teaching activities is permitted before that gate. The user's subsequent instruction on 24 October 2026 explicitly keeps the slide gate closed during this research phase; completing an agent review does not override that instruction.

## Source verification and citation integrity

1. Verify references against retrieved publisher, author, institutional repository or authoritative bibliographic records. Search snippets are discovery leads, not sufficient evidence for detailed claims. Prefer primary full text. Never invent bibliographic fields, quotations, empirical results or access claims.
2. Keep bibliographic verification separate from reading depth. A valid DOI does not establish that the paper supports a claim. Use `metadata_only`, `publisher_description`, `abstract_read`, `selected_sections_read` or `full_text_read`; the last label requires reading the complete text. A successful download is not a read.
3. Record exact consulted URLs, access date, document version, sections or printed page numbers, access limitations and verifier in `sources/registry.json`. Use printed pagination when checked, never infer it from a PDF viewer index. Preserve discrepancies and their resolution. Do not claim a publisher abstract is an independent replication.
4. Each substantive source claim must link to a paper note and a locatable passage, abstract or section. Label statements **Source claim**, **Project interpretation**, **Open question**, or **Illustration**. Attribution means an author made the claim; it does not establish the claim as true.
5. Abstracts support only what they actually say. Publisher book descriptions establish advertised scope, not detailed arguments or findings in unread chapters. Do not launder reviews or blurbs into claims of having read a book. Do not reconstruct inaccessible text from model memory.
6. Distinguish published articles, comments/editorials, books and working papers. Record online-first and issue-year differences. Do not count drafts and final versions as separate contributions unless the comparison is explicitly justified. Bibliographic aggregators may group draft and final locations under a working-paper DOI or version label: inspect the document's title page and journal pagination before upgrading final-text access. Preserve the earlier search outcome when a later user-supplied file resolves the gap.
7. Quote sparingly and exactly, with a checked locator. Prefer attributed paraphrase. Do not store or redistribute copyrighted full texts without an appropriate basis. The repository stores original research notes, bibliographic records and links by default.
8. Every reference included in the core corpus must have verified identity. A candidate that remains unverified belongs in the search backlog, not `references.bib`. Citation counts, journal rankings and author reputation are not truth tests or sufficient selection criteria.
9. Record failed access accurately. A blocked API is not evidence of paywall status, an absent paper or exhausted quota. No invented OpenAlex IDs or claimed API results.

## Methodological balance

Represent each position in its strongest defensible form. Separate disagreement about observed research practice, statistical theory, inferential interpretation and normative decisions. Cross-link rebuttals and identify which proposition they challenge. Do not equate defending calibrated inference with defending mechanical p < .05 rules.

Keep the estimand, estimator, uncertainty model, identification assumptions and decision criterion distinct. Specify units, population, horizon, costs, welfare or utility weights, heterogeneity, and scale when discussing economic importance. A large point estimate is not proof of a large population effect; a non-significant result is not proof of a negligible effect.

Do not assert that all meaningful knowledge requires a significance test, or that every rational action requires rejection of a null. Consider confidence sets, Bayesian posterior decisions, minimax regret, partial identification and robust decisions. Distinguish uncertainty quantification from dichotomous significance testing. Report the assumptions and limitations of each approach, including priors, loss functions and equivalence margins.

Record what would change a tentative conclusion. Seek disconfirming evidence. Disagreements remain open until an evidence trail and critical review justify narrowing them. Absence of a retrieved counterargument is not consensus.

## Wiki and evidence workflow

Use stable source IDs and ordinary relative Markdown links. Maintain `wiki/index.md`, individual paper notes, conceptual notes, claim records and explicit disagreements. Paper notes link to concepts and claims; conceptual and claim notes link back to evidence. `sources/registry.json` is the bibliographic source of truth; `sources/references.bib` and `sources/literature-map.md` are generated from it.

Keep all candidate dispositions, search queries and coverage gaps in `sources/search-log.md`. Separate first-pass verification from independent critical review. A second agent can check source fidelity, but agreement between agents does not replace retrieval or human scholarly judgement.

Supporting application papers, drafts, lectures and legal sources used to audit core claims belong in `sources/aer-audit/supporting-registry.json`, with a separate generated bibliography and evidence-note links. They do not expand the 25–35-work core or turn draft/final versions into independent contributions. A supplied document's self-identification must be distinguished from independently corroborated bibliographic identity. Coding artefacts have their own provenance manifest, checksums and factual transcriptions.

For historical audits, distinguish the original 137-paper 1990s matrix from the book's expanded 187-paper survey, and author-paper rows from independent papers. Reproducing an aggregate is not validation of the underlying codes. Do not infer absence of magnitude reasoning from every negative questionnaire item, or use the presence of a magnitude to acquit every selection/interpretation step. Preserve uncertainty over table transcription and draft/final differences beside the claim they affect.

Paper notes preserve handwritten analysis. Their `registry-sha256` comment identifies the source-record snapshot used to create them; a changed registry record triggers a stale-note error. Reconcile source-derived metadata, claims and limitations with the new record before updating that fingerprint. Never refresh the fingerprint merely to silence the check.

## Reproducibility and review

Use local Git commits for coherent milestones. Do not add a remote or publish unless requested. Never fabricate review approvals or clear a gate by renaming a draft. Record reviewer, date, material reviewed, objections and resolution. The slide gate requires a recorded review decision, not simply a passing script.

Future simulations must declare their data-generating process, estimand, seed, units, assumptions, loss function and Monte Carlo error. Synthetic examples must be visibly labelled. Check numerical claims with code, and distinguish a simulation from evidence about actual markets or policies. Do not tune examples only to favour one methodological position.

Run `python3 scripts/build_catalogue.py` after registry edits and `python3 scripts/check_integrity.py` before a milestone commit. The checker validates structure and links; it cannot certify citation truth or methodological correctness. Broader testing is needed when numerical teaching materials are implemented.

## Learning repository maintenance

The user requested a public learning repository on 23 November 2026. Keep the learning entry points (`README.md`, `QUICKSTART.md`, `CURRICULUM.md`, `papers/`, `resources/`, `exercises/`) aligned with the evidence wiki and honest `STATUS.md`. Run `python3 scripts/check_all.py` for structural, coding-arithmetic and mathematical checks. Deterministic normal-model illustrations are available in `implementations/`; they are not empirical findings or Monte Carlo simulations. Record units and assumptions in every numerical exercise. Public learning publication does not override the closed slide gate.

Earlier local research history contains private machine locations and must not be pushed to the public repository. Public updates must descend from the public snapshot history. Preserve source hashes and reading limits when making provenance locations portable.
