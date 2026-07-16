# Pressure-Test Next Steps: 2021E

Purpose: define the next executable steps for the classification-recognition calibration run.

This is not a paper-generation checklist. It is a route-calibration checklist.

## Step 1: Build Data Tables

- Load each attachment into a stable data table.
- Split labeled rows and target rows.
- Record target IDs:
  - Q2 `OP`: 3, 14, 38, 48, 58, 71, 79, 86, 89, 110, 134, 152, 227, 331, 618.
  - Q3 `OP`: 4, 15, 22, 30, 34, 45, 74, 114, 170, 209.
  - Q4 `Class/OP`: 94, 109, 140, 278, 308, 330, 347.
- Verify no target row participates in supervised fitting.

## Step 2: Produce Minimum Diagnostic Figures

Required before drafting:

- representative MIR and NIR spectra;
- preprocessing-effect comparison;
- feature-representation or selected-band figure;
- classifier comparison table;
- confusion matrix or per-label error table;
- Q3 band-fusion comparison.

## Step 3: Run Route Comparison

Minimum comparison:

```text
baseline route
-> preprocessing + feature-selection route
-> selective fusion/hierarchy route
```

Do not accept a route unless it answers:

- Which preprocessing changed the evidence?
- Which features or components carry separation?
- Which model wins under the same split?
- Which classes or origins remain weak?

## Step 4: Write A Calibration Review Before Any Full Paper

The first review should decide whether the scaffold failed by:

- `claim_overreach`
- `validation_gap`
- `artifact_gap`
- `paragraph_density_misfit`
- `review_gate_miss`

## Step 5: Repo Write-Back

After the first model attempt, update at least one durable guidance file:

- `docs/sample-run-packages/classification-recognition-demo/`
- `docs/run-file-examples/classification-recognition-demo/`
- `knowledge/quality/national-problem-family-evidence-matrix.md`
- `knowledge/latex/national-problem-family-paragraph-density-playbook.md`

The update should be based on an observed failure or confirmed success from this run, not on speculation.
