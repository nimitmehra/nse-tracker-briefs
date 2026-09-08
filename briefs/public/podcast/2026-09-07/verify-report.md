# Verify Podcast Script — 2026-09-07

**VERDICT: FAIL**

**Checks:** L1 0 / L2 0 / L3 0 / L4 3 / L5 1 / L6 0 / S1 1  (counts = FLAG hits)

**Blockers: 2** (S1 inflation inversion; L5 word count)
**Should-fix: 4**
**Sentences ledgered: 57 of 57**

**FAIL drivers:** (1) **S1** — the script asserts the opposite of the brief on the August inflation print, and contradicts its own second paragraph doing it. (2) **L5** — 877-word body against the 500-700 band.

**Clean on every automatic-FAIL check except those two:** L1 naive-listener 0 hits, L2 name-on-mention 0 hits, L3 listener-moment time 0 hits. TTS mechanics machine-verified clean (0 digits, 0 percent/rupee/dollar symbols, 0 em- or en-dashes, 0 `[SAY:]` hints). HEG absent. Sector scope held to Nifty IT alone.

> **Independence note.** This is a fresh cold read of the CURRENT `script.md`, run in a separate context. The prior `verify-report.md` (which described a pre-fix 857-word draft and returned FAIL) was NOT read before this ledger was built, and none of its findings were inherited. The brief (`briefs/public/2026-09-07.md`) was opened only AFTER the ledger below was complete, for the Step 2 source spot-check.

---

## Blockers (FAIL)

### B1 — The August inflation line is impossible, and the script contradicts itself saying it (sentence 52)

> "Before that, India's August inflation figure arrives mid month. It is the first reading that starts to pick up oil moving from eighty nine dollars to ninety seven."

The oil move is a **September** event. The script itself establishes this, in sentence 5:

> "Brent crude is reported to have settled near ninety seven dollars a barrel on Monday, about nine percent above where it sat on the **twenty eighth of August**."

Eighty-nine dollars is where crude sat on Friday 28 August. The move to ninety-seven happened over the weekend of 5–6 September and printed on Monday 7 September. An August inflation reading measures August prices. It therefore contains **none** of this move — not "starts to pick up", not partially, not at the margin. The first Indian inflation print that can carry it is the September print, released in mid-October.

This was caught cold, from the script alone, before the brief was opened: the episode states the move is post-28-August in its second paragraph and then tells the listener an August reading picks it up. That is a self-contradiction inside one five-minute episode, and it is audible — the two numbers, eighty nine and ninety seven, are repeated verbatim in both places, so the listener is holding exactly the figures needed to notice.

I record that the author knowingly softened the source brief's stronger wording ("the first print that can carry crude from 89 to 97") to "the first reading that starts to pick up". **That softening does not fix it.** It converts a plainly false claim into a vaguer false claim. The error is not one of degree.

Suggested rewrite (keeps the beat, costs two words):

> "Before that, India's August inflation figure arrives mid month. It lands before any of this oil move can show up in it, so it tells us where inflation was, not where the oil price is about to push it."

Or, if the beat must shrink, cut it entirely — it is the one forward-looking item in the episode that carries no usable information for the listener.

### B2 — Word count is 877, a full minute past the band (L5)

The skill's L5 makes a body "well outside ~500-700" a FAIL, and Step 3 repeats it. 877 words is 177 over the ceiling — twenty-five percent over — and 5.32 minutes against a 4.5-minute band.

I judged this against the band myself rather than taking the author's declaration. My read: the overage is real but it is the **least serious** thing in this report, and unlike B1 it is a matter the principal can simply overrule. The episode does not *feel* padded. Every gloss that was added back (placing S-K hynix, defining forced selling, the airline fuel mechanism) bought genuine listener comprehension, and I would not trade any of them for eighty seconds.

If it must come down, I agree with the author's two candidates and would order them:
- **Cut the Syrma beat first** (sentences 28–29, about 30 words). It is a name with no cause, and sentence 27 already tells the listener that only one of the ten movers has an explanation. Cutting Syrma costs nothing except the "biggest move is the unexplained one" flourish.
- **Cut the IndiGo non-move second** (sentences 43–44, about 36 words). This one costs more than the author allows: IndiGo is the cleanest worked mechanism in the non-moves block, and it is what teaches the listener how to read the other two. If both go, the "three things did not move" promise in sentence 42 must be re-cut to two.

