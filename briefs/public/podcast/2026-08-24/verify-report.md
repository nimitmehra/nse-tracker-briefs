# Verify Podcast Script — 2026-08-24 (pass 2, post-fix)

**Verdict:** PENDING

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

## Did the fix pass cut a hedge to buy words?

## Mechanical (L5) and length

## Source spot-check (S1)

## Punch list
