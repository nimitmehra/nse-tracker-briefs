# Verify Podcast Script — 2026-09-07

**Verdict:** FAIL
**Checks:** L1 8 / L2 2 / L3 0 / L4 2 / L5 1 / L6 0 / S1 not run (isolation ordered)  (counts = FLAG hits)

_Cold read only. The brief (`briefs/public/2026-09-07.md`) was NOT opened — the invoking session explicitly ordered full context isolation, so Step 2's source spot-check is deferred, not passed. No web searches run._

## Mechanical results (L5)

Run on the spoken body only (everything below the `---` separator):

| Check | Result |
|---|---|
| Digits in body | 0 — clean |
| `%`, `₹`, `$` symbols | 0 — clean |
| Em-dashes / en-dashes | 0 — clean |
| `[SAY:]` hints | 0 — clean |
| Exclamation points | 0 — clean |
| Sentence count | 55 |
| Longest sentence | 32 words, single-thread (the G-R-T open-offer line) |
| Sentences >30 words | 1 |
| **Word count** | **857 — 157 over the 700 ceiling (22.4% over)** |

**L5 FLAG (1):** body word count. The script's own header declares this as a WARN and argues it is earned by the ten-day gap. The gate does not grade it that way: Step 3 makes "body well outside ~500-700" an audio-breaker. 857 is 22% past the ceiling and 71% past the floor of the exemplar band. It is a legitimate FAIL trigger on its own, though it is **not** the reason this report says FAIL — see Verdict rationale. Everything else mechanical is clean, and the respellings (toro I-Q, S-K hynix, G-R-T, S-G-S) are correctly handled.

## Per-sentence ledger

### Open

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on Monday's session." — OK (verbatim exemplar open; "read" here is the sanctioned house phrase, not jargon)

### Oil / the ten-day gap

4. "It has been ten days since I last spoke to you, and the biggest thing that changed is the price of oil." — OK. Handles the gap head-on; good.
5. "Brent crude is reported to have settled near ninety seven dollars a barrel on Monday, about nine percent above where it sat on the twenty eighth of August." — OK (28 words, single thread; the "reported to have" hedge lands cleanly)
6. "That followed the heaviest strikes on oil tankers yet in the American war with Iran, over a weekend when India was shut." — OK
7. "India buys nearly all the oil it burns and has no say in that price." — OK. Exemplar-grade: mechanism in fourteen plain words.
8. "Our own data file could not give a clean oil number, so treat the ninety seven dollars as reported, not confirmed." — **FLAG (L1: producer-view meta).** "Our own data file" exposes internal plumbing to a listener who has no idea the desk has a data file. The honesty is right; the framing is a desk note read aloud.

### The jobs number / software

9. "But oil is not what moved share prices here." — OK
10. "America's jobs number landed on Friday evening India time, after we had closed." — OK
11. "American employers added about a hundred and sixty two thousand jobs, against expectations near fifty three thousand, which pushed up the odds of an American rate rise this month." — OK (29 words, single thread, fully plain)
12. "Indian software shares fell on Monday." — OK
13. "Every news outlet linked those two, and I want to be straight with you that the link is a read, not a confirmed fact." — **FLAG (L1: desk shorthand "a read").** Noun-form "a read" meaning interpretation is exactly the register the exemplar bans. Partially rescued by the contrast with "confirmed fact", which is why it is a flag and not a breaker. Note the header claims the naive-listener pass replaced desk shorthand; this one survived it.

### The close

14. "The Nifty fifty closed at twenty three thousand seven hundred and seventy nine, down half a percent." — OK
15. "The index of Indian software shares fell two point three percent, a fourth losing session in a row, with every company in it lower." — OK. The "index of Indian software shares" workaround for "I-T" is a genuine improvement on the exemplar.
16. "Outside software the day was almost featureless, with small caps flat and the typical share falling about as much as the index." — **FLAG (L4 + internal consistency).** Two problems. (a) "the typical share falling about as much as the index" is a median-move statistic in disguise; on one hearing it is vague, and it sits oddly next to "small caps flat" in the same sentence. (b) It directly undercuts the script's own centrepiece four paragraphs later — "Four hundred and fifty three of seven hundred and ten shares fell" and "a broad decline happened with nobody large selling into it". A day where 64 percent of shares fell is not "almost featureless". A listener who is paying attention hears the contradiction; one who is not has been told to stop listening.

### The world

