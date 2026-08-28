# Verify Podcast Script — 2026-08-27 (ATTEMPT 2 / cold read of v2)

**Verdict:** FAIL (S1, one clause — correctable without re-composition)
**Checks:** L1 8 / L2 1 / L3 0 / L4 3 / L5 0 / L6 4 / S1 1 (blocking)   (counts = FLAG hits)
**Cycle:** second and final verification. v1 FAILED; this judges the rewrite on its own merits.
**Isolation:** ledger built from the script alone. The brief (`briefs/public/2026-08-27.md`) was NOT opened until the ledger below was complete and flushed to disk.

---

## Mechanical pre-check (L5)

| Check | Result |
|---|---|
| Spoken-body word count | 700 — at the top of the 500-700 band, inside it |
| Digits in body | 0 |
| `₹` / `%` / em-dash / en-dash / `[SAY:]` | 0 |
| Exclamation points | 0 |
| Day-name arithmetic (24 Mon, 26 Wed, 27 Thu, 28 Fri, 31 Mon) | all correct |

**L5: PASS.** No audio-breakers.

---

## Per-sentence ledger

_(appended in batches below)_

### Batch 1 — open, the HDFC lead, the tape (1-15)

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK (brand respelled for TTS)
3. "Your read on Thursday's session." — OK. Evening model held; the covered session is named and past-tense throughout (L3 clean).
4. "More than half of Thursday's fall in the Nifty was one share." — OK. Strong, plain, concrete cold open.
5. "H-D-F-C Bank closed down two point two three percent, and on about thirteen percent of the index that is most of a decline of zero point four eight percent." — **FLAG (L4/L6: compressed mechanism).** The listener must independently know that "thirteen percent of the index" means index *weight*, and must do the multiplication themselves. It is also the only place the index's own move (down zero point four eight percent) is stated, and it arrives buried in a subordinate clause. Name-on-mention (L2) is satisfied — the stock is named in the same breath as the move — but the arithmetic is asserted rather than walked. Plain fix: "H-D-F-C Bank is about thirteen percent of the whole index, so when it closed down two point two three percent it dragged the Nifty down most of its zero point four eight percent fall."
6. "This is a problem specific to that one bank." — **FLAG (L1: residual tension, milder than v1).** The replacement for "So this is not a banking story" is better — it no longer denies a sector story outright. But five sentences later the listener hears "Metals and state owned banks were next" in the losing-sector list, and is given no reason for that. The heard effect is still "you told me it was one bank, then you told me banks fell." The three reasons that follow are genuinely HDFC-specific, so the claim is defensible; the *sequencing* is what leaks. Cheapest fix: move this line to after the sector paragraph, or make it "This particular problem is H-D-F-C Bank's own."
7. "Its lending margin is at a record low, its cheap deposits have shrunk from thirty eight percent of the book to thirty two, and foreign investors have cut their holding for a fifth straight quarter." — OK. 34 words but single-thread, three parallel comma-segmented facts, speakable in one breath — L6 explicitly permits this. "Cheap deposits" and "the book" are borderline, but both are recoverable on one hearing.
8. "The Nifty fifty closed at twenty four thousand and ninety." — OK
9. "Underneath it, across roughly seven hundred shares, two hundred and fifty three rose and four hundred and forty nine fell." — OK. Breadth given as a plain count. No symmetric-threshold counterfactual anywhere near it (guardrail 2 respected).
10. "Not one of eleven cement companies rose." — OK. Vivid, concrete, no jargon.
11. "Metals and state owned banks were next." — **FLAG (L1, minor: elliptical).** "Were next" presumes the listener has been told they are hearing a ranked list of worst sectors; they have not. Fix: "Metals and state owned banks were the next worst."
12. "Pharmaceuticals were the one clean positive, up zero point eight four percent." — OK
13. "Asia split on Thursday and India went with the weaker half." — OK. Good plain framing.
14. "Korea, Shanghai and Taiwan rose." — OK
15. "Japan and Hong Kong fell." — OK

