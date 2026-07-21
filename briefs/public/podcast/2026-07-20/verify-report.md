# Verify Podcast Script — 2026-07-20

**Verdict:** WARN
**Checks:** L1 0 / L2 0 / L3 0 / L4 1 / L5 0 / S1 0  (counts = FLAG hits)

Cold read done FIRST, brief withheld until after the ledger. One isolated desk-shorthand line ("sold the margin in both") — mild, context-recoverable, and traceable to the brief's own phrasing. Everything else lands on one hearing. Source spot-check is clean. Clears for TTS at principal discretion; a one-word fix removes the only flag.

## Per-sentence ledger

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK
2. "Today India's biggest private banks let the market down on the one number that matters most for a lender, its margin on loans." — OK (defines "margin" inline)
3. "HDFC Bank and Axis Bank each fell about five percent after their June-quarter results, and that single earnings theme pulled the whole market lower." — OK (names placed on mention; SAY-hint present)
4. "This was a home-grown bank story." — OK
5. "Here is where the market closed today." — OK
6. "The Nifty fifty slipped about four tenths of a percent, to twenty-four thousand two hundred and thirty-eight." — OK
7. "The Bank Nifty fell nearly one percent." — OK
8. "But the fall was shallow, because money did not leave the market." — OK
9. "It rotated inside it." — OK
10. "The day's clear winner was the state-owned banks, and that index jumped almost two point eight percent as government lenders reported strong quarters." — OK
11. "Pharma rose one point four percent, and energy, media and metals all closed higher." — OK
12. "India's fear gauge actually fell, to just under thirteen." — OK ("fear gauge" self-defines)
13. "That tells you this was an orderly, stock-specific sell-off, not a panic." — OK
14. "And here is the unusual part." — OK
15. "Across the region, emerging markets were higher today, yet India slipped anyway." — OK
16. "So this was not foreign money fleeing." — OK
17. "It was India going its own way, down on its own bank earnings." — OK
18. "It is the exact mirror of Friday, when India rose on good results while Asia fell." — OK
19. "Two things frame the week from here." — OK
20. "On the worrying side, the oil premium is back." — OK (phrase is compact but the next two sentences supply the full mechanism, so it lands)
21. "Over the weekend the standoff between the United States and Iran around the Strait of Hormuz flared up again, the narrow lane that carries much of the world's oil." — OK (Hormuz explained in-line)
22. "Brent crude spiked toward ninety-one dollars before easing back to about eighty-eight, now roughly thirty percent above its early-July lows." — OK
23. "For an oil importer like India, that revives the inflation worry that cheap oil had eased just weeks ago." — OK
24. "On the supportive side, domestic institutions bought more than thirteen hundred crore rupees today and fully absorbed the foreign selling, and Iran signalled it could reopen talks, which pared crude back off its high." — OK (long but single-thread, cleanly comma-segmented — not an L6 flag)
25. "Now the movers." — OK
26. "The cleanest gain of the day was D P Abhushan, a jewellery retailer, up more than seven percent." — OK (name + what-it-does; SAY-hint present)
27. "Its June-quarter revenue rose fifty-eight percent and profit seventy-seven percent, and it opened two new showrooms, with the board approving the result during the session." — OK
28. "The falls were the two private banks at the centre of the day." — OK
29. "HDFC Bank dropped about five percent." — OK
30. "Its margin fell to a record low of three point two six percent, and its lending income missed expectations." — OK ("lending income" = NII, plainly put)
31. "Axis Bank fell about five and a half percent." — OK
32. "Its headline profit jumped twenty-three percent, but that was flattered by a one-off write-back of past provisions, while the underlying margin still slipped." — OK ("write-back of past provisions" carries enough context)
33. "The market saw through the headline and sold the margin in both." — FLAG (L4: "sold the margin" is a compressed trader idiom — you don't literally sell a margin; it stands in for "sold the stock on the margin concern." The prior sentences make it recoverable, so this is an isolated slip, not pervasive.)
34. "And the mirror of that trade was Punjab National Bank, up more than five and a half percent." — OK
35. "This state-run lender's quarterly profit more than tripled, up two hundred and thirteen percent." — OK
36. "Here is what struck me most about today." — OK (the one first-person wedge)
37. "This margin squeeze is not a two-stock accident." — OK
38. "It is a signal for the whole large private-bank pack." — OK
39. "As the Reserve Bank has cut interest rates, banks' loan earnings reset lower faster than their deposit costs, so the spread narrows across every big private lender, not just these two." — OK (full plain mechanism)
40. "That is why the market treated the results as a cohort warning, and rotated into the cheaper state banks instead." — OK ("cohort warning" reads plainly after the setup)
41. "The counter-view from several brokers is that cheaper funding should ease the pressure ahead." — OK
42. "Whether that plays out is the read to track." — OK (matches exemplar's closing-idiom register)
43. "Now, what to watch." — OK
44. "On Wednesday the twenty-third, Infosys reports, the big technology verdict of the season." — OK
45. "And Thursday the twenty-fourth brings the United States tariff deadline, when a temporary tariff on Indian goods expires with the trade deal still unsigned." — OK
46. "That is the market's largest scheduled event, now four days out." — OK (Mon 20 → Thu 24 = 4 days)
47. "That's your brief. Before I sign off: this has been general market commentary, not investment advice." — OK
48. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
49. "Markets are risky; you may lose money; act with care. See you tomorrow." — OK

### Cross-check on the standing FAIL gates
- **L3 (time discipline):** clean. Covered session Monday 20-July = "today"; Wednesday 23 / Thursday 24 forward events = future ("On Wednesday", "brings"); Friday and the weekend bank results = past. No morning-model leftover, no future event framed as "today".
- **L5 (TTS mechanics):** clean. All body numbers spelled out (no digits leak from the metadata header into the narrated body), no ₹/%/$ symbols in the body, zero em-dashes. Body 698 words — inside the ~500–700 band, at the top edge.
- **L2 (name-on-mention):** clean. The PSU-bank index rise is attributed to a plural cohort ("government lenders"), and PNB gets its full name + mover treatment later; every company (HDFC Bank, Axis Bank, D P Abhushan, Punjab National Bank, Infosys) is named and placed on first mention.
- **L6 (listenability):** no flags — the two longest sentences (24, 39) are single-thread and comma-segmented, speakable in one breath.

## Punch list
- [L4, line 33] "The market saw through the headline and sold the margin in both." — optional one-word fix: "…and sold both on the margin." or "…and sold both stocks on the margin worry." Removes the only flag. Minor; principal may ship as-is since the mechanism is fully explained in the two preceding sentences (and the phrasing mirrors the brief's own "sold the margins in both").

## Source spot-check (S1)
Checked the script's headline figures against `briefs/public/2026-07-20.md` — all match, no number or direction mismatch:
- Nifty −0.39% / 24,238.50 ✓ ("about four tenths of a percent, to twenty-four thousand two hundred and thirty-eight")
- Bank Nifty −0.98% ✓ ("nearly one percent")
- Nifty PSU Bank +2.78% ✓ ("almost two point eight percent")
- Nifty Pharma +1.40% ✓; energy/media/metals all higher ✓
- India VIX 12.98 ✓ ("just under thirteen")
- Brent ~$91 intraday → $88.28, ~30% above early-July lows ✓
- DPABHUSHAN +7.36%, Q1 rev +58% / PAT +77%, two showrooms, board approved in session ✓
- HDFC Bank −5.12% ("about five percent"), record-low margin 3.26%, NII miss ✓
- Axis Bank −5.46% ("about five and a half percent"), PAT +23% write-back-flattered, margin slipped ✓
- PNB +5.66% ("more than five and a half percent"), PAT +213% ✓
- DII +₹1,312 cr fully absorbed FII −₹1,121 cr ✓; Iran signalled talks ✓
- Infosys Wednesday 23-July ✓; US tariff deadline Thursday 24-July, unsigned ✓; "four days out" ✓

**S1 verdict: PASS** — script is faithful to the verified brief; no wrong-day figure, no direction error.
