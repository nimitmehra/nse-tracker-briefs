# Verify Podcast Script — 2026-08-04 (re-verify, rewrite pass 1)

**Verdict:** FAIL — but a three-line FAIL, not a rewrite. See the ruling below before deciding.
**Checks (FLAG hits):** L1 4 / L2 2 / L3 0 / L4 2 / L5 0 / L6 2 / S1 0
**Totals:** 3 FAIL-grade defects, 4 WARN, 5 minor, across 60 sentences. **Was: 6 FAIL-grade, 8 WARN, 6 minor across 55.**

**Why FAIL, in one line:** all six prior FAILs are genuinely fixed and the script is factually clean, but the compression that paid for L-I-C shaved three words that were carrying weight — an "inflation", a "which is", and a noun behind a pronoun — and the skill FAILs on any L1.

**The ruling the principal actually needs.** This is not the same script as pass 1. Six structural defects are repaired, the honesty regression is repaired, L-I-C is back with every figure correct, and the source spot-check is clean for the second run in a row. The three remaining defects cost **about eight spoken words** to fix and touch three lines. My recommendation is to apply them by hand and send it to TTS — not to send it back for a third writer pass, which risks trading these three for three new ones.

Cold read performed again from the top, with the brief withheld. The whole script was read as a listener hears it — not only the nine repaired lines. The per-sentence ledger below was completed in full before `briefs/public/2026-08-04.md` was opened.

## TTS mechanics (machine-confirmed on the spoken body)

| Check | Result |
|---|---|
| Narrated word count | 700 — top of the band, matches the header claim exactly |
| Digits | zero |
| `₹` / `$` / `%` | zero |
| Em-dashes / en-dashes | zero |
| `[SAY:]` hints | zero |
| Longest sentence | 30 words (sentence 11), single-thread, comma-segmented — was 32 |
| Sentence count | 60 (was 55) |

Respellings unchanged and correctly scoped: `toro I-Q`, `N-S-E`, `B-S-E`, `C-G Power`, `D-L-F`, and `L-I-C` newly added for the restored mover. SEBI, Nifty, Sensex, Ather, Greaves left alone and read correctly by default. **No L5 hits. No mechanical regression.**