Cutting both plus B1's beat lands around 790, still over. Getting to 700 means giving up either the breadth puzzle or the world section, and I would not recommend either. **My recommendation: fix B1, take the Syrma cut, and let the principal accept roughly 820 words as the declared cost of a ten-day gap.**

## Per-sentence ledger

57 sentences in the spoken body (everything below the `---` separator). Every one is quoted and judged.

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK (respelling reads correctly aloud)
3. "Your read on Monday's session." — OK. Day-name variant, not the morning-model "yesterday". No L3 hit: the covered session is named, and no future event is spoken of as past.

**The oil leg**
4. "It has been ten days since I last spoke to you, and the biggest thing that changed is the price of oil." — OK
5. "Brent crude is reported to have settled near ninety seven dollars a barrel on Monday, about nine percent above where it sat on the twenty eighth of August." — OK. 28 words, single thread, one breath. "Brent crude" is placed by the previous sentence ("the price of oil"). Arithmetic self-checks: eighty nine to ninety seven is 8.99 percent.
6. "That followed the heaviest strikes on oil tankers yet in the American war with Iran, over a weekend when India was shut." — OK
7. "India buys nearly all the oil it burns and has no say in that price." — OK. Plain mechanism, no jargon.
8. "And the ninety seven dollars comes from press reports rather than data I could confirm myself, so treat it as reported, not confirmed." — OK. This is the reported-versus-confirmed distinction done audibly and without sounding lawyerly. It is the best line in the episode on that axis, and it sets a standard the script later fails to hold (see sentence 39).

**The rates leg**
9. "But oil is not what moved share prices here." — OK. Good pivot; tells the listener the hook is not the cause.
10. "America's jobs number landed on Friday evening India time, after we had closed." — OK
11. "American employers added about a hundred and sixty two thousand jobs, against expectations near fifty three thousand, which pushed up the odds of an American rate rise this month." — **FLAG (L4, minor):** the step from "jobs beat" to "rate rise odds up" is asserted, never explained. A naive listener is asked to accept that a hot labour market makes a central bank raise rates. Every other chain in this episode is spelled out; this one is not. 29 words, single thread, still speakable.
12. "Indian software shares fell on Monday." — OK
13. "Every news outlet linked those two, and I want to be straight with you that the link is an interpretation, not a confirmed fact." — OK. Reported-versus-confirmed handled in the listener's own vocabulary.

**The close**
14. "The Nifty fifty closed at twenty three thousand seven hundred and seventy nine, down half a percent." — OK
15. "The index of Indian software shares fell two point three percent, a fourth losing session in a row, and every company in it was lower." — OK. Avoiding the initialism "I-T" in favour of "the index of Indian software shares" is a genuine improvement on the exemplar's habit of naming indices raw.
16. "Outside software there was no single story, but the weakness was wide, and I will come back to that." — OK. Correctly forward-loads the breadth centrepiece.

**The world**
17. "America was shut on Monday." — OK
18. "It was Labor Day, so New York never opened." — OK
19. "If you see Monday's Nifty compared with American markets this week, that is Monday's India against Friday's America." — OK. The prior verifier reportedly wanted this cut as producer-view meta; I disagree and side with the author. Re-aimed at the listener ("if you see"), it is a service, not desk chatter.
20. "Asia did trade alongside us, and went the other way, hard." — OK
21. "Korea's main index rose four point six percent, led by Samsung and S-K hynix, the two Korean chipmakers that supply artificial intelligence servers." — OK. **L2 satisfied.** The entity named as the cause of the move is placed in the same breath. "Korea's main index" instead of "KOSPI" is the right call.
22. "Japan's Nikkei rose about two percent." — OK. "Nikkei" is placed by parallelism with the preceding sentence; a listener carries "Korea's index / Japan's Nikkei" without effort.
23. "Same jobs number, opposite directions." — OK. A fragment, but a deliberate rhetorical one that lands cleanly in speech.
24. "A hotter American economy does not hurt demand for those chips." — OK
25. "But Indian software sells project work to American companies, whose budgets get cut first when borrowing looks dearer." — OK. Full cause to effect to so-what in 18 words. Best-constructed sentence in the episode.