17. "Two things about the world India traded into." — OK
18. "America was shut on Monday." — OK
19. "It was Labor Day, so New York never opened, which means any comparison this week between Monday's Nifty and American markets sets Monday's India against Friday's America." — **FLAG (L1: producer-view meta, mild).** The second half warns the listener about an artefact in comparisons the listener was not making. It is a correction aimed at the desk and at other commentators, not a story. Two date-plus-country pairings held in one breath ("Monday's India against Friday's America") is also the densest construction in the script.
20. "Asia did trade alongside us, and went the other way, hard." — OK
21. "Korea's main index rose four point six percent, led by Samsung and S-K hynix, and Japan's Nikkei rose about two percent." — **FLAG (L2: unexplained name).** An index move is pinned on two named companies and neither is placed in the sentence. Samsung survives on global recognition; **S-K hynix is never given a what-it-does anywhere in the script.** The mechanism arrives two sentences later and is generic ("North Asia sells the equipment...") — it never attaches to the name the listener was left holding. By the letter of L2 this is a deferred name.
22. "Same jobs number, opposite directions." — OK. Best line in the script.
23. "North Asia sells the equipment artificial intelligence buildouts run on, which a hotter American economy does not hurt." — OK
24. "Indian software sells project work to American companies, whose budgets get cut first when borrowing looks dearer." — OK. Clean cause → effect → so-what.

### The movers

25. "Now the movers." — OK
26. "Ten shares rose three percent or more, only one fell hard enough to count as a big faller, and just one of them has documents behind it." — **FLAG (L1: desk shorthand, two hits in one sentence).** "has documents behind it" is desk-speak for "has a company announcement explaining it" — a listener hears "documents" and pictures paperwork. "hard enough to count as a big faller" advertises an internal threshold the listener does not have and does not care about.
27. "Not the biggest move." — **FLAG (L1: broken on one hearing — the worst line in the script).** A three-word fragment whose referent is negated and then immediately reused: the next sentence's "That was..." points back to "the biggest move", the thing this sentence just said it was not talking about. Spoken aloud it reads as an editing scar. A cold listener does not recover.
28. "That was Syrma S-G-S Technology, an electronics manufacturer, up twelve percent, with nothing on the record to explain it." — OK in isolation (company placed, plain what-it-does), but see 27 — it cannot be parsed without the broken setup.
29. "The one with documents is Tribhovandas Bhimji Zaveri, a hundred and sixty year old Mumbai jeweller, up ten percent." — **FLAG (L1: "the one with documents", second use).** Same shorthand as 26, now doing structural work as a section opener. Repetition makes it worse, not more familiar.
30. "G-R-T Jewellers has agreed to take just over seventy four percent of it from the founding family, and must now offer the other shareholders about two hundred and fifty rupees a share." — OK (32 words, longest in the script, but single-thread and speakable). "must now offer" leaves the open-offer rule unexplained, but the payoff at 32 makes it work.
31. "The share closed Monday at about five hundred and twenty nine." — OK
32. "So the market is not pricing the offer, it is pricing the business under a new owner." — OK. Exemplar-grade: it makes the 529-versus-250 gap mean something without a single piece of jargon.
33. "The one big faller was Ram Ratna Wires, which makes copper winding wire, down about six percent." — OK
34. "The founding family owns sixty nine percent of it and has not pledged any of those shares against a loan, so this was not forced selling." — **FLAG (L1: "forced selling" is a named example in the rule).** The check text lists "money moved freely / no forced selling" verbatim as the shorthand to catch. The script does better than the bare version — it supplies the pledge mechanism — but it never says what forced selling *is* (a lender selling shares the owner put up as collateral). Fix is one clause, not a rewrite.
35. "Nothing on the record explains it." — OK

### The thing that struck me

36. "Here is what struck me most about Monday, and I have no answer for it." — OK
37. "Four hundred and fifty three of seven hundred and ten shares fell." — OK, borderline. "seven hundred and ten" is the desk's tracked universe and is never named as such; a listener briefly wonders which 710. Not flagged — the ratio still lands.
38. "And the big institutions were not selling." — OK
39. "Foreign investors bought a net two hundred and eighty crore rupees, and Indian institutions bought five hundred and sixty seven crore." — OK
40. "So a broad decline happened with nobody large selling into it, and no source I could find explains why." — OK on its own; see 16 for the contradiction with "almost featureless".
41. "The tempting answer is smaller traders cutting risk while institutions sat still, but that is a guess, and I would rather say I do not know." — OK. Strongest editorial judgement in the episode.

### Things that did not move

42. "Three things also did not move when they should have." — OK
43. "IndiGo rose slightly on a day oil carried a war premium, the wrong direction for an airline's fuel bill." — **FLAG (L4: metaphor standing in for the chain; soft L2).** "oil carried a war premium" is a near-twin of the exemplar's named anti-pattern "a premium sitting under oil" — it is an image, not a mechanism, and the listener is never told that war fear pushes oil *up*. The fuel-bill link is compressed into a trailing fragment. IndiGo also gets no what-it-does (survivable in India, but it is the only mover in the script without one).
44. "The gold lenders, the companies that lend against your jewellery, fell while gold itself rose one percent." — OK. Model gloss — this is how 21 and 43 should read.
45. "And the rupee took an oil shock and a jump in the odds of an American rate rise on the same day, and finished unchanged." — OK
46. "Part of that is a soft dollar, which is a partial account and not a complete one." — **FLAG (L1: jargon plus analyst register).** "a soft dollar" is unexplained (a listener may hear the unrelated brokerage term), and "a partial account and not a complete one" is a stiff, near-tautological hedge that says nothing a plain "but that only explains part of it" would not say better.