### Batch 2 — the two forces, and the movers (16-33)

16. "Two things sit over this market and they disagree." — OK. Clean signpost.
17. "The Reserve Bank of India's August bulletin reads the June quarter as resilient, with exports and imports both growing in double digits in July, which cuts against the idea that America's eighteen percent tariff is crushing exports." — **FLAG (L6: 37 words AND nested).** The trailing "which cuts against the idea that X is crushing Y" is a clause hanging off a clause, and it introduces a debate ("the idea that the tariff is crushing exports") the listener has not been told exists. Two sentences would carry it: "...resilient. Exports and imports both grew in double digits in July, which cuts against the fear that America's eighteen percent tariff is crushing Indian exports."
18. "But rainfall through the twenty sixth of August is thirteen percent below normal." — OK
19. "Both are true." — OK. Good short beat.
20. "The bulletin describes July, when sowing had recovered, and the shortfall widened after that." — OK. This is the reconciliation the listener needs, and it is plain.
21. "Thursday's market moved with the rain, with fertiliser, agrochemical and rural facing shares lower." — **FLAG (L4: the one real casualty of the self-initiated cuts).** v1 carried "though we are not calling it the cause"; v2 carries the hedge entirely in the preposition "with". Strictly, "moved with" states co-movement, not causation — so the sentence is not false. But *as heard*, after a sentence that has just built a monsoon-shortfall story, "Thursday's market moved with the rain" is received as "the rain moved the market." Every other uncertain claim in this script is hedged explicitly and audibly ("no cause we could establish", "our reasoning and not a sourced finding"); this one is the sole exception, and it is the most causally loaded of the three. Restore five words: "Thursday's market moved with the rain, though we are not calling it the cause, with fertiliser, agrochemical and rural facing shares lower." Cost: five words over a 700-word ceiling — take them from sentence 23 (below), which should go anyway.
22. "Now the movers." — OK
23. "No big faller appears among them, because outside the Nifty fifty our list only catches a share once it has dropped ten percent." — **FLAG (L1: process narration, down from four sentences to one, but it still has not earned its place).** Three reasons it has not:
    - It is producer-view meta — "our list" is exactly the register L1 exists to catch. The listener is being told about the desk's screening tool, not about the market.
    - It answers a question the listener has not asked. Nothing has yet been said about fallers, so no absence has been noticed; the sentence *creates* the puzzle it then explains.
    - It sets a rule that sentence 33 appears to break. The listener is told the list only catches a share below the Nifty fifty once it has fallen ten percent, and is then handed Ramco Cements at five point one one percent. The listener will not know Nifty-fifty membership either way, so most will not consciously catch it — but it is a loose thread in a script that is otherwise scrupulous.
    **The rule itself is correctly stated** — it is the ten-percent-outside-the-Nifty-fifty rule, with no invented size floor (guardrail 1 satisfied). The fix is not to reword it, it is to delete the sentence: sentence 24 already gives the listener the true market fact without narrating the tool.
