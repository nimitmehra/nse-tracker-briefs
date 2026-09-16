# Verify Podcast Script — 2026-09-15

**Verdict:** (pending — cold read in progress)
**Checks:** L1 – / L2 – / L3 – / L4 – / L5 – / L6 – / S1 –  (counts = FLAG hits)

## Mechanical (L5) pre-scan

Machine-checked on the spoken body (below the `---` separator): **800 words**, 46 sentences (regex split; the writer's 48 counts "Oil went up." style fragments differently — immaterial). Zero digits, zero ₹ / % / $ symbols, zero em- or en-dashes, zero `[SAY:]` hints, zero exclamation marks. Nine sentences at 28–34 words; every one is single-thread and comma-segmented (see L6 notes in the ledger). Exemplar body is 681 words.

**Length call:** 800 is 100 words (14%) over the 700 ceiling, ~4.85 min at 165 WPM against the 3.5–4.5 min band. The skill's threshold is "body *well* outside ~500–700"; 800 is outside, not well outside. Scored **WARN (L5-length)**, not FAIL. The writer's own cut menu is sound; my ordering is in the punch list.

## Per-sentence ledger

Read cold: script + exemplar only; brief not opened. Verdict per sentence, checks L1–L6.

**Open**
1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK (TTS respelling of the brand; the exemplar's written "toroIQ" is the same thing spoken)
3. "Your read on today's session." — OK

**Hook**
4. "Today the Nifty closed at its lowest level in five months, after a long weekend in which three things turned against India at once." — OK on the cold read (plain, 24 words, evening-model "today" correct). NOTE, deferred to S1: "long weekend in which three things turned" is a factual timing claim; if any of the three was public before the last session traded, it is loose. Held for the brief check.
5. "Oil went up." — OK
6. "American interest rates went up." — OK
7. "And the Reserve Bank of India is about to drain one trillion rupees of cash from the banking system." — OK (plain; the mechanism is paid off in the wedge section, sentences 32–35)

**The close**
8. "The Nifty fifty finished at twenty-three thousand one hundred and eighteen point six, down one point one nine percent." — OK
9. "The Bank Nifty fell one point four three percent, and smaller companies fell twice as hard as the index, the smallcap index down two point four four percent." — OK (28 words, single thread; "twice as hard" is arithmetically fair, 2.44 vs 1.19)
10. "The stocks that had run hardest through the summer fell hardest." — OK (plain; no names needed, it is a pattern statement not a mover)
11. "One sector rose." — OK
12. "Indian software shares closed up two point one nine percent, after being up more than five percent in the morning." — OK
13. "The reported reason was a weekend call by the head of the AI company Anthropic for a slower pace of AI development, read as giving Indian services firms more time to adapt." — FLAG (L1, borderline → WARN): "read as giving" is agentless desk passive; a listener asks "read by whom?". Also "services firms" shifts the noun from "software shares" one sentence earlier. Rewrite: "...for a slower pace of AI development, which investors took to mean Indian software firms get more time to adapt." "AI" is NOT a TTS flag: reading it as the letters A-I is how the term is spoken. 32 words, single thread — no L6.

**Asia / the two forces**
14. "The rest of Asia was mixed rather than crushed, and India fell more than all of it, because the reasons were India's own: a weaker rupee, a higher bond yield and a foreign seller." — OK (34 words but one thread with a three-item list; sayable). Minor: "a foreign seller" sounds like one entity to a naive ear; "foreign investors selling" is plainer. Not a flag.
15. "On the worrying side, oil and American rates arrived together." — OK ("arrived together" is phrasing, not a metaphor standing in for a chain; the chain follows)
16. "Saudi Arabia's main export pipeline, the route around the closed Strait of Hormuz, has been shut since a drone strike last Thursday." — OK (places Hormuz for the naive listener in the same sentence; "last Thursday" is unambiguous in the evening model)
17. "Brent crude traded above one hundred and seven dollars a barrel while India was open, and the rupee fell to a seven-week low, ninety-five point nine four five to the dollar." — OK (31 words, single thread; digit-by-digit decimal is TTS-safe)
18. "The ten-year American bond yield touched five percent on Monday, and a Fed rate rise tomorrow is priced at about ninety-two percent." — FLAG (L1, borderline → WARN): two things on first mention. "the Fed" is never placed as the American central bank (the exemplar spells out "the Reserve Bank of India"; a naive listener gets no equivalent here). "is priced at about ninety-two percent" is market-shorthand — a listener asks "priced by whom, and what does priced mean?". Rewrite: "...and markets put the odds of the American central bank, the Fed, raising rates tomorrow at about ninety-two in a hundred." Direction (rise vs cut) is held for S1.
19. "Five percent on a safe dollar asset pulls foreign money out of markets like India." — OK on L4: this is mechanism, not metaphor — cause (five percent, risk-free, in dollars) → effect (money leaves riskier markets) is stated plainly, and the so-what is the very next sentence. "safe dollar asset" leans on sentence 18 for its referent, which a linear listener has just heard. It is stated as a law rather than a tendency; a softer form is "...gives foreign investors less reason to keep money in riskier markets like India." Judgment: ship as-is; principal's call on tone, not a verifier flag.
20. "Today foreign investors sold a net two thousand nine hundred and seventy-seven point nine crore rupees, a fifth straight day of selling." — OK
21. "On the supportive side, domestic institutions bought two thousand six hundred and eighty-six crore rupees of shares, absorbing about ninety percent of that, which is why the fall was orderly rather than a panic." — OK (34 words, single thread; 2686 / 2977.9 = 90 percent checks; plain cause → effect)

**Movers**
22. "Now the movers." — OK
23. "The biggest fall among large companies was Solar Industries, the explosives maker, down thirteen point six four percent." — OK (named and placed in one breath)
24. "Over the holiday it agreed to buy Omnia, a South African explosives and farm-chemicals business, for about twelve thousand nine hundred and fifty-one crore rupees in cash." — OK (Omnia placed). Minor: "about" plus a to-the-crore figure is odd; either "about thirteen thousand crore" or drop "about". Not a flag.
25. "The filing does not say how that cash will be raised, and that open question is what got sold." — FLAG (L4 slip → WARN): "that open question is what got sold" is an elision standing in for the chain; a naive listener hears a question being sold. Rewrite: "...and that uncertainty over funding is why the shares were sold."
26. "Solar Industries is twelve percent of the defence index, which is part of why defence shares fell almost six percent today." — OK
27. "The biggest gain was Tata Chemicals, up nineteen point nine nine percent and locked at its upper price limit." — FLAG (L2-lite → WARN, not FAIL): Tata Chemicals is the only company in the script with no "what it does". The name is self-describing so it is not an *unexplained* name (the FAIL condition), but the exemplar gives every mover its three words. Add: "Tata Chemicals, the soda-ash and salt maker,". "locked at its upper price limit" is plain enough.
28. "The Reserve Bank of India is reported to have told Tata Sons, the group's holding company, that it cannot give up its registration and should move towards a stock-market listing." — FLAG (L1, borderline → WARN): "give up its registration" — registration as what? The listener cannot know it is the licence as a large finance company. Rewrite: "...that it cannot hand back its licence as a large finance company, and should move towards a stock-market listing." 30 words, single thread — no L6. Hedge "is reported to have told" is correctly placed before the claim.
29. "Tata Chemicals owns two point five three percent of Tata Sons, and at the valuations quoted in the press that stake alone would be worth more than Tata Chemicals itself." — OK (30 words, single thread; the so-what is explicit)
30. "No listing has been announced and there is no date." — OK (the right closing caveat for a listener who might act on the story)

**The wedge**
31. "Here is what I think is going on underneath." — OK (the exemplar's "Here is the one thing that struck me most" is the same move; a first-person frame on an inference is not meta-commentary about the story)
32. "Over the summer Indian banks took in a flood of dollar deposits from Indians abroad and swapped them with the Reserve Bank of India for rupees." — OK (plain mechanism, step one of the chain)
33. "Those rupees are now a cash surplus of about ten and a half trillion rupees in the banking system." — OK (step two; figure held for S1)
34. "The Reserve Bank's answer is to sell one trillion rupees of government bonds, starting Thursday, and take that cash back." — OK (step three; start day held for S1)
35. "More bonds for sale means a higher bond yield, reported today at about seven point one percent, a four-month high." — OK (supply → yield stated plainly; hedge "reported" precedes the number)
36. "That, in my reading, is what sold property shares, down just over four percent, and lenders like Shriram Finance, down four point seven four percent." — FLAG (L4 slip → WARN, same construction as sentence 25): "is what sold property shares" — the yield did not sell anything; investors did. Rewrite: "That, in my reading, is what pushed property shares down just over four percent, and lenders like Shriram Finance down four point seven four percent." Shriram Finance is placed ("lenders like") — L2 OK. "in my reading" is the right hedge for the desk's own inference.
37. "It is not a rate rise, the policy rate is unchanged, but for a business that is really a bet on the cost of money, it felt like one." — FLAG (L4 slip → WARN): "a business that is really a bet on the cost of money" and "it felt like one" are images doing the work of the chain. Rewrite: "The policy rate is unchanged, so this is not a rate rise. But property developers and lenders run on borrowed money, so a higher bond yield hits them the way a rate rise would." 29 words, comma-spliced but sayable — no L6.

**What to watch**
38. "What to watch." — OK
39. "Tomorrow night at about half past eleven, Indian Standard Time, the Fed announces its rate decision." — OK on L3 (evening model: tomorrow = Wednesday 16 September; 2 pm US Eastern in September = 23:30 IST, arithmetic checks). Carries the sentence-18 note: "the Fed" still unplaced; fix once at sentence 18 and this line inherits it.
40. "It lands after our close, so Thursday is the first session here that can trade it." — OK. Minor: "can trade it" → "can react to it" is the plainer verb. Not a flag.
41. "Thursday morning also brings the first fifty thousand crore rupee bond sale, and the number to watch is the yield the Reserve Bank has to offer to get it sold." — OK (30 words, single thread). Minor: a naive listener will not link "fifty thousand crore" to the "one trillion" of sentence 34; "the first of the bond sales, fifty thousand crore rupees, half the total" closes that. Not a flag.

**Sign-off**
42. "That's your brief." — OK
43. "Before I sign off: this has been general market commentary, not investment advice." — OK (end firebreak verbatim vs exemplar)
44. "For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser." — OK (verbatim)
45. "Markets are risky; you may lose money; act with care." — OK (verbatim)
46. "See you tomorrow." — OK (Wednesday 16 September is a trading day)

**Ledger totals:** 46 sentences, 46 checked. L1 borderline: 3 (13, 18, 28). L2-lite: 1 (27). L3: 0. L4 slips: 3 (25, 36, 37) — the three are the same "X is what sold Y / felt like" habit; not pervasive (three of forty-six, all in the movers/wedge), so WARN not FAIL. L5: length only (800 vs ~700). L6: 0 — nine sentences over 28 words, none nested. No reader-directed language, no tips, no producer-view meta, no "the tape / the tell / the lens".


## Punch list

(pending)

## Source spot-check (S1)

(pending — brief NOT opened until the ledger above is complete)
