# Verify Podcast Script — 2026-08-20

> ## ⟶ CURRENT VERDICT (fix pass v2, re-verified 2026-08-21): **WARN — audio UNLOCKED, held for principal approval**
>
> All six v1 blockers cleared, both S1 mismatches fixed, the missing unit removed with its sentence.
> **L1 16 → 2 · L2 1 → 0 · L3 1 → 0 · L4 2 → 0 · S1 2 → 0.** Zero FAIL triggers remain.
> WARN rather than PASS because the fix pass bought its words by cutting three signposts, one of which
> carried a load-bearing comparison. All seven WARNs are optional. **Full v2 pass at the end of this file.**
>
> The v1 record below is retained unedited, as the audit trail.

---

# v1 — first pass (FAIL)

**Verdict:** **FAIL** — 6 blockers, all single-sentence fixes. Script edited and re-verified before TTS.
**Checks (counts = FLAG hits):** L1 **16** / L2 **1** / L3 **1** / L4 **2** / L5 **0** / L6 **0** / S1 **2**
**Blockers:** B1 unsupported "nobody has" · B2 desk shorthand "killed three stories" · B3 the word "either" · B4 the oil cause · B5 "next financial year" (S1) · B6 the fifty two percent comparator (S1)
**Guard scan:** PASS — no tips, no buy/sell/hold, no targets, no portfolio language, no recommendation.
**Audio mechanics:** PASS — 700 words, zero digits, zero symbols, zero em-dashes, longest sentence 29 words unnested.
**Reviewed:** script.md (59 sentences, all ledgered) vs canonical exemplar; brief opened last, for S1 only.

## Method / isolation

Read order was held: exemplar → script → full per-sentence ledger → **only then** the brief, for S1 only.
The ledger below was written with the day's facts withheld. Every judgment in it is a listener's
judgment on one hearing, with no outside context available to repair a sentence.

Mechanical L5/L6 pass was run on the spoken body (below the metadata separator) before the brief was
opened, since it cannot contaminate a naive read:

- Words: **700** (band ~500-700 — at the ceiling, inside it; header claims 699, a tokenizer difference, not a defect)
- Digits: **zero**. Currency/percent symbols: **zero**. Em/en dashes: **zero**. `[SAY:]` hints: **zero**. Exclamations: **zero**.
- Hyphens: two, both benign — `toro I-Q` (deliberate brand respell) and `SEBI-registered` (verbatim firebreak).
- Semicolons: only inside the verbatim firebreak, exactly as the exemplar.
- Longest sentence: **29 words**, single-thread and comma-segmented. Nothing nested. **No L6 hits.**

## Per-sentence ledger

Every sentence of the spoken body, in order. 59 sentences.

**Open**

