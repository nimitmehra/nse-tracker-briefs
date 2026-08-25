# Verify Podcast Script — 2026-08-24

**Verdict:** **FAIL** — one flagrant L1 line. One fix pass, then re-verify before TTS.

**Checks (counts = FLAG hits):** L1 8 (one of them FAIL-grade) / L2 1 (near-miss, WARN-grade) / L3 0 / L4 0 / L5 0 / L6 1 / S1 0 / accuracy-and-hedge 2

**FAIL count: 1. WARN count: 12.**

The single blocker is sentence 16, "That runs backwards to the pattern of money leaving India for North Asia's artificial intelligence trade" — it presupposes a pattern the listener has never been told exists, because the brief's own scaffolding clause was cut to hold 699 words.

This is a close FAIL and the reasoning is set out in full in the punch list rather than buried. Everything else in the episode is WARN-grade or better, the source spot-check is completely clean, the mechanical checks are completely clean, and three of the four passages the producer flagged came back stronger than expected. **The fix is two words net on one paragraph.**

## Method and constraints

Order was honoured: script body + canonical exemplar read first, full per-sentence ledger built and committed, and only then the prior episode and `briefs/public/2026-08-24.md` opened for continuity and the S1 spot-check.

**Zero web searches were run. Zero live pages were opened.** Every input was a file on disk: the script, the exemplar README, the 2026-08-20 script, and the 2026-08-24 public brief. No quote page, no news site, no fetch of any kind. Where a script number disagreed with prior expectation, the script was treated as correct per the producer's digit-check.

The header block (lines 1 to 13) was excluded from the ledger as metadata, per instruction. Its "Tuesday / 25 August" references are backfill provenance, not spoken body, and are not reported as violations. The spoken body was independently confirmed free of any 25-August information.

## Per-sentence ledger

Every sentence of the spoken body, judged as a listener hears it: no source, no re-reading, half-attending.

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on Monday's session." — OK. No throat-clearing; matches exemplar cold-open exactly.

**The deposit window**
4. "The Reserve Bank of India has a window open for dollar deposits from Indians living abroad." — OK. Strong opener: a concrete thing, a plain audience, no jargon.
5. "It closes on the thirty first of August, not the thirtieth of September, leaving seven days on Monday." — OK. The correction is delivered before the error is named, which is the right order for the ear.
6. "The bank moved the date forward on the fourteenth because the response was so large." — OK, with a note. "Moved forward" is ambiguous in isolation (advanced or postponed?), but sentence 5 has already fixed the direction, so the listener cannot be misled.
7. "Its own release on Saturday puts the money raised at seventy two point eight five billion dollars." — OK.
8. "Two things about that date, and the second one is ours." — OK. Cryptic for one beat, resolved two sentences later. Earns its suspense.
9. "The central bank's own list of frequently asked questions still shows the retired thirtieth of September, so anyone checking the central bank's website gets the wrong answer from the central bank." — OK. See adjudication below. Thirty-one words, single-thread, one breath at pace.
10. "And we got it wrong too." — OK. Best sentence in the episode.
11. "This brief carried that retired date for several runs and never went back to check it." — **FLAG (L1: desk-shorthand "for several runs")**. A listener does not know what a "run" is. Production vocabulary leaking into the body. "For several editions" or "for weeks" costs nothing.
12. "It is retired now." — **FLAG (L1: ambiguous referent)**. Heard cold, "it" can attach to the FAQ page just mentioned, which would mean the central bank has fixed its website. It has not. The intended referent is our own use of the date.

**The close**
13. "The Nifty fifty closed Monday at twenty four thousand two hundred and nineteen, down zero point one four percent." — OK.
14. "Underneath it, three hundred and two shares rose and four hundred fell out of seven hundred and five, a second straight session of more fallers than risers under a flat index." — **FLAG (L1, mild: "more fallers than risers under a flat index")**. The plain numbers land first and land well; the trailing clause then restates the same fact in desk vocabulary. Thirty-one words but cleanly segmented, so not an L6 hit.

**Asia**
15. "Asia sold technology on Monday, Korea hardest, and India barely moved." — OK. Elliptical but transparent.
16. "That runs backwards to the pattern of money leaving India for North Asia's artificial intelligence trade." — **FLAG (L1: FAIL-level).** See adjudication. This is the one line in the episode a naive listener cannot follow.