**The movers**
26. "Now the movers." — OK
27. "Ten shares rose three percent or more, only one fell sharply, and just one of those moves has an official company announcement to explain it." — **FLAG (L4 / listener-trip):** "only one fell sharply" is stated with no universe attached. Two paragraphs later the listener hears "four hundred and fifty three of seven hundred and ten shares fell." Those are reconcilable (sharply versus at all, screened set versus all closes) but not on one hearing, and a listener who notices will conclude the host contradicted himself. Fix is one clause, not a rewrite.
28. "The biggest move is not that one." — OK. Reads as a complete sentence aloud; the prior draft's broken fragment is gone.
29. "Syrma S-G-S Technology, an electronics manufacturer, rose twelve percent with nothing on the record to explain why." — OK. Named, placed, and the absence of a cause is stated rather than papered over.
30. "The one with an announcement was Tribhovandas Bhimji Zaveri, a hundred and sixty year old Mumbai jeweller, up ten percent." — OK. Long name, but placed and speakable.
31. "G-R-T Jewellers has agreed to take just over seventy four percent of it from the founding family, and must now offer the other shareholders about two hundred and fifty rupees a share." — OK. 31 words but strictly single-thread and comma-segmented; per L6 this is not a flag on length alone. The open-offer rule is conveyed without the term "open offer", which is the right instinct.
32. "The share closed Monday at about five hundred and twenty nine." — OK
33. "So the market is not pricing the offer, it is pricing the business under a new owner." — OK. Correct inference, plainly drawn. (A listener may privately wonder why an acquirer offers half the market price; the script does not owe that, and answering it would cost words this episode does not have.)
34. "The one that fell sharply was Ram Ratna Wires, which makes copper winding wire, down about six percent." — OK. Placed.
35. "The founding family owns sixty nine percent of it and has not pledged any of those shares against a loan, so no lender was selling stock to cover a debt." — OK. "Forced selling" is defined inside the clause instead of used as jargon. This is the fix working.
36. "Nothing on the record explains it." — OK

**The breadth puzzle**
37. "Here is what struck me most about Monday, and I have no answer for it." — OK
38. "Four hundred and fifty three of seven hundred and ten shares fell, and neither the foreign investors nor the big Indian institutions were selling." — OK
39. "Foreign investors bought a net two hundred and eighty crore rupees, and Indian institutions about five hundred and sixty seven crore." — OK on listenability. **Flagged for the punch list on source discipline, not for the ledger:** these two numbers are stated as flat fact while the Brent number three minutes earlier got an explicit "reported, not confirmed". If these are also reported-only, the episode applies its own honesty rule unevenly on the very figure its centrepiece rests on. Checked in S1 below.
40. "So a broad decline happened with nobody large selling into it, and no source explains why." — OK. Direction check passes: both flows are net buys, so "neither were selling" is correct.
41. "The tempting answer is smaller traders cutting risk while institutions sat still, but that is a guess, and I would rather say I do not know." — OK. Strongest editorial moment in the episode.

**The non-moves**
42. "Three things also did not move when they should have." — OK. Three are promised and exactly three are delivered.
43. "IndiGo, the airline, rose slightly on a day when fear of a wider war pushed oil prices up." — OK. Placed.
44. "Fuel is one of an airline's biggest costs, so that is the wrong direction." — OK. Mechanism stated.
45. "The gold lenders, the companies that lend against your jewellery, fell while gold itself rose one percent." — **FLAG (L4):** the "should have" is never stated. IndiGo gets its mechanism in the very next sentence; the rupee gets one too. This item gets none, so a naive listener is told a fact and left to supply the reason himself — that rising gold makes the jewellery backing those loans more valuable. This is the clearest missing causal chain in the script.
46. "And the rupee took an oil shock and a jump in the odds of an American rate rise on the same day, and finished unchanged." — OK. The oil-to-rupee link rests on sentence 7 ("India buys nearly all the oil it burns"), which is close enough to carry.
47. "Some of that is the dollar being weak everywhere, but that only explains part of it." — OK. Admits the residual instead of over-explaining.

