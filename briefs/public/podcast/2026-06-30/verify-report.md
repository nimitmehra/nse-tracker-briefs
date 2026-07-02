# Verify Podcast Script — 2026-06-30

STATUS: WARN

**Verdict:** WARN
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits) — two WARN-level punch-list items below, no FAILs.

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (exemplar opener verbatim)
2. "Here is the headline." — OK
3. "The index looked almost flat today, but that flatness was hiding a sharp fall in one corner of the market." — OK
4. "The Nifty fifty slipped just a third of a percent, yet underneath, India's big technology shares were sold hard." — OK
5. "Infosys and Tata Consultancy Services both fell to a fresh one-year low." — OK (names placed; IT context set by prior line)
6. "This was not a broad selloff." — OK
7. "Almost everything outside of technology closed green." — OK
8. "It was one sector being re-priced on its own, while the rest of the market held up." — OK ("re-priced" glossed by context)
9. "Here is where the market closed today." — OK
10. "The Nifty fifty finished at twenty-three thousand eight hundred and sixty-five, down zero point three four percent." — OK (matches close 23,865.75 / −0.34%)
11. "The Sensex and the Bank Nifty fell by about the same small amount." — OK
12. "But the one heavy weight was the technology sector, down two point seven three percent to a multi-year low." — OK (IT −2.73% matches brief)
13. "Everything else leaned green." — OK
14. "Realty led, up about one point three percent, and the broader market was positive, with the midcaps and the smallcaps both higher." — OK (Realty +1.31% matches)
15. "So this was not fear." — OK
16. "Money simply moved out of technology and into the home-facing parts of the market." — OK
17. "Now the two threads that shaped the day." — OK
18. "On the supportive side, cheap oil has become a real tailwind." — OK
19. "Brent crude closed the June quarter down about thirty percent, its biggest quarterly drop since twenty twenty." — OK (matches brief)
20. "For a country that imports most of its oil, that means softer inflation and a lighter import bill." — OK
21. "On the worrying side is the weather." — OK
22. "This June was the driest in over a hundred years, and that is a direct risk to the rural economy and to food prices." — OK
23. "The weather office has flagged a system over the Bay of Bengal around the third of July that could finally bring the rains." — OK
24. "Now the movers, and one policy ran through most of them." — OK
25. "Delhi approved a new electric-vehicle policy, effective tomorrow, with subsidies on electric two-wheelers and a plan to bar new petrol two-wheelers from twenty twenty-eight." — OK (long, single-thread, speakable — L6 fine; "effective tomorrow" = 1-July, time-anchor correct)
26. "So the electric-scooter makers jumped." — OK
27. "Ola Electric rose about eight percent and Ather Energy about five percent, to a record high." — OK (Ola +8.37%, Ather +5.24% 52-wk high — matches; pronunciation hint flagged below as WARN)
28. "But the same policy was a threat to old petrol bikes, so Eicher Motors, the maker of Royal Enfield, fell about five percent." — OK (name + what-it-makes in same breath; Eicher −4.75% ≈ "about five percent" — fair rounding)
29. "One policy, picking winners and losers inside the same auto pack." — OK
30. "Maruti Suzuki, meanwhile, rose about five percent on an upgrade from the brokerage Jefferies." — OK (Maruti +5.24% on Jefferies — matches)
31. "Here is the one thing that struck me most about today." — OK (wedge opener; first-person used once)
32. "On a normal day, two things lift India's technology exporters." — OK
33. "A weaker rupee helps, because they earn in dollars and spend in rupees." — OK
34. "And a rising American tech market helps, because it signals their clients are spending." — OK
35. "Today the market delivered both." — OK
36. "The rupee softened, and the US Nasdaq had closed up more than one percent overnight." — OK (Nasdaq +1.3% / rupee −0.22% — matches)
37. "And Indian technology fell anyway." — OK
38. "When a sector ignores both of its usual tailwinds, the weakness is fundamental, not noise." — OK
39. "The real fear is that artificial intelligence is starting to do the routine work these firms used to bill for." — OK
40. "That worry, not the global mood, is what sold them today." — OK (wedge resolves cleanly; sound logic)
41. "One more read, because today was quarter-end." — OK
42. "This was both monthly options expiry and the last day of the June quarter, the kind of session where foreign funds exit and prices can get distorted." — OK
43. "Foreign investors did sell, about two thousand five hundred crore rupees." — OK (FII −₹2,557 cr ≈ "about two thousand five hundred" — correct figure, NOT the stale −1,350)
44. "But domestic funds bought far more, almost seven thousand crore." — OK (DII +₹6,842 cr ≈ "almost seven thousand" — correct, NOT stale +2,801)
45. "So this was book-squaring, not capital flight." — OK ("book-squaring" immediately glossed by next line; naive-listener recovers)
46. "India's own savings absorbed the foreign exit cleanly, even on the year's most flow-heavy day." — OK
47. "Now, what to watch." — OK
48. "The earnings season opens in the middle of July." — OK
49. "Tata Consultancy Services reports first on the ninth, and Infosys follows on the twenty-third, and after today, those two results are the real test of whether this technology selloff is justified." — OK (9-July = TCS earnings, correct; NO pharma-tariff confusion)
50. "Closer in, tomorrow brings the June auto sales numbers and the final manufacturing survey." — OK (time-anchor: next session = "tomorrow", correct)
51. "And around the third of July, watch the monsoon for the rains to finally catch up." — OK
52. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK (exemplar disclaimer verbatim)

