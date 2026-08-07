# Verify Podcast Script — 2026-08-07

**Verdict:** _pending_
**Checks:** _pending_

## Mechanical checks (independently re-run)

Re-measured on the spoken body only (everything below the `---` separator, lines 59-81). I did not take the script header's self-report on trust; every figure below is my own count.

| Claim in header | My measurement | Status |
|---|---|---|
| 696 words | 696 | CONFIRMED |
| ~4.22 min at 165 WPM | 4.22 | CONFIRMED |
| Zero digits | 0 | CONFIRMED |
| Zero currency / percent symbols | 0 | CONFIRMED |
| Zero em-dashes or en-dashes | 0 | CONFIRMED |
| Zero `[SAY:]` hints | 0 | CONFIRMED |
| Zero exclamation points | 0 | CONFIRMED |
| Longest sentence 24 words | 24 ("That is two sessions where...") | CONFIRMED |
| Inside 500-700 band | 696, inside | CONFIRMED |

Sentence count: 61. Only ~7 sentences exceed 20 words and none nests clauses; no L6 hit.

**Remaining acronym / TTS-mangle sweep.** The only all-caps token left in the body is **SEBI**, in the compliance firebreak — that is the exemplar's own house form and reads correctly as a word. Every other initialism is avoided as claimed: "Reserve Bank of India" in full, "Oil and Natural Gas Corporation" in full, "lenders who are not banks" for NBFC, "Bharat Petroleum" and "Indian Oil" as names. No numerals, no symbols, no stray abbreviations. Brand is respelled "toro I-Q". Semicolons in the disclaimer render as pauses and match the exemplar verbatim.

**No TTS-breaking artefact found.** L5 is clean.

## Per-sentence ledger

Built cold: script + exemplar only, brief unopened. 61 sentences, all quoted.

**Open**

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK (respelled brand; TTS will voice the letters, which is the intent)
3. "Your read on today's session." — OK

**The lead — the draft rule**

4. "What moved the Indian market today was not oil, and not earnings." — OK. Strong cold open; the negative resolves one sentence later, so no dangling.
5. "It was a draft." — OK. "Draft" lands abstract for one beat, but sentence 6 pays it off immediately. Acceptable on one pass.
6. "The Reserve Bank of India published a proposal on Thursday." — OK. Full name, no initialism. Today is Friday, so "on Thursday" is correctly yesterday.
7. "It would stop lenders who are not banks from offering revolving credit, the kind of limit you can repay and draw again." — OK. The conditional "would" carries the not-yet-law status, and "revolving credit" is glossed in the same breath. This is the single most important sentence in the episode and it is built correctly.
8. "It is not law." — OK. Four words, unmissable.
9. "Comments are open until the twenty eighth of August." — OK
10. "The market priced it today as though it already were." — **FLAG (L1, minor):** elliptical subjunctive. "as though it already were" needs the listener to supply "law" from two sentences back, and the sentence ends on the hanging "were", which in audio can register as an unfinished thought. Meaning survives; the phrasing does not read aloud cleanly.

**The close**

11. "Here is the close." — OK
12. "The Nifty fifty finished at twenty four thousand five hundred and seventy, down zero point two seven percent." — OK
13. "The Sensex fell more, zero point five eight percent." — OK
14. "But that is only because it holds more financial companies, and financials were where the damage was." — OK. See the escalated-lines section: this self-glosses ("financial companies" then "financials") and the comparison base is carried by the preceding "fell more". It lands as mechanical.
15. "It is not a second piece of bad news." — OK. Explicitly forecloses the misreading. Good.
16. "Across the whole market, three hundred and twenty shares rose and three hundred and sixty two fell." — OK. The universe is stated.
17. "The selling was concentrated, not broad." — **FLAG (L4, minor):** the conclusion is asserted but the one-clause mechanism is missing. A naive listener hears near-even counts and is not told why that implies concentration (index weighting). One clause would close it.
18. "Two things I could not check tonight." — OK. First-person and listener-facing; this frame governs sentences 19-20 and is load-bearing for both.
19. "Most sector indices gave no usable reading." — OK. Under the sentence-18 frame this reads as "I could not see how the sectors did". "No usable reading" is thin but comprehensible.
20. "And for a fourth day running, nothing came back from the government bond market, where borrowing costs are set." — OK, with a polish available. See escalated line 1: the v3 wording already removes the FAIL risk the author raised.
21. "On a day about credit, that is the one number you would want." — OK

**Emerging markets**

22. "Emerging markets went the other way today." — OK
23. "Four exchange traded funds that track emerging market shares and bonds all rose while India fell." — OK. "Four exchange traded funds" has its antecedent; the relative clause does the glossing work.
24. "That is the cleanest evidence we have that today was made in India." — **FLAG (L1, minor):** "made in India" is a national slogan in this market. Spoken aloud to an Indian audience, the phrase collides with Make in India for a beat before the intended sense ("the cause was domestic") arrives.

**Oil**

25. "One thing did go India's way this week." — OK
26. "Brent crude fell again today, and is down roughly nine point four percent over the week." — OK. Direction plus the weekly figure, no daily magnitude. Exactly right.
27. "For a country that imports most of its oil, that matters far more than any single day." — OK. Doubles as the justification for withholding the daily number.

**Movers**

