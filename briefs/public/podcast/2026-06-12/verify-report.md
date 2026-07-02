# Verify Podcast Script — 2026-06-12

**Verdict:** WARN
**Checks:** L1 1 / L2 0 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0  (counts = FLAG hits)

Cold read done first (brief withheld). One L1 desk-shorthand flag ("the quiet tell"). Everything else clean. The load-bearing content test passes decisively: a naive listener hears the US–Iran deal as REPORTED and UNSIGNED, not a done deal. Source spot-check against the brief found zero number/direction mismatches.

## Per-sentence ledger (body, lines 16–34)

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK
2. "Today was a big, broad relief rally, but it leaned on a deal that nobody has actually signed yet." — OK (unsigned caveat in the first content sentence)
3. "The Nifty jumped almost two percent on reports the United States and Iran had agreed a draft to wind down their conflict." — OK ("on reports" + "a draft" = reported framing)
4. "The reported terms reopen the Strait of Hormuz, the world's busiest oil lane, and that sent crude tumbling." — OK ("reported terms"; Hormuz glossed on mention)
5. "For a country that imports most of its oil, like India, cheaper crude is a direct relief." — OK
6. "Here is where the market closed today." — OK
7. "The Nifty fifty finished at twenty-three thousand six hundred and twenty-three, up one point nine nine percent." — OK (numbers spelled)
8. "The Sensex rose two point three percent." — OK
9. "This was as broad as it gets." — OK
10. "All thirty Sensex stocks closed green, and the smaller companies rose even harder than the headline." — OK ("closed green" widely understood)
11. "The engine was the banks, up almost three percent, because lower oil and softer inflation both point to an easier path for interest rates, which helps lenders." — OK (long but single-thread, full cause→effect)
12. "Real estate led all sectors, up three and a half percent, for the same rate-cut logic, since home demand tracks loan costs." — OK
13. "The one corner that did not rise was IT, and I will come back to why." — OK (sets up the wedge)
14. "There was a second, home-grown piece of good news the same afternoon." — OK
15. "India's May inflation came in at three point nine three percent, just below the four percent economists expected." — OK
16. "That eases the worry that the Reserve Bank would have to stop cutting rates." — OK
17. "Softer inflation plus cheaper oil is exactly the mix that lifts banks and property." — OK
18. "Now the one caution that sits over everything." — OK
19. "The deal is only reported, not signed." — OK (explicit unsigned statement)
20. "Iran's foreign ministry publicly called it, quote, merely speculation." — OK ("quote" cues the quote in audio)
21. "The real test is a reported signing in Geneva this Sunday, the fourteenth of June." — OK (names the swing event + date)
22. "If it happens, today's move is confirmed." — OK
23. "If it slips, the crude relief that powered today can reverse, and Monday could open with a gap the wrong way." — OK ("gap the wrong way" is mild but disambiguated by "reverse")
24. "So treat today's rally as resting on a draft, not a done deal." — OK (drives the unsigned point home)
25. "Here is the quiet tell underneath it." — **FLAG (L1: desk-shorthand "the tell" — the skill and exemplar both list "the tell" as a flagged shorthand a naive listener may not parse)**
26. "Foreign investors were actually still net sellers today." — OK ("net sellers" is plain)
27. "It was domestic funds that paid for this rally." — OK
28. "A rally the locals fund is sturdier than one foreigners chase, but it also means the foreign buying that would confirm the move has not shown up yet." — OK (long, two-clause, single-thread, speakable)
29. "Now the movers." — OK
30. "The sharpest was IFCI, a state-backed financier, up its full twenty percent limit on talk that the National Stock Exchange is preparing its long-awaited listing." — OK (name + what-it-does on mention; "twenty percent limit" reads as circuit-cap and is clear in context)
31. "IFCI holds an indirect stake in the exchange, so a listing could unlock that hidden value." — OK
32. "The other clean story was the two big truck makers, Tata Motors Commercial Vehicles and Ashok Leyland, both up about ten percent." — OK (named + placed)
33. "Fuel is a fleet's single biggest cost, so cheaper crude and easier truck-loan rates rotated straight into them." — OK
34. "And that is what struck me most about today." — OK
35. "The fall in oil did not stay in oil stocks." — OK
36. "It travelled." — OK (deliberate short beat)
37. "It lifted the truck makers because fuel is their biggest cost." — OK
38. "It lifted the banks and property because cheaper oil cools inflation, which points to lower rates." — OK
39. "One single headline rotated money across half a dozen sectors at once, and that is why the rally was so broad." — OK
40. "The only loser, IT, sits on the other side of the same coin." — OK
41. "A stronger rupee hurts companies that earn in dollars and spend in rupees, so the very move that helped everyone else worked against them." — OK (correct direction: stronger rupee today)
42. "The whole chain, the good and the bad, rests on that unsigned draft." — OK (third explicit unsigned reinforcement)
43. "Now, what to watch, and the big one is this weekend." — OK
44. "The reported signing in Geneva on Sunday is the single most important event." — OK
45. "A signed text confirms today; a slip is the live risk of a Monday gap the other way." — OK
46. "Alongside it, watch the price of crude over the weekend, the cleanest real-time sign of whether the calm is holding." — OK
47. "That's your brief. Before I sign off: this has been general market commentary, not investment advice." — OK (firebreak)
48. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
49. "Markets are risky; you may lose money; act with care. See you tomorrow." — OK

