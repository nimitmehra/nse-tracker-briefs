# Verify Podcast Script — 2026-08-03

**Verdict:** **FAIL** — 4 fail-level defects, all one-line fixes. Rewrite once and re-verify before TTS. Gates the podcast only; the brief and Twitter have shipped and are untouched by this.

**Checks (counts = FLAG hits):** L1 **9** / L2 **3** / L3 **0** / L4 **2** (both overlap L1) / L5 **0** / L6 **2** / S1 **2**

**The four fail-level items:**
1. **[S1a]** "Each of those six had its own private reason" asserts a cause for JNK India, which the brief grades `cause not established` — and the script contradicts itself two sentences later.
2. **[L2]** "JNK India, down six percent while its own group rose" — the name is unglossed and "its own group" is undefined; the brief's own word, *capital-goods*, was dropped.
3. **[L1]** "this ninety basis point gap" — the episode's central number stated in a unit never defined for the listener, with "the second widest since twenty ten" left dangling two clauses from its noun.
4. **[L1]** "The market bought the claimed half" — does not parse on one hearing; "bought" reads as a purchase inside an oil paragraph.

**This is a good script with localised jargon leakage, not a bad one.** The spine is strong, the auction mechanism is explained in genuinely plain English, the oil transmission is exemplar-grade, the time discipline is perfect, and the honesty beat is the best thing in it. Four sentences let it down and all four are single-line repairs.

_Cold-read discipline: the per-sentence ledger below was built with `briefs/public/2026-08-03.md` withheld. The brief was opened only after the ledger was complete, for the S1 source spot-check._

## Per-sentence ledger

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK

**Lead — the two indices**
4. "The market went up today, and the two numbers everybody quotes disagreed about by how much." — FLAG (L6: "disagreed about by how much" stacks two prepositions and stops short of its object. On one hearing the ear waits for a noun that never arrives. Fix: "…disagreed about how much.")
5. "The Sensex rose zero point seven zero percent." — OK
6. "The Nifty rose one point six zero percent." — OK
7. "And neither is wrong." — OK (strong, and it is the correct framing)

**The mechanism**
8. "Here is why." — OK
9. "The way India's closing prices are worked out changed this morning." — OK — plain, no jargon, exemplar-grade
10. "Until Friday, a stock's close was an average of the last half hour of trading." — OK
11. "From today, for stocks with futures contracts, it comes out of a single auction between quarter past three and half past three." — OK (one short nested clause, still one breath)
12. "On day one, some participants bid above the going price in a few heavyweight Nifty names, and that alone can lift an index close." — FLAG (L1: "names" is desk-shorthand for stocks. Fix: "in a few of the biggest companies in the Nifty".)
13. "So this ninety basis point gap is day-one plumbing, not a signal, and the second widest since twenty ten." — **FLAG (L1, fail-level)**: three separate defects in the episode's single most important sentence. (a) "basis point" is never defined anywhere in the script — the listener has just been given zero point seven zero and one point six zero in *percent*, and is now asked to convert to a unit they do not know; (b) "day-one plumbing" is a metaphor doing the work of the mechanism — tolerable on its own, since the mechanism was just explained in full; (c) "and the second widest since twenty ten" dangles — second widest *what*, and it is separated from its noun ("gap") by two intervening clauses, so on one hearing it attaches to "signal".

**Breadth**
14. "So how much did the market rise?" — OK
15. "The honest answer is the breadth." — FLAG (L1, mild: "breadth" is trade vocabulary landing one sentence before it is defined. Fix: "The honest answer is how many stocks actually rose.")
16. "Of six hundred and eighty stocks we track, five hundred and thirty-four rose and one hundred and forty-four fell." — OK
17. "The typical stock gained one point three five percent." — OK — correct plain-English rendering of a median
18. "The Nifty closed at twenty-four thousand seven hundred and seventy-four." — OK. Long but speakable and single-thread; the exemplar does exactly this with "twenty-three thousand four hundred and sixteen". No stumble risk.
19. "Technology was the strongest part of the board, up three point three percent, with no cause anyone could date to today." — FLAG (L1, mild: "the board" is desk-shorthand, in the same family as "the tape". Fix: "the strongest sector".) The "no cause anyone could date to today" half is honest and lands.

