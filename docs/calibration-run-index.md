# Calibration Run Index

Purpose: track pressure-test runs across route families so the project can see which scaffolds have real calibration evidence and which ones are still only planned.

Use this file together with:

- `first-calibration-batch-plan.md`
- `pressure-test-runbook.md`
- `calibration-log-template.md`
- `v1.6-calibration-log-template.md` for v1.6 generated-paper tests

This file is a tracking ledger, not the calibration log itself.

## Status Labels

- `Planned`: selected for the batch, but no run evidence yet.
- `Prepared`: candidate material and minimum-input gate have been checked, but no run evidence yet.
- `Running`: run files or artifacts are being produced.
- `Reviewed`: draft or run outputs have a review note.
- `Calibrated`: calibration log exists and at least one decision was made.
- `Written back`: the calibration led to a repo update.
- `Deferred`: the route is intentionally postponed.

## Batch 1 Tracking

| Priority | Route family | Status | Candidate source | Target failure signal | Expected evidence | Calibration log | Write-back target |
|---:|---|---|---|---|---|---|---|
| 1 | monitoring-route E | Planned | `calibration-candidates/batch1-candidate-selection.md`, Candidate A; problem statement still needs locating | `decision_object_missing` | diagnostic artifact, policy table, consequence comparison | `reviews/calibration-<name>.md` | monitoring route examples, review checklist, claim boundary |
| 2 | forecast-to-decision | Planned | `sample-run-packages/forecast-to-decision-demo/`; real local problem still to be chosen | `bridge_paragraph_missing` | forecast error, decision table, scenario propagation | `reviews/calibration-<name>.md` | forecast route decision, paragraph-density playbook |
| 3 | classification-recognition | Running | `runs/calibration-2021E-classification/`; problem brief and attachment schema extracted | `claim_overreach` | preprocessing, classifier comparison, confusion evidence, target-row isolation, band-fusion audit | `reviews/calibration-2021E-classification.md` | recognition verification plan, evidence matrix |
| 4 | dynamic-scheduling/update | Planned | `run-file-examples/dynamic-scheduling-demo/`; real local problem still to be chosen | `validation_gap` | baseline schedule, revised schedule, before/after audit | `reviews/calibration-<name>.md` | dynamic package, review cue, section budget |
| 5 | geometry/spatial-design | Planned | `run-file-examples/geometry-spatial-demo/`; real local problem still to be chosen | `visual_role_misfit` | scene schematic, design artifact, replay/feasibility evidence | `reviews/calibration-<name>.md` | geometry package, scene-first prompts, figure guidance |

## How To Update This Ledger

After starting a pressure test:

1. set `Status` to `Running`;
2. record the run folder name in the evidence or candidate-source column if useful;
3. add the review path when review exists;
4. add the calibration log path when it exists;
5. change `Status` to `Written back` only after a concrete repo update is made or a no-change decision is explicitly recorded.

## Batch 1 Completion Checklist

- [ ] at least three route families have calibration logs;
- [ ] at least one failure is converted into a route or review improvement;
- [ ] at least one route is confirmed without immediate rule changes;
- [ ] `objective-coverage-matrix.md` is updated with what the calibration proved;
- [ ] this index is updated with final statuses.

## Notes

- Do not mark a route `Calibrated` based only on a review note.
- Do not mark a route `Written back` based only on an intention to update the repo.
- If a run fails before producing paper artifacts, still record the failure if it exposes a route, data, or scaffold problem.
