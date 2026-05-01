# NSE HiveMind — Public Briefs Mirror

This is the public mirror of the daily briefs from the **NSE HiveMind** Indian-equities investment-research pipeline. The full pipeline (intel agents, graph engineer, brief writer, adversarial verifier, deep-research auto-executor, critical-review stress-tester) lives in a private repo; only the published briefs and the graph viewer surface here.

## What you'll find

| Path | Contents |
|---|---|
| `briefs/{YYYY-MM-DD}.md` | The day's published brief — TL;DR, What Happened, Action Items, Cascade Watch, Trigger Watch, Promise Watch (when triggered), Significant Moves, Graph Health |
| `briefs/silent-days.log` | One-line entries on quiet days where no brief was warranted |
| `viewer.html` | The graph viewer — renders the 178-node knowledge graph (27 T1 stocks, 119 T2 stocks, 16 sectors, 12 macros, 4 commodities) |

## Live viewer

The viewer is served via GitHub Pages at:
**https://nimitmehra.github.io/nse-tracker-briefs/viewer.html**

## Discipline notes

- Briefs follow the Economist World-in-Brief voice: story first, implications second, no bare jargon, no bullet-list patchwork where prose belongs.
- Every numeric claim has been digit-by-digit verified by the adversarial /verify-brief-nse step before publication.
- Every Indian regulatory term (Reg 30, MPC, NBS, SAST, NCLT, PIT, LODR, etc.) is expanded to plain English on first use.
- Verification tags — `[CONFIRMED]`, `[REPORTED]`, `[CLAIMED]`, `[REPORTED — Reuters, with India framing caveat applied]` — are preserved verbatim from the upstream intel layer; tags are never upgraded for prose flow.
- The Suzlon-lesson **Promise Watch — Silent Drops** section surfaces when the system detects a management commitment that has gone silent for two consecutive earnings transcripts.

## Mirror cadence

Briefs are published once per trading day at ~04:30 IST. Mirror sync runs at end of pipeline; expect briefs to appear here within 60 seconds of publication.

---

*Pipeline architecture, skill files, intel-agent personas, graph state, deep-research reports, and verify reports are NOT in this repo. They live in the private `nse-tracker` repo.*
