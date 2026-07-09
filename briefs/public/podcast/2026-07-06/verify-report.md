# Verify Podcast Script — 2026-07-06

**Verdict:** WARN
**Checks:** L1 1 / L2 0 / L3 0 / L4 1 / L5 1 / L6 0 / S1 0  (counts = FLAG hits)

Cold read completed with the brief withheld; source spot-check run last. No FAIL-class defect. Two non-blocking WARNs: body length over the 700-word ceiling (~761), and one inherited phrase ("pre-marked ... anaemic") a naive listener could stumble on. Principal may ship.

## Per-sentence ledger

**Intro**
1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (matches exemplar open)

**Lead (flow flip)**
2. "The quiet move today mattered more than the loud one." — OK
3. "The Nifty rose a modest two-thirds of one percent, its fourth straight gain." — OK
4. "But the real story was underneath it." — OK
5. "Foreign investors have started buying Indian shares again." — OK
6. "In June they pulled more than forty-nine thousand crore rupees out of the market, one of the heaviest monthly exits in years." — OK
7. "In the first three days of July they turned around and bought, and today they stayed on the buy side, with domestic funds buying far more alongside them." — OK (long ~30w but single-thread, comma-segmented, speakable)
8. "The turn is small and early, but the direction has flipped." — OK

**The close**
9. "Here is where the market closed today." — OK
10. "The Nifty fifty finished at twenty-four thousand four hundred and thirty, up zero point six six percent." — OK
11. "But this was not a broad surge." — OK
12. "The money went into rate-sensitive corners." — OK (mild desk-phrase but immediately unpacked by the next line)
13. "Real estate led, up almost two percent to a six-month high, the cleanest bet on interest rates coming down." — OK
14. "Autos, metals and energy firmed alongside it." — OK
15. "The one red spot was technology, down about half a percent to a fresh one-year low." — OK
16. "And the fear gauge sat at just eleven point eight, unusually calm." — OK ("fear gauge" is plain; number rounded from 11.82, fine)
17. "That tells you this was a low-conviction advance, not a crowd piling in." — OK

**Two forces**
18. "Now the two forces under the day." — OK
19. "On the supportive side, oil is doing quiet work." — OK (mild personification, harmless, resolved by the next sentence)
20. "Brent crude is near seventy-two dollars, about a quarter cheaper than a month ago, which eases India's import bill and cools inflation." — OK
21. "And a soft United States jobs report last week took some heat out of the fear that American interest rates stay high, which fed a rate-cut hope into Indian shares." — OK (long ~30w, single-thread)
22. "India's own short-term bond yields eased today, confirming it." — OK
23. "On the worrying side is the rupee." — OK
24. "It was flat on the day, but it is down about one percent on the week, soft even with cheap oil, which points to money still leaving." — OK
25. "One correction matters here." — OK
26. "Last week's news said India's foreign reserves fell almost six billion dollars, which looked like the central bank spending dollars to defend the rupee." — OK
27. "It was not." — OK
28. "Almost the entire drop was the price of gold falling on the books." — OK (plain-English rendering of the gold mark-down)
29. "The bank's actual dollar holdings barely moved." — OK
30. "So it is a valuation effect, not intervention." — OK (mildly technical but earned by the two prior lines)

**Movers**
31. "Now the movers." — OK
32. "The cleanest winner was the Aegis gas-terminal group." — OK
33. "Aegis Vopak Terminals rose almost nine percent, and Aegis Logistics rose more than six." — OK (names placed on mention)
34. "A brokerage note flagged that India's cooking-gas imports are recovering back toward normal levels, which lifts the volume flowing through their terminals and their earnings." — OK ("cooking-gas" is the right plain gloss for LPG)
35. "The second was Dixon Technologies [SAY: DIK-son], an electronics manufacturer, up almost seven percent." — OK (name + what-it-does)
36. "A government group cleared its joint venture with the phone maker Vivo [SAY: VEE-voh], with only the formal approval letter now pending, and a foreign brokerage raised its price target." — OK
37. "The deal pushes Dixon deeper into making components, not just assembling phones." — OK (clean why-it-matters)
38. "The one notable faller was Apollo Micro Systems [SAY: a-POL-oh], a defence electronics firm, down almost six percent." — OK
39. "Its board is considering raising fresh money by issuing new shares." — OK (dilution explained before the word is used)
40. "On a stock that has more than doubled in three months, investors read that possible dilution as a negative and sold it." — OK

