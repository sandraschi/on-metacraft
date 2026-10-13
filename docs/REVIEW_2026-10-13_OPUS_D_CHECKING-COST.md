# Review D - Checking cost, lawyers, defection (Opus 5.5)

**Date:** 2026-10-13. **Reviewer:** Claude Opus 5.5. **Trigger:** Sandra,
2026-10-13: "twenty apps lined up" was a figure of speech and undersells
it (200 or 2,000); Reddit asked for an AutoCAD clone and it arrived; can
lawyers stop the storm of the Bastille; Office users stayed for muscle
memory; a PRC EDA clone; WindowsCraft; Linux desktop never came.
**Closes:** the "twenty more" open item (figure of speech, not a claim).

## 1. Ceiling vs order

Agreed: there is no fixed ceiling on how many apps get cloned. The book's
claim becomes: **the number of targets is unbounded; the cost of checking
a clone against the original decides the order.**

| Checking cost | Examples | Why |
|---|---|---|
| Cheap (first) | Photoshop, Illustrator, Word, Excel, PowerPoint, Acrobat | published formats, observable behavior, pixel/byte-exact outputs |
| Medium | AutoCAD (DWG history: undocumented, reverse-engineered by the Open Design Alliance), Pro Tools, After Effects | partly undocumented formats, plugin ecosystems |
| Expensive (last) | QuickBooks, Cadence/Synopsys, Windows | network, liability, certification, or physical tests |

- **QuickBooks:** the moat is bank feeds, payroll tax filing, the
  accountant network and audit liability, not the UI. A faithful clone
  gets the software, not the network. `[construction]`
- **EDA (Cadence/Synopsys):** foundry certification and tape-out (each
  physical test costs millions) are the checkers. US EDA export
  restrictions to China in 2025 are the motive for a domestic clone;
  Chinese EDA vendors exist but advanced nodes still depend on incumbents.
  Lawyers do not bind a PRC entity; the foundry does. `[construction:
  dates of 2025 BIS EDA restriction and lifting]`
- **Windows:** see s.4.

## 2. Can the lawyers stop the storm?

Precedent: law stops the named defendant, not the practice.
- Napster: shut down 2001 after *A&M Records v. Napster*. File sharing
  continued; the industry's income recovered through catalog licensing +
  a service (Spotify), i.e. it moved to where a moat still worked.
- Expected incumbent move: from the app to the bundle. Microsoft 365's
  enterprise lock-in is Exchange, Teams, identity, compliance, SharePoint
  tenants, not the ribbon. Adobe's: Firefly, stock, cloud libraries,
  enterprise licensing.
- Consequence: individuals and small businesses can defect fast;
  enterprises defect when the bundle, not the app, is cloned.

## 3. Defection is a muscle-memory problem (agreed), with dated cases

- Munich LiMux: Linux + LibreOffice from 2004, reversed 2017. Dated
  failed defection. `[construction: council decision dates]`
- Counter-trend, digital sovereignty: Schleswig-Holstein, a Danish
  ministry, Austrian Bundesheer reported moving to LibreOffice.
  `[construction: unverified, verify each]`
- Thesis: sovereignty supplies the motive LibreOffice always had;
  a faithful clone (surface + three levels deep) removes the
  retraining cost LibreOffice never removed. Candidate chapter.

## 4. WindowsCraft and the Linux desktop

- Prior art: ReactOS (since 1998), Wine (since 1993). The hard part is
  compatibility with decades of binaries and drivers, not the look.
- Best evidence for "three levels deep beats familiarity": Proton on
  the Steam Deck (2022). Linux gaming grew through a compatibility layer.
  Windows-skinned distros (Zorin and others) did not move the needle.
- Agent angle: Wine's conformance tests are a ready-made checker.
  Drivers stay the physical moat.
- Hook for Ch VIII/IX: the year of the Linux desktop never came; the
  year of the Windows clone might.

## 5. CAD anecdote - verify order of events

GitHub API: `storytold/cadcraft` created 2026-10-07, first release
2026-10-08. If the Reddit request is ~2026-10-10, the clone **preceded**
the demand. Need thread URL + date before the anecdote enters the text.
Either version is usable; only one is true.

## 6. Investment framing (book, not advice)

The book should not say "sell all app makers". Ch VI split: vendors whose
moat is the app (UI, formats, features) are exposed; vendors whose moat
is a network, data, liability or certification much less so.
