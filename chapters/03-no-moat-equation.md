# III. No Moat Equation

**Status:** Draft v0.2 2026-10-18. Sources: Gemini draft s.I
(rebuilt), Review C, `mcp-central-docs/projects/adobe-offensive/14-legal-deep-dive.md`
(2026-10-11), Sandra on adhesive ToS 2026-10-18. Not legal advice.
**Revision date:** 2026-10-18.

## The wrong question

The Gemini draft called the incumbents' legal position a bluff: you cannot
copyright a Bezier curve. That is true and beside the point. Copyright
never protected the Bezier curve, the alpha-compositing formula or the
matrix multiply. Nobody believed it did. The law was not the moat.

The right question is why, if reimplementation was legal for forty years,
it was so rare.

## What the law always allowed

The doctrine is old and consistent.

- **Ideas are free.** 17 U.S.C. s.102(b) excludes any idea, procedure,
  process, system or method of operation from copyright. *Baker v. Selden*
  (1879) drew the line between a bookkeeping system and the book that
  explained it.
- **Menus are a method of operation.** *Lotus v. Borland* (1st Cir. 1995,
  affirmed by an equally divided Supreme Court in 1996) held the Lotus
  1-2-3 menu command hierarchy uncopyrightable.
- **Studying the original is allowed.** *Sega v. Accolade* (9th Cir. 1992)
  and *Sony v. Connectix* (9th Cir. 2000) held intermediate copying for
  the purpose of understanding unprotected elements to be fair use. Both
  defendants disassembled code. Watching a program run is milder.
- **Reimplementing an interface can be fair use.** *Google v. Oracle*
  (US Supreme Court, 2021-04-05) held Google's reuse of Java's declaring
  code fair use, weighing the investment programmers had made in learning
  the interface.
- **In Europe, observation is a right the license cannot remove.**
  Software Directive 2009/24/EC Art. 5(3) lets a licensee observe, study
  and test a program to determine its underlying ideas; Art. 8 voids
  contract terms to the contrary. *SAS Institute v. World Programming*
  (CJEU C-406/10, 2012-05-02): functionality, programming language and
  data file formats are not protected; a licensee who observed a learning
  edition to reproduce functionality acted lawfully.

The Phoenix BIOS clean room (1984) is the industrial template: one team
studies the original and writes a specification; a lawyer vets it; a
second team that never saw the original writes the code. The wall exists
to rebut an inference of copying. It is evidence, not a legal requirement.

## So why was it rare?

Because it was expensive. A clean-room Photoshop was always lawful and
always a decade of skilled labor. GIMP (1996), Krita, Inkscape and
LibreOffice show what volunteer labor could reach: capable programs that
deliberately did not imitate the incumbents' interfaces. They
reimplemented functions. They did not reimplement habits.

That is the moat this book is about. **Switching cost** is the time a
trained user loses moving to a program that works differently. For a
professional with ten thousand hours in Photoshop, it is the single
largest cost of leaving. Microsoft Office users did not stay away from
LibreOffice because LibreOffice could not open their files. They stayed
because their hands knew where things were.

*Google v. Oracle* is the doctrine for exactly this cost: the Court
weighed the investment users had made in learning an interface as a
reason reimplementation was fair. PhotoCraft's own pitch is the same
argument told for end users: the menus, shortcuts and panels your hands
already know. The legal theory and the product strategy are one sentence.

## What the clones change

The ArtCraft method (Chapter IV) attacks switching cost directly. Its
parity documents score each app against the installed incumbent, menu
item by menu item. At 2026-10-11 PhotoCraft reported every Photoshop menu
item present (628 of 628) and 56 of 68 tools. A faithful clone, accurate on
the surface and several levels down, makes the trained hand portable.

Agents made that affordable. Nothing in the law changed.

## What still binds

Four legal surfaces survive the clean room. They are thresholds, handed to
Chapter VI with owners and dates.

1. **Patents.** Independent creation is no defense. The surface is real
   but narrow and decaying: twenty-year terms, *Alice v. CLS Bank*
   (2014-06-19) against abstract software claims in the US, and the EPO's
   technical-character test, which since *T 208/84 Vicom* (1986-07-15) has
   treated image processing as technical. Live risk clusters in features
   newer than about 2006, and those are the features the clones lack.
2. **Trade dress.** Lanham Act s.43(a). The most likely first move by an
   incumbent is a letter about look, not code. The defense is that
   familiarity is functional; the cheap remedy is to restyle the chrome.
3. **Contract.** End-user license clauses against reverse engineering
   can bind a US licensee who clicked (*Bowers v. Baystate*, Fed. Cir.
   2003). In the EU, Art. 8 voids them as far as observation goes. They
   are not a moat against clean-room reimplementation. See below.
4. **Format licenses.** Mostly waived by the incumbents themselves to win
   ISO standardization: Adobe's royalty-free patent license for ISO
   32000-1:2008 (PDF 1.7), Microsoft's Open Specification Promise for
   OOXML (scope disputed by FSFE and SFLC in 2008). PDF 2.0 (ISO 32000-2,
   2017) and Adobe XFA sit outside the PDF license.

## Where the AI clean room is weaker than the label

Honesty requires two caveats.

- **The wall.** If one model context both watched the original and wrote
  the code, there is no wall in the Phoenix sense. Separate observer and
  implementer contexts with a vetted specification between them would
  rebuild it. Whether ArtCraft does this is not public.
  `[construction]`
- **The weights.** The model was trained on public material that includes
  tutorials, documentation and screenshots of the incumbent. Clean cannot
  be proven at the level of weights. The test remains the output: protected
  expression must be shown in the clone. Fresh Rust against decades-old C++
  is unlikely to show it.

As of 2026-10-18 no cease-and-desist, takedown or suit against the Crafting
Apps had been reported in press roundups `[construction: re-check github/dmca
and dockets at each revision]`.

## The ToS that is not a threshold

Adobe's terms, as discussed in October 2026 coverage, include language
forbidding monitoring or tracking an application's inputs and outputs
"in order to recreate that system." Counsel pieces treat this as a live
risk. This book does not.

A term that says "do not look at our product in order to compete" is
not a property right. It is a contract of adhesion trying to claw back
what copyright already excluded: ideas, procedures, methods of operation
(s.102(b)), observation of a running program (Sega, Connectix; Directive
Art. 5(3)), and, in Europe, a right the license cannot remove (Art. 8,
SAS). Sandra's position, dated 2026-10-18: the clause is arbitrary, based
on thin air, a no-hoper as a moat for Adobe or any other vendor. A letter
may still be sent. Distribution (Chapter VI, threshold D) may still pinch.
The term itself does not convert looking into infringement.

*Bowers* at most binds the person who clicked that EULA. It does not bind
a team that never took the license. It does not survive Art. 8. This
chapter therefore does not promote anti-clone ToS language to an
attachment point.

## Fleet link

on-hyperart Ch VII: copyright filters as a failed control case. There the
law tried to protect style and could not; here it never tried. The ToS
move is the same wish in contract clothes.
