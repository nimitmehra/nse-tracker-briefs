# Verify Podcast Script — 2026-06-15

**Verdict:** PASS
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0  (counts = FLAG hits)

Cold-read ledger built FIRST with the brief withheld; brief opened only for the S1 spot-check below.

## Per-sentence ledger

1. "Good evening." — OK
2. "This is India Markets Brief from toroIQ." — OK
3. "Your read on today's session." — OK (evening anchor, "today" = covered session, correct per L3)
4. "The deal that markets only hoped for on Friday got signed over the weekend, and that single event powered today's session." — OK (Friday→Monday continuity stands alone; "only hoped for on Friday" vs "got signed over the weekend" makes the bridge clear to someone who missed Friday)
5. "The United States and Iran signed a fourteen-point agreement on Sunday to end their roughly hundred-and-seven-day war." — OK (names placed; "fourteen-point" / "hundred-and-seven-day" spelled out)
6. "The agreement reopens the Strait of Hormuz, the world's busiest oil shipping lane, and that sent crude tumbling." — OK (Hormuz placed with a plain what-it-is; clean cause→effect)
7. "For a country like India, which imports about eighty-five percent of its oil, cheaper crude is a direct relief, and the Nifty rose on it." — OK (mechanism stated plainly; percent spelled out)
8. "Here is where the market closed today." — OK
9. "The Nifty fifty finished at twenty-three thousand eight hundred and fifty-four, up almost one percent, with risers beating fallers about four to one." — OK (numbers spelled; "risers beating fallers" is plain English, not desk-shorthand)
10. "This was a broad rally, not a top-heavy one." — OK
11. "The wider Nifty hundred actually rose more than the giants." — OK ("the giants" reads as plain English for large-caps)
12. "Real estate led every sector, up almost four percent, because lower oil cools inflation, which points to lower interest rates, and property demand tracks home-loan costs." — OK (full cause→effect→so-what chain; long but single-thread, cleanly comma-segmented, says in one breath — exemplar-grade, not L6)
13. "Autos followed, up two and a half percent, helped by cheaper fuel and easier financing." — OK
14. "The one sector that fell was pharma, down about half a percent, as defensive stocks were sold to fund the rate-sensitive names." — OK ("defensive stocks" explained by the funding mechanism in the same sentence)
15. "The fear gauge, India VIX, eased to fourteen point three." — OK (VIX glossed inline as "fear gauge")
16. "There was a second piece of good news." — OK
17. "India's May inflation, released Friday, came in at three point nine three percent, comfortably inside the Reserve Bank's target band." — OK
18. "Cheaper oil and tame inflation together keep the door open for more rate cuts, and that is exactly what today's rally was pricing." — OK (plain so-what)
19. "Now the one honest caveat." — OK
20. "The deal is signed but not yet done." — OK (the load-bearing "signed-but-implementation-pending" line — explicit, not "war fully over")
21. "Clearing the mines from the Strait of Hormuz is assessed at forty to fifty days, and about six hundred ships are still stuck in the Gulf waiting on it." — OK (numbers spelled; concrete caveat)
22. "That is why crude fell on the signing but still sits about sixteen dollars above where it was before the war." — OK (mechanism for the residual; "sixteen dollars" spelled)
23. "The relief is real, but the last leg of it is not yet banked." — OK ("last leg not yet banked" is plain idiom, understandable cold)
24. "Now the movers." — OK
25. "The sharpest was Aarti Industries, a specialty-chemicals maker, up about thirteen percent on a run of long-dated contract wins, with cheaper crude an added feedstock relief." — OK (name + what-it-does + why; "feedstock" lightly technical but glossed by "added relief" context, acceptable for a chemicals maker)
26. "The cleanest trade-deal story was Balkrishna Industries, India's largest off-highway-tyre exporter, up about nine percent." — OK (name + what-it-does + magnitude)
27. "United States tariffs had halted its American shipments, and the weekend de-escalation directly reverses that overhang." — OK (clear cause→effect; "overhang" is mild but understandable)
28. "And Schneider Electric Infrastructure rose nearly ten percent after Goldman Sachs upgraded it to Buy." — OK (third-party rating attributed to Goldman; permitted carve-out, not the host's advice)
29. "Here is what struck me most about today." — OK (first-person wedge, exemplar voice)
30. "The fall in oil did not stay in oil stocks." — OK
31. "In fact the oil companies themselves barely moved." — OK
32. "For the state oil marketers, cheaper crude cuts both ways, since lower input cost is offset by weaker earnings at the upstream producers, so the two roughly cancel." — OK (full mechanism stated plainly; long but single-thread and speakable — not L6)
33. "Instead the relief travelled." — OK
34. "It eased the inflation outlook, which eased the expected rate path, which lifted property, autos and consumer names together." — OK (clean chained cause→effect)
35. "One geopolitical headline rotated money across half a dozen sectors at once, and that is why the rally was so broad." — OK (plain so-what closer for the wedge)
36. "Now, what to watch this week." — OK ("this week" — evening model, next-session events framed forward; correct per L3)
37. "The biggest scheduled event is the United States Federal Reserve, whose rate decision and projections land Wednesday night Indian time, and that sets the global rate mood India trades inside." — OK (forward-framed; plain why-it-matters)
38. "Then on Friday, the formal signing ceremony in Geneva, though the real-time gauge of whether this relief holds is simply the price of crude." — OK (day-name "Friday", not "tomorrow"; clear)
39. "That's your brief." — OK
40. "Before I sign off: this has been general market commentary, not investment advice." — OK (firebreak)
41. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
42. "Markets are risky; you may lose money; act with care." — OK
43. "See you tomorrow." — OK (evening sign-off, matches exemplar)

## TTS mechanical pass (L5)
- Numbers spelled out throughout (23,854 → "twenty-three thousand eight hundred and fifty-four", 3.93% → "three point nine three percent", $16 → "sixteen dollars", 14.3, 40-50, 600, 107 — all spelled). PASS.
- No ₹ symbol, no % symbol, no $ symbol in body. PASS.
- No em-dashes in body (checked every sentence). PASS.
- Spoken body ~637 words (within the ~500-700 band). PASS.

## L6 sentence-listenability pass
Sentences 12, 32 run long but are single-thread, cleanly comma-segmented, and speakable in one breath (exemplar has the same shape). No nested-clause lost-antecedent sentences. No L6 flag.

## Punch list
None. No FLAGs raised.

## Source spot-check (S1) — brief opened LAST

Checked against `briefs/public/2026-06-15.md`:

| Figure / claim | Script | Brief | Match |
|---|---|---|---|
| Nifty close | 23,854, up almost 1%, risers ~4:1 | 23,853.90, +0.98%, ~4:1 | ✅ |
| Nifty 100 vs 50 | wider 100 rose more | Nifty 100 +1.24% vs Nifty 50 +0.98% | ✅ |
| Realty | led, up almost 4% | +3.96% | ✅ |
| Autos | up two and a half percent | +2.60% | ✅ (reasonable round) |
| Pharma | down about half a percent, lone faller | −0.66%, lone red sector | ✅ |
| India VIX | eased to 14.3 | 14.35 (−2.5%) | ✅ |
| May inflation | 3.93%, inside RBI band | 3.93%, inside 2–6% band | ✅ |
| Deal | signed Sunday, 14-point, ~107-day war, signed-but-not-implemented | signed Sunday June 14, 14-point, ~107-day, implementation pending | ✅ |
| Hormuz | 40-50 days, ~600 ships | 40-50 days, ~600 ships | ✅ |
| Crude residual | still ~$16 above pre-war | still ~$16 above pre-conflict $67 | ✅ |
| Aarti | specialty-chemicals, +~13%, long-dated contracts + feedstock | AARTIIND +13.06%, contract wins + crude-feedstock relief | ✅ |
| Balkrishna | off-highway-tyre exporter, +~9%, US tariff reversal | BALKRISIND +8.91%, US tariff-reversal beneficiary | ✅ |
| Schneider | +~10%, Goldman upgrade to Buy | SCHNEIDER +9.99%, Goldman 'Buy' upgrade | ✅ |
| Fed | Wednesday night IST | June 16–17, lands Wednesday night IST | ✅ |
| Geneva ceremony | Friday | Friday June 19 | ✅ |
| Oil-stocks non-move | oil companies barely moved, marketers cut both ways | Nifty Energy +0.64%, marketers cut both ways | ✅ |

No wrong-day numbers, no direction mismatch. All headline figures trace to the brief. S1 PASS.

## Verdict line
**PASS** — clean cold read (0 FLAGs across L1–L6) and a clean source spot-check (0 S1 mismatches). Script is TTS-ready pending the principal's review gate.