**Reserves and house prices**
17. "Foreign exchange reserves rose almost ten billion dollars in the week to the fourteenth, a third straight build, but a build funded by that window's dollars stops when the window stops." — **FLAG (L1, mild: "a build" as a noun, twice)**. The underlying point — the money is temporary, so the cushion is temporary — is excellent and fully chained. Only the vocabulary is desk. Thirty-one words, borderline on L6 but speakable.
18. "And the Reserve Bank's house price index, published Monday, has annual growth down to three point six percent from four point five." — OK.
19. "That is below its own inflation path, so house prices are falling in real money." — **FLAG (L1, mild: "its own inflation path")**. Referent is ambiguous by ear — the index's inflation, or the bank's target? The so-what ("falling in real money") is well put and rescues most of it.

**Movers**
20. "Now the movers." — OK.
21. "The biggest gain was Ratnamani Metals and Tubes, up fourteen point five five percent." — **FLAG (L2, near-miss: no what-it-does)**. Downgraded from FAIL because the company name literally states the business. See adjudication.
22. "A subsidiary won export orders worth about two thousand seven hundred crore rupees, filed while the market was open." — OK.
23. "But the filing names the buyer only as international customers, and part of the work will be sub-contracted, not made in house." — OK. Genuinely good skeptical reporting, in plain words.
24. "The biggest fall was B-L-S International, down almost eleven percent, and here the limits matter more than the number." — OK. "The limits" is abstract for one beat, but functions as a signpost that care is coming, and the next four sentences deliver it.
25. "B-L-S holds outsourced visa processing contracts from governments." — OK. Clean what-it-does.
26. "Reports say a Spanish court has widened an investigation into an alleged visa fraud network at the Spanish consulate in Algiers, to look at the company's own document handling role." — **FLAG (L6: thirty words with a trailing purpose clause)**. The hedges are present and front-loaded, but this is the sentence carrying the sticky words. See adjudication.
27. "We have not read the court's order, and every account traces back to a single report, so three outlets repeating one claim is one source." — OK. "Three outlets repeating one claim is one source" is the single best piece of listener-legible epistemics in the script. Minor: "three outlets" arrives as a new fact, never previously mentioned.
28. "That is enough to say the reports caused the fall." — OK.
29. "It is not enough to say what the company is accused of, or whether it is accused at all." — OK. Load-bearing, and correctly placed where recency protects it.
30. "B-L-S categorically rejected the allegations in a filing made while the market was open." — OK. Same-session denial, given its own sentence.

**The unexplained**
31. "Five of the twelve biggest movers have no cause anyone can point to." — **FLAG (overclaim, mild)**. See adjudication. Also: the listener has not been told there is a list of twelve.
32. "The loudest is I-D-B-I Bank, up six point nine two percent on the day state owned banks led the market lower." — OK. The contrast makes the oddity concrete without a word of jargon. "Loudest" is writerly but clear.
33. "Nothing was filed." — OK.
34. "Nobody knows, and that is the accurate answer." — **FLAG (overclaim: a claim about the world, not about our search)**. See adjudication.

**The Hormuz correction**
35. "Here is what struck me about Monday." — OK. Exemplar-matching signpost.
36. "Much of the coverage said Indian shares fell on fear about the Strait of Hormuz, the narrow lane that carries much of the world's oil, after Iran threatened to seize ships crossing it." — OK. Thirty-three words, longest in the script, but single-thread with an inline gloss. The exemplar has several of these. Not an L6 hit.
37. "We do not accept that explanation, and the oil market is the reason." — OK.
38. "A real threat to that chokepoint does not send crude down, and Brent fell one point eight one percent on the same escalation." — **FLAG (L1, mild: "Brent" unglossed)**. The exemplar says "crude oil"; "Brent" is a benchmark name a general listener may not hold. Context carries it, barely.
39. "Indian refiners rose on the cheaper barrel, with Indian Oil up one point nine one percent." — OK.
40. "And the American sanctions announcement blamed for Monday landed after our market shut." — **FLAG (L2-flavoured: definite article on a never-introduced referent)**. "The American sanctions announcement" arrives as if the listener already knows about it. They do not. Sanctions on whom, for what?
41. "A fall that small does not need a geopolitical cause, and we are not giving it one." — OK. Excellent close to the argument.

