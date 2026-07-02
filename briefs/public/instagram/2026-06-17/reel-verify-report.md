# Verify Reel — 2026-06-17 (Tuesday session, EVENING recap)

**Verdict:** PASS (with 2 minor WARNs — principal may ship)

**Stage A (script):**
R1/spine {7-card v1.2 dense format — current production, not stale 4-card; Card 1 = market+why, Nifty only ✓} ·
R1b/time-anchor {session = Tuesday/today; all forward events framed forward ✓} ·
R2/source-fidelity {CARDINAL — every number traces to the brief ✓} ·
R3/selection {Card 2 = the brief's actual Lead (FII flow-turn); Card 4 = sharpest sourced gainer ✓} ·
R4/naive-scroller {each card self-contained, fact→why→so-what ✓} ·
R5/voice & firebreak {teacher voice, zero tip/target language ✓} ·
R6/closer-dedup {names next-two-days flow watch + podcast, not a stale "watch the Fed" refrain ✓}

**Stage B (render):** SCOPED OUT — no `reel.mp4` / `reel-manifest.json` present in `briefs/public/instagram/2026-06-17/` yet. R7 (white frames) / R8 (reveal integrity) must run via `scan_reel.py` after render, before publish. **The reel must not publish without Stage B.**

---

## Per-card ledger

- **Card 0 (poster)** — "+0.57% · 3rd up-day" — OK. Punchy contrast flash, number matches brief line 8.
- **Card 1 (market)** — "+0.57% · Third up-day in a row · Nifty rose to 23,989.15, broad green, no qualifying faller" — OK. Nifty-only, why = cheaper oil (the active driver, not a global headline). Voice 16w.
- **Card 2 (the Lead)** — "Foreign buyers after 13 straight selling days · the money may be coming back" — OK. Correctly carried as DIRECTIONAL with NO crore figure (brief line 10 flags the exact number as unsettled / ₹749 cr selling on one aggregator). This is the right call — exactly the cross-attribution trap avoided. Voice 16w.
- **Card 3 (the chain)** — "Brent −5.19% to $78.85 · cheaper oil plus returning money = real move" — OK. Number traces clean; the chain logic is the brief's Connections thesis. Voice 17w.
- **Card 4 (big move)** — "Sonata Software +19.55% · ~25× volume · India-AI buying" — OK on the numbers (brief lines 64/74). **Minor wording note (WARN-adjacent, not a source error):** on-screen "riding the same India-AI buying that lifted HCLTech's deal" is slightly ambiguous — it can read as if the buying lifted *the deal*. The brief's logic is the reverse: the HCLTech–Sarvam *deal* lifted the AI cohort/sentiment, which Sonata rode. Suggest "...riding the same India-AI buying the HCLTech–Sarvam deal set off" or "...that the HCLTech deal lifted." Voice line ("India-AI buying in full force") is clean. Voice 16w.
- **Card 5 (the catch)** — "Hormuz 40 days to ~6 months · Brent still above pre-war level · easy relief already priced" — OK. Traces to brief lines 34/113. Strong, correctly-sourced "catch." On-screen ~32 words across two sentences (denser than the legacy ≤25 but inside the v1.2 dense reader-first format). Voice 17w.
- **Card 6 (closer + link)** — "What turns this real · watch next two days of foreign flows · full brief + 4-min podcast on Spotify/Apple, link in bio" — OK. Forward watch is the brief's #1 thing-to-watch (line 104). Voice 27w (closer holds longer) — longest line; fine for a closer but the upper bound for render fit (see WARN 2).

---

## Source-fidelity table (R2 — CARDINAL, all ✓)

| Card | Number / claim | Brief line | Verdict |
|---|---|---|---|
| 0/1 | Nifty +0.57% → 23,989.15 | line 8 (also 18, 42) | ✓ |
| 2 | Foreign buyers after 13 selling sessions; NO crore figure | line 10 (also 18, 95); 113 | ✓ (correctly directional) |
| 3 | Brent −5.19% → $78.85 | line 9 (also 18) | ✓ |
| 4 | Sonata +19.55%, ~25× volume, India-AI / HCLTech | lines 64, 74 (HCLTech 54) | ✓ |
| 5 | Hormuz 40 days to ~6 months; Brent above pre-war ~$67 | line 34 (also 107, 113) | ✓ |
| 6 | "next two days of foreign flows" | line 104 (also 95) | ✓ |

Nothing invented, nothing inflated. "19.55%" honestly spoken as "nearly twenty percent" — legitimate speech-rounding. No cross-attribution: each number sits on the right card, and the unsettled FII crore figure is deliberately NOT asserted.

---

## Punch list

**No FAILs.** Two WARNs (principal may ship as-is, or apply):

1. **WARN — Card 4 wording (clarity, not source).** "the same India-AI buying that lifted HCLTech's deal" reverses the brief's causality. Reword so the deal is the cause and Sonata is the rider: e.g. "...riding the same India-AI bid the HCLTech–Sarvam deal lit up." On-screen only; voice line is fine.

2. **WARN — em-dashes + Card 6 length, both render-fit.** (a) On-screen text uses em-dashes in Cards 1/3/5/6; the reel-design house convention (per MEMORY reel/podcast/video card rules) prefers no em-dashes on cards — swap to periods or commas if the renderer doesn't kern them well. (b) Card 6 voice is 27 words, the longest line; confirm at render that it isn't truncated or rushed. Both are caught definitively by Stage B (`scan_reel.py` R8 reveal-integrity) — do not skip it.

**Mandatory before publish:** run Stage B once the `.mp4` + `reel-manifest.json` exist:
```bash
venv/bin/python hive-mind/scripts/scan_reel.py \
  --reel briefs/public/instagram/2026-06-17/reel.mp4 \
  --manifest briefs/public/instagram/2026-06-17/reel-manifest.json
```
R7 (no white/blank frames) and R8 (number+headline present early, why accumulates, full why shown at end) are FAIL-gates that this script-stage cannot cover.

---

## scan_reel report (R7/R8)
Not run — rendered `.mp4` / `reel-manifest.json` not present at report time. Stage B pending render.
