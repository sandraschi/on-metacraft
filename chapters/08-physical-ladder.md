# VIII. The Physical Ladder

**Status:** Draft v0.2 2026-10-25. Source: Gemini draft s.V (Level 2), restructured per Review E, expanded with tacit craft and electrochemical rungs from October 2026 sessions.
**Revision date:** 2026-10-25.

## Software that makes things

Most professional software outside the office does not produce documents.
It produces instructions for a machine: where a needle goes, which needle
on a knitting bed lifts, where a blade cuts, how a tool head moves. The
design program sits between a person and a machine, and it is often the
most expensive and most locked part of the chain.

That makes it the next target. The method of Chapter IV does not care
whether the output is a PSD file or a stitch file. It needs a spec, an
original to compare against, and a cheap way to check the result.

## The ordering rule

Chapter IV stated the rule: agent synthesis scales as far as cheap
verification reaches. On a screen, verification is a pixel comparison.
Off the screen, it is a physical test, and physical tests have prices.
The ladder is ordered by them.

| Rung | Domain | Physical check | Cost per check |
|---|---|---|---|
| 1 | Machine embroidery, home cutting | stitch-out or cut on scrap | cents, minutes, at a kitchen table |
| 2 | Machine knitting | a swatch | small |
| 3 | Electrochemical and spark machining (ECM/EDM) | bore or cut on scrap stock | dollars, minutes to hours |
| 4 | Garment pattern and fit | bodies vary, cloth drapes | medium; needs people |
| 5 | Kinematic assembly and tacit mechanics | 3D-printed jig or test rig | tens of dollars, camera-in-the-loop |
| 6 | Agriculture | a growing season | a year |
| 7 | Chips | a tape-out | millions |

## Rung 1: needle and blade

Machine embroidery runs on stitch files (DST, PES, EXP and others)
produced by digitizing software: Wilcom, Hatch, Brother PE-Design and
others `[construction: current prices and licensing models]`. Home
cutting machines run on design apps such as Cricut Design Space, which
ties the software to the machine and to a subscription.

The formats are largely documented or long since reverse-engineered by
open-source projects `[construction: name and date the main open
libraries]`. The hard knowledge is physical: how much a stitch pulls the
fabric, how density changes on stretch materials, how underlay holds a
satin column. That knowledge is learned by stitching out samples. A
sample costs a scrap of cloth and a few minutes. An agent with a camera
and a machine can run that loop all night.

Rung 1 is therefore not a distant future. It is plausibly the next step
after office software.

## Rung 2: the knitting bed

Industrial knitting machines (Shima Seiki, Stoll) are programmed through
their makers' design systems `[construction: SDS-ONE APEX, M1plus,
licensing]`. A program is a grid of needle actions. A swatch checks it.
The loop is slower than embroidery and the machines are expensive, but
the check is still small and local.

## Rung 3: the bath and the arc

Subtractive metal machining usually demands heavy, stiff machine tools.
Cutting forces deflect cutters, chatter ruins tolerances, and a rigid
three-axis milling center costs tens of thousands of dollars. That capital
requirement kept subtractive software protected behind commercial CAM licenses
(Mastercam, Siemens NX, PowerMill).

Electrochemical machining (ECM) and electrical discharge machining (EDM)
invert that requirement. Metal dissolves atom by atom into an electrolyte
bath, or erodes across a dielectric spark gap. There is no contact force,
no cutter deflection, and no chatter. A 3D-printed tool head carrying a copper
or 3D-printed conductive cathode in a salt bath cuts hardened alloys that
would destroy carbide end mills.

The barrier in ECM has always been the software: calculating cathode shape
compensation for electric field gradients and electrolyte fluid flow.
Historically, that math stayed inside specialized aerospace turbine
programs. An agent harness running an open-source finite-element field solver
can iterate cathode geometry against test coupons. The physical check is a
saline wash over a scrap of hydraulic tubing, powered by a bench supply.
The test costs two dollars in electricity and salt, takes forty minutes,
and yields a clean micrometric cross-section.

## Rung 4: the garment

Pattern-making software (Gerber AccuMark, Lectra Modaris, Optitex) and
3D garment simulation (CLO3D, Browzwear) turn bodies and cloth into flat
pieces. Here the check gets expensive: fit depends on bodies, and bodies
vary. The simulation is an oracle only as far as it is trusted, and
fashion houses still sew samples. Rung 4 falls more slowly, and falls
first where the body is standardized: uniforms, workwear, sizes from
published tables.

## Rung 5: tacit craft as compiler target

Human history is filled with lost crafts: techniques that vanished because
their knowledge was tacit rather than codified. Historical metallurgical
treatments, manual lathe-bed scraping to sub-micron flatness, precision
watch escapement geometry, and the complex kinematic motions recorded in
Renaissance combat treatises (such as the 15th-century Fechtbuecher) were
transmitted by demonstration and muscle memory. When the guilds died, the
craft died.

An agent harness approaches a lost craft differently. It treats historical
texts, patents, and workshop notebooks as an informal specification. The
agent compiles that specification into a parametric mechanical model in
FreeCAD, exports the scene into an OpenUSD stage, and subjects the physics
to a rigid-body simulator (MuJoCo or Isaac Lab).

The physical check on Rung 5 uses 3D-printed test fixtures, standard
stepper actuators, and an inexpensive USB vision camera. The agent closes
the loop between simulated kinematics and observed physical motion. Where
a human apprentice required seven years under a master to acquire muscle
memory, an agent harness with a camera evaluates fifty motion cycles an
hour. The physical constraint is not human intuition; it is the wear rate
of the actuator gears.

## Rung 6: the field

The Gemini draft's SoilCraft (hydrology and soil models compiled to
guidance tracks and irrigation schedules) meets a check measured in
seasons. Worse for the clone, the moat in agriculture is not the
planning software. It is the machine's firmware and the right to repair
it. That fight is being fought in regulators and courts, not in code
`[construction: FTC action against Deere, 2025, status]`.

## Rung 7: the chip

Chip-design tools are the most expensive case, covered in Review D. The
check is a foundry run that costs millions and the tools only count once a
foundry certifies them. Lawyers do not protect this rung. Physics and
the foundry do.

## Where the moat goes

When the design software is free, lock-in moves to the machine maker:
proprietary formats, cloud-required apps, encrypted firmware, warranty
terms. Agriculture shows the pattern first. Expect embroidery and
cutting machines next, and expect right-to-repair arguments to follow
them from the farm to the sewing room.

## The hand again

There is a cultural inversion in this chapter that the Gemini draft did
not see. For thirty years, the expensive part of a craft hobby or a small
textile business was often the software license. When the license is
free, the scarce part is the human: the eye for cloth, the hand on the
hoop, the judgment about drape. The tools return to the edge, and the
skill becomes the thing worth having again.

## Fleet link

on-hyperart: folk-art demotion under aesthetic abundance. Here the same
abundance runs the other way: it frees the hand rather than replacing it.
