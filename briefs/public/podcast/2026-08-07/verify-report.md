# Verify Podcast Script — 2026-08-07

**Verdict (v2, fix pass): WARN — shippable at the principal's discretion.**
**Checks (v2):** L1 2 / L2 0 / L3 0 / L4 3 / L5 0 / L6 0 / S1 NOT RUN
*(v1 was FAIL — L1 4 / L2 5 / L3 0 / L4 3 / L5 0 / L6 1. All nine v1 FAIL hits cleared.)*

*Both passes were cold reads on the spoken body only (everything below the `---` separator), against `briefs/public/podcast/canonical_voice_example/README.md`. The brief was never opened. No web search, no outside research. v2 body: 61 sentences, 702 words, longest sentence 25 words.*

## v2 headline

The fix pass cleared every FAIL. The episode's causal chain now closes — the listener is told in the same breath that Bajaj Finance is one of the lenders the draft targets — and the producer-view data paragraph has been turned listener-facing with a stated reason it matters. The Sensex composition effect and the oil-wedge punchline are both materially better than v1 and now read at exemplar standard.

Two things the fix pass introduced, neither fatal:

1. **"The government bond market ... came back empty for a fourth day running"** now makes *the market* the grammatical subject of "came back empty". A naive listener can hear that as a fact about the bond market (no trading) rather than a gap in our data. v1's "the government bond curve" was inert jargon; v2 is clearer but newly *mis*-readable. This is the one line I would change before TTS.
2. **"Growth and margins moving together."** — a verbless analyst fragment with no so-what, and "margins" is unglossed.

## Section 1 — v1 FAIL disposition

| # | v1 FAIL | v2 sentence | Status |
|---|---|---|---|
| L2 | Bajaj Finance, no what-it-does | "The biggest fall was Bajaj Finance, one of the lenders that draft is aimed at." | **CLEARED** — placed in the same breath; the lead-to-mover bridge now exists |
| L2 | Siemens Energy India, no what-it-does | "...Siemens Energy India, which makes power equipment." | **CLEARED** |
| L2 | Shivalik Bimetal Controls, no what-it-does | "The oddest was Shivalik Bimetal Controls, a small industrial company." | **CLEARED** — minimal but adequate and non-claiming |
| L2 | Three bare names in what-to-watch | "Several companies filed their quarters after the close today, Titan among them." | **CLEARED** as a FAIL; residual WARN below |
| L2 | "The four funds" — no antecedent | "Four exchange traded funds that track emerging market shares and bonds..." | **CLEARED** — the trailing clause glosses the jargon in place |
| L1 | Producer-view data paragraph (flagrant) | "Two things I could not check for you tonight. / ...where borrowing costs are set... / On a day about credit, that is the one number you would want." | **CLEARED** as flagrant; two residual WARNs below |
| L1 | "That is arithmetic, not a second signal" | "But that is only because it holds more financial companies... It is not a second piece of bad news." | **CLEARED** — also clears the v1 L6 flag on "fell ... further only because" |
| L1 | Breadth count with no universe | "Across the whole market, three hundred and twenty shares rose..." | **CLEARED** as an L1; see S1 note on the label |
| L1 | "any single day's tick" (jargon) | "...that matters far more than any single day." | **CLEARED** |
| L4 | Oil punchline contradicted its own numbers | "...the three that stood to gain did nothing with it, and the one that stood to lose closed higher, not lower." | **CLEARED** — direction-only framing removes the contradiction; this is now the strongest passage in the episode |
| L1/L4 | "The market priced the first document and not the second" | "The market priced the results and ignored the resignation." | **CLEARED** |
| L6 | Sentence 13 re-parse | split into three sentences | **CLEARED** — longest sentence is now 25 words |
