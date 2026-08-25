# Verify Podcast Script — 2026-08-24 (pass 2, post-fix)

**Verdict:** **WARN** — zero FAIL. The blocker is repaired. Clears to the principal for TTS approval.

**Checks (counts = FLAG hits):** L1 8 / L2 2 / L3 0 / L4 0 / L5 0 / L6 0 / S1 0 / residual-and-new 1

**FAIL count: 0 (was 1). WARN count: 11 (was 12).**

All seven edits did what they were meant to do. The FAIL is fixed at the root: the Asia paragraph now states its premise before it uses it, as its own short sentence, and a listener can follow it cold. Five accuracy fixes all landed, three of them by going back to the brief and taking the more careful of the two formulations it carried. The B-L-S block survives the split intact and does not name the company twice — the one identified backfire did not occur. **No hedge, gloss, guard or causal chain was cut to pay for the fourteen words; verified by word-level diff, not taken on trust.** Four of the seven edits added epistemic protection.

One new WARN entered, minor: the pronoun in "We could not find one" reaches three sentences back for its antecedent. It is a better sentence than the overclaim it replaced.

The 713-word body is not an L5 breaker at under two percent over the band, and the accounting below shows all fourteen words went to named fixes rather than to content. **The overage bought accuracy.**

## Method and constraints

Second and final cold read. Order honoured again: the script body and the canonical exemplar were read first, the full per-sentence ledger was built and written to disk, and only then was `briefs/public/2026-08-24.md` opened for the S1 spot-check. The prior verify report was read before this file was overwritten, because it is the file being overwritten; it was read as a record of prior adjudications, not as a substitute for re-reading the script.

**Zero web searches were run. Zero live pages were opened.** Every input was a file on disk: the script, the v1 backup at `backups/2026-08-25/podcast-script-2026-08-24_v1.md`, the exemplar README, the prior verify report, and the 2026-08-24 public brief. No quote page, no news site, no fetch of any kind. Where a script number disagreed with prior expectation, the script was treated as correct per the producer's digit-check.

The header block (lines 1 to 14) is excluded from the ledger as metadata. Its "Tuesday / 25 August" references are backfill provenance, not spoken body, and are not violations — as established last pass. The spoken body was independently re-confirmed free of any 25-August information.

The seven edits were verified mechanically before being judged by ear: a word-level diff of the v1 and v2 spoken bodies returns **seven edit sites and nothing else**. Every deletion in the diff belongs to one of the seven. Nothing was removed anywhere else in the script.

## Per-sentence ledger

Every sentence of the spoken body, re-read cold, as a listener hears it: no source, no re-reading, half-attending. Forty-nine sentences (was forty-seven; the two splits added one each).

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on Monday's session." — OK

**The deposit window**
4. "The Reserve Bank of India has a window open for dollar deposits from Indians living abroad." — OK
5. "It closes on the thirty first of August, not the thirtieth of September, leaving seven days on Monday." — OK
6. "The bank moved the date forward on the fourteenth because the response was so large." — OK. "Moved forward" is ambiguous in isolation but sentence 5 has already fixed the direction.
7. "Its own release on Saturday puts total inflows under the facility at seventy two point eight five billion dollars." — **FLAG (L1, mild, residual): "the facility" is an unglossed definite noun.** The claim is now literally correct, which is what the edit was for. But the listener has been told about "a window", not "a facility", and by ear will most likely map the new word straight back onto the window — so the scope signal that works on the page works only partly in audio. Strictly better than "the money raised"; not fully closed. Non-blocking. Costless tightening: "puts total inflows under the whole scheme at…".
8. "Two things about that date, and the second one is ours." — OK
9. "The central bank's own list of frequently asked questions still shows the retired thirtieth of September, so anyone checking the central bank's website gets the wrong answer from the central bank." — OK. Cleared last pass; unchanged. Thirty-one words, single-thread, one breath at pace.
10. "And we got it wrong too." — OK. Still the best sentence in the episode, and **still immediately adjacent to 9** — nothing was inserted between them.
11. "This brief carried that retired date for several runs and never went back to check it." — **FLAG (L1: "for several runs"). STILL OPEN, KNOWN, NOT NEW.** Deliberately left in place; outside the authorised fix list. A listener does not know what a "run" is.
12. "We have dropped it." — OK. **Edit repaired.** The subject is "we", so the sentence can no longer be heard as the central bank having fixed its page. The referent of "it" now attaches to the date we carried, which is the intended meaning.

