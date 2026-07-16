# Route Decision

Run: calibration-2021E-classification

Read knowledge/algorithms/route-selection-protocol.md and prompts/01_ideation.md before completing this file.

## Selected Route Family

classification-recognition.

## Question Map

- Q1 category recognition from Attachment 1 mid-infrared spectra.
- Q2 origin recognition from Attachment 2 mid-infrared spectra, including 15 target IDs.
- Q3 origin recognition from Attachment 3 near-infrared plus mid-infrared spectra, including 10 target IDs.
- Q4 category and origin recognition from Attachment 4 near-infrared spectra, including 7 target IDs.

## Route Chain By Subquestion

### Subquestion 1: Category Recognition

Chain:

```text
Attachment 1 MIR spectrum
-> spectral preprocessing and exploratory curves
-> feature/band extraction
-> category-separation evidence
-> category-recognition rule
```

### Subquestion 2: Single-Band Origin Recognition

Chain:

```text
Attachment 2 MIR spectrum with observed OP
-> labeled/target row split
-> preprocessing and feature representation
-> classifier comparison for OP
-> fill 15 missing OP results
```

### Subquestion 3: Two-Band Origin Recognition

Chain:

```text
Attachment 3 NIR and MIR spectra with observed OP
-> band-specific preprocessing
-> band-level classifier comparison
-> fusion or agreement rule
-> fill 10 missing OP results
```

### Subquestion 4: Category And Origin Recognition

Chain:

```text
Attachment 4 NIR spectrum with partial Class and OP
-> class model and OP model
-> class-origin consistency check
-> fill 7 target Class/OP pairs
-> bounded reliability statement
```

## Why This Route Fits The Decision Object

- The end product is an identification rule, so a classifier alone is not enough.
- The decision object requires evidence that the rule works across classes, not merely that the overall score is high.
- The route directly tests whether v1.3 forces preprocessing, representation, comparison, and class-level review into one chain.
- The problem escalates from category recognition to origin recognition to two-band fusion, which makes it a strong pressure test for route closure.

## Why Rejected Routes Are Weaker

- Pure regression is weaker because the main output is categorical identification.
- Pure clustering is weaker unless labels are absent or unreliable; the available excellent-paper pattern treats this as supervised recognition.
- Forecast-to-decision is not the correct family because there is no future time axis driving a downstream policy decision.
- Evaluation-to-planning is too broad unless the problem explicitly asks for ranking or resource allocation after classification.

## Required Evidence Chain

- input-file inventory;
- label definition and split policy;
- preprocessing comparison or explicit justification;
- feature representation evidence;
- at least two classifier baselines;
- confusion matrix or per-class metrics;
- final target-ID answer tables;
- final claim-boundary statement.

## Required Visuals

- feature/spectrum overview;
- preprocessing effect chart;
- reduced-feature scatter, feature importance, or component plot;
- classifier comparison table;
- confusion matrix or class-level diagnostic.
- band-fusion comparison figure or table for Q3.

## Expected Failure Modes

- `claim_overreach`: conclusion claims broad recognition without class-level support.
- `validation_gap`: split policy or baseline comparison is missing.
- `artifact_gap`: no visible preprocessing or feature-reduction evidence.
- `paragraph_density_misfit`: method sections become lists instead of evidence loops.
- `review_gate_miss`: review accepts one high score as sufficient.
