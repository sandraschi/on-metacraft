# Side: The Reversing Foundry -- Inverse Engineering and the Leapfrog Craft

**Status:** Technical sidecar, dated 2026-10-28. Author: Sandra Schipal.
**Revision date:** 2026-10-28.

## The inverse engine

Forward engineering takes a human intent and compiles it into machine
instructions. For three decades, that was the only direction software
moved at scale. Reverse engineering was an artisan specialty -- an
expensive, slow, forensic excavation conducted by a tiny guild of assembly
wizards with hex editors and debuggers.

In 2026, the mechanization of programming (Chapter II) inverted that
balance. When an autonomous agent can generate, test, and refactor tens
of thousands of lines of systems code in seconds, reverse engineering
ceases to be a manual crawl. It becomes automated inverse compilation.

This sidecar documents the machinery of that shift: how agents deconstruct
closed binaries, the legal architecture of the two-tier clean room, why
byte-matching decompilation is an architectural trap, and how the method
scales from legacy desktop containers to hardware silicon and the games
industry.

## The two-tier architecture: scaffolding versus craft

The classic clean-room protocol, established by Phoenix Technologies in
1984 to clone the IBM PC BIOS, required two separate human teams separated
by a legal firewall:
1. Team One studied the proprietary original and wrote a functional
   specification.
2. A lawyer vetted the specification to ensure no copyrightable expression
   leaked through.
3. Team Two, who had never seen the original machine code, wrote the clone
   from the specification.

In the agentic foundry, that workflow is modernized into a two-tier
pipeline:

```
[ TIER 1: PRIVATE RESEARCH SCAFFOLDING ]      [ TIER 2: PUBLIC LEAPFROG CRAFT ]
• Lives locally on operator iron (Goliath)     • Pushed to public repositories (GitHub)
• Disassembled binary + Ghidra/ReVa database   • Pure Rust workspace (egui / wgpu)
• Reconstructed, fully-typed source code       • Zero matching bytes or assembly quirks
• Acts as the ground-truth ORACLE TEST BENCH   • Cross-platform: Linux, macOS, Windows, WASM
• NEVER PUBLISHED (zero legal surface area)    • Upgrades formats, UI, performance, and MCP
```

The reconstructed source code is not the product. It is an internal
Rosetta Stone. It exists only to answer one question for the test runner:
*Does the new, clean engine produce the exact same functional result as
the original binary?*

What reaches the public repository is a brand-new application. It shares
no code, no symbols, and no assembly layout with the incumbent. Under
forty years of statutory doctrine (*Baker v. Selden*, *Lotus v. Borland*,
*Google v. Oracle*, and EU Software Directive 2009/24/EC Art. 5(3)),
functional interoperability is non-infringing. The legal moat is bypassed
completely.

## The mechanics of agentic decompilation

An unstripped 32-bit or 64-bit binary presents a human analyst with a wall
of opaque labels: thousands of functions named `FUN_00401000` through
`FUN_0078a4b0`, interconnected by raw pointer arithmetic (`*(int *)(param_1 + 0x18)`).

An agent swarm resolves this through a three-stage topological pipeline:

### 1. Leaf-to-root call graph propagation
The agent sorts the application's call graph topologically and begins at
the leaf nodes -- functions that call no other routines.

Leaf functions are primarily standard C runtime helpers, math utilities,
or statically-linked third-party libraries. By matching compiler idioms,
string cross-references, and copyright banners, the agent identifies known
libraries (such as `zlib` or `libpng`). It renames the leaf functions and
applies strict parameter types via an MCP bridge (such as ReVa).

Once the leaf functions have typed names, meaning bubbles up the call tree.
When a parent function calls `fopen("Data/Text.dki")`, allocates a buffer,
and invokes `zlib_inflate`, its operational intent becomes mathematically
obvious. The agent renames the caller `dki_load_manifest` and documents its
contract. The meaning propagates upward like ink through water.

### 2. Struct and vtable synthesis
Human reverse engineers lose weeks tracking raw pointer offsets across
disassembly. An agent treats struct recovery as an inference constraint
problem:
* It queries every cross-reference where an object pointer is passed.
* It aggregates every accessed offset (`+0x00` vtable, `+0x04` file handle,
  `+0x08` volume name, `+0x24` uncompressed size).
* It defines a typed C or Rust struct representing the internal state.
* It pushes the struct definition into the disassembler's type manager.

Ghidra recalculates the decompilation on the fly. All raw pointer math
vanishes, replaced by clean field accessors.

### 3. On-the-fly tooling synthesis
The traditional defense of proprietary formats was file size: burying data
in a 100-gigabyte archive of proprietary chunks, encrypted headers, and
undocumented compression flags. To twenty human hobbyists in a forum,
sifting through that volume is an insurmountable exhaustion tax.

