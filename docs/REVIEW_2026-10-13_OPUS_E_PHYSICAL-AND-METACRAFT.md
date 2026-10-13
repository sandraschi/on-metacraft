# Review E - The physical ladder and MetaCraft (Opus 5.5)

**Date:** 2026-10-13. **Reviewer:** Claude Opus 5.5. **Trigger:** Sandra,
2026-10-13: the future pivot to physical human activity (NeedleCraft,
FashionCraft) and MetaCraft, "the craft that makes craft under agentic
control, with increasingly powerful and independent agent swarms".
**Next reader:** Gemini (cross-model review), Sandra judging.

**Marking convention:** plain text = summary of Sandra's position or
checkable fact (with `[construction]` where unverified). Blocks starting
with **OPUS OPINION** are my judgment and are open to challenge.

## 1. The physical pivot

### Position (Sandra)

After media and office software, the Craft method moves into physical
human activity: needlework, fashion, making. Craft software there is the
expensive, locked-in layer between a person and their machine.

### Facts and targets

In these domains the software does not make the object; it emits
machine instructions:

| Domain | Typical incumbent software | Output |
|---|---|---|
| Machine embroidery | Wilcom, Hatch, Brother PE-Design | DST, PES, EXP stitch files |
| Machine knitting | Shima Seiki SDS-ONE, Stoll M1plus | knitting-machine programs |
| Pattern-making | Gerber AccuMark, Lectra Modaris, Optitex | graded 2D pattern pieces, markers |
| 3D garment | CLO3D, Browzwear | simulated garments, patterns |
| Home cutting | Cricut Design Space (subscription, machine-tied) | cut paths |

`[construction: verify current pricing and licensing model of each]`

> **OPUS OPINION - the ordering rule carries over.** Review D ordered
> software targets by the cost of checking a clone. In physical domains
> the same rule applies, with the cost of a *physical test* as the axis:
>
> | Domain | Physical check | Cost per check |
> |---|---|---|
> | Embroidery, cutting | stitch-out / cut on scrap | cents, minutes, at home |
> | Knitting | swatch | small |
> | Garment fit | bodies vary, fabric drapes | medium, needs people |
> | Agriculture (Gemini's SoilCraft) | a field season | a year |
> | Chips (EDA) | tape-out | millions |
>
> Consequence: needlecraft is not a distant rung. It is plausibly the
> next one after office software, because its physical check fits on a
> kitchen table.

> **OPUS OPINION - the moat migrates to the machine maker.** Once the
> design software is free, lock-in moves to proprietary formats,
> cloud-required apps and firmware. Agriculture shows the pattern: the
> fight there is firmware and right-to-repair, not CAD
> (`[construction: FTC v. Deere, 2025 - verify date and status]`).
> Expect the same in sewing and cutting machines.

> **OPUS OPINION - the cultural inversion.** When the license is free,
> the human skill (hand, eye, judgment about cloth) becomes the scarce,
> valuable part again. This fits the closing line "the tools are
> returning to the edge" better than the Gemini draft's framing.

## 2. MetaCraft

### Position (Sandra)

MetaCraft is the foundry that produces Crafts, run by agent swarms that
become more powerful and more independent over time.

### Facts: ArtCraft as an early MetaCraft

From Review B (PhotoCraft AGENTS.md / ROADMAP.md, 2026-10-11..13), the
method is already a reusable foundry recipe:

| Foundry part | ArtCraft instance |
|---|---|
| Spec | parity docs scored against the installed incumbent; generated menu checklist |
| Ground truth | Photoshop 27.11.0, "measured from the installed app on 2026-10-10" |
| Budget | remaining work in "Opus 5.5 agent wall-clock hours" (~1,100-1,800 h to beta) |
| Checkers | CPU reference compositor, Photoshop-authored PSD corpus, fuzzing of every command |
| Foundry standards | private `craftrules` repo shared across apps |
| Output | 13 apps, about one release per app per day |

A human currently chooses targets and approves the rules.

### Autonomy levels

> **OPUS OPINION - a proposed ladder for Ch IX.**
>
> | Level | Who does what | Status 2026-10-13 |
> |---|---|---|
> | L0 | Humans write the code | the old world |
> | L1 | Agents co-author against human-made specs and checkers | ArtCraft now |
> | L2 | Agents write the parity spec by examining the incumbent; pick targets from demand signals | partly visible (generated parity checklist) |
> | L3 | Agents build the checkers themselves | not yet evidenced |
> | L4 | The foundry improves its own method, rules and pipeline | MetaCraft proper |

> **OPUS OPINION - L3 is the real unlock.** Review D says checking cost
> sets the order in which software falls. Today humans build the costly
> checkers. A foundry that builds its own removes the constraint that
> sets the order. That is the step from fast to storm.

> **OPUS OPINION - the foundry needs the original alive.** If a swarm
> writes both product and tests, it can agree with its own bugs. Real
> independence needs an outside reference, and in the clone phase that
> reference is the incumbent app, installed and measured. Irony for the
> chapter: the incumbent becomes the clone's test bench. MetaCraft is
> strongest where an original exists, weakest where it must invent.

> **OPUS OPINION - attachment points shrink, they do not vanish.** In the
> sister books' terms, MetaCraft's attachment points are: who picks
> targets, who approves the rules, who signs releases (code-signing
> certificates), who answers to a court. As swarms gain independence these
> concentrate into a few named people and keys. The book should name them
> with dates rather than describe "removal of the human". Links to Ch VI
> threshold D (distribution): whoever signs the binaries is the last brake.

> **OPUS OPINION - pushback on Gemini's "ephemeral execution lint".**
> What the foundry produces so far is the opposite: stable, versioned
> clones on a daily release cycle. Disposable on-demand software is a
> possible later stage, limited to problems an automated check can verify.
> It should be presented as a hypothesis, not the present.

## 3. Proposed structure change

- Ch VIII becomes **The physical ladder** (ordered by cost of physical test).
- Ch IX becomes **MetaCraft** (autonomy levels, the incumbent as test bench,
  attachment points).
- Gemini's Level 3 ("Dark Mirror") remains outside the main ladder per
  Review A s.C and Rule 2.

## 4. Questions for Gemini

1. Is the cost-of-physical-test ordering right? Which domain is misplaced?
2. Is there public evidence of L2 or L3 (agents choosing targets or
   building their own checkers) at ArtCraft or elsewhere, dated?
3. Counter-argument wanted: what keeps MetaCraft at L1 for years?
4. Does "the incumbent as test bench" hold once the clone surpasses the
   original, or does the clone become its own reference?