### What to watch / close

47. "What to watch." — OK
48. "The American rate decision lands on the fifteenth and sixteenth of September." — OK
49. "The odds of a rise sit between about fifty two and sixty five percent depending on the venue, which is why I give you a range and not one number." — **FLAG (L1: "the venue" is opaque desk jargon).** No lay listener knows that different futures and prediction markets price the same odds differently; "venue" is the trading-desk word for it. The trailing clause is also meta — explaining the presenter's own formatting choice rather than the market.
50. "Before that, India's August inflation figure arrives mid month, the first that can carry oil going from eighty nine dollars to ninety seven." — **FLAG (L4 + logic — needs a human eye).** Two issues. (a) "the first that can carry oil going from eighty nine dollars to ninety seven" is compressed to the point of ungrammatical-sounding; "carry" is doing work no listener will follow on one hearing. (b) More seriously: an **August** inflation reading measures prices during August. The script has already told the listener oil was at eighty nine dollars on the twenty eighth of August and reached ninety seven over the September weekend. An August print cannot capture a September price move. Either the number belongs to a later print or the framing needs to say "the first reading that begins to pick up the oil move" — as written the claim appears to contradict the script's own timeline. Flagged from internal evidence only; the brief was not consulted.
51. "That's your brief." — OK
52. "Before I sign off: this has been general market commentary, not investment advice." — OK
53. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
54. "Markets are risky; you may lose money; act with care." — OK
55. "See you tomorrow." — OK as mandated verbatim. Observation, not a flag: an episode that opens "It has been ten days since I last spoke to you" and closes "See you tomorrow" is a promise the last ten days did not keep. Principal's call.

### L3 (time discipline) — clean

No L3 hits. The covered session is consistently "Monday" and is never called "yesterday"; every forward event (the fifteenth and sixteenth of September, mid-month inflation) is framed as future; the Friday jobs print and the Labor Day closure are correctly placed behind Monday. The day-name variant is used consistently and no morning-model phrasing survives. The one-day recording lag is handled without a single "today".

## Punch list

**Blockers — fix before TTS (these drive the FAIL):**

- **[L1, sentence 27] "Not the biggest move."** Delete the fragment and fold it into the next sentence. Suggested: *"The biggest move had nothing behind it. Syrma S-G-S Technology, an electronics manufacturer, rose twelve percent, and there is no company announcement on the record to explain it."*
- **[L1, sentences 26 and 29] "documents behind it" / "The one with documents".** Replace both with plain English. Suggested for 26: *"Ten shares rose three percent or more, only one fell sharply, and just one of those moves has an official company announcement to explain it."* For 29: *"The move with an announcement behind it was Tribhovandas Bhimji Zaveri, a hundred and sixty year old Mumbai jeweller, up ten percent."*
- **[L2, sentence 21] S-K hynix is never placed.** Add the what-it-does in the same breath. Suggested: *"...led by Samsung and S-K hynix, the two companies that make most of the memory chips artificial intelligence servers run on, and Japan's Nikkei rose about two percent."* This also lets sentence 23 shorten.
- **[L1, sentence 49] "depending on the venue".** Suggested: *"The odds of a rise sit between about fifty two and sixty five percent depending on which market you look at, so I will give you the range rather than pretend there is one number."*
- **[L4 + logic, sentence 50] the August inflation / September oil timeline.** Verify against the brief before recording. If the August print genuinely cannot include the September oil move, rewrite. Suggested if it can only partly capture it: *"Before that, India's August inflation figure arrives mid month. It is the first reading that starts to pick up oil moving from eighty nine dollars to ninety seven."*

**Should fix — cheap, and each removes a stumble:**

