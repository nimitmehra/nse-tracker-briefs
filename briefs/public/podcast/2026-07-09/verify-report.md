# Verify Podcast Script — 2026-07-09

**Verdict:** WARN
**Checks:** L1 0 / L2 0 / L3 0 / L4 2 / L6 1 / L5 0 / S1 not-run (brief withheld per orchestrator directive)

Read cold as a naive audio listener, one linear hearing, brief NOT opened. No FAIL-grade defect: no desk-shorthand, no deferred names, timing is clean under the evening model, and TTS mechanics are spotless. Two soft flags plus a marginal word-count overage keep it out of a clean PASS.

## Per-sentence ledger

1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK
4. "After the close today, Tata Consultancy Services, India's largest technology company, opened the earnings season with a soft-but-steady result." — OK (name + plain what-it-does placed on first mention; SAY-hint T-C-S stripped pre-TTS)
5. "Revenue rose almost fourteen percent from a year ago." — OK
6. "But strip out the weaker rupee, which flatters the headline, and underlying growth was just four-tenths of one percent, close to flat." — OK (mechanism stated plainly)
7. "Because it filed after the market shut, the share reaction comes tomorrow." — OK (causal-timing correct: filed after close → reaction is next session)
8. "But the tone for the whole sector is already set." — OK
9. "Here is where the market closed today." — OK
10. "The Nifty fifty added zero point three four percent to twenty-three thousand nine hundred and sixty-three, a relief bounce after Wednesday's oil shock." — OK (day-name anchoring, prior session named)
11. "The banks did the heavy lifting, up zero point nine percent, because they had taken the worst of Wednesday's selling and repaired the most today." — OK
12. "The one red corner was technology, down about a third of a percent, as investors trimmed it ahead of the TCS result." — OK
13. "And the fear gauge, India VIX, collapsed almost nine percent to thirteen point four." — OK (VIX named and placed)
14. "That is the clearest sign the panic came off." — OK
15. "India did not move alone today." — OK
16. "Emerging-market shares were firm across the board, the main gauges up around one percent, and India simply traded alongside them." — OK
17. "This was shared relief, not an India-specific story." — OK
18. "Now the force under the day, and it is the same one that broke Wednesday: Iran." — OK (stylized but clear)
19. "On the supportive side, the conflict partly cooled during the session." — OK
20. "President Trump said on the record that he does not think America and Iran go back to full war, and the strikes that did land hit two islands, not Tehran or nuclear sites." — OK (long ~33w but single-thread, comma-segmented, speakable)
21. "That drained the panic." — OK
22. "Crude oil stopped rising, the rupee firmed a touch, and the fear gauge fell hard." — OK
23. "On the worrying side, nothing is actually settled." — OK
24. "This is rhetoric, not a signed ceasefire." — OK
25. "Oil is still up about nine percent on the week, gold stayed firm, and a United States tariff deadline on Indian goods still lands on the twenty-fourth of July." — OK (single-thread; timing framed as on-the-week, consistent with causal discipline)
26. "Now the movers." — OK
27. "The biggest gainer in the whole market was Kalyan Jewellers, up more than eighteen percent." — OK (name placed; "Jewellers" carries the business)
28. "Kalyan had posted a strong quarterly update on Monday, with sales up thirty-eight percent, but the stock fell nine percent that day on profit-booking." — OK
29. "Today reversed that overshoot, helped by a broad jewellery bid as gold firmed." — OK
30. "The update is the floor; the size of the jump is a snap-back." — FLAG (L4: mild metaphor — "the update is the floor" compresses the cause; recoverable in context but leans on image over plain chain)
31. "The biggest faller was Dr Reddy's Laboratories, down almost six percent, on a clean, company-specific cause." — OK ("clean" is mildly desk-ish but transparent)
32. "The company told the exchange that certain batches of semaglutide, the blockbuster weight-loss and diabetes drug, failed a quality specification because of an ingredient problem, so commercial supply will be delayed." — OK (drug named + placed; long but single-thread, cause→effect explicit)
33. "Dr Reddy's was first to win generic-semaglutide approval in India and Canada, so this dents a flagship product just as it launches." — OK
34. "A real setback, not a passing wobble." — OK
35. "The third was Swiggy, the food-delivery company, up almost seven and a half percent." — OK (name + what-it-does placed)
36. "Its foreign ownership fell below fifty percent, pushing domestic ownership over half for the first time, a step toward letting its quick-commerce arm hold its own stock like rival Blinkit." — FLAG (L4 + L6: the regulatory mechanism is over-compressed and unexplained — a naive listener cannot follow WHY foreign ownership under fifty percent lets "its quick-commerce arm hold its own stock," and "hold its own stock like rival Blinkit" assumes context the listener does not have; also long ~35w AND nested)
37. "Worth knowing, the analysts are split; JM Financial still rates it Reduce." — OK ("Reduce" reads as a sell-lean rating; acceptable)
38. "Here is the thread that struck me about today." — OK (first-person used once, as allowed)
39. "The same unresolved Iran risk that kept oil from crashing also kept gold firm, up about one percent." — OK
40. "And firm gold is a direct tailwind for jewellery retailers, whose inventory is worth more and whose sales value rises with the metal." — OK ("tailwind" immediately unpacked into the plain mechanism)
41. "That is the chain running under the day's loudest winners, Kalyan and the smaller jewellers all moving up together." — OK
42. "Geopolitics to gold to jewellery." — OK (punchy one-line recap of a chain already stated)
43. "Watch whether it holds if the tension actually eases and gold gives back that premium." — OK
44. "Now, what to watch." — OK
45. "Tomorrow brings the first real verdict on TCS, the first session the market can trade those numbers." — OK (timing correct)
46. "And in the evening, the Reserve Bank publishes its weekly figures, where the forex-reserves line matters most." — OK
47. "That's your brief." — OK
48. "Before I sign off: this has been general market commentary, not investment advice." — OK
49. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
50. "Markets are risky; you may lose money; act with care." — OK
51. "See you tomorrow." — OK

