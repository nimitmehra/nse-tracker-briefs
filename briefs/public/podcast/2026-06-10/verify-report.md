# Verify Podcast Script — 2026-06-10

**Verdict:** WARN
**Checks:** L1 2 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)

Cold read done with the brief withheld; brief opened only for the Step 2 source spot-check. The script is geopolitically disciplined, TTS-clean, and sources cleanly. The only flags are two uses of the desk-word "tape" — the exact term the exemplar/skill name as banned L1 desk-shorthand. Both are isolated and trivially fixable; the principal may ship as-is, but the cleaner fix is to swap the word.

## Per-sentence ledger

**Hook**
1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (matches exemplar open verbatim)
2. "Today the market ran a full circle, and the round trip is the whole story." — OK (plain, sets the day's frame)
3. "The June eighth pledge between Israel and Iran to stop attacking each other broke down overnight, with the United States now reported to have struck Iran directly." — OK (reported/developing framing intact; "now reported to have" keeps it as a claim, not asserted fact; no scope/casualty/damage)
4. "India opened firm anyway, with the Sensex up about six hundred points by midday, on hope the oil-war premium was easing." — OK (plain cause; "oil-war premium" is explained later)
5. "Then the market gave the entire gain back as the fresh escalation pushed oil risk straight back up." — OK (market reaction stated as fact, correct)
6. "The Nifty closed almost exactly flat." — OK

**Tape / breadth**
7. "Here is where the market closed today." — OK (signpost, mirrors exemplar)
8. "The Nifty fifty finished at twenty-three thousand two hundred and fifteen, down a flat zero point one two percent." — OK (number spelled, reads clean)
9. "But the flat headline hid the real damage." — OK
10. "The broader market fell about one and a third percent, with mid-caps and small-caps each down that much." — OK (plain)
11. "So if you own mid-caps, the index was flat but your basket likely fell." — OK (excellent naive-listener so-what)
12. "The one green corner was fertilisers, with Chambal up five percent on a report that surging global prices could double next year's subsidy bill." — OK (name placed, cause given)
13. "Metals were the weakest patch, as aluminium futures fell sharply and dragged Hindalco and Hindustan Zinc down three percent or more." — OK (names placed)

**Breadth read**
14. "And here is the more telling part." — OK (signpost)
15. "The index held flat only because domestic funds kept buying." — OK
16. "They bought about three thousand crore rupees while foreign investors sold about two thousand crore." — OK (rounded, reads clean in TTS)
17. "So the flat number is not a calm session, it is domestic money absorbing a foreign exit underneath a soft, narrow tape." — **FLAG (L1: desk-shorthand "tape")**. "underneath a soft, narrow tape" is exactly the kind of desk word the exemplar bans. A naive listener does not know "tape" = the market's price action. Suggested rewrite below.

**Macro frame**
18. "Now the macro frame." — OK
19. "The same Middle-East escalation that whipsawed shares is the live threat to Friday's inflation print." — OK ("whipsawed" is borderline but the prior sentences explain the full-circle move, so it lands)
20. "Brent crude ended higher near ninety-two dollars, and that feeds straight into fuel costs." — OK (named, explained)
21. "A Reuters poll already sees May inflation rising to four percent, from about three and a half in April, mostly on fuel." — OK
22. "On the supportive side, India's bond story is still a counter-current." — OK
23. "After last week's tax change for foreign bond buyers, the ten-year yield sits near a four-week low at six point nine percent, even with today's global risk-off." — OK (plain-language gloss of the bond-tax ordinance; reads clean)

**Movers**
24. "Now the movers." — OK
25. "The cleanest winner was Inox India, up twelve percent." — OK
26. "The cryogenic-equipment maker posted a record quarter and won three hundred crore rupees of fresh orders since April, including a large cryogenic-storage order from a global private space-exploration company." — OK ("cryogenic-equipment maker" places what it does; figure rounded from 322 to 300, acceptable)
27. "A heavy-volume new high in a weak tape." — **FLAG (L1: desk-shorthand "tape")**. Same banned word as #17; also a sentence fragment. Suggested rewrite below.
28. "The second was CarTrade Tech, also up twelve percent, after the brokerage InCred started coverage with a Buy and a target near three thousand rupees, on top of strong used-car platform growth." — OK (name + what-it-does via "used-car platform"; attributed third-party Buy is fine)
29. "The third was a fall." — OK
30. "Oil India dropped ten percent, as the market faded its recent natural-gas discovery in the Andaman waters." — OK
31. "The find is real, but it sits in remote deep water, so any production is a multi-year story." — OK (clear so-what)

**Wedge**
32. "Here is what struck me about today." — OK (first-person wedge signpost, matches exemplar)
33. "On a day of fresh military escalation, you would expect gold to rally as the safe haven." — OK
34. "Instead gold fell two percent." — OK
35. "The reason is that today's fear was specifically an oil-supply risk, the threat to the narrow shipping lane that carries much of the world's oil, not a broad flight to safety." — OK (Hormuz explained in plain words without naming it; good)
36. "Gold falling while crude rose is the signal that the fear was being priced through energy, not through havens." — OK (clean mechanism, not metaphor)

**Watch / firebreak**
37. "Now, what to watch, and it is Friday." — OK
38. "India's May inflation figure lands, the first read that captures this crude spike, with fuel the swing factor." — OK
39. "The same day brings the Reserve Bank's weekly reserves figure, the cleanest sign of how hard it is defending the rupee." — OK (plain gloss)
40. "And the oil price stays the live signal." — OK
41. "Any further escalation overnight is a Thursday input, and a re-spike in crude would tighten Friday's inflation read further." — OK (correct causal timing — overnight = next-session input, not today's cause)
42. "That's your brief. Before I sign off: this has been general market commentary, not investment advice." — OK (firebreak)
43. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
44. "Markets are risky; you may lose money; act with care. See you tomorrow." — OK

## Punch list

- **[L1] Line 17** — "underneath a soft, narrow tape" uses the banned desk-word "tape." Suggested rewrite: "...it is domestic money absorbing a foreign exit underneath a soft, narrow session." or simpler "...it is domestic money quietly absorbing a foreign exit, on a soft and narrow day."
- **[L1] Line 27** — "A heavy-volume new high in a weak tape." Same banned word, plus it is a fragment. Suggested rewrite: "It hit a new high on heavy volume, even on a weak day for the broader market."

Neither flag is an audio-breaker or a fidelity error; both are single-word substitutions. If the principal prefers the current cadence, the script is shippable, but swapping "tape" brings it fully in line with the exemplar's naive-listener bar.

## Geopolitics discipline (geopolitics-day check)

PASS. Every reference to the US-Iran escalation is reported/developing, never asserted as on-the-ground fact:
- "now reported to have struck Iran directly" — claim framing, not assertion
- "the fresh escalation pushed oil risk straight back up" — states the market reaction, not the event
- No scope, casualty, or damage claims anywhere in the body.
- Causal timing correct: the overnight pre-open strikes are treated as today's driver; any further overnight move is named only as a Thursday input.

## Source spot-check (S1)

All headline figures trace to the brief; no wrong-day leakage. PASS.

| Script | Brief | Match |
|---|---|---|
| Nifty 23,215, −0.12% | 23,214.95, −0.12% | ✓ |
| Broader market −1.33% (mid/small) | mid- & small-cap −1.3% | ✓ |
| Sensex up ~600 pts midday | "Sensex up about 600 points by midday" | ✓ |
| Chambal +5% | +5.04% | ✓ |
| Hindalco/Hindustan Zinc −3%+ | "down 3% or more" | ✓ |
| Brent near $92 | $91.91 | ✓ |
| May CPI 4% from ~3.5% Apr | 4.0% from 3.48% | ✓ |
| 10Y 6.9%, four-week low | 6.91%, four-week low | ✓ |
| DII ~+3,000 cr / FII ~−2,000 cr | +3,124 / −2,125 | ✓ (rounded) |
| Inox +12%, ~₹300 cr orders | +12.15%, ₹322 cr | ✓ (rounded down; minor) |
| CarTrade +12%, InCred Buy, target ~₹3,000 | +12.06%, ₹2,953 | ✓ |
| Oil India −10%, Andaman gas fade | −10.21%, Andaman gas give-back | ✓ |
| Gold −2% | −2.0% | ✓ |

One minor rounding note (not a flag): Inox order figure is read as "three hundred crore" vs brief's ₹322 crore — rounding down by ~7%. Optional tightening to "over three hundred crore" or "about three hundred and twenty crore," but not a fidelity error.
