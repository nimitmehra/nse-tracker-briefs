# Verify Podcast Script — 2026-07-30 (v2, second and final pass)

**Verdict:** WARN — clears the gate to the principal's read. The v1 FAIL is genuinely fixed, not papered over.
**Checks (v2):** L1 1 / L2 0 / L3 0 / L4 2 / L5 0 / L6 1 / **S1 0**
**Prior run:** v1 = FAIL (L1 6 / L2 3 / L3 1 / L4 3 / L5 0 / L6 3 / S1 1). The full v1 report is preserved verbatim at the bottom of this file.

> Order of work, unchanged and load-bearing: exemplar → **continuous read of v2 aloud, start to finish, without opening the v1 report** → ledger written → v1 punch list checked → brief opened for the source pass. The two findings I rank highest below (W1, W2) came out of the continuous read, before the v1 report or the brief was open.

**The one-line verdict:** the causal inversion that failed v1 is gone, correctly, and the replacement is better than the replacement I proposed — mine contained an error. What is left is one unexplained mechanism (expiry), one over-tight framing sentence the third example does not fit, and one residual sequencing wobble in the very passage that was rewritten. None of the three can mislead a listener; all three are one-sentence swaps. **Ship-able as-is; better with W1 and W2 taken.**

---

## Rulings you asked for

### R1 — my own v1 replacement text: **the writer is right and I was wrong. Concede without qualification.**

My punch-list item 1 proposed *"Hyundai had already closed up over one percent before its results landed."* Hyundai filed at **15:20:43** against a **15:30 close** — roughly nine minutes *before* the bell, not after. My sentence asserts a close that precedes a filing that in fact preceded the close. It is the same defect class as the error I failed v1 for, pointing the other way.

**This matters beyond one sentence:** a fix from my punch list, taken literally, would have introduced a fresh time error into the passage that had just been failed for a time-and-cause error. The writer caught it by checking the timestamp instead of accepting the verifier's wording. That is the correct instinct and it should be recorded as such.

**But the same standard applies to what replaced it** — see W1. The shipped line, *"Hyundai rose over one percent today and then filed results…"*, puts the filing after the day's move. Nine minutes of trading followed the filing. Milder than my error, same shape.

### R2 — deviation 1, expiry compressed to one sentence inside the tape paragraph: **sufficient on substance, NOT sufficient on explanation.**

The shipped sentence is: *"Part of the strength in the biggest names was mechanical, because the monthly Sensex contracts settled today, on the Bombay exchange, not the National Stock Exchange."*

Taking the two halves of my v1 finding separately, because the writer answered one and not the other:

- **Scope — fixed, and this was the substantive half.** v1 pointed the mechanism at the whole headline-versus-breadth split (*"props the headline up while the average stock falls"*), which the brief does not support. v2 says *"part of the strength in the biggest names"* — that is brief line 42's *"concentrates in the large, index-weighted names"*, hedged twice. Correct. Dropping the 7-bp Sensex-over-Nifty margin was the right audio call; the margin was never the point, the scope was.
- **Accuracy — held.** Sensex named, Bombay exchange named, NSE explicitly excluded. No sentence says "NSE expiry."
- **Explanation — not fixed.** *"The monthly Sensex contracts settled today"* does not tell a listener who knows nothing about markets what a contract is, what settling one involves, or why any of it moves large companies. The word doing all the work is "mechanical", and it gestures rather than explains. **Answering your direct question: no, monthly expiry is not adequately explained to a listener.**

It is a WARN, not a FAIL, for one reason: the sentence hedges hard enough ("part of", "mechanical") that a listener who does not follow it loses a detail and is not misled about the day. A FAIL has to be a line that flagrantly fails the naive ear or asserts something false; this asserts nothing false and can be skipped without damage. See W4 for the rewrite, and note it costs one net word if the "not the National Stock Exchange" clause goes — that clause is written for a reader who might assume NSE, and an audio listener carries no such assumption.

### R3 — deviation 2, Brent rounded to "just under ninety dollars a barrel": **confirmed. Your reading of the constraint is correct.**

The v1 constraint was **variant integrity** — that the script use the −1.19% / $89.66 / +22.96% set and not the rejected −0.87% / −0.78% / +24.13% ones. That integrity survives intact and is in fact carried by the two *percentages*, not the level: "about one point two percent" pins the day figure, "almost twenty-three percent over the month" pins the month figure and excludes +24.13%. The level was corroborating detail.

