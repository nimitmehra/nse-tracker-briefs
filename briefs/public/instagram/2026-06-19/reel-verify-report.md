# Verify Reel — 2026-06-19 (18-Jun Thursday evening recap)

**Verdict:** WARN (ship after the em-dash fix below; nothing factual is wrong)

**Format note:** v1.2 dense 7-card (Card 0 poster + Cards 1–6) matching `build_reel_fast.py`. The stale "exactly 4 cards" R1 rule is not applied.

**Stage A (script):** R1 {spine OK — Card 1=market+why, Nifty only} · R1b {time-anchor OK — session=today/Thursday, RBI=Friday/forward} · R2 {source fidelity OK — every number traces} · R3 {selection OK — Lead, chain, catch, named mover} · R4 {naive-scroller OK} · R5 {voice/firebreak OK} · R6 {closer OK} · **em-dash rule: WARN (3 cards)**
**Stage B (render):** SCOPED OUT — no `reel.mp4` / `reel-manifest.json` present yet (this is the pre-render script gate). Run `scan_reel.py` after render, before publish.

---

## The four mandated checks — all PASS

1. **Fed → 18-Jun IT selloff: CORRECTLY tied.** Card 3 frames the hawkish Fed (new chair Warsh) as landing "overnight," lifting US rates + dollar, and IT "the only sector to fall, down 1.19%." The Fed decision landed overnight 17→18-Jun, BEFORE the 18-Jun open, so it is a legitimate **same-session driver** for the 18-Jun close — not a next-session input. Brief line 24 ("last night's US Federal Reserve decision… shaped Thursday") and line 46 (IT "took the full force of the hawkish Fed twice over") confirm. ✓
2. **FII = the −₹855 cr SELL (not the +₹102 cr stale echo): CORRECT.** Card 4 = "−₹855 cr FII sell," "Foreign investors sold about ₹855 crore after the Fed." Brief line 12 explicitly flags +₹101.60 cr as the STALE 17-Jun figure and −₹854.63 cr as the correct 18-Jun provisional. The reel uses the correct figure. ✓
3. **No cross-attribution: CLEAN.** Card 3 Fed→IT; Card 4 FII-sell→post-Fed (line 127); Card 5 Bata→ex-Nike CEO. No driver borrowed from the wrong event. ✓
4. **Voice lines short / no truncation risk: CLEAN.** All voice lines 9–10 words (Card 1 = 10, rest = 9). ✓

---

## Per-card ledger
- **Card 0 — Poster:** "NSE · WED FILING · ₹30,000 cr · India's biggest-ever IPO, the exchange is listing itself." → brief line 18. OK (em-dash in `sub`, see WARN).
- **Card 1 — Market:** "+0.34% · Nifty 24,168, fifth straight up-day · A fifth up-day, but a lagging one · caught only part of a global rally." → line 8 + line 18 (number), line 24/127 (lagged). Nifty only, Sensex omitted. OK.
- **Card 2 — Lead:** "₹30,000 cr · NSE is listing itself · India's largest-ever IPO, >₹5 lakh cr valuation; BSE fell ~4.3%." → line 18. OK.
- **Card 3 — Chain:** "−1.19% · The Fed found one door: IT · hawkish Fed under Warsh lifted rates + dollar overnight; IT only sector down." → lines 8, 24, 46. OK.
- **Card 4 — Catch:** "−₹855 cr FII sell · +₹3,130 cr DII buy · rally is domestically funded." → lines 10, 127. OK.
- **Card 5 — Mover:** "+16% · Bata's two-decade jump · surged 16% (biggest day in ~20 years) on ex-Nike CEO." → lines 67, 78. OK (em-dashes in `why`, see WARN).
- **Card 6 — Closer:** "The catch to remember · a fifth up-day foreigners sat out; full brief + 4-min podcast on Spotify/Apple, link in bio." OK (em-dash in `why`, see WARN). Names the podcast — promotional, not a tip; firebreak intact.

## Source-fidelity table (R2)
- ₹30,000 cr / India's largest / >₹5 lakh cr / BSE −4.3% / "Wed filing" → brief line 18 ✓
- Nifty +0.34% / 24,168 / fifth straight up-day → line 8, line 18 ✓
- Nifty IT −1.19%, lone red sector → lines 8, 46, 58 ✓
- Hawkish Fed under Warsh, rates + dollar up overnight → lines 24, 46 ✓
- FII −₹855 cr (sell) / DII +₹3,130 cr (buy) → line 10 (−₹854.63 / +₹3,129.79), line 127 ✓
- Bata +16% (16.42%) / ex-Nike CEO / biggest day in ~20 yrs → lines 67, 78 ✓
- Honest rounding: 16.42%→"16%", −₹854.63→"₹855 cr", +₹3,129.79→"₹3,130 cr" — all honest speech-rounding, none inflated for drama. ✓

Nothing invented; nothing dramatised; nothing pulled from the stale FII echo.

---

## Punch list (fix before render)
1. **[WARN — em-dashes in rendered card copy]** Three rendered body fields contain em-dashes. House rule is no em-dashes in on-screen text. Replace with commas/periods:
   - **Card 0 `sub`:** "India's biggest-ever IPO — the exchange is listing itself." → "India's biggest-ever IPO. The exchange is listing itself."
   - **Card 5 `why`:** "Bata India surged 16% — reportedly its biggest day in about twenty years — after naming an ex-Nike executive as its new CEO." → "Bata India surged 16%, reportedly its biggest day in about twenty years, after naming an ex-Nike executive as its new CEO."
   - **Card 6 `why`:** "A fifth up-day that foreigners sat out — only local money pushed it higher." → "A fifth up-day that foreigners sat out. Only local money pushed it higher."
   (The `## Card N —` headings and the prose Selection/Source notes are structural / author-only, not rendered — those em-dashes are fine to leave.)
2. **[NOTE — non-blocking wording]** Script line 67 ("Evening time-discipline") calls the Fed "a next-session input, not a same-session intraday cause." That is imprecise for this script: the Fed landed overnight BEFORE the 18-Jun open, so it IS the same-session driver — which the cards (Card 3) get right. Consider tightening the note to "landed overnight before the open, so it drove this same session; forward events (RBI Friday) live in the brief." Cards are correct; only the note is loosely worded. No render impact.

## Stage B (render) — to run after the mp4 exists
```bash
venv/bin/python hive-mind/scripts/scan_reel.py \
  --reel briefs/public/instagram/2026-06-19/reel.mp4 \
  --manifest briefs/public/instagram/2026-06-19/reel-manifest.json
```
R7 (no white/blank frames) and R8 (number+headline present early, why accumulates, full why shown at end) must pass before publish. The reel must not publish without this scan.
