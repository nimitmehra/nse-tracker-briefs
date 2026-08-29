# Verify Podcast Script — 2026-08-28 — ATTEMPT 2 (final cycle)

**Verdict:** _pending_

_Second and final cold read. Target: `briefs/public/podcast/2026-08-28/script.md` (v2). Pass-1 report at `verify-report.md` is preserved untouched._

## 1. Per-sentence ledger (cold read, brief withheld)

Full re-ledger of the v2 body. Verdicts are re-derived, not copied; where pass 1 already judged a line and the line is byte-identical, the verdict is re-stated with any change of view called out. **Changed lines are marked ▲ and were read fresh, in place, in running order.**

### Open + close (1-13)

1. "Good evening." — OK
2. "This is India Markets Brief from toro I-Q." — OK
3. "Your read on Friday's session." — OK
4. "One sector carried Friday's entire market." — OK
5. "Indian software shares rose three and a half percent, with every one of the nine in that index higher." — OK on its own. See 13 for a collision this sentence creates downstream.
6. "The reason came from America, a session late." — OK
7. "Here is where the market closed on Friday." — OK
8. "The Nifty fifty finished at twenty four thousand one hundred and seventy five, up about a third of a percent." — OK
9. "But more shares fell than rose." — OK
10. "Three hundred and forty three were up, three hundred and sixty one were down." — FLAG (L6, carried from pass 1, unfixed): no scope marker; the listener is not told this is the whole market.
11. "Set the technology shares aside and the Nifty fifty was flat, eighteen up and eighteen down." — FLAG (L6, carried from pass 1, unfixed): second up/down pair, second universe, no marker.
12. "The banks did not join in, with Nifty Bank closing level." — OK
13. ▲ "And eight of the nine sectors we can see were flat to down." — **The L1 producer-view FAIL is CLEARED.** Fresh read: this is now a market fact with a direction, not a statement about our data feed. "Usable" is gone; "published no usable move" — the phrase that described our screen rather than the market — is gone. What replaces it is arithmetic a listener can actually hold: nine sectors, eight flat-to-down, one up, and the one that was up is the technology sector named in sentence 5. The narrow-rally point does not merely survive, it lands harder than v1, because v1 gave no direction at all. **One residual, new, minor (L6):** "the nine sectors" arrives thirty words after "every one of the *nine* in that index" — the same number attached to two different denominators (IT index constituents, then sector count). A listener half-attending can hear it as the same nine. One word fixes it if the principal wants: "eight of the nine *other* sectors". Not a gate. **"we can see"** — I looked hard at this, because it is the residue of the confession. It reads as ordinary spoken hedging ("as far as we can see"), not as desk plumbing: it makes no claim about a feed, a table, or a fifth session of failure, and a listener does not stop on it. It stays on the right side of L1.

### The causal chain (14-18) — byte-identical to v1

14. "So why software, and why Friday." — OK
15. "Nvidia, the American chip designer, reported results on Wednesday evening American time." — OK on form. Provenance note carried from pass 1 (S1-c) — see §7.
16. "The verdict arrived a day later, as a broad rise across American software companies, and it landed at Thursday's American close, about half past one on Friday morning here." — OK. Still the best sentence in the episode.
17. "India had already shut on Thursday, three and a half hours before Wall Street opened, and Indian software shares fell that day." — OK. Pre-empts the listener's objection; makes Friday a catch-up.
18. "Friday morning was India's first chance to react." — OK

**No regression:** the causal timing chain is untouched. Verified by diff, not by eye.

### The wedge (19-26) — byte-identical to v1, and still adjacent to the chain

19. "Here is what struck me." — OK
20. "The tempting sentence is that a chip company's demand turns into Indian software revenue." — OK. Hedge before claim.
21. "I do not think that is what happened, and four things say so." — OK
22. "Companies with no artificial intelligence story rose just as much." — OK
23. "The leaders were smaller, jumpier names, and Infosys, the one most people would assume led, lagged its own sector." — OK. Infosys still cast as laggard, never driver. L2-soft (relational placement) carried.
24. "A weaker rupee is what helps a company that earns dollars and spends rupees, and the rupee moved the other way." — OK
25. "And no brokerage published a note on the sector all day." — OK
26. "This was borrowed share price movement, not borrowed business." — OK, intact, and still the strongest line.

