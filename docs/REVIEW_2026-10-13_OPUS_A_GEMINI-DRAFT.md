# Review A - Gemini first draft (Opus 5.5)

**Date:** 2026-10-13 (morning, before web verification). **Reviewer:** Claude
Opus 5.5. **Source:** `docs/GEMINI_DRAFT_2026-10-13.md`.
**Status:** kept as written for the record. **Partly superseded by Review B**
(same day): the app-count row below is WRONG. It relied on a stale list in
the PhotoCraft README; the storytold org had 13 Crafting Apps, including
WordCraft / GridCraft / DeckCraft (created 2026-10-07). Gemini's "twelve,
through DeckCraft" was close to correct. The "solo" row stands only in
nuanced form (see Review B s.1).

## Summary

The Gemini draft has a good spine (headless engine + MCP control plane as
the real inversion; amortized compute as the subsidy; physical firewall as
the honest close). But its three load-bearing factual claims about the
cold-open subject are contradicted by the public repo, and its legal
argument is the weakest link in the book. Rewrite before building
on it. The fix is not cosmetic: a book whose thesis is "the moats were
illusions" cannot afford to rest on illusions of its own.

## A. Facts the draft gets wrong (checked against the local fork of
`storytold/photocraft`, last upstream commit 2026-10-11)

| Draft claim | Observed | Action |
|---|---|---|
| "twelve-app ecosystem ... PhotoCraft through DeckCraft" | PhotoCraft README lists **7** Crafting Apps: PhotoCraft, VectorCraft, FilmCraft, LightCraft, PdfCraft, EffectCraft, DesignCraft. No WordCraft / GridCraft / DeckCraft listed. | Use 7, dated. Office suite = `[construction]` until a public repo exists. |
| "Born not from a venture-backed startup ... but from an experienced developer" (solo) | Org `storytold`, app IDs `ai.storyteller.*`. First commit 2026-09-30 by Brandon Thomas; **227** distinct commit authors by 2026-10-11, including 275 commits authored as "Claude". | Drop "solo". The real story is sharper: a small company + one lead + agent co-authors + a fast-forming community, 11 days. Funding status = `[construction]`, verify. |
| "clean-room ... Laundering Effect: provenance dissolved into statistical representations" | README defines clean-room as "implemented from public specs and observed behaviour only. No proprietary code, shaders or assets." | That is the *legal discipline*, the opposite of laundering. Do not put words in the project's mouth that invite litigation. |

## B. Arguments that need repair

1. **IP Litigation Bluff (Ch III).** Wrong frame. Copyright never protected
   the Bezier curve; it was not the moat. The real legal surface is:
   patents (method claims on e.g. content-aware fill, codecs); EULA
   anti-reverse-engineering clauses; DMCA s.1201 / EU Software Directive
   Art. 6 interoperability carve-out; trademark and trade dress (UI look,
   names, icons); file-format specs (the PSD spec is published, which is why
   the attack works there). Anchor cases: *Sega v. Accolade* (1992),
   *Sony v. Connectix* (2000), *Oracle v. Google* (US Supreme Court, 2021-04-05),
   *SAS Institute v. World Programming* (CJEU C-406/10, 2012-05-02).
   The defensible thesis: the moat was never IP, it was **labor cost of
   reimplementation**; agents collapsed that cost, and the law
   *already* allowed clean-room reimplementation. That is stronger than a bluff
   claim and survives a lawyer reading it.
2. **"Silicon does not rot" (Ch VII).** Half true. It understates
   (a) hardware failure at scale (Meta's Llama 3 paper, 2024-07: 419
   unexpected interruptions in 54 days on 16k H100s, majority GPU/HBM
   related; verify figures before citing), and (b) **perf-per-watt
   obsolescence**: an amortized A100 still pays full price for electricity
   per token, and when newer silicon makes tokens cheaper per joule, the old
   rack is uneconomic before it is dead. Dark fiber was different: glass
   gets better with new lasers at the ends. GPUs do not. Keep the analogy,
   but name where it breaks.
3. **"Zero-cost."** Marginal cost of *replication* approaches zero; cost of
   *synthesis* is not zero (tokens, review, test oracles: PhotoCraft
   ships 1,700+ tests and Photoshop-authored oracle PSDs). The title promise
   should be "near-zero marginal" or the book gets caught out by its own Ch VII.
4. **Lineage table (Ch II).** Jacquard/Ford/Hinton hold. Huang is OK
   (vs. scalar CPU). The **Amodei row is a category error**: constitutional
   scaffolding *constrains* a mechanizer; it breaks no guild. Either move it to
   a "brakes" column or replace with a demolition figure (e.g. Linus Torvalds /
   GNU for Unix licensing, or Stallman 1983). Dates needed for Huang (CUDA
   2006-11?) `[construction]`.
5. **"Sub-twenty millisecond cold boot", "gigabytes to megabytes."** Plausible
   for egui; needs a measured number from a named app on named hardware
   (`perf/` dir exists in photocraft - mine it) or cut.
6. **"Death of the Application" (Ch IX).** Overreach as written. Counter-force
   to name: file formats, collaboration, certification (medical, avionics,
   accounting software) and liability need *stable* artifacts. Ephemeral
   software works where outputs are verifiable; it fails where the
   *process* must be audited. That boundary is the chapter.

## C. Hazard (Rule 2) - Level 3 "Dark Mirror"

The draft's Level 3 names BreachCraft (EDR evasion), KineticCraft
(GPS-denied terminal strikes) and SyndicateCraft (precursor logistics).
These stay in the book **only** as named categories with institutional
facts and governance criteria (who regulates, what export-control /
platform / dual-use regimes apply, what is already publicly documented).
No mechanism, no architecture diagram, no component list. KineticCraft
defers to `on-hyperwar`, which already owns that domain under its own
hazard rule. Moved to `chapters/side-dark-mirror.md`, out of the main ladder,
so the book's spine does not depend on it.

## D. What transfers from sisters

Ladder method (reversibility ordering), thresholds-as-attachment-points,
living Ch V with revision dates, `[construction]` flag discipline, lorecheck
+ declaim gates, Issues as system of record. Fleet link: on-ai-takeover's
$50/seat SaaS collapse is this book's Ch V seen from the buyer's side.

## E. Housekeeping found in passing

- `on-hyperart` serves on 10968, which `WEBAPP_PORTS.md` assigns to kick-mcp.
  This repo claims **11026** (free in registry at 2026-10-13); registry line not
  yet added.

## Gate to v0.2

Ch V with >= 7 dated rows (one per Crafting App first public commit / first
release), Ch III rewritten on case law, Ch VII failure-rate + perf/watt cite,
funding status of Storyteller verified. Then multi-model fill pass.
