# Verify Podcast Script — 2026-08-04 (re-verify, rewrite pass 1)

**Verdict:** _pending_
**Checks (FLAG hits):** _pending_

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

_pending_

## Punch list

_pending_

## Source spot-check (S1)

_pending_