**No regression:** wedge text and wedge placement both unchanged.

### Bonds and flows (27-31) — byte-identical to v1

27. "Underneath, India's own bond market is pricing rate rises." — OK
28. "The ten year government bond yield sat near six point nine percent on Friday, a two month high, on a heavy week of government borrowing and renewed expectation that the Reserve Bank of India could raise rates." — OK on listenability (37 words, single-thread). Source hedge still stripped — see §7 (S1-d, carried).
29. "On the money, foreign investors sold about five thousand crore rupees while domestic institutions bought about five thousand two hundred crore." — OK
30. "Foreigners were selling into a rising market." — FLAG (L4, carried from pass 1, unfixed): stated and dropped, no so-what. **This is also the largest piece of free slack in the script — see §3.**
31. "And the fear gauge, India V-I-X, closed near its lowest level in a year." — OK

### Movers (32-44)

32. "Now the movers, and there were no fallers to speak of." — FLAG (L1/L6, carried from pass 1, unfixed): still reads as a contradiction of sentence 9 to a listener who cannot scroll back. Three-word fix still available.
33. ▲ "Not one share fell five percent on Friday, while fifty five rose three percent or more." — **The unsourced-figure FAIL is CLEARED** (provenance confirmed in §7). "Not one share fell five percent on Friday" is byte-identical and untouched. **Does the contrast still land? Yes — but measurably less cleanly than v1, and the reason is worth stating rather than waving through.** v1 compared like with like: nothing fell five, twenty-four rose five. v2 moves the goalposts inside the sentence: nothing fell *five*, fifty-five rose *three*. The rhetorical shape survives — the listener takes away "no big fallers, plenty of decent gainers", which is the true and intended impression — but a listener who is paying full attention can notice the second threshold is lower and discount the contrast slightly. That is an honest cost of the fix, and it is the right trade: a softer contrast that is sourced beats a sharper one that is not. FLAG-lite (L6), not a gate. Optional one-word insurance if the principal wants the snap back: "while fifty five rose at least three."
34. "The biggest gainer was Mastek, a mid-sized Indian software services company, up about eighteen percent." — OK. Superlative re-checked in §6.
35. "A brokerage note holding a positive view on it was doing the rounds." — OK, intact. Still neutral reporting, not endorsement.
36. "But that note was four days old, so it does not explain why Friday." — OK, intact. The four-day-old-note point survives verbatim.
37. "The sector explains about three and a half of those eighteen points." — FLAG (L1, carried from pass 1, unfixed): "points" still collides with the Nifty level.
38. "The rest has no dated trigger." — OK
39. ▲ "Also worth your time, Ather Energy, the electric scooter maker, up eight percent to a genuine new fifty two week high." — **The false-ordinal FAIL is CLEARED, and cleared at the right depth.** Tested against the harder version of the question the parent asked: does the sentence imply *any* rank, not just "second"? It does not. "Also worth your time" is an editorial judgement about attention, not a position in a table. It cannot be heard as second, third or fifth, because it does not enter the ranking frame at all — which matters here, because sentence 34 opened that frame with "The biggest gainer was". The transition steps out of the frame rather than taking a lower rung in it, and that is the only construction that is safe when the true rank is unknown to the listener and the intervening names have been cut. **This is the correct class of fix, not a patch:** the pass-1 error was created by cutting names while keeping an ordinal, and the repair removes the ordinal rather than correcting it — so it stays true no matter what the real rank is. (It is sixth, not fifth — see §6. The fix survives my own pass-1 error, which a corrected ordinal would not have.) FLAG-lite carried: "genuine" is still there (pass-1 item 6, unfixed).
40. "Hero MotoCorp, already Ather's largest shareholder, bought about seventeen hundred and fifty eight crore rupees of shares from an existing holder, taking it to about thirty two point eight percent of the company." — Intact and correct: **"thirty two point eight percent" present, no before-figure, "from an existing holder" present.** FLAG (L2-soft, carried, unfixed): Hero still never described as India's largest two-wheeler maker.
41. "Say this plainly." — OK
42. "No new money went into Ather." — OK. **Present and untouched** — the listener-protection sentence of the episode.
43. "Hero bought shares that already existed, and the deal completes in early September." — OK
44. "Separately, Ola Electric launched its S-one-Z scooter during Friday's session at just under eighty thousand rupees, below where the market expected Ather's next scooter to sit." — OK, intact. **The Konarc / Community Day claim is still absent from the entire spoken body** (grep-confirmed: zero occurrences of "Konarc", "Community" or any launch-event verb attached to Ather).