## Load-bearing content check — West Asia deal heard as REPORTED/UNSIGNED?

PASS. A naive listener cannot mistake this for "a peace deal happened." The unsigned status is stated four distinct times, plainly:
- Hook: "it leaned on a deal that nobody has actually signed yet."
- Framing of the move: "on reports … had agreed a draft" / "the reported terms."
- Dedicated caution beat: "The deal is only reported, not signed." + Iran's "merely speculation" quote + Geneva-Sunday as the test + "treat today's rally as resting on a draft, not a done deal."
- Wedge close: "The whole chain … rests on that unsigned draft."
Only the market reaction (the rally, crude's fall, the fear-unwind) is stated as fact. No claim is made that the deal is signed or about its terms.

## Punch list
- [L1] Line 25 "Here is the quiet tell underneath it." → recommend a plain rewrite, e.g. **"Here is the quiet signal underneath it."** or **"Here is the quiet catch underneath it."** Removes the one piece of desk-shorthand; the rest of the script is exemplar-clean. (WARN-level; principal may ship as-is — the following sentence ("Foreign investors were actually still net sellers today") immediately makes the meaning concrete, so a listener recovers within one sentence.)

## Source spot-check (S1)
Checked against `briefs/public/2026-06-12.md` — all match, no number or direction mismatch:
- Nifty "twenty-three thousand six hundred and twenty-three / up one point nine nine percent" vs brief 23,622.90 / +1.99% — MATCH
- Sensex +2.3% vs +2.30% — MATCH
- Banks "almost three percent" vs Bank Nifty +2.97% — MATCH
- Real estate "three and a half percent" vs realty +3.53% — MATCH
- IT "did not rise" vs IT −0.09% (lone laggard) — MATCH
- May inflation 3.93% below 4% expected vs CPI 3.93% vs 4.0% Reuters poll — MATCH
- Iran "merely speculation" — MATCH (verbatim)
- Geneva signing "this Sunday, the fourteenth of June" vs Sunday June 14 — MATCH
- IFCI +20% limit / state-backed financier / NSE listing / indirect stake vs IFCI +19.99%, NSE-IPO via Stock Holding stake `[SOURCED]` — MATCH
- Tata Motors CV + Ashok Leyland "both up about ten percent" vs +10.15% / +10.01% — MATCH
- FII still net sellers / DII funded rally vs FII −₹1,082 cr / DII +₹5,341 cr — MATCH
- "Stronger rupee hurts IT" vs rupee +0.57% (stronger), IT hurt — MATCH (correct direction; no wrong-day leak from yesterday's weaker-rupee wedge)

No S1 mismatch. Wrong-day-number risk (the 2026-06-04 failure class) specifically checked and clean.
