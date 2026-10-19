# I. The Breach

**Status:** Draft v0.2 2026-10-18. Sources: GitHub API on the
`storytold` org, PhotoCraft README / AGENTS.md / ROADMAP.md, press
2026-10-07..18, Goliath install check 2026-10-18,
`mcp-central-docs/projects/adobe-offensive/01` (2026-10-08).
**Revision date:** 2026-10-18.

## Thirteen days

On 2026-09-30 a developer named Brandon Thomas made the first commit to a
repository called `storytold/photocraft`: an image editor, written in Rust
from scratch, described as a clean-room reimplementation of Adobe
Photoshop. Four more repositories were created the same day: VectorCraft
for Illustrator, FilmCraft for Premiere, LightCraft for Lightroom,
PdfCraft for Acrobat. EffectCraft and DesignCraft, for After Effects and
InDesign, followed the next day. All seven shipped their first releases on
2026-10-02. The suite went public at getartcraft.com/apps over the
weekend of 2026-10-04 `[construction: confirm site launch date]`.

On 2026-10-07 Ars Technica ran the story under the headline "Software is
over". The same day, five more repositories appeared: WordCraft,
GridCraft and DeckCraft for Microsoft Word, Excel and PowerPoint;
SoundCraft for Avid Pro Tools; CADCraft for Autodesk AutoCAD. FigCraft,
for Figma, followed on 2026-10-09.

By 2026-10-12 the thirteen apps had published 93 releases between them,
about one release per app per day. PhotoCraft had 55,197 GitHub stars
in the 2026-10-13 snapshot. The 2026-10-18 snapshot (`evidence/2026-10-18.json`):
67,027 stars, 12 releases, latest tag v0.10.0; suite-wide 120 releases and
167,586 stars. Inflow cooled after an Oct 7-12 spike. Stars are weather.
Chapter V holds the living count. PhotoCraft is dual-licensed MIT or Apache-2.0.
The generative studio is a separate product, `storytold/artcraft`, not
one of the thirteen.

Its commit log since 2026-09-30 held 1,511 commits and about 1,579
`Co-Authored-By: Claude` lines as of 2026-10-13: nearly every change had
an agent as co-author. `[construction: re-count Co-Authored-By at next
evidence run]`

## Not a lone genius, not a corporation

The Gemini draft described the origin as a single experienced developer.
That is half the picture. Thomas leads; press reports describe fifteen
years of programming and about three years as chief executive of the AI
start-up Storyteller.ai `[construction: verify; funding history open]`.
He has said he worked exclusively with AI coding tools from early 2026 and
settled on Claude Opus 5.5 `[construction: primary source]`. The commit
log shows the rest: parallel agent instances writing most of the code,
and, within days of launch, a crowd of human contributors. 227 distinct
names had committed to PhotoCraft by 2026-10-11.

The correct unit is neither a person nor a company. It is a lead, a
method and a swarm.

## What was claimed, what was shipped

The founder's claims ran ahead of the software. Early posts spoke of
reaching full parity with Adobe within a month; he later revised this to
months rather than years `[construction: HN thread ids in
adobe-offensive/01]`. Reviewers found the apps glitchy, incomplete and
early. The project itself agrees: PhotoCraft's own roadmap, reviewed
2026-10-11, rates it about 45 percent ready for real work, with feature
breadth near 76 percent.

Counting bugs on day thirteen measures the wrong thing. Discovery is
being done for free by thousands of users filing issues; fixing is being
done in parallel by agents; every fix lands in a shared Rust core used by
all thirteen apps. The number to watch is not the bug count but the slope
of the parity curve.

## The number that matters

The PhotoCraft roadmap contains one line that should open every history
of this period. It estimates the remaining distance to beta at 1,100 to
1,800 hours, measured in Opus 5.5 agent wall-clock hours for one agent
working sequentially, calibrated from the repository's own 1,004 merged
pull requests, and notes that about 80 percent of the work parallelizes.

Adobe's Photoshop organization measures its work in engineers and years
`[construction: dated headcount source]`. PhotoCraft measures its
remaining work in model time. That difference is the breach.

## What the moat was

The Gemini draft opened with a sentence worth keeping: the moats were
never laws of physics. They were the cost of human keystrokes. Chapter III
shows the law never protected what the clones copy. Chapter IV shows how
the method works. This chapter only fixes the date: between 2026-09-30
and 2026-10-12, the labor cost of reimplementing professional desktop
software stopped being the barrier it had been for forty years.

## Fleet link

on-ai-takeover: the per-seat subscription line item, seen from the buyer's
budget, that this chapter makes optional. on-hyperart: the Crafts are how
a generated picture becomes a PSD, AI, or PREL a client can still open.
on-hyperwar: dual-use consumer stack versus exquisite incumbent; analogical
only, no munitions software.
