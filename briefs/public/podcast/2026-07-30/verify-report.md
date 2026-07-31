# Verify Podcast Script — 2026-07-30

**Verdict:** FAIL (fixable — every finding is a sentence-level rewrite, none requires re-reporting)
**Checks:** L1 6 / L2 3 / L3 1 / L4 3 / L5 0 / L6 3 / S1 (pending)

> Cold read completed before the brief was opened. Ledger below was written from the script + exemplar only.

---

## The fifteen-second test — PASS, and it is the script's best feature

At 165 WPM the first fifteen seconds carry roughly forty-one words. The listener gets:

> "Good evening. This is India Markets Brief from toroIQ. Your read on today's session. The index went up today and most of the market went down. Two out of every three shares ended lower..."

They know what happened before the fifteen-second mark, in a plain-English sentence with no jargon and no patience required. This is a better hook than the exemplar's. Nothing in the punch list should touch the opening paragraph.

---

## Per-sentence ledger

**Opening**

1. "Good evening. This is India Markets Brief from toroIQ. Your read on today's session." — OK (exemplar-identical)
2. "The index went up today and most of the market went down." — OK. Best line in the script.
3. "Two out of every three shares ended lower, four hundred and fifty-seven falling against two hundred and fifteen rising." — OK
4. "Anyone who read only the index number read the opposite of what happened." — OK (minor: "read... read" repeats; survives one hearing)

**The close**

5. "Here is where the market closed." — OK
6. "The Nifty fifty finished at twenty-four thousand three hundred and seventeen, up zero point two eight percent, and the Sensex up zero point three five percent." — OK
7. "But the median stock fell about six-tenths of a percent, and the fear gauge, India VIX, rose over one percent." — FLAG (L1: "the median stock" is statistical vocabulary; "the typical stock" says the same thing to a naive ear)
8. "Fear rising on a rising market is unusual." — OK
9. "Auto shares were the strength, up over one and a half percent as a group, carried by Mahindra and Mahindra's quarter." — **FLAG (L2: a sector move pinned on one named company that is never placed.** No "what it does", and no statement of what the quarter actually showed. The exemplar glosses even Zee and PhysicsWallah.) Also minor L1: "were the strength".
10. "Property developers were the weakest, down about two percent, with insurers and non-bank lenders sold too." — FLAG (L1: "sold too" is desk voice; on one hearing "insurers and non-bank lenders sold" briefly parses as those firms selling something)

**Expiry**