**What to watch and sign-off**
42. "The date to keep is Monday the thirty first, when that deposit window shuts." — OK. Absolute date anchoring is the correct call for a backfilled episode.
43. "That's your brief." — OK
44. "Before I sign off: this has been general market commentary, not investment advice." — OK
45. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
46. "Markets are risky; you may lose money; act with care." — OK
47. "See you tomorrow." — OK. Standard sign-off; the forward date is pinned absolutely in 42, so no time-word confusion.

**L3 (listener-moment time): zero hits.** The covered session is named "Monday" throughout and spoken in the past tense; the only forward event is pinned to an absolute date safely ahead. The covered session is never called "yesterday", and no unhappened event is framed as "today". The day-name convention (standing deviation from 2026-08-20) is the right choice here and defuses the backfill risk rather than creating one.

**L4 (mechanism not metaphor): zero hits.** Every causal claim in the episode is stated as a full chain — the reserves build, the real house-price fall, the oil counter-argument. No oblique image stands in for a mechanism anywhere.

## The three flagged lines — adjudicated

### 1. "…anyone checking the central bank's website gets the wrong answer from the central bank." — **CLEARED**

Truth was not mine to judge; the producer independently corroborated the stale FAQ. Judged on delivery and fairness only:

**Delivery: passes.** Thirty-one words, but one thread and one breath. The rhetorical repetition ("the central bank's website … from the central bank") is the device that makes it land, and it lands cleanly by ear because the two halves are short. A listener gets exactly one idea: the official source is stale.

**Fairness: passes, and is in fact strengthened by what follows.** The line would be a cheap shot standing alone. It does not stand alone — the very next sentence is "And we got it wrong too," and the two after that own the error without qualification. Criticising a source and then immediately confessing the same failure is the fairest available construction, and it converts the line from a jab into a shared standard. Sentence 10 is the reason sentence 9 is publishable.

**The one real defect is downstream:** "It is retired now" (12) is ambiguous by ear and can be heard as "the central bank has now fixed its page." That is the opposite of the point and it is factually wrong. Fix the referent, not the criticism.

### 2. "Nobody knows, and that is the accurate answer." — **WARN, overclaim confirmed**

The writer's worry is correct, and I am not going to talk them out of it.

Literally, the sentence claims universal ignorance. It is false in that reading — the people who bought I-D-B-I on Monday know why they bought it. The defensible claim is narrower: *we* could not establish a cause. And the evidence the spoken body offers for even that narrower claim is one negative check, "Nothing was filed." The three empty search lanes and the dead block-deal feed that would justify the confidence are in the producer files, not in the listener's ears. So the script asserts its widest claim on its thinnest spoken evidence.

**Why this is a WARN and not a FAIL.** Two counterweights. First, ordinary English hears "nobody knows" as "there is no known public explanation," which is what we actually mean and what the listener actually takes away — the gap between claim and truth does not produce a false belief about the world. Second, the harm direction is right: an overclaim of *ignorance* is epistemically conservative, and it is paired with "Nothing was filed," which is a checkable fact. Compare the failure mode we are guarding against, which is manufacturing a cause. This sentence refuses to.

Sentence 31 carries the same overclaim in weaker form ("no cause anyone can point to") and should be fixed in the same pass.

**Fix (one word each, no length cost):** 31 → "Five of the twelve biggest movers have no cause we could establish." 34 → "We could not find one, and that is the accurate answer."

### 3. The B-L-S block, read aloud at pace — **HOLDS. Does not collapse into an accusation.**

This is the highest-stakes item in the episode and I read the six sentences aloud at speaking pace three times, listening for where a half-attending listener lands.

**The architecture is right, and the order is why.** The block runs: what-it-does → hedged report → epistemic limit → what we *can* say → what we *cannot* say → company denial. The two strongest protections sit at positions five and six, where recency works hardest. A listener who tunes out early hears less accusation, not more; a listener who hears the whole block ends on "whether it is accused at all" followed immediately by "categorically rejected." That is the correct terminal impression.