"Just under ninety dollars a barrel" is also *true* of $89.66, which is the only test that matters. And it is better audio: "eighty-nine dollars and sixty-six cents" spends seven spoken tokens on precision no listener uses. **No overrule.** Had the rounding been the *only* Brent figure spoken, I would have pushed back; with both percentages exact, it is free.

### R4 — Hexaware's 352 bps moved to show notes: **accepted.**

No constraint required the figure. The plain-language pair that replaced it — *"the profit from its actual business grew"* and *"the entire fall came from one-off items and tax, not from the business itself"* — is the brief's claim (*"Every rupee of the decline sits below the operating line"*) stated in words a listener holds on one hearing. This is a straight upgrade over v1, not a concession.

*Proportionality note, not a flag:* the brief also says Hexaware's *genuine* soft spot is growth — 6.3% constant currency after a 28% three-month run. The script omits it, which leaves the listener slightly more sympathetic to Hexaware than the brief is. The brief's own closing line (*"Anyone writing 'profit fell 13%, so the stock fell 7%' has the cause and effect wrong"*) is what the script delivers, so this is compression, not distortion. No action.

### R5 — PCBL merged into the wedge: **correct call, better than v1.**

v1 told PCBL twice — once as a mover, once as wedge example one — and the second telling had to say *"PCBL was one"*, a back-reference audio handles badly. One telling, in the place where it does teaching work, is right. The wedge is now the longest paragraph (13 sentences, ~230 words), which is defensible because it is the episode's argument and it is signposted at both ends.

### R6 — opening and firebreak intact: **confirmed by diff, not by eye.**

Diffed the narrated body of v2 against `backups/2026-07-31/script_2026-07-30_v1.md`. The opening paragraph and the firebreak paragraph do not appear in the diff at all — byte-identical. The fifteen-second test still passes on the same words that passed it in v1, and it remains the script's best feature and a better hook than the exemplar's.

---

## Per-sentence ledger (v2 — cold read, brief not yet open)

**Opening (untouched from v1)**

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (exemplar-identical)
2. "The index went up today and most of the market went down." — OK. Still the best line in the script.
3. "Two out of every three shares ended lower, four hundred and fifty-seven falling against two hundred and fifteen rising." — OK
4. "Anyone who read only the index number read the opposite of what happened." — OK

**The close**