11. "Today was also the Sensex monthly expiry, on the B-S-E, not the National Stock Exchange." — **FLAG (L1: "monthly expiry" is never explained** — a naive listener does not know what expires. The "on the BSE, not the NSE" distinction is a source-accuracy constraint leaking into narration; it means nothing to the listener and costs a clause.)
12. "Expiry days concentrate trading in the biggest index companies, which props the headline up while the average stock falls." — **FLAG (L4 + unsupported generalisation:** stated as a universal law of expiry days, with the mechanism asserted rather than shown, and "props the headline up" is desk voice. **The writer's self-flag #1 is correct** — see Item A.)

**Asia**

13. "Across Asia, Korea, Shanghai and Taiwan fell while Japan rose, and India finished mid-pack." — OK (minor: mixes two countries, a city and a country)
14. "That was a pause in North Asia's chip leadership, not money moving into India." — FLAG (L1: "North Asia's chip leadership" is compressed shorthand. The listener was never told these markets are chip-driven, so the sentence explains a thing they did not know with a thing they also do not know.)

**The two forces**

15. "Now the two forces underneath." — OK
16. "The pressure is interest rates." — OK
17. "The Reserve Bank of India decides on rates next week, and a Reuters poll of seventy-two economists found sixty-eight expecting no change, four expecting a rate hike, and not one expecting a cut." — OK (long at ~35 words but single-thread and cleanly segmented; "not one expecting a cut" is a strong spoken punch. Per L6, not flagged on length alone.)
18. "So the market bought the earnings story and sold anything that depends on rates coming down." — OK (idiomatic but the meaning survives one hearing)
19. "The support is oil." — OK
20. "Brent crude eased about one point two percent today to eighty-nine dollars and sixty-six cents a barrel." — OK
21. "But it is still up almost twenty-three percent over the month, and India imports about eighty-five percent of its oil." — **FLAG (L4: the paragraph declares oil "the support", then gives two facts that both argue the opposite and never resolves them.** A listener is left holding a contradiction. **The writer's self-flag #2 is correct** — see Item B.)

**Movers**

22. "Now the movers." — OK
23. "The biggest gain was Balkrishna Industries, a tyre maker, up almost eleven percent." — OK (properly placed)
24. "It reported revenue up twenty-five percent and profit up fifty-six percent." — OK
25. "A clean result-driven move, from a beaten-down base." — **FLAG (L1: verbless fragment carrying two pieces of desk shorthand.** "Result-driven move" and "beaten-down base" are both note-to-self register, and the fall that created the base is never mentioned elsewhere, so the listener is told to remember something they were never told. **The writer's self-flag #3 is correct** — see Item C.)
26. "Second was Redington, a technology-products distributor, up over eight percent to a one-year high on record quarterly revenue, up thirty-four percent." — FLAG (L6: two different "up X percent" figures in one breath, stacked four facts deep; the listener has to decide which number attaches to what)
27. "But the company itself says part of that came from higher personal-computer prices caused by a global memory-chip shortage." — OK. Strong line — the attribution to the company is exactly right.
28. "That is margin handed to it by a component squeeze, not margin it earned." — FLAG (L1: "margin" is used twice unglossed and "component squeeze" compresses the shortage into jargon one sentence after it was stated plainly)
29. "The sharpest fall was PCBL Chemical, a carbon black maker, down about ten percent on a profit that rose sixty-five percent." — FLAG (L2: "a carbon black maker" is a name, not a what-it-does. A listener does not know what carbon black is or who buys it.) The down-on-good-profit construction itself is excellent.
30. "But roughly seventy crore rupees of that profit was a one-off inventory gain, brokerages pointed out, not operating earnings." — FLAG (L6: the attribution is buried mid-sentence, which strands "not operating earnings" a long way from what it negates)
31. "Strip it out and the growth is a fraction of the headline." — OK. Clean, plain, lands.

**The wedge**

32. "Here is what struck me most about today." — OK (exemplar-matching, and the one first-person use)
33. "Three times over, the market priced where a number came from rather than how big it was." — FLAG (L1, mild: "the market priced where a number came from" uses "priced" in a sense a naive ear does not hold)
34. "PCBL was one." — OK
35. "Hexaware, a technology services firm, was the same idea in reverse." — OK
36. "Its profit fell thirteen percent and the share fell almost seven, but its operating margin actually widened by three and a half percentage points." — FLAG (L1/L6: "fell almost seven" drops its unit and hangs; "operating margin ... percentage points" asks a non-finance listener to hold two technical distinctions at once)
37. "The whole decline sat below the operating line, in one-off items and tax." — **FLAG (L1: "below the operating line" is unambiguous desk shorthand.** Flagrant — this is the single clearest naive-listener failure in the script.)
38. "And KPIT Technologies, whose customers are carmakers, fell nearly eight percent on its guidance rather than its quarter, after European carmakers suddenly cut spending." — FLAG (L1/L6: "on its guidance rather than its quarter" is compressed shorthand for a two-step idea, inside a thirty-word sentence with a trailing cause)
39. "The size of a profit told you very little today." — OK
40. "Where it came from told you almost everything." — OK. Best close of any paragraph here.

**What to watch**

41. "Now, what to watch." — OK
42. "Four large companies filed results in the last eight to twenty-one minutes of trading today." — FLAG (L6, mild: "the last eight to twenty-one minutes" is a data range read aloud as prose; "the final twenty minutes" carries the same meaning)
43. "Vedanta, Bajaj Finance, Hyundai and Mankind." — FLAG (L2: four companies named, none placed. One word each fixes it.)
44. "Their numbers had no time to trade." — OK in isolation, but see next.
45. "Hyundai rose over one percent on profit that fell thirty-five percent, and Bajaj Finance closed flat on profit up almost twenty-eight percent." — **FLAG (internal contradiction, L1/L4): the script has just said these numbers "had no time to trade", then immediately attributes each company's move to those same numbers with the word "on".** A listener hears the script contradict itself one sentence later. **This was not among the writer's three nominations and is more damaging than two of them.**
46. "Tomorrow is when those get priced." — FLAG (L1, mild: "get priced" is desk voice). Time-word itself is correct: Thursday session, Friday reaction.
47. "And the week's real event is the Reserve Bank's rate decision next Wednesday, the fifth of August." — **FLAG (L3: "the week's real event" is wrong.** Today is Thursday the thirtieth; Wednesday the fifth of August is *next* week, as the script itself said in sentence 17. The script contradicts its own time-frame.) **Also not among the writer's nominations.**

**Firebreak**

48. "That's your brief. Before I sign off: this has been general market commentary, not investment advice. For investment advice tailored to your situation, consult a SEBI-registered Investment Adviser. Markets are risky; you may lose money; act with care. See you tomorrow." — OK. Present, complete, exemplar-verbatim, and adequate. No recommendation language appears anywhere in the body.

---

## The writer's three nominations — my independent view

### Item A — the expiry generalisation. **The writer is right, and understates it.**

Two problems, not one. The generalisation ("Expiry days concentrate trading...") is real: it states a standing law of market microstructure where a source can only support what happened today. But the larger cold-read failure is that **"monthly expiry" is never explained at all** — the listener does not know what expires, so the mechanism sentence is explaining an effect of a thing they have not been told about. Fixing only the generalisation leaves the paragraph opaque.

### Item B — the dropped oil caveat. **The writer is right; the caveat is not optional.**

This is not a completeness nicety, it is a coherence failure detectable on the cold read with no source access. The paragraph announces "The support is oil" and then supplies two facts (up twenty-three percent on the month, eighty-five percent import dependence) that both read as pressure. Without the closing clause the listener is handed a contradiction and no resolution. Fifteen words is a bargain.

### Item C — "A clean result-driven move, from a beaten-down base." **The writer is right.**

It reads as a desk note pasted into speech: verbless, and both "result-driven move" and "beaten-down base" are shorthand. The compounding problem the writer did not name: "beaten-down base" assumes prior knowledge of a fall the script never mentions, so it is also an orphan reference.

### Where I differ from the writer

Its three nominations are all valid, but it missed the two findings I would rank highest after the expiry paragraph: the **"no time to trade" / "rose on profit" self-contradiction** (sentence 45) and the **"the week's real event ... next Wednesday" time error** (sentence 47). Both are audible on a single cold hearing. A writer reviewing its own compression looks for things it removed; it does not hear what it left adjacent.

---

## Narratability

- **Mechanically clean (L5: zero hits).** Body is 700 narrated words after SAY-hints are stripped — inside the 500–700 band, at the ceiling. No digits, no percent/rupee/dollar symbols, no em-dashes or en-dashes anywhere in the body. Verified by scan, not by eye.
- **SAY-hints are safe.** `hive-mind/scripts/tts-podcast-nse.py:101` strips `[SAY: ...]` with a regex before synthesis, so the five hints (B-S-E, R-B-I, bal-KRISH-na, RED-ing-ton, P-C-B-L, HEX-a-ware, K-P-I-T, HUN-day) will not be spoken. The 700-word count already excludes them.
- **Constructions TTS will handle poorly:**
  - "the share fell almost seven" — the missing unit will be read as written and lands as an unfinished thought.
  - "the last eight to twenty-one minutes" — a range read as prose; Sarvam will render it flatly and it will sound like a misread.
  - "six-tenths of a percent" is fine spoken; "three and a half percentage points" is fine but conceptually dense.
- **Breath length:** no sentence is unspeakable. Sentence 17 (~35 words) and sentence 38 (~30 words) are the longest; 17 is single-thread and cleanly comma-segmented and passes, 38 nests and does not.

---

## Punch list

Ranked. The first four are the ones I would not ship without.

**1. [L1/L4] Sentences 11–12 — the expiry paragraph.** Replace both sentences with:

> "Today was also settlement day for the monthly derivative contracts on the Sensex, the Bombay exchange's main index, not the National Stock Exchange. On a settlement day, trading crowds into the largest companies in that index, and that can lift the headline number even while the average stock falls."

Explains what expires, keeps the BSE-not-NSE accuracy constraint, and softens the universal law to "can", which is what the day supports.

**2. [L1/L4] Sentence 45 + 44 — the self-contradiction.** Replace with:

> "Their numbers had no time to trade. Hyundai had already closed up over one percent before its profit landed, and that profit was down thirty-five percent. Bajaj Finance closed flat, and its profit was up almost twenty-eight percent. Neither close had anything to do with the numbers."

**3. [L3] Sentence 47 — the week error.** Replace with:

> "And the event that matters most from here is the Reserve Bank's rate decision on Wednesday, the fifth of August."

**4. [L1] Sentence 37 — "below the operating line".** Replace with:

> "The entire fall came from one-off items and tax, not from the business itself."

**5. [L4] Sentence 21 — restore the oil caveat (~16 words).** Append:

> "...and India imports about eighty-five percent of its oil. So today's dip helps at the margin, but at these levels that support is thin and could reverse quickly."

**6. [L2] Sentence 9 — place Mahindra and Mahindra.** Replace with:

> "Auto shares led, up over one and a half percent as a group, after a strong quarter from Mahindra and Mahindra, the tractor and SUV maker."

**7. [L1] Sentence 25 — the Balkrishna fragment.** Replace with:

> "That was a straight reaction to good numbers, and the stock had been beaten down hard going into them."

**8. [L2] Sentences 29 and 43 — one-phrase glosses.**
- "PCBL Chemical, which makes carbon black, the material that goes into tyres and inks, down about ten percent..."
- "Vedanta the miner, Bajaj Finance the lender, Hyundai the carmaker, and Mankind the drugmaker."

**9. [L6] Sentence 26 — split Redington.** Replace with:

> "Second was Redington, which distributes technology products, up over eight percent to a one-year high. Its quarterly revenue was the highest it has ever reported, up thirty-four percent."

**10. [L1, minor] Sentence 7** "the median stock" → "the typical stock". **Sentence 10** "sold too" → "sold as well". **Sentence 14** "a pause in North Asia's chip leadership" → "a pause in the chip trade that drives those markets". **Sentence 46** "get priced" → "get their reaction".

Items 1–5 add roughly forty words net and items 8–9 add about fifteen; items 4, 7 and 10 give some back. Expect the body to land near 730–740 words, above the 700 ceiling. **The word to cut is the Asia paragraph (sentences 13–14, thirty-one words)** — it is the only passage in the script that does not serve the day's story, and removing it pays for every fix above.

## Source spot-check (S1)

_Pending — see below._
