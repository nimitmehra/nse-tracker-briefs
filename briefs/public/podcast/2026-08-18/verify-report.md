# Verify Podcast Script — 2026-08-18

**Verdict:** FAIL — fix and re-verify before TTS. Do not spend Sarvam credits on this cut.
**Checks:** L1 12 / L2 2 / L3 1 / L4 1 / L5 0 / L6 0 / S1 _pending_  (counts = FLAG hits)

**One-line read:** the reporting, the structure and the mechanics are all sound — this is a well-built episode that fails on vocabulary. Twelve L1 hits are not twelve different problems; they are one habit, the desk register leaking into the narration ("green", "the benchmark", "on the board", "the call", "we track", "Brent", "the next session is entitled to price that"). The two L2 hits are the serious ones: a company named twice and never placed, and a cohort referenced a sentence before its members. Every fix below is a phrase swap. None of them touches the reporting or the word band.

**Isolation note:** the ledger below was built cold — script plus canonical exemplar only. The brief was never opened in this verifier's context; the Step 2 source spot-check was delegated to a separate reader after the ledger was written to disk.

## Per-sentence ledger

**Open**

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK

**Beat 1 — the two notifications**

4. "Two government notifications organised today's session, and neither was a market event." — OK (borderline: "a market event" is mildly abstract, but the next four sentences supply the meaning)
5. "The electronics ministry cleared its first batch of component projects, nearly seven thousand nine hundred crore rupees." — FLAG (L1: the money figure hangs as a bare appositive — nearly seven thousand nine hundred crore rupees *of what*? approved investment, committed subsidy, project value? A listener cannot tell. Also "component projects" is unplaced: components for what.)
6. "The defence ministry published a sixth list of four hundred and five items to be bought from Indian suppliers." — OK (borderline: "a sixth list" invites "sixth of what", but the sense survives one hearing)
7. "Both sets of shares rose while the market fell." — FLAG (L2: "both sets of shares" is a two-cohort reference whose members are named only in the NEXT sentence. A listener hears linearly and has nothing to attach it to. The exemplar names Zee in the same breath as the media move.)
8. "Paras Defence and Space Technologies gained ten percent, and Jyoti C N C Automation eight point three percent." — FLAG (L2: neither company gets a plain what-it-does. Paras half-explains itself in its name; Jyoti C N C Automation does not — "C N C" is jargon, and the listener never learns it is a machine-tool maker. Jyoti is named twice in the episode and never placed.)

**Beat 2 — the index versus the market**