**Sentence 29 is the load-bearing line and it is unusually good.** "Or whether it is accused at all" explicitly holds open the possibility that the company is not a target. Most newsroom hedging stops at "alleged"; this goes a step further, and it is placed where it survives.

**Where it is weakest: sentence 26.** Thirty words, and it carries every sticky noun in the block — court, investigation, fraud, consulate, the company. The hedges "Reports say" and "alleged" are both present and both early, which is correct practice. But the trailing purpose clause, "to look at the company's own document handling role," is the part that names B-L-S, and by then the front-loaded "Reports say" is twenty-five words behind. At speaking pace a hedge that far back is doing less work than it does on the page. A listener half-listening can plausibly retain "Spanish court, visa fraud, the company" as a unit.

**Why this is still not a FAIL.** The 26-second exposure is repaired 15 seconds later by sentences 27 and 29, and the repair is explicit rather than implied. The block never asserts the company did anything; it asserts only that reports exist and that reports moved the price, which is the one claim we can actually stand behind. And the denial is not buried in a subordinate clause — it gets its own sentence, with "categorically," and notes it was filed the same session.

**Recommended (not required) hardening:** split 26 into two so the company clause carries its own hedge — "Reports say a Spanish court has widened an investigation into an alleged visa fraud network at the Spanish consulate in Algiers. Those same reports say the court is now also looking at the company's document handling role." Two short sentences, the attribution repeated, roughly the same word count.

## Declared cuts — did any remove a hedge?

Three of the four declared cuts are clean. One degraded a surviving claim. Two **undeclared** cuts did more damage than any declared one.

### Declared cut 1 — the FCNR(B) sub-total. **WARN: this one did degrade a surviving claim.**

The brief reads: "total inflows under the facility at US$72.85 billion, **of which US$65.4 billion is those deposits**." The facility total covers the deposit leg plus an overseas-borrowing leg; the deposits are the smaller number.

The script sets up "a window open for **dollar deposits** from Indians living abroad" and then says "puts **the money raised** at seventy two point eight five billion dollars." With the split gone, the listener attaches the whole facility total to the deposit window they were just told about, and over-counts the deposits by roughly seven and a half billion dollars. The brief's own What to Watch uses the correct figure for this window: "US$65.4 billion was in by 21 August."

Cutting for time is sanctioned; this cut changed what a surviving number refers to. **Fix costs three words and no restructuring:** "Its own release on Saturday puts total inflows under the facility at seventy two point eight five billion dollars." "Total inflows under the facility" signals the wider scope without spending the sub-total.

### Declared cut 2 — the withheld-sector-ranking note. **Minor.**

The script makes no sector-ranking claim, so the withholding note is not needed. One small consequence: "on the day state owned banks led the market lower" is stated bare, where the brief adopts it explicitly on a named outside source (Business Standard, Nifty PSU Bank −0.93%) after checking it against its own constituent reading. The brief did adopt it as its own conclusion, so the script is entitled to it. Noted, not flagged.

### Declared cut 3 — the Aegis Logistics beat. **Clean.**

Pure beat drop. No hedge attached to any surviving claim, and the "five of the twelve" count is unaffected. The skill sanctions cutting a mover rather than rushing the rest.

### Declared cut 4 — the realty-versus-house-prices connection. **Clean.**

This removed a tension, not a hedge. The surviving house-price sentences are brief-faithful, including "falling in real money" verbatim. Nothing in the script now asserts anything the brief qualified.

### Undeclared cut A — the scaffolding on the Asia paragraph. **This is the FAIL.**

The brief reads: "the pattern **this desk has flagged for weeks**, of money leaving India for the North Asian artificial-intelligence trade, ran backwards on Monday."

The script keeps the pattern and drops "this desk has flagged for weeks" — which is precisely the clause that tells the audience the pattern exists and is a recurring theme they have heard before. What survives presupposes the pattern with a definite article and never establishes it. On the page the reader can hold it; in audio it is the premise the whole sentence rests on, and it is gone. This cut is not in the declared list.

### Undeclared cut B — the reserves verification caveat. **WARN, and the one to look at after the FAIL.**

The brief hedges the swap-funding link twice and then forbids it outright: "**We have not verified how much of the build is swap-related**, because the weekly supplement does not break it out, so that is **a question to test against the next three weekly releases and not something to state as cause**."