24. "Twenty six shares fell three percent or more on Thursday." — OK. This is the load-bearing line, stated as a market fact with no counterfactual attached (guardrail 2 satisfied). It survives on its own if 23 is cut.
25. "The biggest riser was Bombay Burmah Trading Corporation, up thirteen percent." — OK
26. "It is an old plantations and holding company, and it owns the Wadia family's stake in Britannia, the biscuit maker." — **OK — resolved.** This lands. "Plantations" is concrete, and anchoring on "Britannia, the biscuit maker" gives a listener with no market knowledge something they can actually picture. "Holding company" is the only soft spot and the sentence carries it. L2 satisfied.
27. "The Supreme Court withdrew an observation it made in May, that four thousand six hundred and fifty five crore rupees of lease rent was recoverable over a former tea estate in Tamil Nadu." — **FLAG (L6: dense, 34 words, nested).** "Withdrew an observation... that a sum was recoverable" is a legally careful construction and legally careful is not the same as listenable. The following four sentences do rescue it, so the cluster works; the sentence alone does not.
28. "That is about forty one percent of what the company is worth." — OK. Excellent — this is what makes the number mean something.
29. "It did so on procedure." — **FLAG (L1: legal shorthand).** Four words, and "on procedure" is not plain English for a non-lawyer. It is partially rescued by the next sentence, but a listener spends that next sentence still decoding this one. Fix: "It did so on a technical point about how the case was handled."
30. "It did not rule that nothing is owed." — OK. Important honesty; keep.
31. "What moved the share was not the order, which is a week old, but the company's filing after Wednesday's close." — **FLAG (L1, minor: referent).** "The order" has not been called an order — it was introduced as "an observation" that was "withdrawn". The listener must map three things (May observation / week-old withdrawal / Wednesday filing) onto two nouns. Fix: "...was not the court's decision, which is a week old..."
32. "Nine of the ten risers have no cause we could establish." — OK on honesty; **minor flag (L1)** on the unintroduced "the ten risers" — the listener has never been told there were ten. Trivially fixed with "Nine of the ten biggest risers".
33. "The biggest fall was Ramco Cements, a cement maker, down five point one one percent, and we could not establish a cause there either." — OK. "A cement maker" supplies the what-it-does (L2 satisfied), the cause is explicitly not established (guardrail 4 satisfied), and it ties back cleanly to sentence 10.

### Batch 3 — the Nvidia observation, the forward look, the close (34-54)

