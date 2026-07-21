# Verify Podcast Script — 2026-07-17

**Verdict:** WARN
**Checks:** L1 0 / L2 1 / L3 0 / L4 0 / L5 0 / L6 1 / S1 skipped (brief deliberately withheld from cold reader)

## One-paragraph summary
Cold-read as a naive listener, this script largely stands on its own. Every causal claim is stated plainly as cause → effect → so-what (the Asia-decoupling point, the domestic-money caveat, the oil-premium wedge landing on CEAT's margin), names are placed the moment they appear, time-words are consistent with an evening recap ("Thursday night" = the night before today's Friday close; "See you tomorrow"), and it is fully TTS-clean — all numbers spelled out, no rupee/dollar/percent symbols, and zero em-dashes in the body. The one substantive miss is that the top mover, eClerx Services, is never given a plain "what it does" the way CEAT ("the tyre-maker") and HFCL ("an optical-fibre and network-gear maker") are — a naive listener hears a company name with no idea what business it is in. Secondarily, that same eClerx sentence stacks four clauses and runs long. Both are minor and non-breaking, so this is a WARN, not a FAIL. The `[SAY: H-F-C-L]` bracket is intentional pronunciation guidance stripped before TTS, not an audio-breaker.

## Per-sentence ledger
1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK
2. "Today the June-quarter results season did its real work." — OK
3. "It started separating the strong companies from the weak ones, and that pulled Indian shares up even as most of Asia fell hard." — OK
4. "A record quarter from Federal Bank lifted the private banks, and strong software results lifted technology." — OK
5. "Those were the day's two engines." — OK
6. "But one caveat runs under the whole session, and I will come back to it." — OK (first-person used sparingly, matches exemplar's deferred-pointer style)
7. "This was home-grown money, not a foreign vote of confidence." — OK
8. "Here is where the market closed today." — OK
9. "The Nifty fifty rose just over one percent, to twenty-four thousand three hundred and thirty-four." — OK
10. "The banks did the heaviest lifting, up one point six percent, after Federal Bank's record quarter set the private-bank tone." — OK
11. "Technology added one point eight percent, carrying Thursday night's software results into today." — OK (L3: "Thursday night" reads as the night before today's Friday close — evening model consistent)
12. "The one weak corner was pharma, down one point four percent, as money rotated out of the defensive names into the day's growth stories." — OK (mild: "defensive names" is light jargon but clarified by the rotate-into-growth contrast; not a break)
13. "Now the part that makes today unusual." — OK
14. "Right through Indian trading hours, the rest of Asia was falling hard." — OK
15. "Japan's Nikkei dropped four percent." — OK (name placed with country)
16. "Korea's market fell three and a half." — OK
17. "India rose over one percent anyway." — OK
18. "So this was not a global tide lifting everyone." — OK
19. "India went the other way, on the strength of its own results." — OK
20. "Now that caveat about the money." — OK
21. "All month the story has been that foreign investors are returning to India, and over July that is genuinely true." — OK
22. "But today itself does not prove it." — OK
23. "Foreign investors were small net sellers." — OK
24. "It was Indian institutions, buying just over a thousand crore rupees, that carried the market up." — OK
25. "Do not read today's rise as foreign conviction." — OK
26. "Now the movers. The biggest gainer was eClerx Services, up more than twelve percent." — FLAG (L2: eClerx Services is named with no plain "what it does"; a naive listener does not know what business this is — contrast "the tyre-maker" / "an optical-fibre and network-gear maker")
27. "It reported a strong quarter, with profit up twenty-six percent, flagged better demand into the second half, and drew a buy call from Nomura with a raised price target, on top of a hot one-month run." — FLAG (L6: four stacked clauses, ~35 words, hard to hold in one breath)
28. "The clean fall was CEAT, the tyre-maker, down more than seven percent." — OK (name + what-it-does placed)
29. "Its revenue actually grew twenty-two percent, but its profit collapsed ninety-six percent, to almost nothing." — OK
30. "Costlier natural rubber, crude-linked inputs and a currency loss wiped out the margin." — OK
31. "This was a genuine margin miss, not profit-taking." — OK
32. "The third was HFCL, an optical-fibre and network-gear maker, down five percent and locked at its lower price limit." — OK (name + what-it-does; "lower price limit" plainly restates the circuit)
33. "There was no fresh bad news." — OK
34. "The stock had simply run up more than two hundred percent this year, and today it gave some of that back." — OK
35. "Here is the one thing that struck me most about today." — OK (matches exemplar's wedge frame)
36. "For weeks the market traded a cheap-oil-helps-India story." — OK
37. "That has quietly reversed." — OK
38. "Brent crude is back near eighty-six dollars, up about nine percent over the month." — OK
39. "You do not see it yet in the oil-refiner stocks, because a single day's move is too small to shift them." — OK
40. "But you see it clearly in a company that buys oil-linked inputs." — OK
41. "That is exactly what happened to CEAT today." — OK
42. "The oil premium is back, and now it shows up as a margin line, not as relief." — OK (mild: "shows up as a margin line" is light desk phrasing, but the CEAT setup above makes it followable)
43. "Watch the whole tyre and auto-parts cohort." — OK
44. "Now, what to watch, and it is two clocks." — OK ("two clocks" is an image but immediately unpacked as nearer/bigger)
45. "The nearer worry is prices." — OK
46. "India's June retail inflation ran hot at four point three eight percent, the highest in over a year, as food prices jumped." — OK
47. "That narrows the Reserve Bank's room to cut rates in early August." — OK
48. "The bigger clock is trade." — OK
49. "A temporary ten percent United States tariff on Indian goods expires on the twenty-fourth of July, and the interim deal is stuck on the last piece of legal text." — OK
50. "That deadline is the market's largest scheduled event, now one week out." — OK
51. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK (matches exemplar sign-off; evening model consistent)

## Punch list
- [L2] eClerx Services is named but never told what it does. Add a two-to-three-word plainer descriptor the moment the name appears, e.g. "The biggest gainer was eClerx Services, a back-office and data-analytics firm, up more than twelve percent." Every other mover gets one; this one is the odd one out.
- [L6] The eClerx follow-up sentence stacks four clauses. Consider splitting, e.g. "It reported a strong quarter, with profit up twenty-six percent, and flagged better demand into the second half. On top of a hot one-month run, Nomura kept its buy call and raised its price target."

## Source spot-check (S1)
SKIPPED by design. The brief (`briefs/public/2026-07-17.md`) was deliberately withheld to preserve the cold-read stance. Figures in the script (Nifty ~+1% to 24,334; Bank Nifty +1.6%; Nifty IT +1.8%; pharma −1.4%; Nikkei −4%; KOSPI −3.5%; DII buy ~₹1,000 cr vs FII net sell; eClerx +12%/PAT +26%; CEAT −7%/PAT −96%/rev +22%; HFCL −5%/+200% YTD; Brent ~$86/+9% MoM; CPI 4.38%; 24-July tariff) were NOT verified against source and need the informed brief-auditor / principal to confirm.

## Lines most likely to need a human eye
1. Sentence 26 — "The biggest gainer was eClerx Services, up more than twelve percent." — FLAG (L2): the top mover has no "what it does"; naive listener hears an unknown company name.
2. Sentence 27 — the eClerx four-clause follow-up — FLAG (L6): runs long and stacks clauses; hard to hold on one hearing.
3. Sentence 12 — "...as money rotated out of the defensive names into the day's growth stories." — soft note (L1-adjacent): "defensive names" is mild jargon; followable here but the one spot most likely to make a non-markets friend pause.
