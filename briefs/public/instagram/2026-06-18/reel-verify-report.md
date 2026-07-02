# Verify Reel — 2026-06-18 (Wednesday 2026-06-17 evening recap, June 17 session)

**Verdict:** PASS
**Format:** v1.2 dense 7-card (Card 0 poster + Cards 1–6). The legacy R1 "exactly 4 cards" rule is stale for this format and is NOT applied — judged against the dense production spine instead.

**Stage A (script):** R1 {spine OK — Card 1 = market/Nifty-only/with-why; Card 6 = forward+podcast closer, not stale} · R1b {time-anchor OK — session = "today/Wednesday", Fed = "tonight → Thursday"} · R2 {source-fidelity OK — every number traces, CARDINAL pass} · R3 {selection OK — Lead-first, sourced movers, sideshows excluded} · R4 {naive-scroller OK} · R5 {voice/firebreak OK — no tips, no hype, no meta} · R6 {closer-dedup OK — distinct from 06-15/16/17}
**Stage B (render):** SCOPED OUT — no `reel.mp4` / `reel-manifest.json` in `2026-06-18/` yet (pre-render session). R7/R8 must run via `scan_reel.py` after render, before publish. Reel must not publish without Stage B.

---

## Per-card ledger

0. **Card 0 — Poster** — "NIFTY · WED CLOSE / 24,000 / Cleared for the first time this rally." — **OK.** Single striking fact, flash poster, no body to read. Day-correct ("WED CLOSE"). Traces to brief line 8.

1. **Card 1 — Market** — "+0.40% · NIFTY 50 · Nifty cleared 24,000 · …added 0.40% to 24,085.70 on its fourth straight up-day, money positioning into cyclicals before tonight's US Fed decision." — **OK.** Nifty only (no Sensex/Bank Nifty on the card). Fact → why (pre-Fed cyclical bid) present. Voice line 9 words. Time-anchor clean: session is today, Fed is "tonight." Traces to lines 8, 42.

2. **Card 2 — The Lead** — "₹1.78 lakh cr · DEFENCE PRODUCTION · Defence stocks re-rated · …record FY26 home-built output of ₹1.78 lakh crore, up 15.6%, and the whole listed defence cohort jumped." — **OK.** Matches the brief's Lead. Number is the production milestone (not an order — handled correctly). +15.6% matches line 18. Voice 9 words.

3. **Card 3 — Why it matters (the chain)** — "+6.41% · PARAS DEFENCE · A cohort, not one stock · Paras Defence closed +6.41% at an all-time high, with MTAR, Data Patterns, Astra, HAL and BEL all up. A policy number lifted the shelf." — **OK.** Uses the **+6.41% CLOSE, NOT the faded +18% intraday** — the brief's explicit instruction (lines 84, 90) is honoured. Cohort names all in the brief (line 18 + table 60–85). "A policy number lifted the shelf" = the brief's structural read (line 98). Voice 9 words.

4. **Card 4 — Second notable mover** — "+7.07% · TRENT · Trent caught up to a beat · Trent rose 7.07% as the market re-rated its April Q4 result — revenue up about 20%, profit up 30% — now up 40% off its March low." — **OK on content.** Every figure traces to brief line 63. NOTE on em-dashes below (cosmetic, on-screen text only). Voice 10 words.

5. **Card 5 — The catch** — "₹101 cr vs ₹1,561 cr · THE FLOW SIGNAL · Foreign money barely showed · Domestic funds bought ₹1,561 crore; foreigners bought just ₹101 crore. The rally is real but domestically carried — selling paused, money not yet back." — **OK.** Both figures trace to lines 10, 42, 90. "domestically carried" lifted from brief line 42. No cross-attribution. Voice 10 words.

6. **Card 6 — Closer** — "WHAT TO WATCH · the podcast · Tonight's US Fed decision lands after the close, so it sets up Thursday. Full brief and 4-min podcast on Spotify and Apple, link in bio." — **OK.** Forward catalyst stated with correct causal timing (lands tonight after close → sets up Thursday, NOT today). Podcast named on Spotify + Apple. Voice 11 words. Distinct from recent closers (see R6).

---

## R2 — Source-fidelity table (CARDINAL — all trace)

