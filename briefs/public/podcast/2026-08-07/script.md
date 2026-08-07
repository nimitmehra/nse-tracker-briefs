# Podcast Script — 2026-08-07 (evening recap: a draft rule that is not law moved a large-cap almost six percent)

**Word count:** 696 words narrated (spoken body only)
**Estimated duration:** 4.22 minutes at 165 WPM
**Self-verify:** PASS. Machine-checked on the spoken body: zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation points, zero banned trader jargon, zero recommendation words before the firebreak. Longest sentence 24 words. Word count 696, inside the 500-700 band.
**Revision:** fix pass v4. v1 FAILed the cold read; v2 cleared all nine FAIL hits (verdict WARN); v3 applied the two issues the v2 fix pass itself introduced, both flagged by the verifier; v4 applies the independent cold-read verifier's two blockers plus one orchestrator override (see "Fix pass v4" below). Backup of v3 at `backups/2026-08-07/podcast-script_2026-08-07_v3.md`. Backup of v1 at `backups/2026-08-07/podcast-script_2026-08-07_v1.md`. Report at `verify-report.md`.
**Cold-read verifier (`verify-podcast-script-nse`):** v1 FAIL (L1 4 / L2 5 / L4 3 / L6 1) → v2 **WARN**, all nine FAILs cleared, L2 and L6 to zero. v3 is v2 plus the verifier's own two v2 punch-list items, so the report's residual WARNs are already spent.
**Skill version:** podcast-script-public-nse v1.7 (evening recap model)
**TTS-ready:** YES

**No `[SAY:]` hints anywhere — they are inert.** `tts-podcast-nse.py:100` strips them with no substitution, so only the visible spoken text is voiced. Every mangle risk is respelled or avoided in the spoken body itself.

**Respelled in-body:** **toro I-Q** (the brand; a known live mangle risk no hint can fix). **Initialisms avoided rather than respelled:** the Reserve Bank of India is said in full (never "R-B-I"); Oil and Natural Gas Corporation in full (never "O-N-G-C"); "lenders who are not banks" (never "N-B-F-C"); Bharat Petroleum and Indian Oil said as names (never "B-P-C-L" / "I-O-C"). **Deliberately NOT respelled**, because the default word-reading is correct: SEBI, Nifty, Sensex, Bajaj Finance, Siemens, Shivalik, Titan, Ola.

## Composition notes — the accuracy decisions

**The draft is never spoken as enacted policy.** Three separate sentences carry the status: "It was a draft", "It is not law", "Comments are open until the twenty eighth of August", and the close returns to it a fourth and fifth time ("when comments close on that draft. Whether the ban survives at all is still open"). The framing sentence is "The market priced it today as though it already were" — the whole point of the episode.

**Brent direction, front-loaded and magnitude-safe.** Spoken as "fell again, and is down roughly nine point four percent over the week." No daily magnitude anywhere, because the brief withholds it (our feed and an independent read disagree on size, agree on direction).

**ONGC direction.** Said in full as Oil and Natural Gas Corporation and explained in plain words before the number: "It pumps crude rather than buying it, so a cheaper barrel cuts what it earns. It closed up zero point four percent." The payoff line is the inversion, worded so it cannot contradict its own numbers. Both earlier attempts failed the cold read. The shipping wording and its history sit in Fix pass v4 below.

**Hormuz is omitted entirely.** The brief carries two separate instruments (the Iran-Oman in-principle arrangement, and a separate Iranian parliamentary measure on American and Israeli vessels) that are actively being conflated in the press. Narrating them apart correctly costs about eighty words and neither has a causal role in today's Indian session. Omitting is safer than compressing, and it bought the oil wedge its full length.

**No Hero MotoCorp growth rate** — the name is not spoken at all. The brief publishes levels only because the comparison base is broken, and a level with no growth rate is not audio material.

**Two descriptors are not in the brief, by necessity.** "Siemens Energy India, which makes power equipment" and "Shivalik Bimetal Controls, a small industrial company" — the brief carries neither company's line of business, but the cold read failed both names as unplaceable by ear. Both descriptors are the minimum that makes the name hearable, carry no causal or valuation weight, and are consistent with what the brief does state (an order backlog for the first, a market value of five thousand three hundred crore rupees for the second). Every number in both beats is the brief's.

**Five, not seven, unexplained names.** The brief's "cause not established" gainers above seven percent number five (Sapphire Foods, Pearl Global, Avalon, Devyani, Techno Electric). The script says five.

**Deliberate omissions, all for the word band:** the rupee level, India VIX, the two additional Reserve Bank capital consultations, the market regulator's inspection rewrite, the gold retailers-versus-fabricators wedge, the IT large-cap-versus-mid-cap wedge, EIH and Tata Technologies. One wedge only, per the skill.

## Fix pass v2 — what the cold read caught

**FAIL 1, the episode-breaker.** The lead pinned the day on a draft aimed at "lenders who are not banks", and the biggest fall was never identified as one of them. A naive listener heard two unconnected stories. Now: "The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at."

**FAIL 2, movers with no what-it-does.** Siemens Energy India is now "which makes power equipment"; Shivalik Bimetal Controls is now "a small industrial company"; both descriptors are minimal and non-claiming. Siemens also regained a significance line ("Growth and margins moving together").

**FAIL 3, producer-view data gaps.** "Two things we could not see tonight / thirteen of the fifteen sector indices / the government bond curve" narrated our pipeline's status as market news. Now listener-facing, with the bond point given the reason it matters: "the government bond market, where borrowing costs are set, came back empty for a fourth day running. On a day about credit, that is the one number you would want."

