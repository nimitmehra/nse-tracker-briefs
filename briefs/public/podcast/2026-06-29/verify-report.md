# Verify Podcast Script — 2026-06-29

STATUS: PASS

**Verdict:** PASS
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 1 (WARN) / S1 0  (counts = FLAG hits)

The script is clean on every FAIL gate: naive-listener comprehension, name-on-mention, evening time discipline, mechanism-not-metaphor, and TTS mechanics. One L6 listenability WARN (a single long, multi-clause sentence). The source spot-check ties every headline figure back to the brief with no mismatch, and the script correctly avoids the wrong-day trap the brief itself flags (Thursday's 24,056 print).

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (matches exemplar opener)
2. "Here is the headline." — OK
3. "The oil shock that everyone feared all weekend simply did not arrive." — OK (strong hook, naive-clear)
4. "Over the long weekend the Gulf flared up, with American and Iranian strikes around the Strait of Hormuz, and India came back to work today braced for crude to spike." — OK (long but single-thread; Hormuz placed in the same breath)
5. "But on Sunday the United States and Iran agreed to halt the fighting and start talking." — OK
6. "So oil rose only about one percent, the rupee held flat, and the Nifty slipped just under half a percent." — OK (TTS-clean, percent spelled)
7. "A weekend that could have hit India hard ended as a cautious reopen, not a crisis." — OK
8. "Here is where the market closed today." — OK (L3: "today" = covered session, correct evening model)
9. "The Nifty fifty finished at twenty-three thousand nine hundred and forty-six, down zero point four six percent." — OK (numbers spelled out)
10. "The Sensex and the Bank Nifty fell by about the same." — OK
11. "Underneath, though, the story was a clean defensive split." — OK
12. "The safe corners were green." — OK (idiomatic but naive-clear)
13. "Pharma led, up about one percent, with Healthcare just behind it, both bid up as money looked for shelter." — OK
14. "The corners that sold were Auto, down two percent, and IT, down about one percent." — OK
15. "The fear gauge, India VIX, ticked up a little but stayed deep in calm territory." — OK (VIX glossed)
16. "Now the two threads that shaped the day." — OK
17. "On the relief side, the feared oil shock was defused." — OK
18. "Through the weekend the Strait of Hormuz looked like a real crisis, with strikes and tankers hit." — OK
19. "For a country that imports about eighty-five percent of its oil, that is the worst combination, a higher import bill and a weaker rupee." — OK (mechanism plain)
20. "But the Sunday deal capped crude near a four-month low, so the import-bill channel never fired." — OK (cause → effect)
21. "On the policy side, there was good news for drug-makers." — OK
22. "The United States extended its pause on new pharmaceutical tariffs to the ninth of July, which eased the pressure on Indian generic exporters and powered that pharma bid." — OK
23. "Now the movers, and the framing matters on each." — OK
24. "The biggest fall was Persistent Systems, down eleven percent to a one-year low." — OK (placed as a tech firm by the next two sentences)
25. "This was not the global tech selloff." — OK
26. "Persistent made a takeover offer for all of Germany's Nagarro, and the market sold the deal on its size and its integration risk." — OK (Nagarro named + placed as German company)
27. "That is a company-specific decision, not a sector story." — OK
28. "Next was Netweb Technologies, down about ten percent." — OK
29. "Netweb called a board meeting to consider raising fresh money, which can dilute existing shareholders, and at over a hundred times earnings it was the most exposed name when Friday's worry about artificial-intelligence valuations reached India." — FLAG (L6: ~40 words and chains four ideas — board meeting → dilution → 100x earnings → AI-valuation worry. Speakable but dense; WARN, not FAIL.)
30. "The cleanest gainer was Schneider Electric Infrastructure, up almost nine percent, on a twenty-seven percent jump in its order book and the broad electrification re-rating." — OK (borderline "electrification re-rating" but contextually clear)
31. "Here is the one thing that struck me most about today." — OK (first-person wedge, matches exemplar)
32. "The worst sector was Auto, down two percent, and the easy reading is that high oil hurt the carmakers." — OK
33. "But that is wrong." — OK
34. "Auto fell on policy, not on fuel." — OK
35. "Delhi approved a new electric-vehicle policy, with a fat subsidy on electric two-wheelers and a plan to ban new petrol two-wheelers from twenty twenty-eight." — OK
36. "So the electric-scooter maker Ather Energy jumped about eight and a half percent, while the old petrol-engine makers sold off." — OK (Ather named + placed)
37. "The index fall is just the legacy leg of that split." — OK
38. "Policy is picking winners inside the auto pack, and the market is repricing who is on which side." — OK
39. "Now, what to watch, and it is tomorrow." — OK (L3: next session = "tomorrow", correct evening model)
40. "Tuesday the thirtieth is a double event." — OK
41. "The Nifty and Bank Nifty monthly options expire on the same day as the June quarter-end, so expect heavier positioning." — OK
42. "Beyond that, the monsoon is still the home-grown worry, with June on track to be the driest in about a hundred and forty-six years." — OK
43. "And keep an eye on oil." — OK
44. "The Hormuz truce is defused, not closed, so crude stays the swing risk if it frays." — OK
45. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK (standard exemplar close)

## Punch list

- [L6 — optional, principal may ship as-is] Sentence 29 (Netweb) is the one dense line: it stacks the board meeting, the dilution risk, the 100x valuation, and the AI-valuation wobble into one ~40-word breath. Splitting it reads cleaner aloud, e.g.: "Next was Netweb Technologies, down about ten percent. Netweb called a board meeting to consider raising fresh money, which can dilute existing shareholders. And trading at over a hundred times earnings, it was the most exposed name when Friday's worry about artificial-intelligence valuations reached India." Not a blocker — the line is single-thread and speakable; this is polish only.

## Source spot-check (S1)

Opened the brief (`briefs/public/2026-06-29.md`) only after the ledger. Every script figure traces with no mismatch:

- Close 23,946 / down 0.46 percent → brief line 8 + Lead line 16. Match.
- Sensex / Bank Nifty "fell by about the same" → −0.48% / −0.77%, line 8. Match.
- Pharma up ~1% (1.03%), Healthcare just behind (0.94%) → lines 8, 40. Match.
- Auto down 2% (2.08%), IT down ~1% (1.07%) → lines 8, 40. Match.
- VIX up a little, stayed calm → 13.61 (+4.3%), line 9. Match.
- Oil up ~1% near a four-month low; rupee flat; ~85% oil imports → Brent ~$72.80 +1.1%, rupee 94.53, line 9/30. Match.
- US pharma-tariff pause extended to 9 July → line 32. Match.
- Persistent −11% to a one-year low; Nagarro (Germany) takeover; M&A not the selloff → −11.22% 52-week low, €81 Nagarro, lines 56/79/101. Match.
- Netweb ~−10%; fund-raise/dilution; "over a hundred times earnings"; AI-valuation wobble → −9.89%, ~126x earnings, lines 57/80/102. Match (script's "over a hundred times" is true against 126x).
- Schneider ~+9%, order book +27%, electrification → +8.86%, +27.4% orders, lines 69/92. Match.
- Ather ~+8.5%; Delhi EV policy; petrol two-wheeler ban 2028 → +8.51%, April 2028, lines 70/93/119. Match.
- Tuesday 30th double event (Nifty/Bank Nifty expiry + quarter-end) → line 127. Match.
- Monsoon driest in ~146 years → lines 34/130. Match.

No wrong-day leak: the script uses Monday's −0.46% / 23,946 close, correctly avoiding the Thursday 25-June "24,056 / +0.14%" print the brief explicitly flags as a stale aggregator number (line 138). S1 PASS.
