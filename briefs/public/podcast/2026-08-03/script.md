# Podcast Script — 2026-08-03 (evening recap: the closing-price mechanism changed, the two headline indices disagreed about the size of the rally by ninety basis points, and neither number is wrong)

**Word count:** 699 words narrated (SAY-hint brackets stripped before TTS)
**Estimated duration:** ~4.2 minutes at 165 WPM
**Self-verify:** PASS (REWRITE pass 1, against the cold-read verify report). TTS-clean, machine-checked: zero digits, zero rupee/dollar/percent symbols, zero em-dashes or en-dashes in the spoken body. Longest sentence 28 words, single-thread. First-person used twice, once in the wedge. Lead inherited in substance from the brief. All four FAIL items repaired inside the original word budget: no basis points anywhere, JNK India glossed and respelled, the six-fallers claim regraded to five, and the Hormuz close rewritten to parse on one hearing.
**Skill version:** podcast-script-public-nse v1.7 (evening recap model)
**TTS-ready:** YES (numbers spelled out, no em-dashes). **SAY hints are inert** — `tts-podcast-nse.py:100` strips them with no substitution, so anything a TTS engine would mangle is respelled in the *spoken body* instead. Five documentation-only hints remain (India VIX, OPEC plus, Hormuz, SEBI, Muthoot); "J-N-K India" is respelled in-body and the inert R-B-I hint (attached to a phrase with no abbreviation in it) was removed.