**VIX**
20. "India VIX, the fear gauge, rose one point four percent to eleven point nine three, on a rising market two days before a rate decision." — OK (26 words, single-thread, gloss placed on mention)
21. "Fear was bid up on an up day." — FLAG (L1 + L4: "bid up" is trader usage, and the sentence only restates sentence 20 without the so-what. The exemplar's VIX beat earns its place by explaining the oddity: "Normally fear rises into a big decision; today it fell." This one asserts an oddity and never says why it is odd.)

**Oil**
22. "What lifted the market was oil." — OK
23. "Brent fell seven point three percent over the weekend, from ninety dollars and twelve cents on Friday to eighty-three dollars and fifty-four cents a barrel." — OK
24. "OPEC plus agreed a September output increase on Sunday, and Donald Trump called off a planned strike on Iran." — OK
25. "India buys about eighty-five percent of the oil it burns, so a fall that size is money that stays in the country." — OK — textbook cause → effect → so-what

**The contested half**
26. "Be careful with half of that story." — OK (cryptic for one beat, resolved immediately)
27. "The called-off strike is confirmed." — OK
28. "A deal is not." — OK — elliptical but it lands
29. "Iran's foreign ministry said today that there are no negotiations with the United States." — OK — the denial travels with the claim, correctly
30. "And the Strait of Hormuz is still restricted, with ships needing Iranian permission to pass." — FLAG (L2-adjacent: Hormuz is never placed. The listener is not told it is the narrow shipping lane that carries much of the world's oil, so the sentence is a fact about a name they do not hold. The exemplar glosses it in the same breath.)
31. "The market bought the claimed half." — **FLAG (L1, fail-level)**: see ruling below.

**Movers — Zee**
32. "Now the movers." — OK
33. "The biggest fall was Zee Entertainment, down more than fourteen percent." — FLAG (L2, mild: no what-it-does. Muthoot gets "the gold lender" and Urban Company gets "the home services app"; Zee gets nothing, and unlike the exemplar there is no media-index context to place it either.)
34. "The regulator, SEBI, issued a final order on Friday." — OK — "the regulator" placed before the acronym is exactly right
35. "It bars the company from the market for two months, and its two promoters for a year each, over an unauthorised pledge of company land in twenty sixteen." — OK (28 words, but a single thread with clean comma segmentation — not an L6 hit)
36. "On that same Friday, shareholders had approved a share issue to those promoters at one hundred and twenty-six rupees." — OK
37. "The stock closed today at ninety-eight." — OK — the juxtaposition does its own work

**Movers — Muthoot**
38. "Second, Muthoot Finance, the gold lender, fell over seven percent on a profit that rose forty-three percent." — OK — tension stated in one line
39. "Its lending margin fell one hundred and seventy-four basis points over the year, and profit was lower than the previous quarter." — FLAG (L1: second undefined use of "basis points". Fix: "narrowed by about one and three quarter percentage points".)
40. "That forty-three percent is flattered by a weak base." — FLAG (L1, mild: "flattered by a weak base" is analyst compression. Fix: "That forty-three percent is measured against an unusually weak quarter a year ago.")

**Movers — Urban Company**
41. "The biggest gain was Urban Company, the home services app, up almost thirteen percent on revenue up forty-four percent." — OK
42. "It is still loss-making." — OK (two sentences rather than the exemplar's three; the why-it-matters is implied rather than said, which is acceptable at this word count)

**The wedge**
43. "Here is what struck me about today." — OK
44. "Five hundred and thirty-four stocks rose, and only six fell five percent or more." — OK
45. "Each of those six had its own private reason, a regulator's order, a set of results, a margin." — OK (bare apposition, but it reads as a list on the ear)
46. "None was about the market." — OK — the point of the whole wedge, cleanly made
47. "But five of the ten biggest gainers have no explanation anyone could establish, and neither does JNK India, down six percent while its own group rose." — **FLAG (L2, fail-level)**: an unexplained name, twice over. JNK India gets no what-it-does, and "its own group" is undefined — a listener cannot tell whether that means its sector, its index, or its parent company. The sentence's *function* survives; its specifics are dead air.
48. "Nobody can tell you why those moved, and anyone who says otherwise is guessing." — OK — see ruling below

**What to watch**
49. "Now, what to watch." — OK
50. "Wednesday brings the Reserve Bank of India's rate decision." — OK — L3 clean, a not-yet-happened event named for its own day
51. "The repo rate has been held at five point two five percent for three meetings and economists expect no change." — OK ("repo rate" is carried by "rate decision" one sentence earlier)
52. "So the language and the inflation forecast matter more than the number." — FLAG (L1, mild: *whose* language. The exemplar says "the Governor's language". Fix: "the Governor's language".)
53. "Tomorrow, watch whether that index gap narrows." — OK — correct evening-model time word, and a good callback to the lead

**Close**
54. "That's your brief." — OK
55. "Before I sign off: this has been general market commentary, not investment advice." — OK
56. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
57. "Markets are risky; you may lose money; act with care." — OK
58. "See you tomorrow." — OK

**L3 (time discipline) — clean across the whole script.** The covered session is "today" throughout; Iran's denial is "today"; RBI is "Wednesday"; the gap-watch is "tomorrow". No morning-model residue, no not-yet-happened event framed as having happened. Zero L3 flags.

**Compliance — clean.** No recommendation, no price target, no broker rating, no ratings language anywhere in the body. The standing firebreak (sentences 55-57) is present, verbatim, and intact at the close.

## TTS mechanics (machine-confirmed)

Re-ran the machine check independently on the spoken body (post-SAY-strip). **Confirmed, no re-litigation:**

| Check | Result |
|---|---|
| Narrated words | 699 — inside the 500–700 band, at its ceiling |
| Digits | 0 |
| `₹` / `$` / `%` | 0 |
| Em-dashes / en-dashes | 0 |
| Longest sentence | 28 words, single-thread (sentence 35) — no L6 hit |
| SAY hints | 7 — India VIX, OPEC plus, Hormuz, SEBI, Muthoot, JNK India, RBI |

**Are the spelled-out numbers listenable?** Yes. The two candidates for a stumble are "twenty-four thousand seven hundred and seventy-four" and "one hundred and seventy-four basis points". The first is fine — the exemplar reads an index level the same way and a human reader takes it in one breath. The second is not a *reading* problem but a *comprehension* problem (see the basis-point flag). Nothing else in the body requires the reader to slow down or re-take.

**The SAY hints do not reach the audio engine — machine-verified.** `hive-mind/scripts/tts-podcast-nse.py:100` is `strip_say_hints()`, which *deletes* the bracket and its contents ("Sarvam doesn't use them"). There is no substitution dictionary anywhere in the script. So all seven hints are documentation of intent only; they change nothing about what is spoken. Consequences:

- **"JNK India" is the live risk.** With the hint stripped, Sarvam receives the bare string `JNK` and will most likely voice it as a word — "junk India". That is an on-air error in the principal's voice. If the name stays in the script, it must be respelled **in the body** (e.g. "J N K India").
- **"toroIQ" has no hint at all** and is the brand, in sentence 2 of every episode. Worth a one-time decision on how it should be respelled in the body, since a hint cannot fix it.
- "Hormuz", "Muthoot", "SEBI", "OPEC plus", "India VIX" carry hints that will not fire, but all five are ordinary enough that a general engine usually gets them; they are watch-items on playback, not pre-emptive rewrites.
- The `[SAY: R-B-I]` hint is attached to "the Reserve Bank of India's", where no abbreviation appears at all — it is inert twice over.

This is a pipeline observation, not a defect the writer introduced. **The operational rule it implies: anything a TTS engine would genuinely mangle has to be respelled in the spoken body, because the hint is thrown away.**

## Rulings requested by the writer

### 1. "The market bought the claimed half." — **CUT IT.** Too clever; it does not parse on one hearing.

Two independent failures, and they compound. First, "bought" is being used in the believed-it sense, but the sentence sits at the end of an *oil* paragraph, four sentences after "Brent fell" and "India buys about eighty-five percent of the oil it burns". The purchase reading is primed and arrives first. Second, "the claimed half" is a back-reference to "half of that story" five sentences earlier, which itself was never named — the listener has to hold an unlabelled abstraction across a paragraph and then match it to a second abstraction. Even a listener who lands both halves lands them a beat late, and by then the script has moved on to the movers.

The judgement itself is right and worth keeping. Say it: **"So the market priced in a deal that has not been agreed."** One hearing, no back-reference, same conclusion, and it cannot be misread as a verdict on the diplomacy because the object is the market's behaviour, not Iran's or Trump's.

### 2. "Nobody can tell you why those moved, and anyone who says otherwise is guessing." — **KEEP IT VERBATIM.** Candour, not abdication.

This would be an abdication if it appeared early, or if it were the script's only posture. It appears at sentence 48, after the script has explained the auction mechanism in four sentences, the oil move with its transmission to India, Zee's regulatory order in five, Muthoot's margin, and Urban Company's revenue. The listener has just been given six causes in a row. Against that record, refusing a seventh reads as the same discipline applied honestly, not as a shrug — and the second clause ("anyone who says otherwise is guessing") is what converts it from a gap into a claim. It is the most trust-building line in the episode and it is doing the editorial thesis's work.

One caveat: it currently rests on sentence 47, which is the script's weakest sentence (see the JNK flag). Fix 47 and this line lands harder.

### 3. Dropping the EM-divergence beat rather than faking it — **RIGHT CALL, and the right reason.**

The stated reason is that the global inputs came back stale, Tuesday-stamped, or blocked, and that writing the beat anyway would be independent reporting. That is correct on both counts: a divergence claim is a *comparative* claim, and a comparison built from readings the desk could not date is a fabrication with a decimal point on it. Dropping it costs the episode nothing structurally — the crude paragraph already carries a genuine upstream global input, and at 699 narrated words the script is at the ceiling of its band, so the beat had nowhere to go anyway. Restoring it would have required cutting something verified to make room for something unverified.

The deviation is disclosed in the composition note, which is the standard being met. No action.

## Punch list

### Must fix before TTS (the four that make this a FAIL)

- **[S1a, sentence 45] The script says all six big fallers had a reason, then says one of them did not.** The brief grades JNK India `cause not established`. Rewrite: *"Five of those six had a private reason of its own, a regulator's order, a set of results, a margin. None was about the market."* This also sets up sentence 47 instead of colliding with it.
- **[L2, sentence 47] "JNK India, down six percent while its own group rose" — an unexplained name and an undefined group.** The listener is told neither what the company does nor what "its own group" means. The brief has the missing word: it is the **capital-goods** group. Rewrite: *"…and neither does JNK India, an industrial equipment maker, which fell six percent while the rest of its engineering sector rose."*
- **[L1, sentence 13] "ninety basis point gap" — the episode's central number in a unit the listener does not know**, and *"the second widest since twenty ten"* left dangling two clauses from its noun. Split it: *"So that gap, nine tenths of one percent, is day-one plumbing and not a signal. It is the second widest gap between the two indices since twenty ten."* (Same fix needed at sentence 39: "one hundred and seventy-four basis points" → *"about one and three quarter percentage points"*.)
- **[L1, sentence 31] "The market bought the claimed half" — cut.** Replace with *"So the market priced in a deal that has not been agreed."* Full reasoning in the ruling above.

### Should fix — cheap, and each one removes a stumble

- **[S1b, sentence 12]** Add the brief's hedge: *"Brokers say some participants bid above the going price in a few of the biggest companies in the Nifty."* This fixes the certainty upgrade and the "names" shorthand in one edit.
- **[L1, sentence 21] "Fear was bid up on an up day"** asserts an oddity without saying why it is odd, and "bid up" is trader usage. The exemplar's version of this beat earns its place by explaining: *"Normally fear falls when the market rises. Two days before a rate decision, it did the opposite."*
- **[L2, sentence 30] Place Hormuz on mention:** *"the Strait of Hormuz, the narrow lane that carries much of the world's oil, is still restricted."*
- **[L2, sentence 33] Give Zee its one-line what-it-does:** *"Zee Entertainment, the television broadcaster, down more than fourteen percent."*
- **[L1, sentence 19] "the strongest part of the board"** → *"the strongest sector"*.
- **[L1, sentence 15] "The honest answer is the breadth"** → *"The honest answer is how many stocks actually rose."*
- **[L1, sentence 40] "flattered by a weak base"** → *"measured against an unusually weak quarter a year ago."*
- **[L6, sentence 4] "disagreed about by how much"** → *"disagreed about how much."*
- **[L1, sentence 52] "the language"** → *"the Governor's language"* (as the exemplar has it).

### Watch on playback, not a rewrite

- **"JNK India" will probably be voiced as "junk India."** The `[SAY: J-N-K India]` hint is deleted before the audio engine ever sees it (`tts-podcast-nse.py:100`). If the name survives the rewrite, respell it in the body as *"J N K India"*.
- **"toroIQ"** has no hint and cannot be fixed by one. Worth a standing decision on how it should be spelled in the body, since it opens every episode.

### Word budget

The body is at **699 of a ~700 ceiling**. Every fix above except the Hormuz gloss and the Zee gloss is either neutral or shortens the script; those two add about fifteen words. Cutting the redundant second half of sentence 21 covers it. No structural cut is needed.

## Source spot-check (S1)

Opened `briefs/public/2026-08-03.md` only at this point. **No number is wrong, no direction is reversed, and nothing is a wrong-day figure.** Every headline figure ties:

| Figure in script | Brief | Tie |
|---|---|---|
| Sensex zero point seven zero percent | +0.70% | ✅ |
| Nifty one point six zero percent | +1.60% | ✅ |
| "neither is wrong" | "neither number is wrong" | ✅ |
| ninety basis point gap, second widest since twenty ten | 90 bps, second widest since 2010 | ✅ |
| auction quarter past three to half past three | 15:15–15:30 | ✅ |
| previous method: average of the last half hour | "averaging the last thirty minutes" | ✅ |
| 534 rose / 144 fell / 680 tracked / typical stock 1.35% | identical | ✅ |
| Nifty at twenty-four thousand seven hundred and seventy-four | 24,774.30 | ✅ |
| Technology up three point three percent, no dateable cause | Nifty IT +3.28%, "no catalyst dated to Monday was established" | ✅ |
| India VIX eleven point nine three, up one point four percent | 11.93, +1.40% | ✅ |
| Brent −7.30%, ninety dollars twelve cents → eighty-three fifty-four | $83.54, −7.30% (implies $90.12 Friday — arithmetic exact) | ✅ |
| India buys about eighty-five percent of its oil | "roughly 85%" | ✅ |
| Iran's foreign ministry denial, today; strait still restricted | "said on Monday"; "passage requiring Iranian permission" | ✅ |
| Zee down more than fourteen percent; two months / one year each; 2016 land pledge; issue at 126; close at 98 | −14.33%; identical terms; ₹126; ₹98.14 | ✅ |
| Muthoot over seven percent; profit +43%; margin −174 bps; below previous quarter; weak base | −7.33%; +43%; −174 bps YoY; −16.9% QoQ; "flattered by a weak year-ago base" | ✅ |
| Urban Company almost thirteen percent, revenue up forty-four, still loss-making | +12.98%, +44%, ₹92 cr loss | ✅ |
| six fell five percent or more against 534 up | identical | ✅ |
| five of the ten biggest gainers unexplained | Indo Borax, Balrampur, Pine Labs, Deep Industries, Aegis — exactly five `[cause not established]` | ✅ |
| JNK India down six percent while its own group rose | −6.10% vs capital goods +2.19% | ✅ |
| RBI Wednesday; 5.25% for three meetings; no change expected | 05-Aug; 5.25% for three meetings; polls unanimous for a hold | ✅ |

Two **grading** discrepancies, though — both cases of the script stating with more certainty than the brief allows:

**S1a — the six fallers (fail-level, and it is also an internal contradiction).** Sentence 45 says *"Each of those six had its own private reason, a regulator's order, a set of results, a margin."* The brief grades only five of the six that way; **JNK India is `[Cause not established at primary source]`** — the brief says so explicitly and calls it "the most watchable unexplained divergence of the session". So the script asserts, at cohort level, a cause the brief refused to assert. Worse, it then contradicts itself two sentences later ("neither does JNK India"). A listener paying attention hears the script say all six were explained and then, within one breath, that one of them was not. Fix: *"Five of those six had a private reason of its own, a regulator's order, a set of results, a margin. None was about the market."*

**S1b — the auction order flow (warn-level).** The script states flatly that *"some participants bid above the going price in a few heavyweight Nifty names."* The brief carries the caveat the script drops: *"That explanation comes from one brokerage official rather than from an exchange, so the mechanism is established while the specific order flow is only reported."* This is the load-bearing explanation of the entire lead, and it is currently single-sourced and unhedged in the audio. Fix costs three words: *"Brokers say some participants bid above the going price…"*

Everything else in the brief that the script chose to omit — the GST and PMI detail, the Connections beats, the late-filing timing note, CAMS, Persistent and Dhanuka — is omitted cleanly, with no residue that would mislead.