34. "Here is what struck me about Thursday." — OK. Matches the exemplar's turn.
35. "Nvidia reported after Wednesday's American close, with revenue up one hundred and six percent on the year and guidance ahead of expectations." — OK for a listener. "Guidance ahead of expectations" is the softest phrase in the sentence and is still recoverable. (Figure goes to S1.)
36. "The chip makers of North Asia rose on it." — OK
37. "Indian software services fell anyway." — OK. Four words, and the whole observation turns on them. Good writing.
38. "This next part is our reasoning and not a sourced finding." — OK. **This is the guardrail-5 hedge, and it is correctly placed *before* the claim, not after.** Do not let any future edit move or trim it.
39. "Korea and Taiwan build the memory and the chips that a bigger chip forecast mechanically orders more of." — **FLAG (L6/L1: the syntax defeats the point).** A forecast does not order anything, and the sentence ends on a stranded "of" three clauses from its subject. This is the one sentence in the script a listener is most likely to simply lose, and it is carrying the whole mechanism. Fix: "Korea and Taiwan make the memory and the chips themselves, so a bigger forecast from Nvidia means bigger orders for them."
40. "Indian technology companies sell people's time, and no order for chips turns into an Indian services contract." — OK. This is the best line in the script; it is the mechanism in fourteen plain words.
41. "The same pattern ran backwards on Monday, when Korea sold off sharply and India barely moved." — OK on the guardrail: Korea is "sold off sharply" with **no magnitude attached** (guardrail 3 satisfied). **Minor flag (L4)** on "ran backwards" — what reversed was the *direction of the chip news*, not the disconnect itself, and a listener could read it either way. "The same disconnect showed up on Monday, in the other direction, when Korea sold off sharply and India barely moved."
42. "It has now run backwards twice in three sessions." — **FLAG (verify, not yet an error).** Monday the twenty fourth to Thursday the twenty seventh spans Mon / Tue / Wed / Thu. That is four sessions unless one of Tuesday or Wednesday was an exchange holiday. The script itself refers to "Wednesday's close" twice, so Wednesday traded — which puts the whole question on Tuesday the twenty fifth. **If Tuesday was a trading day, this reads "three" where it should read "four" and must be corrected before TTS.** See the source spot-check below.
43. "That is worth noticing, not yet a trend." — OK. **Resolved.** This is the replacement for "inverted" and it does the job: the jargon is gone, and the claim is now correctly sized — a two-point observation is called an observation, not a pattern.
44. "Tomorrow evening, after India has closed, America's new central bank chief, Kevin Warsh, gives his first Jackson Hole speech." — **FLAG (L2, minor: unexplained proper noun).** "America's new central bank chief" is a good plain gloss for the man. "Jackson Hole" gets none, and to a listener with no market background it is just a place name. Fix: "...gives his first speech at Jackson Hole, the annual gathering where central bankers signal what comes next." L3 is clean: a not-yet-happened event is correctly "tomorrow".
45. "He has been talking about American interest rates going up, not down, the opposite of what Indian markets have priced all year." — OK. Plain, and it supplies the stakes.
46. "It lands on Monday." — **FLAG (L1, minor: referent).** "It" is the market reaction, but the nearest noun is the speech, and the speech does not land on Monday. Fix: "India cannot react to it until Monday."
47. "And Monday the thirty first is the date to keep." — **FLAG (L1, minor: broken idiom).** "The date to keep" is not a phrase; "the date to keep in mind" or "the date to watch" is.
48. "India's June quarter growth figure lands, expected around seven point one percent against seven point eight." — OK. "Against seven point eight" is compact but the comparison is inferable.
49. "And the M-S-C-I index review takes effect at that close, so funds tracking it must trade whatever they think." — **FLAG (L1/L2: weakest sentence in the script).** Two faults compounding. First, M-S-C-I is never glossed — the listener is given initials and left to guess; "funds tracking it" is the only clue that it is an index at all. Second, "must trade whatever they think" reads as broken — the intended meaning is *regardless of* what they think. Fix: "And M-S-C-I, which builds the indexes that big foreign funds follow, changes its India list at that close, so those funds have to buy and sell to match it, whatever their own view."
50. "That's your brief." — OK
51. "Before I sign off: this has been general market commentary, not investment advice." — OK (verbatim compliance block, intact)
52. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
53. "Markets are risky; you may lose money; act with care." — OK
54. "See you tomorrow." — **OK — resolved.** Tested as heard: sentence 44 says the speech lands "after India has closed", which presupposes an Indian session tomorrow; sentence 46 then tells the listener India reacts on Monday. So the listener now knows Friday exists as a trading day, and "see you tomorrow" promises a Friday episode about a Friday session. That is no longer a contradiction. It also does not conflict with "Monday the thirty first is the date to keep" — a quiet Friday and a big Monday are compatible, and the exemplar's close is preserved verbatim.

---

## Source spot-check (S1) — brief opened only now

### Figures that match