## Per-sentence ledger

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "The Reserve Bank of India decides on interest rates at ten tomorrow morning, and the number to watch is not the rate." — OK. Evening model correct.
5. "It is the Bank's inflation forecast of five point one percent, built on oil at about ninety-five dollars a barrel." — OK
6. "Oil has been much cheaper than that all week." — **OK. Prior FAIL fixed.** Direction is now spoken. A listener knows which way the gap points.
7. "Cheaper oil argues for a lower forecast." — **FLAG (minor L4: the word "inflation" was dropped).** The mechanism behind it (cheaper fuel pulls prices down) is left implicit, while the very next sentence spells its mechanism out in full. And "a lower forecast" loses the qualifier one sentence before a *second* forecast — the rain forecast — enters. Recoverable, but the asymmetry is audible.
8. "But the weather office has just cut its August rain forecast, and less rain pushes food prices up." — OK. Mechanism stated plainly, cause to effect.
9. "So the two inputs point in opposite directions." — OK. "Inputs" is faintly desk-flavoured but sentence 5 already said the forecast was "built on" oil, so it lands. Note the v1 tail "which is why this is not the easy call it sounds like" is gone — that removes the one line that faintly implied a consensus. Good trade.
10. "Indian shares fell into that decision." — OK
11. "The Nifty fifty closed down zero point six four percent, the Sensex down zero point two seven percent, and the fear gauge rose about two percent to a one-week high." — **FLAG (minor L6).** Improved: the fear gauge is now "about two percent" and the sentence is down to 30 words. Two two-decimal index figures still sit in one breath, but they are the headline numbers and the parallel structure carries them. Down from FAIL-adjacent to a note.
12. "So the market fell and fear rose together." — OK
13. "Nearly four hundred shares fell against two hundred and eighty that rose." — **OK. Prior WARN fixed.** Shape, not a count. The dropped "out of six hundred and eighty" costs nothing.
14. "The two headline indices spent most of today moving in opposite directions." — **FLAG (minor L1: audible tension with sentence 11).** The listener was told three sentences ago that both indices closed down. "Moving in opposite directions" now depends entirely on hearing "spent most of today" as the intraday path rather than the close. It resolves, but it costs a beat.
15. "Since Monday, India has set closing prices a new way, by one auction in the last twenty minutes." — **OK. Prior FAIL fixed.** The term is defined before it is used, and defined by what it does. The episode now stands alone without the 03-August script. Dropping the "instead of an average of the last half hour" contrast is a fair budget call — the definition is sufficient to support sentence 17.
16. "On one newspaper's count, the N-S-E auction carried about a hundred and sixty-five rupees for every one on the B-S-E." — **OK. Prior S1 hit fixed.** The hedge is heard before the number, which is the whole point; the listener cannot bank the figure before being told whose figure it is. The two absolute crore figures are gone and the ratio survives alone, as it should.
17. "A thin auction moves prices further, so one company can close at two different prices on the two exchanges." — **OK, with a minor note.** The venue is now named, which was the prior L4 hit. "Moves prices further" is a slightly loose way to say a thinner auction has more price impact, but the sentence delivers its consequence.
18. "That is plumbing, never a signal." — OK. Exactly the right framing, retained.
19. "On the worrying side, that rain forecast." — OK. Clean fragment; parallel with sentence 22.
20. "August is now seen about six percent below normal, after a July that ran one percent above, so this is a forecast turning, not a shortfall." — **OK. Prior WARN fixed.** "Long-period average" is gone and nothing is lost. The turning/shortfall distinction is honest and survives compression.
21. "And the Bank named monsoon uncertainty when it raised that forecast in June." — **FLAG (L1: pronoun collision, and a regression the rewrite introduced).** v1 read "that **inflation** forecast". The qualifier was cut, and now the nearest antecedent is the *rain* forecast two sentences earlier. On one hearing the listener parses "the Bank raised the rain forecast", which is nonsense, then has to reach back six sentences to sentence 5. One word restores it. This is the clearest example of the rewrite trimming a word that was carrying weight.
22. "On the supportive side, oil." — **OK. Prior FAIL fixed.** The producer-view clause "and the timestamp matters" is gone and the cadence is clean.
23. "Crude traded near eighty-six dollars a barrel, up almost three percent, while Indian markets were open." — OK. The session timestamp is inside the sentence, where it must be.
24. "By quarter past nine tonight it was seventy-nine dollars, a nine percent round trip in a day." — OK. "Tonight" places it after the close unmistakably.
25. "That fall came with American claims that a Gulf settlement is close." — **OK. Prior FAIL fixed.** The claim now precedes the denial and is attributed to the American side. "Came with" is carefully chosen — correlation, not cause. One residual: the script never says there is a Gulf conflict to settle, and never states *why* a settlement would cheapen oil. Sentence 27 supplies the parties a beat later, so it closes, but the causal link stays implicit.
26. "Nothing is signed." — **OK. Prior FAIL fixed.** It now has something to attach to.
27. "Iran says it is not negotiating with the United States, its talks are with Oman, and it calls that route temporary." — **OK.** "That route" is introduced in the same breath now. Attribution is correct: the claim is American, the denial is Iran's, and neither is asserted as fact.
28. "Now the movers." — OK
29. "Six names fell five percent or more today." — OK, and now supported by two of the six being named rather than one.
30. "The biggest move in either direction was Greaves Cotton, down fourteen percent." — OK; the what-it-does arrives in the next breath.
31. "The engine maker filed results this afternoon." — OK
32. "Revenue rose thirty-one percent, but net profit fell twenty-two percent." — OK. The operating-profit clause was dropped; the mechanism in sentence 33 does not need it, and two numbers land better than three.
33. "It sold much more and kept less of it." — **OK. Prior FAIL fixed.** The aphorism is gone; this is the mechanism in plain words.
34. "That is what the market punished." — OK. The so-what, stated once.
35. "Search that name tonight and the top article says profit jumped two hundred and twenty percent, from July last year." — **FLAG (L1: the date now dangles, and the mishearing is the opposite of the point).** v1 read "which is from July last year" — an unambiguous appositive on *the article*. Compressed to a bare comma, "from July last year" attaches just as readily to "jumped two hundred and twenty percent", i.e. a year-on-year growth figure. A listener who hears it that way is left with a flat contradiction against "net profit fell twenty-two percent" eighteen words earlier, and nothing later corrects it. This is the one line in the script whose failure mode is worse than confusion — it is the inoculation sentence, and the mishearing re-infects.
36. "The second biggest fall was L-I-C, the state-owned life insurer, down almost nine percent." — OK. Name, plain what-it-does, and number in one breath. This is the restoration working.
37. "The government is selling six and a half percent of it at a fixed price eleven percent below Monday's close." — OK. Two percentages with different referents, but they are structurally distinct enough to survive.
38. "The share drifted towards it." — **FLAG (L1: pronoun points at the wrong noun, and the wrong reading inverts the direction).** The nearest antecedent is "Monday's close". A share drifting *towards Monday's close* is the opposite of what happened — it fell away from Monday's close, towards the discounted floor. Four words, one ambiguous pronoun, and the prior report's own suggested wording ("the price drifts towards that discount") was explicit for exactly this reason.
39. "Supply, not a verdict on the insurer." — OK. Slightly clipped as a fragment, but sentence 37 has already supplied the mechanism, so "supply" is not asked to carry an abstraction on its own.
40. "The biggest gain was Ather Energy, the electric two-wheeler maker, up almost fourteen percent." — **OK. Prior WARN fixed.** "Almost fourteen" now sits properly under Greaves' "fourteen", so the biggest-move-in-either-direction claim no longer contradicts itself on the ear.
41. "Revenue rose eighty-nine percent, and for the first time the core business made money instead of losing it." — **OK. Prior FAIL fixed.** "Sign change" is gone; the merge into one sentence is a clean saving.
42. "Said honestly, this is still a loss-making company." — **OK, with a minor note.** The whole distinction between the core business making money and the company still losing money rests on the two words "core business" in the previous sentence. It holds, but it is the thinnest load-bearing phrase in the movers section.
43. "Here is what struck me today." — OK
44. "Property was the worst corner of the market on the eve of a rate decision." — OK
45. "It is tempting to call that rate fear." — OK
46. "It was not." — OK
47. "Three of the five worst property names had filed weak results, and D-L-F's new sales bookings fell about ninety-four percent." — **FLAG (L2: what-it-does still missing).** Punch-list item 11 was not taken. Context places D-L-F as a property name, so a listener is not lost, but the reason the datapoint is striking — that this is the country's largest listed developer — is never said.
48. "So do not blame tomorrow's rate decision for a fall that weak results already explain." — **OK. Prior FAIL fixed.** Plain, decodes on one hearing, and reads unmistakably as an instruction about attribution rather than about money.
49. "One admission." — OK
50. "C-G Power rose six and a half percent with no company announcement on Monday or today." — **FLAG (L2 partial).** The unanchored "either day" is fixed — the two days are now named. The what-it-does gloss was still not added.
51. "Nine of the thirty-two moves we graded have no established cause." — OK
52. "Nobody can tell you why, and that is truer than a tidy answer." — OK. Tighter than v1 and no reuse of yesterday's closing clause.
53. "Now, what to watch." — OK
54. "Ten tomorrow morning, the Reserve Bank's decision, the Governor's press conference at twelve." — **FLAG (minor L6: cadence).** v1's "and" before the press conference was dropped, leaving three comma-separated fragments with no conjunction. Read aloud it runs together.
55. "Listen for whether the inflation forecast moves off five point one, and whether the Bank restates what it assumes oil will cost." — OK. **This is still the sentence that keeps the episode legal on the Lead:** *whether*, twice, and never *which way*.
56. "That's your brief." — OK
57. "Before I sign off: this has been general market commentary, not investment advice." — OK
58. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK. Firebreak present and intact in the spoken body.
59. "Markets are risky; you may lose money; act with care." — OK
60. "See you tomorrow." — OK

