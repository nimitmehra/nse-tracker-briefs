# Verify Podcast Script — 2026-07-02

**Verdict:** WARN
**Checks:** L1 2 / L2 0 / L3 0 / L4 0 / L5 0 / L6 1 / S1 0  (counts = FLAG hits)

Cold-read stance held: script + exemplar read first, brief opened only for the S1 spot-check after the ledger was complete.

## Per-sentence ledger

**Intro**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK

**Para 1 — the Lead (rupee)**
4. "Here is the story of today." — OK
5. "The loud move was a jump in the Nifty, but the quiet move mattered more." — OK
6. "The rupee fell to a record low, past ninety-five point four to the dollar." — OK
7. "That is strange, because the dollar was weak around the world and oil stayed cheap, and both of those normally lift the rupee." — OK
8. "When a currency falls against a falling dollar, the usual reason is money leaving the country." — OK (mechanism stated plainly)
9. "And that is what showed up." — OK
10. "Foreign investors sold Indian shares again, a fifth day in a row, with domestic funds again absorbing the selling." — OK
11. "So the real signal today was the rupee, not the rally." — OK

**Para 2 — the close (IT bounce)**
12. "Here is where the market closed today." — OK
13. "The Nifty fifty rose zero point seven one percent, to twenty-four thousand one hundred and seventy-five." — OK
14. "But almost all of that gain came from one corner." — OK
15. "India's technology shares jumped about four point six percent, the top sector by a wide margin, with all ten members higher and Infosys up more than five percent." — OK (SAY tag present, name placed)
16. "Everything else barely moved." — OK
17. "The banks, which carry the most weight in the market, sat flat, and public-sector banks fell." — OK
18. "That one sector bounced because it had fallen too far, too fast." — OK
19. "Four losing days had pushed technology to a three-year low, and today buyers came back for the bargain." — OK
20. "That is a spring uncoiling, not a trend turning." — OK (L4 checked; the cause→effect chain is stated plainly in the two prior sentences, so the image is a restatement, not a stand-in. Also inherited verbatim from the brief's Connections.)
21. "Nothing underneath changed." — OK
22. "American clients are still spending slowly, artificial intelligence is still eating into the routine work these firms bill for, and United States interest rates are still high." — OK ("eating into" is a common, clear image)

**Para 3 — the two forces**
23. "Now the two forces under the day." — OK
24. "On the supportive side, cheaper oil keeps doing quiet work." — OK (mild but clear)
25. "Brent crude is under seventy-one dollars, which eases India's import bill and cools inflation." — OK
26. "The bond market agrees the pressure is off." — OK
27. "Government yields eased, and the fear gauge fell more than seven percent, a calm session." — OK ("fear gauge" is self-explanatory)
28. "On the worrying side is that record-low rupee, which says foreign money is still leaving." — OK
29. "And after India had closed, American jobs data landed and was read as hawkish." — FLAG (L1: "hawkish" is undefined finance jargon on first hearing; the next sentence unpacks the mechanism but never defines the word itself)
30. "Hiring was weak, but wages ran hot, so United States bond yields rose." — OK (clear cause→effect; rescues #29's meaning if not its vocabulary)
31. "That keeps alive the fear of high American rates, which is the very thing weighing on Indian technology." — OK
32. "So the after-hours news cut against the rate-relief hope technology had bought during the day." — OK
33. "It is a headwind for Friday, not something that drove today." — OK ("headwind" is common and used transparently as "works against")

**Para 4 — the movers**
34. "Now the movers." — OK
35. "The cleanest winner was Sona Comstar, an auto-parts maker, up almost seven percent to a fresh high." — OK (name + what-it-does + SAY tag)
36. "It reported an order book worth about twenty-three thousand seven hundred crore rupees, a real pipeline of future work, not a bounce." — OK
37. "The second was Cantabil Retail, a clothing chain, up more than eleven percent." — OK
38. "It opened five new stores in June and reiterated next year's targets, though the pop ran ahead of the news." — OK
39. "The one big faller was Saksoft, a small technology firm, down almost eight percent." — OK
40. "It was the only red name in a green technology sector, giving back a big three-month run as money moved out of the stretched small-cap corner." — OK (red/green colour is intuitive)

**Para 5 — the listener moment (wedge)**
41. "Here is the one thing that struck me most about today." — OK (first person, once, in the wedge — allowed)
42. "The clue was who did not move." — OK
43. "Banks are the heaviest weight in the market and the usual engine of a real, broad rally." — OK
44. "Today they sat flat, and public-sector banks fell." — OK
45. "If this were a genuine own-everything session, banks would have led it." — OK ("own-everything" is a plain coinage, clear on one hearing)
46. "They did not." — OK
47. "So today was a narrow bounce in one beaten-down corner, not money returning to Indian shares across the board." — OK
48. "The rupee says the same thing." — OK
49. "The first real test of whether technology has actually turned is not the chart." — OK
50. "It is earnings, and Tata Consultancy Services reports on the ninth of July." — OK (SAY: T-C-S)

**Para 6 — what to watch**
51. "Now, what to watch, and it is all tomorrow, Friday." — OK (time-anchor correct: tomorrow = Friday)
52. "United States markets are closed for a holiday, so India trades thin on the read-through of that hawkish jobs data." — FLAG (L1: stacks two jargon terms — "read-through" AND a re-use of "hawkish" — in one sentence, the densest jargon load in the script; a naive listener loses "read-through")
53. "And in the evening, the Reserve Bank of India publishes its weekly figures." — OK
54. "Watch one line in them, the foreign-exchange reserves, because a large drop would show how hard the central bank is spending to defend the record-low rupee." — OK

**Sign-off**
55. "That's your brief." — OK
56. "Before I sign off: this has been general market commentary, not investment advice." — OK
57. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
58. "Markets are risky; you may lose money; act with care." — OK (semicolons are TTS-safe)
59. "See you tomorrow." — OK

## Cold-listener comprehension test
PASS. The narrative arc lands cleanly on one hearing: rupee = the real signal (money leaving), IT bounce = loud but hollow (oversold snap-back, nothing underneath changed), the wedge (banks sat out, so it was narrow not broad), and a correctly-framed Friday watch. Only two vocabulary snags ("hawkish", "read-through") momentarily tax the naive listener, and in both cases surrounding sentences carry the meaning. No line is a flagrant comprehension breaker.

## Time-discipline (L3)
PASS. The covered Thursday session is consistently "today"; Friday RBI/PMI and TCS 9-July are "tomorrow"/next-session; the US June jobs report is explicitly handled as an after-close, next-session Friday headwind, "not something that drove today." No morning-model leakage.

## TTS-cleanliness (L5)
PASS/clean. All numbers spelled out; no ₹, $, or % symbols; zero em-dashes in the body (compound hyphens like "auto-parts", "record-low", "three-year" are not em-dashes); colon and semicolons in the sign-off are TTS-safe. SAY pronunciation tags present for Infosys, Sona Comstar, Cantabil, Saksoft, TCS.

## Punch list
- [L1, sentence 52] "...India trades thin on the read-through of that hawkish jobs data." — densest jargon in the script. Suggested plain rewrite: "...so India trades quietly, mostly reacting to that weak-hiring-but-hot-wages jobs report from overnight." (drops "read-through" and "hawkish" in one move)
- [L1, sentence 29] "...American jobs data landed and was read as hawkish." — either define or drop "hawkish". Suggested: "...American jobs data landed, and markets read it as a reason rates could stay high." (the word "hawkish" then becomes optional shorthand, already earned)
- [L6, word count] Body is ~760 words vs the ~700 ceiling (~60 over, ~8.6%). Not an L5 audio-breaker and in line with the two prior accepted days (733/727), but the outer edge of the band. Principal may ship as-is; if trimming, the two rewrites above and any one redundant restatement in Para 2/3 would bring it under 700 without losing causation.

## Source spot-check (S1)
PASS — no number or direction mismatch. Verified against `briefs/public/2026-07-02.md`:
- Nifty +0.71% to 24,175.70 ✓ | IT +4.64% ("about four point six"), all ten green, Infosys >5% ✓
- Rupee record low past 95.4 ✓ (95.38, near 95.43) | Brent under $71 ✓ ($70.54) | VIX −7.19% ("more than seven percent") ✓ | 10-yr yield eased ✓ (6.71%)
- FII net sell, fifth straight day, DII absorbing ✓ (−₹312 cr / +₹1,784 cr)
- US jobs after 15:30 close, weak hiring + hot wages → US yields up, read hawkish ✓ (57k jobs, +3.5% wages, 10-yr to 4.49%)
- Sona Comstar +~7% / ₹23,700 cr order book ✓ (+6.93%) | Cantabil +>11% / 5 new June stores + reiterated FY27 guidance ✓ (+11.33%) | Saksoft −~8%, sole red IT, 3-month unwind ✓ (−7.75%)
- Banks flat, PSU banks down ✓ | TCS earnings 9 July ✓ | RBI weekly (forex reserves) Friday evening ✓ | US markets closed Friday holiday ✓

The script also correctly inherits the brief's Lead (rupee, not rally) and the "spring uncoiling" framing verbatim.

---

VERDICT: WARN
