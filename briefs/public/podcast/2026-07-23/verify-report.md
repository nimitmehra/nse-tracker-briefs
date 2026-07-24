# Verify Podcast Script — 2026-07-23

**Verdict:** WARN
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 2 / S1 0  (counts = FLAG hits)

Cold read done with the brief WITHHELD; brief opened only for the S1 spot-check below. Time-model note honored: covered session = "today" (Thu 23-Jul), "tomorrow/Friday" = 24-Jul (correct, not flagged). Rupee worded "near its weakest ever" / "toward its weakest-ever level" throughout — never "record" (correct, not flagged). SAY-hints (Ashiss Kumar Dash / Salil Parekh / C-I-E / H-F-C-L / IndiGo) are intentional TTS aids, not flagged.

## Per-sentence ledger

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK (matches exemplar)

**Hook**
4. "Today Indian shares fell for a fourth straight day, and the culprit was the same one that has driven the whole slide: oil." — OK (colon is a TTS pause, not an audio-breaker)
5. "Brent crude crossed one hundred dollars a barrel, up about seven percent, after fresh attacks on tankers near the Strait of Hormuz and in the Red Sea." — OK (long but single-thread)
6. "For a country that imports most of its oil, that lands straight on the bill and the rupee." — OK
7. "But this was an orderly fall, not a panic." — OK
8. "The fear gauge barely moved." — OK

**Close**
9. "Here is where the market closed today." — OK
10. "The Nifty fifty finished at twenty-three thousand eight hundred and sixty-nine, down about half a percent." — OK
11. "The fall was broad but shallow, with more stocks falling than rising, and the mid and small caps off about one percent." — OK
12. "The one striking non-move was technology." — OK
13. "The IT index closed flat, even though a rupee near its weakest ever normally helps software exporters who earn in dollars." — OK (weakest-ever framing correct)
14. "Two things cancelled that help." — OK
15. "An overnight global tech sell-off, and traders sitting on their hands ahead of Infosys, whose results were due after the close." — OK (fragment, but speaks cleanly)

**Divergence**
16. "And here is the part worth holding on to." — OK
17. "India fell, but it fell far less than the rest of the world, even as American and Asian markets were sold hard." — OK
18. "The reason was homegrown, not a global wave washing over everyone equally." — OK

**Two forces**
19. "Now the two forces that framed the day." — OK
20. "On the worrying side, oil got worse, not better." — OK
21. "Beyond the Strait of Hormuz, militants struck two Saudi tankers in the Red Sea, opening a second supply front, and a major pipeline halted its flows." — OK
22. "A sustained one hundred dollar oil feeds inflation and narrows the Reserve Bank of India's room to cut interest rates later this year." — OK
23. "On the supportive side, the one real cushion was domestic money." — OK
24. "Foreign investors sold about three thousand crore rupees of Indian shares, but domestic funds bought almost exactly the same amount, share for share, soaking up the entire foreign exit." — OK (long but single causal thread, cleanly comma-segmented — per L6, not flagged on length)

**Movers**
25. "Now the movers." — OK
26. "The biggest gainer was Tanla Platforms, a messaging-technology company, up about ten percent." — OK (name + what-it-does, in one breath)
27. "It posted a clean quarter, profit up twenty percent, and the market rewarded the beat on a red day." — OK
28. "The biggest fall was C-I-E Automotive India, an auto-parts maker, down about eleven percent." — OK
29. "Revenue grew, but profit margins missed, and the market punished the squeeze." — OK
30. "And a momentum name gave back." — OK
31. "H-F-C-L, a telecom-gear company, fell five percent, cooling off after running up more than ninety percent in three months." — OK

**Wedge**
32. "Here is what struck me most about today." — OK (first-person, once, matches exemplar)
33. "One oil shock hit this market in three completely separate places." — OK
34. "First, it pushed the state fuel retailers into losses, because the price they pay for crude jumped while the price they charge at the pump did not, and one of them posted its first loss in about fourteen quarters." — FLAG (L6: 39 words, nests because → while → and; the "price they pay… while the price they charge… did not" contrast plus the tacked-on loss clause is a lot to hold by ear. Longest sentence in the script.)
35. "Second, it blew up the fuel bill at IndiGo, the airline, tipping it into a quarterly loss." — OK
36. "And third, it pressed the rupee toward its weakest-ever level, which quietly raises the cost of everything India imports." — OK (weakest-ever framing correct)
37. "Same trigger, three different wounds." — OK
38. "That is why, for India, oil is never just a number on a screen." — OK

