# VII. Dark Megawatts

**Status:** Draft v0.1 2026-10-13 (Opus 5.5). Source: Gemini draft s.III,
revised per Review A. Gemini and Sandra review pending.
**Revision date:** 2026-10-13.

## Who pays for the agent-hours

Chapter IV ended with a budget in agent-hours. Somebody pays for them.
The Gemini draft's answer is the most interesting economic claim in its
text: the datacenter buildout of the mid-2020s, whatever it does to its
investors, will leave behind cheap compute the way the telecom crash left
behind cheap fiber.

The claim is half right. This chapter keeps the right half and dates the
wrong one.

## The fiber precedent

Between 1996 and 2001, carriers laid far more fiber than the traffic of
the day required. When the bubble burst, much of it went unlit `[construction:
share of US long-haul fiber unlit ca. 2002, dated source]`. Bankrupt
carriers sold their networks for a fraction of what they cost. The buyers
lit the fiber cheaply over the following decade, and the web of video,
cloud and mobile data ran on capacity that someone else had already
written off.

The mechanism is general: capital that is destroyed on the balance sheet
is not destroyed in the world. A written-off asset that still works has
near-zero capital cost to its next owner.

## The right half

A GPU written down to zero on an accountant's schedule still computes.
Depreciation is an accounting convention; it is not a physical clock. When
a newer generation arrives, older racks that are fully paid for do not
vanish. Their owners can sell their time cheaply, and for work that does
not need the lowest latency, such as batch code synthesis, test runs and
fuzzing, they are good enough.

That is precisely the workload of Chapter IV. The agent swarms that build
the Crafting Apps do not need to answer a user in two hundred
milliseconds. They need many hours of patient compute, and they can wait
for it overnight.

## The wrong half

The Gemini draft claimed silicon does not rot. Two facts disagree.

1. **Failure at scale.** Meta's Llama 3 report (2024-07) recorded hundreds
   of unexpected interruptions during a 54-day training run on about
   16,000 H100 GPUs, a majority attributed to GPU and memory faults
   `[construction: verify exact figures]`. Large GPU fleets fail
   continuously. Old fleets fail more.
2. **Electricity is not amortized.** A fully written-off accelerator still
   pays full price for every joule. When a newer chip produces several
   times more tokens per joule, the old rack loses on running cost alone,
   long before it breaks. Fiber was different: the glass got more
   valuable when better lasers were fitted at each end. A GPU cannot be
   upgraded at the ends. Its useful life is set by the efficiency of its
   successors.

So the dark-fiber analogy holds for years, not decades. `[construction:
tokens per joule by generation, A100 / H100 / current, at a stated power
price]`

## What reaches the clone-builders

The subsidy only matters if it reaches the people running the swarms.
That depends on who owns the stranded racks (hyperscalers, specialist
cloud providers, lenders who repossess them) and whether spot prices for
older hardware actually fall. The evidence to collect is a dated series
of spot prices for previous-generation accelerators and of API token
prices for the models used to write code `[construction]`.

There is a second subsidy the Gemini draft did not name: the model
providers' own price competition. When frontier labs cut token prices to
win developers, the cost of an agent-hour falls whether or not any
datacenter goes dark.

## The honest word

The Gemini draft's subtitle promised a zero-cost frontier. The PhotoCraft
roadmap refutes it: 1,100 to 1,800 agent-hours to beta is not zero.
The correct claim is that the **marginal cost of replication** is near zero
and the **cost of synthesis** is falling fast. The chart this chapter
needs is agent-hours to parity multiplied by the price of an hour, plotted
over time. That curve, not the word zero, is the argument.

## Fleet link

on-ai-takeover: the capital cycle from the investor's side. on-hyperwar:
compute as a strategic stockpile.