**L3 (listener-moment time): zero hits.** "Today's session", "this afternoon", "tonight", "Since Monday", "ten tomorrow morning", "tomorrow's rate decision", "See you tomorrow" — all correct under the evening model.

**Compliance: clean.** No tips, recommendations, price targets or broker ratings. Sentence 48 is about attribution, not money.

**The two cuts, ruled on.**
- **Asia/Korea beat (30 words) — costs nothing structural.** I checked for orphans: no sentence anywhere in the script depends on the Korea print or on the deduction it supported ("whatever moved India today was Indian"). The wedge, the auction paragraph and the movers are all domestic and self-standing. What is lost is texture — the episode's only non-India frame is now oil and the Gulf. That is an acceptable price for L-I-C, and the writer's reasoning is honest.
- **"It is the only crude number that belongs to today's session" (12 words) — the constraint survives without it.** See the crude-timing ruling in the source spot-check below.

## The six prior FAILs — fixed or not

Confirmed at source after the ledger, not taken on the writer's word.

| # | Prior FAIL | Now | Ruling |
|---|---|---|---|
| 1 | Lead direction never stated | Sentences 6-9 | **FIXED, and fixed the right way.** Both mechanisms are spoken: cheaper oil argues one way, a cut rain forecast pushing food prices up argues the other, landing on "the two inputs point in opposite directions". The brief's own position is "anyone arguing the forecast must come down has to net the two" — the script now renders exactly that. **The no-prediction constraint holds on purpose, not by vagueness:** no cut, no revision, no consensus, no expectation is asserted anywhere, and the v1 tail "not the easy call it sounds like" — which faintly implied a consensus the script never named — is gone. The documented hawkish sell-side path is not contradicted. |
| 2 | Iran denial shipped without the claim | Sentences 25-27 | **FIXED.** The claim comes first and is attributed to the American side, matching the brief's "Claimed, by the American side only". "Came with" asserts correlation, not cause, which is precisely the brief's stance ("the diplomacy stood still; the oil price moved 9% inside a day"). Iran's denial matches the brief word for word, including "temporary". |
| 3 | Greaves aphorism | Sentences 33-34 | **FIXED.** "It sold much more and kept less of it. That is what the market punished." Plain cause, plain so-what. |
| 4 | Ather "sign change" | Sentence 41 | **FIXED.** The spreadsheet word is gone and the merge into one sentence saves words. "Still a loss-making company" retained, and it is accurate — the brief has operating profit at plus ₹9 crore against a net loss of ₹51 crore. |
| 5 | Property attribution idiom | Sentence 48 | **FIXED.** "So do not blame tomorrow's rate decision for a fall that weak results already explain" decodes on one hearing and reads as attribution, not advice. |
| 6 | Closing auction assumed prior episode | Sentence 15 | **FIXED.** Defined before use, and defined by function. The episode now stands alone. |