The script: "a third straight build, **but** a build funded by that window's dollars stops when the window stops."

Read on the page, "a build funded by…" is generic and mirrors the brief's counterfactual. Heard aloud, the contrastive "but" plus the immediate context collapses the generic into the specific: the listener takes it that *this* build was funded by that window's dollars, which is exactly the causal claim the brief refuses to make. No verification caveat appears anywhere in the spoken body.

In fairness the brief is itself in tension here — its Lead says "the plumbing sitting under three consecutive weekly builds," which is the confident version the script picked up. But the Macro section is the more careful statement and it governs.

**Fix costs one word.** "but a build funded by that window's dollars **would** stop when the window stops." The conditional mood restores the hedge with no length penalty.

## Mechanical (L5) and length

**L5: zero hits. Independently machine-checked on the spoken body, not taken from the header.**

| Check | Result |
|---|---|
| Digits | none |
| Currency / percent symbols | none |
| Em-dashes / en-dashes | none |
| `[SAY:]` hints, brackets, parentheses, exclamation marks | none |
| Word count | 699, inside the 500–700 band |
| Longest sentence | 33 words (S36), single-thread with an inline gloss |

The header's self-report is accurate in every particular. Four sentences run 30 to 33 words (S9, S14, S17, S36); all four are comma-segmented single threads and speakable in one breath, so per L6 none is flagged on length alone. Only S26 draws an L6 flag, and for its trailing purpose clause rather than its count.

The respellings are correct for TTS: **toro I-Q**, **B-L-S International**, **I-D-B-I Bank**, and the Reserve Bank of India always said in full. "Ratnamani Metals and Tubes" is spelled with "and" rather than an ampersand.

**Does 699 feel padded or earned?** Earned. There is no filler sentence in the episode and no throat-clearing anywhere — the open is three words of brand and then straight into the window. The density is in fact the opposite problem: three of the flags above (S14, S16, S17) are compression artefacts, sentences squeezed to buy room rather than sentences spending room they did not need. Being one word under the ceiling is why the Asia paragraph lost its premise. That is worth saying plainly: **this script is not too long, it is too tight in three specific places**, and the fixes below are costed so they can be paid for.

## Continuity with 2026-08-20

**Voice: continuous and correct.** Identical open and identical sign-off, the same "Here is what struck me about Monday" signpost in the same slot, the same first-person-plural desk voice, the same practice of naming what we could not establish. A listener hears the same programme.

**The gap is handled correctly.** There was no episode on 21 August, so Friday's session is unseen. The script never references Friday, never assumes it, and pins its one forward date absolutely rather than relatively. The day-name convention carried over from 20 August is the right call for a backfilled episode and actively defuses the L3 risk rather than creating one.

**One regression against a previously adjudicated finding, and it matters.** The 20-August episode failed its cold read and was fixed; its v3 header records W1: cutting "Asia rallied and India rallied least" to pay down the word ceiling removed the comparison the next sentence depended on, leaving the listener to infer the premise. It was restored verbatim as its own short sentence.

**The same defect has recurred, in the same paragraph slot, one episode later, from the same cause.** The Asia paragraph again drops the clause that establishes the premise, again to pay down the ceiling, and again the following sentence is left with nothing stated to stand on. That precedent is the single strongest reason I am not downgrading the S16 flag to a WARN: this exact trade-off has already been adjudicated once and the ruling was that the premise sentence is load-bearing and must be paid for elsewhere.

The 20-August fix pass also established *where* the words should come from: "not one of them from a connective sentence, a gloss, a guard or the sugar causal chain… the words came out of the interiors of long sentences." That method is the one to reuse here, and the costed fixes below follow it.

## Source spot-check (S1)

**Zero mismatches. S1 passes.** Every figure and every causal direction traced to `briefs/public/2026-08-24.md`.

