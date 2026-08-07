# Verify Podcast Script — 2026-08-07

**Verdict:** FAIL
**Checks:** L1 4 / L2 5 / L3 0 / L4 3 / L5 0 / L6 1 / S1 NOT RUN (see below)

*Cold read performed on the spoken body only (everything below the `---` separator, lines 37-59), against `briefs/public/podcast/canonical_voice_example/README.md`. The brief was NOT opened. No web search, no outside research. Sentence numbering below matches a mechanical split of the spoken body (56 sentences, 700 words).*

## Headline

Two structural failures, both listener-fatal on one hearing:

1. **The episode's own causal chain never closes.** The lead says a Reserve Bank draft on "lenders who are not banks" moved the market. The biggest fall is Bajaj Finance. The script never tells the listener that Bajaj Finance *is* one of those lenders. A naive listener hears two unconnected stories.
2. **Producer-view meta is spoken as market news** — thirteen sector indices with "no usable reading" and a bond curve that "came back empty for a fourth day" is our data pipeline's status, not the listener's session.

## Per-sentence ledger

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "What moved the Indian market today was not oil, and not earnings." — OK (strong cold open; evening-model "today" correct)
5. "It was a draft." — OK
6. "The Reserve Bank of India published a proposal on Thursday." — OK (2026-08-07 is a Friday, so Thursday reads as yesterday; no L3 breach. Minor: "yesterday" would be one beat clearer for a listener who does not track weekdays.)
7. "It would stop lenders who are not banks from offering revolving credit, the kind of limit you can repay and draw again." — OK (the gloss on revolving credit is exactly the exemplar's move)
8. "It is not law." — OK
9. "Comments are open until the twenty eighth of August." — OK
10. "The market priced it today as though it already were." — OK, borderline (elliptical: "as though it already were" drops "law". Survives because sentence 8 is two beats back.)
11. "Here is where things closed." — OK
12. "The Nifty fifty finished at twenty four thousand five hundred and seventy, down zero point two seven percent." — OK
13. "The Sensex fell zero point five eight percent, further only because it carries more financial weight and financials were where the damage was." — FLAG (L6: "fell ... further only because" is a compressed construction that has to be re-parsed mid-sentence; the listener hears "fell zero point five eight percent further" before the clause resolves. Single-thread but not clean on one hearing.)
14. "That is arithmetic, not a second signal." — FLAG (L1: desk-shorthand. "A second signal" is analyst vocabulary; a naive listener does not know what the first signal was.)
15. "Three hundred and twenty shares rose and three hundred and sixty two fell." — FLAG (L1: out of what? No universe is given. The listener cannot size six hundred and eighty two against a market.)
16. "The selling was concentrated, not broad." — FLAG (L4: the conclusion is asserted, not derived. Three hundred and twenty up versus three hundred and sixty two down sounds *even*, not concentrated; the chain from the count to the conclusion is missing.)
17. "Two things we could not see tonight." — FLAG (L1: producer-view meta. This is the desk's data-availability status, not the market's day. The exemplar's rule six: the listener gets the story, not the analyst's view of the story.)
18. "Thirteen of the fifteen sector indices gave no usable reading, and the government bond curve came back empty for a fourth day." — FLAG (L1, flagrant: "gave no usable reading" and "came back empty" are pipeline shorthand; "the government bond curve" is never explained and never made to matter. A smart non-finance listener gets nothing from this sentence and cannot even tell whether it is good or bad news.)
19. "Emerging markets went the other way." — OK
20. "The four funds that track emerging market shares and bonds all rose while India fell." — FLAG (L2: "The four funds" — definite article, no antecedent, never named or placed. Which four?)
21. "Those funds trade after our close, so they are a read on the day, not a cause of it." — OK (the "read not cause" distinction is earned by the clause before it)
22. "But it is the cleanest evidence we have that today was made in India." — OK, borderline (L4-lite: "made in India" is a pun doing the work of a causal statement, and "the cleanest evidence we have" is again the desk talking about itself. Plain rewrite: "so the selling was Indian, not global.")
23. "Two things sit behind the session." — OK
24. "On the supportive side, Brent crude fell again, and is down roughly nine point four percent over the week." — OK ("Brent" unglossed but self-evident from "crude"; weekly-only magnitude is the safe call)
25. "For a country that imports most of its oil, that matters far more than any single day's tick." — FLAG (L1: "tick" is trader jargon. The header's self-verify claims zero banned trader jargon; this is one. Say "any single day's move".)
26. "On the worrying side, the rupee slipped again, on a day the dollar itself was falling against everything else." — OK
27. "When your currency weakens while the dollar is being sold, the weakness is your own." — OK (clean cause to so-what, exemplar quality)
28. "Now the movers." — OK
29. "The biggest fall was Bajaj Finance, down almost six percent, the worst share in both benchmarks." — FLAG (L2, the episode-breaking one: no plain what-it-does. Bajaj Finance is never identified as one of the "lenders who are not banks" the draft targets, so the listener has no bridge from the lead to the biggest fall. Exemplar standard: "PhysicsWallah, the education company"; "Anant Raj, a real-estate and data-centre developer".)
30. "It had touched a fresh fifty two week high a week earlier, on a quarter with profit up twenty nine percent." — OK
31. "Nothing about its earnings changed in seven days." — OK
32. "What changed was the list of products it might be allowed to sell." — OK as a line, but it is carrying the whole connection alone; it only lands if sentence 29 has already placed the company as a non-bank lender.
33. "The biggest gain among the large companies was Siemens Energy India, up twelve percent, on revenue up thirty nine percent and operating profit up almost seventy four percent." — FLAG (L2: no what-it-does; also the exemplar's three-beat mover shape — what it does / what happened / why it matters — is collapsed into one number-stacked sentence with no why-it-matters at all.)
34. "The oddest was Shivalik Bimetal Controls, up twenty percent and locked at its daily price limit, on revenue up a third and profit up forty five percent." — FLAG (L2: no what-it-does for an unfamiliar small company. "Locked at its daily price limit" is acceptable — it self-explains.)
35. "In the same twenty four hours it disclosed that its statutory auditor had resigned." — FLAG (L4: why an auditor resigning matters is never said. The listener is handed the fact and left to know that it is a warning sign about the accounts.)
36. "The market priced the first document and not the second." — FLAG (L1/L4: "the first document" has no antecedent — the word "document" has not been used since the lead, and the two things being contrasted were called results and a resignation. Oblique image standing in for the chain.)
37. "Five other shares rose more than seven percent, and I could not establish why any of them moved." — OK (honest, plain, first person; this is the good version of an admission)
38. "We checked everything we normally check, and it came back empty." — OK, borderline (L1-lite: producer-view, and the voice switches from "I" in the previous sentence to "we" here.)
39. "Here is what struck me most about today." — OK
40. "The Indian companies that buy crude did nothing with that weekly fall." — OK (this is the right way to place names: the collective gloss arrives *before* the names)
41. "Bharat Petroleum finished slightly lower, Indian Oil up half a percent, Reliance Industries up under one percent." — OK (covered by the gloss in 40)
42. "Oil and Natural Gas Corporation sits on the other side." — OK
43. "It pumps crude rather than buying it, so a cheaper barrel cuts what it earns." — OK (model cause to effect)
44. "It closed up zero point four percent." — OK
45. "So the three that stood to gain sat still, and the one that stood to lose went up." — FLAG (L4: the payoff contradicts the numbers the listener just heard. Indian Oil up half a percent is filed under "sat still" while ONGC up zero point four percent is "went up" — a smaller move. The wedge's punchline is not supported by its own evidence on one hearing.)
46. "That is two sessions running where neither side of India's oil chain has priced a big move in crude, and I cannot tell you why." — OK (25 words, single thread; "priced" is the fourth use of the verb in the episode — see punch list)
47. "What to watch." — OK
48. "Titan, Ola Electric and Hitachi Energy India all filed their quarters after the close, so that is Monday's news, not today's cause." — FLAG (L2: three names, no what-they-do, and no reason a listener should care about any of them. "Filed their quarters" is also shorthand for "filed their quarterly results". Time logic is correct: Friday close means Monday news.)
49. "Wednesday brings July inflation." — OK (Aug twelfth is a Wednesday; forward event correctly in the future, L3 clean)
50. "The date that matters most for today's story is the twenty eighth of August, when comments close on that draft." — OK (strong close on the spine)
51. "Whether the ban survives at all is still an open question." — OK, borderline ("the ban" is the first use of that word for what was described as a proposal to stop a product; a listener may hear a new subject.)
52. "That's your brief." — OK
53. "Before I sign off: this has been general market commentary, not investment advice." — OK
54. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
55. "Markets are risky; you may lose money; act with care." — OK
56. "See you tomorrow." — OK (boilerplate, matches exemplar. Note only: this is a Friday, so "tomorrow" is a Saturday with no session.)

### Mechanical pass (L5) — clean

Machine-checked on the spoken body: zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation points. Word count 700 — inside the 500-700 band, but at the ceiling with no headroom for the L2 fixes below, so the trims in the punch list are load-bearing. Longest sentence 28 words (33), single-thread. The header's self-verify claim is accurate on every mechanical count and wrong only on "zero banned trader jargon" (sentence 25, "tick").

## Punch list

**Must fix before TTS (the FAIL set)**

- **[L2, sentence 29] Place Bajaj Finance as a non-bank lender in the same breath as the name.** This is the fix that makes the episode work. Suggested: "The biggest fall was Bajaj Finance, the largest of those non-bank lenders, down almost six percent, the worst share in both benchmarks." Everything after it (sentence 32, "the list of products it might be allowed to sell") then lands without the listener doing any work.
- **[L1, sentences 17 and 18] Cut the data-availability paragraph entirely, or reduce it to one plain sentence that says why a listener should care.** "Two things we could not see tonight. Thirteen of the fifteen sector indices gave no usable reading, and the government bond curve came back empty for a fourth day." As written it is our pipeline's status narrated as market news, and "the government bond curve" is never explained. Cutting it also buys back roughly twenty two words for the fixes above. If it must stay: "One caveat. Our sector-level and bond-market data were incomplete tonight, so this is a read on the headline indexes only."
- **[L2, sentence 33] Give Siemens Energy India a what-it-does and a why-it-matters.** Suggested: "The biggest gain among the large companies was Siemens Energy India, which builds power grid and generation equipment, up twelve percent. Revenue rose thirty nine percent and operating profit almost seventy four percent." Two sentences read better than the current twenty eight-word number stack.
- **[L2, sentence 34] Give Shivalik Bimetal Controls a what-it-does.** It is an unfamiliar name doing the episode's most interesting work; the listener needs one clause on what it makes.
- **[L2, sentence 48] Either gloss Titan, Ola Electric and Hitachi Energy India, or drop to the one that matters.** Three bare names in a what-to-watch line give a listener nothing to hold. Also expand "filed their quarters" to "filed their quarterly results".
- **[L1, sentence 14] Replace the desk-shorthand.** "That is arithmetic, not a second signal." Suggested: "That is just the way the two indexes are built, not a second piece of bad news."

**Should fix (WARN set, principal's call)**

- **[L4, sentence 45] The oil wedge's punchline contradicts its own numbers.** Indian Oil up half a percent is filed under "sat still" while ONGC up zero point four percent is "went up" — a smaller move described as the bigger reaction. Either state the point as "nobody in the chain moved much either way, in either direction the fall should have pushed them" or drop the up-versus-still framing.
- **[L1/L4, sentence 36] "The market priced the first document and not the second" has no antecedent for "document".** Suggested: "Investors traded the results and ignored the resignation." Pair it with a half-clause in sentence 35 on why an auditor walking away matters.
- **[L4, sentences 15-16] Give the advance-decline count a universe and close the chain.** Suggested: "Across the broader market, three hundred and twenty shares rose and three hundred and sixty two fell. That is close to even, which tells you the damage was in a few big names rather than everywhere."
- **[L2, sentence 20] Name or characterise "the four funds".** At minimum: "The four big exchange traded funds that foreign investors use to hold emerging market shares and bonds all rose while India fell."
- **[L1, sentence 25] "any single day's tick" → "any single day's move".** Trader jargon.
- **[L6, sentence 13] Unpack "further only because".** Suggested: "The Sensex fell more, zero point five eight percent, because it holds more financial companies, and financials were where the damage was."
- **Verb repetition:** "priced" carries four different jobs across the episode (sentences 10, 36, 46, and the lead's logic). Vary at least two of them.
- **[sentence 51] "the ban"** is the word's first appearance; the thing was introduced as a proposal to stop a product. Use "the proposal" or introduce "ban" earlier.

**Word budget note.** The body is at 700 words, the ceiling. The L2 fixes add roughly forty words; cutting sentences 17-18 returns twenty two, and the composition notes already list several trimmable deliberate inclusions. Re-count before TTS.

## Source spot-check (S1)

**NOT RUN — deliberately withheld this pass.** This run was commissioned as a strict naive-listener cold read: the brief (`briefs/public/2026-08-07.md`) was not opened, and no web search or outside research was used. The skill's Step 2 spot-check therefore remains outstanding and must be run before TTS by a pass that is allowed to open the brief.

Figures to check when it is run:

| Item | Script value |
|---|---|
| Nifty 50 close / move | twenty four thousand five hundred and seventy, down 0.27 percent |
| Sensex move | down 0.58 percent |
| Advance / decline | 320 up, 362 down (and *which* universe) |
| Bajaj Finance | down almost 6 percent; profit up 29 percent; 52-week high "a week earlier" |
| Siemens Energy India | up 12 percent; revenue up 39 percent; operating profit up almost 74 percent |
| Shivalik Bimetal Controls | up 20 percent, at daily price limit; revenue up a third; profit up 45 percent; statutory auditor resigned in the same 24 hours |
| Brent | down roughly 9.4 percent over the week; direction "fell again" |
| Bharat Petroleum / Indian Oil / Reliance | slightly lower / up 0.5 percent / up under 1 percent |
| ONGC | up 0.4 percent |
| Unexplained gainers above 7 percent | five |
| RBI draft | published Thursday; comments close 28 August |
| July inflation | Wednesday |
| Post-close filers | Titan, Ola Electric, Hitachi Energy India |

Two internal consistency checks that a brief-reading pass should resolve: (a) whether the advance-decline count supports "concentrated, not broad", and (b) whether ONGC up 0.4 percent genuinely reads as "went up" against Indian Oil up 0.5 percent filed as "sat still" (sentence 45).

**Calendar check (computed locally, no sources):** 2026-08-07 is a Friday. "Thursday" for the draft (yesterday), "Monday's news" for post-close filings, and "Wednesday brings July inflation" (12 August) are all internally consistent with the evening model. **L3 is clean — zero hits.**

## Verdict rationale

Per Step 3: any L1 or L2 match is a FAIL. This script has four L1 hits (one flagrant — the data-availability paragraph) and five L2 hits (one of them structural — the lead's causal chain never reaches its own biggest mover). **FAIL. Fix and re-verify before `tts-podcast-nse.py` runs.**

Worth saying plainly: the failures are concentrated and cheap to fix. The oil wedge (sentences 39-46), the rupee-versus-dollar chain (26-27), the revolving-credit gloss (7), and the unexplained-movers admission (37) are all at or above exemplar standard. This is a near-miss draft with four missing what-it-does clauses and one paragraph of desk-talk, not a rewrite.