**What to watch**
48. "What to watch." — OK
49. "The American rate decision lands on the fifteenth and sixteenth of September." — OK. L3 clean: a future event framed as future.
50. "The odds of a rise sit between about fifty two and sixty five percent depending on which market you look at, so I will give you the range and not one number." — OK. 31 words, single thread, one breath with a natural comma pause. Refusing a false point estimate out loud is good practice.
51. "Before that, India's August inflation figure arrives mid month." — OK in isolation.
52. "It is the first reading that starts to pick up oil moving from eighty nine dollars to ninety seven." — **FLAG (BLOCKER — factual impossibility AND self-contradiction).** See Blockers section. The script's own sentence 5 dates the oil move to after the twenty eighth of August; an August inflation reading cannot contain a September price move, partially or otherwise.

**Sign-off**
53. "That's your brief." — OK
54. "Before I sign off: this has been general market commentary, not investment advice." — OK
55. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK (mandated disclaimer, verbatim)
56. "Markets are risky; you may lose money; act with care." — OK (mandated)
57. "See you tomorrow." — OK against the skill, which mandates this verbatim. Raised for the principal below, not scored as a flag: a verifier cannot penalise compliance with a mandate.

## Punch list

**Blockers — must be fixed and re-verified before TTS (2)**

- **[B1 / S1] Sentence 52 — the August inflation line.** The script asserts what the brief twice denies in bold. Rewrite to the brief's own position: *"Before that, India's August inflation figure arrives mid month. It measures August prices, so none of this oil move is in it. The first reading that can carry it is September's, out in mid-October."* That is 34 words against the current 24 — ten words to convert a false statement into the episode's sharpest forward-looking beat, because it tells the listener the big story is deliberately invisible for another five weeks. Worth every word.
- **[B2 / L5] Body is 877 words against a 500-700 band.** See Blockers above for the recommended cut order (Syrma first, IndiGo only if forced). Mechanically the script is otherwise spotless: machine-checked at zero digits, zero percent or rupee or dollar symbols, zero em-dashes or en-dashes, zero `[SAY:]` hints, zero exclamation marks. Word count is the single L5 breach.

**Should fix — high value, cheap (4)**

- **[S1 discipline] Sentence 39 — label the flow figures as reported.** The brief marks them explicitly: "provisional cash-segment figures, **reported** from two flow aggregators that agree to the decimal, because the depository's and the exchange's own pages both failed when we tried them." The brief's own methodology rule (line 159) is "anything reported rather than confirmed carries that word in the same sentence as the claim." The script honours that rule for Brent and drops it here — on the two numbers the entire centrepiece rests on. If the flows are unconfirmed, then "nobody large was selling" is an unconfirmed claim, and the episode's most striking moment is standing on unlabelled ground. Four words fix it: *"Foreign investors are reported to have bought a net two hundred and eighty crore rupees..."*
- **[L4] Sentence 45 — restore the gold-lender mechanism.** The brief supplies it in one clause (line 139): "Their loan books are secured against gold, so a higher gold price normally raises what they can lend against." The script cut exactly that sentence, leaving the only non-move in the block with no stated reason it is a non-move. Add: *"...fell while gold itself rose one percent. Their loans are backed by that gold, so a higher gold price should have helped them."*
- **[L4 / listener-trip] Sentence 27 — attach the universe to "only one fell sharply."** Currently it reads as a claim about the whole market and collides with "453 of 710 fell" two paragraphs later. The brief is explicit that this is a screen of twelve candidates. Fix: *"Ten shares rose three percent or more, and only one big faller, and just one of those moves has an official company announcement to explain it."*
- **[S1 framing] Sentences 30-31 — TBZ's move is continuation, not news.** The brief says so twice in bold: "The deal is dated 31 August, not Monday, and Monday's rise is continuation, not news," and the stock is up 74.20% in a week. The script presents the deal as the explanation for Monday's ten percent with no date attached, so a listener hears "deal announced, stock up ten percent today." Six words fix it: *"...up ten percent, on a fifth session of climbing since the deal was filed on the thirty first of August."* Strictly this is an omitted qualifier rather than an inverted claim, which is why it sits here and not in Blockers — but a strict reading would promote it.

**Observations — no action required**

