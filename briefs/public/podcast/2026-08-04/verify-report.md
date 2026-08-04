# Verify Podcast Script — 2026-08-04

**Verdict:** FAIL
**Checks (FLAG hits):** L1 10 / L2 2 / L3 0 / L4 3 / L5 0 / L6 4 / S1 1
**Totals:** 6 FAIL-grade defects, 8 WARN, 6 minor FLAG, across 55 sentences.

**Why FAIL, in one line:** the script's factual discipline is excellent and its compliance is intact, but six sentences do not parse on one hearing — including the hook and the oil paragraph's turn — and the skill FAILs on any flagrant L1.

Cold read performed with the brief withheld. The per-sentence ledger below was completed in full before `briefs/public/2026-08-04.md` was opened.

## TTS mechanics (machine-confirmed on the spoken body)

| Check | Result |
|---|---|
| Narrated word count | 700 — top of the 500-700 band, matches the header claim |
| Digits | zero |
| `₹` / `$` / `%` | zero |
| Em-dashes / en-dashes | zero |
| `[SAY:]` hints | zero (correct — `tts-podcast-nse.py:100` deletes them with no substitution) |
| Longest sentence | 32 words, single-thread, comma-segmented |

Respellings are correctly scoped to the standing rule — respell only where the default word-reading is wrong. `toro I-Q`, `N-S-E`, `B-S-E`, `C-G Power`, `D-L-F` are respelled; SEBI, Nifty, Sensex, Ather, Greaves, Korea, Oman, Hormuz-free body text are left alone and read correctly by default. Nothing else in the body is a mangle risk. **No L5 hits.**

Speakability of the spelled-out numbers is a separate judgment from correctness, and it is where the numbers fall down — see L6 in the ledger (sentences 9, 11, 12).