## Word count / TTS mechanics
- Body word count (SAY-hints stripped): **713** — marginally over the ~700 ceiling (~13 words). Within the "~" tolerance and consistent with recently accepted days (761 on 07-06). WARN, not FAIL.
- Em-dashes in body: **0**. Digits: **0** (all numbers spelled out). Symbols (₹ / % / $): **0**. TTS-clean.

## Punch list
- **[L4/L6 — primary] Sentence 36 (Swiggy):** the "foreign ownership below fifty percent → quick-commerce arm can hold its own stock like Blinkit" mechanism is packed and unexplained for a one-hearing listener, and the sentence runs long with nested clauses. Suggested rewrite (split + explain): "Its foreign ownership fell below fifty percent, so Indian investors now hold more than half for the first time. That matters because it moves Swiggy closer to letting its quick-commerce arm, its answer to Blinkit, list or hold shares on its own."
- **[L4 — minor] Sentence 30 (Kalyan):** "The update is the floor; the size of the jump is a snap-back." Consider a plainer close, e.g. "The strong update justified a rise; the size of today's jump was mostly the stock snapping back from Monday's overshoot."
- **[L5 word-count — minor] 713 words:** ~13 over the ceiling. If trimming, the two clauses above are the natural place to tighten without losing causation.

## Source spot-check (S1)
NOT RUN. The orchestrator explicitly withheld the brief (`briefs/public/2026-07-09.md`) to preserve the naive-listener stance for this cold read, overriding the skill's Step 2. Headline figures (Nifty +0.34% / 23,963, VIX −8.97% / 13.4, Kalyan +18%, Dr Reddy's −6%, Swiggy +7.5%, TCS +14% YoY / +0.4% CC) are therefore self-consistent within the script but unverified against the brief in this pass. Recommend a separate brief-informed run (or the principal's Step 7 read) close the S1 loop before TTS.
