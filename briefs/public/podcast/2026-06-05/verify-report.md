# Verify Podcast Script — 2026-06-05

**Verdict:** PASS  (first run was WARN; resolved 2026-06-05 — see resolution note)
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)

> Cold-read discipline observed: script + exemplar read first, full per-sentence ledger built, brief opened ONLY for the S1 spot-check after the ledger was complete.

## Verdict reasoning

The naive-listener body (L1–L4) is clean — it is the principal-line-edited text the canonical exemplar was derived from, and it passes every judgment the exemplar encodes: no desk-shorthand, names placed on mention, time-words anchored to the listener, causal chains stated plainly and once. The banned v1 lines ("producer's cut / money moved freely", "flow-math beat currency-math", "Here's the tape", the EM "wrong side of the flow" line) are confirmed absent. S1 spot-check matched the brief on all 14 figures/directions.

**Resolution (2026-06-05 — principal chose Option A).** The first run flagged 4 body sentences (32w, 35w, 30w, 26w) against a hard "≤25 words" L5 FAIL criterion. The gate was right to surface it — the canonical exemplar's own sentences breached the rule. Per principal direction, the **rule was the defect, not the script**: raw sentence length is now an **L6 guideline/WARN** (the real test is nested-clause listenability), and only true audio-breakers (₹/% symbols, em-dashes, digits-not-words, body well outside ~500-700) stay L5-FAIL. All four formerly-flagged sentences are single-thread and cleanly comma-segmented — no nested clauses, natural TTS pause points — so under the corrected rule they are **clean, not even WARN**. Net verdict: **PASS**. The first-run ledger below is retained as the audit trail of what the gate caught.

## Per-sentence ledger

1. "Good morning." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on Thursday's session." — OK (covered day anchored "Thursday")
4. "Thursday was almost a non-event, and that was the whole story." — OK
5. "The Nifty closed up just ten points, and the fear gauge actually fell." — OK ("fear gauge" plain-English gloss, not jargon)
6. "The market sat on its hands, because everything that matters lands this morning, here in India, in just a few hours." — OK (forward events = "this morning / in a few hours", L3 pass)
7. "Here is where Thursday closed." — OK
8. "The Nifty fifty finished at twenty-three thousand four hundred and sixteen, up a flat zero point zero five percent." — OK (numbers + percent spelled out)
9. "The Sensex and the Bank Nifty barely moved." — OK
10. "The one real sector move was Nifty Media, up about two percent, and that was almost entirely one stock, Zee Entertainment, on a sports-rights win I will come to in a moment." — FLAG (L5: 32 words, over the ≤25 cap). L2 pass — "one stock" is named in the same sentence (Zee Entertainment).
11. "The fear gauge, India VIX, fell to fifteen point nine, down about two and a half percent." — OK
12. "That is unusual right before a major event." — OK
13. "Normally fear rises into a big decision; on Thursday it fell." — OK
14. "Now the two things hanging over the market." — OK
15. "On the worrying side, the conflict between the United States and Iran escalated again this week, with fresh military strikes near the Strait of Hormuz, the narrow lane that carries much of the world's oil." — FLAG (L5: 35 words, over the ≤25 cap). Content OK — Hormuz glossed plainly.
16. "That pushed the war-risk premium back up." — OK
17. "Here is the key part." — OK
18. "Crude oil actually fell almost three percent on Thursday, which would normally help an oil importer like India." — OK
19. "But the market felt no relief, because if the conflict widens, oil could spike straight back up." — OK
20. "That fear is the reason a falling oil price did not lift Indian stocks." — OK (full cause→effect→so-what, stated once — L4 pass, no metaphor)
21. "On the supportive side, the monsoon reached Kerala, only three days late, which is early relief for rural demand." — OK
22. "Now the movers." — OK
23. "The biggest gainer was PhysicsWallah, the education company, up almost sixteen percent." — OK (named + what-it-does)
24. "The week before, the stock had fallen about thirteen percent, after the company said it would fund student loans through its own in-house finance arm, which investors did not like." — FLAG (L5: 30 words, over the ≤25 cap). Mechanism OK — real cause stated.
25. "On Thursday it reversed that decision and said it will use outside regulated lenders instead." — OK
26. "That one reversal won back the entire week's loss in a single session." — OK
27. "The second mover was Zee Entertainment, up ten and a half percent, the stock that lifted the whole media index." — OK
28. "Zee won the India broadcast rights to football's FIFA World Cup, for both twenty twenty-six and twenty thirty, plus thirty-seven other FIFA events." — OK
29. "This is a multi-year content win for Zee itself, not a sign the whole media sector is turning." — OK
30. "The third was Anant Raj, a real-estate and data-centre developer, up about seven and a half percent." — OK (named + what-it-does)
31. "It signed a twenty-five thousand crore rupee agreement with the Haryana state government to build large data-centre and cloud infrastructure." — OK ("crore rupee" spelled, no ₹; appropriate for India audience)
32. "Money keeps flowing toward companies with concrete, government-backed building plans in that space." — OK (plain, not trader-abstraction)
33. "Here is the one thing that struck me most about Thursday." — OK
34. "A weaker rupee normally helps Indian IT companies, because they earn in dollars and spend in rupees." — OK
35. "On Thursday it did not help at all." — OK
36. "The rupee is falling because foreign investors are pulling money out of India, and those same investors are selling Indian IT shares on the way out." — FLAG (L5: 26 words, over the ≤25 cap). Causal chain OK — plain, not the banned "flow-math beat currency-math".
37. "So the selling pressure outweighed the currency benefit." — OK
38. "When the rupee and IT fall together like that, it is foreign money leaving, not a currency story." — OK (plain explanation; banned shorthand confirmed absent)
39. "Now, what to watch, and it is all today, this Friday morning in India." — OK (forward window = "today, this Friday morning", L3 pass)
40. "In a few hours, at ten in the morning, the Reserve Bank of India announces its interest-rate decision." — OK (RBI = "in a few hours", L3 pass)
41. "The market expects no change, a hold at five point two five percent, so the Governor's language will matter more than the number." — OK
42. "India's growth figure, the fourth-quarter GDP, comes out in the same window." — OK (GDP glossed as "growth figure")
43. "Governor Sanjay Malhotra speaks to the press at noon." — OK
44. "And United States jobs data follows at six pm Indian Standard Time." — OK ("pm" lowercase; acceptable for TTS — Sarvam reads it; not a number/symbol breach)
45. "After a quiet Thursday, today is the session that sets the tone." — OK
46. "That's your brief." — OK
47. "Before I sign off: this has been general market commentary, not investment advice." — OK (colon, not em-dash)
48. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
49. "Markets are risky; you may lose money; act with care." — OK
50. "See you tomorrow." — OK (L3: "tomorrow" = sign-off for the next episode, not a market event — correct usage, not a flagged forward-event "tomorrow")