| Script | Brief | |
|---|---|---|
| Nifty fifty closed at 24,090 | 24,090.85 | match |
| a decline of 0.48% | Nifty 50 −0.48% | match |
| HDFC Bank down 2.23%, ~13% of the index, "most of" the fall | −2.23%, "roughly 13% of the index... about 0.29pp out of a 0.48% decline"; lead reads "Over half of Thursday's fall was one stock" | match |
| NIM record low / low-cost deposits 38 to 32 / foreign holding down a fifth quarter | 3.26% record-low NIM, 32% vs 38%, fifth straight quarter | match |
| 253 rose, 449 fell, roughly 700 shares | 253 / 449 of 707 priced | match |
| Not one of eleven cement companies rose | "Not one of eleven cement names rose" | match |
| Metals and state-owned banks next | metals −1.12% typical, PSU banks −0.90%, "next... after them" | match |
| Pharma +0.84%, the one clean positive | Nifty Pharma +0.84%, "the one clean positive" | match |
| Korea/Shanghai/Taiwan up, Japan/Hong Kong down | KOSPI +1.53, Shanghai +1.13, TAIEX +0.31, Nikkei −0.20, Hang Seng −0.34 | match |
| RBI August bulletin, exports and imports double digits in July, cuts against the 18% tariff idea | verbatim in Macro & Policy | match |
| Rainfall through 26 August 13% below normal | 577.8mm vs 664.7mm, 13% below | match |
| 26 shares fell 3% or more | "26 stocks fell 3% or more on the day" | match |
| Bombay Burmah +13%, ₹4,655 crore, 41%, order a week old, filing after Wednesday's close | +13.14%, ₹4,655.24 cr, 41.3%, order dated 19-Aug, filed 15:59:29 on 26-Aug | match |
| Nine of the ten risers, no cause established | verbatim | match |
| Ramco Cements −5.11%, cause not established | −5.11%, "we could not establish a cause for it" | match |
| Nvidia revenue +106%, guidance ahead of expectations | US$96.2bn, +106%, guidance US$108bn vs US$104.2bn expected | match |
| Korea sold off sharply on Monday, India barely moved | verbatim, no magnitude in the brief either | match — **guardrail 3 satisfied** |
| Warsh, first Jackson Hole speech, tomorrow evening after India closes, lands Monday | Friday 28-Aug ~19:30 IST, "lands after India has closed, so it is Monday's input rather than Friday's" | match |
| GDP ~7.1% against 7.8%, MSCI review effective at Monday's close | consensus ~7.1% vs 7.8%; MSCI takes effect at the close | match |
| Screen rule: outside the Nifty fifty a share must fall ten percent | "Anything outside the Nifty 50 has to fall 10%, not 5%, to show up at all" | match — **guardrail 1 satisfied, no size floor invented** |
| September American rate-rise odds | brief flags single-source and refuses them; script does not carry them | correctly omitted |

### S1 MISMATCH — FAIL

> **Script, sentence 33: "The biggest fall was Ramco Cements, a cement maker, down five point one one percent…"**
>
> **Brief, Big Movers preamble:** *"Only three names fell 5% or more on Thursday — Ramco Cements (RAMCOCEM) −5.11%, and two smaller names trading under the tickers MODIS (−5.05%) and **SHANTIGOLD (−7.52%)** — and none of the three made the screen's cut."*

Ramco was **not** the biggest fall. SHANTIGOLD fell 7.52%, nearly half again as far, and it sits four lines above the very sentence the script paraphrased for "twenty six shares fell three percent or more." The brief also publishes **zero** fallers on its table and explicitly declines to rank fallers at all.

The listener takeaway from the script is "the worst any share did on Thursday was fall about five percent." That is false against the desk's own source. The number attached to Ramco is right and the cause-not-established hedge is right; the **superlative is invented**, and it is invented in the one section where this desk's published standard is strictest about superlatives — the same brief refuses to print a 52-week superlative on the volatility index because two data vendors disagree about a low.

It also collides with the script's own sentence 23: the listener is told the screen only catches a sub-Nifty-fifty share once it has fallen ten percent, and is then handed a ranked "biggest fall" of five point one one percent — a name that, per the brief, did not make the screen either. There is no frame in which both sentences are true for the listener.

**This is not new in v2 — it was in v1, and the attempt-1 report matched only the −5.11% figure and missed the superlative.** That is a miss in the previous verification, not a regression by the writer. It is still a live factual error, and it is still in the script.

**Fix (one clause, no word-count cost):** drop the superlative.
> "Ramco Cements, a cement maker, fell five point one one percent, and we could not establish a cause there either."

### S1 secondary — attribution drift (WARN)

> **Script, sentence 45:** "**He** has been talking about American interest rates going up, not down…"
> **Brief:** "The read that matters: **this is currently a conversation** about whether American rates go up, not down…"

The brief describes the ambient debate around the appointment; the script puts the position in Kevin Warsh's own mouth. The brief nowhere attributes that view to him. Fix: "The conversation around him is about American interest rates going up, not down, the opposite of what Indian markets have priced all year."

### S1 note — an inherited arithmetic wobble (low priority, upstream)

