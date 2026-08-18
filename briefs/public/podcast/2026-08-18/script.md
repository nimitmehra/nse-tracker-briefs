# Podcast Script — 2026-08-18 (evening recap: two notifications organised the session, and the papers blamed an oil price that did not move)

**Word count:** 700 words (spoken body only)
**Estimated duration:** 4.24 minutes at 165 WPM
**Self-verify:** PASS. Machine-checked on the spoken body: zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation points, zero banned trader jargon, zero recommendation language before the firebreak. Longest sentence 25 words, single-thread. Word count 700, at the ceiling of the 500-700 band.
**Revision:** fix pass v3. v1 was 1,088 words (over band). v2 (698 words) FAILed the cold read on vocabulary. v3 applies every FAIL-level item plus all six WARNs, with one orchestrator override (below). Backups at `backups/2026-08-18/podcast-script_2026-08-18_v1.md` and `_v2.md`.
**Cold-read verifier (`verify-podcast-script-nse`):** v2 **FAIL** — L1 12 / L2 2 / L3 1 / L4 1 / L5 0 / L6 0, **S1 PASS** (source spot-check found no number or direction mismatch across 23 claims). Mechanics and reporting were clean; the failure was desk vocabulary leaking into narration. Report at `verify-report.md`. **v3 has not been re-verified — re-run the verifier before TTS.**
**Skill version:** podcast-script-public-nse v1.7 (evening recap model)
**TTS-ready:** YES
**Source:** `briefs/public/2026-08-18.md` only. No independent reporting.
**Continuity:** last public episode was 2026-08-07; there is no 2026-08-17 script. Voice inherited from the 08-07 script and the canonical exemplar.

**No `[SAY:]` hints** — `tts-podcast-nse.py` strips them with no substitution, so they are inert. Mangle risks are respelled in the spoken body: **toro I-Q** (the brand) and **Jyoti C N C Automation** (spaced so the letters are read as letters). Initialisms otherwise avoided: the Reserve Bank of India is said in full, never "R-B-I"; "the technology index" replaces "Nifty I-T", which a voice engine reads as the word "it".

## Fix pass v3 — what the cold read caught

**L2, the two blockers.** (1) Jyoti C N C Automation was named twice and never placed. The brief carries no description of its business, so no descriptor could be imported; it is now placed with the brief's own fact — "which is putting over a thousand crore rupees into its Rajkot plant". (2) "Both sets of shares rose" referenced two cohorts a sentence before their members. The companies are now named once only, in the movers beat, and the opening says "Shares in both groups rose while the market fell" with no forward reference to recover.

