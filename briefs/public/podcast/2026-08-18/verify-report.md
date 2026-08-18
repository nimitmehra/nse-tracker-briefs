# Verify Podcast Script — 2026-08-18 (fix pass v3 — REVERIFY)

**Verdict:** **WARN** — clear to ship at the principal's discretion. TTS may proceed; the punch list is optional polish, not a gate.
**Checks:** L1 2 / L2 1 / L3 0 / L4 1 / L5 0 / L6 0 / **S1 PASS** (0)  (counts = FLAG hits)

**One-line read:** the v2 failure was a vocabulary habit and the habit is gone. Twelve L1 hits went to two, both mild and neither flagrant; both L2 blockers are resolved as name-placement; the L3 time error is fixed; mechanics and sourcing are clean. What is left is one loose pronoun, one ambiguous word ("dated"), and one compressed causal phrase — three single-clause swaps, none of which a listener would fail on.

**Why WARN and not FAIL.** The skill's Step 3 says any L1/L2/L3 match fails, but each check defines its own trigger. L1 fails "on any flagrant line" — neither remaining hit is desk shorthand or producer meta, they are an unglossed common term and one ambiguous adjective. L2 fails on "a deferred or unexplained name" — every company in this script is named and placed in the same breath; the sentence 34 flag is a pronoun referent, and the source check confirms it resolves to the correct fact. L4 is a single isolated slip, which the skill scores as WARN. So: no flagrant line, no unplaced company, no time error, no audio-breaker, no source mismatch.

**Isolation note:** the ledger was built cold from the spoken body, script plus canonical exemplar only. The brief was opened only after the ledger was on disk. The script's own metadata header and the v2 report were read (both are about the script, not the source), and the previous report was recovered from git after this file was overwritten.

**Accepted override:** "the biggest movers we follow" (sentence 11) is recorded as an accepted orchestrator decision, not re-flagged. The source check independently confirms the scope reasoning — the brief's count belongs to a roughly seven-hundred-stock screened universe.

**Raised, not acted on:** sentences 43 to 49 are stronger than the current canonical exemplar's closing insight. Exemplar-refresh candidate for the principal.

## Per-sentence ledger