To an agent, scale is an illusion. The agent does not read the gigabytes
into its prompt context. It reads the first 4 KB and the trailing index
table, deduces the container format, and writes a dedicated, multi-threaded
decompression tool in Rust. It compiles the tool, runs it, observes where
a block offset misaligns, patches the source code, and re-executes.
The synthesized tool cuts through the archive at disk bus speed. Forward
code generation turns inverse extraction into routine plumbing.

## The matching-decompilation trap

In digital preservation communities, the holy grail is often "matching
decompilation" -- tweaking reconstructed C source until a legacy compiler
emits a binary that matches the original retail release down to the SHA-256
hash.

As a feat of archaeological forensics, matching decompilation is
magnificent. As an engineering and legal strategy, it is a double trap:

1. **The Legal Trap:** By reproducing the exact machine code of the original
   binary, the output replicates compiler artifacts, register allocation
   quirks, and dead-code sequences. An adversary can credibly argue that
   the output is a forensic reproduction of their protected creative
   expression.
2. **The Technical Trap:** Compiling to identical bytes preserves the
   corpse rather than liberating the software. A byte-exact match of a 1998
   application remains a 32-bit Win32 binary, tethered to obsolete GDI
   drawing calls, vulnerable to vintage buffer overflows, and dead on
   modern ARM64 mobile hardware and Linux workstations.

The leapfrog craft avoids the trap. It extracts the ground-truth
specification, discards the legacy scaffolding, and implements a modern,
memory-safe Rust architecture. It does not reproduce the 1998 binary; it
replaces it.

## The microcosm: two hours on Goliath

The efficiency of this pipeline is not theoretical. On 2026-10-26, on the
workstation Goliath, Sandra Schipal directed Claude Opus 5.5 through
`reversing-mcp`, ReVa, and Ghidra against `Digibib5.exe` -- the 32-bit
reader for Directmedia's Digitale Bibliothek, comprising 11,532 functions.

For twenty-five years, dozens of German literature CD-ROMs had remained
locked inside Directmedia's proprietary `.dki` and `.dka` containers.
Community efforts had stalled under the assumption of a bespoke licensing
cipher.

Within two hours, the agentic pipeline:
1. Checked library copyright banners and proved that the "bespoke codec"
   was standard statically-linked `zlib 1.1.2` and `libpng 1.0.4`.
2. Traced the manifest loader at `FUN_0061c6b0` and mapped the archive
   object vtable.
3. Wrote a self-healing Python/Rust extractor that unpacked the container
   volumes into clean XHTML and CSS.
4. Used ClickerLab to drive `Digibib5.exe` via CUA clickthrough, using the
   original running application as the behavioral oracle to verify the
   extracted text against the viewport.

A quarter-century of format lock-in dissolved in 120 minutes of wall-clock
time.

## The macrocosm: hardware and the games industry

The same pipeline that dissolved Digibib5's container format is now scaling
across two vastly larger industrial targets:

### 1. Hardware silicon and instrument cloning
As documented in the fleet's hardware analysis (`BEHRINGER_PLAYBOOK.md`),
Music Tribe (Behringer) transitioned from cloning discrete analog Curtis
silicon (V3340 VCOs) to extracting vintage digital ROMs (Roland JP-8000,
Prophet VS, Casio CZ Phase Distortion).

By using agent-native reversing bridges (such as REA) to decompile legacy
Motorola 56k DSP code and proprietary ASICs, the mathematical synthesis
engines are recompiled into clean C code targeting modern sub-\$1.50 ARM
Cortex-M and RISC-V microcontrollers. Coupled with Music Tribe City's
vertical injection molding and automated SMT lines in Zhongshan, vintage
four-figure instruments are reproduced as \$49 to \$99 consumer hardware.
The same economics make the \$3,000 dual-platter club DJ controller market
the next obvious target for sub-\$500 disruption.

### 2. Universal console liberation and static recompilation
The video game console industry relied on two moats: custom silicon and
binary opacity on optical or encrypted media.

As detailed in `MASS_RECOMP_AND_CONSOLE_LIBERATION.md`, static recompilation
(recomp) transliterates console binaries once at build time into native
C or Rust, targeting modern Vulkan, SDL, and Metal backends. When paired
with black-box 120 FPS behavioral oracles that extract kinematics and
geometry through pure screen observation, the walled garden collapses.
Every console exclusive becomes a portable, cross-platform open-source
engine accompanied by a user-supplied asset pack.

## Summary

The reversing revolution is the inevitable shadow cast by the coding
revolution. When software synthesis becomes effortless, software analysis
becomes instantaneous.

Binary obscurity, complex container archives, and proprietary instruction
sets no longer function as moats. The only software that remains defended
is software bound to a physical liability, an audited regulatory process,
or a live, verified network. Everything else can be read, understood, and
rebuilt between lunch and dinner.