**All six are genuinely fixed.** None was papered over.

## What the rewrite broke

Every new defect below came from the same cause: the writer funded L-I-C by shaving individual words, and three of the words shaved were load-bearing. Together the fixes cost about eight spoken words.

1. **[L1, sentence 21] "when it raised that forecast in June" — restore "inflation".** v1 had it. With two forecasts now in play and the rain one nearer, "that forecast" points at the wrong noun and produces "the Bank raised the rain forecast". The brief confirms the intended referent: the Bank raised the *inflation* projection to 5.1% from 4.6% in June, naming monsoon uncertainty as one of three reasons.
   *Fix (one word):* "…when it raised that **inflation** forecast in June."
2. **[L1, sentence 35] "profit jumped two hundred and twenty percent, from July last year" — the date now dangles onto the wrong noun.** v1's "which is from July last year" was unambiguous. As compressed, "from July last year" attaches just as naturally to the growth figure, and a listener who parses it that way is left with a straight contradiction against "net profit fell twenty-two percent" eighteen words earlier — with nothing later to correct it. This is the anti-misinformation line; its failure mode is re-infection, so it is the one I would fix first.
   *Fix (three words):* "…the top article says profit jumped two hundred and twenty percent, **and that article is** from July last year."
3. **[L1, sentence 38] "The share drifted towards it" — the pronoun's nearest antecedent is "Monday's close", which inverts the direction.** The share fell *away* from Monday's close, towards the discounted floor. The prior report's own suggested wording said "towards that discount" for exactly this reason.
   *Fix (two words):* "The share drifted **down towards that price**."

## Punch list

### FAIL-grade — fix before TTS

1. **[L1, s35]** restore the article's date as an explicit appositive (above).
2. **[L1, s38]** name what the share drifted towards (above).
3. **[L1, s21]** restore "inflation" (above).

### WARN — carried over from pass 1, still not taken

4. **[L2, s47] D-L-F has no what-it-does.** Context places it as a property name, so nobody is lost, but the reason the number is striking — the country's largest listed developer — is never said. Punch-list item 11 from pass 1.
5. **[L2, s50] C-G Power has no what-it-does.** The "either day" half of the prior item was fixed; the gloss half was not. "C-G Power, which makes electrical equipment, rose six and a half percent…" is five words.

### Minor