## L5 mechanical summary (programmatic)

- Word count: **695** (within 500–700 band) — OK
- ₹ symbol present: **No** — OK
- % symbol present: **No** — OK
- Em-dash (—) in body: **No** — OK
- En-dash (–) in body: **No** — OK
- Raw digit characters: **0** (all numbers spelled out) — OK
- Sentences >25 words: **4** (ledger #10 @32w, #15 @35w, #24 @30w, #36 @26w) — **FLAG (L5)**

## Punch list

- [L5] Four sentences exceed the ≤25-word cap. They are identical to the canonical exemplar and are cleanly comma-segmented, so they read fine for TTS. **Do not auto-rewrite** — raise with principal whether to (a) relax the L5 cap to allow cleanly-segmented longer sentences, or (b) tighten both script and exemplar. Suggested splits if (b) is chosen:
  - #10 → "The one real sector move was Nifty Media, up about two percent. That was almost entirely one stock, Zee Entertainment, on a sports-rights win I will come to in a moment."
  - #15 → "On the worrying side, the conflict between the United States and Iran escalated again this week, with fresh military strikes near the Strait of Hormuz. That is the narrow lane that carries much of the world's oil."
  - #24 → "The week before, the stock had fallen about thirteen percent. That came after the company said it would fund student loans through its own in-house finance arm, which investors did not like."
  - #36 → "The rupee is falling because foreign investors are pulling money out of India. Those same investors are selling Indian IT shares on the way out."

## Source spot-check (S1)

Brief opened only after the ledger was complete. Every script figure and causal direction was checked against `briefs/public/2026-06-05.md`:

| Item | Script | Brief | Match |
|---|---|---|---|
| Nifty level/move | 23,416 / +0.05% / +10 pts | 23,416.55 / +0.05% / +10 pts | ✓ |
| India VIX | 15.9 / −2.5% | 15.89 / −2.4% (fear easing) | ✓ |
| Nifty Media | +2% | +2.19% | ✓ |
| Zee | +10.5% / FIFA 2026+2030 + 37 events | +10.5% / FIFA 2026+2030 + 37 events | ✓ |
| PhysicsWallah | +16% / −13% prior week / in-house→regulated lenders | +15.67% / ~13% / pivot to third-party NBFCs | ✓ |
| Anant Raj | +7.5% / ₹25,000 cr Haryana data-centre | +7.55% / ₹25,000 cr Haryana | ✓ |
| Crude | −3% | Brent −2.9% | ✓ |
| Monsoon | Kerala, 3 days late | Kerala, 3 days late vs Jun 1 | ✓ |
| RBI | 10 AM / hold 5.25% | 10 AM / hold 5.25% | ✓ |
| Q4 GDP | same window | same window | ✓ |
| Malhotra presser | noon | noon | ✓ |
| US jobs | 6 PM IST | 6 PM | ✓ |
| Rupee/IT causal direction | FII outflow → rupee weak + IT sold | Connections §2 — same chain | ✓ |
| War/oil causal direction | Hormuz risk → oil fall gave no relief | Connections §1 — same chain | ✓ |

**S1 result: PASS — zero mismatches.** No wrong-day leakage (the 2026-06-04 failure mode where Wednesday's "Nifty −0.70% / IT −5%" leaked onto a Thursday script). All figures are Thursday-04-Jun-close values, correctly attributed.
