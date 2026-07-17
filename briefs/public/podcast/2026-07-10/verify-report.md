# Verify Podcast Script — 2026-07-10

**Verdict:** WARN
**Checks:** L1 3 / L2 1 / L3 0 / L4 0 / L5 0 / S1 0  (counts = FLAG hits; all borderline, none flagrant)

Cold read done against the exemplar with the brief closed; per-sentence ledger built first, brief opened only for the S1 spot-check.

## Per-sentence ledger

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK (matches exemplar opener)

**Hook**
4. "Indian shares rose for a second day running today, and the reason was earnings." — OK
5. "The June-quarter results season opened well." — OK
6. "Tata Consultancy Services, the country's largest software company, had reported strong numbers the night before, and that lifted the whole technology sector today." — OK (L2 name placed with what-it-does; L3 "the night before" correctly handles the Thursday post-close report)
7. "State-run banks then beat too, led by Indian Bank." — OK
8. "Money flowed back into technology, banks and property." — OK
9. "But one caveat runs under the whole day, and I will come back to it." — OK (signposts, doesn't defer a name)
10. "This was home-grown money, not foreign." — OK

**Market close**
11. "Here is where the market closed today." — OK
12. "The Nifty fifty added just over one percent, to twenty-four thousand two hundred and seven." — OK
13. "The banks did real work, up one point four percent, on that run of strong state-lender results." — OK ("did real work" is plain colloquial, understood on one hearing)
14. "Technology went from Thursday's worst corner to today's rally leader, the IT index up almost two percent on the read from TCS." — FLAG (L1 borderline: "the read from TCS" is desk-shorthand of the "the tell / the lens" family; comprehensible here because sentence 6 already established TCS lifted tech, so borderline not flagrant)
15. "And property was the single best sector, the realty index up three and a half percent." — OK
16. "Nearly twice as many stocks rose as fell." — OK (plain-English breadth)
17. "The fear gauge, India VIX, fell another eight percent to twelve point two five, close to a one-year low." — OK (names + defines the gauge)

**Caveat**
18. "Now that caveat about the money." — OK
19. "All week the story has been that foreign investors are coming back to India after a long exodus." — OK
20. "Over several weeks that is true." — OK
21. "But today itself does not support it." — OK
22. "Foreign investors were small net sellers." — OK
23. "It was Indian institutions, buying more than two thousand crore rupees, that carried the market up." — OK
24. "So do not read today's rise as proof foreign money drove it." — OK (clean so-what)

**Two forces**
25. "Now the two forces under the day." — OK
26. "On the supportive side, the Reserve Bank's weekly figures, out around five this evening, showed India's foreign-exchange reserves rose more than seven billion dollars, to about six hundred and seventy-four billion." — OK (L3 "this evening" fits evening model; single-thread, listenable)
27. "That is reserve building, not the central bank spending money to defend the rupee." — OK (L4 mechanism stated plainly)
28. "On the worrying side, the weather turned." — OK
29. "The weather office now expects below-normal rain across much of the country this month." — OK
30. "A weaker monsoon threatens rural demand and food prices, so watch consumer and farm-input names." — OK (cause to so-what)

**Movers**
31. "Now the movers." — OK
32. "The biggest single jump, Godrej Industries up sixteen percent, had no clean cause I could find, so I will not invent one." — FLAG (L2 borderline: "Godrej Industries" is named but given no what-it-does; mitigated because the line explicitly sets it aside as a no-story non-explanation, so comprehension of the narrative is not harmed)
33. "The clean stories were elsewhere." — OK
34. "Indian Bank rose almost ten percent after a strong first quarter." — OK
35. "Profit was up ten percent, and bad loans nearly halved, from three percent of loans to under two." — OK (bad loans explained in plain terms, no jargon)
36. "It opened the state-bank season, and Bank of Maharashtra beat on the same day, turning one result into a pattern." — OK
37. "The technology bounce showed up most in the mid-caps." — OK
38. "Zensar Technologies jumped almost fourteen percent, riding the TCS read plus heavy short-covering on more than fifty times its usual volume." — FLAG (L1 borderline x2: "the TCS read" desk-shorthand again, and "short-covering" is unexplained finance jargon a naive listener won't know; the sentence's gist survives — it jumped on the tech rebound plus heavy technical buying on huge volume — so borderline, not flagrant)
39. "The large software names moved far less." — OK
40. "The third was Greaves Cotton, up eleven percent." — OK
41. "Its electric-vehicle arm raised about three hundred and thirty crore rupees through a rights issue that was fully subscribed." — OK (places the company via its EV arm; "rights issue... fully subscribed" is understandable in context)
42. "That funds the EV business without leaning on the parent company." — OK (so-what)

**Wedge**
43. "Here is the one thing that struck me about today." — OK (first-person once, matches exemplar wedge)
44. "When fear drains out of a market, money flows first into the corners most sensitive to interest rates and sentiment." — OK (L4 mechanism, plain)
45. "That is why property led." — OK
46. "The odd part is this." — OK
47. "Property rose even as the United States ten-year bond yield ticked up, which normally hurts rate-sensitive real estate." — OK (single-thread, listenable; explains the norm it violates)
48. "Today a domestic-demand and earnings story simply overwhelmed that global signal." — OK
49. "Watch whether it holds if US yields keep climbing into next week's inflation reading." — OK

**Forward**
50. "Now, what to watch, and it is two clocks." — OK ("two clocks" is a light frame, immediately unpacked into monsoon + trade — L4 clean)
51. "The nearer one is the monsoon, whether the below-normal call actually verifies through the end of July." — OK
52. "The bigger one is trade." — OK
53. "A temporary ten percent United States tariff on Indian goods expires on the twenty-fourth of July, and while both sides call the talks constructive, nothing is signed." — OK (long but single-thread, cleanly comma-segmented; L6 not flagged on length alone)
54. "That deadline is the market's largest unresolved event." — OK

**Close**
55. "That's your brief." — OK
56. "Before I sign off: this has been general market commentary, not investment advice." — OK
57. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
58. "Markets are risky; you may lose money; act with care." — OK
59. "See you tomorrow." — OK

## Punch list (if any)
- [L1] Sentence 38 "short-covering" — unexplained finance jargon. Suggested rewrite: "...riding the same TCS lift, sharpened by traders who had bet against it rushing to buy back on more than fifty times its usual volume." (Explains the mechanism instead of naming it.)
- [L1] Sentences 14 and 38 "the read from TCS" / "the TCS read" — compressed desk-shorthand. Borderline because sentence 6 already established the link; if tightening, prefer "on the lift from TCS's results" / "riding that same TCS lift."
- [L2] Sentence 32 Godrej Industries has no what-it-does. Optional one-clause fix: "...Godrej Industries, a Godrej-group holding company, up sixteen percent, had no clean cause..." — but acceptable to ship as-is since it is an explicit non-story that the line dismisses.

None of the above are flagrant naive-listener breakers; all are eyeball-and-decide items for the principal. No L3 (time discipline) issues: covered Friday session is consistently "today," TCS's Thursday post-close report is "the night before," and all not-yet-happened events (monsoon end-July, tariff 24-July, next-week inflation) are framed forward. No L4 pervasive metaphor. No L5 audio-breakers (all numbers spelled out, no rupee/dollar/percent symbols, no em-dashes; body ~703 words, at the top edge of the 500-700 band, not "well outside"). No L6 unspeakable nested sentences.

## Source spot-check (S1)
All headline figures match the brief `briefs/public/2026-07-10.md` — 0 mismatches:
- Nifty +1.02% to 24,206.90 → script "just over one percent, to twenty-four thousand two hundred and seven" ✓
- India VIX 12.25, −8.29% → "another eight percent to twelve point two five, close to a one-year low" ✓
- DII +₹2,058 cr / FII −₹533 cr (domestic-led, foreign net sellers) → "Indian institutions, buying more than two thousand crore rupees" + "Foreign investors were small net sellers" ✓
- Indian Bank +9.78%, Q1 PAT +10% to ₹3,273 cr, GNPA 3.01%→1.86% → "almost ten percent," "Profit was up ten percent," "from three percent of loans to under two" ✓
- Bank of Maharashtra beat same day → "Bank of Maharashtra beat on the same day" ✓
- Zensar +13.60% (TCS read + short-covering ~52x volume) → "almost fourteen percent, riding the TCS read plus heavy short-covering on more than fifty times its usual volume" ✓
- Greaves Cotton +11.12%, EV-arm ₹331 cr rights issue subscribed → "up eleven percent," "about three hundred and thirty crore rupees through a rights issue that was fully subscribed" ✓
- Nifty Realty +3.49% (best sector) → "the realty index up three and a half percent," "single best sector" ✓
- Nifty IT +1.96% → "up almost two percent" ✓; Bank Nifty +1.39% → "up one point four percent" ✓
- FX reserves +$7.26 bn to $674.19 bn → "rose more than seven billion dollars, to about six hundred and seventy-four billion" ✓
- IMD below-normal July rain → "below-normal rain across much of the country this month" ✓
- Godrej Industries +16.28%, cause not established → "up sixteen percent, had no clean cause I could find, so I will not invent one" ✓
- US 10-year 4.57% ticked up → "the United States ten-year bond yield ticked up" ✓
- Temporary 10% US tariff expires 24 July, talks constructive/unsigned → "temporary ten percent United States tariff on Indian goods expires on the twenty-fourth of July, and while both sides call the talks constructive, nothing is signed" ✓

No number or direction contradicts the brief.
