# Verify Podcast Script — 2026-08-07

**Verdict (v2, fix pass): WARN — shippable at the principal's discretion.**
**Checks (v2):** L1 2 / L2 0 / L3 0 / L4 3 / L5 0 / L6 0 / S1 NOT RUN
*(v1 was FAIL — L1 4 / L2 5 / L3 0 / L4 3 / L5 0 / L6 1. All nine v1 FAIL hits cleared.)*

*Both passes were cold reads on the spoken body only (everything below the `---` separator), against `briefs/public/podcast/canonical_voice_example/README.md`. The brief was never opened. No web search, no outside research. v2 body: 61 sentences, 702 words, longest sentence 25 words.*

## v2 headline

The fix pass cleared every FAIL. The episode's causal chain now closes — the listener is told in the same breath that Bajaj Finance is one of the lenders the draft targets — and the producer-view data paragraph has been turned listener-facing with a stated reason it matters. The Sensex composition effect and the oil-wedge punchline are both materially better than v1 and now read at exemplar standard.

Two things the fix pass introduced, neither fatal:

1. **"The government bond market ... came back empty for a fourth day running"** now makes *the market* the grammatical subject of "came back empty". A naive listener can hear that as a fact about the bond market (no trading) rather than a gap in our data. v1's "the government bond curve" was inert jargon; v2 is clearer but newly *mis*-readable. This is the one line I would change before TTS.
2. **"Growth and margins moving together."** — a verbless analyst fragment with no so-what, and "margins" is unglossed.

## Section 1 — v1 FAIL disposition

| # | v1 FAIL | v2 sentence | Status |
|---|---|---|---|
| L2 | Bajaj Finance, no what-it-does | "The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at." | **CLEARED** — placed in the same breath; the lead-to-mover bridge now exists |
| L2 | Siemens Energy India, no what-it-does | "...Siemens Energy India, which makes power equipment." | **CLEARED** |
| L2 | Shivalik Bimetal Controls, no what-it-does | "The oddest was Shivalik Bimetal Controls, a small industrial company." | **CLEARED** — minimal but adequate and non-claiming |
| L2 | Three bare names in what-to-watch | "Several companies filed their quarters after the close today, Titan among them." | **CLEARED** as a FAIL; residual WARN below |
| L2 | "The four funds" — no antecedent | "Four exchange traded funds that track emerging market shares and bonds..." | **CLEARED** — the trailing clause glosses the jargon in place |
| L1 | Producer-view data paragraph (flagrant) | "Two things I could not check for you tonight. / ...where borrowing costs are set... / On a day about credit, that is the one number you would want." | **CLEARED** as flagrant; two residual WARNs below |
| L1 | "That is arithmetic, not a second signal" | "But that is only because it holds more financial companies... It is not a second piece of bad news." | **CLEARED** — also clears the v1 L6 flag on "fell ... further only because" |
| L1 | Breadth count with no universe | "Across the whole market, three hundred and twenty shares rose..." | **CLEARED** as an L1; see S1 note on the label |
| L1 | "any single day's tick" (jargon) | "...that matters far more than any single day." | **CLEARED** |
| L4 | Oil punchline contradicted its own numbers | "...the three that stood to gain did nothing with it, and the one that stood to lose closed higher, not lower." | **CLEARED** — direction-only framing removes the contradiction; this is now the strongest passage in the episode |
| L1/L4 | "The market priced the first document and not the second" | "The market priced the results and ignored the resignation." | **CLEARED** |
| L6 | Sentence 13 re-parse | split into three sentences | **CLEARED** — longest sentence is now 25 words |

