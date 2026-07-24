# Verify Podcast Script — 2026-07-24

**Verdict:** WARN
**Checks:** L1 3 / L2 1 / L3 0 / L4 1 / L5 0 / S1 0  (counts = FLAG hits)

Cold read completed against the canonical exemplar BEFORE the brief was opened. Source spot-check (S1) run last. No FAIL trigger fired: no flagrant naive-listener break, no L3 time error, no L5 audio-breaker, no source mismatch. The flags are desk-voice residue plus one genuinely unplaced company name — all WARN-level.

## Per-sentence ledger

**Intro**
1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (standard, matches exemplar)

**Lead**
2. "Indian shares fell for a fifth straight day today, the worst losing streak since January, and the pressure was homegrown." — OK ("homegrown" lands on one hearing = domestic cause)
3. "A ten percent American tariff on Indian exports reached its legal expiry and lapsed this morning." — OK
4. "But it brought no relief at all, because Washington is reported to be moving the same duty onto a new, open-ended legal footing, and the bigger tariff deadline still lands on the first of August with the India-United States trade deal unsigned." — OK (long, single-thread, comma-segmented; cause→effect intact; L6 does not trip on word count alone)
5. "The fall stayed shallow only because domestic funds kept buying." — OK

**The close**
6. "Here is where the market closed today." — OK
7. "The Nifty fifty finished at twenty-three thousand seven hundred and sixty-seven, down zero point four three percent, with the Sensex down the same." — OK (numbers spelled, easy to hear)
8. "But the Bank Nifty closed up a fraction, and the technology index was the one green sector, up about eight-tenths of a percent." — OK (writer-flag c: "one green sector" is a day-only statement, accurate; the brief's −25% YTD context is omitted but the script makes no strength claim beyond the session — the exemplar itself does day-only sector framing. Not a flag.)
9. "Auto, metal and energy shares led the losses." — OK
10. "The fear gauge, India VIX, rose about four percent to fourteen, a jump into the weekend, even though the level is still low." — OK (name-on-mention for VIX handled)

**Divergence**
11. "India fell, but far less than its neighbours." — OK
12. "The emerging-market basket dropped almost two percent, and Taiwan fell over two and a half percent on a global chip sell-off." — OK
13. "That gap is a flows story, not a good-news story." — FLAG (L1: "flows story" is desk-shorthand on first hearing; rescued by the next sentence, and inherited verbatim from the principal-approved brief, so WARN not FAIL)
14. "Domestic buying cushioned the foreign selling; nothing actually turned positive." — OK (this is the sentence that unpacks #13)

**Two forces**
15. "Now the two forces that framed the day." — OK
16. "On the worrying side was oil." — OK
17. "Brent crude breached one hundred dollars a barrel on Thursday, on fresh supply scares in the Red Sea and near the Strait of Hormuz, and stayed near ninety-eight through today's session." — OK (long but single-thread)
18. "For a country that imports about eighty-five percent of its oil, that is the pressure the market kept selling." — OK
19. "Crude did ease almost three percent, but only after the Indian close, so it is a possible relief for Monday, not a help to today." — OK (writer-flag a: the oil-timing sentence lands cleanly for the ear — "eased... but only after the Indian close... a possible relief for Monday, not a help to today" is a complete, plain cause→timing→so-what chain. This is the strongest line in the script. Timing discipline correctly observed.)
20. "On the supportive side was domestic money." — OK
21. "Local funds bought about five thousand four hundred crore rupees of shares against under four thousand crore of foreign selling, and the Reserve Bank's reserves rose, so it was not spending dollars to defend the rupee." — OK (long, single-thread; the "not spending dollars to defend the rupee" so-what is clear)

**Movers**
22. "Now the movers." — OK
23. "The biggest clean gainer was PVR INOX, the cinema operator, up about five and a half percent." — FLAG (L1: "clean gainer" — "clean as opposed to what?" has no referent for a naive listener who does not know Indo Borax +11.4% was excluded for cause-not-established. Honest and precise from the desk's side, but mildly opaque on the ear. Rescued by #25.) (writer-flag b: the PVR-over-Indo-Borax choice is correct and defensible — brief marks PVR [SOURCED], Indo Borax "cause not established" — the word "clean" is the only residue of that reasoning.)
24. "It swung to a fifty-six crore rupee profit from a loss a year ago, with revenue up almost twelve percent, and turned cash-positive on strong footfalls." — OK ("footfalls" = cinema attendance, common enough)
25. "A genuine turnaround, not a momentum pop." — FLAG (L1/L4: "momentum pop" is light desk-jargon; the "genuine turnaround" contrast carries the meaning, so WARN)
26. "The biggest fall was Spandana Sphoorty, a microfinance lender, down about ten and a half percent." — OK (name-on-mention + what-it-does, clean)
27. "It scraped back to a wafer-thin twelve crore rupee profit, and the market read it as an unconvincing recovery, not a real one." — OK
28. "And a momentum name gave back." — FLAG (L1: "a momentum name gave back" is desk-shorthand as a topic sentence — "gave back" = gave back gains, "momentum name" = a stock that had run up; opaque on one hearing, though the next sentence resolves it. WARN.)
29. "Syrma SGS, an electronics manufacturer up a third over three months, fell almost seven percent." — OK (name + what-it-does)
30. "Its board meets next week to consider raising fresh capital through a share sale, and on a stock trading near ninety times earnings, that dilution worry was enough to sell." — OK (plain-English gloss of QIP = "raising fresh capital through a share sale")

**Wedge**
31. "Here is what struck me most about today." — OK (the single first-person moment, matches exemplar)
32. "It was a heavy results day, and the lesson was that a good past quarter is not enough if the future looks softer." — OK
33. "Acutaas Chemicals reported revenue up fifty-nine percent and still fell almost six percent, because management held its growth guidance flat and the stock was already expensive." — OK (what-it-does = chemicals, embedded in name)
34. "Motilal Oswal's profit rose ten percent, but it came from treasury gains, not its core business, and it fell seven percent." — FLAG (L2: "Motilal Oswal" is named with NO plain what-it-does — a naive listener does not know it is a brokerage / financial-services firm. Brief calls it "Motilal Oswal Financial Services." "treasury gains, not its core business" gives partial placement and the LESSON still lands, so WARN not hard-FAIL — but this is the one real name-on-mention gap and the top punch-list item.)
35. "In a nervous market, investors are pricing the next two quarters, not the last one." — OK

**What to watch**
36. "Now, what to watch." — OK
37. "The single biggest event is the first of August, the United States reciprocal-tariff deadline." — OK
38. "The trade deal is stuck, unsigned, over farm and dairy tariffs, so treat it as reported, not confirmed." — OK
39. "And on Monday, watch whether that late easing in oil gives this five-day slide a breather." — OK (time-word "Monday" correctly forward-looking)

**Sign-off**
40. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK (matches exemplar disclaimer)

## Punch list

- [L2 — recommended fix] Sentence 34: add a two-word what-it-does for Motilal Oswal. Suggested: "Motilal Oswal, the broking and wealth firm, saw profit rise ten percent, but it came from treasury gains, not its core business, and it fell seven percent." One-word/one-phrase edit; closes the only genuine name-on-mention gap.
- [L1 — optional] Sentence 23: "biggest clean gainer" → "biggest gainer with a clear reason behind it" (or just "biggest gainer") removes the unreferenced "clean."
- [L1 — optional] Sentence 28: "And a momentum name gave back." → "And a stock that had run up fast gave up ground." — plainer topic sentence for the ear.
- [L1/L4 — optional] Sentence 25: "not a momentum pop" → "not a quick trader's bounce" — de-jargons the contrast.

## Source spot-check (S1) — PASS

Figures cross-checked against `briefs/public/2026-07-24.md`; all match, no direction errors, no wrong-day leakage:

- Nifty 23,767 / −0.43%, Sensex −0.43% (brief: 23,767.45 / −0.43%) ✓
- Bank Nifty "up a fraction" (brief +0.18%) ✓; Nifty IT "one green sector, ~0.8%" (brief +0.82%, "lone green sector") ✓
- Auto/metal/energy led losses ✓; VIX ~4% to 14 (brief 14.03 / +4.08%) ✓
- EM basket "almost two percent" (brief −1.8%), Taiwan "over two and a half" (brief −2.67%) ✓
- Brent breached 100 Thu, ~98 through Fri; eased "almost three percent" after close (brief −2.7%, post-close) ✓ — oil-timing framing matches brief's data-honesty note exactly
- ~85% oil imports ✓; DII ~5,454 cr vs FII under 4,000 cr (brief +5,454 / −3,893) ✓; RBI reserves rose ✓
- PVR INOX +5.5% (brief +5.61%), 56 cr profit from loss, rev +~12% (brief 11.9%), net-cash ✓
- Spandana −10.5% (brief −10.52%), 12 cr profit, unconvincing recovery ✓
- Syrma +33% 3M / −~7% (brief +32.6% / −6.64%), 29-Jul board, share sale, ~90x PE ✓
- Acutaas rev +59% / −~6% (brief −5.77%), guidance held, 69x ✓
- Motilal Oswal profit +10% on treasury gains / −7% (brief −7.3%) ✓
- 1 Aug reciprocal-tariff deadline, deal unsigned on farm/dairy ✓; Monday oil-breather watch ✓

## TTS-hazard scan — CLEAN

Mechanical scan of the body: zero em-dashes, zero ₹/$/% symbols, zero digits (all numbers spelled out). Body word count 699 — inside the ~500-700 band, but at the top edge; any added fix (e.g. the Motilal descriptor) should trade a word out elsewhere to stay under 700. SAY-hint brackets present and, per the header, stripped before TTS.

## Recommendation

**Fix-first (light).** The script is essentially ship-ready — timing discipline, source accuracy, and structure are all clean, and the writer-flagged oil-timing line is the strongest sentence in it. Make the one L2 fix (place Motilal Oswal, sentence 34) before TTS; the three L1 desk-voice tweaks are optional polish. No re-verify needed for the optional items — only re-check word count stays ≤700 after the Motilal edit.
