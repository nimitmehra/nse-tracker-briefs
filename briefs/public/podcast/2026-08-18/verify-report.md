# Verify Podcast Script — 2026-08-18 (fix pass v3 — REVERIFY)

**Verdict:** _pending_
**Checks:** _pending_

## Per-sentence ledger

Built cold, before the brief was opened. Fifty-seven sentences in the spoken body (everything below the metadata separator).

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on today's session." — OK
4. "Two government notifications organised today's session, and neither was a market event." — OK. "Neither was a market event" is plain English, not desk shorthand; a listener hears "neither was itself about the market" and the next three sentences pay it off.
5. "The electronics ministry approved its first batch of component-making projects, worth nearly seven thousand nine hundred crore rupees." — OK
6. "The defence ministry published a sixth list of four hundred and five items to be bought from Indian suppliers, not imported." — OK. The "not imported" tail does the explaining work without jargon.
7. "Shares in both groups rose while the market fell." — OK. The reference now points backwards to the two ministries just described. The v2 forward-reference is gone.
8. "The Nifty fifty closed down zero point five five percent, at twenty four thousand one hundred and fifty four." — OK
9. "Eight of its shares rose and thirty three fell." — OK for listenability. Flagged to S1 only: eight plus thirty three is forty one of fifty, which implies nine unchanged. Checked against the brief below.
10. "The smallcap index was the only major index to rise." — FLAG (L1, advisory): "smallcap" is never glossed. The exemplar glosses its one piece of market vocabulary in the same breath ("the fear gauge, India VIX"). Not flagrant desk shorthand, so not a blocker; "the index of smaller companies" would close it at zero word cost.
11. "Six of the biggest movers we follow closed at their highest level in a year." — OK (accepted orchestrator override). "We follow" is producer-scope language, kept deliberately because the count is scoped to the roughly seven-hundred-stock screened universe and an unscoped phrasing would over-claim to the whole exchange. Not re-flagged as a blocker.
12. "So the average fell and most of the market did not." — OK. "The average" is a plain-English stand-in for the index and lands after its evidence, not before it. This is the v2 L4 fix and it works.
13. "Almost all the damage came from technology." — OK
14. "That index fell one point nine three percent, more than three times the fall in the Nifty fifty, with all eleven of its companies down." — OK. Twenty-five words, single-thread, comma-segmented, sayable in one breath. Arithmetic is internally consistent (one point nine three over zero point five five is three and a half).
15. "Asian markets went in different directions today, and foreign money across emerging markets barely moved." — OK
16. "Nothing outside India explains today's fall, which was made at home." — OK
17. "The worrying story is oil, and not because of today." — OK
18. "Tanker attacks have resumed near the Strait of Hormuz, the narrow lane that carries much of the world's oil." — OK. Gloss carried verbatim from the exemplar; correct call.
19. "Weekend traffic through it reportedly nearly stopped." — OK. The hedge "reportedly" is audible and correct.
20. "Brent crude, the global oil price, is about nine percent higher than on the seventh of August." — OK. First-use gloss present.
21. "The Reserve Bank of India cut its inflation forecast this month, explicitly because crude was cheap." — OK. Said in full, no initialism.
22. "That reason has reversed inside a fortnight." — OK, with a note: the chain is complete (cheap crude was the stated reason, crude is no longer cheap), but the so-what is left for the listener to finish. A five-word tail ("so that forecast is now at risk") would make it explicit. Not a flag; the exemplar allows this much compression.
23. "Another thing gets missed." — OK
24. "What factories charged for their goods rose eight point two nine percent in July." — OK. Factory-gate framing is plain and the roles are the right way round.
25. "What households paid in the shops rose four point four five percent." — OK
26. "That gap gets absorbed by whoever sits in between and cannot raise prices." — OK. "Whoever sits in between" is vague but self-explaining in context, and naming the layer would cost accuracy.
27. "It is a margin story, not an inflation story." — OK. Same construction the exemplar sanctions ("it is foreign money leaving, not a currency story").
28. "Now the movers." — OK
29. "Paras Defence and Space Technologies rose ten percent." — OK. The name carries its own what-it-does.
30. "The defence list was announced at twelve nineteen, during trading hours, the clearest link between news and price today." — OK. "During trading hours" does the work the old desk phrasing was doing.
31. "The whole list, though, is an estimated three thousand and seventy crore rupees of business, spread over years and the whole supply chain." — OK. The caveat travels with the number, in the same sentence.
32. "Paras on its own is valued on the stock market at about four times that." — OK. "Valued on the stock market" replaces the bare "worth"; the comparison is now unambiguous.
33. "Jyoti C N C Automation, which is putting over a thousand crore rupees into its Rajkot plant, gained eight point three percent." — OK, with a residual note. The v2 blocker (named twice, never placed) is cleared: the listener now knows it is a manufacturer with a plant in Rajkot spending real money. It is placement by fact rather than a what-it-does descriptor, which is the honest ceiling given the brief carries no business description. A sourced three-word descriptor would fully satisfy L2; do not invent one.
34. "It disclosed that approval at ten twenty two on Monday night, so today was the first session that could react." — FLAG (L2 referent, WARN): "that approval" has no antecedent. The word "approval" was last heard in sentence five, attached to the electronics ministry. A listener hearing "It disclosed that approval" can plausibly attach it to the ministry scheme rather than to Jyoti's own board sign-off on the plant spend. The time anchor and the L3 fix in the second half are both correct.
35. "The one real fall was Ahluwalia Contracts, a construction company, down almost eleven percent." — OK. Named and placed in the same breath.
36. "June quarter sales rose twelve percent and net profit fell almost eighty percent." — OK
37. "That is a cost problem, not a demand problem." — OK. Mechanism stated plainly, once.
38. "The results came out after Friday's close, the management call recording after Monday's close, and today the market gave its verdict." — OK. Twenty-one words, three clean beats, one thread. "The management call recording" is now glossed enough to survive one hearing.
39. "The call had made things worse, not better." — OK
40. "Tube Investments of India, an engineering group, ran the same sequence the other way, up almost eight percent." — FLAG (L4, isolated): "ran the same sequence the other way" asserts a chain it never shows. For Ahluwalia the listener got three dated events; for Tube there is no timestamp, no call, no verdict, only a revenue line. The phrase is doing the work a plain clause should do. Suggested plain rewrite: "Tube Investments of India, an engineering group, went the other way, up almost eight percent, on results the market liked."
41. "June quarter revenue rose seventeen percent, with double digit growth in every segment." — OK
42. "Here is what struck me most today." — OK. Exemplar's own hinge line.
43. "The papers explained the fall with high crude and rising American bond yields." — OK, with a note: "bond yields" is unglossed, but it is being reported as what the papers said and is then dismissed, so a listener does not need to price it to follow the argument.
44. "Brent moved one hundredth of one percent today." — OK
45. "It did not move." — OK. The strongest line in the script.
46. "Crude is at a high level and American yields are rising, but a level is not an event." — OK. Cause-and-effect distinction made in plain words.
47. "I could not find a dated reason for the technology fall, and I am not going to invent one." — FLAG (L1, WARN): "a dated reason" is ambiguous on one hearing. In speech, "dated" most commonly means out of date, so a listener can hear "I could not find an outdated reason", which is the opposite of the meaning. Suggested rewrite: "I could not find a piece of news today that explains the technology fall, and I am not going to invent one."
48. "I can tell you what the press got wrong." — OK
49. "I cannot tell you why technology fell." — OK
50. "Tomorrow night, around half past eleven our time, the American Federal Reserve is due to publish the minutes of its July meeting." — OK. Correct evening model: a not-yet-happened event is "tomorrow night". The hedge "is due to publish" is audible.
51. "Three of its regional presidents voted there for a rate increase." — OK. "There" anchors it to the July meeting; the v2 time-anchor gap is closed.
52. "Indian markets get their first chance to react on Thursday." — OK. Internally consistent: today is a Tuesday (Friday results, Monday call, today's verdict; Monday-night disclosure reacted to today), so a Wednesday-night release lands on Thursday.
53. "That's your brief." — OK
54. "Before I sign off: this has been general market commentary, not investment advice." — OK
55. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK
56. "Markets are risky; you may lose money; act with care." — OK
57. "See you tomorrow." — OK

## Punch list

None of these is a blocker. All three are single-clause swaps that cost no words.

- **[L2 referent, sentence 34]** "It disclosed that approval at ten twenty two on Monday night" — "that approval" has no antecedent and can attach to the electronics ministry approval from sentence five. Rewrite: **"It announced that investment at ten twenty two on Monday night, so today was the first session that could react."**
- **[L1, sentence 47]** "a dated reason" reads as "an out-of-date reason" on one hearing. Rewrite: **"I could not find a piece of news today that explains the technology fall, and I am not going to invent one."**
- **[L4, sentence 40]** "ran the same sequence the other way" asserts a chain the script never shows for Tube Investments (no timestamp, no call, no verdict). Rewrite: **"Tube Investments of India, an engineering group, went the other way, up almost eight percent, on results the market liked."**
- **[L1, advisory, sentence 10]** "the smallcap index" is unglossed. Optional swap: **"the index of smaller companies was the only major index to rise."** Note this one adds two words against a body already at the seven-hundred ceiling, so it trades against the fixes above.

**Accepted override (not a finding):** sentence 11, "the biggest movers we follow". Producer-scope language, kept deliberately for scope accuracy — the count belongs to the roughly seven-hundred-stock screened universe, and an unscoped phrasing would over-claim to the whole exchange. Recorded as accepted, not re-flagged.

**Above the exemplar.** Sentences 43 to 49 — the crude correction paired with the refusal to invent a reason for the technology fall — are stronger than anything in the current canonical exemplar. The exemplar's closing insight explains a move; this one refuses to, and says so out loud. Per the skill's drift rule, this is raised to the principal as an exemplar-refresh candidate rather than acted on silently.

## Previous FAIL items — cleared?

_pending_

## Mechanical checks (L5 / L6)

_pending_

## Source spot-check (S1)

_pending_
