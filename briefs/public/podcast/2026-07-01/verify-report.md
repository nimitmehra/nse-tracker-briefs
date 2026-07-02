# Verify Podcast Script — 2026-07-01

**Verdict:** WARN (ship-eligible)
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)
**One WARN:** body ~733 words, 33 over the 700 ceiling (borderline, on par with yesterday's accepted 727 — not an L5 "well outside" audio-breaker).

## Per-sentence ledger

**Open (line 17)**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK (evening model, L3 clean)

**The story of today (line 19)**
4. "Here is the story of today." — OK
5. "India and the United States are close to a trade deal, and the hope of it lifted the market." — OK (unsigned framing: "hope of it")
6. "Officials call the talks very close, with only about one percent left to settle." — OK
7. "But nothing is signed, and the clock is ticking, because a temporary American tariff on Indian goods expires on the twenty-fourth of July." — OK (unsigned + deadline, plain cause)
8. "That hope, along with cheaper oil, pushed the Nifty fifty up a little over half a percent and snapped a two-day fall." — OK
9. "Yet underneath the green, one corner kept sinking." — OK (plain image, not desk-shorthand)
10. "India's technology shares fell again, to a fresh three-year low." — OK (sector named plainly)
11. "So today was really two markets in one." — OK (L3 "today", correct)

**Where the market closed (line 21)**
12. "Here is where the market closed today." — OK
13. "The Nifty fifty finished at twenty-four thousand and six, up zero point five nine percent." — OK (spelled out)
14. "The Sensex and the Bank Nifty rose by about the same small amount." — OK
15. "But the real story was the gap between sectors." — OK
16. "Money moved out of technology and into home-facing shares." — OK (understandable via contrast; "home-facing" = domestic)
17. "Realty led, up about three and a half percent." — OK
18. "Consumer goods, media and autos all rose more than one percent." — OK
19. "Technology was the lone loser, down two percent, to a three-year low." — OK
20. "That is a spread of more than five percentage points between the best and worst corners, on a day the index barely moved." — OK (long but single-thread, L6 pass)

**EM context (line 23)**
21. "There was one more piece of context." — OK
22. "After India had closed, emerging-market shares elsewhere fell more than two percent, on a jump in American bond yields." — OK (L3: correctly framed as after-close / next-session input)
23. "But India had already closed higher on its own, a home-driven up-day standing apart from that weaker crowd." — OK

**Two forces (line 25)**
24. "Now the two forces under the day." — OK
25. "On the supportive side, three things lined up." — OK
26. "Cheaper oil is showing up in company accounts." — OK
27. "Hindustan Unilever said its input costs should ease as crude falls, part of why consumer shares led." — OK (name placed + pronunciation gloss stripped in narration)
28. "June's goods-and-services-tax collection hit a record, about one lakh ninety-five thousand crore rupees, up nearly fourteen percent on a year earlier." — OK (long but single-thread; spelled out)
29. "And June car and two-wheeler sales were strong." — OK
30. "On the worrying side is the weather." — OK
31. "This June closed about forty percent short of normal rain, a direct threat to rural incomes and food prices." — OK (plain cause -> so-what)

**Movers (line 27)**
32. "Now the movers." — OK
33. "The biggest gainer was Paisalo Digital, a small non-bank lender, up almost twenty percent to a fresh high on promoter confidence." — OK (name + what-it-does in same breath)
34. "Its own promoters raised their stake to about forty-seven percent, which the market read as a vote of confidence rather than an operating update." — OK
35. "The biggest fall was the face of the technology weakness." — OK
36. "KPIT Technologies dropped almost seventeen percent to a one-year low." — OK
37. "The company warned that its June-quarter dollar revenue will fall about one percent on a year earlier." — OK
38. "That is its first revenue decline in twenty-three quarters, as some European carmakers pulled back after their own profit warnings." — OK (mechanism stated plainly)
39. "Several brokerages cut their targets." — OK
40. "The third mover was RITES, the state-owned transport consultancy, up about fourteen percent, after winning a fresh order worth about one hundred and seventy-five crore rupees." — OK (name + what-it-does + why)

**The wedge / first-person (line 29)**
41. "Here is the one thing that struck me most about today." — OK (single sanctioned first-person)
42. "A weaker rupee normally helps India's technology exporters, because they earn in dollars and spend in rupees." — OK (full mechanism)
43. "Today the rupee did weaken, and technology fell to a three-year low anyway." — OK
44. "When a sector ignores its own tailwind, the weakness is about demand, not the currency." — OK (the tell, stated plainly not as jargon)
45. "The worry is structural." — OK
46. "Artificial intelligence is starting to do the routine work these firms used to bill for, and American interest rates are staying high." — OK
47. "KPIT's first revenue fall in twenty-three quarters put a single name to that fear." — OK

**What to watch (line 31)**
48. "Now, what to watch." — OK
49. "Around the third of July, watch the monsoon, where a Bay of Bengal system is expected to finally bring July's rains." — OK (L3: forward event, correctly next-session)
50. "The same Friday, the third, brings American jobs data, which matters more now that United States interest rates are weighing on Indian technology." — OK
51. "Then Tata Consultancy Services reports on the ninth, and Infosys follows on the twenty-third." — OK (full name, not "TCS" cold)
52. "And the big one is the twenty-fourth of July, when that temporary American tariff on Indian goods expires, and the trade deal is still unsigned." — OK (unsigned framing held to the close)

**Close (line 33)**
53. "That's your brief." — OK
54. "Before I sign off: this has been general market commentary, not investment advice." — OK
55. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
56. "Markets are risky; you may lose money; act with care." — OK
57. "See you tomorrow." — OK

## TTS mechanical (L5)
- No digits in narration — all numbers spelled out. PASS
- No ₹ / % / $ symbols in body. PASS
- Zero em-dashes in body (hyphenated compounds only: two-day, three-year, non-bank, June-quarter, goods-and-services-tax, Bay of Bengal). PASS
- Word count ~733 (33 over 700) — borderline, NOT "well outside" the band -> WARN, not FAIL.

## Punch list
- [L5/word count] Optional trim of ~30 words if the principal wants it inside the ceiling. Lowest-value cut candidate: sentence 14 ("The Sensex and the Bank Nifty rose by about the same small amount.") is the most compressible without losing causation. Not required to ship.

## Source spot-check (S1) — all clean
| Figure in script | Brief | Match |
|---|---|---|
| Nifty 24,006, +0.59% | 24,005.85, +0.59% | ✓ |
| IT "down two percent", three-year low, lone loser | IT −2.01%, three-year low, lone red | ✓ |
| Realty "about three and a half percent" | +3.58% | ✓ |
| EM shares "more than two percent" after close, US yields | EEM −2.32%, US 10-yr 4.47% | ✓ |
| GST "one lakh ninety-five thousand crore, nearly fourteen percent" | ₹1,94,812 cr, +13.9% | ✓ |
| June rain "forty percent short" | ~40% short | ✓ |
| Paisalo "almost twenty percent", stake "forty-seven percent" | +19.86%, promoters ~46.7% | ✓ |
| KPIT "almost seventeen percent", one-year low, "about one percent" fall, 23 quarters | −16.98%, 52-wk low, ~1% YoY, first drop in 23 quarters | ✓ |
| RITES "about fourteen percent", "one hundred and seventy-five crore" | +14.02%, ~₹175 cr | ✓ |
| Trade deal "one percent left", unsigned, 24-July deadline | "only ~1% left", unsigned, 24 July | ✓ |
| TCS 9th, Infosys 23rd, US jobs Fri 3rd, monsoon ~3rd | TCS 9 Jul, Infosys 23 Jul, jobs 3 Jul, Bay-of-Bengal ~3 Jul | ✓ |

No number or direction mismatch. No wrong-day leak.

## Verdict rationale
No L1/L2/L3 hits, no pervasive L4, no L5 audio-breaker, no S1 mismatch. The single WARN is the 33-word overage above the 700 ceiling, which the skill treats as borderline (not "well outside") and which matches yesterday's accepted 727-word precedent. The script is a clean cold-read pass on every substantive gate: a naive listener follows it end to end, every name is placed on mention, the trade deal is framed unsigned in both the hook and What-to-Watch, the evening time model holds, and the hook lands ("today was really two markets in one"). **TTS-ready.**
