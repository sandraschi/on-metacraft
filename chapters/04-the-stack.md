# IV. The Stack

**Status:** Draft v0.1 2026-10-13 (Opus 5.5). Sources: Gemini draft s.II,
PhotoCraft README / AGENTS.md / ROADMAP.md (2026-10-11), Review B.
Gemini and Sandra review pending.
**Revision date:** 2026-10-18.

## The inversion

A desktop application used to be a window with a program behind it. The
window was the product; the program existed to serve the mouse. The
Crafting Apps invert this. The program is a document model and a list of
commands. The window is one of four ways to call those commands, and not
the most important one.

```
human intent / agent
        |
        v
  command registry  <---  UI (egui)  |  CLI  |  JSON channel  |  MCP server
        |
        v
  document model  ->  CPU reference compositor  <== compare ==>  GPU compositor
        |
        v
  files (PSD, PDF, DOCX, ...)  /  pixels  /  audio  /  drawings
```

## Everything is a command

PhotoCraft's contributor rules start with one sentence: everything is a
command. Every user-visible behavior is registered once in the engine,
with an id, a label, a menu path, a shortcut, documented parameters, an
enabled-check and a run function. The UI, the command line, the JSON
control channel and the MCP server all dispatch the same ids. At
2026-10-11 the registry held more than 500 commands.

The consequence is easy to miss. Agent control is not a feature added
after the fact. An app built this way cannot have a function the agent
cannot reach, because there is no other way to add a function. The Gemini
draft called MCP "the real nervous system". It is more exact to say there
is only one nervous system, and the human hand is one of its four inputs.

Goliath, 2026-10-18: Sandra reports CLI and MCP on the installed Crafts
are usable. That is an operator fact about this machine, not a benchmark.
Cursor's user `mcp.json` on Goliath does not register the Craft servers;
the control plane is the app's own CLI / JSON / MCP, as the READMEs
describe.

## Native, not wrapped

The apps are written in Rust only. The rules forbid JavaScript, webview
shells and Electron. The desktop build draws with egui on wgpu; the web
build is the same Rust compiled to WebAssembly. One codebase reaches
macOS, Windows, Linux and the browser; PhotoCraft also builds for FreeBSD.
FilmCraft alone had no web build at 2026-10-13.

The Gemini draft promised cold starts under twenty milliseconds and memory
in megabytes rather than gigabytes. That may be true; it is not yet
measured in public. `[construction: measure named app vs incumbent on
named hardware; PhotoCraft has a perf/ directory]`

## The oracle

This is the part the Gemini draft missed, and it is the part that makes
the rest possible.

PhotoCraft composites images twice. A CPU compositor, written for
clarity, is the reference. A GPU compositor, written for speed, is tested
against it. The PSD reader is tested against files authored in Photoshop
itself and kept in a separate, checksum-pinned corpus. Every command is
fuzzed with adversarial parameters by a test called `panic_hunt`; a crash
on bad input fails the build. A parity floor records how many incumbent
menu items are live and may only rise.

An oracle is anything that can say, cheaply and without a human, whether
the output is right. Agents can write code quickly. What they cannot do
without an oracle is know when they are wrong. Every part of this stack
that an agent touches has one.

Rule, stated once here and used for the rest of the book: **agent
synthesis scales exactly as far as cheap verification reaches.**

## The rules agents follow

The code rules read like a contract written for machines:

- No `unsafe` code anywhere but one isolated crate for pen-tablet input.
- No `unwrap`, `expect` or `panic` outside tests, enforced by the linter.
- No assumption of 8-bit color or sRGB in any public interface.
- No proprietary code, shaders, profiles or assets; implement from public
  specifications and observation.
- Every change comes with tests; every crash fix with a test that crashed
  before the fix.

Shared rules across all the Crafting Apps live in a private repository
called `craftrules`. Shared Rust libraries live in `craft-libs`, pinned by
revision.

## The budget

The PhotoCraft roadmap does something no software plan known to this
book has done before. It gives the distance to beta, 1,100 to 1,800
hours, in Opus 5.5 agent wall-clock hours for one agent working
sequentially, calibrated from 1,004 merged pull requests, and notes that
about 80 percent of the work parallelizes.

A project that budgets its future in model time has changed what a
software project is. Labor has become a line item priced in tokens.
Chapter VII is about who pays for them.

## Fleet link

on-ai-takeover: MCP as the interface that turns seat licenses into API
calls. The buyer's side of the same stack.
