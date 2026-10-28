# Side: The Dark Mirror (governance only)

**Status:** Draft v0.1 2026-10-13 (Opus 5.5). Replaces Gemini draft s.V
Level 3. Governed by Rule 2 (`CONTRIBUTING.md`): institutional facts and
governance criteria only. No mechanisms, now or in later revisions.
**Revision date:** 2026-10-13.

## Why this file exists

The foundry is indifferent to its target. A method that clones a photo
editor can be pointed at contested domains. A book that ignored this
would be naive; a book that described how would be dangerous. This file
does neither. It names the domains, the institutions that govern them,
and the attachment points that apply.

## Three contested domains

| Domain | Main governing instruments | Attachment points |
|---|---|---|
| Offensive cyber capability | Wassenaar Arrangement controls on intrusion software (added 2013) `[construction]`; national computer-misuse law; model-provider usage policies | model providers, compute providers, code hosts |
| Weapons autonomy | US DoD Directive 3000.09 (updated 2023-01-25); UN CCW Group of Governmental Experts on lethal autonomous weapons; export controls | states, manufacturers, export authorities |
| Illicit commerce | anti-money-laundering and know-your-customer regimes (FATF standards); controlled-substance and precursor law | financial intermediaries, logistics carriers |

Weapons autonomy is the subject of the sister book `on-hyperwar`, which
owns that domain under its own hazard rule. This book defers to it.

## The 2026 shift: automated reverse engineering and scaffolding CVEs

Six months after the spring 2026 Mythos security demonstrations, the labor cost
of binary analysis and vulnerability discovery underwent the same collapse as
desktop application development:

1. **The Reverse Engineering Tsunami:** Tools automating Ghidra and IDA Pro
   via MCP bridges (the fleet's `reversing-mcp`, Rea.ai) synchronized white-box
   decompilation with behavior clickthroughs. Proprietary binary formats,
   legacy PE internals, and closed protocols no longer require months of human
   disassembly; agents extract functional specifications and feature-to-code
   maps in hours. Binary obscurity is no longer a moat.
2. **Scaffolding Under Continuous Audit:** Automated CVE discovery accelerated
   sharply against foundational software scaffolding. Runtimes historically
   defended by ubiquity (such as PHP interpreters) and low-level roots of
   trust (UEFI firmware) now face automated vulnerability synthesis faster than
   human security teams can write, test, and distribute patch advisories.

## The pattern

In each domain the binding constraint is the same as in Chapter VI:
not the code, but who will run it, host it, pay for it or carry its
outputs. The attachment points in this table are institutional: model
providers who refuse, compute providers who verify customers, banks and
carriers who report. The cost collapse of Chapter I lowers the price of
writing software. It does not lower the price of passing through these
points, and the book's position is that they are where governance effort
belongs.

## What this file will never contain

Techniques, architectures, component lists, target selection or any
detail that would help an operator rather than a principal. A proposed
edit that adds any of these is cut on sight.
