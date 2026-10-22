# Review C - The patent objection (Opus 5.5)

**Date:** 2026-10-13. **Reviewer:** Claude Opus 5.5. **Trigger:** Sandra's
rebuttal (2026-10-13): algorithms cannot be patented; patents expire; they
are circumvented or ignored when national interest is at stake (Bessemer);
rounded-corner design patents kept lawyers busy while Shenzhen ignored them.
**Not legal advice.**

## Verdict

Directionally right; the book should argue that patents are a **weak and
decaying** moat for the Crafting Apps. But three of the four supporting
claims are wrong or overstated as phrased, and a hostile reviewer will
attack the weakest one. Below: what holds, what to fix, and a stronger
version of the argument.

## 1. "Algorithms can't be patented" - partly true; wrong for images in Europe

- **US:** *Alice Corp. v. CLS Bank* (US S.Ct., 2014-06-19, unanimous):
  abstract ideas implemented on a generic computer are ineligible. That
  killed many software patents. But claims to a specific technical
  improvement survive (e.g. *Enfish v. Microsoft*, Fed. Cir. 2016
  `[construction: verify]`).
- **Europe:** EPC Art. 52(2)(c) and (3) exclude programs "as such", but the
  foundational case for patentable software is **T 208/84 Vicom**
  (EPO Board of Appeal, 1986-07-15): a method of *digitally processing
  images* was patentable, while the same method on a generic 2D data
  array was not. Image processing is the textbook *technical* domain.
- **So:** "algorithms can't be patented" is the wrong sentence for a book
  about Photoshop clones. Correct sentence: *the math is free; specific
  technical applications of it can be claimed, and image processing is
  exactly where that has been allowed longest.*

## 2. "Patents have a sell-by date" - true, and the strongest point

- Term is 20 years from filing (TRIPS Art. 33). Photoshop 1.0 shipped
  1990-02; the layers, masks, blend modes and adjustment layers a clone
  needs most date from 1990-2005 and are long expired.
- Recent features (Content-Aware Fill ca. 2010, AI features from 2023)
  are where live claims cluster. ArtCraft's own parity docs say PhotoCraft
  lacks AI features. **Being behind is a patent shield**: the parity gap
  falls largely on the features most likely still protected.
  `[construction: map PhotoCraft gaps vs. Adobe patent filing dates]`
- Bessemer itself shows expiry at work: Mushet's 1856 spiegeleisen patent
  lapsed and Bessemer incorporated the step from 1859.

## 3. "Bessemer: the whole world ignored the patents" - wrong as stated

- Bessemer licensed his process and is estimated to have earned **over
  GBP 1 million in royalties** before the patent expired (1870). In the US,
  Kelly's rival patent was bought and pooled with Bessemer's under one
  licensing scheme; mills took licenses under both "to keep out of
  trouble". The Bessemer story is a patent *success*, not a case of the
  world ignoring patents. Using it invites an easy rebuttal.
- **Better historical cases for "nations ignore patents when it pays":**
  - Netherlands abolished its patent law 1869-1912; Switzerland had none
    until 1888 (chemicals only from 1907) and built a chemical and
    pharmaceutical industry partly on copying German inventions.
  - The US ignored foreign copyright until the Chace Act (1891); British
    authors were reprinted without royalties.
  - Wright brothers patents: the US government forced the 1917
    Manufacturers Aircraft Association patent pool at war entry. This is
    the **national-interest override** in its cleanest form.
  - Today it is codified: compulsory licensing (TRIPS Art. 31, Doha
    Declaration 2001) and US government use (28 U.S.C. s.1498).
  `[construction: verify all dates before manuscript]`

## 4. "Rounded corners ... Shenzhen ignores the lot" - half-right, half-dated

- These were **design patents** (Apple D618,677, D593,087, etc.), not
  utility "micropatents". *Apple v. Samsung*: 2012 jury verdict ~USD 1.05 bn;
  *Samsung v. Apple* (US S.Ct., 2016-12-06) narrowed damages to the
  "article of manufacture"; settled 2018. Point stands: years of lawyers,
  over a shape the market had already copied.
  `[construction: verify patent numbers and figures]`
- "Shenzhen ignores the lot" was true of shanzhai phones ca. 2005-2012. It
  is outdated in 2026: China has been the world's largest patent filer for
  years and Huawei has led WIPO PCT filings for years. Shenzhen companies
  now *assert* patents. The modern point is the reverse and more useful:
  **patents became a weapon between giants, not a barrier to small entrants.**
  `[construction: cite current WIPO PCT ranking]`

## 5. The argument the book should actually make

The patent threat to ArtCraft is real but narrow and getting narrower:

1. **The incumbents waived the format patents themselves.** Adobe's Public
   Patent License grants royalty-free use of essential claims for ISO
   32000-1:2008 (PDF 1.7); Microsoft's Open Specification Promise covers
   OOXML (ISO/IEC 29500), though FSFE and SFLC disputed its scope (2008).
   To win ISO standardization, they gave away the file-format moat. Caveat:
   PDF 2.0 (ISO 32000-2, 2017) is outside Adobe's license; XFA remains
   proprietary.
2. **Expiry favors the clone.** The core of every incumbent app is older
   than 20 years.
3. **Damages track revenue.** A free MIT/Apache project with no sales
   offers little to win in damages; the realistic remedy is an injunction
   against a named, US-reachable lead developer and the distribution
   channel (GitHub, app stores, code signing). The pressure point is
   distribution, not the code. Cross-reference Ch VI threshold D.
4. **Assertion is expensive in reputation.** Suing a 50k-star open-source
   project over a feature the incumbent charges a subscription for is a
   public-relations cost. Not a legal argument; an economic one.
5. **Jurisdiction arbitrage is real but rarely needed.** Code on GitHub
   is mirrored worldwide; patents are territorial.

Honest residual risk: method claims on post-2006 features, especially
AI-assisted editing, and anything that copies a specific patented
pipeline rather than reaching the result independently. Chapter III
should name this risk, not deny it.

## 6. Placement

- Ch III (No moat equation): sections 1, 2, 5.1.
- Ch II (Mechanizers): Netherlands / Switzerland / Wright pool as the
  "guilds lose; law bends" pattern. Use Bessemer as the counter-case
  (the inventor who *did* get paid), which strengthens the chapter.
- Ch VI (Thresholds): A (patents) downgraded to "partial, decaying";
  D (distribution) upgraded as the real enforcement chokepoint.