**The close**
13. "The Nifty fifty closed Monday at twenty four thousand two hundred and nineteen, down zero point one four percent." — OK
14. "Underneath it, three hundred and two shares rose and four hundred fell out of seven hundred and five, a second straight session of more fallers than risers under a flat index." — **FLAG (L1, mild). STILL OPEN, NOT NEW.** The trailing clause restates in desk vocabulary what the plain numbers just said. Thirty-one words but cleanly segmented, so not an L6 hit.

**Asia**
15. "For weeks now, money has been leaving India for artificial intelligence shares in North Asia." — OK. **The premise is now stated, plainly and first, as its own sentence.** "Artificial intelligence shares" is a concrete object where "the artificial intelligence trade" was a desk noun. "For weeks now" carries the recurring-theme scaffolding without leaking production vocabulary — the right call, and it is the one place in the episode where a desk term was replaced rather than added.
16. "On Monday that ran backwards." — OK. Five words, one idea, and "that" has an antecedent the listener heard one sentence ago. The non-idiomatic "runs backwards to" is gone; "ran backwards" alone is idiomatic.
17. "Asia sold technology, Korea hardest, and India barely moved." — OK. Now functions as evidence for 16 rather than as an orphan premise. The chain a cold listener follows is: normally money leaves India for North Asian AI shares → on Monday the reverse → here is what that looked like. **Followable on one hearing.**

*Residual note, non-blocking:* the paragraph still ends without an explicit so-what. That was one strand of the original FAIL reasoning; it is not itself FAIL-grade, and the load-bearing defect (a presupposed premise) is gone.

**Reserves and house prices**
18. "Foreign exchange reserves rose almost ten billion dollars in the week to the fourteenth, a third straight build, but a build funded by that window's dollars would stop when the window stops." — OK on the hedge. **Edit repaired:** the conditional mood restores the brief's refusal to state swap-funding as cause, and the sentence now reads as a general proposition rather than a claim about this build. Thirty-two words, comma-segmented single thread, speakable. Residual: "a build" as a noun twice is still desk vocabulary — **STILL OPEN, NOT NEW.**
19. "And the Reserve Bank's house price index, published Monday, has annual growth down to three point six percent from four point five." — OK
20. "That is below its own inflation path, so house prices are falling in real money." — **FLAG (L1, mild): ambiguous owner of "its own". STILL OPEN, NOT NEW.**

**Movers**
21. "Now the movers." — OK
22. "The biggest gain was Ratnamani Metals and Tubes, up fourteen point five five percent." — **FLAG (L2 near-miss): no what-it-does. STILL OPEN, NOT NEW.** Downgraded from FAIL because the company name states the business.
23. "A subsidiary won export orders worth about two thousand seven hundred crore rupees, filed while the market was open." — OK
24. "But the filing names the buyer only as international customers, and part of the work will be sub-contracted, not made in house." — OK

**B-L-S**
25. "The biggest fall was B-L-S International, down almost eleven percent, and here the limits matter more than the number." — OK
26. "B-L-S holds outsourced visa processing contracts from governments." — OK. Clean what-it-does, untouched.
27. "Reports say a Spanish court has widened an investigation into an alleged visa fraud network at the Spanish consulate in Algiers." — OK. Twenty-two words. Attribution front-loaded, "alleged" present, **and the company is not named in this sentence at all.**
28. "Those same reports say the court is now also looking at the company's document handling role." — OK. Sixteen words, carrying its own attribution. **The company is referred to as "the company", not named a second time** — the backfire the producer flagged did not occur.
29. "We have not read the court's order, and every account traces back to a single report, so three outlets repeating one claim is one source." — OK. Unchanged, and still the best piece of listener-legible epistemics in the script.
30. "That is enough to say the reports caused the fall." — OK
31. "It is not enough to say what the company is accused of, or whether it is accused at all." — OK. **Present, verbatim, and still the penultimate sentence of the block, immediately before the denial.**
32. "B-L-S categorically rejected the allegations in a filing made while the market was open." — OK. Still closes the block.