## Per-sentence ledger

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "The Reserve Bank of India decides on interest rates at ten tomorrow morning, and the number to watch is not the rate." — OK. Evening model correct: the decision is "tomorrow".
5. "It is the Bank's inflation forecast of five point one percent, built on crude oil at about ninety-five dollars a barrel." — OK
6. "Oil has traded nowhere near that all week." — **FLAG (L1: direction never stated).** "Nowhere near" does not tell a listener whether oil is above or below ninety-five. The entire lead turns on oil being *cheaper* than the Bank assumed, and the script never says so. On one hearing the listener does not know which way the gap points.
7. "But the monsoon has just moved the other way, so this is not the easy call it sounds like." — **FLAG (L1 + L4: the other way from what; the mechanism is never stated).** The listener has heard nothing about monsoon, nothing about what monsoon does to prices, and no "easy call" has been named. The chain the sentence compresses — cheaper oil argues one way, a worse monsoon argues the other, so the forecast is genuinely contested — is nowhere in the audio. This is the hook line and it does not parse cold.
8. "Indian shares fell into that decision." — OK
9. "The Nifty fifty closed down zero point six four percent, the Sensex down zero point two seven percent, and the fear gauge rose two point one eight percent to a one-week high." — **FLAG (L6: correct but not listenable).** Three two-decimal figures spelled out in one 32-word breath. "Two point one eight percent" is a mouthful that carries no more meaning than "about two percent". Spelled-out is not the same as speakable.
10. "So the market fell and fear rose together." — OK. Good, plain, and the right so-what.
11. "Two hundred and seventy-nine shares rose and three hundred and ninety-two fell, out of six hundred and eighty." — **FLAG (L6).** Three long spoken numerals back to back. A driving listener retains the shape, not the count; "roughly four hundred fell against two hundred and eighty that rose" does the same work with less friction.
12. "The two headline indices also spent most of today moving in opposite directions, on day three of India's new closing auction." — **FLAG (L1: "closing auction" is never explained).** The episode has to stand alone; a listener who did not hear the 03-August script has no idea what a closing auction is or why the market has a new one. The plumbing explanation that follows presumes the term.
13. "Turnover in that auction was fifteen hundred and forty-two crore rupees on the N-S-E against nine crore on the B-S-E, about a hundred and sixty-five to one." — **FLAG (L6).** The ratio is the point and it survives on its own; the two absolute crore figures are spoken ballast.
14. "A thin auction moves prices further, so one company can close at two different levels." — **FLAG (L4: incomplete chain).** Two different levels *on the two exchanges* — the venue is what makes the sentence make sense, and it is left implicit.
15. "That is plumbing, never a signal." — OK. Exactly the right framing.
16. "Asia was firm today and India was not." — OK
17. "Korea's main index rose one point six percent on a memory-chip deal for artificial-intelligence hardware." — OK
18. "So whatever moved India today was Indian." — OK. Clean deduction, plainly said.
19. "On the worrying side, the weather office now forecasts below-normal August rain, ninety-four percent of the long-period average." — **FLAG (L1: "long-period average" is jargon).** Ninety-four percent of what, a listener asks. "About six percent below a normal August" needs no gloss.
20. "Rain through July was one percent above normal, so this is a forecast turning rather than a shortfall." — OK. Good honest distinction.
21. "But the Bank named monsoon uncertainty when it raised that inflation forecast in June." — OK. Ties the monsoon to the rate decision without predicting anything.
22. "On the supportive side, oil, and the timestamp matters." — **FLAG (L1: producer-view meta + broken cadence).** "The timestamp matters" is the desk talking about its own methodology. Spoken aloud the clause-comma-clause construction stumbles.
23. "Crude traded near eighty-six dollars a barrel, up almost three percent, while Indian markets were open." — OK. Correctly timestamped to the session.
24. "It is the only crude number that belongs to today's session." — OK, borderline meta but it earns its place as the honesty guard.
25. "By quarter past nine tonight it was seventy-nine dollars, a round trip of about nine percent in one day." — OK, and correctly placed after the close.
26. "But nothing on a Gulf settlement is signed." — **FLAG (L1: dangling referent).** No Gulf settlement, no talks, no peace headline has been mentioned anywhere in the script. The listener hears a denial of a claim that was never made and has nothing to attach it to. The instruction that "the denial travels with the claim" is only half-honoured: the denial shipped, the claim did not.
27. "Iran says it is not negotiating with the United States, its talks are with Oman, and that route is temporary." — **FLAG (L1, consequent).** Correct and properly hedged as content, but "that route is temporary" is unparseable when the route was never introduced. Fix 26 and this sentence lands.
28. "Now the movers." — OK
29. "Six names fell five percent or more today." — OK. See the ruling on the omitted names below.
30. "The biggest move in either direction was Greaves Cotton, down fourteen percent." — OK; the what-it-does arrives in the next breath, which is acceptable.
31. "The engine maker filed results in the afternoon." — OK
32. "Revenue rose thirty-one percent, but operating profit fell one percent and net profit fell twenty-two percent." — OK. Three numbers, but parallel structure carries them.
33. "Growth bought at a worsening margin punishes a share price hardest." — **FLAG (L1 + L4: aphorism standing in for the mechanism).** This is desk language. Plain version: the company sold a lot more and kept less of it, and that is what the market punished.
34. "And if you search that name tonight, the article at the top says profit jumped two hundred and twenty percent, which is from July last year." — OK. Genuinely good — inoculates the listener against the stale article and dates it.
35. "The biggest gain was Ather Energy, the electric two-wheeler maker, up fourteen percent." — Name and what-it-does in the same breath, as the exemplar requires. But **FLAG (L6: the two rounded numbers collide).** Sentence 30 calls Greaves "the biggest move in either direction, down fourteen percent"; five sentences later the biggest gain is also "up fourteen percent". On the ear that is a contradiction — the listener has just been told nothing moved more, and then hears something that moved the same. The underlying figures are −14.04 and +13.96, so the claim is true and the rounding is what breaks it. Say "up almost fourteen percent" and the collision disappears.
36. "Revenue rose eighty-nine percent, and operating profit turned positive for the first time." — OK
37. "That sign change is the substance." — **FLAG (L1: desk-shorthand).** "Sign change" is a spreadsheet word. Say it: for the first time the core business made money instead of losing it.
38. "Said honestly, this is still a loss-making company." — OK, mild meta but the honesty is worth it.
39. "Here is what struck me today." — OK
40. "Property was the worst corner of the market on the eve of a rate decision, and it is tempting to call that rate fear." — OK
41. "It was not." — OK
42. "Three of the five worst property names had filed weak results, and D-L-F's new sales bookings fell about ninety-four percent." — **FLAG (L2: no what-it-does).** D-L-F is named with no plain gloss; a naive listener does not know it is India's largest listed property developer, which is exactly what makes the datapoint matter.
43. "Do not hand the Reserve Bank a move that already has an earnings explanation." — **FLAG (L1: does not parse on one hearing).** "Hand the Reserve Bank a move" is an idiom the listener has to decode. Compliance-wise it is fine (attribution, not advice), but plainly: do not blame the rate decision for a fall that weak results already explain.
44. "One admission." — OK
45. "C-G Power rose six and a half percent with no filing on either day and nothing dated to today." — **FLAG (L2: no what-it-does; "either day" is unanchored).** Which two days? And C-G Power gets no gloss. The refusal to assert a cause is correct and well handled.
46. "Nine of the thirty-two moves we graded have no established cause." — OK
47. "Nobody can tell you why, and that is a truer answer than a tidy one." — OK. Strong close to the section.
48. "Now, what to watch." — OK
49. "Ten tomorrow morning, the Reserve Bank's decision, and the Governor's press conference at twelve." — OK. Correct evening-model time-words throughout.
50. "Listen for whether the inflation forecast moves off five point one, and whether the Bank restates what it assumes oil will cost." — OK. **This is the sentence that keeps the episode legal on the Lead:** it asks *whether*, it does not say *which way*. No cut, no revision, no expectation asserted anywhere in the script.
51. "That's your brief." — OK
52. "Before I sign off: this has been general market commentary, not investment advice." — OK
53. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK. Standing firebreak present and intact in the body.
54. "Markets are risky; you may lose money; act with care." — OK
55. "See you tomorrow." — OK

**L3 (listener-moment time): zero hits.** The covered Tuesday session is "today" throughout; the RBI decision, the press conference and the sign-off are all "tomorrow". Clean under the evening model.

**Compliance: clean.** No tips, no recommendations, no price targets, no broker ratings. Sentence 43 is an instruction about *attribution*, not about money, and reads as such once rewritten.

## Punch list

_(section written below)_

## Source spot-check (S1)

_(section written below)_
