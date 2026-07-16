# Calibration Log: 2021E Classification Recognition

## Header

- run name: `calibration-2021E-classification`
- date: 2026-07-13
- problem source: local 2021 CUMCM E problem package, including `CUMCM2021-E.pdf` and four `.xlsx` attachments
- route family: classification-recognition
- nearest run-file example used: `docs/run-file-examples/classification-recognition-demo/`
- nearest sample package used: `docs/sample-run-packages/classification-recognition-demo/`
- nearest deep-reading anchor used: `knowledge/cumcm/deep-reading-2021E014.md`
- extracted source notes: `runs/calibration-2021E-classification/problem-brief.md`, `source-extraction.md/json`, `data-schema-summary.md/json`

## Route Decision Audit

- modeled object: high-dimensional sample features after preprocessing and representation selection
- decision object: category or origin identification rule with class-level evidence
- chosen family: classification-recognition
- nearest rejected family: generic evaluation or clustering
- did the route fit: `yes`, pending problem-text extraction confirmation
- note: this run is selected because it stresses preprocessing, classifier comparison, and claim-boundary discipline.

## Evidence Audit

| Check | Status | Evidence | Notes |
| --- | --- | --- | --- |
| each major subquestion has a visible artifact | planned | Q1 spectral overview, Q2/Q3/Q4 answer tables, Q3 band-fusion audit are named | must be confirmed after first draft |
| family-specific evidence burden is met | planned | preprocessing, feature representation, classifier comparison, confusion evidence, target-row isolation named | not yet executed |
| validation is real rather than ceremonial | partial | split policy, target-row exclusion, and baseline comparison now have first artifacts | stronger route still needed before paper drafting |
| first strong figure has the right role for this family | planned | feature or spectrum overview should come before result charts | figure plan now names the route, raw-feature, preprocessing, representation, comparison, confusion, and sensitivity figures |
| abstract numbers and main results match the artifact ledger | not started | no draft yet | check after generated paper exists |

## Writing Audit

- did the abstract close each major subquestion: not started
- did the conclusion stay within the claim boundary: not started
- which section felt too thin: not started
- which bridge paragraph was missing or weak: likely preprocessing-to-classifier bridge; verify after draft
- did any section feel artifact-stacked: not started
- did paragraph density match the family: not started

## Major Failures To Watch

- bucket: `claim_overreach`
  evidence: overall score without class-level diagnostics
  impact: paper sounds award-like but cannot justify identification reliability

- bucket: `validation_gap`
  evidence: no split policy, no baseline, or metrics from inconsistent preprocessing routes
  impact: model comparison becomes ceremonial

- bucket: `artifact_gap`
  evidence: missing preprocessing-effect figure or feature-reduction evidence
  impact: method chain becomes uninspectable

## What Actually Worked

- strongest section: not started
- strongest artifact: `problem-brief.md` and `data-schema-summary.md` converted a generic classification candidate into a concrete four-subquestion spectral-identification pressure test.
- strongest family-specific control that helped: source extraction converted the route from generic classification into four concrete spectral-identification subtasks.
- first baseline signal: `baseline-observations.md` shows category recognition is much easier than origin recognition, and Q3 fusion improves the simple baseline.

## Required Repo Write-Back

- file to update: pending
  why: decide after the first generated attempt exposes a real route, evidence, writing, or review weakness.

## Next Decision

- keep current route family guidance unchanged / refine it / split it further: pending after draft review
- run another pressure test on the same family or move to a different family: likely move to monitoring-route E if missing problem statement is found
- recommended next target problem type: monitoring-route E, because it tests decision closure after diagnosis

## Immediate Next Step

- follow `runs/calibration-2021E-classification/pressure-test-next-steps.md`;
- execute the route comparison in `model-candidates.md`;
- do not start full paper drafting until the minimum diagnostic figures and comparison tables exist.
- use `runs/calibration-2021E-classification/baseline-observations.md` as the floor that stronger models must beat.