| Card | Number / claim | Brief line | ✓ |
|---|---|---|---|
| 0/1 | Nifty 24,000 cleared, +0.40% to 24,085.70, fourth straight up-day | 8 | ✓ |
| 1 | pre-Fed cyclical positioning ("money positioning into cyclicals") | 42 | ✓ |
| 2 | record FY26 defence production ₹1.78 lakh cr, +15.6% | 18 | ✓ |
| 2/3 | whole listed defence cohort jumped (MTAR, Data Patterns, Astra, HAL, BEL) | 18, 60, 84–85 | ✓ |
| 3 | Paras Defence **+6.41% CLOSE**, all-time high | 18, 84 | ✓ |
| 3 | +18% intraday explicitly NOT used | 90 (note) | ✓ |
| 4 | Trent +7.07%, revenue ~+20%, profit +30%, +40% off March low | 63 | ✓ |
| 5 | FII +₹101 cr vs DII +₹1,561 cr | 10, 42, 90 | ✓ |
| 6 | US Fed tonight (~11:30 PM IST), after close, gates Thursday | 36, 108 | ✓ |

**Untraceable / dramatised figures: NONE.** Honest speech-rounding only (₹101.59→₹101, ₹1,561.40→₹1,561, +20.x%→"about 20%"). No inflation. CARDINAL gate PASSES.

## R3 — Selection
PASS. Card 2 = the brief's Lead (defence re-rating). Card 3 = the chain/why-it-matters. Card 4 = Trent, a clean **sourced** riser (chosen over the also-clean TMPV −8.30% — defensible, keeps a riser and avoids crowding defence). Card 5 = the honest flow caveat. Correctly **excluded**: IDBI +17.12% (`[REPORTED]` privatisation, not sourced-and-clean), SEAMEC −16.08% and Olectra (cause not established), the Connections second-order threads. No sideshow leads, no obscure small-cap featured, no "cause-not-established" mover on a card.

## R4 — Naive-scroller
PASS. Each card stands alone with fact → why → so-what under ~25 words on-screen. No unexplained jargon ("cyclicals," "re-rated," "cohort" each carry enough context in-card; "DII/FII" rendered as "domestic funds"/"foreigners" in plain English on Card 5).

## R5 — Voice & firebreak
PASS. toroIQ teacher voice throughout. No hype, no cliffhanger/"swipe" bait, no meta. **Zero recommendation/tip language** — no buy/target/sure-thing. Card 5's "Conviction is missing" is a market-state observation, not advice. Regulatory firebreak intact.

## R6 — Closer dedup (WARN-level check)
PASS (no warn). 06-17 closer = "watch the next two days of foreign flows"; 06-16 = the signed-but-not-implemented oil twist; 06-15 = plain podcast plug. Today's closer (Fed-lands-tonight → Thursday + podcast) is distinct — not a repeated refrain.

## Cross-attribution spot-check
Clean. The defence production number drives Cards 2–3 only; Trent's Q4 beat is its own cause on Card 4; the flow signal stands alone on Card 5. No number or cause bleeds across stories.

## Voice-line truncation check (≤12-word ceiling)
All pass: C1=9 · C2=9 · C3=9 · C4=10 · C5=10 · C6=11. None at risk of TTS/caption truncation.

---

## Punch list (non-blocking — cosmetic / next-stage)

1. **(MINOR / house-style)** Cards 4 and 5 `why` text contain em-dashes ("April Q4 result **—** revenue up about 20%, profit up 30% **—** now up 40%"; "domestically carried **—** selling paused"). House rule across podcast/reel copy is no em-dashes. These are on-screen body text (not voice lines), so they do not affect the spoken read, but recommend swapping to a period or comma before render for consistency with the no-em-dash standard. Not a FAIL.
2. **(STAGE B — REQUIRED BEFORE PUBLISH)** Render not present. After `build_reel_fast.py` writes `reel.mp4` + `reel-manifest.json`, run `scan_reel.py` for R7 (no white/blank frames) and R8 (number+headline present early, why accumulates, full why shown at end — especially that Card 3's longer why and Card 4's two-clause why are not cut off). Reel must not publish without this pass.

---

## scan_reel report (R7/R8)
Not run — no rendered `.mp4` in `briefs/public/instagram/2026-06-18/` this session. Stage B scoped out per skill §83. Re-run this verifier's Stage B after render.
