# Podcast Script — 2026-08-20 (evening recap: the rise was made in Washington, and India got the smallest share of it)

**Word count:** 700 words (spoken body only)
**Estimated duration:** 4.24 minutes at 165 WPM
**Self-verify:** PASS. Machine-checked on the spoken body: zero digits, zero currency or percent symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation points, zero banned trader jargon, zero recommendation language before the firebreak. Longest sentence 29 words, single-thread and comma-segmented. Word count 700, at the ceiling of the 500-700 band.
**Revision:** **fix pass v2** — the one permitted pass against the cold read's FAIL. v1 is backed up at `backups/2026-08-21/podcast-script_2026-08-20_v1.md`.
**Cold-read verifier (`verify-podcast-script-nse`):** v1 **FAIL** — L1 16 / L2 1 / L3 1 / L4 2 / L5 0 / L6 0, S1 2. Six blockers plus a missing unit. Report at `verify-report.md`. v2 clears all six blockers, the unit, both S1 factual mismatches, and 14 of the 16 L1 items.
**Skill version:** podcast-script-public-nse v1.7 (evening recap model)
**TTS-ready:** YES
**Source:** `briefs/public/2026-08-20.md` only. No independent reporting.
**Continuity:** the last public episode was 2026-08-18. There was no public run on the 19th, so this is a two-session gap.

## Fix pass v2 — every change, and what it cost

**The two factual mismatches (S1), both fixed.**

1. **Wrong period, and a dropped hedge.** "She sees a case for a rate increase emerging next financial year" pushed the brief's FY 2026-27 roughly twelve months out — on 20 August 2026 that is the *current* financial year — and dropped the brief's "may". Now: *"She argues a case for a rate rise may emerge in this financial year."* Both the period and the modal are restored.
2. **The missing comparator on the takeover premium** is fixed by removal, not rewording. See the beat-drop note below.

**The four cold-read blockers, all fixed.**

3. **The oil "because" argued against itself.** As heard, India came last *because* Brent rose, three sentences after Japan and Korea, also oil importers, rose more. Confidence is now hedged and the mechanism is spoken: *"The likely reason India lagged is oil... India buys almost all of its oil from abroad, so a dearer barrel feeds straight into Indian inflation, and inflation is what the Reserve Bank is already worried about."* The inflation clause is the part that actually separates India from Tokyo and Seoul, and it hands the listener forward to the wedge.
4. **"either" is gone.** It attached the risers to Himadri, whose only nearby statement was that we did not search — converting our non-search into "no cause exists", the exact false negative the Himadri line was written to prevent. The risers sentence now stands alone with the brief's own wording, "no cause anyone can point to".
5. **"Nobody has set those two side by side"** is now *"Set those two documents side by side."* Same rhetorical turn, no claim about all commentary everywhere.
6. **The newsroom register is gone.** "We ran fifteen checks and killed three stories that would have shipped, all wrongly dated" is now *"We did go looking there, fifteen times over. Three of the explanations we found turned out to be old stories with the wrong date."*
7. **The missing unit is gone with its sentence.** "The thirty year fell nine" read most naturally as nine percent, off by about 150 times. The verifier and the orchestrator both offered the cut; taken, because it also retires the script's most mangle-prone line. The ten-year now carries its unit, a gloss and a rounded level.

**Nine further L1 clarity fixes, unprompted but flagged in the ledger.** "Yields" glossed for the first time (*"A bond's yield is what it pays whoever holds it"*). "The ten year" given its noun (*"the ten year"* now sits inside a glossed-yield sentence, and the three-decimal 4.647% is spoken as "about four point six five percent"). "Basis point" glossed. "Now the part the headlines skipped" replaced with the exemplar's own claim-free signpost, "Here is the key part". The hook's second pronoun given a real antecedent (*"the rally it set off"*). The sugar chain spelled out in full — a government only rations stock when a price has already run, so the order is *evidence* of a high price, and a high price is good for the mills. "Easing" replaced with "no room left to cut". "Records that" replaced with "says". The Fed fragment given a verb and a subject (*"Its rate setters voted nine to three to hold, and the three who dissented wanted a rise"*). "Those minutes" in the close given its owner ("Its August minutes"). "Share we follow" replaced with *"stock in the seven hundred we cover"*, which defines the universe and retires the faint portfolio reading. "We ran no search on it, so I am not going to guess" re-voiced as *"I cannot tell you why, because we did not look into that one."*

**⚠️ What it cost: the Indo Borax beat is dropped entirely.** The fixes above add roughly 110 words and the band ceiling is 700. Every clarity fix is load-bearing; the takeover was the one beat that is not part of the episode's three acts (Washington, the two sets of minutes, sugar), and the skill explicitly sanctions cutting movers to two rather than rushing. Dropping it also retires both of its own flags — the missing what-it-does descriptor and the fifty-two-percent comparator — without spending words on either. **This means the orchestrator's fix 2 was executed by removal.** If the beat is wanted back, something else has to go; say which and I will swap. The written brief carries it in full.