28. "Now the movers." — OK
29. "The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at." — OK. Name, placement and the tie back to the lead all in one sentence. This is the fix that makes the episode cohere.
30. "It fell almost six percent, the worst share in both benchmarks." — OK
31. "It had touched a fresh fifty two week high a week earlier, on a quarter with profit up twenty nine percent." — OK. "A quarter" is briefly ambiguous by ear, but "with profit up twenty nine percent" disambiguates inside the same clause.
32. "Nothing about its earnings changed in seven days." — OK
33. "What changed was the list of products it might be allowed to sell." — OK. "Might be allowed" keeps the rule hypothetical. Good.
34. "The biggest gain among the large companies was Siemens Energy India, which makes power equipment." — OK. Name plus what-it-does.
35. "It rose twelve percent." — OK
36. "Revenue was up thirty nine percent and operating profit almost seventy four percent, so profit grew faster than sales." — OK. The trailing clause glosses "operating profit" for a naive ear. See escalated line 2: this fully replaces the fragment the author worried about.
37. "The oddest was Shivalik Bimetal Controls, a small industrial company." — OK. "The oddest" runs parallel to sentence 34 and carries.
38. "It rose twenty percent and locked at its daily price limit, on revenue up a third and profit up forty five percent." — OK. "Locked" is the one opaque word, but "its daily price limit" explains itself.
39. "In the same twenty four hours it disclosed that its outside auditor had resigned, from it and from both its subsidiaries." — OK, with a polish available. "From it" is a thin spoken object; "from the company" reads better aloud.
40. "The market priced the results and ignored the resignation." — OK. See escalated line 3: no cause is asserted for the departure.
41. "Five other shares rose more than seven percent and I could not establish why any of them moved." — OK. Honest, and the count matches the composition note.
42. "We checked everything we normally check and came back empty." — **FLAG (L1, minor):** pronoun shift. Sentences 18, 41 and 43 are "I"; this one is "we", one sentence after "I could not establish". A listener notices the desk appearing and disappearing.

**The wedge**

43. "Here is what struck me most about today." — OK. Mirrors the exemplar's turn.
44. "The Indian companies that buy crude did nothing with that weekly fall." — OK. The gloss is delivered before the names, which is the right order for a linear listener.
45. "Bharat Petroleum finished slightly lower, Indian Oil up half a percent, Reliance Industries up under one percent." — OK as spoken; but see sentence 49, which these numbers later contradict.
46. "Oil and Natural Gas Corporation sits on the other side." — OK. Full name, no initialism.
47. "It pumps crude rather than buying it, so a cheaper barrel cuts what it earns." — OK. The mechanism is stated in plain words, in the right direction, before the number arrives.
48. "It closed up zero point four percent." — OK
49. "So the three that stood to gain did nothing with it, and the one that stood to lose closed higher, not lower." — **FLAG (L4, substantive — the strongest finding in this pass):** the payoff line contradicts its own numbers. Indian Oil at up half a percent is filed under "did nothing", while Oil and Natural Gas Corporation at up zero point four percent is filed under "closed higher, not lower". The smaller rise is the one called a rise. The numbers are three sentences apart, so this is audible in one pass, and it undercuts sentence 50, which states the honest version (nobody moved much). The author's note claims the v2 fix resolved this; it did not — it relocated the same asymmetry into the payoff.
50. "That is two sessions where neither side of India's oil chain has priced a big move in crude, and I cannot tell you why." — OK. This is the accurate framing. Twenty-four words, single thread, speakable in one breath.

**Forward look and close**

51. "What to watch." — OK
52. "Several companies filed their quarters after the close today, Titan among them." — **FLAG (L1 + L2, minor):** "filed their quarters" is desk shorthand for filing quarterly results, and Titan is the one company name in the script with no what-it-does. A strict reading of L2 makes an unexplained name a FAIL; I am grading it WARN because no move, cause or number rides on the name — it is a timing mention. The two-word gloss is free and I recommend taking it.
53. "Those are Monday's news, not today's cause." — OK on the time model (Friday, so the next session is Monday). Minor grammar: "news" is uncountable, so "Those are ... news" is slightly off the ear.
54. "Wednesday brings July inflation." — OK. Correctly future; 12 August is a Wednesday.
55. "The date that matters most is the twenty eighth of August, when comments close on that draft." — OK. Returns to the draft status a fourth time.
56. "Whether the ban survives at all is still open." — **FLAG (L1, minor but positioned badly):** "the ban" is a definite article on an instrument that does not exist. "Survives ... is still open" keeps it provisional and sentence 55 has just said "that draft", so this is not a FAIL. But it is the last substantive line of the episode, which is the worst place to leave a definite noun that could settle in a listener's memory as a thing that happened.
57. "That's your brief." — OK
58. "Before I sign off: this has been general market commentary, not investment advice." — OK
59. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK. Exemplar wording.
60. "Markets are risky; you may lose money; act with care." — OK. Exemplar wording.
61. "See you tomorrow." — **FLAG (L3):** this is a Friday evening recap. "Tomorrow" is Saturday, and the script has itself just told the listener the next market news is Monday's. The sign-off promises an episode that will not exist and contradicts sentence 53 four lines earlier. The exemplar's "See you tomorrow" is correct because that episode was a Thursday.

## The four escalated lines

## Hormuz omission

## The three absolute factual rules

## Punch list

## Source spot-check (S1)

## Disagreements with the author's self-assessment
