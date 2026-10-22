# Review B - ArtCraft Crafting Apps, verified (Opus 5.5)

**Date:** 2026-10-13. **Reviewer:** Claude Opus 5.5. **Method:** GitHub API
on the `storytold` org, local fork of `storytold/photocraft` (AGENTS.md,
ROADMAP.md, git log), getartcraft.com, press coverage 2026-10-07..12.
**Supersedes:** Review A s.A row 1 (app count). Snapshot numbers will go
stale within days; re-run before citing in manuscript.

## 1. Facts (snapshot 2026-10-13)

### What they clone (13 apps, repo created)

| App | Incumbent | Repo created | Releases to 10-12 | Latest |
|---|---|---|---|---|
| PhotoCraft | Photoshop | 2026-09-30 | 10 | v0.8.2 |
| VectorCraft | Illustrator | 2026-09-30 | 12 | v0.10.0 |
| FilmCraft | Premiere | 2026-09-30 | 8 | v0.7.2 |
| LightCraft | Lightroom | 2026-09-30 | 8 | v0.7.1 |
| PdfCraft | Acrobat | 2026-09-30 | 8 | v0.7.1 |
| EffectCraft | After Effects | 2026-10-01 | 10 | v0.9.2 |
| DesignCraft | InDesign | 2026-10-01 | 8 | v0.7.1 |
| WordCraft | Word | 2026-10-07 | 5 | v0.6.1 |
| GridCraft | Excel | 2026-10-07 | 5 | v0.6.1 |
| DeckCraft | PowerPoint | 2026-10-07 | 5 | v0.6.1 |
| SoundCraft | Pro Tools | 2026-10-07 | 4 | v0.6.1 |
| CADCraft | AutoCAD | 2026-10-07 | 5 | v0.6.2 |
| FigCraft | Figma | 2026-10-09 | 5 | v0.5.1 |

Plus shared infra: craft-libs, craft-fonts, craft-launcher (+ web build),
craft-common-actions, craft-repo-status-app, photocraft-corpus.

- **Release cadence:** 93 releases across 13 apps, 2026-10-02..12. About
  8.5/day suite-wide, about 1/day per app. "A release a day" holds per app.
- **Platforms:** macOS, Windows, Linux for all; Web (WASM) for all except
  FilmCraft (getartcraft.com/apps); PhotoCraft also FreeBSD.
- **Agent control:** PhotoCraft has one registry of 500+ commands; UI, CLI,
  JSON control channel and MCP server dispatch the same command ids.
  AGENTS.md rule 1: "Everything is a command." Fully agent-drivable is a
  build-time invariant, not a bolt-on.
- **Attention:** PhotoCraft ~54.8k GitHub stars by 2026-10-13 (13 days).
- **People:** lead Brandon Thomas (press: 15 years programming, ~3 years
  CEO of Storyteller.ai). PhotoCraft since 09-30: 1,511 commits, ~1,579
  `Co-Authored-By: Claude` trailers (nearly every commit agent co-authored);
  top human committers Thomas 250, then 95 / 93 / 84 / 56. 227 distinct
  authors overall. Read: one lead + parallel Opus 5.5 agents + a crowd that
  arrived after launch. Not "solo", not "a company of 5,000".

### Building method (from AGENTS.md / ROADMAP.md, PhotoCraft)

1. **Parity target measured against the real app.** Scored vs Photoshop
   27.11.0 "measured from the installed app on 2026-10-10". Generated
   checklist of every Photoshop menu item, live or missing. Menus 628/628,
   tools 56/68, panels 30/35, formats 13+4 of 31. Breadth ~76%, "ready for
   real work" ~45% (self-estimate).
2. **Effort budgeted in agent-hours.** Remaining distance to beta:
   "~1,100-1,800 h", in "Opus 5.5 agent wall-clock hours ... calibrated from
   this repository's 1,004 merged PRs"; "about 80% of the work parallelizes".
3. **Oracles everywhere.** CPU compositor as reference oracle for the wgpu
   compositor; Photoshop-authored PSD corpus (sha256-pinned); round-trip,
   synthetic-generator and fuzz tests; `panic_hunt` fuzzes every command
   with adversarial params; parity FLOOR may only rise.
4. **Machine-enforced code rules.** `unsafe_code = "forbid"` (one isolated
   exception), no unwrap/expect/panic outside tests via clippy deny.
5. **Clean-room in the project's words:** studied proprietary editors "for
   behaviour and look only"; implement from public specs (Adobe PSD spec,
   ICC, ISO 32000 blend modes, papers) and observation.
6. **Shared private standards** (`craftrules`) across apps; shared crates
   pinned by git revision.

### Not verified

- "Twenty more apps lined up": no public source found 2026-10-13. Site
  says only "More crafts on the way". Needs a dated statement or stays
  `[construction]`.
- Storyteller.ai funding history; Thomas's current role there.
- Download links reportedly removed from the site (trendingtopics,
  2026-10-12) vs GitHub releases present. Resolve.
- Office parity numbers (WordCraft ~60%, GridCraft 501/523 functions) come
  from secondary press; read the repos' own ROADMAP.md before citing.

## 2. Assessment of the book in light of these facts

**Verdict:** strong subject, unusually good evidence (the project publishes
its own dated parity metrics), wrong thesis in the Gemini draft.

**Thesis the evidence supports:** the moat was the labor cost of
reimplementation, not the law. Agents + oracles turned person-decades into
a few thousand parallelizable agent-hours.

**Question the book must answer:** GIMP, Krita, Inkscape, LibreOffice were
free for 20-30 years and did not break Adobe or Microsoft. So labor was
never the whole moat. Candidate answers (to be evidenced):

1. **Muscle memory is now the target.** GIMP declined to imitate Photoshop.
   ArtCraft targets 1:1 menus, shortcuts and file fidelity, measured item
   by item. Switching cost, the real moat, is attacked head-on.
2. **Agent-native from commit one.** When the operator is increasingly an
   agent, the MCP-drivable app beats the better app.
3. **Velocity exceeds the incumbent's release cycle.** Daily releases with
   a monotonic parity floor remove the "clone is always two years behind"
   assumption.

**Where the book gets attacked:** patents (see Review C), the last 25%
(color management, plugins, fidelity, stability - where open source
stalled before), distribution / code signing, and "zero cost" (the
project's own 1,100-1,800 agent-hours refute zero; use "near-zero marginal"
and chart agent-hours x token price instead).

**"Death of the app" (Gemini s.VI):** ArtCraft contradicts it. It ships
stable, versioned, parity-tracked clones, not throwaway software.
Disposable software fits where outputs can be verified by an oracle;
certification, liability and audited process keep stable apps alive.

## 3. Proposed chapter I opening

Lead with the agent-hours line. It is the first dated public artifact in
which a software project budgets its own remaining work in model time.