- **India VIX is absent from the episode.** The brief calls it "the largest proportional move in the day's headline set" (11.16, +4.49%) and reads it as the market charging almost nothing to insure against a coin-flip rate decision a week out. The exemplar always gives the fear gauge a line. Cutting it is a defensible call at 877 words, and I would not add it back before B2 is resolved — but it is the most interesting thing the episode chose not to say.
- **The "which market you look at" phrasing** (sentence 50) is a genuine improvement on the brief's "depending on which venue you read." Venue is desk vocabulary; market is not.
- **Sentence 19, the Labor Day comparison caveat, should stay.** The prior verifier wanted it trimmed as producer-view meta and the author declined. I side with the author. Re-aimed as "if you see Monday's Nifty compared with American markets this week," it is a direct service to a listener who will encounter exactly that comparison. It is not meta; it is a warning about what he is about to read elsewhere.
- **No L1, L2 or L3 hits anywhere in the episode.** Every named entity is placed on first mention in the same breath, including S-K hynix and Samsung, which the prior draft reportedly failed. Every company gets a plain what-it-does: Syrma "an electronics manufacturer", TBZ "a hundred and sixty year old Mumbai jeweller", Ram Ratna "which makes copper winding wire", IndiGo "the airline", gold lenders "the companies that lend against your jewellery". Time-words are consistent throughout — day names, no "today", future events framed as future. On the three checks that carry an automatic FAIL, this script is clean.

## Source spot-check (S1)

Run against `briefs/public/2026-09-07.md` only after the ledger above was finished.

### S1 MISMATCH — the script says the opposite of its own brief on the inflation print

This is the finding that converts B1 from "a factual impossibility the script inherited" into an outright source contradiction. **The brief is already correct.** Line 151:

> "**This print cannot carry crude going from US$89 to US$97 — an August number measures August prices, and that leg came in September**; the first print that can carry it is September's, released in mid-October."

And line 137 again, independently:

> "**Oil will show up in the September inflation print released in mid-October, not in Monday's chart**"

The script says:

> "It is the first reading that starts to pick up oil moving from eighty nine dollars to ninety seven."

The brief states in bold that the August print **cannot** carry this move and names the September print as the first that can. The script tells the listener the August print **is** the first reading that picks it up. That is a direct inversion of a source claim the brief makes twice, in bold, both times. The script's own metadata describes "softening" the brief's wording — but the brief's current wording is not the claim being softened; it is the correction. The script is not a softened version of its source, it is the negation of it.

**S1 count: 1 mismatch. This alone is a FAIL under Step 2.**

### Everything else traced clean

| Claim in script | Brief | Verdict |
|---|---|---|
| Nifty fifty at 23,779, down half a percent | 23,779.15, −0.50% | OK |
| Software index down two point three percent | Nifty IT −2.28% | OK |
| "a fourth losing session in a row" | "a fourth consecutive down session" | OK |
| "every company in it was lower" | "every constituent we can price in the red" | OK (drops "we can price"; immaterial aloud) |
| Brent near ninety seven, about nine percent above 28 August, **reported** | identical, and labelled reported | OK — hedge correctly carried |
| Heaviest tanker strikes yet, over a weekend India was shut | line 36 | OK |
| Payrolls about 162,000 vs expectations near 53,000 | 162,000 vs consensus near 53,000 | OK |
| Link jobs → Indian software is "an interpretation, not a confirmed fact" | "reported rather than confirmed — the read every carrier ran" | OK |
| Korea's index +4.6%, Samsung and S-K hynix, Japan about 2% | KOSPI +4.61% at 6,995.39, Samsung +5.68%, SK hynix +8.26%, Nikkei +2.07% | OK |
| "the two Korean chipmakers that supply artificial intelligence servers" | "North Asia sells the physical equipment for AI buildouts" | OK — no market-share claim invented |
| Ten shares up three percent or more, one genuine faller, one with documents | "ten stocks up 3% or more and exactly one genuine faller"; one of eleven sourced to primary documents | OK on the numbers (universe issue is a listenability flag, not S1) |
| Syrma, electronics manufacturer, up twelve percent, nothing on the record | SYRMA +12.18%, cause not established, EMS cohort explanation ruled out | OK |
| TBZ, 160-year-old Mumbai jeweller, up ten percent | TBZ +9.99% | OK |
| GRT taking just over seventy four percent; offer about 250 rupees; close about 529 | 74.12%; ₹249.61; ₹528.90 | OK |
| "the market is not pricing the offer, it is pricing the business under a new owner" | near-verbatim from line 72 | OK |
| Ram Ratna Wires, copper winding wire, down about six percent | RAMRAT −5.97% | OK |
| Promoters sixty nine percent, zero pledged, no forced selling | 69.30%, zero pledged, checklist empty | OK |
| 453 of 710 fell | 453 of 710, 254 rose, 3 unchanged | OK |
| FII +280 crore, DII about 567 crore, neither selling | +₹280.1 cr, +₹566.8 cr, both net buyers | OK on figures — see punch list on the missing "reported" label |
| IndiGo rose slightly; fuel "one of an airline's biggest costs" | INDIGO +0.48%; "fuel-cost arithmetic" | OK — superlative correctly avoided |
| Gold lenders fell while gold rose one percent | Muthoot −1.16%, Manappuram −4.15%, gold +1.06% | OK on facts — mechanism dropped, see punch list |
| Rupee finished unchanged; dollar weak explains only part | USDINR 94.485, −0.01%; dollar index −0.23%; "a partial account, not a complete one" | OK |
| Fed on fifteenth and sixteenth; odds fifty two to sixty five percent | 52%–65%, 15–16 September | OK |
| Labor Day, New York shut, Monday's India vs Friday's America | line 24 | OK |

