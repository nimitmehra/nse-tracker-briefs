# Verify Podcast Script — 2026-09-15

**Verdict:** WARN
**Checks:** L1 3 / L2 1 / L3 0 / L4 3 / L5 1 / L6 0 / S1 0  (counts = FLAG hits; all L1/L2 hits are borderline, none flagrant; L5 hit is length only — body is symbol-, digit- and dash-clean)

**One line:** No FAIL. Numbers, directions and the evening-model time-words all check against the brief; the script is 100 words over the ceiling and carries seven ear-level phrasings (three inherited verbatim from the brief) that a listener would stumble on once. Principal may ship as-is or take the punch list; nothing needs a re-verify.

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

No FAIL. Nothing blocks TTS on correctness. Items in the order I would take them:

- **[L5-length] 800 words → 700.** Take the writer's own cut menu: (b) Solar's defence-index sentence 26 (20 words), (c) "stocks that ran hardest" sentence 10 (11 words), (d) Tata Sons stake-value sentence 29 (30 words) → ~739. I would NOT take (a), the Asia sentence 14: it is the "why India, specifically" line and the only comparative anchor a listener gets. If the principal wants 700 flat, cut sentence 40 ("It lands after our close…", 17 words) and trim sentence 24's "about twelve thousand nine hundred and fifty-one" to "about thirteen thousand" (−4 words) before touching sentence 14.
- **[L1] Sentence 18 — place the Fed on first mention, drop "priced":** "...and markets put the odds of the American central bank, the Fed, raising rates tomorrow at about ninety-two in a hundred." Sentence 39 then inherits the placement.
- **[L1] Sentence 28 — say what registration:** "...that it cannot hand back its registration as an investment company, and should move towards a stock-market listing." (The brief has "core investment company"; "investment company" is enough for the ear.)
- **[L1] Sentence 13 — give "read as" an agent:** "...for a slower pace of AI development, which investors took to mean Indian software firms get more time to adapt."
- **[L4] Sentences 25 and 36 — the "X is what sold Y" habit, twice:** 25 → "and that uncertainty over funding is why the shares were sold." 36 → "That, in my reading, is what pushed property shares down just over four percent, and lenders like Shriram Finance down four point seven four percent."
- **[L4] Sentence 37 — mechanism for the image:** "The policy rate is unchanged, so this is not a rate rise. But property developers and lenders run on borrowed money, so a higher bond yield hits them the way a rate rise would."
- **[L2-lite] Sentence 27 — three words:** "Tata Chemicals, the soda-ash and salt maker, up nineteen point nine nine percent..."
- **[borderline, after S1] Sentence 4 — "turned" → "stacked":** "after a long weekend that left three things stacked against India at once." Fixes the Friday-announcement looseness without losing the hook.
- **Not flagged, noted:** "AI" is TTS-safe (read as A-I, which is how it is said); sentence 19's "five percent on a safe dollar asset pulls foreign money out" is a plainly stated mechanism and matches the brief's own causal line — keep, or soften to "gives foreign investors less reason to keep money in riskier markets like India" if the principal wants it as a tendency rather than a law; "in my reading" (36) is the correct hedge for a desk inference and is not meta-commentary.

## Source spot-check (S1)

Brief `briefs/public/2026-09-15.md` opened only after the ledger above was written. Result: **PASS — 0 mismatches.** Every figure and every causal direction in the script is in the brief, on the right day.