9. "The Nifty fifty closed at twenty four thousand one hundred and fifty four, down zero point five five percent." — OK
10. "But the index fell and the market did not." — FLAG (L4: an epigram standing in front of the mechanism instead of behind it. The listener meets a flat contradiction before the explanation arrives. Plain form: "the average fell, but most shares did not.")
11. "Inside the Nifty fifty, eight shares rose and thirty three fell." — OK
12. "The smallcap index was the only green headline index, and six of the eleven biggest movers we track closed at one year highs." — FLAG (L1, two hits: "green" is trader shorthand for up, and "the eleven biggest movers we track" is producer-view meta — it exposes the desk's internal tracking universe, exactly the "producer's cut" failure the exemplar bans.)
13. "That is a market pulling apart, not a market selling off." — OK (borderline L4 — figurative, but the two preceding sentences have already earned it)
14. "Almost all of the damage came from technology." — OK
15. "That index fell one point nine three percent, more than three times the benchmark, with all eleven members down." — FLAG (L1: "the benchmark" is desk shorthand for the Nifty fifty and is never defined; "members" is index jargon. Also elliptical — three times the benchmark's *fall*, not the benchmark.)

**Beat 3 — nothing from abroad**

16. "Asia split in two today and emerging market funds barely moved." — FLAG (L1: "Asia split in two" is unexplained (split how? which half went where?), and "emerging market funds" is desk vocabulary dropped without a gloss. Neither survives one hearing.)
17. "Nothing outside India explains a fall of half a percent." — OK
18. "Today was made at home." — OK (figurative but immediately legible, and it closes the chain rather than replacing it)

**Beat 4 — oil**

19. "The worrying story is oil, and it is not about today." — OK
20. "Tanker attacks near the Strait of Hormuz have resumed, and weekend traffic through it reportedly nearly stopped." — FLAG (L1: the Strait of Hormuz is used unplaced. The exemplar explicitly glosses it — "the narrow lane that carries much of the world's oil" — precisely because a naive listener does not know why that waterway matters.)
21. "Brent is about nine percent higher than on the seventh of August." — FLAG (L1: "Brent" is never explained. First use, no gloss, and the whole oil beat rests on it. A listener who does not know Brent is the world crude price loses the paragraph.)
22. "The Reserve Bank of India cut its inflation forecast this month, explicitly because crude was cheap." — OK
23. "That reason has reversed inside a fortnight." — OK

**Beat 5 — the price gap**

24. "One more thing that gets missed." — OK
25. "What factories charged for their goods rose eight point two nine percent in July." — OK (strong: wholesale inflation rendered in plain English with no jargon at all — this is exemplar-grade)
26. "What households paid in the shops rose four point four five percent." — OK
27. "That gap gets absorbed by whoever sits in between and cannot raise prices." — OK
28. "Packaged goods, chemicals, cement." — OK (fragment, but it reads as a deliberate audio beat)
29. "It is a margin story, not an inflation story." — OK

**Beat 6 — the gainers**

30. "Now the movers." — OK
31. "Paras rose on the defence list, announced at twelve nineteen, during trading hours." — OK
32. "That timing makes it the cleanest explanation on the board." — FLAG (L1: "on the board" is trading-desk shorthand; "the cleanest explanation" is the analyst's view of the story rather than the story — exemplar rule six.)
33. "But hold the size in mind." — OK
34. "The whole list is an estimated three thousand and seventy crore rupees of business potential, spread over years across the entire defence supply chain." — OK (24 words, single thread, speakable)
35. "Paras alone is worth about four times that." — FLAG (L1: "worth" silently means stock-market value. A listener will read it as revenue or assets, and the comparison — the company is bigger than the whole opportunity — is the point of the beat, so the ambiguity lands on the load-bearing sentence.)
36. "Jyoti disclosed its own approval at ten twenty two on Monday night." — FLAG (L1: "its own approval" has no referent a listener can recover. Approval of what, by whom? The electronics scheme is never linked back.)
37. "The next session is entitled to price that." — FLAG (L3 + L1: desk shorthand, and it strands the listener in time. "Monday night" plus "the next session" points at today — the session just recapped — but on one hearing it sounds like a forward-looking claim about tomorrow. In an evening recap the same fact should be stated as: today was the first session that could react to it.)

**Beat 7 — the fall and its mirror**

38. "The one real fall was Ahluwalia Contracts, a construction company, down almost eleven percent." — OK (name-on-mention done right)
39. "June quarter sales rose twelve percent and net profit fell almost eighty percent." — OK
40. "That is not a demand problem but a cost problem, in a business where input costs decide margins." — OK
41. "The results came after Friday's close, the call after Monday's close, and the verdict today." — FLAG (L1: "the call" is unglossed shorthand for the analyst or earnings call. Nothing earlier in the script introduces it, so the listener hits an undefined noun in the sentence that carries the whole timestamp lesson.)
42. "The call made it worse, not better." — FLAG (L1: inherits the undefined "the call"; also "made it worse" has an unstated object — worse for the shares.)
43. "The same sequence ran the other way at Tube Investments of India, an engineering group, up almost eight percent." — OK
44. "June quarter revenue rose seventeen percent, with double digit growth in every segment, not one lucky division." — OK
45. "Same order of events, opposite ending." — OK

**Beat 8 — the correction and the limit**

46. "Here is what struck me most today." — OK
47. "The papers explained the fall with high crude and rising American bond yields." — OK (borderline: "bond yields" unglossed, but it is common enough currency)
48. "Brent moved one hundredth of one percent today." — OK on its own terms (inherits the undefined "Brent" from sentence 21)
49. "It did not move." — OK (excellent — the correction stated flatly, once)
50. "Crude is at a high level and American yields are rising, but a level is not an event." — OK (borderline L4 aphorism, but the distinction is the point and it is made in plain words)
51. "And now my own limit." — OK
52. "I could not find a dated reason for the technology fall, and I am not going to invent one." — OK
53. "I can tell you what the press got wrong." — OK
54. "I cannot tell you why technology fell." — OK

**Beat 9 — tomorrow**

55. "Tomorrow night the American Federal Reserve is due to publish the minutes of its July meeting, around half past eleven our time." — OK (L3 correct for the evening model: a not-yet-happened event framed as tomorrow)
56. "Three of its regional presidents voted for a rate increase." — OK (borderline: no time anchor — at the July meeting — so it briefly reads as present tense)
57. "India trades them on Thursday." — FLAG (L1: "India trades them" is desk shorthand. Plain form: Indian markets get their first chance to react on Thursday.)

**Close**

58. "That's your brief." — OK
59. "Before I sign off: this has been general market commentary, not investment advice." — OK
60. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK (SEBI is an initialism the TTS will read as a word, which is the intended pronunciation; consistent with the exemplar)
61. "Markets are risky; you may lose money; act with care." — OK
62. "See you tomorrow." — OK

**L5 — TTS mechanical (machine-checked on the spoken body):** zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero exclamation points, zero bracket hints. Word count 698 — inside the 500-700 band, at its ceiling. **PASS.**

**L6 — Sentence listenability:** longest sentence 24 words (sentence 34), single-thread and cleanly comma-segmented. No nested-clause sentences anywhere. **PASS.**

**L3 — Time discipline:** the covered session is consistently "today"; the Fed minutes are "tomorrow night" with the Indian reaction on Thursday; Friday and Monday closes are correctly past. One defect only — sentence 37. Otherwise clean.

## Punch list

Ordered by severity. The first three are the ones the principal's eye should go to.

**FAIL-level**

1. **[L2, sentence 8] Jyoti C N C Automation is never told what it does.** It is named twice — as an eight point three percent gainer, and again on the Monday-night disclosure — and a listener finishes the episode not knowing it makes machine tools. "C N C" is unglossed jargon carrying the weight.
   *Rewrite (source-bound — see S1 constraint 2 below):* "Paras Defence and Space Technologies gained ten percent. Jyoti C N C Automation, one of the companies in that electronics batch, gained eight point three percent."
   *Note added after the source spot-check:* the brief carries NO description of Jyoti's business, so the fix cannot import one. Place the company by its role in the story instead. A real what-it-does line has to be added to the brief first.

2. **[L1, sentence 21] "Brent" is used unexplained, and the entire oil beat rests on it.** Compounded at sentence 48, where the correction that Brent did not move is the spine of the episode.
   *Rewrite (first use):* "Brent crude, the world benchmark oil price, is about nine percent higher than on the seventh of August."

3. **[L1, sentence 12] "the only green headline index" plus "the eleven biggest movers we track".** Two hits in one sentence: "green" is trader shorthand, and "we track" exposes the desk's internal universe — the producer-view failure the exemplar names first.
   *Rewrite:* "The smallcap index was the only major index to finish higher, and six of the biggest movers of the day closed at their highest level in a year."

4. **[L1, sentence 20] The Strait of Hormuz is used unplaced.** The exemplar glosses it every time for exactly this reason.
   *Rewrite:* "Tanker attacks have resumed near the Strait of Hormuz, the narrow lane that carries much of the world's oil, and weekend traffic through it reportedly nearly stopped."

5. **[L3 + L1, sentence 37] "The next session is entitled to price that."** Desk shorthand, and it strands the listener in time — Monday night plus "the next session" means today, the session being recapped, but on one hearing it sounds like a claim about tomorrow.
   *Rewrite:* "That landed overnight, so today was the first session that could react to it."

6. **[L1, sentences 41-42] "the call" is never introduced.** It appears in the sentence carrying the whole timestamp lesson.
   *Rewrite:* "The results came out after Friday's close. The company took questions from analysts after Monday's close. Today the market gave its verdict, and those questions had made things worse, not better."

7. **[L1, sentence 36] "Jyoti disclosed its own approval" has no recoverable referent.** Approval of what, by whom — the electronics scheme from the opening beat is never linked back.
   *Rewrite:* "Jyoti told the exchange at ten twenty two on Monday night that it had won a place in that same electronics scheme."

8. **[L1, sentence 16] "Asia split in two today and emerging market funds barely moved."** Split how, and which way? Both halves are desk vocabulary.
   *Rewrite:* "Some Asian markets rose today and others fell, with no common direction, and foreign money moving across emerging markets barely shifted."

**WARN-level**

9. **[L1, sentence 15] "the benchmark" and "members".** Say "more than three times the fall in the Nifty fifty, with every one of its eleven companies down."
10. **[L1, sentence 35] "Paras alone is worth about four times that."** "Worth" silently means stock-market value; a listener will hear revenue or assets. Say "Paras on its own is valued on the stock market at about four times that."
11. **[L1, sentence 32] "the cleanest explanation on the board."** "On the board" is desk shorthand and the phrase is the analyst's view of the story. Say "That timing is the clearest link we have between news and price today."
12. **[L1, sentence 57] "India trades them on Thursday."** Say "Indian markets get their first chance to react on Thursday."
13. **[L1, sentence 5] The electronics figure is a bare appositive.** Nearly seven thousand nine hundred crore rupees *of what*? Give the noun.
14. **[L4, sentence 10] "But the index fell and the market did not."** The epigram arrives before the mechanism that earns it. Consider inverting: state the eight-up, thirty-three-down split first, then land the line.
15. **[sentence 56] "Three of its regional presidents voted for a rate increase"** has no time anchor and briefly reads as present tense. Add "at that July meeting".
16. **[S1, sentence 34] Restore "public-sector".** The brief says the three thousand and seventy crore is spread across the entire defence *public-sector* supply chain; the script drops the qualifier and widens the scope. One word, free to fix.

**Do NOT touch during the fix pass**

- Sentences 25 to 29 (the factory-gate versus shop-price beat). The plain phrasing is load-bearing for accuracy, not just for style — see S1 constraint 1.
- The withheld Tube Investments profit figure (sentence 44). The brief refuses to publish one on purpose.
- The "reportedly" hedge (sentence 20) and "is due to publish" (sentence 55). Both mirror real hedges in the brief and must survive.

**What the script gets right (do not lose these in the fix)**

- Sentences 25 to 29 are exemplar-grade: wholesale versus retail inflation rendered with zero jargon, then the so-what named in one line.
- Sentences 46 to 54 — the press correction and the honest admission of not knowing why technology fell — are the strongest passage in the episode and better than anything in the current exemplar. Flagging for the principal: this is the "script improves on the exemplar" signal the skill says to raise rather than let drift.
- Ahluwalia and Tube Investments both get a proper what-it-does on first mention (sentences 38 and 43). The fix for Paras and Jyoti is to match what the script already does correctly twice.
- L5 and L6 are fully clean; nothing here requires a re-run of the mechanical checks.

## Source spot-check (S1)

**S1 PASS — no number or direction mismatch against the brief.** Run after the ledger was written to disk, and delegated to a separate reader so the brief never entered the cold-read context.

Twenty-three checkable claims reconciled. All resolve to a line in `briefs/public/2026-08-18.md`. **No wrong-day leakage** — the 2026-06-04 failure mode (a prior session's numbers landing on the wrong script) does not recur here. The two date-bearing figures, the nine percent crude move since the seventh of August and the Monday-night Jyoti filing, are both correctly carried as dated rather than as today's. **No causal reversals.**

Confirmed against the brief: Nifty fifty at twenty four thousand one hundred and fifty four point nine, down zero point five five percent; eight up and thirty three down inside the index; smallcap the only green headline index; six of eleven biggest movers at fifty two week highs; Nifty IT down one point nine three percent with all eleven members down; Paras plus ten point zero zero percent; Jyoti plus eight point three zero percent; Ahluwalia minus ten point eight five percent with sales up twelve point zero three percent and profit down seventy nine point seven one percent; Tube Investments plus seven point nine four percent with revenue up seventeen percent; Brent at ninety point eight six dollars, minus zero point zero one percent on the day and roughly nine percent above the seventh of August; retail inflation four point four five percent; the twelve nineteen defence announcement; the three thousand and seventy crore figure with its "not an order book, nothing awarded" caveat; Paras at roughly four times it (market cap twelve thousand three hundred and eight crore divided by three thousand and seventy equals four point zero one); the Fed minutes on Wednesday the nineteenth at about twenty three thirty India time with three regional presidents dissenting for an increase, and India trading them Thursday.

Also confirmed correct: **the Jyoti timestamp.** The brief says twenty two twenty two on Monday night; the script's "ten twenty two on Monday night" is the correct twelve-hour rendering, not an error.

Also confirmed correct: **the withheld Tube Investments profit figure.** The brief explicitly refuses to publish one, because two public versions exist showing profit down three percent and down forty three percent. Omitting it is mandatory, not stylistic. **Do not let a rewrite pass restore a profit number.**

### Three sourcing constraints the fix pass must respect

1. **The eight point two nine percent is NOT headline wholesale inflation.** The brief's headline July wholesale figure is nine point seven eight percent; eight point two nine percent is the factory-gate component. The script's phrasing — "what factories charged for their goods" — tracks the brief exactly and is the reason the number stays correct. **Do not "clarify" this to "wholesale prices" or "producer prices" during the rewrite.** That single word swap would attach the right sentence to the wrong number and would be the one place a listener could carry away a false figure. This is the strongest argument for leaving sentences 25 to 29 exactly as they are.

2. **The brief contains no description of what Jyoti C N C Automation does.** It carries only the Rajkot plant and the one thousand and twenty point six five crore rupee five-year investment under the electronics scheme. So the L2 fix in punch item 1 cannot import a business descriptor from outside the source — the script is source-bound to the brief and does no independent reporting. Fix it from inside the source instead: place Jyoti by its role in the story that is already being told, for example "Jyoti C N C Automation, one of the companies in that electronics batch, gained eight point three percent." If the principal wants a real what-it-does line, it has to be added to the BRIEF first, not invented at the script stage. The L2 flag stands either way — a company named twice and never placed is still a listener failure.

3. **Scope widening on the defence supply chain.** Brief: "the entire defence **public-sector** supply chain." Script (sentence 34): "the entire defence supply chain." Dropping "public-sector" widens who the three thousand and seventy crore is spread across. Not a number error and not an S1 mismatch, but it is a free fix — restore the word.

### Minor, non-blocking

- Sentence 15 says the technology index fell "more than three times the benchmark"; the brief says three and a half times. The script understates, which is the safe direction. No action needed beyond the L1 wording fix already listed.
- Sentence 16 says emerging market funds "barely moved"; the brief says "mildly weaker". The script drops a direction rather than contradicting one. If the L1 rewrite of that sentence happens anyway, restore "slightly weaker".
- Sentence 6's "to be bought from Indian suppliers" is true by definition of an indigenisation list but is not spelled out in the brief. Acceptable as a gloss of the instrument; noted for completeness.
- Sentence 20's "reportedly" hedge and sentence 55's "is due to publish" hedge both correspond to real hedges in the brief. **Both must survive the rewrite.** The brief flags that the Hormuz transit counts trace to a single shipping-data read, and that the Fed date comes from one markets desk rather than the Fed's own calendar.

---

## Verdict rationale

FAIL is driven entirely by the cold read, not the sourcing. The episode is factually clean, correctly timed, mechanically TTS-ready and inside the word band. It fails on listener vocabulary: twelve L1 desk-shorthand hits and two L2 name-placement misses. Every fix is a phrase swap that leaves the reporting untouched, and the word budget has room only at the margin — the body is at six hundred and ninety eight of a seven hundred word ceiling, so the fix pass will need to trade the gloss words in against something. The eight L1 items in the FAIL block are the ones that must clear before TTS.

Per the skill's honest-constraints note: sentences 46 to 54, the press correction and the refusal to invent a reason for the technology fall, are better than any passage in the current canonical exemplar. Raising it with the principal rather than letting it drift silently — this may be exemplar-refresh material once the vocabulary is fixed.