1. "Good evening." — FLAG (L3-minor: see the deviation-consistency section. The script drops "today" on the stated ground that it would be false at the moment of listening; "Good evening" is false in exactly the same way on a Friday-daytime publish. Not a fact error; an internal inconsistency in the deviation's own logic.)
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on Thursday's session." — OK (day-name deviation, executed correctly)

**Lede**

4. "The Nifty rose on Thursday, ending a seven session losing run." — OK. Clean, concrete, stands alone.
5. "But the reason was not made in India." — OK
6. "It was made in Washington, and India got the smallest share of it." — FLAG (L1: the pronoun changes referent mid-sentence. The first "it" is *the reason* (carried from sentence 5); the second "it" has to be *the rise*, which has not been named as a noun a pronoun can grab. Heard aloud, the literal reading is "India got the smallest share of the reason", which is not a thing. On the page the headline supplies "the rise"; in audio nothing does.)

**The close**

7. "Here is where the market closed." — OK
8. "The Nifty fifty finished at twenty four thousand two hundred and thirty one, up zero point six four percent." — OK
9. "About three and a half shares rose for every one that fell, on a count taken during the session." — FLAG (L1-minor: "on a count taken during the session" is a precision hedge with no listener payoff — a naive listener cannot do anything with it and will stall on why it was said. The ratio itself is fine.)

**Asia / oil**

10. "Asia rallied and India rallied least." — OK
11. "Korea's Kospi gained roughly five and a half to six percent, and Japan and Hong Kong each rose a little over one percent." — OK (Kospi is placed by "Korea's"; the range is honestly hedged)
12. "India came last because Brent crude rose for a fifth straight session, to ninety three dollars and eighty seven cents a barrel." — **FLAG (L4 + L1: the highest-value clarity finding in the script.)** Two separate problems. (a) *Confidence:* "because" states a bare causal fact. This is the script's one inferred cause and the language does not mark it as inference. (b) *Mechanism missing:* the chain is never spoken. Why does dearer crude hurt India specifically? Because India imports nearly all its oil. That clause is absent — and without it the logic does not even close for a listener, because **Japan and Korea, which the script just said rallied harder, are also large oil importers.** A listener who is paying attention hears a reason that contradicts the sentence before it. The exemplar never does this: its oil beat spells out "an oil importer like India" explicitly.
13. "The Strait of Hormuz, which carries much of the world's oil, has been shut since February." — OK (glossed in-line, exemplar-standard)
14. "The rally came from Washington." — OK
15. "The brake came from Hormuz." — OK (a metaphor, but a dead one, and it lands immediately after the literal mechanism; L4 tolerates this)

**Washington / the buyback**

16. "So, Washington." — OK
17. "On Wednesday the American Treasury said it will at least double its buybacks of long dated government bonds, from two billion dollars an operation to at least four billion." — OK (29 words, single-thread. "Buyback" is used before it is glossed, but the gloss arrives two sentences later inside the same beat, which is a deliberate and defensible structure.)
18. "American long term yields fell the same session." — FLAG (L1: **"yields" is never glossed anywhere in the script.** It is the pivot word of the entire Washington beat. The exemplar glosses far easier terms than this.)
19. "The ten year fell five point seven basis points, to four point six four seven percent." — FLAG (L1: three distinct problems in one short sentence. "The ten year" — ten-year *what*? The listener must construct "ten-year government bond yield" unaided. "Basis points" is unglossed jargon; the composition note claims the level self-glosses it, but hearing "five point seven basis points, to four point six four seven percent" teaches you nothing about the unit unless you do two-decimal arithmetic in your head mid-sentence. And "four point six four seven percent" is three spoken decimals — precision no listener can hold or use.)
20. "The thirty year fell nine, to five point one nine six percent." — FLAG (L1: "fell nine" is elliptical. The unit lives in the previous sentence. Heard cold, "the thirty year fell nine" reads most naturally as nine percent, which is off by a factor of about a hundred and fifty. This is the single most mangle-prone sentence in the script.)
21. "Now the part the headlines skipped." — FLAG (L1-minor: a claim about what other outlets did, asserted with no basis, and a mild producer-view frame. The exemplar's equivalent signpost is "Here is the key part", which claims nothing about anyone else.)
22. "A buyback is a debt management operation, not new money and not stimulus." — OK. **Best gloss in the script.**
23. "And it does not begin until the ninth of September." — OK
24. "India rose on an announcement whose first effect is three weeks away." — OK as a sentence; note it silently hardens the sentence-12 inference into settled fact. Good line, resting on a claim the script has not marked as inferred.

**Movers — sugar**

25. "Now what moved." — OK
26. "The biggest gain was a sugar producer, Balrampur Chini Mills, up seventeen point eight seven percent." — OK. Textbook L2: name and what-it-does in the same breath.
27. "Sugar shares rose up to eighteen percent across the industry." — OK
28. "On Wednesday the government capped bulk buyers of sugar at fifteen days of stock." — OK
29. "Read that the right way round." — OK (direct address, earns its place)
30. "It binds buyers, not mills, and it is meant to cool sugar prices, not support them." — OK. The correction the composition note promised, and it does land before the number.
31. "What lifted the shares is the price the order confirms." — **FLAG (L4: second-highest-value finding.)** This is the load-bearing causal sentence of the whole sugar beat and it is compressed past the point of parsing. The unspoken chain is: government only caps stockholding when prices are already high → so the order is *evidence* of a high price → a high sugar price is good for the mills that sell sugar. Three links, zero spoken. Heard once, "the price the order confirms" is a riddle.
32. "Spot sugar touched five thousand five hundred and thirty rupees for a hundred kilos, reported as a sixteen year high." — OK ("a hundred kilos" for "a quintal" is a genuinely good audio call; "reported as" hedges honestly)

**Movers — Indo Borax**

33. "Indo Borax and Chemicals rose almost fifteen percent, and it was the buyer in a takeover." — FLAG (L2-minor: **no plain what-it-does.** Every other company in the script gets one or carries one in its name. Here the listener gets "and Chemicals" and must make do. Name is on-mention and not deferred, so this is a descriptor gap, not the deferred-name failure L2 is built to catch — see the verdict rationale for why I am not escalating it.)
34. "It is taking sixty four point two six percent of a listed peer, Kronox Lab Sciences, for two hundred and forty six crore rupees." — OK, marginally ("a listed peer" is doing the what-it-does work by inheritance, which is thin but survives; "crore" unglossed matches the exemplar's practice for an Indian audience)
35. "That forces a compulsory offer to Kronox's public shareholders, at about fifty two percent more." — FLAG (L1: **"more" than what?** The comparator is never spoken. Fifty two percent above the market price is the intended meaning; a listener could as easily hear "fifty two percent more shares" or "fifty two percent more money".)
36. "Buyers do not usually get that reception." — OK (the so-what, plainly made; "reception" is loose but recoverable from "rose almost fifteen percent")

**The faller / the unexplained**

37. "Only one share we follow fell more than five percent." — FLAG (L1: the universe is undefined. One out of *what*? And "share we follow" is the closest the script comes to portfolio language — heard cold it can suggest a list we hold rather than a list we cover. Not a guard breach, but it is the sentence a compliance-minded listener would stop on.)
38. "Himadri Speciality Chemical, down six point one four percent." — OK
39. "We ran no search on it, so I am not going to guess." — FLAG (L1: process meta. The honesty is right and the instinct is right; the register is a desk note. The listener is told about our research workflow rather than the market.)
40. "Eight of the ten biggest risers have no cause either." — **FLAG (L1 + unsupported-by-implication: see the writer-flagged-lines section. The word "either" does real damage.)**
41. "We ran fifteen checks on them and killed three stories that would have shipped as reasons, all wrongly dated." — **FLAG (L1: the most flagrant desk/newsroom shorthand in the script.** "Ran fifteen checks", "killed three stories", "would have shipped", "wrongly dated" — four pieces of in-house production vocabulary in nineteen words. This is precisely the "producer's cut" register L1 names. The underlying point — that we caught and discarded three explanations that turned out to be from other days — is a trust-building point worth keeping, in plain English.)

**The observation**

42. "Here is what struck me this week." — OK (exemplar-consistent signpost, correctly re-scoped to "this week" under the day-name deviation)
43. "Two central banks published minutes seven hours apart on Wednesday, and both were arguing about raising rates." — OK. Strong, plain setup.
44. "At the Reserve Bank of India, Deputy Governor Poonam Gupta records that no further easing is possible." — FLAG (L1: "easing" is unglossed jargon for rate cuts, and "records that" is an odd, bureaucratic verb aloud.)
45. "She sees a case for a rate increase emerging next financial year, with inflation peaking at five point nine percent in the December quarter." — FLAG (L1-minor: whose forecast is the five point nine? Attached to "she sees", it reads as Gupta's personal projection; it may well be the central bank's. Ambiguous as heard.)
46. "The rate itself is unchanged at five point two five percent, held unanimously." — OK
47. "The American Federal Reserve's minutes followed that night." — OK
48. "A nine to three hold, three regional presidents wanting a higher rate." — FLAG (L1: verbless fragment carrying two pieces of jargon. "A nine to three hold" assumes the listener knows this is a vote; "three regional presidents" assumes they know the regional Federal Reserve banks vote on rates.)
49. "Nobody has set those two side by side." — **FLAG (unsupported claim + implies research we did not do — see the writer-flagged-lines section. This is the finding I would fix first.)**
50. "The irony is that Thursday's relief came from a debt operation, not from any change in the rate path." — OK, marginally ("the rate path" is soft jargon but is carried by the surrounding beat; "the irony is" is analyst-voice but the exemplar sanctions one personal observation per episode)
51. "Both are arguing about the same direction, and it is not down." — OK. **Best closing line in the script.** Plain, concrete, no jargon, lands the whole beat.

**What to watch**

52. "One date to keep." — OK
53. "The Reserve Bank meets on rates from the fifth to the seventh of October." — OK
54. "Those minutes just made that meeting a lot more interesting." — FLAG (L1-minor: "those minutes" — whose? The Federal Reserve's minutes were discussed four sentences ago and the Reserve Bank's five before that. The intended referent is the Reserve Bank's, but proximity pulls the listener to the Fed's.)

**Firebreak**

55. "That's your brief." — OK
56. "Before I sign off: this has been general market commentary, not investment advice." — OK (verbatim exemplar)
57. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK (verbatim exemplar)
58. "Markets are risky; you may lose money; act with care." — OK (verbatim exemplar)
59. "See you tomorrow." — OK (sanctioned standing sign-off)

## Punch list

Ordered by severity. The four blockers are all single-sentence edits — **no restructure is needed.**

### Blockers (fix before TTS)

- **[B1 — sentence 49] "Nobody has set those two side by side."** Unsupported universal claim about all published
  commentary, and it implies a survey of coverage that we did not run. Nothing in a brief can support "nobody".
  → Cut it, or make it a framing move rather than a claim: **"Set those two side by side."** Zero words lost, all
  of the rhetorical work kept, no claim made.

- **[B2 — sentence 41] "We ran fifteen checks on them and killed three stories that would have shipped as reasons, all wrongly dated."**
  Flagrant producer-view meta — the exact register L1 exists to catch ("killed", "shipped", "ran checks").
  → **"We looked for explanations and found three that did not hold up, because they turned out to be from other days."**
  Same trust-building point, no newsroom vocabulary.

- **[B3 — sentence 40] "Eight of the ten biggest risers have no cause either."** The word "either" reaches back and
  attaches to Himadri — and the only Himadri proposition available to attach to is "we ran no search on it". Heard
  once, "either" converts our *non-search* into *no cause exists*, which is precisely the false negative the
  composition notes say the script avoids. The word undoes the care taken three sentences earlier.
  → Drop "either" and name the standard: **"For eight of the ten biggest risers, we could not verify a reason."**

- **[B4 — sentence 12] "India came last because Brent crude rose for a fifth straight session…"** Stated as flat
  fact when it is the script's one inference, and the mechanism that would make it make sense is missing. As
  heard the reasoning is self-defeating: Japan and Korea import oil too, and the script has just said they rose more.
  → Mark the inference and close the chain: **"The most likely brake on India was oil. Brent crude rose for a fifth
  straight session, to ninety three dollars and eighty seven cents a barrel, and India buys almost all of its oil
  from abroad."**

- **[B5 — sentence 45, added by the S1 pass] "She sees a case for a rate increase emerging next financial year."**
  The brief says **2026-27**, which is the financial year we are currently in. "Next financial year" moves the
  rate-hike case about twelve months further out than the source supports, and the sentence also drops the brief's
  "may". See S1-1.
  → **"She sees a case for a rate increase possibly emerging later this financial year."**

- **[B6 — sentence 35, added by the S1 pass] "at about fifty two percent more."** With no comparator spoken, the
  listener supplies "more than the market price" — and the brief says the market price is *above* the deal price,
  so the default reading inverts the fact. See S1-2.
  → **"at about fifty two percent more than the sellers themselves got."**

### Should fix

- **[sentence 31] "What lifted the shares is the price the order confirms."** Three unspoken links in one clause.
  → **"The shares rose because of what the order implies. Governments only ration sugar when the price is already
  high, and a high sugar price is good news for the mills that sell it."**
- **[sentences 18-20] "yields" / "the ten year" / "fell nine".** "Yields" is never glossed and is the pivot word of
  the beat; "the ten year" has no noun; "fell nine" drops its unit and invites a hundred-fold misread.
  → Gloss once and cut the second bond: **"That pushed down what America pays to borrow. The rate on its ten year
  government debt fell to about four point six five percent."** Drops the thirty-year line and the basis points
  entirely, which the listener cannot use.
- **[sentence 35] "at about fifty two percent more."** *(Promoted to a blocker by the S1 pass — see S1-2. My first
  suggested comparator here was "above where the shares were trading", and checking the brief showed that is
  **wrong**: the fifty two percent is above the price the sellers negotiated, and the brief says the market price
  is above the deal price, not below it.)* Correct fix: **"at about fifty two percent more than the sellers
  themselves got."**
- **[sentence 6] "India got the smallest share of it."** The pronoun changes referent mid-sentence.
  → **"It was made in Washington, and India got the smallest share of the gain."**
- **[sentence 37] "Only one share we follow fell more than five percent."** Undefined universe, faint portfolio
  connotation. → **"Only one large company fell more than five percent."**
- **[sentence 39] "We ran no search on it, so I am not going to guess."** Keep the honesty, drop the workflow.
  → **"I do not have a verified reason for that one, so I am not going to guess."**

### Nice to have

- [sentence 9] Cut "on a count taken during the session" — a hedge with no listener payoff. (Frees words for B4.)
- [sentence 21] "Now the part the headlines skipped" → "Here is the part that matters" (claims nothing about other outlets).
- [sentence 44] "records that no further easing is possible" → "says there is no room left to cut rates further."
- [sentence 48] "A nine to three hold, three regional presidents wanting a higher rate." → "The Federal Reserve
  also held, by nine votes to three, with the three dissenters wanting a higher rate."
- [sentence 54] "Those minutes" → "The Reserve Bank's minutes" (proximity currently points at the Fed's).
- [sentence 45] Attribute the five point nine percent inflation figure explicitly.

**Word-budget note.** The body is at 700, the ceiling. B4 and the yields gloss add words. Cutting the thirty-year
sentence (sentence 20, twelve words) and the sentence-9 hedge (eight words) funds both with room to spare, and both
cuts improve the audio independently.

## The three writer-flagged lines

Assessed independently. I reached the ledger verdicts on all three before reading the writer's flags back; two of
the three are worse than the writer judged, one is roughly as flagged.

**1. "India came last because Brent crude rose for a fifth straight session."** The writer flagged this as an
inference rather than a filing. Correct, and **"because" does overstate** — it is the grammar of an established
fact, not of a read. But the confidence problem is the smaller half. The larger problem the writer did not flag is
that **the mechanism is absent**, and without it the sentence argues against itself: Japan and Korea are also oil
importers and the script has just said they rose more. A listener who follows the logic ends up more confused than
before the reason was given. Fix both halves together — see B4.

**2. "Eight of the ten biggest risers have no cause either."** The writer flagged "either" as linking back to a
prior item and asked what a listener attaches it to. **The honest answer is: Himadri, and it attaches to the wrong
proposition.** The only Himadri statement in earshot is "we ran no search on it" — an admission about *us*, not a
finding about *the stock*. "Either" needs a shared predicate, and the nearest one it can borrow is "has no cause".
So the word retroactively upgrades our non-search into a factual claim that no cause exists. That is the exact
false negative the composition notes take credit for avoiding; the avoidance is real in sentence 39 and is undone
by one word in sentence 40. Also, "have no cause" is loose in its own right — everything has a cause; the claim
is that we could not verify one. Fix both in one rewrite — see B3.

**3. "Nobody has set those two side by side."** The writer flagged the antecedent, trimmed for the word band, and
asked whether it survives in speech. **The antecedent is the lesser problem, and it does mostly survive**: "those
two" reaches back about five sentences to "two central banks", and there is no competing pair in between, so a
listener does get there — call it a slight stumble, not a break. **The real problem is the claim itself.** "Nobody
has" is a universal statement about all published commentary everywhere, it cannot be supported by any brief, and
it implies we surveyed the coverage. This is the one line in the script I would refuse to send to audio as
written. The rhetorical move it is reaching for survives intact as an imperative — "Set those two side by side" —
which asserts nothing. See B1.

## Guard scan (no advice / no tips / no portfolio)

Scanned the full body specifically for recommendation language, targets, ratings, and holdings framing.

| Guard | Result |
|---|---|
| Buy / sell / hold / accumulate / book profits | **Clean** — zero instances |
| Price targets, fair value, valuation calls | **Clean** — zero instances |
| "We own / our position / our portfolio / holdings" | **Clean** |
| Forward-looking predictions stated as fact | **Clean** — the one forward statement, Gupta's rate-hike case, is attributed to a named person and scoped to next financial year |
| Imperatives to the listener | Two, both benign: "Read that the right way round" (a comprehension instruction) and "One date to keep" (a watch-item, exemplar-sanctioned) |
| Firebreak present and verbatim | **Yes**, sentences 55-58, word-for-word with the exemplar |

**One item to note, not a breach:** "Only one **share we follow** fell more than five percent" (sentence 37). This
is coverage language, not holdings language, and I do not read it as a guard breach. But it is the single sentence
in the script where a listener could infer a tracked book, and it costs nothing to neutralise. Rewrite suggested
in the punch list.

**Guard verdict: PASS.** No tips, no recommendation, no advice, no targets, no portfolio claims.

## Sanctioned-deviation execution check

Judging execution only, not permission. The day-name substitution for "today" is sanctioned; so is keeping
"See you tomorrow".

Every time-word in the body:

| # | Phrase | Verdict |
|---|---|---|
| 3 | "Thursday's session" | Correct |
| 4 | "The Nifty rose on Thursday" | Correct |
| 9 | "during the session" | Correct (relative, unambiguous) |
| 17 | "On Wednesday the American Treasury" | Correct |
| 18 | "fell the same session" | Correct (relative) |
| 23 | "the ninth of September" | Correct (absolute date, no drift) |
| 28 | "On Wednesday the government capped" | Correct |
| 42 | "what struck me this week" | Correct — properly re-scoped from the exemplar's "about today" |
| 43 | "seven hours apart on Wednesday" | Correct |
| 47 | "followed that night" | Correct (relative to Wednesday) |
| 50 | "Thursday's relief" | Correct |
| 53 | "the fifth to the seventh of October" | Correct |
| 59 | "See you tomorrow" | Sanctioned |

**Zero instances of "today", "yesterday", "this morning", or "in a few hours".** The substitution is executed
cleanly and consistently across all thirteen time-words. On its own terms this is the best-executed part of the
script — no L3 hits of the kind the check is built for.

**One inconsistency in the deviation's own logic, flagged not as a fact error but because the principal should
decide it consciously.** The script's stated reason for dropping "today" is that *"saying today would be wrong at
the moment of listening."* **"Good evening" (sentence 1) is wrong in exactly the same way** on a Friday-daytime
publish — and unlike "See you tomorrow", it was not named as a kept standing element. Either it is a fixed show
open, in which case the deviation note should say so alongside the sign-off, or the same reasoning that removed
"today" removes it too. Two consistent positions exist; the script is currently holding half of each.

## Source spot-check (S1)

Opened `briefs/public/2026-08-20.md` only at this point. **Two mismatches found, one of them material.**

### Figures that match — clean

| Claim in script | Brief | Match |
|---|---|---|
| Nifty twenty four thousand two hundred and thirty one, up zero point six four percent | 24,231.85 (+0.64%) | ✓ |
| Ending a seven session losing run | "first rise after seven straight falls" | ✓ |
| Three and a half risers per faller, counted during the session | 2,148 to 600 (= 3.58), "measured during the session" | ✓ |
| Kospi roughly five and a half to six percent | 5.5%–6% | ✓ |
| Japan and Hong Kong each a little over one percent | Nikkei 1.16–1.3%, Hang Seng 1.1–1.19% | ✓ |
| Brent ninety three dollars eighty seven, fifth straight session | $93.87, "a fifth straight session" | ✓ |
| Treasury doubling buybacks, two billion to at least four billion an operation, announced Wednesday | identical | ✓ |
| Ten year fell five point seven basis points to four point six four seven percent | identical | ✓ |
| Thirty year fell nine, to five point one nine six percent | identical | ✓ |
| Buybacks begin ninth of September | 9 September | ✓ |
| "Not new money and not stimulus" | verbatim | ✓ |
| Balrampur Chini Mills up seventeen point eight seven percent, biggest gain | +17.87%, "the day's biggest move" | ✓ |
| Sugar shares up to eighteen percent | "up to 18% across the industry" | ✓ |
| Stock cap set Wednesday, fifteen days, binds buyers not mills, meant to cool | 19 Aug (= Wednesday), identical framing | ✓ |
| Spot sugar five thousand five hundred and thirty rupees for a hundred kilos, sixteen year high | ₹5,530 a quintal (a quintal *is* 100 kg), "reported as a 16-year high" | ✓ |
| Indo Borax almost fifteen percent | +14.82% | ✓ |
| Sixty four point two six percent of Kronox for two hundred and forty six crore | 64.26%, ₹246.12 crore | ✓ |
| Himadri down six point one four percent, no search run | −6.14%, "we ran no search on it" | ✓ |
| Fifteen checks, three stories killed, all wrongly dated | verbatim from the brief | ✓ |
| Minutes seven hours apart Wednesday; Fed's followed that night | 17:00 and ~23:30 on 19 Aug | ✓ |
| Nine to three hold, three regional presidents wanting higher | identical | ✓ |
| Rate unchanged five point two five percent, held unanimously | identical | ✓ |
| Inflation peaking at five point nine percent in the December quarter | 5.9% in Oct–Dec | ✓ |
| Reserve Bank meets fifth to seventh of October | 5–7 October | ✓ |
| Hormuz shut since February | "effectively shut since 28 February" | ✓ (hedge softened, see below) |

**Guarded-omission check — all honoured.** No India VIX, no India ten-year yield, no sector ranking, no
institutional flows, no year-to-date figures, no Indo Borax per-share price, Kospi kept as a range. Every
suppression the brief demands is respected in the script.

### S1-1 — MISMATCH (material): "next financial year"

> Script, sentence 45: "She sees a case for a rate increase emerging **next financial year**."
> Brief, line 35: "a case for a rate *increase* may emerge in **2026-27**."

The Indian financial year 2026-27 runs from April 2026 to March 2027. The session covered is **20 August 2026** —
we are *inside* 2026-27 right now. The source's window is **the current financial year**; the script relocates it
to the next one, pushing the rate-hike case roughly twelve months further out than the brief says.

The internal evidence agrees with the brief and against the script: the same sentence has inflation peaking in the
October–December quarter, which is this financial year. A hike case that emerges *after* that peak is a
this-year story.

The script also drops the brief's modal — "**may** emerge" becomes "she **sees** a case ... emerging" — so the
line simultaneously hardens the claim and mis-dates it.

→ Fix: **"She sees a case for a rate increase possibly emerging later this financial year."**

### S1-2 — MISMATCH (misleading as heard): the fifty two percent

> Script, sentence 35: "That forces a compulsory offer to Kronox's public shareholders, **at about fifty two percent more**."
> Brief, line 66: "the public offer sits about 52% **above what the sellers negotiated** ... the takeover code doing its job **when the market price is well above the deal price**."

The number is right; the missing comparator makes it wrong in the ear. With no reference stated, a listener
supplies the obvious default — fifty two percent above the market price — and the brief says explicitly that the
market price sits *above* the deal price, so the default reading points the wrong way. The brief's 52% is
₹157.27 against a negotiated ₹103.22, a deal-price comparison, not a market one.

This is the finding I would have got wrong from the cold read alone: my ledger flagged only "more than what?", and
my first suggested repair supplied the wrong comparator. The S1 pass caught it. Corrected fix is in the punch list.

### S1-3 — Hedge attrition (pattern, WARN)

Not mismatches, but the script is consistently one notch more confident than its source:

- "effectively shut since 28 February" → "**has been shut** since February"
- "may emerge in 2026-27" → "**she sees** a case ... emerging" (also S1-1)
- "no cause anyone can point to" → "**have no cause**", with the brief's own governing caveat dropped: *"Large-deal
  data is not wired in at all, which weakens every 'cause not established' above — that is a hole, not a clean negative."*
- breadth: the brief hedges twice, "from **one live report** and measured during the session"; the script keeps the
  weaker half of the hedge and drops the single-source half.

Individually small. Together they mean the audio asserts more than the brief is willing to.

### Two inherited items — flag upstream, fix here anyway

**"Nobody has set those two side by side"** (B1) and **"killed three stories that would have shipped"** (B2) both
come from the brief nearly verbatim (lines 121 and 125). The script did not invent them, and B2's numbers are
correct. That does not make either shippable as audio: "nobody has" is still an unsupportable universal claim, and
newsroom register still fails a listener. **This gate covers the podcast only and never blocks the brief** — so
fix both in the script, and raise "Nobody has set the two documents side by side" with the principal as a brief-side
claim that cannot be sourced.

Likewise, the **"either" problem (B3) exists in the brief too** — line 125 groups Himadri with the risers as having
"no cause anyone can point to", while line 85 says of the same stock "we ran no search on it". A reader can hold
both statements and see the difference. A listener cannot.

## Verdict rationale

**FAIL.** Six blockers, on three independent grounds. Stating the grounds separately because each would fail on its own.

1. **A source mismatch (S1-1).** "Next financial year" mis-dates the brief's 2026-27, which is the year we are in.
   This is the wrong-period class of error the S1 check exists to catch — the direct descendant of the 2026-06-04
   wrong-day leak. It sits in the episode's one analytical set-piece, where the whole point is *when* rates turn.
2. **A figure that inverts as heard (S1-2).** "Fifty two percent more" with the comparator missing sends the
   listener to the market price; the brief's comparison is to the negotiated deal price, and the brief states the
   market price runs the other way.
3. **Unsupportable claims and desk register (L1).** "Nobody has set those two side by side" asserts a survey of all
   commentary that nobody ran. "Killed three stories that would have shipped" is the producer-view shorthand L1
   names by example. "Have no cause **either**" converts an admitted non-search into a factual negative, three
   sentences after the script correctly refuses to make that claim.

Add two L4 mechanism gaps — the oil sentence, whose stated logic argues against itself once you notice Japan and
Korea also import oil, and "the price the order confirms", which asks the listener to reconstruct three unspoken
links — and the case is not close.

**What this verdict is not.** This is not a bad script, and none of the six blockers is structural. The spine is
strong and genuinely original, the buyback caveat is the best-executed beat of any recent episode, the sugar
direction correction lands before the number exactly as designed, the day-name deviation is executed cleanly across
all thirteen time-words, every guarded omission is honoured, the guard scan is clean, and L5/L6 are mechanically
perfect. **All six blockers are single-sentence edits.** The word budget absorbs them if sentence 20 (the thirty
year yield) and the sentence 9 hedge are cut, both of which improve the audio regardless.

Re-verify after the edits, then TTS. Do not burn Sarvam credits on the current draft.

### Note for the principal — two of the blockers came in from the brief

B1 ("Nobody has set the two documents side by side") and B2 ("killed three stories that would have shipped") are
carried almost verbatim from `briefs/public/2026-08-20.md` lines 121 and 125, and the "either" tension in B3 exists
there too. This gate does not touch the brief. But an unsupportable "nobody has" is worth a look upstream, since
every downstream surface inherits it.

---

# Re-verify — fix pass v2 (2026-08-21)

**Verdict:** **WARN** — audio generation **UNLOCKED**, held for the principal's approval per the TTS gate.
**Checks (counts = FLAG hits):** L1 **2** (was 16) / L2 **0** (was 1) / L3 **0** (was 1) / L4 **0** (was 2) / L5 **0** / L6 **0** / S1 **0** (was 2)
**Blockers cleared:** B1 ✓ B2 ✓ B3 ✓ B4 ✓ B5 ✓ B6 ✓ · missing unit ✓
**Open items:** 7 WARNs, none blocking. Three are regressions introduced by the fix pass.
**Backup check:** `backups/2026-08-21/podcast-script_2026-08-20_v1.md` exists (8,218 bytes, 11:08). File-management rule honoured.

## Honest limitation on this pass

**This could not be a true cold read and I am not going to claim it was.** I hold the brief from the v1 pass and
cannot un-know it. Mitigation: I ran the listenability ledger on the new body first and only re-opened the brief
to re-check changed figures and the guarded omissions. The naive-listener judgments below are therefore weaker
evidence than v1's, and that limitation is structural, not a lapse — it is the reason the skill puts the cold read
first and once. Where a v2 judgment depends on not knowing the story, I have said so.

## Ledger — v2 body, 54 sentences (was 59)

Sentences carried over unchanged from v1 and marked OK there are not re-argued; they are listed as **carried**.
Every changed, new, or newly-adjacent sentence is judged fresh.

**Open (1-3)** — carried OK. "Good evening" flag **withdrawn**, see the ruling below.

4. "The Nifty rose on Thursday, ending a seven session losing run." — carried OK
5. "The reason was not Indian." — OK. Terser than v1's "was not made in India"; "not Indian" as a predicate is slightly clipped but parses first time.
6. "It was made in Washington, and India got the smallest share of the rally it set off." — **FIXED.** Both pronouns now point at the same antecedent (the reason), and "the rally" is a real noun the second "it" can hang off. The v1 referent-switch is gone.
7-8. Close sentences — carried OK
9. "About three and a half shares rose for every one that fell." — **FLAG (W2, hedge attrition — and partly my fault).** I suggested cutting "on a count taken during the session" as a nice-to-have. It went, and so did the rest: the brief hedges this number **twice**, "from one live report and measured during the session." The script now states a single-sourced intraday ratio flat. "About" carries some softening and the figure is right (2,148:600 = 3.58), so this is not an S1 mismatch — but the audio is more confident than the source.
10. "Korea's Kospi gained roughly five and a half to six percent, and Japan and Hong Kong each rose a little over one percent." — **FLAG (W1, the one real regression).** The sentence is unchanged; what changed is that **"Asia rallied and India rallied least" was deleted above it.** That cut cost three things at once: the paragraph's topic sentence, the transition into it, and — the expensive one — the explicit comparison that the very next sentence depends on. See W1.
11. "The likely reason India lagged is oil." — **FIXED (B4, confidence half).** "The likely reason" marks the inference correctly. "Lagged" now leans on an unstated comparison, which is W1, not this sentence's fault.
12. "Brent crude rose for a fifth straight session, to ninety three dollars and eighty seven cents a barrel." — carried OK
13. "India buys almost all of its oil from abroad, so a dearer barrel feeds straight into Indian inflation, and inflation is what the Reserve Bank is already worried about." — **FIXED (B4, mechanism half). Ruling below: the loop closes.** 29 words, three clauses, but a single forward chain (A so B and C), comma-segmented, no nesting — passes L6. Minor: "a dearer barrel" is faintly literary; a listener still gets it. Separately flagged as **W5** for provenance.
14. "The Strait of Hormuz, which carries much of the world's oil, has been shut since February." — FLAG (W7, carried from v1: the brief says "**effectively** shut since 28 February". Minor, unchanged.)
15-16. "The rally came from Washington. / The brake came from Hormuz." — carried OK
17. "On Wednesday the American Treasury said it will at least double its buybacks..." — carried OK. Newly the paragraph's first sentence, since "So, Washington." was cut — see W3.
18. "A bond's yield is what it pays whoever holds it." — **NEW, and well placed.** The gloss lands immediately *before* the first use of "yield", which is the correct order. Accurate enough for lay audio. Clears the v1 L1 hit.
19. "Long term American yields fell the same session, the ten year by five point seven basis points, to about four point six five percent." — **LARGELY FIXED.** Three decimals gone (4.647 → "about four point six five", correct rounding). "The ten year" still has no noun, but it now sits in apposition inside a sentence that opens "Long term American yields", so the listener can assemble it. Residual, minor.
20. "A basis point is one hundredth of one percent." — **FLAG (W4, minor).** The gloss is right, but it lands **one sentence after** first use, unlike the yield gloss which correctly precedes. The listener meets "five point seven basis points" cold, then gets the definition. Recoverable, and the level in the same sentence cushions it.
21. "Here is the key part." — **FIXED.** The exemplar's own claim-free signpost replaces "Now the part the headlines skipped", retiring the unsupported claim about other outlets.
22-24. Buyback caveat block — carried OK. Still the strongest beat in the script.
25. "The biggest gain was a sugar producer, Balrampur Chini Mills, up seventeen point eight seven percent, and sugar shares rose up to eighteen percent industry wide." — OK (two v1 sentences merged, 26 words, single-thread). Newly paragraph-initial since "Now what moved." was cut — see W3.
26. "On Wednesday the government capped bulk buyers of sugar at fifteen days of stock." — carried OK
27. "The order binds buyers, not mills, and it is meant to bring sugar prices down, not push them up." — **IMPROVED.** "The order" replaces a bare "It"; "bring down / push up" replaces "cool / support". Plainer than v1 and the direction still leads the number, as designed.
28. "But a government only rations stock when the price has already run hard." — **NEW. This is the missing link, now spoken.**
29. "Spot sugar touched five thousand five hundred and thirty rupees for a hundred kilos, reported as a sixteen year high." — carried OK
30. "Which is good for the mills that sell it, and that is what lifted the shares." — **FIXED (my second-highest v1 finding).** The chain now runs complete and in order: rationing implies a high price → here is the high price → high prices are good for mills → that is what moved the shares. Nothing left for the listener to reconstruct. Sentence-initial "Which" is informal but natural in speech.
31. "Only one stock in the seven hundred we cover fell more than five percent." — **FIXED.** Universe defined, matches the brief's 707-name set, and the faint portfolio reading is gone.
32. "Himadri Speciality Chemical, down six point one four percent." — carried OK
33. "I cannot tell you why, because we did not look into that one." — **FIXED.** Same honesty, zero workflow register.
34. "Eight of the ten biggest risers have no cause anyone can point to." — **FIXED (B3).** "Either" gone. The brief's own wording, and "no cause anyone can point to" is meaningfully softer than v1's "have no cause" — it claims nobody can point to one, not that none exists.
35. "We did go looking there, fifteen times over." — **FIXED (B6), and better than a fix.** v1 left the Himadri/risers contrast implied; "We did go looking **there**" now states it affirmatively, so the listener actively hears *we skipped one and worked the others*. **This is better than v1 was before the flag.** Minor: "fifteen times over" can read as an intensifier rather than a literal count of fifteen.
36. "Three of the explanations we found turned out to be old stories with the wrong date." — **FIXED.** Newsroom register gone, meaning preserved exactly.
37. "Here is what struck me this week." — carried OK
38. "Two central banks published their meeting minutes seven hours apart on Wednesday..." — **IMPROVED.** "Their meeting minutes" quietly glosses "minutes".
39. "At the Reserve Bank of India, Deputy Governor Poonam Gupta says there is no room left to cut." — **FIXED.** "Easing" and "records that" both gone.
40. "She argues a case for a rate rise may emerge in this financial year, and she has inflation peaking at five point nine percent in the December quarter." — **FIXED (B5).** Period corrected, modal restored, and the forecast now has an explicit owner, resolving the v1 ambiguity.
41. "India's rate itself is unchanged at five point two five percent, held unanimously." — **IMPROVED.** "India's" pre-disambiguates from the Fed sentence that follows.
42. "The American Federal Reserve's minutes followed that night." — carried OK
43. "Its rate setters voted nine to three to hold, and the three who dissented wanted a rise." — **FIXED.** Verb and subject supplied; "three regional presidents" traded away, which loses colour but removes jargon the listener could not place. Good trade.
44. "Set those two documents side by side." — **FIXED (B1).** The rhetorical turn survives intact with no claim about anyone's commentary. "Documents" pairs cleanly with "minutes" in both halves and the imperative sits right after the Fed sentence, so the antecedent is closer than in v1.
45. "The irony is that Thursday's relief came from a debt operation, not from any change in rates." — **IMPROVED** ("the rate path" → "in rates").
46. "Both are arguing about the same direction, and it is not down." — carried OK. Still the best line in the script.
47-48. "One date to keep. / The Reserve Bank of India next meets..." — OK, "of India" added.
49. "Its August minutes just made that meeting a lot more interesting." — **FIXED.** Owner supplied; no longer pulls toward the Fed's minutes.
50-54. Firebreak — carried OK, verbatim.

## Mechanical re-check (L5 / L6)

700 words, at the ceiling and inside the band. **Zero** digits, currency/percent symbols, em- or en-dashes,
`[SAY:]` hints, exclamations, ampersands, slashes. Hyphens: `toro I-Q` and `SEBI-registered` only. Longest
sentence **29 words** (two of them, both single-thread and comma-segmented). **L5 = 0, L6 = 0.**

## Source spot-check (S1) — changed figures only

| Changed claim | Brief | Verdict |
|---|---|---|
| "may emerge in **this** financial year" | "may emerge in 2026-27" — and 20 Aug 2026 falls inside FY 2026-27 | **S1-1 RESOLVED** — period and modal both correct |
| "about four point six five percent" | 4.647% | ✓ correct rounding |
| "she has inflation peaking at five point nine percent in the December quarter" | 5.9% in the October–December quarter | ✓ |
| "Its rate setters voted nine to three to hold, and the three who dissented wanted a rise" | 9–3 hold, three regional presidents dissenting for a higher rate | ✓ |
| "no cause anyone can point to" | brief line 125, verbatim | ✓ |
| "fifteen times over… old stories with the wrong date" | fifteen checks, three killed, all wrongly dated | ✓ |
| "the seven hundred we cover" | 707-stock universe | ✓ |
| "Its August minutes" | RBI minutes of the 3–5 Aug meeting, published 19 Aug | ✓ |
| The fifty two percent comparator | — | **S1-2 RESOLVED by deletion of the beat** |

**S1 = 0. Both v1 mismatches are gone and the fix pass introduced no new ones.**

**Guarded omissions — re-verified by grep on the spoken body, not taken on trust.** Zero hits for: VIX, fear
gauge, 52-week / lowest-since / one-year-low, Suven, Genus, Netweb, MMTC, CEAT, Sensex, Bank Nifty, midcap,
smallcap, year-to-date, institutional flows, sector, Indo Borax, Kronox. The single "rupee" hit is the sugar
price in rupees, not the currency. **The India ten-year guard holds**: the only "ten year" in the script sits
inside "Long term **American** yields fell the same session", so it cannot be misheard as the withheld Indian
figure. Kospi is still a range; the Reserve Bank is still 5.25% held unanimously; Himadri still carries our own
limit; the fifteen checks are still scoped to the risers by the word "there". **All hold.**