**Wedge (IT with a currency tailwind)**
41. "Here is the one thing that struck me most about today." — OK (first person, once, in the wedge — allowed)
42. "Technology shares fell to a fresh one-year low, and they did it with the wind at their back." — OK (metaphor, but immediately and fully unpacked by the next two sentences; borderline, not flagged)
43. "A weaker rupee normally helps these companies, because they earn in dollars and spend in rupees." — OK
44. "So they should have had support this week." — OK
45. "Instead they made new lows." — OK
46. "The reason is not the currency." — OK
47. "It is the business." — OK
48. "The broker Nomura [SAY: no-MOO-ra] has pre-marked next year's sector growth as anaemic, blaming weak American client spending and pricing pressure from artificial intelligence." — FLAG (L1: "pre-marked ... as anaemic" — "pre-marked" is not everyday English; a cold listener may not parse it on one hearing. Inherited verbatim from the brief. Non-blocking, but the softest line in the script.)
49. "The market is pricing that in ahead of results." — OK ("pricing in" is common enough)
50. "These stocks got cheaper because expectations for the business fell, not because of the exchange rate." — OK

**What to watch**
51. "Now, what to watch." — OK
52. "Thursday is the first real test." — OK (L3: Thursday 9 July is a NEXT session vs the covered Monday close — correct evening-model framing)
53. "Tata Consultancy Services [SAY: T-C-S], the country's largest technology firm, reports its June-quarter results after hours, the first hard read on whether that year-long slide is bottoming." — OK
54. "And on Friday evening, the Reserve Bank publishes its weekly figures." — OK
55. "Watch the actual dollar-holdings line this time, not the gold-inflated headline." — OK (ties the RBI watch back to the reserves correction cleanly)

**Outro**
56. "That's your brief. Before I sign off: this has been general market commentary, not investment advice." — OK
57. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
58. "Markets are risky; you may lose money; act with care." — OK
59. "See you tomorrow." — OK

## Punch list (optional — principal may ship without acting)
- [L1, sentence 48] "pre-marked next year's sector growth as anaemic" → suggest a plainer render: "has already forecast next year's growth for the sector as weak" (or "…as barely-there"). Keeps the meaning, removes the desk verb.
- [L5/L6, whole body] Body ~761 words, ~61 over the 700 ceiling — same as the last accepted day (760), and the self-verify justifies it (two load-bearing threads + the reserves correction). Not "well outside" the band, so WARN not FAIL. If a trim is wanted, sentence 19 (oil "doing quiet work") is the softest candidate to compress.

## TTS-cleanliness (L5)
Clean. All numbers spelled out (no digits in body); no rupee / dollar / percent symbols; zero em-dashes. `[SAY: ...]` pronunciation hints are stripped pre-TTS. Only mechanical WARN is the length (above).

## Time discipline (L3)
Clean, evening model. The Monday close is "today" throughout; TCS (Thu 9 July) and RBI (Fri 10 July) are framed as next sessions. Monday's US session is correctly kept OUT of the narrated body (composition note flags it as tomorrow's input). No "yesterday" for the covered close, no morning-model leakage.

## Source spot-check (S1) — run LAST, after the ledger
Checked every headline figure against `briefs/public/2026-07-06.md`; all match, direction and magnitude:
- Nifty twenty-four thousand four hundred and thirty, up 0.66% — matches (24,430.35 / +0.66%).
- Fear gauge eleven point eight — matches VIX 11.82 (rounded).
- Realty "almost two percent" to six-month high — matches +1.81%.
- IT "about half a percent" to a fresh one-year low — matches −0.59% at 52-week lows.
- FII +₹243 cr / DII +₹3,791 cr, both buyers, fourth straight up day — matches.
- June exit "more than forty-nine thousand crore" — matches ₹49,340 cr.
- Brent "near seventy-two dollars, about a quarter cheaper than a month ago" — matches ~$72.1 / ~26%.
- Rupee flat on day, down ~1% on the week — matches ₹95.39 (−0.15% day, ~1% week).
- Reserves "almost six billion dollars," drop is gold mark-down, dollar holdings "barely moved" — matches ($5.65bn total; gold −$5.39bn; FCA −$150m).
- Aegis Vopak "almost nine" (+8.76%) / Aegis Logistics "more than six" (+6.32%); LPG import recovery — matches.
- Dixon "almost seven percent" (+6.81%); Vivo-JV clearance + TP hike — matches.
- Apollo Micro "almost six percent" (−5.82%); preferential-issue dilution; "more than doubled in three months" (+114%) — matches.
- Nomura FY27 "anaemic" — matches The Connections.
- TCS Thursday 9 July after hours; RBI weekly Friday 10 July — matches What to Watch.

No number or causal-direction mismatch. No wrong-day leakage. S1 = 0.

---

VERDICT: WARN