Script sentence 42, "twice in three sessions," is **faithful to the brief**, which says "Twice inverted in three sessions." But the brief elsewhere states that the NSE's monthly Nifty expiry "had already gone on **Tuesday 25 August**" — so Tuesday traded, and Monday-24 to Thursday-27 is four sessions, not three. Not an S1 mismatch (the script copies the source correctly) and not a podcast gate item; flagging it back to the brief side. If the line is being touched anyway, "twice in four sessions" is the safe read.

---

## Attempt-1 punch list — resolution status

| # | Attempt-1 item | Status in v2 |
|---|---|---|
| 1 | Process narration (four sentences of desk-tool talk) | **PARTIAL.** Four sentences to one. The stale-stories line and "shares we could price" are gone and not missed. The survivor — "outside the Nifty fifty our list only catches a share once it has dropped ten percent" — still narrates our screen, still answers a question the listener has not asked, and now conflicts with sentence 33. **Recommend deletion, not rewording**; sentence 24 already carries the market fact. Downgraded FAIL to WARN. |
| 2 | Bombay Burmah and Ramco unexplained | **RESOLVED.** "An old plantations and holding company… it owns the Wadia family's stake in Britannia, the biscuit maker" lands cleanly for a listener — "the biscuit maker" is the anchor that does it. Ramco's "a cement maker" is minimal but sufficient, and it now ties back to the eleven-cement-names line. (Business description is declared out-of-brief, sourced from one web check; the Wadia/Britannia link is uncontroversial and correctly held to that core.) |
| 3 | Missing forward-look bridge | **RESOLVED.** Friday's Jackson Hole is restored, its after-close timing is stated, the stakes are given in plain English, and "It lands on Monday" supplies Monday its cause. Two residual nits, both minor: "Jackson Hole" is never glossed for a listener who has never heard of it, and "It lands on Monday" has a loose referent. |
| 4 | Sign-off contradicted the forward look | **RESOLVED — tested as heard.** "After India has closed" presupposes a Friday session; "It lands on Monday" tells the listener India reacts on Monday. So Friday now exists in the listener's head as a trading day, and "See you tomorrow" promises a Friday episode about a Friday session. No contradiction remains, and "Monday is the date to keep" does not fight it — a quiet Friday and a big Monday coexist fine. The exemplar's verbatim close is preserved. The writer's argument holds. |
| 5 | "Selling was concentrated rather than general" | **RESOLVED on the flagged line — replacement is milder but not clean.** "This is a problem specific to that one bank" no longer denies a sector story outright, and the brief supports it (Kotak +1.80%, ICICI +0.91%, Axis +0.08% all rose). But the script cut that supporting evidence, so five sentences later the listener hears "Metals and state owned banks were next" with nothing to reconcile it. **No new contradiction introduced; the old one is softened, not eliminated.** Eight words fix it for good: "Kotak, I-C-I-C-I and Axis all rose." |
| 6 | "Inverted" | **RESOLVED.** Jargon gone. "It has now run backwards twice in three sessions. That is worth noticing, not yet a trend." is plainer than the brief's own phrasing and correctly sizes a two-point observation. Two small residuals: what "backwards" reverses is ambiguous (it is the direction of the chip news, not the disconnect), and the "three sessions" count is inherited from the brief and looks like it should be four. |

## The self-initiated cuts — what was lost

The rewrite cut roughly twenty-five words beyond the binding punch list to hold 700. Most of it was free: "the other" from the risers count, the stale-stories sentence, "shares we could price." Those are pure gain — the script is tighter and nothing died with them.

**One cut was not free, and it is the single most important line in this report after the S1 failure.**

v1: *"Thursday's market moved with the rain, though we are not calling it the cause…"*
v2: *"Thursday's market moved with the rain, with fertiliser, agrochemical and rural facing shares lower."*

That hedge was not a writer's flourish the editor could trade for word count. It is the brief's own explicit editorial position, stated in bold: **"We record that the direction lines up and we do not claim the cause, because the rainfall figure is Wednesday's cumulative data rather than a Thursday release."**

