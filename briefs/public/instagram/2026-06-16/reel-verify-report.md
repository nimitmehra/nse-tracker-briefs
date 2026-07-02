# Verify Reel — 2026-06-16 (Monday 15-Jun IST close · EVENING recap)

**Verdict:** FAIL
**Stage A (script):** R1 FAIL (card count) · R1b PASS · R2 PASS · R3 PASS · R4 WARN (several cards >25 words) · R5 PASS · R6 PASS
**Stage B (render):** R7/R8 SCOPED OUT — no `reel.mp4` / `reel-manifest.json` in the date folder yet (render not run). Stage B must run before publish.

---

## Headline reason for FAIL

**R1 (Spine) — FAIL on card count.** The skill requires **exactly 4 cards**. This script ships **Card 0 (Poster) + Card 1 through Card 6 = 7 frames, i.e. 6 content cards** beyond the poster. The exemplar is a tight 4-card spine (market · biggest story · big move · closer). The content here is strong and well-sequenced, but the structure does not meet R1's "exactly 4 cards" requirement. This is a hard FAIL independent of card quality.

Mapped spine as written:
- Card 1 = market (Nifty + why)
- Card 2 = the Lead (US–Iran deal)
- Card 3 = the India-transmission chain (teaching card)
- Card 4 = the big move (Aarti)
- Card 5 = the catch/closer twist
- Card 6 = podcast-link card

To pass R1, collapse to 4 cards. Suggested merge (not prescriptive): fold the Card 3 chain into Card 1's *why* or Card 2's *why* (the 85%-import → inflation → rate-cut chain is the *why* behind both), keep Card 4 (Aarti) as the big move, and merge Card 5 (the twist) + Card 6 (link) into a single closer card — yielding market · Lead · big move · closer.

---

## Per-card ledger

- **Card 0 — Poster** "NIFTY · MON CLOSE · +0.98% · A peace deal, cheaper oil, and a broad rally." — OK as a poster, but it is an extra frame on top of the 4-card spine.
- **Card 1 — "+0.98% · A broad rate-sensitive rally · Nifty rose nearly 1%, risers beating fallers ~4:1, after a weekend peace deal sent oil lower."** — Content OK; number traces; reads clean on a cold read. *why* runs ~30 words (over the ≤25 naive-scroller cap — WARN).
- **Card 2 — "−5.27% · The US and Iran signed a peace deal · 14-point deal, ~107-day war, reopens Hormuz, Brent to $82.73 a three-month low."** — Content OK; the Lead is correctly Card 2; numbers trace. *why* ~40 words (well over 25 — WARN). Number-attribution correct: −5.27% is labelled BRENT CRUDE, not Nifty (good — no cross-attribution).
- **Card 3 — "CHEAPER OIL · why India rallied · 85% import dependence → import bill → inflation → rate-cut room; realty +3.96%, autos +2.60% led."** — Content OK and the best teaching card, but it is a 5th frame (extra card). *sub* ~40 words (WARN).
- **Card 4 — "+13.06% · AARTI INDUSTRIES · the day's sharpest move · multi-year contract wins + ~$150m supply deal + crude feedstock tailwind."** — OK; correctly the cleanest `[SOURCED]` mover; +13.06% labelled to Aarti, not the index (good). Traces to brief line 56.
- **Card 5 — "SIGNED, NOT DONE · the catch · signed but not implemented; mine-clearance 40–50 days; Brent still ~$16 above pre-war."** — OK as a closer twist; not a stale "watch the RBI." *sub* ~33 words (WARN).
- **Card 6 — "the podcast · India Markets Brief on Spotify and Apple; full brief and links in bio."** — OK as a link card, but it is a separate frame; in a 4-card spine this belongs folded into the closer.

---

## Source-fidelity table (R2) — PASS (CARDINAL gate clean)

Every number on every card traces to a brief line; nothing invented or dramatised.

| Card | Number / claim | Brief line | Trace |
|---|---|---|---|
| 1 | Nifty +0.98% (up) | line 8 (+ Lead line 16) | ✓ |
| 1 | risers beating fallers ~4:1 | line 16 | ✓ |
| 2 | Brent −5.27% to $82.73, three-month low | line 9 (+ line 16) | ✓ |
| 2 | 14-point deal, ~107-day war, Hormuz "busiest oil lane" | line 16 | ✓ |
| 3 | ~85% of crude imported | line 16 | ✓ |
| 3 | Realty +3.96%, Autos +2.60% | line 40 | ✓ |
| 4 | Aarti +13.06% | line 56 | ✓ |
| 4 | ~$150m supply deal + backward-integration tie-up | line 56 | ✓ |
| 5 | signed but not implemented; mine-clearance 40–50 days | lines 16, 32 | ✓ |
| 5 | Brent ~$16 above pre-war $67 | lines 9, 32 | ✓ |

Speech-rounding only: +0.98% → "nearly one percent", +13.06% → "thirteen percent" — both honest. **No index/number cross-attribution** (−5.27% is on Brent, +13.06% is on Aarti, neither presented as the market). Single index used (Nifty only); Sensex/Bank Nifty correctly omitted. No em-dashes used as connectors in the on-screen copy. PASS.

## Selection (R3) — PASS
- Card 2 = the brief's Lead (US–Iran). ✓
- Card 4 mover = Aarti +13.06%, the cleanest `[SOURCED]` biggest mover; `[HYPOTHESIS]` / "cause not established" names (Kalyan, Ajmera, SPAL) correctly hard-excluded per the mover filter. ✓
- No sideshow leading, no obscure small-cap featured. ✓

## Voice & firebreak (R5) — PASS
toroIQ teacher voice throughout. No hype, no cliffhangers ("swipe for 🤯"), no meta. Zero recommendation/tip language. Note: the brief's Goldman 'Buy' upgrade (Schneider, line 58) does NOT leak in because Schneider is not a card. PASS.

## Time-anchor (R1b) — PASS
Session framed as Monday/"today" (the close just covered); deal signed "over the weekend" (past); Fed (June 16–17) and Geneva (Fri June 19) kept off the cards. No inverted time-words. PASS.

## Closer dedup (R6) — PASS
Closer = "SIGNED, NOT DONE" (the day's real nuance), not a recycled "watch the RBI" refrain. PASS.

---

## scan_reel report (R7/R8)
Not run — `briefs/public/instagram/2026-06-16/reel.mp4` and `reel-manifest.json` are not present (only `reel-script.md` and a `carousel/` folder exist). Per the skill's honest-constraints clause, Stage B scopes out with a note. The reel must not publish without Stage B passing (no white frames; headline+number present early; why accumulates and shows in full).

---

## Punch list (fix before publish)
1. **[FAIL — R1] Card count.** Collapse the Poster + 6 content cards down to **exactly 4 cards** (market · Lead · big move · closer). The Card 3 transmission chain should become the *why* of Card 1/Card 2; the Card 6 link should fold into the closer. Re-check after restructuring.
2. **[WARN — R4] Length.** Cards 1, 2, 3 and 5 each run 30–40 words in the on-screen *why/sub* vs the ≤25-word naive-scroller cap. Tighten the on-screen copy (the longer *voice* line can stay; the read-on-screen text should be terser).
3. **[BLOCKER for publish — Stage B] Render not present.** Run the render pipeline, then run `scan_reel.py` for R7/R8 before the principal-review-and-publish gate.

Gates the reel only — not the brief, not the podcast.