**Scope compliance:** the script names exactly one sector index — "the index of Indian software shares." Nifty Pharma was cut. No other sector move is asserted anywhere. Matches the brief's own standing restriction (line 127: "no other sector move appears anywhere in this brief"). **PASS.**

**HEG:** does not appear in the script in any form. The brief excludes it from the movers count as a demerger record-date price reset (lines 77, 83, 109). The script's "only one fell sharply" is therefore consistent with the brief's own eleven-name table, not a silent inclusion. **PASS — the trap was avoided.**

**One place the script improves on the brief:** the brief calls the day "almost featureless" outside IT (line 54) four paragraphs before reporting that 453 of 710 stocks fell (line 58). That tension is in the source. The script's "Outside software there was no single story, but the weakness was wide, and I will come back to that" resolves it and sets up the centrepiece. That is a real editorial gain, and it should be noted rather than buried.

## For the principal

**Three lines before you approve the TTS spend:**

1. **The script tells the listener the opposite of what your brief says, on the inflation print.** The brief states twice, in bold, that an August number cannot carry the crude move from eighty-nine to ninety-seven and that the September print in mid-October is the first that can. The script says the August reading "starts to pick up" that move. It is impossible on its face, it contradicts the script's own second paragraph, and the two numbers appear verbatim in both places, so an attentive listener is holding exactly what he needs to catch it. **One sentence, ten words to fix.**
2. **Everything else in this episode is in good shape, and better than the length debate suggests.** No unplaced entities, no desk-register, no time-word errors, mechanically spotless for TTS, every figure traced to the brief, HEG correctly kept out, sector scope correctly held to software alone. The 877 words are 177 over the band and that is a real breach of the skill — but the overage bought comprehension, not padding, and it is the one thing here you can simply overrule. **The inflation line is not.**
3. **Two cheap honesty fixes I would take before recording.** The foreign and domestic flow numbers are labelled "reported" in your brief and stated as flat fact in the script — on the two figures the episode's centrepiece rests on. And the gold lenders are the only non-move in the block with no reason attached; the brief hands you the missing clause ready-made. Together they cost about fifteen words and they hold the reported-versus-confirmed discipline that is otherwise the best thing in this episode.

**On the sign-off you flagged.** "See you tomorrow" after "it has been ten days since I last spoke to you" does ring slightly hollow, but the skill mandates that closing verbatim and a verifier cannot penalise compliance with a mandate. If it bothers you, the cheaper repair is at the top, not the bottom: the opening does not need to say ten days out loud. "The biggest thing that changed since I last spoke to you is the price of oil" carries the same information without starting a clock the sign-off then has to answer for. Your call, not a flag.

**On self-verification.** The prior report in this folder was produced inside the author's own context and is not an independent check. Its verdict was not inherited here. Where I can see its findings through the author's metadata, I agree with most of them, and I explicitly disagree with one: it wanted the Labor Day caveat cut, and the author was right to keep it. Note that neither the author's self-verify nor the prior report caught the inflation inversion — the self-verify pass actually recorded it as *fixed*. That is precisely the failure mode an independent read exists to catch, and it is the argument for keeping this gate outside the writer's context.

---

*Cold read completed before the brief was opened. Ledger built from `script.md` and `canonical_voice_example/README.md` only. Source spot-check run last, against `briefs/public/2026-09-07.md`.*
