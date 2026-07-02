# Verify Podcast Script — 2026-06-28

**Verdict:** PASS
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)

> Off-cycle context applied: this is a pre-open Monday weekend-catch-up episode. India had no session 26–28 June. The pre-open frame ("Good morning", "what to watch at today's open") is the correct frame for this special episode and is NOT flagged under L3. L3 was applied in spirit: weekend global moves treated as past, the Monday open and Tuesday expiry treated as forward. No time-logic errors found.

## Per-sentence ledger

**Opening (line 15)**
1. "Good morning." — OK (correct pre-open frame for this off-cycle episode)
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on what you missed over the long weekend, and what to watch at today's open." — OK (forward frame correct; "today's open" = the not-yet-happened Monday open, valid)

**The one thing (line 17)**
4. "Here is the one thing to understand before the market opens." — OK
5. "India did not trade for three days, so there is no fresh close to report." — OK (plain, honest, naive-clear)
6. "But two big global forces moved while we were shut, and they pull today's open in opposite directions." — OK
7. "Oil kept falling, which helps." — OK (cause→so-what, plain)
8. "And technology shares sold off worldwide, which hurts Indian IT." — OK
9. "The two roughly cancel out, and that is why the futures point to a flat, only-slightly-higher start, not a jump." — OK (mechanism stated plainly)

**Tailwind (line 19)**
10. "Start with the tailwind, because it is the cleaner one." — OK ("tailwind" is acceptable plain-English market term, immediately contextualised)
11. "Brent crude fell to about seventy-two dollars, a four-month low, and it is down more than ten percent on the week." — OK (numbers spelled, no symbols)
12. "Tankers are moving back through the Strait of Hormuz, the narrow lane that carries much of the world's oil, and Gulf supply has largely normalised." — OK (Hormuz placed/explained in same breath — name-on-mention satisfied)
13. "For a country that imports about eighty-five percent of its oil, cheaper crude is good news for the import bill, for inflation, and for the rupee." — OK (clean cause→effect; long but single-thread, comma-segmented — not an L6 flag)
14. "It keeps the same cheaper-fuel trade running that lifted the car-makers and the airlines on Thursday." — OK (L3: "on Thursday" = past event correctly anchored)

**Headwind (line 21)**
15. "Now the headwind, and this one is new." — OK
16. "Over the weekend, global technology shares sold off." — OK (weekend = past, correct)
17. "The United States Nasdaq fell for a fifth straight session, and the big Asian memory-chip makers, Samsung and SK Hynix, dropped hard." — OK (names placed with plain descriptor "memory-chip makers"; SAY tag for TTS)
18. "The trigger was abroad." — OK
19. "A report that the maker of ChatGPT may delay its share listing to twenty twenty-seven was read as the money funding the artificial-intelligence boom getting tighter." — OK (ChatGPT identified by what it is; mechanism plain; long but single-thread)
20. "The way that reaches India is through mood, not order books." — OK (plain, vivid but clear — not desk-shorthand)
21. "When global tech de-rates, Indian IT services tend to move with the gloom even when their own business has not changed." — OK ("de-rates" borderline jargon but immediately glossed by context "move with the gloom"; acceptable)
22. "So the most exposed corner at our open is IT, the names like TCS, Infosys, and HCL Tech." — OK (names placed)

**The picture for the open (line 23)**
23. "So here is the picture for the open." — OK
24. "The forward signal is the GIFT Nifty, the futures contract that points to where the Nifty is likely to start." — OK (GIFT Nifty explained in same breath — exemplary name-on-mention)
25. "It is sitting around twenty-four thousand and ninety, just above Thursday's close of twenty-four thousand and fifty-six." — OK (figures match brief; L3 "Thursday's close" past-anchored correctly)
26. "That is a muted, modestly-higher read." — OK
27. "Cheaper oil should help autos and airlines, names like Maruti, Mahindra, and IndiGo." — OK (names placed)
28. "The global tech wobble should weigh on IT." — OK
29. "To be clear, there are no weekend Indian movers to name, because the market did not trade." — OK (honest non-invention, matches brief Big Movers)
30. "The first fresh price action since Thursday is at today's open." — OK (L3 forward frame correct)