## Punch list

- **[L5/WARN] Bracketed pronunciation hints sit inside the spoken body.** Sentences 27 and 30 carry `[SAY: AH-ther]` and `[SAY: JEFF-reez]` inline. These are not em-dashes/symbols/digits, so not a hard audio-breaker on the listed criteria, BUT if `tts-podcast-nse.py` does not strip `[SAY: ...]` tokens, the engine will literally voice "say ah-ther / say jeff-reez." Fix: confirm the TTS preprocessor strips `[SAY: ...]`, OR move the hints to the metadata header and inline a phonetic spelling instead (e.g. "Ather Energy" → leave as is if the model says it correctly; "Jefferies" is reliably pronounced). Low effort, high safety.
- **[L6/WARN] Body runs ~727 words, about 27 over the 700 ceiling.** Agreeing with the script's own self-note: this is depth, not padding. The day genuinely carried two load-bearing stories (the IT re-pricing wedge + the Delhi EV winners/losers split) plus a quarter-end flows read; trimming further would drop causation, not filler. Ship at principal's discretion.

## Source spot-check (S1) — all clean

- Close: script "twenty-three thousand eight hundred and sixty-five, down zero point three four percent" vs brief 23,865.75 / −0.34% — MATCH.
- IT sector: script "two point seven three percent to a multi-year low" vs brief Nifty IT −2.73% multi-year low — MATCH.
- Realty: script "about one point three percent" vs brief +1.31% — MATCH.
- Movers: Ola +8% (brief +8.37%), Ather +5% record high (brief +5.24% 52-wk high), Eicher "about five percent" (brief −4.75%), Maruti +5% on Jefferies (brief +5.24% Jefferies) — all MATCH within fair rounding.
- FII/DII: script "about two thousand five hundred crore" sold / "almost seven thousand crore" bought vs brief −₹2,557 cr / +₹6,842 cr — MATCH (correct fresh figures, NOT the stale −1,350 / +2,801).
- Nasdaq: script "up more than one percent overnight" vs brief Nasdaq +1.3% — MATCH.
- Brent: script "down about thirty percent ... biggest quarterly drop since twenty twenty" vs brief — MATCH.
- 9-July: script frames it as "Tata Consultancy Services reports first on the ninth" vs brief "9 July is the TCS results date ... there is no '9 July' pharma date" — MATCH. **No 9-July pharma-tariff appears anywhere in the script. Confirmed clean.**
- Handle: script metadata states @nimitmehra, not @toroiq; brief channel bar uses @nimitmehra — MATCH. (Sign-off body carries no handle, which is fine.)

## Specific confirmations requested

(a) NO "9-July pharma-tariff" in the script — CONFIRMED. 9-July is correctly TCS earnings (sentence 49). Pharma dates (31-July / 29-Sep, generics exempt) are not misstated; the script omits the pharma watch entirely, which is acceptable trimming for a 727-word body.
(b) FII/DII = −2,557 cr / +6,842 cr — CONFIRMED correct ("about two thousand five hundred" / "almost seven thousand"); the stale −1,350 / +2,801 does NOT appear.
(c) Close 23,865.75 / −0.34% — CONFIRMED (sentence 10).
(d) The "IT fell despite a green Nasdaq and softer rupee = India-IT-fundamentals" wedge — SOUND. Both tailwinds were present (sentences 36), IT fell anyway (37), conclusion is fundamental-not-noise (38) with a named mechanism (AI eating billable routine work, 39). Logically tight and matches the brief's Connections section.
(e) Handle @nimitmehra, no @toroiq — CONFIRMED.
