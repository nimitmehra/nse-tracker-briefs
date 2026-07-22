# Verify Podcast Script — 2026-07-22

**Verdict:** WARN
**Checks:** L1 2 / L2 0 / L3 0 / L4 0 / L5 0 / S1 0  (counts = FLAG hits)

One-line: script is TTS-clean, correctly time-anchored to the evening model, every mover named-and-placed, all figures match the brief. Two soft jargon flags ("risk-off", "oil premium got worse") are the only marks — both borderline, neither flagrant. Principal may ship.

## Per-sentence ledger

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK

**Hook**
4. "Today Indian shares fell for a third day running, and this time the fear finally showed up." — OK (plain, sets the arc)
5. "The Nifty fifty slipped back below twenty-four thousand, and the market's fear gauge climbed." — OK (VIX glossed as "fear gauge")
6. "The reason was oil." — OK
7. "A fresh flare-up between the United States and Iran pushed crude sharply higher." — OK
8. "For a country that imports most of its oil, that lands straight on the bill." — OK (clear cause→effect; mild image but transparent)

**Close of day**
9. "Here is where the market closed today." — OK
10. "The Nifty fifty finished at twenty-three thousand nine hundred and ninety-six, down about eight tenths of a percent." — OK
11. "The damage was broad, with fourteen of the sixteen sectors red." — OK
12. "Financials led the way down, the Bank Nifty off about one and a quarter percent, its worst day of this slide." — OK
13. "The surprise was technology, down about one and a half percent, even though a weak rupee normally helps software exporters who earn in dollars." — OK (~24 words, single-thread, gloss built in)
14. "On a risk-off day, that currency help just got ignored." — FLAG (L1: "risk-off" is desk-shorthand; a non-finance listener may not parse it on one hearing. Borderline, not flagrant → WARN)
15. "Only staples and autos held green, both on their own earnings." — OK

**VIX**
16. "The real signal was the fear gauge, India VIX." — OK
17. "It rose five and a half percent, its first climb on a down day this week." — OK
18. "That tells you the selling turned from an orderly drift into something more nervous." — OK

**Divergence**
19. "And here is the unusual part." — OK
20. "Overnight, American markets rose, and emerging markets across the region gained nearly three percent, yet India fell anyway." — OK (overnight US correctly framed as next-day input contrasting the divergence, not a Wednesday driver)
21. "So this was not foreign money fleeing the whole region." — OK
22. "It was India going its own way, dragged down by an oil-import bill its neighbours do not carry." — OK (plain replacement for "decoupling"; good)

**Two forces**
23. "Two forces framed the day." — OK
24. "On the worrying side, the oil premium got worse." — FLAG (L1/L4 soft: "the oil premium got worse" is slightly oblique — a premium rises, it doesn't "get worse", and "premium" is unglossed. Rescued immediately by the next sentence's concrete price, so mild → WARN)
25. "Brent crude pushed toward ninety-five dollars a barrel." — OK
26. "That came after an eleventh night of United States and Iran strikes, and an attack on a tanker in the Strait of Hormuz." — OK
27. "That strait carries about a fifth of the world's seaborne oil." — OK (self-glosses why Hormuz matters)
28. "For India, costlier crude revives inflation worry and pressures the rupee." — OK
29. "On the supportive side, foreign investors were net buyers on Tuesday, about sixteen hundred and fifty crore rupees, while domestic funds sold." — OK (Tuesday flow correctly dated; FII data lags a day)
30. "One day, and it may not last, but worth watching." — OK

**Movers — Data Patterns**
31. "Now the movers." — OK
32. "The cleanest gain was Data Patterns, a defence-electronics company, up nearly thirteen percent." — OK (named + what-it-does in the same breath)
33. "It emerged as the lowest bidder for a project worth about thirteen hundred crore rupees from Hindustan Aeronautics, India's state aircraft maker." — OK (HAL glossed)
34. "One caveat, lowest-bidder status is not yet a signed contract." — OK (correct caveat, matches brief)
35. "Even so, the stock closed near its year high against a falling market." — OK

**Movers — Bandhan**
36. "The biggest fall was Bandhan Bank, down about seventeen percent." — OK
37. "The bank reported a strong quarter, profit up thirty-five percent, bad loans easing." — OK
38. "But management cut its forward profitability guidance, the number that shows how much a bank expects to earn on its assets next year, blaming rising deposit costs." — OK (~28 words but single-thread, cleanly comma-segmented; the nested clause is a helpful definition, not a listener-loser)
39. "The market sold the weaker outlook hard and looked past the good headline." — OK

