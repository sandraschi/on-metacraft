# Side: Two Hours of Digibib5

**Status:** Narrative note, dated 2026-10-28. Author: Sandra Schipal.
**Revision date:** 2026-10-28.

## The twenty-year vault

For a quarter of a century, the Digitale Bibliothek series (Directmedia
Publishing, Berlin) sat on German bookshelves: dozens of CD-ROM volumes
holding thousands of works of classic literature, philosophical treatises,
and historical lexicons.

The text was locked inside two proprietary container extensions: `.dki`
(the compressed content volumes) and `.dka` (the allocation and offset
tables). Generations of German humanities students and open-source hobbyists
wrote forum posts asking how to get their Goethe and Kant out of the
Directmedia viewer and into plain text or Calibre. A few partial Python
scripts circulated on SourceForge and GitHub, half-working, brittle, and
abandoned. The consensus was that Directmedia had engineered a bespoke,
Byzantine licensing container with custom bit-plane encryption.

On 2026-10-26, on Goliath, we set out to extract it.

## The session

The operator was Sandra Schipal. The agent was Claude Opus 5.5, connected
via MCP to `reversing-mcp`, the ReVa interactive bridge, and a headless
Ghidra instance analyzing `Digibib5.exe` (a 32-bit PE binary with 11,532
functions).

The initial pass fell into the classic human trap. Opus followed the error
string "Decompression error" down an xref chain into three dense functions
(`FUN_00514dd0`, `FUN_00521234`, `FUN_00522294`) and began drafting notes on
a "bespoke DKI bit-plane codec".

Then the agent did what no tired human does: it stepped back and checked the
library banners.

Buried in the disassembly were copyright strings for `zlib 1.1.2` and
`libpng 1.0.4`. The three "bespoke" functions were not a secret Directmedia
invention; they were Adam7 interlaced row-pass routines from stock libpng.
The binary had statically linked open-source compression thirty years ago
and wrapped it in a custom header table.

Once the false mystique cleared, the task stopped being cryptography and
became plumbing:

1. **Vtable tracing.** Opus traced `FUN_0061c6b0`, the manifest loader,
   identified the archive object vtable, and mapped the registration loop
   for `text.dki`, `tree.dki`, and `tree.dka`.
2. **On-the-fly tool synthesis.** The agent wrote an ad-hoc decoder script in
   Python, executed it against the CD-ROM images, hit an offset mismatch on
   the block boundary, read the error output, patched the offset logic, and
   ran it again.
3. **The behavioral oracle.** To verify that the extracted XHTML and CSS
   matched reality, `reversing-mcp` launched `Digibib5.exe` under ClickerLab,
   navigated the original UI, and captured window buffers to verify text and
   markup rendering against the original viewport.

From the first Ghidra import to a clean, working extractor dumping full
libraries of XHTML text, the clock ran for **two hours**.

## The moral

The story is funny because of the contrast. Twenty years of assumed
impenetrability dissolved over a single cup of coffee.

The serious point is the one Chapter IV makes: binary obscurity was never
a technical moat. It was a tax on human patience. When an agent can read
eleven thousand functions, spot the static library signatures, write a
throwaway unpacker, compile it, fail, patch it, and verify the output
against the running program in 120 minutes, proprietary container formats
cease to exist as an obstacle.
