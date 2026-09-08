# Verify Podcast Script — 2026-09-07

**Verdict:** FAIL
**Checks:** L1 8 / L2 2 / L3 0 / L4 2 / L5 1 / L6 0 / S1 not run (isolation ordered)  (counts = FLAG hits)

_Cold read only. The brief (`briefs/public/2026-09-07.md`) was NOT opened — the invoking session explicitly ordered full context isolation, so Step 2's source spot-check is deferred, not passed. No web searches run._

## Mechanical results (L5)

Run on the spoken body only (everything below the `---` separator):

| Check | Result |
|---|---|
| Digits in body | 0 — clean |
| `%`, `₹`, `$` symbols | 0 — clean |
| Em-dashes / en-dashes | 0 — clean |
| `[SAY:]` hints | 0 — clean |
| Exclamation points | 0 — clean |
| Sentence count | 55 |
| Longest sentence | 32 words, single-thread (the G-R-T open-offer line) |
| Sentences >30 words | 1 |
| **Word count** | **857 — 157 over the 700 ceiling (22.4% over)** |

**L5 FLAG (1):** body word count. The script's own header declares this as a WARN and argues it is earned by the ten-day gap. The gate does not grade it that way: Step 3 makes "body well outside ~500-700" an audio-breaker. 857 is 22% past the ceiling and 71% past the floor of the exemplar band. It is a legitimate FAIL trigger on its own, though it is **not** the reason this report says FAIL — see Verdict rationale. Everything else mechanical is clean, and the respellings (toro I-Q, S-K hynix, G-R-T, S-G-S) are correctly handled.

## Per-sentence ledger

## Punch list

## Source spot-check (S1)

## Verdict rationale