**L1, the vocabulary habit (twelve hits, all phrase swaps).** "green" to "the only major index to rise"; "the benchmark" / "members" to "the fall in the Nifty fifty" / "its companies"; "on the board" to "the clearest link between news and price today"; "the call" now introduced as "the recording of the management call"; "Brent" glossed on first use as "the global oil price"; the Strait of Hormuz glossed as "the narrow lane that carries much of the world's oil" (the exemplar's own gloss); "worth four times" to "valued on the stock market at about four times"; "its own approval" given its referent; "Asia split in two" to "Asian markets went in different directions"; "India trades them" to "Indian markets get their first chance to react".

**L3 + L4.** "The next session is entitled to price that" stranded the listener in time and is now "so today was the first session that could react". The epigram "But the index fell and the market did not" arrived before its mechanism; the breadth split now comes first and the line lands after it as "So the average fell and most of the market did not". The Federal Reserve dissent gained its time anchor.

**Orchestrator override — one item not taken.** The verifier flagged "the biggest movers **we track**" as producer-view meta and asked for it to be dropped. Scope accuracy wins: the brief's 52-week-high count is scoped to our ~700-stock screened universe, and an unscoped "biggest movers of the day" would over-claim to the whole exchange. Kept as "the biggest movers we follow" — the softer phrasing, the same scope. Same call the 08-07 script made.

**Paid for out of the word band (the fixes cost roughly 70 words).** Cut: the Sensex, "That is a market pulling apart, not a market selling off" (now redundant with the plainer line), "Same order of events, opposite ending", "Packaged goods, chemicals, cement", the Ahluwalia margin mechanism clause, and "And now my own limit". No sourced figure was altered, and the spine — the crude correction plus the refusal to invent a reason for the technology fall — is untouched.

## Composition notes — the accuracy decisions

**The spine is the crude correction paired with our own limit.** "Brent moved one hundredth of one percent today. It did not move." is followed inside the same beat by "I could not find a dated reason for the technology fall, and I am not going to invent one." The episode never implies we know why technology fell. The verifier flagged this passage as stronger than the current canonical exemplar — principal's call whether it becomes the new exemplar.

**The defence number travels with its caveat.** Three thousand and seventy crore rupees is spoken as "business, spread over years and the whole supply chain", immediately followed by "Paras on its own is valued on the stock market at about four times that". No order, no award, no contract implied.

**The factory-gate figure is not headline wholesale inflation.** Eight point two nine percent is what factories charge at their own gate, said as "what factories charged for their goods" against "what households paid in the shops". The roles are not inverted and the 9.78% headline is deliberately absent.

**No Tube Investments profit figure** (two irreconcilable public versions exist). **No MSCI, no gold, no India bond yield, no institutional flows** — all unobservable, unpublished or excluded by the brief.

**eMudhra and J.G. Chemicals are omitted entirely.** Both post-close timestamps are good audio, but the timestamp lesson is already carried by Ahluwalia's Friday-close, Monday-close, Tuesday-verdict sequence and by Jyoti's overnight disclosure.

**Two hedges carried from the brief:** "reportedly" on the Hormuz weekend traffic (single shipping-data read), and "is due to publish" on the Federal Reserve minutes (date reported by one markets desk, not confirmed from the Fed's calendar).

**Deliberate omissions for the word band:** the Sensex, the rupee, India VIX, the Reserve Bank draft-rule pair, the market regulator's caution, the Milky Mist listing, the four cause-not-established gainers, and the thirtieth-of-September swap-window date.

**Audio status:** NOT generated. Awaiting principal review per the TTS gate.

---

Good evening. This is India Markets Brief from toro I-Q. Your read on today's session.

Two government notifications organised today's session, and neither was a market event. The electronics ministry approved its first batch of component-making projects, worth nearly seven thousand nine hundred crore rupees. The defence ministry published a sixth list of four hundred and five items to be bought from Indian suppliers, not imported. Shares in both groups rose while the market fell.

The Nifty fifty closed down zero point five five percent, at twenty four thousand one hundred and fifty four. Eight of its shares rose and thirty three fell. The smallcap index was the only major index to rise. Six of the biggest movers we follow closed at their highest level in a year. So the average fell and most of the market did not. Almost all the damage came from technology. That index fell one point nine three percent, more than three times the fall in the Nifty fifty, with all eleven of its companies down.

Asian markets went in different directions today, and foreign money across emerging markets barely moved. Nothing outside India explains today's fall, which was made at home.

The worrying story is oil, and not because of today. Tanker attacks have resumed near the Strait of Hormuz, the narrow lane that carries much of the world's oil. Weekend traffic through it reportedly nearly stopped. Brent crude, the global oil price, is about nine percent higher than on the seventh of August. The Reserve Bank of India cut its inflation forecast this month, explicitly because crude was cheap. That reason has reversed inside a fortnight.

Another thing gets missed. What factories charged for their goods rose eight point two nine percent in July. What households paid in the shops rose four point four five percent. That gap gets absorbed by whoever sits in between and cannot raise prices. It is a margin story, not an inflation story.

Now the movers. Paras Defence and Space Technologies rose ten percent. The defence list was announced at twelve nineteen, during trading hours, the clearest link between news and price today. The whole list, though, is an estimated three thousand and seventy crore rupees of business, spread over years and the whole supply chain. Paras on its own is valued on the stock market at about four times that. Jyoti C N C Automation, which is putting over a thousand crore rupees into its Rajkot plant, gained eight point three percent. It disclosed that approval at ten twenty two on Monday night, so today was the first session that could react.

The one real fall was Ahluwalia Contracts, a construction company, down almost eleven percent. June quarter sales rose twelve percent and net profit fell almost eighty percent. That is a cost problem, not a demand problem. The results came out after Friday's close, the management call recording after Monday's close, and today the market gave its verdict. The call had made things worse, not better.

Tube Investments of India, an engineering group, ran the same sequence the other way, up almost eight percent. June quarter revenue rose seventeen percent, with double digit growth in every segment.

Here is what struck me most today. The papers explained the fall with high crude and rising American bond yields. Brent moved one hundredth of one percent today. It did not move. Crude is at a high level and American yields are rising, but a level is not an event. I could not find a dated reason for the technology fall, and I am not going to invent one. I can tell you what the press got wrong. I cannot tell you why technology fell.

Tomorrow night, around half past eleven our time, the American Federal Reserve is due to publish the minutes of its July meeting. Three of its regional presidents voted there for a rate increase. Indian markets get their first chance to react on Thursday.

That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow.
