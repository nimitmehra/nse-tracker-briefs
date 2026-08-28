# Verify Podcast Script — 2026-08-27 (ATTEMPT 2 / cold read of v2)

**Verdict:** _pending_
**Checks:** L1 _ / L2 _ / L3 _ / L4 _ / L5 _ / L6 _ / S1 _   (counts = FLAG hits)
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

