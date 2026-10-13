# Assessment - on-metacraft (rolling)

**Last updated:** 2026-10-13. **Stage:** skeleton v0.1, 0/10 chapters real.

Dated reviews live in `docs/REVIEW_<date>_<model>_<letter>_<topic>.md`.
Never edit a review after its date; supersede it with a new one and note
it here.

**Opinion marking:** from Review E on, Opus judgments are marked as
`> **OPUS OPINION ...**` blocks; everything else is fact or a summary of
Sandra's position. In Reviews A-D, any statement without a cite or
`[construction]` flag is Opus opinion. Cross-model reviews go in as `REVIEW_<date>_<MODEL>_<letter>_<topic>.md`
(GEMINI, GROK, ...), answering by letter; free-form assessments
(`<tool>-assessment-<date>.md`) are indexed here too. Opinion blocks use the
reviewer's name (`> **GEMINI OPINION**`, `> **GROK OPINION**`).

| Date | Review | Verdict | Status |
|---|---|---|---|
| 2026-10-13 | [A - Gemini draft](REVIEW_2026-10-13_OPUS_A_GEMINI-DRAFT.md) | Good spine, wrong thesis; legal frame rebuilt; Level 3 hazard-boxed | App-count row superseded by B |
| 2026-10-13 | [B - ArtCraft verified](REVIEW_2026-10-13_OPUS_B_ARTCRAFT.md) | 13 apps, about 1 release/day/app, agent-hour budgeting, oracle-driven method | Current |
| 2026-10-13 | [C - Patent objection](REVIEW_2026-10-13_OPUS_C_PATENTS.md) | Patents are a weak, decaying moat; Bessemer and "Shenzhen ignores" need replacing | Current |
| 2026-10-13 | [D - Checking cost](REVIEW_2026-10-13_OPUS_D_CHECKING-COST.md) | Targets unbounded; checking cost sets the order; law stops defendants, not practices; compatibility beats familiarity | Current |
| 2026-10-13 | [E - Physical ladder + MetaCraft](REVIEW_2026-10-13_OPUS_E_PHYSICAL-AND-METACRAFT.md) | Physical rungs ordered by test cost; MetaCraft L0-L4, L3 (agents build checkers) is the unlock; incumbent as test bench; 4 questions for Gemini | Answered by F |
| 2026-10-13 | [F - Cross-model assessment](REVIEW_2026-10-13_GEMINI_F_CROSS_MODEL_ASSESSMENT.md) | Answers 4 questions; 6-rung physical ladder; L0-L4 formalization; oracle triangulation trap | Current |
| 2026-10-13 | [Cursor (Grok 4.6) assessment](cursor-assessment-2026-10-13.md) | Thesis right (checking cost, dated breach); working notes stronger than chapters; Review F not yet absorbed | Current, independent |

## Current thesis

The moat was the labor cost of reimplementation, not the law. Agents plus
cheap automated oracles collapsed that cost in 2026. What remains is
switching cost, distribution, certification and liability, plus a narrow
and decaying patent surface.

## Open items (gate to v0.2)

- Reddit AutoCAD-request thread: URL + date (did it precede 2026-10-07?).
- Storyteller.ai funding / Thomas's role.
- Download-link removal vs GitHub releases.
- Office-app parity numbers from their own ROADMAP.md files.
- Verify all `[construction]` dates in Review C before manuscript use.
- Port 11026 registered in WEBAPP_PORTS.md; on-hyperart's collision resolved (assigned to 11156).
- Refine Chapter VIII with the 6-rung physical ladder from Review F.
- Refine Chapter IX with metamorphic testing and oracle triangulation trap analysis.

## Stage at 2026-10-13

All chapters have Draft v0.1 prose. Lorecheck: 0/10 chapters real (stubs/drafts),
27 open flags in claims ledger (`docs/claims.json`). All tools migrated to shared
bookkit shims. Next: burn down [construction] flags and integrate Review F ladder.