## Section 2 — v2 per-sentence ledger (full re-read)

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "What moved the Indian market today was not oil, and not earnings." — OK
5. "It was a draft." — OK
6. "The Reserve Bank of India published a proposal on Thursday." — OK (2026-08-07 is a Friday; Thursday reads as yesterday, L3 clean)
7. "It would stop lenders who are not banks from offering revolving credit, the kind of limit you can repay and draw again." — OK
8. "It is not law." — OK
9. "Comments are open until the twenty eighth of August." — OK
10. "The market priced it today as though it already were." — OK, borderline (elliptical, but sentence 8 is two beats back)
11. "Here is the close." — OK
12. "The Nifty fifty finished at twenty four thousand five hundred and seventy, down zero point two seven percent." — OK
13. "The Sensex fell more, zero point five eight percent." — OK
14. "But that is only because it holds more financial companies, and financials were where the damage was." — OK (v1 flag cleared; the composition effect now reads as mechanical)
15. "It is not a second piece of bad news." — OK (plain-English replacement for "not a second signal")
16. "Across the whole market, three hundred and twenty shares rose and three hundred and sixty two fell." — OK on the listener test; see S1 (the label "the whole market" against a total of six hundred and eighty two needs a source check)
17. "The selling was concentrated, not broad." — FLAG (L4, carried over unfixed: the conclusion is still asserted, not derived. Near-even breadth followed by "concentrated" is a non-sequitur on one hearing. Suggested bridge: "That is close to even, so the damage was in a few big names, not everywhere.")
18. "Two things I could not check for you tonight." — OK (v1's "we could not see" is now listener-facing; good fix)
19. "Most sector indices gave no usable reading." — FLAG (L1, residual: "gave no usable reading" is still pipeline vocabulary, "sector indices" is unglossed, and unlike the bond point this one is given no reason to matter. It is now a dangling item.)
20. "And the government bond market, where borrowing costs are set, came back empty for a fourth day running." — FLAG (L1, **new ambiguity**: the gloss is a real improvement, but making *the bond market* the subject of "came back empty" invites a listener to hear it as a fact about the market — no trading, nothing happening — rather than a hole in our data. Suggested: "And for a fourth day running I have no data from the government bond market, where borrowing costs are set.")
21. "On a day about credit, that is the one number you would want." — OK (this is the why-it-matters the v1 paragraph lacked; keep it)
22. "Emerging markets went the other way today." — OK
23. "Four exchange traded funds that track emerging market shares and bonds all rose while India fell." — OK (the trailing clause glosses "exchange traded funds" in place)
24. "That is the cleanest evidence we have that today was made in India." — OK, borderline (unchanged from v1: "made in India" is a pun doing a causal job, and "the cleanest evidence we have" is the desk talking about itself. Note the v1 caveat "those funds trade after our close" was cut; the sentence survives because it claims evidence, not cause — but the cut removed the line that made the comparison *valid*.)
25. "One thing did go India's way this week." — OK
26. "Brent crude fell again today, and is down roughly nine point four percent over the week." — OK
27. "For a country that imports most of its oil, that matters far more than any single day." — OK
28. "Now the movers." — OK
29. "The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at." — OK (**the fix that makes the episode work**)
30. "It fell almost six percent, the worst share in both benchmarks." — OK ("benchmarks" unglossed but carried by sentence 12)
31. "It had touched a fresh fifty two week high a week earlier, on a quarter with profit up twenty nine percent." — OK
32. "Nothing about its earnings changed in seven days." — OK
33. "What changed was the list of products it might be allowed to sell." — OK (now lands, because 29 built the bridge)
34. "The biggest gain among the large companies was Siemens Energy India, which makes power equipment." — OK
35. "It rose twelve percent, on revenue up thirty nine percent and operating profit up almost seventy four percent." — OK
36. "Growth and margins moving together." — FLAG (L4, **new**: verbless analyst fragment, "margins" unglossed, and it asserts significance without saying why a listener should care. Suggested: "It is selling much more and keeping more of each sale, which is the combination investors pay for.")
37. "The oddest was Shivalik Bimetal Controls, a small industrial company." — OK
38. "It rose twenty percent and locked at its daily price limit, on revenue up a third and profit up forty five percent." — OK
39. "In the same twenty four hours it disclosed that its outside auditor had resigned, from it and from both its subsidiaries." — FLAG (L4, carried over unfixed: *why* an auditor walking matters is still never said. "Outside auditor" is better than "statutory auditor", and the subsidiaries detail adds weight, but weight is not meaning. Suggested: "...had resigned, from the company and from both its subsidiaries. An auditor leaving is the kind of thing that usually raises questions about the accounts.")
40. "The market priced the results and ignored the resignation." — OK (clean replacement; reads as observation, not allegation — the principal's concern in the composition notes is unfounded to my ear)
41. "Five other shares rose more than seven percent today and I could not establish why any of them moved." — OK
42. "We checked everything we normally check and came back empty." — OK, borderline (voice slips from "I" in 41 to "we"; and "came back empty" is now the episode's second use of that phrase, after sentence 20)
43. "Here is what struck me most about today." — OK
44. "The Indian companies that buy crude did nothing with that weekly fall." — OK (collective gloss lands before the names — the right pattern)
45. "Bharat Petroleum finished slightly lower, Indian Oil up half a percent, Reliance Industries up under one percent." — OK
46. "Oil and Natural Gas Corporation sits on the other side." — OK
47. "It pumps crude rather than buying it, so a cheaper barrel cuts what it earns." — OK
48. "It closed up zero point four percent." — OK
49. "So the three that stood to gain did nothing with it, and the one that stood to lose closed higher, not lower." — OK (**v1 contradiction cleared** — direction-only framing no longer fights the numbers in 45 and 48)
50. "That is two sessions running where neither side of India's oil chain has priced a big move in crude, and I cannot tell you why." — OK (25 words, single thread)
51. "What to watch." — OK
52. "Several companies filed their quarters after the close today, Titan among them." — OK, borderline ("filed their quarters" is still shorthand for "filed their quarterly results" — the v1 punch-list note on this was not actioned. Titan carries no what-it-does, but it is a household name and the beat is about timing, not the company.)
53. "Those are Monday's news, not today's cause." — OK (Friday close, so Monday is right)
54. "Wednesday brings July inflation." — OK (12 August is a Wednesday)
55. "The date that matters most for today's story is the twenty eighth of August, when comments close on that draft." — OK
56. "Whether the ban survives at all is still open." — OK, borderline ("the ban" is still the first use of that word for what was described as a proposal to stop a product)
57. "That's your brief." — OK
58. "Before I sign off: this has been general market commentary, not investment advice." — OK
59. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
60. "Markets are risky; you may lose money; act with care." — OK
61. "See you tomorrow." — OK (boilerplate; note only that this is a Friday)

### Mechanical pass (L5) — clean

Machine-checked on the v2 spoken body: zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation points, zero trader jargon (the v1 "tick" is gone — the header's self-verify claim is now accurate on every count). Longest sentence 25 words, down from 28. **Word count 702** — two words over the band ceiling. That is not "well outside ~500-700", so it is not an L5 FAIL, but the two residual L4 fixes above add words, so trim while fixing: cutting "the cleanest evidence we have that" to "so" in sentence 24 returns five words on its own.

## Section 3 — v2 punch list (WARN set; principal's call, none block TTS)

Ranked. The first two are the ones I would fix.

1. **[L1, sentence 20] Stop the bond market being the subject of "came back empty".** Current: "And the government bond market, where borrowing costs are set, came back empty for a fourth day running." A listener can hear that as *the market* being empty — no trading, nothing happening — rather than a hole in our data. Fix: "And for a fourth day running I have no data from the government bond market, where borrowing costs are set." Keep sentence 21 exactly as it is; it is the best save in the fix pass.
2. **[L4, sentence 36] "Growth and margins moving together." needs a verb and a so-what.** Suggested: "It is selling much more and keeping more of each sale, which is the combination investors pay for."
3. **[L4, sentence 17] Bridge the breadth count to the conclusion.** "Across the whole market, three hundred and twenty shares rose and three hundred and sixty two fell. The selling was concentrated, not broad." Add: "That is close to even, so the damage was in a few big names, not everywhere."
4. **[L4, sentence 39] Say why an auditor resigning matters.** One clause: "An auditor leaving is the kind of thing that usually raises questions about the accounts." Without it the listener is handed a fact and expected to supply its meaning.
5. **[L1, sentence 19] "Most sector indices gave no usable reading" is now the one dangling data-gap item.** Either give it a reason to matter, as the bond point got, or cut it and spend the words on item 3.
6. **[minor, sentence 52] "filed their quarters" → "filed their quarterly results".** Carried from the v1 punch list, not actioned.
7. **[minor, sentences 41-42] Voice slips from "I" to "we" across adjacent sentences,** and "came back empty" is used twice in the episode (20 and 42). Pick one voice; vary the second phrase.
8. **[minor, sentence 56] "the ban"** is still the first use of that word for what was introduced as a proposal to stop a product.
9. **[watch, sentence 24] Cutting "those funds trade after our close" removed the line that made the comparison valid.** The sentence survives the cold read because it claims evidence and not cause, but that caveat was doing real work if the word budget ever allows it back.

## Section 4 — Source spot-check (S1)

**STILL NOT RUN.** Both passes were commissioned as strict naive-listener cold reads: `briefs/public/2026-08-07.md` was never opened, and no web search or outside research was used. The skill's Step 2 spot-check remains outstanding and **must be run before TTS** by a pass that is allowed to open the brief.

Figures to check:

| Item | v2 script value |
|---|---|
| Nifty 50 close / move | twenty four thousand five hundred and seventy, down 0.27 percent |
| Sensex move | down 0.58 percent |
| Advance / decline | 320 up, 362 down — **and whether "Across the whole market" is the right label for a 682-stock universe** |
| Bajaj Finance | down almost 6 percent; profit up 29 percent; 52-week high "a week earlier"; **that it is in scope of the draft** |
| Siemens Energy India | up 12 percent; revenue up 39 percent; operating profit up almost 74 percent; "makes power equipment" |
| Shivalik Bimetal Controls | up 20 percent, at daily price limit; revenue up a third; profit up 45 percent; outside auditor resigned from the company and both subsidiaries within 24 hours |
| Brent | down roughly 9.4 percent over the week; "fell again today" |
| Bharat Petroleum / Indian Oil / Reliance | slightly lower / up 0.5 percent / up under 1 percent |
| ONGC | up 0.4 percent (the script says "closed higher, not lower") |
| Unexplained gainers above 7 percent | five |
| RBI draft | published Thursday; comments close 28 August |
| July inflation | Wednesday |
| Post-close filers | "several companies, Titan among them" |
| Bond / sector data gaps | fourth day running; "most" sector indices |

Two labels are new in v2 and were not in the verified v1 text, so they need the closest look: **"Across the whole market"** (v1 said only "three hundred and twenty shares rose") and **"one of the lenders that draft is aimed at"** (a scope claim about Bajaj Finance that the cold read cannot check). Both are load-bearing.

**Calendar check (computed locally, no sources):** 2026-08-07 is a Friday. "Thursday" for the draft, "Monday's news" for post-close filings, and "Wednesday brings July inflation" (12 August) are internally consistent with the evening model. **L3 clean, zero hits, both passes.**

## Verdict rationale (v2)

Per Step 3: zero L1-flagrant, zero L2, zero L3, zero L5 audio-breakers, and three isolated L4 slips — not pervasive — plus two residual L1 WARN-level flags. That is **WARN**: a punch list the principal may ship over, not a block.

The fix pass did what a fix pass should. Nine FAIL hits cleared, no number altered, and the two best passages in the episode (the oil wedge and the Sensex composition effect) came out of it stronger. It cost two new blemishes — the bond-market subject slip and the "Growth and margins" fragment — which is a good trade. Neither is worth a third round on its own; fold them in only if the script is being touched anyway before TTS.
