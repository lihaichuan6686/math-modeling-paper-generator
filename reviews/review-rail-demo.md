# Paper Quality Review

Run: rail-demo
Reviewed: 2026-07-07

## Overall Status

Needs revision

## Critical Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| C01 | `paper/rail_demo.tex` | Warn | The repository includes a compact rail-timetable demo paper that consumes generated Type I artifacts. | It is still synthetic and shorter than a production 20-30 page paper. | Replace synthetic data with real attachments and expand OD/fleet constraints before production use. |

## Important Findings

| ID | Location | Status | Evidence | Risk | Required repair |
|---|---|---|---|---|---|
| I01 | Type I artifacts | Pass | Operation plan, full timetable, capacity audit, tracking audit, dwell audit, and scenario analysis were generated. | Low risk for missing core timetable artifacts. | Check against real problem statement in production runs. |
| I02 | data source | Warn | Data are synthetic and embedded in `src/rail_timetable_demo.py`. | Results cannot support a real contest conclusion. | Replace with parsed attachment data for real runs. |
| I03 | PDF evidence | Unknown | The generation script does not compile or render the PDF. | Layout quality is unverified immediately after generation. | Run `scripts/compile.ps1 -Main rail_demo.tex` and render pages before final acceptance. |

## Warnings

| ID | Location | Status | Evidence | Risk | Suggested repair |
|---|---|---|---|---|---|
| W01 | figures | Pass | Chinese-labeled section-flow, tradeoff, and timetable figures are generated. | Low visual-route risk. | Inspect rendered PDF size and readability. |

## Evidence Checked

- Required Type I machine-readable artifacts exist.
- Capacity and tracking audits have pass/fail fields.
- Scenario table exists for Q3-style recommendations.
- `paper/rail_demo.tex` exists as the compact paper source.

## Evidence Missing Or Not Checked

- PDF compile and rendered-page inspection.
- Real-data parsing from a contest attachment.
- Full 20-30 page contest-paper pacing.

## Required Repairs Before Pass

1. Compile and render the PDF after generation.
2. Replace synthetic data with real problem data for research cases.
3. Add OD assignment and fleet/turnback constraints for production-quality research cases.

## Human Verification Needed

- Confirm whether this demo route should become the next packaged v1.1 example.

## Responsible-Use Notes

- Synthetic research demo only.
- Do not present outputs as official contest results.

Machine gate passed: `scripts/check-run-quality.ps1 -Run rail-demo -Paper rail_demo.tex`.
