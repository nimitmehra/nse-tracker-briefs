# Verify Podcast Script — 2026-06-11

**Verdict:** PASS
**Checks:** L1 0 / L2 0 / L3 0 / L4 0 / L5 0 / S1 0  (counts = FLAG hits)

Cold read done first with the brief withheld; brief opened only for the Step 2 source spot-check. Geopolitics causal-timing trap checked explicitly (see notes below the ledger).

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (standard exemplar open)
2. "Today was a quiet red close that hid a one-sided story." — OK (plain; "hid a one-sided story" is a light frame but reads as a listener-friendly setup, not desk-shorthand or thesis-statement slop)
3. "The Nifty slipped just under a quarter percent, but almost all of that came from one corner, the IT pack." — OK (names the corner in the same breath; "just under a quarter percent" reads cleanly in TTS)
4. "Indian IT earns most of its money from American clients, so when US tech tumbled overnight, our IT fell straight down with it the next morning." — OK (full cause → effect → so-what, plain words)
5. "Here is where the market closed today." — OK (exemplar signposting)
6. "The Nifty fifty finished at twenty-three thousand one hundred and sixty-two, down zero point two three percent." — OK (numbers spelled, TTS-clean)
7. "The Sensex was down about the same." — OK
8. "The damage was concentrated." — OK (short, plain)
9. "Nifty IT fell one and a half percent, the worst sector, and is now off about five percent on the week." — OK
10. "It tracked last night's US tech selloff, where the Nasdaq fell around two percent and the chipmakers were hit hardest." — OK (mechanism plain; "chipmakers" listener-friendly)
11. "Against that drag, the defensives held." — OK ("defensives" is mild but immediately illustrated by the next sentence)
12. "Pharma rose, and Bank Nifty actually closed slightly green, with private banks the cushion that kept the index from falling further." — OK (single-thread, comma-segmented; reads in one breath)
13. "A midday recovery briefly took the Sensex back above seventy-four thousand, but it faded." — OK
14. "During Indian hours, Iran declared the Strait of Hormuz closed after fresh US strikes, and crude jumped about two and a half percent toward ninety-five dollars." — OK ("during Indian hours" correctly anchors this as a same-session, intraday input; NO scope/casualty/damage claim — only the declaration and the crude move are stated)
15. "For an oil importer like India, that revived the inflation worry, and the bounce gave way." — OK (plain mechanism; ties intraday escalation to the faded bounce — correct causal attribution for today)
16. "Now the flows." — OK
17. "Foreign investors sold again, about two thousand crore rupees, and domestic funds absorbed it." — OK (rounded cleanly for audio; matches brief's ~1,987 cr)
18. "That is the now-familiar pattern." — OK
19. "The rupee was the soft spot, weaker by about four-tenths of a percent, pressured by that foreign selling and the intraday oil spike." — OK
20. "Here is what struck me most about today." — OK (exemplar first-person wedge signpost)
21. "A weaker rupee should help Indian IT, because those companies earn dollars and spend rupees." — OK
22. "Today it did not help at all." — OK
23. "IT was still the worst sector." — OK
24. "The reason is that the worry about US tech demand was the stronger force." — OK
25. "If American clients tighten their budgets, Indian IT bills less, and that fear overwhelmed the currency benefit." — OK (plain, complete chain)
26. "When the cushion that should soften a fall gets overwhelmed, the market is pricing the bigger structural worry, not the day-to-day math." — OK (borderline near-meta, but it lands as a plain so-what payoff to the wedge, mirrors the exemplar's closing-the-wedge sentence; not desk-shorthand)
27. "There is one more turn worth knowing, and it sets up tomorrow." — OK (clean transition to forward inputs)
28. "After our three-thirty close, the picture flipped." — OK (explicitly time-stamps what follows as POST-close — the load-bearing firewall against the causal trap)
29. "The United States is reported to have cancelled the planned strike and signalled a deal, oil crashed back toward ninety dollars, and US and emerging markets surged." — OK ("is reported to have" = developing framing; de-escalation/crude crash/surge stated only as post-close facts, never credited with today's move)
30. "India did not trade any of that today, so it becomes Friday's setup." — OK (explicitly denies any same-session causal role — exactly the required framing)
31. "Now, what to watch, and it is Friday." — OK (evening-model: next session = Friday/tomorrow)
32. "India's May inflation figure lands, the first read that captures this crude spike, with fuel the swing factor." — OK
33. "A Reuters poll sees it near four percent, up from about three and a half in April." — OK (matches brief 4.0% from 3.48%)
34. "But read it against that post-close oil crash, which points the other way for June, so a hot May number could already be the high-water mark." — OK (the two-sidedness, plain)
35. "The same day brings the Reserve Bank's weekly reserves figure, the cleanest sign of how hard it is defending the rupee." — OK
36. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK (standard firebreak; matches exemplar)

## Geopolitics causal-timing trap — explicit confirmation

- **(a) US-Iran escalation stays reported/developing, no scope/casualty/damage claims:** PASS. Sentence 14 reports only "Iran declared the Strait of Hormuz closed after fresh US strikes" and the crude move; sentence 29 uses "is reported to have cancelled... and signalled a deal." No casualty, damage, or scope claim anywhere in the body.
- **(b) Post-close de-escalation / crude crash / US-EM surge framed ONLY as Friday/next-session inputs, NEVER as a cause of today's red close:** PASS. Sentence 28 stamps "After our three-thirty close, the picture flipped"; sentence 30 states "India did not trade any of that today, so it becomes Friday's setup." Today's red close is correctly attributed to (i) the overnight US-tech rout pulling IT down (sentences 3-4, 10) and (ii) the intraday Hormuz *escalation* capping the midday bounce (sentences 14-15). No sentence credits today's move to the de-escalation.

## Punch list
None. No L1/L2/L3/L4/L5/L6 flags. Sentence 26 was the closest call (a near-meta payoff line) but it functions as the plain so-what closing the first-person wedge, matching the exemplar's equivalent, so it is OK rather than a WARN.

## Source spot-check (S1)
All script figures trace cleanly to the brief (2026-06-11.md):
- Nifty 23,162 / −0.23% → brief 23,161.60 / −0.23%. Match (rounded for audio).
- Sensex "down about the same" → brief −0.20%. Match.
- Nifty IT −1.5% / −5% on week → brief −1.62% / about −5% week. Match (rounded down to "one and a half" — acceptable audio rounding).
- Nasdaq about −2%, chipmakers hardest → brief "Nasdaq fell about 2%, chipmakers Nvidia and Broadcom hardest." Match.
- Bank Nifty slightly green, pharma rose → brief Bank Nifty +0.14%, pharma +0.61%. Match.
- Midday Sensex back above 74,000, faded on Hormuz "closed" + crude +2.5% toward $95 → brief identical. Match.
- FII sell about 2,000 cr, DII absorbed → brief −₹1,987 cr / DII buy. Match (rounded).
- Rupee weaker about four-tenths percent → brief −0.41% to ₹95.75. Match.
- Post-close: US cancelled strike, oil crashed toward $90, US/EM surged → brief Lead + Connections + Watch. Match (framed post-close in both).
- May CPI poll near 4% from about 3.5% in April → brief 4.0% from 3.48%. Match.
- RBI weekly reserves figure Friday → brief RBI Weekly Statistical Supplement Friday June 12. Match.

No wrong-day numbers, no direction mismatch. S1 clean.
