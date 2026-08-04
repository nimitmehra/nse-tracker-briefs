# Verify Podcast Script — 2026-08-04

**Verdict:** FAIL
**Checks (FLAG hits):** L1 6 / L2 3 / L3 0 / L4 3 / L5 0 / L6 3 / S1 0

Cold read performed with the brief withheld. The per-sentence ledger below was completed in full before `briefs/public/2026-08-04.md` was opened.

## TTS mechanics (machine-confirmed on the spoken body)

| Check | Result |
|---|---|
| Narrated word count | 700 — top of the 500-700 band, matches the header claim |
| Digits | zero |
| `₹` / `$` / `%` | zero |
| Em-dashes / en-dashes | zero |
| `[SAY:]` hints | zero (correct — `tts-podcast-nse.py:100` deletes them with no substitution) |
| Longest sentence | 32 words, single-thread, comma-segmented |

Respellings are correctly scoped to the standing rule — respell only where the default word-reading is wrong. `toro I-Q`, `N-S-E`, `B-S-E`, `C-G Power`, `D-L-F` are respelled; SEBI, Nifty, Sensex, Ather, Greaves, Korea, Oman, Hormuz-free body text are left alone and read correctly by default. Nothing else in the body is a mangle risk. **No L5 hits.**

Speakability of the spelled-out numbers is a separate judgment from correctness, and it is where the numbers fall down — see L6 in the ledger (sentences 9, 11, 12).

## Per-sentence ledger

_(section written below)_

## Punch list

_(section written below)_

## Source spot-check (S1)

_(section written below)_