**The unexplained**
33. "Five of the twelve biggest movers have no cause we could establish." — OK. **Edit repaired:** the claim is now about our search. Residual, unchanged from last pass: the listener has not been told there is a list of twelve.
34. "The loudest is I-D-B-I Bank, up six point nine two percent on the day state owned banks led the market lower." — OK
35. "Nothing was filed." — OK
36. "We could not find one, and that is the accurate answer." — OK on the overclaim. **Edit repaired:** a claim about the world became a claim about our search, which is the defensible one. **FLAG (L1, mild, NEW): the antecedent of "one" is "cause" in sentence 33, three sentences back.** In context — a paragraph entirely about missing explanations — it resolves for almost any listener, and "Nothing was filed" immediately before it primes exactly the right reading. Minor, non-blocking. Costless fix if wanted: "We could not find a reason, and that is the accurate answer."

**The Hormuz correction**
37. "Here is what struck me about Monday." — OK
38. "Much of the coverage said Indian shares fell on fear about the Strait of Hormuz, the narrow lane that carries much of the world's oil, after Iran threatened to seize ships crossing it." — OK. Thirty-three words, longest in the script, single-thread with an inline gloss.
39. "We do not accept that explanation, and the oil market is the reason." — OK
40. "A real threat to that chokepoint does not send crude down, and Brent fell one point eight one percent on the same escalation." — **FLAG (L1, mild): "Brent" unglossed. STILL OPEN, NOT NEW.**
41. "Indian refiners rose on the cheaper barrel, with Indian Oil up one point nine one percent." — OK
42. "And the American sanctions announcement blamed for Monday landed after our market shut." — **FLAG (L2-flavoured): definite article on a never-introduced referent. STILL OPEN, NOT NEW.**
43. "A fall that small does not need a geopolitical cause, and we are not giving it one." — OK

**What to watch and sign-off**
44. "The date to keep is Monday the thirty first, when that deposit window shuts." — OK
45. "That's your brief." — OK
46. "Before I sign off: this has been general market commentary, not investment advice." — OK
47. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
48. "Markets are risky; you may lose money; act with care." — OK
49. "See you tomorrow." — OK

**L3 (listener-moment time): zero hits.** Unchanged and re-checked. The covered session is named "Monday" throughout and spoken in the past tense; the only forward event is pinned to an absolute date safely ahead of the recording. None of the seven edits touched a time-word — confirmed against the diff.

**L4 (mechanism not metaphor): zero hits.** The Asia edit moved the episode further from a flag, not toward one: an oblique presupposition was replaced with a stated cause-and-effect.

## The seven edits — per-edit verdict

### Edit 1 — the FAIL fix, Asia paragraph. **FIXED.**

> For weeks now, money has been leaving India for artificial intelligence shares in North Asia. On Monday that ran backwards. Asia sold technology, Korea hardest, and India barely moved.

The defect was a premise presupposed with a definite article and never established. It is now stated first, plainly, as its own short sentence — the identical repair the 20-August episode used for the identical defect in the identical slot, which is the precedent that made this a FAIL rather than a WARN. **A listener can now follow it cold**, and I tested it by reading the three sentences aloud without the surrounding script: normal state → reversal → what the reversal looked like. Three short sentences, one idea each, no nested clause anywhere.

Three secondary improvements came with it, none of them asked for. "Artificial intelligence shares" is a concrete object where "the artificial intelligence trade" was a desk noun. The non-idiomatic "runs backwards to" is gone. And "On Monday" moved from a mid-sentence adverbial into the sentence that needs it.

**On the choice of "For weeks now" over the brief's "this desk has flagged for weeks":** the right call, and it holds. It carries the recurring-theme scaffolding — this is not new, you have heard it before — without asking the listener to know what a desk is or care what it flags. The one thing it shifts is whose duration is being claimed: the brief times the *flagging*, the script times the *pattern*. Those are near-equivalent, since a pattern cannot be flagged for weeks without persisting for weeks, and the brief's own sentence only parses if the pattern was ongoing. Not a mismatch. Noted for completeness because it is the single place the script states something the brief states obliquely.

**Residual, non-blocking:** the paragraph still ends without an explicit so-what. That was one strand of the original FAIL reasoning and it survives. It is not FAIL-grade on its own and never was — the blocker was the missing premise, and the premise is now there.

### Edit 2 — "It is retired now" → "We have dropped it". **FIXED.**

The failure mode was that "it" could attach to the FAQ page and be heard as the central bank having fixed its website, which is false and the opposite of the point. The new sentence opens with "We", so the subject is unambiguously the desk from the first syllable, and the sentence cannot be heard as a statement about the central bank at all. Costless: four words for four.

### Edit 3 — "the money raised" → "total inflows under the facility". **FIXED, with a residual ear-note.**