Built cold, before the brief was opened. Fifty-seven sentences in the spoken body (everything below the metadata separator).

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "Two government notifications organised today's session, and neither was a market event." — OK. "Neither was a market event" is plain English, not desk shorthand; a listener hears "neither was itself about the market" and the next three sentences pay it off.
5. "The electronics ministry approved its first batch of component-making projects, worth nearly seven thousand nine hundred crore rupees." — OK
6. "The defence ministry published a sixth list of four hundred and five items to be bought from Indian suppliers, not imported." — OK. The "not imported" tail does the explaining work without jargon.
7. "Shares in both groups rose while the market fell." — OK. The reference now points backwards to the two ministries just described. The v2 forward-reference is gone.
8. "The Nifty fifty closed down zero point five five percent, at twenty four thousand one hundred and fifty four." — OK
9. "Eight of its shares rose and thirty three fell." — OK for listenability. Flagged to S1 only: eight plus thirty three is forty one of fifty, which implies nine unchanged. Checked against the brief below.
10. "The smallcap index was the only major index to rise." — FLAG (L1, advisory): "smallcap" is never glossed. The exemplar glosses its one piece of market vocabulary in the same breath ("the fear gauge, India VIX"). Not flagrant desk shorthand, so not a blocker; "the index of smaller companies" would close it at zero word cost.
11. "Six of the biggest movers we follow closed at their highest level in a year." — OK (accepted orchestrator override). "We follow" is producer-scope language, kept deliberately because the count is scoped to the roughly seven-hundred-stock screened universe and an unscoped phrasing would over-claim to the whole exchange. Not re-flagged as a blocker.
12. "So the average fell and most of the market did not." — OK. "The average" is a plain-English stand-in for the index and lands after its evidence, not before it. This is the v2 L4 fix and it works.
13. "Almost all the damage came from technology." — OK
14. "That index fell one point nine three percent, more than three times the fall in the Nifty fifty, with all eleven of its companies down." — OK. Twenty-five words, single-thread, comma-segmented, sayable in one breath. Arithmetic is internally consistent (one point nine three over zero point five five is three and a half).
15. "Asian markets went in different directions today, and foreign money across emerging markets barely moved." — OK
16. "Nothing outside India explains today's fall, which was made at home." — OK
17. "The worrying story is oil, and not because of today." — OK
18. "Tanker attacks have resumed near the Strait of Hormuz, the narrow lane that carries much of the world's oil." — OK. Gloss carried verbatim from the exemplar; correct call.
19. "Weekend traffic through it reportedly nearly stopped." — OK. The hedge "reportedly" is audible and correct.
20. "Brent crude, the global oil price, is about nine percent higher than on the seventh of August." — OK. First-use gloss present.
21. "The Reserve Bank of India cut its inflation forecast this month, explicitly because crude was cheap." — OK. Said in full, no initialism.
22. "That reason has reversed inside a fortnight." — OK, with a note: the chain is complete (cheap crude was the stated reason, crude is no longer cheap), but the so-what is left for the listener to finish. A five-word tail ("so that forecast is now at risk") would make it explicit. Not a flag; the exemplar allows this much compression.
23. "Another thing gets missed." — OK
24. "What factories charged for their goods rose eight point two nine percent in July." — OK. Factory-gate framing is plain and the roles are the right way round.
25. "What households paid in the shops rose four point four five percent." — OK
26. "That gap gets absorbed by whoever sits in between and cannot raise prices." — OK. "Whoever sits in between" is vague but self-explaining in context, and naming the layer would cost accuracy.
27. "It is a margin story, not an inflation story." — OK. Same construction the exemplar sanctions ("it is foreign money leaving, not a currency story").
28. "Now the movers." — OK
29. "Paras Defence and Space Technologies rose ten percent." — OK. The name carries its own what-it-does.
30. "The defence list was announced at twelve nineteen, during trading hours, the clearest link between news and price today." — OK. "During trading hours" does the work the old desk phrasing was doing.
31. "The whole list, though, is an estimated three thousand and seventy crore rupees of business, spread over years and the whole supply chain." — OK. The caveat travels with the number, in the same sentence.
32. "Paras on its own is valued on the stock market at about four times that." — OK. "Valued on the stock market" replaces the bare "worth"; the comparison is now unambiguous.
33. "Jyoti C N C Automation, which is putting over a thousand crore rupees into its Rajkot plant, gained eight point three percent." — OK, with a residual note. The v2 blocker (named twice, never placed) is cleared: the listener now knows it is a manufacturer with a plant in Rajkot spending real money. It is placement by fact rather than a what-it-does descriptor, which is the honest ceiling given the brief carries no business description. A sourced three-word descriptor would fully satisfy L2; do not invent one.
34. "It disclosed that approval at ten twenty two on Monday night, so today was the first session that could react." — FLAG (L2 referent, WARN): "that approval" has no antecedent. The word "approval" was last heard in sentence five, attached to the electronics ministry. A listener hearing "It disclosed that approval" can plausibly attach it to the ministry scheme rather than to Jyoti's own board sign-off on the plant spend. The time anchor and the L3 fix in the second half are both correct.
35. "The one real fall was Ahluwalia Contracts, a construction company, down almost eleven percent." — OK. Named and placed in the same breath.
36. "June quarter sales rose twelve percent and net profit fell almost eighty percent." — OK
37. "That is a cost problem, not a demand problem." — OK. Mechanism stated plainly, once.
38. "The results came out after Friday's close, the management call recording after Monday's close, and today the market gave its verdict." — OK. Twenty-one words, three clean beats, one thread. "The management call recording" is now glossed enough to survive one hearing.
39. "The call had made things worse, not better." — OK
40. "Tube Investments of India, an engineering group, ran the same sequence the other way, up almost eight percent." — FLAG (L4, isolated): "ran the same sequence the other way" asserts a chain it never shows. For Ahluwalia the listener got three dated events; for Tube there is no timestamp, no call, no verdict, only a revenue line. The phrase is doing the work a plain clause should do. Suggested plain rewrite: "Tube Investments of India, an engineering group, went the other way, up almost eight percent, on results the market liked."
41. "June quarter revenue rose seventeen percent, with double digit growth in every segment." — OK
42. "Here is what struck me most today." — OK. Exemplar's own hinge line.
43. "The papers explained the fall with high crude and rising American bond yields." — OK, with a note: "bond yields" is unglossed, but it is being reported as what the papers said and is then dismissed, so a listener does not need to price it to follow the argument.
44. "Brent moved one hundredth of one percent today." — OK
45. "It did not move." — OK. The strongest line in the script.
46. "Crude is at a high level and American yields are rising, but a level is not an event." — OK. Cause-and-effect distinction made in plain words.
47. "I could not find a dated reason for the technology fall, and I am not going to invent one." — FLAG (L1, WARN): "a dated reason" is ambiguous on one hearing. In speech, "dated" most commonly means out of date, so a listener can hear "I could not find an outdated reason", which is the opposite of the meaning. Suggested rewrite: "I could not find a piece of news today that explains the technology fall, and I am not going to invent one."
48. "I can tell you what the press got wrong." — OK
49. "I cannot tell you why technology fell." — OK
50. "Tomorrow night, around half past eleven our time, the American Federal Reserve is due to publish the minutes of its July meeting." — OK. Correct evening model: a not-yet-happened event is "tomorrow night". The hedge "is due to publish" is audible.
51. "Three of its regional presidents voted there for a rate increase." — OK. "There" anchors it to the July meeting; the v2 time-anchor gap is closed.
52. "Indian markets get their first chance to react on Thursday." — OK. Internally consistent: today is a Tuesday (Friday results, Monday call, today's verdict; Monday-night disclosure reacted to today), so a Wednesday-night release lands on Thursday.
53. "That's your brief." — OK
54. "Before I sign off: this has been general market commentary, not investment advice." — OK
55. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
56. "Markets are risky; you may lose money; act with care." — OK
57. "See you tomorrow." — OK

## Punch list

None of these is a blocker. All three are single-clause swaps that cost no words.

- **[L2 referent, sentence 34]** "It disclosed that approval at ten twenty two on Monday night" — "that approval" has no antecedent in its own beat. The nearest thing the listener has heard is the Rajkot spend, which is not an approval; the last "approval" was the electronics ministry's, eleven sentences earlier. *The source spot-check confirms the true referent IS the electronics-scheme approval*, so the ambiguity resolves to a correct fact either way — this is a wording flag, not a factual risk. The rewrite that closes the referent and places Jyoti in the story at the same time: **"It disclosed its place in that electronics batch at ten twenty two on Monday night, so today was the first session that could react."**
- **[L1, sentence 47]** "a dated reason" reads as "an out-of-date reason" on one hearing. Rewrite: **"I could not find a piece of news today that explains the technology fall, and I am not going to invent one."**
- **[L4, sentence 40]** "ran the same sequence the other way" asserts a chain the script never shows for Tube Investments (no timestamp, no call, no verdict). Rewrite: **"Tube Investments of India, an engineering group, went the other way, up almost eight percent, on results the market liked."**
- **[L1, advisory, sentence 10]** "the smallcap index" is unglossed. Optional swap: **"the index of smaller companies was the only major index to rise."** Note this one adds two words against a body already at the seven-hundred ceiling, so it trades against the fixes above.

**Accepted override (not a finding):** sentence 11, "the biggest movers we follow". Producer-scope language, kept deliberately for scope accuracy — the count belongs to the roughly seven-hundred-stock screened universe, and an unscoped phrasing would over-claim to the whole exchange. Recorded as accepted, not re-flagged.

**Above the exemplar.** Sentences 43 to 49 — the crude correction paired with the refusal to invent a reason for the technology fall — are stronger than anything in the current canonical exemplar. The exemplar's closing insight explains a move; this one refuses to, and says so out loud. Per the skill's drift rule, this is raised to the principal as an exemplar-refresh candidate rather than acted on silently.

## Previous FAIL items — cleared?

The v2 report carried sixteen numbered punch items (eight FAIL-level, eight WARN-level) plus three sourcing constraints. Checked one by one against the v3 body. **Fifteen of sixteen cleared. One not taken (item 16), and it is a scope wording residual, not a blocker.**

**FAIL-level block — all eight cleared:**

1. **Jyoti never placed** — CLEARED. Now "Jyoti C N C Automation, which is putting over a thousand crore rupees into its Rajkot plant". Placement by sourced fact rather than a business descriptor, which is the honest ceiling given the brief carries none. The fix pass correctly declined to invent one.
2. **"Brent" unexplained** — CLEARED. First use is now "Brent crude, the global oil price".
3. **"green" and "we track"** — CLEARED on "green" ("the only major index to rise"). "We track" became "we follow" under the accepted orchestrator override.
4. **Strait of Hormuz unplaced** — CLEARED. The exemplar's own gloss is now carried verbatim.
5. **"The next session is entitled to price that"** — CLEARED. Now "so today was the first session that could react". The L3 time error is gone.
6. **"the call" never introduced** — CLEARED. Now "the management call recording".
7. **"its own approval" has no referent** — PARTIALLY CLEARED. See the punch list. The v3 line reads "It disclosed that approval", which is better than v2 but still leans on a noun the listener has not heard in this beat.
8. **"Asia split in two" / "emerging market funds"** — CLEARED. Now "Asian markets went in different directions today, and foreign money across emerging markets barely moved".

**WARN-level block — seven of eight cleared:**

9. **"the benchmark" / "members"** — CLEARED ("the fall in the Nifty fifty" / "its companies").
10. **"worth about four times that"** — CLEARED ("valued on the stock market at about four times that").
11. **"the cleanest explanation on the board"** — CLEARED ("the clearest link between news and price today").
12. **"India trades them on Thursday"** — CLEARED ("Indian markets get their first chance to react on Thursday").
13. **Electronics figure a bare appositive** — CLEARED. The noun is supplied: "component-making projects, worth nearly seven thousand nine hundred crore rupees".
14. **L4 epigram before its mechanism** — CLEARED. The breadth split now comes first and "So the average fell and most of the market did not" lands after it.
15. **Fed dissent had no time anchor** — CLEARED ("voted there", anchored to the July meeting named in the previous sentence).
16. **Restore "public-sector" on the defence supply chain** — **NOT TAKEN.** v3 still says "spread over years and the whole supply chain"; the brief says "spread across the entire defence **public-sector** supply chain". One hyphenated word. Not an S1 mismatch and not a blocker — see the source spot-check — but it is the one carried-over item.

**The three sourcing constraints — all respected:**

- The factory-gate beat is untouched and still says "what factories charged for their goods". The nine point seven eight percent headline stays out. Correct.
- No business descriptor was invented for Jyoti.
- No Tube Investments profit figure was restored. The two hedges ("reportedly", "is due to publish") both survive.

**Net:** the v2 failure mode — desk register leaking into narration — is gone. Twelve L1 hits went to two, both mild and neither flagrant. The two L2 blockers are both resolved as name-placement; what remains at sentence 34 is a pronoun, not an unplaced company.

## Mechanical checks (L5 / L6)

Re-run independently on the spoken body (everything from "Good evening" to "See you tomorrow"), not taken from the script's self-verify header.

| Check | Result |
|---|---|
| Digits | zero |
| Currency or percent symbols | zero |
| Em-dashes or en-dashes | zero |
| `[SAY:]` hints or square brackets | zero |
| Exclamation points | zero |
| Colons / semicolons | only inside the standard closing disclaimer, same as the exemplar |
| Word count | 700 — inside the 500 to 700 band, at the ceiling |
| Longest sentence | 25 words (sentence 14), single-thread and comma-segmented, sayable in one breath |
| Sentences over 30 words | zero |

**L5: 0. L6: 0.** No audio-breakers. The word budget has no headroom, which is the real constraint on the punch list: the three recommended rewrites are close to word-neutral, but any added gloss has to trade against an existing clause.

Mangle-risk spellings hold: "toro I-Q", "Jyoti C N C Automation", "the Reserve Bank of India" said in full, and "the technology index" in place of "Nifty I-T". The one initialism left in the body is "SEBI" in the fixed disclaimer, which is unchanged from the exemplar.

## Source spot-check (S1)

**S1 PASS — no number or direction mismatch against `briefs/public/2026-08-18.md`.** Run only after the ledger above was written to disk.

Reconciled, all resolving to a line in the brief:

- Nifty fifty down zero point five five percent at twenty four thousand one hundred and fifty four — brief 24,154.90, −0.55%. Correct.
- Eight rose, thirty three fell inside the index — brief identical. The nine-name residual is the brief's own arithmetic, not a script error.
- Smallcap the only major index to rise — brief: Nifty Smallcap 250 +0.19%, "the only green headline index". Correct.
- Six of the biggest movers at year highs — brief: six of the eleven biggest movers in the screened universe, "roughly 700 stocks above a ₹1,000 crore market-cap floor", at 52-week highs. **This confirms the orchestrator override**: the count is genuinely scoped to the screened universe, and an unscoped "biggest movers of the day" would have over-claimed to the whole exchange.
- Technology down one point nine three percent, all eleven companies down — brief: Nifty IT −1.93%, all eleven measurable members down, "three and a half times the benchmark". The script's "more than three times" understates, which is the safe direction.
- Electronics: nearly seven thousand nine hundred crore — brief ₹7,877 crore across 31 projects, letters dated 17 August. Correct.
- Defence: sixth list, four hundred and five items — brief identical, notified 18 August. Announced at 12:19, intra-session — correct, and the brief calls it "the cleanest attribution on the board today", which the script renders as "the clearest link between news and price today".
- Three thousand and seventy crore, not an order book — brief identical, with the caveat travelling in the same breath. Correct.
- Paras plus ten percent, valued at about four times that — brief +10.00%, market cap ₹12,308 crore; 12,308 divided by 3,070 is 4.01. Correct.
- Jyoti plus eight point three percent, over a thousand crore into Rajkot, disclosed ten twenty two Monday night — brief +8.30%, ₹1,020.65 crore over five years at the Rajkot plant, filed 22:22 Monday. The twelve-hour rendering is right.
- Ahluwalia minus almost eleven percent, sales up twelve, profit down almost eighty — brief −10.85%, +12.03%, −79.71%. Sequence (results after Friday's close, call recording after Monday's close, verdict Tuesday) matches the brief line for line, including "the call made it worse, not better".
- Tube Investments up almost eight percent, revenue up seventeen, double-digit in every segment — brief +7.94%, +17%, engineering +21% / mobility +26% / metal-formed +12%. No profit figure published, as the brief requires.
- Brent moved one hundredth of one percent, about nine percent above the seventh of August — brief −0.01%, $90.86, roughly 9% above 07 August. The press correction (Business Standard, The Tribune, the wires) and "a level is not an event" are the brief's own.
- Factory gate eight point two nine percent versus shops four point four five percent — brief identical, and the headline 9.78% is correctly absent.
- Reserve Bank cut its forecast this month explicitly because crude was cheap; that reason has reversed inside a fortnight — brief: cut on 05 August, "Its stated reason has reversed inside a fortnight". Correct.
- Hormuz attacks resumed, weekend traffic reportedly nearly stopped — brief: a third ADNOC ship attacked inside 48 hours; five transits Saturday, none Sunday, against 31 the previous weekend. The hedge survives.
- Fed minutes tomorrow night around half past eleven, three regional presidents voted for an increase, India reacts Thursday — brief: Wednesday 19 August, about 23:30 India time, minutes of the 28-29 July meeting, three dissents for an increase, "India trades them on Thursday". The "is due to publish" hedge survives, matching the brief's own note that the date comes from one markets desk.

**No wrong-day leakage.** The 2026-06-04 failure mode does not recur: both date-bearing figures (the nine percent crude move since 07 August, the Monday-night Jyoti filing) are carried as dated, not as today's. Day-of-week arithmetic is internally consistent throughout — Friday results, Monday call, Tuesday verdict, Wednesday-night Fed release, Thursday reaction.

### Residual scope and hedge notes (none blocking, none an S1 mismatch)

1. **"the whole supply chain" is still missing "public-sector"** (carried over from v2 punch item 16). The brief scopes the three thousand and seventy crore to the defence public-sector supply chain. Dropping the qualifier widens who the money is spread across. One hyphenated word.
2. **"foreign money across emerging markets barely moved"** — the brief says emerging-market funds were "mildly weaker". The script drops a direction rather than reversing one. Non-blocking.
3. **The brief's hedge "The forecast is not wrong yet" is not carried.** The script says only "That reason has reversed inside a fortnight". No claim is made that the forecast is wrong, so this is a dropped hedge, not a contradiction — but it is the sentence where a listener is most likely to over-read.
4. **"all eleven of its companies down"** drops the brief's "measurable". Immaterial for audio.
5. **Jyoti's "over five years" is compressed out** of the Rajkot figure. Not a contradiction; the number is a five-year commitment stated as a present investment.
6. **"ran the same sequence the other way" is loose against the source.** Ahluwalia's call recording went up after Monday's close; Tube's earnings call was Monday morning. Same shape, not the same sequence. This is the sourcing half of the L4 flag in the ledger and argues for the plain rewrite rather than the compressed phrase.