6. **[L4, s7]** "Cheaper oil argues for a lower forecast" — the oil mechanism is implicit while the rain mechanism one sentence later is spelled out. The asymmetry is audible, and "a lower **inflation** forecast" would also pre-empt defect 1.
7. **[L1, s14]** "The two headline indices spent most of today moving in opposite directions" sits three sentences after both were reported down. It resolves on "spent most of today", but it costs a beat.
8. **[L6, s11]** two two-decimal index figures still share one 30-word breath. Improved, and acceptable as the headline numbers.
9. **[L6, s54]** the dropped conjunction leaves three comma-separated fragments: "Ten tomorrow morning, the Reserve Bank's decision, the Governor's press conference at twelve." Restore "and".
10. **[L4, s25]** the script never says there *is* a Gulf conflict, nor why a settlement would cheapen oil. Sentence 27 supplies the parties a beat later, so it closes, but the causal link stays inferred.

## Source spot-check (S1)

Run against `briefs/public/2026-08-04.md` **after** the ledger was complete. **No value or direction mismatches. Zero wrong-day numbers. Zero factual regressions from v1.**

### The restored L-I-C block — every figure checked

| Spoken | Brief | Result |
|---|---|---|
| "down almost nine percent" | LICI −8.68% | match |
| "the state-owned life insurer" | Life Insurance Corporation of India; the seller is the Government of India | match |
| "selling six and a half percent of it" | "up to 6.5% of the company", 82.22 crore shares | match, with a note below |
| "at a fixed price eleven percent below Monday's close" | floor ₹382, "roughly 11% below Monday's ₹428.50 close" | match |
| "The share drifted towards it" | "the market drifted towards the floor, closing at ₹391.30, some 2.4% above it" | direction correct in substance; the defect is the pronoun, not the fact |
| "Supply, not a verdict on the insurer" | "the ordinary gravity of a share sale in progress, not a verdict on the insurer" | match, near-verbatim |
| No earnings implied | "No earnings information reached the market today — LIC reports on 06 August" | match — the script asserts no earnings cause |

**"Six names fell five percent or more today" still stands.** The brief's Big Movers section is headed "6 names fell 5% or more, out of 680" and lists exactly six, with Greaves and L-I-C first and second. Naming two of the six strengthens the line rather than straining it.

**One precision note, not a mismatch:** the brief says "up to 6.5%"; the script says "six and a half percent". Audio hardens a ceiling into a figure. Trivial, and I would not spend a word on it.

### The 165-to-one hedge

**Holds.** The brief's position is: "That turnover figure comes from a single newspaper report (Business Standard, 04 August) whose page we could not open, so we attribute it rather than assert it." The script front-loads "On one newspaper's count" so the listener is told whose figure it is *before* the figure arrives, which is the correct construction for audio — a hedge that trails the number arrives too late to stop the listener banking it. The attribution strength matches: single newspaper, attributed not asserted. The two absolute crore figures are correctly dropped and the ratio recast as "a hundred and sixty-five rupees for every one", which is a fair and more listenable rendering of ₹1,542.65 crore against ₹9.36 crore. **The prior S1 hit is cleared.**

### The crude-timing constraint without the meta line

**Holds.** Three independent guards survive the cut:

1. The session price carries its timestamp *inside its own sentence* — "near eighty-six dollars a barrel, up almost three percent, **while Indian markets were open**". That is the guard the meta line was only restating.
2. The evening price is explicitly placed after the close — "**By quarter past nine tonight** it was seventy-nine dollars" — matching the brief's 21:15 IST print of $79.29.
3. **The evening fall is never used to explain the Indian tape.** Its only causal attachment is to an evening event, the American settlement claims. The script also never repeats the error the brief warns about — no line says rising oil caused the market to fall.

The hook's "Oil has been much cheaper than that all week" is a week-range claim, matching the brief's "$79 to $86 all week", not a session claim. The cut costs nothing.

### Everything else checked