**The "Good evening" consistency point, decided.** Kept, and declared here as a **fixed brand open**, on the same footing as "See you tomorrow" at the close. The skill specifies Section 0 verbatim as "consistent every day for brand recognition; NOT a per-day variation", so it is a show open, not a time-of-day claim. The day-name deviation continues to apply to every *factual* time-word.

**Deliberate deviation from the exemplar, restated.** The exemplar's evening model calls the covered session "today". This brief covers **Thursday**, was written Friday roughly fifteen hours late, and publishes Friday. Saying "today" would be false at the moment of listening, so the script uses day names throughout — verified clean across all time-words in v1 and unchanged in v2.

**No `[SAY:]` hints** — `tts-podcast-nse.py` strips them with no substitution, so they are inert. Mangle risks are respelled in the spoken body: **toro I-Q** for the brand. The Reserve Bank of India is said in full, never "R-B-I", and "Nifty I T" is avoided entirely.

**Guarded omissions, all still honoured:** no India VIX, no 52-week or lowest-since anything, no Suven, no Genus Power, no Netweb, no India ten-year yield, no sector ranking, no institutional flows, no year-to-date. Kospi stays a range. Reserve Bank policy is unchanged at 5.25%, held unanimously, with Gupta's hike case scoped to the minutes and to this financial year. Himadri carries our own limit, never a false negative, and the fifteen checks are scoped to the risers alone.

**Audio status:** NOT generated. Awaiting the re-verify and principal approval per the TTS gate.

---

Good evening. This is India Markets Brief from toro I-Q. Your read on Thursday's session.

The Nifty rose on Thursday, ending a seven session losing run. The reason was not Indian. It was made in Washington, and India got the smallest share of the rally it set off.

Here is where the market closed. The Nifty fifty finished at twenty four thousand two hundred and thirty one, up zero point six four percent. About three and a half shares rose for every one that fell.

Korea's Kospi gained roughly five and a half to six percent, and Japan and Hong Kong each rose a little over one percent. The likely reason India lagged is oil. Brent crude rose for a fifth straight session, to ninety three dollars and eighty seven cents a barrel. India buys almost all of its oil from abroad, so a dearer barrel feeds straight into Indian inflation, and inflation is what the Reserve Bank is already worried about. The Strait of Hormuz, which carries much of the world's oil, has been shut since February. The rally came from Washington. The brake came from Hormuz.

On Wednesday the American Treasury said it will at least double its buybacks of long dated government bonds, from two billion dollars an operation to at least four billion. A bond's yield is what it pays whoever holds it. Long term American yields fell the same session, the ten year by five point seven basis points, to about four point six five percent. A basis point is one hundredth of one percent.

Here is the key part. A buyback is a debt management operation, not new money and not stimulus. And it does not begin until the ninth of September. India rose on an announcement whose first effect is three weeks away.

The biggest gain was a sugar producer, Balrampur Chini Mills, up seventeen point eight seven percent, and sugar shares rose up to eighteen percent industry wide. On Wednesday the government capped bulk buyers of sugar at fifteen days of stock. The order binds buyers, not mills, and it is meant to bring sugar prices down, not push them up. But a government only rations stock when the price has already run hard. Spot sugar touched five thousand five hundred and thirty rupees for a hundred kilos, reported as a sixteen year high. Which is good for the mills that sell it, and that is what lifted the shares.

Only one stock in the seven hundred we cover fell more than five percent. Himadri Speciality Chemical, down six point one four percent. I cannot tell you why, because we did not look into that one. Eight of the ten biggest risers have no cause anyone can point to. We did go looking there, fifteen times over. Three of the explanations we found turned out to be old stories with the wrong date.

Here is what struck me this week. Two central banks published their meeting minutes seven hours apart on Wednesday, and both were arguing about raising rates. At the Reserve Bank of India, Deputy Governor Poonam Gupta says there is no room left to cut. She argues a case for a rate rise may emerge in this financial year, and she has inflation peaking at five point nine percent in the December quarter. India's rate itself is unchanged at five point two five percent, held unanimously. The American Federal Reserve's minutes followed that night. Its rate setters voted nine to three to hold, and the three who dissented wanted a rise. Set those two documents side by side. The irony is that Thursday's relief came from a debt operation, not from any change in rates. Both are arguing about the same direction, and it is not down.

One date to keep. The Reserve Bank of India next meets on rates from the fifth to the seventh of October. Its August minutes just made that meeting a lot more interesting.

That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow.