**The risk (line 25)**
31. "Here is the one risk that could upset all of this." — OK
32. "The entire cheaper-oil story rests on the Strait of Hormuz staying open." — OK
33. "Over the weekend the Iran-United States ceasefire frayed." — OK (past, correct)
34. "A tanker was hit, the United States struck Iranian military targets, and drones reached Bahrain and Kuwait." — OK (plain, factual; matches brief)
35. "Crude ignored it and kept falling, betting that supply stays normal." — OK
36. "But a real escalation that actually threatens Hormuz shipping is the single biggest risk to the whole trade." — OK
37. "It would push oil back up, pressure the rupee, and turn the import relief into an inflation worry." — OK (full causal chain, plain)
38. "That is the thing that could flip a calm open into a nervous one." — OK

**What to watch (line 27)**
39. "Now, what to watch." — OK
40. "Today, Monday, the Sensex monthly options contracts settle, so expect some positioning in Sensex futures and options." — OK (L3: "Today, Monday" = the live/forward session, correct for pre-open frame; matches brief What-to-Watch)
41. "Tomorrow, Tuesday the thirtieth, is the bigger event, the Nifty and Bank Nifty monthly expiry landing together with the June quarter-end." — OK (forward event = "tomorrow", correct; matches brief)
42. "And keep watching two things all day." — OK
43. "Brent crude, for whether the oil relief holds." — OK
44. "And the monsoon, where the July rainfall catch-up is the real swing factor for rural demand and food prices." — OK (matches brief)

**Sign-off (line 29)**
45. "That's your brief." — OK
46. "Before I sign off: this has been general market commentary, not investment advice." — OK (standard disclaimer)
47. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
48. "Markets are risky; you may lose money; act with care." — OK
49. "See you tomorrow." — OK

## Punch list
None. No FLAGs raised.

Minor watch-items (not flags, no action required):
- "de-rates" (sentence 21) and "tailwind/headwind" are mild market terms but are each glossed or contextualised on the spot, so they pass the naive-listener test. If the principal wants maximum plainness, "de-rates" could become "falls out of favour" — optional polish only.

## Source spot-check (S1)
Opened the brief AFTER completing the ledger. All headline figures verified, no mismatches:
- Brent ~$72, four-month low, >10% on the week — matches brief (lines 8, 10, 16, 28).
- GIFT Nifty ~24,090 pre-open vs Thursday close 24,056 — matches brief (lines 8, 9, 38). Direction (modestly higher) consistent.
- Nasdaq fifth straight loss; Samsung + SK Hynix dropped hard — matches brief (lines 16, 22).
- OpenAI/ChatGPT-maker IPO possibly delayed to 2027 as AI-funding-tightening trigger — matches brief (lines 16, 22, 72).
- 85% oil import dependence — matches brief (lines 28, "about 85%").
- IT cohort TCS/Infosys/HCL Tech as most exposed — matches brief (lines 38, 72).
- Autos/airlines Maruti, Mahindra (M&M), IndiGo as cheaper-fuel beneficiaries — matches brief (line 38).
- Hormuz risk: tanker hit, US struck Iranian targets, drones to Bahrain and Kuwait, crude kept falling — matches brief (line 74).
- Monday 29-June = Sensex monthly options settle; Tuesday 30-June = Nifty + Bank Nifty monthly expiry + June quarter-end — matches brief (lines 80, 81). Note: brief explicitly corrects Thursday's brief that mis-placed the whole expiry on Tuesday; the script correctly carries the corrected split.
- Monsoon July catch-up as swing factor — matches brief (lines 30, 84).

No wrong-day-number leak, no direction reversal. S1 PASS.

## TTS mechanical (L5)
- Numbers spelled out throughout (seventy-two, eighty-five percent, twenty-four thousand and ninety, etc.). PASS.
- No ₹ or % symbols in body. PASS.
- No em-dashes in body. PASS.
- Body length ~640 words (per header), within the ~500–700 band. PASS.
- SAY-tags present for tricky tokens (S-K Hynix, Chat-G-P-T, T-C-S, H-C-L Tech, gift NIFF-tee, IN-dee-go) — aids TTS, no defect.