| Script | Brief | Match |
|---|---|---|
| Nifty fifty 24,219, down 0.14% | 24,219.05, −0.14% | ✓ |
| 302 rose, 400 fell, of 705 | 302 / 400 / 705 | ✓ |
| Second straight session of more fallers than risers | "second consecutive session of negative breadth under a flat headline" | ✓ |
| Window closes 31 Aug not 30 Sep; seven days on Monday | "closes on 31 August rather than 30 September, and Monday left seven days of it" | ✓ |
| Date moved forward on the 14th | "brought the date forward on 14 August" | ✓ |
| Saturday release, US$72.85bn | "release on Saturday 22 August… US$72.85 billion" | ✓ figure; see scope note in Declared cut 1 |
| FAQ still shows the retired 30 Sep date | brief, Lead sourcing note | ✓ |
| Reserves up almost US$10bn, week to the 14th, third straight build | US$9.905bn to US$716.907bn, week to 14 Aug, third consecutive | ✓ |
| House price index annual growth 3.6% from 4.5%, below the inflation path, falling in real money | 3.6% from 4.5%, "below the bank's own projected inflation path… falling in real money" | ✓ |
| Ratnamani +14.55%, orders ~₹2,700 crore, filed intraday, buyer unnamed, partly sub-contracted | +14.55%, US$286mn ≈ ₹2,700 crore, filed 14:13, "International Customers", partly sub-contracted | ✓ |
| B-L-S down almost 11%, biggest fall | −10.98%, largest fall in the 705-name universe | ✓ |
| Spanish court, Algiers consulate, document-handling role, denial filed intraday | Spain's National Court, Algiers, "administrative and document-processing role", denial filed 13:04 | ✓ |
| Five of the twelve movers unexplained | "Five of the twelve" | ✓ |
| I-D-B-I +6.92%, nothing filed, PSU banks led the market lower | +6.92% to ₹87.93, "no exchange filing dated Monday", Nifty PSU Bank −0.93% | ✓ |
| Brent −1.81%; Indian Oil +1.91%; sanctions landed after the close | −1.81%; IOC +1.91%; 17:30–19:00 IST, after the 15:30 close | ✓ |
| Deposit window shuts Monday 31 August | What to Watch, 31 August | ✓ |

Three notes, none of them mismatches:

1. **Hedges correctly honoured by omission.** The brief adopts the Asian direction but explicitly refuses the magnitudes ("we adopt the direction… and not the magnitudes, which we could not verify"). The script gives Korea's direction and no number. That is exactly right.
2. **One hedge is stronger in the script than in the brief.** "Or whether it is accused at all" goes further than the brief's "not enough to characterise the legal exposure." A hedge added, not removed — credit where due, and it is the line that saves the B-L-S block.
3. **"Nobody knows, and that is the accurate answer" is brief-verbatim** (The Connections: "'Nobody knows' is the accurate answer, and it is a better one than something plausible"). The overclaim originates upstream, not with the script writer. It still warrants the audio fix, because the brief carries a table showing "searched 3 lanes" and a dead block-deal feed in the same eyeful, and audio carries none of that context.

## Punch list

### FAIL — must fix before TTS (1)

**F1 [L1, S16] — "That runs backwards to the pattern of money leaving India for North Asia's artificial intelligence trade."**

The sentence presupposes a pattern it never establishes. "The pattern" arrives with a definite article, "the artificial intelligence trade" is a desk noun, "runs backwards to" is not the idiom ("runs counter to" is), and the paragraph closes without a so-what — twenty-seven words spent and nothing concluded. The brief's own scaffolding, "this desk has flagged for weeks," was dropped in the squeeze to 699.

**Fix (+2 words), which also restores the premise as its own short sentence per the 20-August ruling:**

> For weeks now, money has been leaving India for artificial intelligence shares in North Asia. On Monday that ran backwards. Asia sold technology, Korea hardest, and India barely moved.

**Honest statement of the counterargument, since it is a close call.** The sentence does describe the pattern inline — "money leaving India for North Asia's artificial intelligence trade" is a gloss as well as an object. A listener may well extract "this is the opposite of normal" without knowing the pattern, and that is roughly the intended takeaway. If the principal reads it as adequately self-glossing, this drops to WARN and the episode ships as written. I am holding it at FAIL for three reasons: the nine-word noun phrase is doing gloss duty and object duty simultaneously, which is one nesting too many for the ear; the non-idiomatic "runs backwards to" costs a beat exactly where the listener cannot afford one; and this is the second consecutive episode in which the Asia paragraph's premise sentence was cut to pay the word ceiling, having already been adjudicated once as load-bearing. The precedent, more than the sentence, is what decides it.