| Figure in script | Brief | Result |
|---|---|---|
| Nifty down 0.64%, Sensex down 0.27% | −0.64% / −0.27% | match |
| Fear gauge up about two percent, one-week high | VIX 12.19, +2.18%, one-week high | match |
| Nearly 400 fell against 280 that rose | 392 fell, 279 rose | match |
| Indices moved in opposite directions most of today | "the two spent most of the session moving in opposite directions" | match |
| New closing price since Monday, one auction, last twenty minutes | SEBI framework, single call auction 15:15-15:35, since Monday | match; see note |
| 165 to one, one newspaper's count | ₹1,542.65 cr NSE vs ₹9.36 cr BSE, attributed | match |
| Thin auction, two prices on two exchanges | "the same heavyweight can close at two different levels on two exchanges" | match |
| August about six percent below normal; July one percent above | 94% of LPA; July +1% | match |
| Bank named monsoon uncertainty raising the June forecast | 5.1% from 4.6%, monsoon one of three reasons | match (referent defect is listenability, not fact) |
| Crude near $86, up ~3%, market hours | $86, ~+2.9%, Indian market hours | match |
| $79 at quarter past nine tonight; nine percent round trip | $79.29 at 21:15; "moved 9% inside a day" | match |
| American claims a Gulf settlement is close | "Claimed, by the American side only: a deal is imminent" | match, correctly attributed |
| Nothing signed; Iran not negotiating; Oman; temporary | same, unretracted | match |
| Six names fell 5% or more | six | match |
| Greaves −14%, largest move either direction; rev +31%, PAT −22% | −14.04%, "largest move on the board in either direction"; +31% / −22% | match |
| "+220%" article from July last year | 31 July 2025 | match, correctly dated |
| Ather up almost 14%; rev +89%; first time core business made money | +13.96%; +89%; first-ever positive operating profit, ₹9 cr | match |
| Still a loss-making company | net loss ₹51 cr | match |
| Property worst corner; three of five filed weak results | same | match |
| D-L-F bookings down about 94% | ₹657 cr vs ₹11,425 cr | match |
| C-G Power up 6.5%, no announcement Monday or today | +6.53%, no filing 03 or 04-Aug | match, and no cause asserted |
| Nine of thirty-two moves ungraded | same | match |
| RBI ten tomorrow, presser at twelve | 10:00, 12:00 | match |
| "whether the forecast moves off five point one, whether the Bank restates its crude assumption" | brief's watch-list, in that order | match, and direction-neutral |

**Two minor precision notes, neither a mismatch:** the brief scopes the new closing mechanism to "every stock with listed derivatives" while the script says "India has set closing prices a new way"; and the auction window is 15:15-15:35, which straddles the 15:30 close rather than sitting entirely inside the last twenty minutes. Both are acceptable audio simplifications.

**Hard constraints, each checked individually:**

- **Lead is a gap, not a prediction — PASS,** and now on purpose. See ruling 1 above. The v1 residual risk is gone.
- **Crude timestamping — PASS** without the meta line. See above.
- **FII/DII — PASS.** Absent entirely, not alluded to. Correct: the brief calls the figures provisional, single-source and uncorroborated.
- **Nykaa — PASS.** Absent entirely. Correct: filed 16:14, forty-four minutes after the bell.
- **No cause asserted that the brief refused to assert — PASS.** C-G Power is named as unexplained with the check spoken, and the nine-of-thirty-two grading is said out loud.
- **165-to-one attributed — PASS.** Prior S1 hit cleared.
- **Closing auction called plumbing — PASS.** "That is plumbing, never a signal."
- **Hormuz claim travels with the denial — PASS.** Prior PARTIAL cleared.
- **Greaves 22% decline and the dated July-2025 article — PASS on substance, FLAGGED on delivery.** Both facts are present and correct; the date's grammatical attachment is the defect (punch-list item 1).
- **Compliance — PASS.** No tips, recommendations, price targets or broker ratings. The SEBI-registered-adviser firebreak is present and intact in the spoken body.
- **Continuity with 03-August — PASS.** Movers fully disjoint, the auction re-explained from scratch, yesterday's closing clause not reused.

---

## Before you approve TTS

1. **Three lines, about eight words, and it ships.** Restore "inflation" in sentence 21, "and that article is" in sentence 35, and "down towards that price" in sentence 38. All three are words v1 had and the L-I-C edit removed; none is a judgment call, and the word budget absorbs them (or trade against the two second decimals in sentence 11).
2. **Sentence 35 is the one to fix even if you fix nothing else.** "Profit jumped two hundred and twenty percent, from July last year" can be heard as a year-on-year growth figure, which flatly contradicts "net profit fell twenty-two percent" two breaths earlier. It is the line whose entire job is inoculating a listener who searches Greaves tonight, and mis-parsed it does the opposite.
3. **The lead now works, and it works for the right reason.** Both mechanisms are spoken and neither direction is predicted, so the no-prediction constraint holds on purpose rather than by being too vague to point anywhere. Read sentences 6 to 9 aloud once and confirm they land as tension, not as a forecast — that is the only judgment call left in the episode, and everything else here is mechanical.
