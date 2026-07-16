# Batch 1 Calibration Candidate Selection

Purpose: choose the first concrete problems for methodology pressure testing without turning the work into one-off optimization for a single topic.

This note sits between:

- `../first-calibration-batch-plan.md`
- `../calibration-run-index.md`
- `../pressure-test-runbook.md`

It records which real local materials can support the first calibration run and which route family each candidate should test.

## Selection Rule

The first candidate should satisfy two conditions:

1. it stresses a reusable route family that matters for future papers;
2. it has enough local material to compare the generated run against a strong human paper.

When these conflict, prefer methodologically important candidates for planning, but use material-complete candidates for immediate execution.

## Candidate A: Monitoring-Route E

Status: preferred methodology target, not yet ready for full pressure test.

Route family:

```text
monitoring-route E
```

Why it matters:

- Monitoring and diagnosis papers are easy to make long but hard to make useful.
- The main reusable failure is `decision_object_missing`: the paper diagnoses data patterns but never turns them into a monitoring rule, sampling scheme, intervention comparison, or policy artifact.
- This route tests whether v1.3 can force prediction and diagnosis into a downstream decision object.

Current local anchor:

- `../../knowledge/cumcm/deep-reading-2023E176.md`
- local excellent-paper PDF observed in the 2023 E excellent-paper folder: `E176.pdf`

Observed human-paper pattern:

```text
data cleaning
-> seasonal and relation analysis
-> periodicity and abruptness diagnosis
-> trend prediction
-> monitoring-frequency optimization
-> policy-effect evaluation
```

Minimum evidence target:

- data-cleaning and aggregation pipeline;
- diagnostic artifact;
- prediction or trend evidence;
- monitoring or policy decision table;
- sensitivity or consequence comparison;
- claim-boundary note explaining what the monitoring rule does and does not prove.

Blocker before full pressure test:

- the matching problem statement PDF has not yet been located in the local truth-folder search.

Decision:

```text
Keep as Batch 1 Priority 1, but do not start a full pressure test until the problem statement is found or supplied.
```

## Candidate B: 2021 E Classification / Recognition

Status: running as the first executable calibration candidate.

Route family:

```text
classification-recognition
```

Why it matters:

- Classification papers often look polished while relying on one global score.
- The reusable failure is `claim_overreach`: the paper reports a high accuracy but does not explain preprocessing, split policy, class-level errors, or why the chosen classifier fits the data.
- This route tests whether v1.3 can force a full data-to-metric-to-interpretation chain.

Current local material:

- Problem statement: `CUMCM2021-E.pdf` in the local 2021 CUMCM problem folder.
- Attachments in the same folder: four `.xlsx` files for problem E.
- Extracted run notes:
  - `../../runs/calibration-2021E-classification/problem-brief.md`
  - `../../runs/calibration-2021E-classification/data-schema-summary.md`
  - `../../runs/calibration-2021E-classification/source-extraction.md`
- Deep-reading note: `../../knowledge/cumcm/deep-reading-2021E014.md`
- Excellent-paper anchors found locally:
  - `E014.pdf`
  - `E025.pdf`
  - `E037.pdf`

Expected human-paper pattern:

```text
raw spectrum or high-dimensional table
-> preprocessing comparison
-> feature extraction / reduction
-> classifier comparison
-> final class-level diagnosis
-> bounded identification conclusion
```

Minimum evidence target:

- explicit split or validation policy;
- preprocessing comparison;
- feature-reduction or feature-selection evidence;
- at least two classifier baselines;
- class-level error evidence such as confusion matrix or per-class metrics;
- conclusion wording that stays inside the tested sample scope.

Decision:

```text
Use this as the first executable Batch 1 pressure test while Candidate A remains blocked by missing problem statement material.
```

## Candidate C: Forecast-To-Decision

Status: second executable family after one E-route test.

Route family:

```text
forecast-to-decision
```

Why it matters:

- Forecasting routes are common and deceptively easy to complete.
- The reusable failure is `bridge_paragraph_missing`: forecast output exists, but no downstream decision changes because of it.

Candidate source:

- use the existing `sample-run-packages/forecast-to-decision-demo/` as the nearest package until a real local problem is selected.

Decision:

```text
Do not make this the first run unless both E-route candidates are blocked.
```

## Recommended First Move

Use this order:

1. Try to locate or receive the missing problem statement for the monitoring-route E anchor.
2. If found, start the monitoring-route E pressure test because it is the strongest stress test for decision closure.
3. If not found, start the 2021 E classification-recognition pressure test because it has a complete local problem package and multiple excellent-paper anchors.
4. Record the result in `../calibration-run-index.md` before any repo write-back.

## Minimum-Input Gate

Do not start a pressure test unless these are true:

| Gate | Candidate A | Candidate B |
|---|---|---|
| Problem statement exists | Missing | Ready and rendered |
| Attachments/data available | Unknown | Ready and schema-extracted |
| Route family selected | Ready | Ready |
| Nearest scaffold exists | Ready | Ready |
| Human-paper anchor exists | Ready | Ready |
| Failure signal named | Ready | Ready |

## Failure Buckets To Watch

Candidate A:

- `decision_object_missing`
- `artifact_gap`
- `bridge_paragraph_missing`
- `claim_overreach`
- `visual_role_misfit`

Candidate B:

- `claim_overreach`
- `validation_gap`
- `artifact_gap`
- `paragraph_density_misfit`
- `review_gate_miss`

## Write-Back Rule

After the first executable candidate finishes, at least one of these must happen:

- update the matching sample run package;
- strengthen a route-specific verification or figure plan;
- add a review-case example showing the failure;
- record a no-change decision with evidence in a calibration log.

The run is not useful if it only produces a paper-like output and no reusable repo learning.