Verified against the brief, which reads: "Its own release on Saturday 22 August puts **total inflows under the facility** at US$72.85 billion, of which US$65.4 billion is those deposits." **The script now uses the brief's own phrasing verbatim.** The over-count against a deposits-only mental model is closed as a matter of fact: the sentence no longer claims the seventy two point eight five is the deposit leg.

The residual is a listening problem rather than an accuracy one, and I am recording it as a WARN, not as a failure of the edit. The listener has been told about "a window", and "the facility" arrives as a new, unglossed, definite noun; by ear most listeners will simply map it back onto the window they were just told about, which recovers some of the over-count the edit was meant to remove. The fix is correct and is the best available at zero structural cost. If a word ever becomes free, "under the whole scheme" would close it by ear as well as on the page.

### Edit 4 — "stops" → "would stop". **FIXED.**

The brief hedges this twice and then forbids it: "We have not verified how much of the build is swap-related... so that is a question to test against the next three weekly releases **and not something to state as cause**." The brief's own sentence uses a present tense — "A reserve build funded by swapping in FCNR(B) dollars... stops when the window stops" — but its subject is an indefinite class, so the present tense is safe there. In the script the same words sat behind "a third straight build, **but**", and the contrastive collapsed the generic into the specific: *this* build was swap-funded. The conditional mood breaks that collapse and returns the sentence to a general proposition. One word, hedge restored, no contradiction with the brief.

### Edit 5 — the two overclaim narrowings. **BOTH FIXED.**

"No cause we could establish" is, again, **the brief's own line 109 verbatim** — the brief carries both formulations and the script has moved from the loose one to the tight one. "We could not find one" departs from the brief's "'Nobody knows' is the accurate answer" in the direction of a narrower claim, which is a hedge added rather than removed, and so is not an S1 mismatch. Both now claim about our search rather than about the world, which was the whole point.

**One new minor WARN arrived with the second of these**, and I am reporting it rather than smoothing it: "We could not find one" reaches back three sentences for its antecedent, "cause" in sentence 33, with "Nothing was filed" in between. "Nobody knows" needed no antecedent. In practice the paragraph is entirely about missing explanations and "Nothing was filed" primes exactly the right reading, so it resolves for almost any listener. Minor, non-blocking, and a strictly better trade than the overclaim it replaced. "We could not find a reason" would close it for one word.

### Edit 6 — the B-L-S sentence split. **FIXED, and the feared backfire did not occur.**

Covered in full in the next section.

### Edit 7 — nothing else. **CONFIRMED.**

The word-level diff of the two spoken bodies returns seven edit sites and no eighth. No time-word, no figure, no gloss and no guard outside those seven was touched.

## Does the B-L-S block still hold by ear after the split?

**Yes. Read aloud at speaking pace three times, the block holds, and it is marginally stronger than it was.**

**The company is not named twice.** This was the one identified way the fix could have backfired and it did not happen. The new second sentence says "**the company's** document handling role", not "B-L-S". Across the whole block the name is spoken exactly three times, unchanged from v1: once to identify the fall, once for the what-it-does, and once for the denial. **Neither of the two sentences describing the allegation says the company's name.** Sentence 27, which carries the sticky nouns — court, investigation, fraud, consulate — does not name the company at all.

**The order is intact.** what-it-does → hedged report → hedged report continued → epistemic limit → what we can say → what we cannot say → denial. "Or whether it is accused at all" is still the penultimate sentence, still immediately before the denial, still where recency protects it. Its ordinal moved from five-of-six to six-of-seven only because the split added a sentence; **its position relative to the denial, which is what makes it work, is unchanged.**

**The split reduced accusatory force rather than raising it.** The defect it fixed was real: in v1 the clause naming the company's role sat twenty-five words downstream of "Reports say", and at speaking pace a hedge that far back does less work than it does on the page. Now each of the two allegation sentences carries its own attribution, so a listener who catches only the second one still hears "Those same reports say" before anything about the company. That is the correct direction.

The one genuine counter-pressure, stated honestly: a standalone sentence carries more prosodic weight than a trailing clause, so the company-implicating material is now slightly more emphasised than it was. That is the trade the fix consciously made, and it is the right trade — emphasis carrying its own attribution beats de-emphasis leaning on someone else's. The material is immediately followed by "We have not read the court's order", and the block still ends where it must.

## Did the fix pass cut a hedge to buy words?