**FAIL 4, bare names and orphan articles.** "Titan, Ola Electric and Hitachi Energy India" was three unexplained names for a beat whose only point is timing; now "Several companies filed their quarters after the close today, Titan among them." "The four funds" had no antecedent; now "Four exchange traded funds".

**Also fixed:** "That is arithmetic, not a second signal" (desk shorthand) is now "It is not a second piece of bad news". "any single day's tick" (jargon) is gone. Breadth counts carry a universe (v2 used "Across the whole market"; v4 narrows it to ours, see below). "The market priced the first document and not the second" is now "The market priced the results and ignored the resignation", and the auditor resignation now says it covered the company and both subsidiaries.

**Paid for out of the word band:** the rupee macro beat (thirty four words, no causal role in today's story) and the emerging-market funds' after-our-close caveat (the script never claims they caused anything, so the caveat was insuring against a claim not made). No sourced figure was altered.

**v3, the two the verifier's v2 pass asked for:**
1. "the government bond market ... came back empty for a fourth day running" made the market the grammatical subject, so a listener could hear it as *no trading in bonds* rather than *we could not get the data*. Now: "for a fourth day running, nothing came back from the government bond market, where borrowing costs are set."
2. "Growth and margins moving together." was a verbless analyst fragment with "margins" unglossed. Now: "so profit grew faster than sales."

**Fix pass v4 — the two blockers plus one override:**
1. **Sign-off day.** "See you tomorrow." on a Friday, inherited from a Thursday exemplar, while the script itself calls the after-close filings "Monday's news" four sentences earlier. Now "See you Monday."
2. **Oil-wedge payoff.** v3 filed Indian Oil at plus zero point five and Reliance at plus zero point seven four under "did nothing with it", then called Oil and Natural Gas Corporation at plus zero point four four "closed higher" — the smaller rise called the rise. Now "So the three that stood to gain barely moved, and the one that stood to lose did not fall at all." No number changed; the direction explanation is untouched.
3. **Scope, orchestrator override (the verifier passed this line).** "Across the whole market" invites NSE-wide breadth. Our universe is the 687 priced stocks the brief scopes explicitly. Now "Across the stocks we track". One word of cost.

Net word change across all three: zero. Body stays at 696.

**Two lines most likely to need the principal's eye:**
1. "The Sensex fell more, zero point five eight percent. But that is only because it holds more financial companies, and financials were where the damage was." — check the composition effect lands as mechanical rather than as a second cause.
2. "The market priced the results and ignored the resignation." — Shivalik. It is the brief's own framing, but check it does not sound like an allegation when spoken.

**Audio status:** NOT generated. Awaiting principal review per the TTS gate.

---

Good evening. This is India Markets Brief from toro I-Q. Your read on today's session.

What moved the Indian market today was not oil, and not earnings. It was a draft. The Reserve Bank of India published a proposal on Thursday. It would stop lenders who are not banks from offering revolving credit, the kind of limit you can repay and draw again. It is not law. Comments are open until the twenty eighth of August. The market priced it today as though it already were.

Here is the close. The Nifty fifty finished at twenty four thousand five hundred and seventy, down zero point two seven percent. The Sensex fell more, zero point five eight percent. But that is only because it holds more financial companies, and financials were where the damage was. It is not a second piece of bad news. Across the stocks we track, three hundred and twenty shares rose and three hundred and sixty two fell. The selling was concentrated, not broad. Two things I could not check tonight. Most sector indices gave no usable reading. And for a fourth day running, nothing came back from the government bond market, where borrowing costs are set. On a day about credit, that is the one number you would want.

Emerging markets went the other way today. Four exchange traded funds that track emerging market shares and bonds all rose while India fell. That is the cleanest evidence we have that today was made in India.

One thing did go India's way this week. Brent crude fell again today, and is down roughly nine point four percent over the week. For a country that imports most of its oil, that matters far more than any single day.

Now the movers. The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at. It fell almost six percent, the worst share in both benchmarks. It had touched a fresh fifty two week high a week earlier, on a quarter with profit up twenty nine percent. Nothing about its earnings changed in seven days. What changed was the list of products it might be allowed to sell.

The biggest gain among the large companies was Siemens Energy India, which makes power equipment. It rose twelve percent. Revenue was up thirty nine percent and operating profit almost seventy four percent, so profit grew faster than sales.

The oddest was Shivalik Bimetal Controls, a small industrial company. It rose twenty percent and locked at its daily price limit, on revenue up a third and profit up forty five percent. In the same twenty four hours it disclosed that its outside auditor had resigned, from it and from both its subsidiaries. The market priced the results and ignored the resignation.

Five other shares rose more than seven percent and I could not establish why any of them moved. We checked everything we normally check and came back empty.

Here is what struck me most about today. The Indian companies that buy crude did nothing with that weekly fall. Bharat Petroleum finished slightly lower, Indian Oil up half a percent, Reliance Industries up under one percent. Oil and Natural Gas Corporation sits on the other side. It pumps crude rather than buying it, so a cheaper barrel cuts what it earns. It closed up zero point four percent. So the three that stood to gain barely moved, and the one that stood to lose did not fall at all. That is two sessions where neither side of India's oil chain has priced a big move in crude, and I cannot tell you why.

What to watch. Several companies filed their quarters after the close today, Titan among them. Those are Monday's news, not today's cause. Wednesday brings July inflation. The date that matters most is the twenty eighth of August, when comments close on that draft. Whether the ban survives at all is still open.

That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you Monday.