### Forward look and firebreak (45-54) — byte-identical to v1

45. "Now, what to watch, and it all lands on Monday." — OK
46. "India's June quarter growth figure comes out, with forecasts running from about six point nine percent to eight percent, an unusually wide spread." — OK
47. "The M-S-C-I index reshuffle transacts in the closing auction, and the Reserve Bank's window for foreign currency deposits from Indians abroad shuts." — FLAG-lite (L1, carried, unfixed): "transacts in the closing auction" still ungloss.
48. "And Monday is India's first chance to price Friday night's Jackson Hole speech, where the American central bank's new chairman said inflation is still too high and the Fed may have to raise rates." — OK. **Jackson Hole still framed as Monday's input, and no hike-odds figure anywhere in the body** (grep-confirmed).
49. "That speech landed long after India closed, so it explains nothing about Friday." — OK, intact.
50. "That's your brief." — OK
51-53. Disclaimer block — **verbatim and intact**, all three sentences, in order.
54. "See you Monday." — OK, intact.

**Ledger counts (FLAG hits, v2):** L1 4 · L2 2 (both soft) · L3 0 · L4 1 · L5 1 (word count, see §3) · L6 4 · S1 0 hard, 2 soft (see §7).
All four L1 hits and every L6 hit are **carried-forward pass-1 WARN items that were never gates**. The three items that made pass 1 a FAIL are gone.

## 2. The three fixes — audited, not accepted

I diffed the two spoken bodies mechanically rather than reading for changes, so nothing could hide. **Three clause-level changes, no others.** Sentences 14-31 and 45-54 are byte-identical to v1; every "no regression" claim below rests on that diff, not on my memory.

| # | Fix | Cleared? | Basis |
|---|---|---|---|
| 1 | False ordinal | **CLEARED** | "Also worth your time" implies no rank at all, not a lower rank. See ledger 39 for why that distinction is the whole fix. |
| 2 | Unsourced count | **CLEARED** | Traced to the brief in §7. Contrast still lands, at a small measured cost — ledger 33. |
| 3 | Desk-process line | **CLEARED** | Plumbing confession gone; narrow-rally point stronger than v1, not merely preserved — ledger 13. |

**On fix 1, the part I got wrong at pass 1.** The parent is right and I was wrong: I ranked Ather fifth off the brief's screen table; the full universe puts it sixth (Sonam is missing from the table). I re-derived this independently in §6 rather than accepting it. The material point for this gate: **the fix I recommended at pass 1 — "delete the ordinal" — was correct for a reason better than the one I gave.** I proposed deleting the ordinal because the ordinal was wrong. The stronger reason, which I did not state, is that the script has no reliable access to rank at all once names are cut, so any ordinal is an unverifiable claim regardless of which number is chosen. Had the writer "fixed" this by changing "Second" to "Fifth" — the obvious patch, and one my pass-1 wording half-invited — the script would have shipped a second false superlative and I would have passed it. The writer took the structural repair. That is the right outcome and it is worth recording, because the failure mode here has now produced errors on three consecutive days.

**On fix 2, and the writer's protest.** The parent records that the 24-figure was factually true and the defect was provenance, not accuracy. I accept that and it does not change the pass-1 grade: the script's own header declares "Source: `briefs/public/2026-08-28.md` only. No independent reporting", and a hard spoken count that cannot be reached from the declared source is a defect whether or not it is true — because the gate cannot tell true-and-undeclared from wrong. That is the whole point of the declaration. The replacement is sourced. Correct outcome, correct reason.

**On fix 3, the residue.** "we can see" is the surviving trace of the confession and I tested it rather than assuming. It does not narrate the desk's plumbing to the listener — no feed, no table, no failed session — and no listener stops on it. It clears L1. The one thing fix 3 introduces is a numeric collision with sentence 5 ("nine" twice, two denominators, thirty words apart), which is new and minor; one word ("nine *other* sectors") retires it.