### WARN — recommended, principal may ship without (12)

**W1 [accuracy, S7] — the FCNR figure now covers more than the window described.** "Puts the money raised at seventy two point eight five billion dollars" → **"puts total inflows under the facility at seventy two point eight five billion dollars."** (+2)

**W2 [accuracy, S17] — the swap-funding hedge is gone.** "…but a build funded by that window's dollars **stops** when the window stops" → **"…would stop when the window stops."** (+1) Restores the brief's refusal to state this as cause, at a cost of one word.

**W3 [L1, S11] — "for several runs" is production vocabulary.** → **"in brief after brief"** or **"for several editions."** (−3 as written below, and this is the offset that pays for F1, W1 and W2.)

> We carried that old date in brief after brief and never went back to check it.

**W4 [L1, S12] — "It is retired now" has the wrong referent by ear**, and can be heard as "the central bank has now fixed its page," which is false. → **"We have dropped it."** (−1)

**W5 [overclaim, S31 and S34] — the flagged "Nobody knows" line.** Confirmed as an overclaim: it is a claim about the world where the defensible claim is about our search, and the spoken evidence for it is a single negative check. Two one-word fixes, no length cost:
- S31 → "Five of the twelve biggest movers have no cause **we could establish**."
- S34 → "**We could not find one**, and that is the accurate answer."

**W6 [L6, S26] — the B-L-S sentence carries every sticky noun with its hedge twenty-five words upstream.** Recommended hardening, splitting so the company clause carries its own attribution:

> Reports say a Spanish court has widened an investigation into an alleged visa fraud network at the Spanish consulate in Algiers. Those same reports say the court is now also looking at the company's document handling role.

**W7 [L1, S40] — "the American sanctions announcement" is introduced with a definite article and no referent.** The listener has never heard of it. → **"And an American sanctions announcement that much of the coverage blamed for Monday landed after our market shut."** (+3)

**W8 [L1, S14] — "more fallers than risers under a flat index" restates in desk vocabulary what the plain numbers just said.** → **"That is the second session in a row where more fell than rose."** (level)

**W9 [L1, S17] — "a build" used twice as a noun.** Covered by the W2 rewrite if that phrasing is adopted; otherwise "a third straight rise."

**W10 [L1, S19] — "below its own inflation path" has an ambiguous owner by ear.** → **"below the bank's own inflation path."** (+1)

**W11 [L2 near-miss, S21] — Ratnamani gets no what-it-does.** Downgraded from FAIL only because the company name states the business: a listener hearing "Metals and Tubes" plus "won export orders" knows enough. It is the thinnest company placement in the episode and the one place I came closest to a second FAIL — the skeptical point in S23 about margin mix asks the listener to evaluate a business they have not been told about. If a word becomes available, "the pipe maker Ratnamani Metals and Tubes" costs three and closes it.

**W12 [L1, S38] — "Brent" is unglossed.** The exemplar says "crude oil." Context carries it, barely. Optional: "and Brent crude fell one point eight one percent." (+1)

### Word budget

F1 +2, W1 +2, W2 +1, W7 +3, W10 +1 = **+9**. W3 −3 and W4 −1 return four. The remaining five come out of sentence interiors, per the method the 20-August fix pass established — never from a connective sentence, a gloss, a guard or a causal chain. S23 offers two ("does not name the buyer" for "names the buyer only as international customers") and S24's "and here the limits matter more than the number" offers eight if the principal will spend it, though it is a good signpost and I would look elsewhere first.

### What is right, and should not be touched in the fix pass

- **Sentence 10, "And we got it wrong too."** The best line in the episode, and the sentence that makes the central-bank criticism fair rather than cheap. Do not trim the correction paragraph to pay for anything.
- **The whole B-L-S hedge architecture**, and sentence 29 in particular. It goes further than the brief and it is correctly placed.
- **The Hormuz block.** A full counter-argument with evidence, stated as cause and effect, closing on "we are not giving it one." This is exemplar-grade and is the strongest passage in the episode.
- **The day-name time convention and the absolute forward date.** Correct handling of the backfill.

