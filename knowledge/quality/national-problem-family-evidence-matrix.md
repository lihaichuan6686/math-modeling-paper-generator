# National Problem-Family Evidence Matrix

Purpose: map common CUMCM problem families to the minimum evidence a reviewer should expect before trusting the paper's main claims.

This note is the bridge between:

- family-level methodology;
- generic evidence families;
- review decisions about whether a result is actually proven or only narrated.

Use this file when:

- `artifact-ledger.md` feels complete but the paper still looks under-proven;
- the review needs to know what kind of proof burden belongs to this family;
- the paper has many artifacts, but it is unclear whether they are the right artifacts.

## How To Use

1. Identify the primary problem family.
2. Check the required evidence row below.
3. Verify that the paper contains at least one artifact in each mandatory evidence slot.
4. Mark the run `Warn` or `Fail` if the family-specific proof burden is not met.

## Matrix

| Problem family | Minimum model evidence | Minimum decision evidence | Minimum validation evidence | Minimum comparison evidence | Weak evidence that should not be enough alone |
|---|---|---|---|---|---|
| Evaluation and ranking | indicator system and weighting logic | ranking or shortlisted recommendation | weight sensitivity or method comparison | alternative weighting/ranking comparison | one final score table with no stability check |
| Evaluation to planning | candidate-to-plan model link | executable plan table | feasibility audit | baseline or scenario comparison | ranking table plus one plan screenshot |
| Forecast to decision | forecast model and error evidence | decision table under forecast | out-of-sample or rolling error | scenario or uncertainty propagation comparison | one forecast curve with no error table |
| Classification and recognition | feature and split policy | thresholded judgment rule or classifier outcome table | confusion evidence and multi-metric evaluation | baseline classifier or threshold comparison | one AUC or accuracy number |
| Geometry and engineering mechanics | coordinate/physical model derivation | numeric design/result table | residual or feasibility evidence | parameter or design comparison | one final parameter answer without scene or residual proof |
| Production planning and scheduling | planning model with constraints | schedule/production table | capacity or rule-feasibility audit | abnormal-scenario or rolling comparison | quantity list with no feasibility evidence |
| Graph and network | reproducible node-edge/path construction | chosen route/layout/coverage table | bottleneck, connectivity, or capacity audit | baseline path/layout comparison | route list with no network construction evidence |
| Queue and service systems | queue/service mechanism model | staffing/service recommendation | waiting/utilization or bottleneck check | peak vs non-peak or before/after comparison | average metric summary only |
| Experimental factor optimization | fitted factor-response model | optimal-condition table | domain or residual validation | alternative factor-level or local comparison | one optimum point with no domain check |
| Rail / timetable service planning | service-pattern and recurrence logic | selected plan and timetable artifact | capacity/tracking/dwell audits | candidate-plan or scenario comparison | timetable figure only |
| Production-route E | forecast-to-production logic | executable production table | service-level/inventory/support audit | scenario/capacity comparison | demand forecast with no production consequence |
| Monitoring-route E | diagnosis-to-policy logic | monitoring or policy scheme table | intervention, trigger, or long-horizon consequence evidence | policy or intervention comparison | stacked diagnostic plots with no policy artifact |

## Family-Specific Review Prompts

### Evaluation and ranking

Ask:

- Can the reader see why the top-ranked option remains credible if weights move?
- Is the recommendation more than a raw ranking?

### Evaluation to planning

Ask:

- Does the candidate layer truly feed the plan?
- Can the plan be executed under the stated constraints?

### Forecast to decision

Ask:

- What happens to the decision if forecast error gets worse?
- Is the decision artifact visible, not just the forecast?

### Classification and recognition

Ask:

- What threshold or decision rule is the paper really using?
- Can the reviewer see false positives and false negatives, not only summary accuracy?

### Geometry and engineering mechanics

Ask:

- Is the scene or coordinate frame visible before optimization?
- Is the final answer feasible in the physical or geometric sense?

### Production planning and scheduling

Ask:

- Is there a real executable table?
- What happens under abnormal capacity, demand, or rolling updates?

### Graph and network

Ask:

- Can the graph or network be reconstructed from the paper?
- Where is the bottleneck or coverage proof?

### Queue and service systems

Ask:

- Are peak conditions checked?
- Is the recommendation supported by more than average values?

### Experimental factor optimization

Ask:

- Is the optimum inside the valid domain?
- Are residuals or significance checks visible?

### Rail / timetable service planning

Ask:

- Is there a machine-readable timetable artifact?
- Are service claims audited through capacity, tracking, and dwell evidence?

### Production-route E

Ask:

- How does the forecast become a production rule or quantity table?
- Where is the service or support consequence evidence?

### Monitoring-route E

Ask:

- How do the diagnostics close into a monitoring rule or policy decision?
- Where is the intervention or long-horizon consequence evidence?

## Best Use

Read this note together with:

- `evidence-family-index.md`
- `quality-rubric-v2.md`
- `../cumcm/national-problem-family-methodology-matrix.md`
- `../latex/national-problem-family-visual-matrix.md`
- `../../docs/review-checklist.md`