| Script | Brief | |
|---|---|---|
| Nifty 23,118.6, −1.19%, five-month closing low | 23,118.60 (−1.19%), five-month closing low | ✓ |
| Bank Nifty −1.43% | Nifty Bank −1.43% | ✓ |
| Smallcap −2.44%, "twice as hard" | Nifty Smallcap 250 −2.44%; brief says "twice as hard as the index" | ✓ |
| Software +2.19%, "up more than five percent in the morning" | Nifty IT +2.19%, +5.2% at morning high | ✓ |
| Anthropic head's weekend call, "reported reason" | "reported catalyst… Anthropic chief executive Dario Amodei… primary was not opened" | ✓ hedge matches |
| Asia "mixed rather than crushed", India fell more than all of it | verbatim in the brief, with Nikkei/KOSPI/HSI/ASX ranges | ✓ |
| Saudi pipeline shut since drone strike "last Thursday" | East–West pipeline shut since Thursday 10 September | ✓ |
| Brent above 107 dollars while India was open | "Brent traded above US$107 during Indian hours" | ✓ |
| Rupee 95.945, seven-week low | USD/INR 95.945, seven-week low | ✓ |
| US 10-year touched five percent on Monday | 5.01% intraday Monday | ✓ |
| Fed **rise** tomorrow priced ~92% | "Fed rate rise this Wednesday… about 92% on the CME's tracker" | ✓ direction correct |
| FII net sold 2,977.9 cr, fifth straight day | ₹2,977.90 crore, fifth straight session | ✓ |
| DII bought 2,686 cr, absorbed ~90%, orderly not panic | ₹2,686.00 crore, "about 90%", "orderly way, not one that panicked" | ✓ |
| Solar Industries −13.64%, explosives maker | −13.64% | ✓ |
| Omnia, South African explosives + farm-chemicals, ~12,951 cr cash, "over the holiday" | ₹12,951 crore all-cash, filed Monday 14 September (holiday) | ✓ |
| Filing silent on funding; "that open question is what got sold" | "that open question is what was sold" (brief wording inherited) | ✓ |
| Solar = 12% of defence index; defence fell almost six percent | 12% of Nifty India Defence; −5.96% | ✓ |
| Tata Chemicals +19.99%, locked at upper limit | +19.99%, locked at upper price band | ✓ |
| RBI told Tata Sons it cannot give up registration, should list; "reported" | "cannot surrender its registration as a core investment company… letter itself is not public" | ✓ — see punch list: the brief supplies the "what registration" the script drops |
| Tata Chem owns 2.53% of Tata Sons; stake worth more than Tata Chem | 2.53%; US$200 bn valuation → more than ₹18,722 cr market value (arithmetic: ~₹48,000 cr) | ✓ |
| No listing announced, no date | verbatim | ✓ |
| Banks took dollar deposits from Indians abroad, swapped with RBI for rupees; ~10.5 trn surplus | US$136 bn, "mostly foreign-currency deposits from Indians abroad"; ₹10.5 trillion surplus | ✓ |
| RBI to sell 1 trn of bonds starting Thursday; first tranche 50,000 cr Thursday | ₹1 trillion; ₹50,000 crore Thursday 17 September, then ₹25,000 crore each on 21 and 28 September | ✓ |
| 10-year ~7.1%, four-month high, "reported" | about 7.1%, four-month high, press-reported level only | ✓ |
| Realty "just over four percent", Shriram Finance −4.74% | Nifty Realty −4.04%; SHRIRAMFIN −4.74% | ✓ |
| "Not a rate rise, the policy rate is unchanged" | "liquidity management, not a rate rise; the repo rate is unchanged" | ✓ |
| Fed decision tomorrow ~23:30 IST; Thursday first session to trade it | Wednesday 16 September ~23:30 India time; "Thursday is the first Indian session that can trade it" | ✓ |
| Nothing from the 16 September session | script carries no Wednesday data; brief's own global file rows dated Wednesday were rejected and are not in the script | ✓ |

**Hook timing (sentence 4), resolved against the brief:** the brief's own lead says "after a holiday weekend in which oil, American interest rates and the cost of money at home all turned against India at once", so the script matches its source — not an S1 mismatch. But the brief also dates the RBI bond-sale announcement to **11 September, a Friday trading day**. "Three things turned against India" over the long weekend is therefore loose for the third item (the announcement pre-dates the weekend; what happened over the weekend is that it sat there waiting for a session). One-word fix, no re-verify needed: "after a long weekend that left three things **stacked** against India at once." The brief's wording carries the same looseness; that is the brief verifier's business, not this gate's.

**Inherited phrasings worth knowing:** three of the ledger's WARN lines are the brief's sentences carried over verbatim — "read as giving Indian services firms more time to adapt" (13), "that open question is what was/got sold" (25), "a business that is really a bet on the cost of money" (37). They read fine on a page and less well in the ear; the podcast rewrite should diverge from the brief here.