Strictly, "moved with" states co-movement and not causation, so the sentence is not false. But it arrives immediately after two sentences building the monsoon-shortfall case, and *as heard* the listener takes "Thursday's market moved with the rain" as "the rain moved the market." Every other uncertain claim in this script is hedged out loud and unmistakably — "no cause we could establish," "our reasoning and not a sourced finding." This is the only one where the hedge is carried by a preposition, and it is the most causally loaded of the three.

**Restore the five words.** Fund them from sentence 23, which should go anyway.

---

## Punch list

**Blocking (must be fixed before TTS):**

- **[S1] Sentence 33 — delete the invented superlative.** → "Ramco Cements, a cement maker, fell five point one one percent, and we could not establish a cause there either." (SHANTIGOLD fell 7.52%; the brief publishes no faller ranking at all.)

**Strongly recommended, same edit pass (all cheap, all improve the listen):**

- **[L4] Sentence 21 — restore the monsoon hedge.** → "Thursday's market moved with the rain, though we are not calling it the cause, with fertiliser, agrochemical and rural facing shares lower."
- **[L1] Sentence 23 — delete it.** Funds the two additions above and removes the last piece of desk-tool narration. Sentence 24 stands alone.
- **[L1] Sentence 6 — add the counter-evidence.** → "This is a problem specific to that one bank. Kotak, I-C-I-C-I and Axis all rose." Kills the tension with "state owned banks were next" outright.
- **[S1] Sentence 45 — de-personalise.** → "The conversation around him is about American interest rates going up, not down, the opposite of what Indian markets have priced all year."
- **[L1/L2] Sentence 49 — the weakest line in the script.** → "And M-S-C-I, which builds the indexes that big foreign funds follow, changes its India list at that close, so those funds have to buy and sell to match it, whatever their own view."

**Optional polish (ship-with is fine):**

- [L4/L6] Sentence 5 — walk the weight arithmetic instead of asserting it.
- [L6] Sentence 39 — "…so a bigger forecast from Nvidia means bigger orders for them." (the current sentence ends on a stranded "of" three clauses from its subject).
- [L6] Sentence 17 — split into two.
- [L1] Sentence 29 — "It did so on a technical point about how the case was handled."
- [L2] Sentence 44 — gloss Jackson Hole in four words.
- [L1] Sentences 11, 31, 32, 46, 47 — small referent and idiom fixes listed in the ledger.

---

## Verdict

**FAIL — on S1 only, on one clause, and everything else in this rewrite is genuinely better.**

**Checks:** L1 8 / L2 1 / L3 0 / L4 3 / L5 0 / L6 4 / **S1 1 (blocking)**

The honest summary: v2 fixed five of six attempt-1 items outright and materially improved the sixth. It is tighter, plainer, better hedged, and TTS-clean at exactly 700 words. Judged as a listen, it is the best version of this episode. **It is not the meta-quality that fails it — it is a false statement of fact that would be spoken aloud.** The script tells listeners the biggest fall on Thursday was about five percent when the desk's own brief records one at 7.52%, and it does so in the section where this desk is proudest of its discipline about superlatives.

That error is not the writer's regression; it survived v1 because the attempt-1 spot-check matched the number and never questioned the superlative. It is nonetheless in the script now.

**Is this fit to spend TTS credits on? Not as it stands — but it is one clause away.** The blocking fix is a five-word deletion that costs no word count and touches nothing else. This is not a rewrite; it is a correction.

**Escalation note for the principal.** Under the pipeline rule as stated, a second FAIL kills the episode for this date. I am recording the classification the evidence supports, not the consequence. Whether a single-clause factual correction — with no structural change and no re-composition — should trigger the kill rule rather than a correct-and-ship is a principal call, not a verifier call. If the correction is applied, the remaining ledger is WARN-level throughout and the episode is airworthy.