**Composition note (evening recap of TODAY's Monday 03-August close):**
Hook inherits the brief's Lead: the closing-auction switch went live this morning, the Sensex closed up 0.70% and the Nifty up 1.60%, and neither is wrong. The honest measure is breadth — 534 of 680 rose, 144 fell, median stock +1.35%, Nifty 24,774.30. Mechanism order preserved from the brief: (1) the closing-auction plumbing explains why the number you would quote is unreliable, (2) crude at −7.30% to $83.54 is what actually lifted the market, (3) the diplomacy half of the crude story is contested and travels with Iran's denial. Movers: Zee −14.33% (SEBI final order, largest move on the board), Muthoot Finance −7.33% (43% profit growth, margin down 174 bps, sequentially lower), Urban Company +12.98% (the winner, still loss-making). Wedge is the structural contrast: 534 up, only six down 5% or more, five of them for a private reason — set against the honest admission that five of the ten biggest gainers and the day's most watchable fall have no established cause.

**Hard constraints honoured, checked line by line:**
- **Neither index number is called wrong.** The gap is given in plain English as nine tenths of one percent (the brief's 90 bps), stated as day-one plumbing on a new mechanism, explicitly "not a signal". The "second widest since twenty ten" claim now sits in its own sentence, attached to the noun it modifies. No sentence treats the gap as a market message.
- **The auction order flow is attributed, not asserted.** The brief sources it to one brokerage official rather than the exchange, so the script says "brokers say". The mechanism itself is stated flatly; only the day-one order flow carries the hedge.
- **Brent: −7.30%, to $83.54, from Friday's $90.12.** No other crude figure appears anywhere in the script.
- **Hormuz denial travels with the claim, in the same paragraph.** "The called-off strike is confirmed. A deal is not." Iran's foreign ministry denial is stated as of today; the strait is described as still restricted, with ships needing Iranian permission to pass. No sentence presents a deal as settled.
- **India VIX +1.40% to 11.93** on a rising market, two days before the rate decision, given its own line as the odd note. The follow-on "fear was bid up on an up day" was cut: it restated the number in trader idiom without saying why the oddity matters, and the cut funded the four repairs above.
- **Six fell 5% or more against 534 up** carries the wedge.
- **RBI is Wednesday, in What to Watch only.** The 5.25% repo across three meetings is described as what has already happened; the decision is explicitly forward.
- **No cause asserted that the brief refused to assert.** Nifty IT's 3.28% is stated "with no cause anyone could date to today". The wedge now says **five** of the six big fallers had a private reason, matching the brief, which grades JNK India `cause not established`; the earlier "each of those six" both overclaimed and contradicted the next sentence. The five unexplained gainers and JNK India are named as unexplained, and the script says so plainly rather than fitting a story.
- No recommendation language outside the firebreak. No price targets. No broker ratings. No banned trader jargon (machine-checked).

**Deliberate deviations from the skill's section list (both for the word band, both stated):**
1. **No EM-divergence beat (Section 3).** The brief could not read the global frame for Monday — Europe and Taiwan came back stale, the Asia readings were stamped Tuesday, the GIFT Nifty feed was blocked. Inventing an EM divergence would be independent reporting, so the beat is dropped rather than faked. The crude paragraph carries the only genuinely upstream global input.
2. **Sector detail compressed to IT plus breadth.** Nine of eleven sector indices had no previous close, so only IT and Pharma had valid readings; Pharma's 0.48% and the midcap/smallcap +1.2% line were cut for the word band. The median-move group figures (auto ancillaries, capital goods) stay in the written brief.

**Continuity vs the 30-July script:** that spine was the index rising while two of three stocks fell, with a wedge on *where* a profit came from rather than how big it was. Today's is structurally distinct — the index number itself is the thing that cannot be trusted, and breadth is the honest answer. No repeated mover (30 July: Balkrishna, Redington, PCBL, Hexaware, KPIT; today: Zee, Muthoot Finance, Urban Company). Oil has flipped again, from the standing support just under ninety dollars to a seven percent collapse, and the rate meeting has arrived rather than looming.

**Two lines most likely to need the principal's eye:**
1. "So the market priced in a deal that has not been agreed." — replaces "The market bought the claimed half.", which the verifier ruled unparseable on one hearing ("bought" reads as a purchase inside an oil paragraph). Same judgement, no back-reference, and the object is the market's behaviour rather than the diplomacy.
2. "Nobody can tell you why those moved, and anyone who says otherwise is guessing." — deliberately blunt honesty about the seven unexplained moves, and kept verbatim on the verifier's ruling (candour, not abdication). Check the tone is confident rather than defensive.

**Audio status:** NOT generated. Awaiting principal review per the TTS gate.
---

Good evening. This is India Markets Brief from toroIQ. Your read on today's session.

The market went up today, and the two numbers everybody quotes disagreed about how much. The Sensex rose zero point seven zero percent. The Nifty rose one point six zero percent. And neither is wrong.

Here is why. The way India's closing prices are worked out changed this morning. Until Friday, a stock's close was an average of the last half hour of trading. From today, for stocks with futures contracts, it comes from a single auction between quarter past three and half past three. On day one, brokers say, some participants bid above the going price in a few heavyweight Nifty names, and that alone can lift an index close. So that gap, nine tenths of one percent, is day-one plumbing, not a signal. It is the second widest gap since twenty ten.

So how much did the market rise? The honest answer is the breadth. Of six hundred and eighty stocks we track, five hundred and thirty-four rose and one hundred and forty-four fell. The typical stock gained one point three five percent. The Nifty closed at twenty-four thousand seven hundred and seventy-four. Technology was the strongest sector, up three point three percent, with no cause anyone could date to today.

India VIX [SAY: India VIKS], the fear gauge, rose one point four percent to eleven point nine three, on a rising market two days before a rate decision.

What lifted the market was oil. Brent fell seven point three percent over the weekend, from ninety dollars and twelve cents on Friday to eighty-three dollars and fifty-four cents a barrel. OPEC plus [SAY: OH-pek plus] agreed a September output increase on Sunday, and Donald Trump called off a planned strike on Iran. India buys about eighty-five percent of the oil it burns, so a fall that size is money that stays in the country.

Be careful with half of that story. The called-off strike is confirmed. A deal is not. Iran's foreign ministry said today there are no negotiations with the United States. And the Strait of Hormuz [SAY: hor-MOOZ] is still restricted, with ships needing Iranian permission to pass. So the market priced in a deal that has not been agreed.

Now the movers. The biggest fall was Zee Entertainment, down more than fourteen percent. The regulator, SEBI [SAY: SEE-bee], issued a final order on Friday. It bars the company from the market for two months, and its two promoters for a year each, over an unauthorised pledge of company land in twenty sixteen. On that same Friday, shareholders had approved a share issue to those promoters at one hundred and twenty-six rupees. The stock closed today at ninety-eight.

Second, Muthoot Finance [SAY: mu-THOOT], the gold lender, fell over seven percent on a profit that rose forty-three percent. Its lending margin narrowed by about one and three quarter percentage points over the year, and profit was lower than the previous quarter. That forty-three percent is flattered by a weak base.

The biggest gain was Urban Company, the home services app, up almost thirteen percent on revenue up forty-four percent. It is still loss-making.

Here is what struck me today. Five hundred and thirty-four stocks rose, and only six fell five percent or more. Five of those six had a private reason, a regulator's order, a set of results, a margin. None was about the market. But five of the ten biggest gainers have no explanation anyone could establish. Neither does J-N-K India, an industrial equipment maker, down six percent while its capital-goods sector rose. Nobody can tell you why those moved, and anyone who says otherwise is guessing.

Now, what to watch. Wednesday brings the Reserve Bank of India's rate decision. The repo rate has been held at five point two five percent for three meetings and economists expect no change. So the language and the inflation forecast matter more than the number. Tomorrow, watch whether that index gap narrows.

That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow.