**Movers — M&M Financial**
40. "The mirror was M and M Financial Services, up about eight percent." — OK (SAY-hint present for TTS; stripped pre-narration)
41. "Its profit jumped seventy-five percent, with its best asset quality in eight years." — OK

**Wedge**
42. "Here is what struck me most about today." — OK (first-person, once, as designed)
43. "Side by side, those two are the season's clearest lesson on how the market reads a bank." — OK
44. "Both grew profit, one by a third, one by three quarters, yet one fell seventeen percent and the other rose eight." — OK (vivid contrast, lands on one hearing)
45. "The difference was not last quarter's number." — OK
46. "It was the outlook." — OK
47. "A bank's forward guidance moves its stock more than the profit it just reported, because the market pays for next year, not last quarter." — OK (the payoff, stated plainly)
48. "And Bandhan's cut is a warning that may read across the whole small-lending pack." — OK

**What to watch**
49. "Now, what to watch." — OK
50. "Tomorrow, Thursday the twenty-third, Infosys reports its June-quarter results, the big technology verdict of the season, and the whole sector will trade off it." — OK (Infy = tomorrow/Thu, correct)
51. "And on Friday, the United States tariff deadline on Indian goods, still unsigned." — OK (Fri 24-Jul, correct)

**Sign-off**
52. "That's your brief." — OK
53. "Before I sign off: this has been general market commentary, not investment advice." — OK (colon in a spoken sign-off is fine, not an em-dash)
54. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
55. "Markets are risky; you may lose money; act with care." — OK
56. "See you tomorrow." — OK

## Punch list

- [L1, sentence 14] "On a risk-off day, that currency help just got ignored." — "risk-off" is desk vocabulary. Suggested plain rewrite: "On a day when investors were dumping anything risky, that currency help just got ignored." (Or lean on the fear already established: "With fear running high, that currency help just got ignored.")
- [L1/L4, sentence 24] "On the worrying side, the oil premium got worse." — "premium got worse" is oblique and unglossed. Suggested rewrite: "On the worrying side, oil kept climbing." (The next sentence already gives the price, so no meaning is lost.)

Both are WARN-grade only; neither is a flagrant naive-listener break. No FAIL condition present.

## Source spot-check (S1)

Opened `briefs/public/2026-07-22.md` after the ledger. All headline figures match:

| Figure | Script | Brief | Match |
|---|---|---|---|
| Nifty close / move | 23,996 / ~ −0.8% | 23,996.25 / −0.79% | ✓ |
| Sectors red | 14 of 16 | 14 of 16 | ✓ |
| Bank Nifty | ~ −1.25%, worst of slide | −1.23%, heaviest of slide | ✓ |
| IT | ~ −1.5% | −1.5% | ✓ |
| VIX | +5.5%, first up-on-down-day | +5.5% to 13.29, first rise on a down day in this slide | ✓ (script "this week" ⊇ the 3-day slide; not a contradiction) |
| EM / US overnight | EM ~ +3%, US rose | EEM +2.8%, S&P +0.89% / Nasdaq +1.29% | ✓ |
| Brent | toward $95 | ~$95, up 4-5% | ✓ |
| Hormuz / strikes | 11th night, tanker attack, ~1/5 seaborne oil | matches | ✓ |
| FII flow | Tue net buy ~1,650 cr, DII sold | FII +₹1,650 cr, DII −₹657 cr, Tue 21-Jul provisional | ✓ |
| DATAPATTNS | +~13%, HAL ~1,300 cr L1 bid | +12.70%, HAL ~₹1,300 cr L1 | ✓ |
| Bandhan | −~17%, +35% PAT, RoA guidance cut on deposit costs | −16.92%, +35% PAT, RoA 1.2-1.4 from 1.6-1.8, deposit costs | ✓ |
| M&M Fin | +~8%, +75% PAT, 8-yr-best asset quality | +8.09%, +75% PAT, 8-yr-best asset quality | ✓ |
| Forward events | Infy Thu 23-Jul; tariff Fri 24-Jul unsigned | Infy Thu 23-Jul; tariff Fri 24-Jul unsigned | ✓ |

No number or direction mismatch. No wrong-day leak. **S1 PASS.**

---

**Clears for TTS:** Yes, at principal discretion (WARN, not FAIL). The two soft jargon lines are optional one-word fixes; nothing blocks the Sarvam run.
