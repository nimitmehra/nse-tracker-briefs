# Verify Podcast Script — 2026-06-09

**Verdict:** FAIL
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 1 / S1 0  (counts = FLAG hits)

The single FAIL is an L5 audio-breaker: a bracketed pronunciation directive left INSIDE the spoken body. It will be read aloud by TTS and garble the line. Everything else — voice, naive-listener clarity, time discipline, causal mechanism, and every number against the brief — is clean. One mechanical fix, then ship.

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK
2. "India closed green today, but only just, and the reason was made entirely at home." — OK (plain hook, leads with the consequential domestic-policy story)
3. "The Reserve Bank of India opened a new window today that pulls foreign-currency deposits into Indian banks." — OK
4. "Under it, the central bank itself pays the full cost of hedging fresh three-to-five-year deposits that banks raise from non-residents." — OK (explains the mechanism in plain words on first mention)
5. "That cuts what banks pay for funding, so bank stocks jumped and dragged the whole index up." — OK (clean cause → effect)
6. "The Nifty rose half a percent on the back of banks alone." — OK
7. "Here is where the market closed today." — OK
8. "The Nifty fifty finished at twenty-three thousand two hundred and forty-two, up zero point five two percent, and almost all of that lift came from financials." — OK
9. "The public-sector bank index led, up three point six percent, with every one of its twelve members green, and the broader Bank Nifty rose two percent." — OK (long but single-thread, comma-segmented, speakable — not an L6 flag)
10. "The one red sector was information technology, down half a percent." — OK
11. "The fear gauge, India VIX, fell more than eight percent to fifteen point six, the look of a relief session, not a conviction breakout." — OK (VIX named and glossed as "fear gauge")
12. "Now put India against Asia, because that is the gap." — OK
13. "Today the rest of Asia ripped on chip stocks." — OK ("ripped" is colloquial but clear to a naive listener; not desk-shorthand)
14. "Korea surged more than eight percent and tripped a circuit-breaker, Taiwan rose almost three and Japan over two, all on memory-chip optimism." — OK
15. "India barely owns that trade." — OK
16. "Its tech weight is software services, not chips, so India sat out the rally and had to make its own gain." — OK (explains why India is on the outside)
17. "And the flows confirm it." — OK
18. "Foreign investors were net sellers of four thousand five hundred crore rupees while domestic funds bought six thousand crore, and the rupee weakened even though the dollar was soft." — OK
19. "So today's green was a home-made policy bid, not foreign money coming back." — OK (clean so-what)
20. "Now the macro frame." — OK
21. "Today's deposit window sits on top of last week's bond-tax ordinance, which scrapped the taxes foreign investors pay on Indian government bonds." — OK
22. "Together they pushed the ten-year yield to a four-week low of six point nine percent." — OK
23. "But the rupee is still slipping and foreign money is still leaving, so this policy is a response to pressure that has not yet turned." — OK
24. "The monsoon is the standing food worry, forecast below normal at about ninety percent of average." — OK
25. "Now the movers." — OK
26. "The cleanest winner was JNK India, up almost sixteen percent." — OK
27. "The company makes heating equipment, and it won a large order from an Emirates engineering firm for an Abu Dhabi gas project, taking the stock up about ninety percent this year." — OK (plain "what it does" on first mention; "about ninety percent" rounds the brief's ~94% — acceptable)
28. "The second story was defence." — OK
29. "Data Patterns rose ten percent and Paras Defence almost eight, both at new highs, as twenty-five of twenty-seven tracked defence names rose on strong order-book outlooks." — OK
30. "This is the cohort the market is paying up for." — OK
31. "The third was Larsen and Toubro Technology Services [SAY: LARsen and toob-ROW Technology Services], up eight percent against a red IT sector, on the sale of one of its units." — **FLAG (L5: an inline TTS directive left in the spoken body). The bracketed string `[SAY: LARsen and toob-ROW Technology Services]` is a pronunciation note for the writer, not narration. TTS will read it aloud — the listener hears "...Larsen and Toubro Technology Services, say, lar-sen and toob-row Technology Services, up eight percent...". This is an audio-breaker.**
32. "A stock-specific win, not a sector turn." — OK
33. "Here is what struck me about today." — OK (first-person wedge, matches exemplar)
34. "One policy lever moved an entire sector at once, with thirteen of fourteen big lenders green." — OK
35. "But the relief is specific." — OK
36. "Affordable-housing financiers, which do not fund themselves with non-resident dollars, sat out, one of them basically flat while banks ran." — OK
37. "A funding subsidy helps the lenders that use that funding." — OK
38. "Do not assume it spreads to all of them." — OK
39. "Now, what to watch, and it is Friday." — OK
40. "India's May inflation figure lands, the first read after this policy package, and the food part is the one to watch given the weak monsoon." — OK
41. "The same day brings the Reserve Bank's weekly reserves figure, the cleanest sign of how hard it is defending the rupee." — OK
42. "One timing note." — OK
43. "After India closed today, United States markets were firm and US yields eased." — OK
44. "That is a Wednesday input for tomorrow's open." — OK (overnight US move correctly placed as next-session input, not today's cause — L3 clean)
45. "It did not lift today's close." — OK
46. "That's your brief. Before I sign off: this has been general market commentary, not investment advice." — OK
47. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
48. "Markets are risky; you may lose money; act with care. See you tomorrow." — OK

## Punch list

- **[L5 — FAIL, line 31]** Strip the inline directive from the body. The bracket `[SAY: LARsen and toob-ROW Technology Services]` must not survive into the TTS feed. Two clean options:
  - Remove the bracket entirely and let "Larsen and Toubro Technology Services" be narrated as written (Sarvam reads it acceptably), OR
  - Replace the company's first written form with the phonetic spelling so the model says it right without any visible tag, e.g. "The third was L and T Technology Services — the engineering arm of Larsen and Toubro — up eight percent..." (spell "L and T" so it reads as the initials, and gloss it once).
  - Suggested rewrite (cleanest): *"The third was L and T Technology Services, the engineering arm of Larsen and Toubro, up eight percent against a red IT sector, on the sale of one of its units."*
  - After the fix, re-run this gate before TTS — do not burn Sarvam credits on the bracketed version.

## Source spot-check (S1)

Opened the brief AFTER the ledger. Every headline figure traces:
- Nifty 23,242 / +0.52% — matches brief (23,242.10 / +0.52%). PASS
- PSU Bank +3.6%, all 12 members green — matches (3.62%, 12 constituents all green). PASS
- Bank Nifty +2% — matches (2.09%). PASS
- IT down half a percent (only red) — matches (−0.48%, only red). PASS
- India VIX more than eight percent to 15.6 — matches (−8.54% to 15.58). PASS
- Korea +8% circuit-breaker / Taiwan ~3 / Japan over 2, memory-chip — matches (KOSPI 8.18% buy-side circuit-breaker, TAIEX 2.76%, Nikkei 2.17%). PASS
- FII sell 4,500 cr / DII buy 6,000 cr — matches (FII −4,566 / DII +6,159). PASS
- Rupee weaker while dollar soft — matches (−0.41% to ₹95.34, DXY −0.29%). PASS
- 10Y at four-week low of 6.9% — matches (6.90%, four-week low). PASS
- Bond-tax ordinance last week scrapping foreign bond taxes — matches (FPI G-Sec ordinance June 5). PASS
- Monsoon ~90% of average, below normal — matches. PASS
- JNK +16% / Emirates firm / Abu Dhabi gas / ~90% this year — matches (15.70%, ADNOC TA'ZIZ Abu Dhabi, brief says ~94%; "about ninety" is an acceptable round). PASS
- Data Patterns +10% / Paras ~8% / new highs / 25 of 27 — matches (10.07%, 7.71%, 25 of 27). PASS
- L&T Technology Services +8%, against red IT, unit sale — matches (LTTS +7.98%, Smart World unit sale). PASS
- 13 of 14 big lenders green — matches The Connections ("13 of 14 Bank Nifty names green"). PASS
- Affordable-housing financiers sat out, one basically flat — matches. PASS
- CPI Friday June 12 + RBI reserves Friday — matches What-to-Watch. PASS
- Overnight US firm, yields eased, Wednesday input — matches Global Setup / Sources. PASS

No number or causal-direction mismatch. S1 = 0 flags. The only defect is the mechanical L5 bracket on line 31.
