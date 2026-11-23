# Initial scaffold review — 24 October 2026

**Scope:** source-record spot-checks, argument-framework critique and infrastructure inspection. **This does not pass the knowledge-base/synthesis review gate.** No complete substantive synthesis exists yet.

## Source-fidelity spot-check

Reviewer: research subagent `debate_sources`, checking records prepared by other research streams. Independently retrieved publisher or primary-document evidence for Wasserstein–Lazar 2016, Wasserstein–Schirm–Lazar 2019, Imbens 2021, Manski 2021 and Kandel–Stambaugh 1996. No material metadata or attribution errors found in those five records.

The review reconfirmed the distinction between the official ASA statement and the 2019 editorial, and the supersession of Manski's 2019 draft by the differently titled 2021 publication. It recommended specifying that current predictor values affect portfolio choice in Kandel–Stambaugh; that precision correction was applied to the registry and paper note. The entire 32-work corpus has not received independent second-pass checking.

## Argument-framework critique

Reviewer: research subagent `inference_sources`, inspecting the conceptual notes, claims, positions and pre-synthesis framework.

| Finding | Revision |
|---|---|
| A negligible but significant effect tests sufficiency, not necessity | Split H1 into necessary and sufficient conditions and assigned examples accordingly |
| Minimax-regret discussion omitted minimisation and blurred action versus rule | Defined maximum expected regret and sampling-based evaluation of a data-dependent rule separately from choosing an action after observing data |
| Abolition and retention proposals could appear mutually exclusive | Labelled distinct axes and stated specialised decision-use exceptions beside the abolition position |

## Infrastructure inspection

Reviewer: research subagent `decision_finance_sources`, comparing its original records with the registry and inspecting generated notes and scripts.

| Finding | Revision |
|---|---|
| Registry changes could leave readable paper notes silently stale | Added per-record fingerprints; integrity check now requires reconciliation after source-record changes |
| Generated reading/review status was hardcoded | Generated status now derives from registry fields and counts |
| An unrecognised gate sentence could skip checks | Missing or ambiguous gate status now fails the check and remains blocked |

## Validation and remaining limits

The main integrity check passes for 32 records, matching bibliography entries and paper notes, and local Markdown links. Isolated temporary fixtures confirmed that stale records, unknown gate status and premature deck files are detected; repeated generation preserves handwritten notes; status text follows changed registry fields. Temporary fixture artifacts were removed automatically. No slide file was created in the research repository.

These checks validate consistency and guard against specific workflow errors. They do not validate empirical findings, certify a complete reading, reproduce the AER audit or adjudicate competing methodologies. The [critical-review gate](review-gate.md) remains **NOT PASSED**.
