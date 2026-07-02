# Verify Podcast Script — 2026-06-19

**Verdict:** PASS
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)

> Cold-read ordering honored: the per-sentence ledger (L1–L6) was built from the script + canonical exemplar ONLY. The brief was opened LAST, after the ledger, for the S1 source spot-check. This is an EVENING recap of the Thursday 18-Jun close, published 19-Jun (cross-date publish — not flagged). Fed = "last night/overnight" (correct), RBI weekly data = "tomorrow" (correct).

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (exact exemplar opener)
2. "India's biggest stock exchange filed to list itself today, and that single filing drove the whole session." — OK (today-anchored, plain)
3. "The National Stock Exchange filed papers for a thirty-thousand-crore-rupee share sale, the largest in India's history, valuing the exchange above five lakh crore rupees." — OK (NSE named; numbers spelled; L5 clean)
4. "Here is the catch." — OK (conversational, exemplar-style signpost)
5. "The entire deal is existing owners selling down their stakes, so no new money goes to the exchange itself." — OK (plain mechanism, cause→effect)
6. "The value flows to whoever owns NSE shares." — OK (plain so-what)
7. "So the buying showed up not in exchange stocks, but across the insurers and asset managers that hold NSE stakes." — OK (clear cause→effect)
8. "New India Assurance rose about eight percent, and Aditya Birla's asset-management arm about six." — OK (names placed; "about six" reads fine aloud)
9. "The one clear loser was the rival exchange, BSE, down about four percent, because it is about to get a much larger listed competitor." — OK (BSE named + placed as "rival exchange" + why)
10. "That financials bid is what kept the Nifty green." — OK (plain link to the tape)
11. "Here is where the market closed today." — OK (exemplar line)
12. "The Nifty fifty finished at twenty-four thousand one hundred and sixty-eight, up about a third of a percent." — OK
13. "That is a fifth straight up-day, but a narrow one." — OK
14. "Healthcare and the financials led, and there was exactly one sector in the red." — OK (sets up the IT beat)
15. "That one red sector was information technology, down about one and a quarter percent." — OK
16. "The reason was last night's United States Federal Reserve decision." — OK (L3: Fed correctly "last night" — evening model)
17. "The Fed held interest rates, but in Kevin Warsh's first meeting as Chair, its own projections turned hawkish and now lean toward a rate hike rather than a cut." — OK ("hawkish" immediately defined as "lean toward a rate hike"; ~32 words but single-thread, cleanly comma-segmented — not flagged on count alone per L6)
18. "That hit Indian IT twice over." — OK
19. "Higher United States rates lower the value the market puts on their future earnings, and a firmer rupee trims the rupee value of the dollars they earn." — OK (full plain mechanism, both legs)
20. "Infosys, T-C-S [SAY: T-C-S] and HCL Tech [SAY: H-C-L Tech] all fell together." — OK (names placed; SAY hints are TTS pronunciation directives, not audio-breakers)
21. "Now the movers." — OK (exemplar transition)
22. "The biggest gainer was Bata India, the footwear company, up about sixteen percent, reportedly its best single day in two decades." — OK (what-it-does placed)
23. "The reason was a new boss." — OK
24. "Bata appointed a former senior Nike executive as its chief executive, and the market read that as a turnaround signal for a brand that has lagged." — OK (plain why)
25. "The other clear theme was textiles." — OK
26. "K-P-R Mill [SAY: K-P-R Mill], Welspun Living and SP Apparels all jumped double digits together." — OK (cohort named)
27. "Two trade tailwinds drove the whole cohort." — OK ("tailwinds" explained in the next two sentences)
28. "The India-United Kingdom free-trade deal takes effect in mid-July and gives Indian textiles duty-free access to Britain." — OK (plain mechanism)
29. "And a reported cut in the United States tariff on Indian goods, from about fifty percent down to about eighteen, brings Indian exporters closer to their Asian rivals." — OK (plain)
30. "This was a policy move across the group, not one company's story." — OK ("not X" disambiguation, exemplar pattern)
31. "Here is what struck me most about today." — OK (exemplar's signature wedge opener)
32. "The Nifty rose for a fifth day, but it under-joined a global relief rally, and the reason was the foreign money." — OK ("under-joined" understandable in context; reads fine)
33. "Around the world, equity markets bounced once the Fed decision cleared, but here in India, foreign investors actually sold about eight hundred fifty crore rupees of shares." — OK (plain contrast; single-thread)
34. "Domestic institutions bought about three thousand one hundred crore and carried the entire day on their own." — OK
35. "So this rally is real, but it is domestically funded, not foreign-backed." — OK (plain so-what)
36. "And the foreigners have now turned seller." — OK
37. "That is the single thing this advance still lacks, and it is why the next few sessions of flow data matter more than the index level." — OK
38. "Now, what to watch." — OK
39. "Tomorrow evening, the Reserve Bank of India publishes its weekly data, including the foreign-exchange reserves, worth watching for any sign the central bank is acting around the rupee near ninety-four." — OK (L3: RBI data correctly "tomorrow"; ~33 words but single-thread, cleanly comma-segmented, no lost antecedent — not flagged on length alone per L6)
40. "And the bigger thing to track is the flows themselves." — OK
41. "Does the foreign selling deepen, or does it reverse, now that the rally is resting entirely on domestic money." — OK (plain rhetorical question)
42. "That's your brief." — OK
43. "Before I sign off: this has been general market commentary, not investment advice." — OK (exemplar firebreak)
44. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
45. "Markets are risky; you may lose money; act with care." — OK
46. "See you tomorrow." — OK

**Ledger result: 46/46 sentences OK. Zero FLAGs across L1–L6.**

L5 audio-breaker sweep: 0 ₹ symbols, 0 % symbols, 0 em-dashes in body, all numbers spelled out, body = 657 words (within 500–700). The `[SAY: ...]` tags are pronunciation hints for TTS, not audio-breakers. PASS.

## Punch list (if any)

None. The script is ship-ready. (Optional, non-blocking taste notes, NOT flags: "under-joined" in sentence 32 is a lightly coined verb — it reads cleanly aloud and is immediately explained by "the reason was the foreign money," so it is left as OK. "hawkish" and "tailwinds" both appear with their plain-English meaning attached in the same breath, so neither trips L1.)

## Source spot-check (S1)

Opened the brief (`briefs/public/2026-06-18.md`) LAST. All headline figures match:

- Nifty 24,168 / +~0.34% (script "up about a third of a percent") — match
- IT lone red sector, −1.19% (script "about one and a quarter percent") — match (rounding)
- NSE IPO: ₹30,000 cr, valuation >₹5 lakh cr, largest-ever, all-OFS / no new money to NSE — match
- New India Assurance +7.98% ("about eight"), Aditya Birla AMC +6.30% ("about six"), BSE −4.3% ("about four") — match
- Fed: held, Warsh's first meeting, hawkish, tilts to a hike, "last night" — match
- Infosys / TCS / HCL Tech all fell — match
- Bata +16.42% ("about sixteen"), ex-Nike CEO, best day in ~2 decades — match
- Textiles: KPR Mill / Welspun Living / SP Apparels double-digit; UK FTA mid-July (CETA 15-Jul); US tariff ~50%→~18% — match
- FII −₹854.63 cr ("about eight hundred fifty crore"), DII +₹3,129.79 cr ("about three thousand one hundred crore"), foreigners flipped to seller — match
- RBI weekly data Friday 19-Jun (~5 PM), forex reserves, rupee ~94.3 ("near ninety-four"), framed "tomorrow" — match

No number or causal-direction mismatch. No wrong-day leakage (the 2026-06-04-style failure). S1: PASS.

---

**Gate:** PASS — clears the podcast for the principal review gate (`podcast-script-public-nse` Step 7). Safe to proceed to TTS once principal approves.