5. "Here is where the market closed." — OK
6. "The Nifty fifty finished at twenty-four thousand three hundred and seventeen, up zero point two eight percent." — OK (Sensex print dropped; no loss, the paragraph is cleaner for it)
7. "But the typical stock fell about six-tenths of a percent, and the fear gauge, India VIX, rose over one percent." — OK ("typical" fixes v1's "median")
8. "Fear rising on a rising market is unusual." — OK
9. "Auto shares led, up over one and a half percent as a group, after a strong quarter from Mahindra and Mahindra, the tractor and SUV maker." — OK. v1's L2 hit is cleared; the gloss is accurate to a company that is both.
10. "Property developers were the weakest, down about two percent, with insurers and non-bank lenders sold as well." — OK ("sold as well" removes the momentary mis-parse)
11. "Part of the strength in the biggest names was mechanical, because the monthly Sensex contracts settled today, on the Bombay exchange, not the National Stock Exchange." — **FLAG (L1: "the monthly Sensex contracts settled" is unexplained** — the listener is told the effect of a thing they were never told about. Scope and accuracy are fixed; the explanation is not. See W4.)

**The two forces**

12. "The pressure on the day was interest rates." — OK, but the v1 signpost "Now the two forces underneath" is gone and the jump from expiry mechanics to rates now happens with no hinge. Minor, see W5.
13. "The Reserve Bank of India decides on rates next week, and a Reuters poll of seventy-two economists found sixty-eight expecting no change, four a hike, and none a cut." — OK. 29 words, the longest in the script, but single-thread and cleanly comma-segmented; per L6 not flagged on length. "None a cut" lands well spoken.
14. "So the market bought the earnings story and sold anything that depends on rates falling." — OK
15. "The support was oil." — OK (past tense now consistent with 12; the v1 tense clash is gone)
16. "Brent crude eased about one point two percent today, to just under ninety dollars a barrel." — OK
17. "But it is still up almost twenty-three percent over the month, and India imports about eighty-five percent of its oil." — OK — and now resolved by the next sentence, which is what v1 lacked.
18. "Today's dip helps, but only for as long as the oil keeps physically flowing." — OK, with one reservation (L4, mild): the caveat is restored but its *cause* is not. The listener is told the relief is conditional and never told what would end it. "Physically flowing" is concrete enough to survive alone, so I am not flagging it — but if a word or two ever comes free, "while the fighting near the Gulf leaves the barrels moving" is the brief's own logic in seven words.

**Movers**

19. "Now the movers." — OK
20. "The biggest gain was Balkrishna Industries, a tyre maker, up almost eleven percent on revenue up twenty-five percent and profit up fifty-six percent." — **FLAG (L6: three percentages in one 24-word breath**, and the mover has lost its third beat entirely. v1's fragment is correctly gone, but the exemplar's what-it-does / what-happened / why-it-matters shape went with it. See W3.)
21. "Second was Redington, which distributes technology products, up over eight percent to a one-year high on record quarterly revenue." — OK (v1's fourth stacked figure dropped; three facts is inside what a listener holds)
22. "But the company itself says part of that came from higher personal-computer prices caused by a global memory shortage." — OK. Still the strongest single line in the movers block; the attribution to the company is exactly right.
23. "That is profit handed to it by a shortage, not profit it earned." — OK (minor precision note at S1 below: the brief's word is "margin", not "profit")

**The wedge**

24. "Here is what struck me most today." — OK (the one first-person use, as the header claims)
25. "Three times over, the market cared about where a profit came from rather than how big it was." — **FLAG (internal logic: the third example does not fit the promise.** KPIT fell on guidance — about the quarter *ahead*, not about where this quarter's profit came from. Heard in sequence, the script promises three of one thing and delivers two plus a different thing. See W2.)
26. "The sharpest fall was PCBL Chemical, which makes carbon black for tyres." — OK (v1's L2 hit cleared)
27. "It fell about ten percent on a profit that rose sixty-five percent." — OK. Excellent construction — the paradox is the hook.
28. "Brokerages pointed out that roughly seventy crore rupees of it was a one-off inventory gain, not money the business earned." — OK. Attribution moved to the front, which fixes v1's stranded negation, and "not money the business earned" is a clean plain-English rendering of "not operating earnings".
29. "Strip that out and the growth is a fraction of the headline." — OK
30. "Hexaware, a technology services firm, was the same idea in reverse." — OK
31. "Its profit fell thirteen percent and the share fell almost seven percent, but the profit from its actual business grew." — OK (missing unit restored; "operating margin … percentage points" correctly replaced with something a listener holds)
32. "The entire fall came from one-off items and tax, not from the business itself." — OK. v1's flagrant "below the operating line" is gone.
33. "And KPIT Technologies, whose customers are carmakers, fell nearly eight percent." — OK
34. "Not on the quarter it reported, but on what it said about the next one, after European carmakers cut spending." — OK. Verbless, but it attaches to 33 as natural spoken apposition and reads better than v1's 30-word single sentence.
35. "The size of a profit told you little today." — OK
36. "Where it came from told you almost everything." — OK as a line; inherits W2's mismatch as the closing half of the frame.

**What to watch**

37. "Now, what to watch." — OK
38. "Four large companies filed results in the last twenty minutes of trading today." — OK (v1's read-aloud data range is gone; Vedanta at 15:09 is 21 minutes, so "the last twenty minutes" is a rounding a listener will never trip on)
39. "Vedanta the miner, Bajaj Finance the lender, Hyundai the carmaker, Mankind the drugmaker." — OK. v1's L2 hit cleared at one word each, exactly as costed.
40. "Their numbers had no time to trade." — OK
41. "Hyundai rose over one percent today and then filed results showing profit down thirty-five percent." — **FLAG (sequencing: "and then" places the filing after the day's move.** Hyundai filed at 15:20 against a 15:30 close, so about ten minutes of trading followed it — and sentence 38 has already told the listener the filings happened *during* trading. Two sentences that disagree when heard three apart. See W1.)
42. "Bajaj Finance closed flat, and its profit was up almost twenty-eight percent." — OK. The "on" that caused the v1 FAIL is gone; this is now juxtaposition, not attribution.
43. "Neither close had anything to do with those results." — OK. **This is the sentence that fixes the FAIL**, and stating it flatly rather than implying it is the right choice.
44. "Hyundai moved with a strong auto sector, and Bajaj Finance with lenders being sold ahead of the rate meeting." — OK, with a wobble: "moved with" is doing double duty across a stock that rose and a stock that closed flat, two sentences after the listener was told Bajaj Finance closed flat. Not wrong — a flat close in a sold sector is a real reading, and it is the brief's own — but "sat flat in a lending sector being sold ahead of the rate meeting" would say it without the friction. Optional.
45. "Tomorrow is when the results get their reaction." — OK ("get priced" fixed; Thursday session, Friday reaction — correct under the evening model)
46. "The event that matters most from here is the Reserve Bank's rate decision on Wednesday, the fifth of August." — OK. v1's L3 error is gone, and 5 August 2026 is indeed a Wednesday. Consistent with sentence 13's "next week".

**Firebreak (untouched from v1)**

47. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK. Exemplar-verbatim, complete. No recommendation language anywhere in the body.

---

## v1 punch list — audit of the ten items

| # | v1 item | v2 status |
|---|---|---|
| 1 | **[S1 FAIL]** Hyundai / Bajaj causal inversion | **FIXED**, and better than my proposed wording, which was itself wrong (R1). Residual sequencing nit → W1. |
| 2 | Expiry paragraph — explain + re-narrow | **PARTIAL.** Scope fixed, accuracy held, explanation still missing → W4. |
| 3 | "the week's real event" (L3) | **FIXED**, my wording taken verbatim. |
| 4 | "below the operating line" (L1) | **FIXED**, my wording taken verbatim. |
| 5 | Oil caveat restored (L4) | **FIXED.** Cause of the fragility still unstated — noted at ledger 18, not flagged. |
| 6 | Place Mahindra and Mahindra (L2) | **FIXED**, verbatim. |
| 7 | Balkrishna fragment (L1) | **FIXED by deletion**, not by rewrite. Flag cleared; the mover's third beat went with it → W3. |
| 8 | Glosses: PCBL + four late filers (L2) | **FIXED**, all five. |
| 9 | Split Redington (L6) | **FIXED** by dropping the fourth figure rather than splitting — same effect, cheaper. |
| 10 | "median"→"typical", "sold too"→"sold as well", "get priced"→"get their reaction", Asia line, missing "percent", the 8-to-21 range | **ALL FIXED.** Asia cut entirely, which was the recommended way to pay for the rest. |

**Eight fully, two partially. No v1 finding was ignored, and none was fixed by assertion.** The word budget I costed at 740–750 came in at 700 on the nose, which required the two documented deviations — both of which I have ruled on above, and both of which I would have authorised had I been asked in advance.

---

## New findings in v2 (all WARN)

**W1 — sentence 41, "and then filed".** The rewrite fixed the causation and left a sequencing claim behind. Replace:

> "Hyundai closed up over one percent today. Its results, filed minutes before the bell, showed profit down thirty-five percent."

Costs five words, claims nothing about order beyond what is true, and loses no punch because sentences 40 and 43 carry the point. *(If you would rather spend nothing: deleting the two words "and then" and replacing them with a comma plus "and" leaves "Hyundai rose over one percent today, and filed results showing profit down thirty-five percent" — the sequencing implication weakens but does not vanish. The five-word version is the clean one.)*

**W2 — sentence 25, the frame the third example does not fit.** Note first that the *trio* is the brief's own (*"Three results where the market read the quality of the number, not its size"* — PCBL, Hexaware, KPIT). The script did not invent the grouping; it tightened the brief's "quality" to "where a profit came from", and KPIT's fall was about the quarter ahead. One swap fixes it and frees words:

> Sentence 25 → "Three times over, the market looked past the size of a profit to what was really behind it."
> Sentence 36 → "What was behind it told you almost everything."

Net −1 word, and the third example now fits the promise it is filed under.

**W3 — sentence 20, Balkrishna.** Three percentages in one breath, and the only mover with no "why it matters". Not worth words unless the budget allows; if it does, splitting after "up almost eleven percent" and letting the two result figures form their own short sentence restores the exemplar's shape at zero net cost.

**W4 — sentence 11, expiry still unexplained** (the R2 ruling). If you want it fixed:

> "Part of the strength in the biggest names was mechanical. Monthly bets on the Sensex, the Bombay exchange's main index, expired today, and closing those bets means trading the largest companies in it."

Net +1 word once "not the National Stock Exchange" goes — a clause written for a *reader* who might assume NSE, which an audio listener has no reason to assume. Accuracy is preserved by naming the Sensex and the Bombay exchange positively. **If you would rather keep the disclaimer, keep the sentence as shipped** — it is a WARN either way and the disclaimer is the more conservative of the two.

**W5 — sentence 12, missing hinge.** The v1 signpost "Now the two forces underneath" was cut and nothing replaced it, so the script moves from expiry mechanics to interest rates on a paragraph break alone. Five words would restore the exemplar's signposting rhythm. Lowest priority here.

**Word budget if you take W1 + W2 + W4:** +5 −1 +1 = **+5, landing at 705** — five words over the band ceiling, about two seconds of audio. If you want it back inside 700, W3's split is free and dropping "as well" from sentence 10 and "today" from sentence 45 pays the rest without touching a fact.

---

## Narratability (L5 — zero hits, verified by scan)

- **700 narrated words** after `[SAY: …]` hints are stripped — at the ceiling of the 500–700 band, inside it. **Zero digits. Zero `%` / `₹` / `$`. Zero em-dashes or en-dashes.** Independently re-verified by script, not by eye; matches your own count exactly.
- **SAY-hints safe:** `hive-mind/scripts/tts-podcast-nse.py:101` strips `[SAY: …]` by regex before synthesis. Seven hints (R-B-I, bal-KRISH-na, RED-ing-ton, P-C-B-L, HEX-a-ware, K-P-I-T, HUN-day). The B-S-E hint is gone with v1's expiry paragraph — if W4's rewrite is taken, no new hint is needed, since "Bombay exchange" is spoken as words.
- **Longest sentence: 29 words** (ledger 13), single-thread and comma-segmented — passes L6. Nothing in the body is unspeakable in one breath.
- **Constructions that garbled in v1 are gone:** the unit-less "fell almost seven", the "eight to twenty-one minutes" range, and "three and a half percentage points" all resolved.
- **~4.2 minutes at 165 WPM.**

---

## Source spot-check (S1) — no mismatch. **PASS.**

Run against `briefs/public/2026-07-30.md`, after the ledger above was written.

**The v1 FAIL is cleared at source, not just at surface.** The brief's most emphatic instruction — *"Their results cannot explain their share moves today… that is the most useful thing to take from tonight"* — is now stated outright by the script (sentence 43), and both of the brief's alternative causes are carried: Hyundai's *"+1.27% was auto-sector strength"* and Bajaj Finance's *"today's price moved with the non-bank lending pack being sold ahead of the rate meeting."* The script says exactly this and nothing more.

| Claim in script | Brief | Match |
|---|---|---|
| Nifty twenty-four thousand three hundred and seventeen, up zero point two eight percent | 24,317.15, +0.28% | ✓ |
| 457 falling / 215 rising | 457 declines / 215 advances | ✓ |
| Typical stock about six-tenths of a percent | median −0.60% | ✓ |
| VIX rose over one percent | +1.21% | ✓ |
| Auto up over one and a half percent as a group | +1.63%, close reports / aggregation | ✓ (correctly spoken as group direction) |
| Property developers down about two percent | Realty −2.06% | ✓ (same caveat, same handling) |
| M&M a strong quarter, tractor and SUV maker | profit +34%, revenue +27%, filed 12:58, +1.92%; autos and farm equipment | ✓ |
| Part of the strength in the biggest names mechanical; monthly Sensex contracts, Bombay exchange, not NSE | "BSE Sensex monthly and weekly derivatives expiry, not an NSE one… concentrates in the large, index-weighted names" | ✓ **scope now correct** |
| RBI decides next week; 72 economists, 68 / 4 / none | meeting 3–5 Aug; 72, 68 hold / 4 hike / 0 cut | ✓ |
| Brent eased about one point two percent, just under ninety dollars | −1.19% to $89.66 | ✓ correct variant, rounding true |
| Up almost twenty-three percent over the month | +22.96% | ✓ (excludes the rejected +24.13%) |
| India imports about eighty-five percent of its oil | ~85% | ✓ |
| Relief lasts only while oil keeps physically flowing | "a confirmed and sustained blockage of physical flow re-prices the import bill… contingent rather than structural" | ✓ |
| Balkrishna almost eleven, revenue twenty-five, profit fifty-six | +10.82%, +25.19%, +56.35% | ✓ |
| Redington over eight, one-year high, record quarterly revenue | +8.18%, 52-week high, record revenue +34% | ✓ |
| Redington: company attributes part to PC prices on a memory shortage | company's own attribution, memory-chip shortage | ✓ |
| PCBL about ten percent down on profit up sixty-five; seventy crore one-off; "brokerages pointed out" | −10.31%, +65%, ~₹70 cr; "Business Today, citing brokerage commentary" | ✓ attribution preserved |
| PCBL makes carbon black for tyres | chemical maker; carbon black | ✓ (true; the brief does not gloss the use, and tyres is its principal one) |
| Hexaware profit down thirteen, share down almost seven, operating business grew, fall from one-offs and tax | −13%, −6.91%, operating profit rose (+352 bps), "every rupee… below the operating line: other income, writeback, finance costs, tax" | ✓ |
| KPIT nearly eight percent, on the next quarter not this one, European carmakers cut spending | −7.67%, guidance not the quarter, sudden June cuts by European carmakers | ✓ |
| Four filed in the last twenty minutes; Vedanta miner, Bajaj lender, Hyundai carmaker, Mankind drugmaker | 15:09 / 15:19 / 15:20 / 15:21 vs 15:30 close | ✓ (glosses all accurate) |
| Hyundai up over one percent, profit down thirty-five | +1.27%, profit −35% to ₹889 cr | ✓ |
| Bajaj Finance flat, profit up almost twenty-eight | −0.09%, profit +27.6% | ✓ |
| Neither close caused by the results; auto strength / lenders sold into the rate meeting | brief, in bold, plus both alternative causes | ✓ **the v1 S1 hit is resolved** |
| Tomorrow is when the results get their reaction | "Friday is the first real reading" | ✓ |
| RBI decision Wednesday the fifth of August | 5 August (meeting 3–5 Aug) | ✓ |

**One precision note, below flag level.** Sentence 23 says *"That is profit handed to it by a shortage, not profit it earned."* The brief's phrasing is *"margin handed over by a component squeeze, not earned"*, and the antecedent in the script's previous sentence is record **revenue**. Higher selling prices at unchanged cost do drop through to profit, so the claim is not false, and "margin" is a word the naive-listener test would have thrown out anyway. Recorded for completeness; no change recommended.

**Hard constraints — all held.** No "NSE expiry" anywhere. Correct Brent variant. No dollar index. No FII/DII flows. No gold, yen, or US session used as a Thursday cause. Nine unusable sector indices neither quoted nor implied — Auto and Realty appear only as group direction. No Garware/GRWRHITECH, no HFCL. No figures for Mankind (named in the late-filer list only), Vedanta, Vardhman or Prestige. No recommendation language outside the firebreak, no price targets, no broker ratings — the brief's Nomura and Motilal Oswal targets correctly stayed out of audio.

---

## Note for the writer skill

v1's lesson was that self-review searches for what it *removed* and misses what it left *adjacent*. v2 shows the writer acted on that — it ran its own read-aloud and self-caught a tense clash and a dangling pronoun, both real. The two flags left standing (W1, W2) are still adjacency failures, but at a longer range: W1 is a contradiction across three sentences, W2 across eleven. **The read-aloud is working at paragraph range and not yet at section range.** The cheapest next increment is to read each paragraph against the promise made by the sentence that introduced its section, rather than only against its neighbours.

Second, and worth writing down: **the writer was right to refuse a verifier fix.** My item 1 replacement contained a timestamp error. A verifier's suggested wording is a suggestion, not a finding — the finding was "the causation is inverted", and that was correct. Checking the proposed wording against the filing time before adopting it is exactly the behaviour that should be repeated.

---
---

# ARCHIVE — v1 report (FAIL), preserved verbatim

*The report below is the first-pass ledger, written against `backups/2026-07-31/script_2026-07-30_v1.md`. It is superseded by the v2 verdict above and retained as history. Note that punch-list item 1's suggested replacement text contains a timestamp error — see ruling R1.*