**Forward**
39. "Now, what to watch, and it all lands tomorrow, Friday." — OK (tomorrow = 24-Jul, correct)
40. "The big one is Infosys." — OK
41. "It reported after today's close." — OK
42. "Revenue beat, but profit fell about nine percent from the prior quarter, and it trimmed the top end of its full-year growth guidance to between one and a half and three percent." — FLAG (L6: the range said aloud — "to between one and a half and three percent" — stacks 'and a half and three' and is a genuine ear-stumble; 34 words. A listener can lose which numbers bound the range.)
43. "It also named a new chief executive, Ashiss Kumar Dash, to take over from Salil Parekh in April twenty twenty-seven." — OK (SAY-hints intentional)
44. "Its American-listed shares were already down about five percent overnight, so Friday's home-market reaction sets the tone for the whole technology pack." — OK ("American-listed shares" is good plain-English for ADR)
45. "And the United States tariff deadline on Indian goods also expires Friday, still unsigned." — OK

**Sign-off**
46-49. Disclaimer block ("That's your brief… See you tomorrow.") — OK (matches exemplar verbatim in structure)

## L5 mechanical sweep (body only, below the metadata separator)
- Em-dashes in body: none (all are hyphens: twenty-three, share for share, messaging-technology, auto-parts, telecom-gear, weakest-ever, home-market). PASS.
- Currency/percent symbols: none — all spelled out. PASS.
- Digits-not-words: none — all numbers narrated. PASS.
- Body length: 692 words per header, within the ~500–700 band (top end). PASS.
- (Metadata/composition notes above the `---` do contain em-dashes and %/− symbols, but those are stripped pre-TTS and are out of scope for L5.)

## Punch list (borderline — principal may ship)
- **[L6, sentence 34]** Split the fuel-retailer sentence. Suggested: "First, it pushed the state fuel retailers into losses. They pay more for crude, but cannot raise pump prices to match, and one of them posted its first loss in about fourteen quarters."
- **[L6, sentence 42]** Ease the guidance range so it lands aloud. Suggested: "…and it trimmed the top of its full-year growth outlook, now just one and a half to three percent."

## Source spot-check (S1) — PASS
Opened `briefs/public/2026-07-23.md` after the ledger. Every headline figure matches:
- Nifty 23,869.60 / −0.53% → "twenty-three thousand eight hundred and sixty-nine, down about half a percent." ✓
- Brent ~$100, +~7% → "one hundred dollars a barrel, up about seven percent." ✓
- VIX 13.48 / +1.39% → "fear gauge barely moved." ✓
- IT flat −0.06% → "IT index closed flat." ✓
- FII −₹2,999 cr / DII +₹2,947 cr → "about three thousand crore rupees… almost exactly the same amount, share for share." ✓
- Tanla +10.13%, PAT +20% → "up about ten percent… profit up twenty percent." ✓
- CIE Automotive −11.32%, margin miss despite revenue growth → "down about eleven percent. Revenue grew, but profit margins missed." ✓
- HFCL −5.00%, +94% 3M → "fell five percent… more than ninety percent in three months." ✓
- HPCL first loss in ~14 quarters → "first loss in about fourteen quarters." ✓
- IndiGo swung to a Q1 loss on fuel → "blew up the fuel bill at IndiGo… into a quarterly loss." ✓
- Infosys PAT −9% QoQ, FY27 guide top trimmed to 1.5–3.0%, Ashiss Kumar Dash succeeds Salil Parekh from 1 Apr 2027, ADR −5% → all narrated correctly. ✓
- US-India tariff deadline Friday 24-Jul, unsigned → "expires Friday, still unsigned." ✓
- Rupee: brief frames near record-weak (₹96.56 vs ₹96.84 all-time), NOT a fresh record → script says "near its weakest ever" / "toward its weakest-ever level." ✓ Correct, no record claim.

No number or direction mismatch. No wrong-day figure leakage.