- **[L1, sentence 8] "Our own data file".** Suggested: *"I could not confirm that price from a second source, so treat the ninety seven dollars as reported, not confirmed."* Keeps the hedge, drops the plumbing.
- **[L1, sentence 13] "the link is a read".** Suggested: *"...and I want to be straight with you that the link is an interpretation, not a confirmed fact."*
- **[L4 + consistency, sentence 16] "almost featureless".** It contradicts the episode's own centrepiece. Suggested: *"Outside software there was no single story, but the weakness was wide, and I will come back to that."* This also sets up sentence 37 instead of undercutting it.
- **[L1, sentence 34] "forced selling".** Define it in the clause where it appears. Suggested: *"...and has not pledged any of those shares against a loan, so no lender was dumping stock to cover a debt."*
- **[L4, sentence 43] "oil carried a war premium".** State the mechanism. Suggested: *"IndiGo, the airline, rose slightly on a day when the fear of a wider war pushed oil prices up. Fuel is an airline's largest cost, so that is the wrong direction."*
- **[L1, sentence 46] "a soft dollar ... a partial account and not a complete one".** Suggested: *"Some of that is the dollar being weak everywhere, but that only explains part of it."*
- **[L1, sentence 19] the Labor Day comparison caveat.** Trim the producer-view half. Suggested: *"It was Labor Day, so New York never opened. India traded on Monday with America still shut."*

**Length (declared WARN, assessed here):** 857 words. Roughly 90 of those come back for free from the punch list above (the fragment at 27, the meta half of 19, the double "documents" construction, the "partial account" tautology). That lands near 770 — still over, but defensibly so for a ten-day-gap episode. The header's argument that clarity was worth thirty-one words is sound in principle; the problem is that the words bought clarity in some places and desk shorthand survived in others. **The length is not earned as it stands, because the overage is not all carrying signal — some of it is the unclear phrasing this report is flagging.** Fix the L1 hits first, then re-count.

## Source spot-check (S1)

**NOT RUN — deferred, not passed.**

The invoking session ordered strict context isolation and explicitly forbade opening `briefs/public/2026-09-07.md` or any other file under `briefs/public/*.md`, and forbade web searches. Step 2 of this skill requires the brief. That step therefore did not execute.

**Consequence the principal must hold:** no figure in this script has been checked against source by this pass. The 2026-06-04 failure class this check exists to catch — a wrong-day number leaking onto the script — remains **unchecked** for this episode. Every one of the following is unverified here: the Nifty close of twenty three thousand seven hundred and seventy nine and the half-percent fall; the software index down two point three percent and the fourth losing session; Brent near ninety seven dollars and the nine percent rise from the twenty eighth of August; the American payrolls figure of a hundred and sixty two thousand against fifty three thousand expected; Korea up four point six percent and the Nikkei up about two percent; Syrma up twelve percent; Tribhovandas Bhimji Zaveri up ten percent, the seventy four percent stake, the two hundred and fifty rupee offer and the five hundred and twenty nine close; Ram Ratna Wires down six percent and the sixty nine percent unpledged family holding; four hundred and fifty three of seven hundred and ten; the two hundred and eighty crore FII and five hundred and sixty seven crore DII nets; gold up one percent; the fifty two to sixty five percent rate-rise odds; the fifteenth and sixteenth of September.

**Internal-consistency cross-checks that WERE possible cold, and their results:**
- Oil at eighty nine dollars on 28 August rising to ninety seven is about nine percent — the script's two statements of the oil move agree with each other. Consistent.
- "almost featureless" (16) versus "four hundred and fifty three of seven hundred and ten shares fell" / "a broad decline" (37, 40) — **inconsistent within the script.** Flagged.
- An **August** inflation print described as "the first that can carry oil going from eighty nine dollars to ninety seven", when the script itself dates ninety seven dollars to the September weekend — **apparently inconsistent within the script.** Flagged; needs the brief to resolve.

Someone with brief access must run S1 before TTS. This report does not substitute for it.

## Verdict rationale

**FAIL.**

Not for the declared word count, and not for anything mechanical — the TTS hygiene is genuinely clean (zero digits, zero symbols, zero em-dashes, respellings correct) and no sentence fails the listenability test on length or nesting.

It fails on **L1 density**. Eight separate lines put desk register in a listener's ear, and three of them are load-bearing structure rather than incidental word choice: the movers section is opened by a broken fragment ("Not the biggest move."), organised around an opaque metaphor used twice ("documents behind it" / "the one with documents"), and closed with a phrase the rule names verbatim as a thing to catch ("forced selling"). The forward-look section signs off on "depending on the venue". That is not one slip; it is a register the compression passes did not reach.

It also carries **one clean L2**: S-K hynix is named as the cause of a four point six percent index move and is never told to the listener what it is. That is a standalone FAIL condition in this skill and requires no judgement call.

The script's real strengths are worth stating, because the fixes are small and the episode is close: the epistemic honesty is the best this desk has produced ("I would rather say I do not know", the reported-not-confirmed oil hedge, the range-not-a-number instinct), "Same jobs number, opposite directions" and the two-fifty-versus-five-twenty-nine payoff are exemplar-grade, and dodging "I-T" in favour of "the index of Indian software shares" improves on the exemplar. This is a FAIL that a single editing pass clears — roughly twelve line edits, most of them one clause each, which also recovers most of the word overage.

**Do not run `tts-podcast-nse.py` until the blockers are cleared and S1 has been run by a session with brief access.**