**No. Verified mechanically, not taken on trust.**

The word-level diff of the v1 and v2 spoken bodies shows deletions at exactly seven sites, each one inside a named edit. Nothing was removed from a connective sentence, a gloss, a guard, or a causal chain anywhere else in the script. The four passages flagged last pass as untouchable are byte-identical: sentence 10 ("And we got it wrong too"), the B-L-S hedge architecture including sentence 31, the entire Hormuz block, and the time convention with its absolute forward date.

Every individual deletion is replaced by equal or stronger language:

| Deleted | Replaced by | Net effect on epistemics |
|---|---|---|
| "the money raised" | "total inflows under the facility" | scope corrected, brief-verbatim |
| "It is retired now." | "We have dropped it." | referent corrected |
| the old Asia sentence | two sentences stating strictly more | premise now stated, not presupposed |
| "stops" | "would stop" | **hedge added** |
| "to look" / "own" | a full repeated attribution clause | **hedge added** |
| "anyone can point to" | "we could establish" | **claim narrowed** |
| "Nobody knows," | "We could not find one," | **claim narrowed** |

**Four of the seven edits added epistemic protection. None removed any.** This is the failure mode that caused the original FAIL and it did not recur.

### Where the fourteen words went

| Edit | Net words |
|---|---|
| FCNR scope | +2 |
| "We have dropped it" | 0 |
| Asia FAIL fix | **+2** |
| "would stop" | +1 |
| B-L-S split | **+7** |
| "we could establish" | −1 |
| "We could not find one" | +3 |
| **Total** | **+14** |

Every one of the fourteen is traceable to a named fix. **Not one went to new content, a new claim, or a flourish.** The FAIL fix — the one the overage was authorised for — cost two net words, because the writer paid for it largely by deleting the broken sentence it replaced. Half the overage went to a single edit, the B-L-S split, which is the most defensive change in the pass. Two of the seven edits were free or net-negative.

**Judgment on the overage: the words bought accuracy, not length.** Last pass I said this script was not too long but too tight in three specific places, and that three of its defects were compression artefacts. All three of those places have now been paid for, and the payment went where the compression damage was.

## Mechanical (L5) and length

**L5: zero hits. Independently machine-checked on the spoken body, not taken from the header.**

| Check | Result |
|---|---|
| Digits | none |
| Currency / percent symbols | none |
| Em-dashes / en-dashes | none |
| Brackets, parentheses, `[SAY:]` hints, exclamation marks | none |
| Word count | **713** |
| Sentence count | 49 (was 47; the two splits added one each) |
| Longest sentence | 33 words (S38), single-thread with an inline gloss — unchanged from v1 |

The header's self-report is accurate in every particular.

**713 against a 500–700 band is not an L5 audio-breaker.** The skill's FAIL condition is a body "well outside" the band; 713 is under two percent over, the producer authorised the overage in advance, and the accounting above shows every extra word bought a named accuracy fix. At 165 words per minute the overage is five seconds.

**The +14 pushed no sentence into L6 territory.** Only one edit lengthened a sentence that was already long: S18 went from 31 to 32 words with "would stop". It remains a comma-segmented single thread with no nesting, so per L6 it is not flagged — the rule is long *and* nested, never word count alone. The B-L-S split moved in the opposite direction, replacing a 30-word sentence with a 22 and a 16, which retires last pass's only L6 flag. **L6: zero hits, down from one.**

Respellings remain correct for TTS: toro I-Q, B-L-S International, I-D-B-I Bank, and the Reserve Bank of India always said in full.

## Source spot-check (S1)

**Zero mismatches. S1 passes.**

The diff makes this pass cheap and conclusive: since only seven sites changed, every other figure in the script is byte-identical to the v1 that already spot-checked clean against `briefs/public/2026-08-24.md` with zero mismatches. That table carries over by construction. Only the seven touched sites needed re-checking, and all seven were re-checked against the brief directly.