## 3. The word-count refusal — adjudication

**The writer was right. My pass-1 estimate was wrong, and wrong because I asserted a saving I had not counted.**

First, the mechanical facts, which I re-derived rather than took: v1 body **730** words, v2 body **735** (`awk` on the spoken body, both files). Not 736. The header's "735" is correct.

The writer's per-fix arithmetic, checked word by word:

| Fix | v1 | v2 | Δ |
|---|---|---|---|
| 3 (sector line) | "And nine of the eleven sector indices published no usable move." (11) | "And eight of the nine sectors we can see were flat to down." (13) | **+2** |
| 2 (count) | "while twenty four rose five percent or more" (8) | "while fifty five rose three percent or more" (8) | **0** |
| 1 (ordinal) | "Second, Ather Energy," (3) | "Also worth your time, Ather Energy," (6) | **+3** |
| | | | **+5 → 735** |

Exact. 730 + 5 = 735. Every figure the writer gave is correct.

**Now the harder question: was my "~25 words of slack in the punch-list sentences" recoverable?** I re-costed my own pass-1 punch list, which I did not do when I wrote it:

- Item 1 (sentence 13): the only real saving, and only if *deleted* (−11). My own suggested rewrite saved 2 — and the fix actually applied *costs* 2.
- Item 2 ("no fallers to speak of" → "no big fallers"): −2.
- Item 3 ("three and a half of those eighteen points" → "the sector move accounts for only a small part of that rise"): **+1. My own fix adds a word.**
- Item 5 (scope markers): adding "across the whole market" to sentence 10 is **+4**; the 18/18 rewrite is −3. Net **+1**.

My punch list nets to roughly **−2 words**, not −25 — and that is before the three FAIL fixes, two of which had to add words by construction. The 25 was a number I wrote to make a rhetorical point ("the overage pays for itself"), not one I derived. The writer caught it. **It should not have needed catching, and this is the second arithmetic error I have made on this episode** (the other being Ather's rank). Both were assertions made without doing the count in front of me.

**Is the overage now structural rather than sloppy? Yes — with about ten words of nameable slack left, not thirty-five.** The genuinely free cuts, meaning words whose removal costs no content and *also* retires a pass-1 flag:

1. **"Foreigners were selling into a rising market."** — **−7.** Cut it outright. It is a claim with no consequence attached (L4, flagged at pass 1, unfixed); removing it loses nothing a listener was going to keep, and it is by some distance the largest free saving in the file.
2. **"genuine"** in "a genuine new fifty two week high" — **−1.** Pass-1 item 6. It answers a question no listener asked.
3. **"to speak of"** → "no big fallers" — **−2.** Pass-1 item 2, and it removes an apparent contradiction with sentence 9.

That is **735 → 725**. Getting from 725 to 700 does require cutting into the causal chain, the wedge, or the Mastek note point — all of which I passed, twice, and two of which are the reason the episode exists. **So the writer's substantive claim stands: 700 was not reachable without damage.** Its procedural choice — declare the overage in the WARN block rather than hide it or pay for it by cutting a hedge — is the correct one, and it is what I want a writer to do when a verifier's instruction is arithmetically unachievable.

**Does 735 trip L5?** L5 fails a body "well outside ~500-700". 735 is 5% over a soft ceiling written with a tilde; that is not "well outside", and duration — the thing the band exists to protect — is 4.45 min against a 3.5-4.5 band. **WARN, not FAIL.** One caveat I cannot resolve and will not paper over: 4.45 min assumes 165 WPM, and there is **no Sarvam audio on disk for any recent episode to calibrate that against** (checked; no mp3 in any August podcast folder). At 165 WPM the ceiling is ~742 words, so the episode sits about **eight words** inside it. If Sarvam narrates slower than 165 WPM, this episode is over 4.5 minutes. The three cuts above buy back that margin for free and I would take them for that reason alone.

## 4. Show-notes edit — in scope or not

_pending_

## 5. Regression check on everything passed at pass 1

_pending_

## 6. Superlative re-check

_pending_

## 7. Source spot-check (S1) — run LAST

_pending_

## 8. For the principal, before TTS

_pending_