| Changed line | Brief | Match |
|---|---|---|
| "total inflows under the facility at seventy two point eight five billion dollars" | line 19: "puts total inflows under the facility at US$72.85 billion, of which US$65.4 billion is those deposits" | ✓ **script now brief-verbatim on the scope phrase** |
| "We have dropped it" | line 41: "The 30 September date is retired" | ✓ same claim, correctly attributed to us |
| "For weeks now, money has been leaving India for artificial intelligence shares in North Asia. On Monday that ran backwards." | line 29: "the pattern this desk has flagged for weeks, of money leaving India for the North Asian artificial-intelligence trade, ran backwards on Monday" | ✓ direction and duration faithful; magnitudes still correctly omitted per the brief's own refusal |
| "Asia sold technology, Korea hardest, and India barely moved" | line 29: "Korea sold off hard and India barely moved" | ✓ |
| "a build funded by that window's dollars would stop when the window stops" | line 35: generic "it stops when the window stops" + "not something to state as cause" | ✓ conditional is faithful and restores the governing hedge |
| "Those same reports say the court is now also looking at the company's document handling role" | line 79: "Reports say Spain's National Court has widened an investigation... to examine BLS's own administrative and document-processing role" | ✓ attribution made explicit rather than inherited |
| "no cause we could establish" | line 109: "Five of the twelve have no cause we could establish" | ✓ **brief-verbatim**; the script moved off the brief's looser line-146 wording onto its tighter line-109 wording |
| "We could not find one, and that is the accurate answer" | line 146: "'Nobody knows' is the accurate answer" | ✓ not a mismatch — a claim narrowed relative to source, i.e. a hedge added |

Two notes, neither a mismatch:

1. **Three of the five accuracy fixes landed on the brief's own words.** "Total inflows under the facility" and "no cause we could establish" are brief-verbatim, and "would stop" restores the brief's governing caution. The fix pass did not invent language; it went back to the source and took the more careful of the two formulations the brief carried. That is the right instinct and worth recording.
2. **"For several runs" is itself brief-verbatim** (line 41). That explains why the writer was comfortable with it and does not excuse it: "runs" is fine in a written brief a reader can re-scan and is production vocabulary in audio. W1 below stands.

## Punch list

### FAIL — none (0)

**The prior blocker F1 is repaired.** No new FAIL was introduced by any of the seven edits.

### WARN — 11. Principal may ship without any of these.

Of last pass's twelve WARNs, **five are closed** (the FCNR scope, the swap hedge, the "it is retired now" referent, both overclaims, and the B-L-S sentence). Seven carry over unchanged, three are residuals sitting inside repaired lines, and one is new and minor.

**Carried over, unchanged, not re-argued:**

**W1 [L1, S11] — "for several runs" is production vocabulary.** Deliberately left in place, outside the authorised fix list. Still stands as a listener defect; **not new, and not grounds for FAIL.** → "in brief after brief" or "for several editions".

**W2 [L1, S14] — "more fallers than risers under a flat index"** restates in desk vocabulary what the plain numbers just said.

**W3 [L1, S18] — "a build" used twice as a noun.**

**W4 [L1, S20] — "below its own inflation path" has an ambiguous owner by ear.** → "the bank's own inflation path".

**W5 [L2 near-miss, S22] — Ratnamani gets no what-it-does.** The thinnest company placement in the episode. → "the pipe maker Ratnamani Metals and Tubes" (+3).

**W6 [L1, S40] — "Brent" is unglossed.** → "Brent crude" (+1).

**W7 [L2-flavoured, S42] — "the American sanctions announcement"** arrives with a definite article and no referent.

**Residuals inside repaired lines:**

**W8 [L1, S7] — "the facility" is an unglossed definite noun.** The accuracy defect is closed; the ear defect is partly open, because a listener will map "the facility" back onto "the window". → "under the whole scheme".

**W9 [S15–17] — the Asia paragraph still ends without an explicit so-what.** The blocker was the missing premise and it is fixed; this strand survives and is not FAIL-grade.

**W10 [S33] — the listener still has not been told there is a list of twelve** before "five of the twelve" is used.

**New this pass:**

**W11 [L1, S36] — "We could not find one" reaches three sentences back for its antecedent.** Introduced by the overclaim fix, which was the right trade. Resolves in context for almost any listener. → "We could not find a reason" (+1).

### What is right, and must not be touched

Unchanged from last pass, and all four verified byte-identical in the diff:

- **Sentence 10, "And we got it wrong too."** Still adjacent to sentence 9, still the reason sentence 9 is publishable.
- **The B-L-S hedge architecture**, and sentence 31 in particular. Verified intact after the split.
- **The Hormuz block.** Exemplar-grade, untouched.
- **The day-name time convention and the absolute forward date.**

Add to that list: **the Asia paragraph as now written.** It went from the episode's only FAIL to one of its cleaner passages, and its three-short-sentences shape is the pattern to reuse the next time a premise needs establishing.
