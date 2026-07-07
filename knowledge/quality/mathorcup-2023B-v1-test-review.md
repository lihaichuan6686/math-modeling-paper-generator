# MathorCup 2023 B v1 Test Review

Date: 2026-07-07

Reviewed material:

- Problem: `D:\math-modeling-paper-generator\2023年MathorCup高校数学建模挑战赛B题.pdf`
- Generated paper: `D:\math-modeling-paper-generator\paper\main.pdf`
- Generated source and evidence: `D:\math-modeling-paper-generator\paper\`, `D:\math-modeling-paper-generator\runs\current\`
- Excellent-paper references: `B题优秀论文-1.pdf`, `B题优秀论文-2.pdf`, `B题优秀论文-3.pdf`

## Overall Judgment

The v1 output is a real closed-loop draft, not just a shell. It reads the attachments, generates a 17-page LaTeX paper, produces Q1 and Q2 Excel outputs, creates section-flow, OD, Pareto, timetable, and sensitivity figures, and gives concrete operation-plan numbers.

However, compared with the three excellent papers, it is still at "demo paper" level. The main gap is not basic structure; the structure is already recognizable. The gap is the rigor, auditability, and contest-style depth of the model chain.

The excellent papers are 34-39 pages. Their density comes from detailed model decomposition, explicit constraint groups, algorithm explanation, richer result tables, running-diagram logic, and quantitative recommendation experiments. The generated v1 paper has the right skeleton but compresses too many important contest-scoring elements into short paragraphs.

## What Already Works

1. Complete route coverage: the draft addresses Q1 operation planning, Q2 equal-interval timetable generation, and Q3 improvement suggestions.
2. Evidence artifacts exist: `q1_output.xlsx`, `q2_timetable.xlsx`, figures, LaTeX tables, and an artifact ledger are generated.
3. The core problem decomposition is directionally right: section-flow analysis, small-route candidate search, cost-service tradeoff, timetable construction, and sensitivity analysis.
4. The paper includes real quantitative outputs, for example big/small route trains, overlap headway, train-km, service time, tracking-interval checks, and demand sensitivity.

## Major Gaps Against Excellent Papers

### 1. Method strength is too modest for the title-level impression

Excellent paper 1 frames the solution around NSGA-II plus TOPSIS from the title and abstract. It presents the method as a multi-objective optimization problem, then uses TOPSIS to select from the Pareto set.

The v1 paper uses enumeration plus a weighted score. This is useful and transparent, but the paper does not make it feel like a strong mathematical modeling method. If enumeration is kept, it needs to be justified as exhaustive search over a small discrete feasible space and paired with Pareto dominance/TOPSIS or entropy-weighted scoring.

### 2. Objective functions need business decomposition

Excellent paper 2 decomposes cost into interpretable pieces such as vehicle operation, standby/maintenance allocation, train-kilometers, and variable operating cost. The v1 draft reports normalized cost and train-km, but the reader cannot fully audit what "0.7388" means.

Needed:

- fixed cost, fleet-use cost, and train-km variable cost;
- passenger service level split into waiting time, in-vehicle time, transfer/penalty time if applicable;
- normalization formula and weight-selection rationale;
- a final table showing raw metrics before normalized ranking.

### 3. Constraint system is under-explained

Excellent papers spell out constraints in separate groups: frequency/headway bounds, station dwell-time bounds, minimum tracking interval, capacity constraints inside and outside the small route, ratio constraints for big/small route operation, and integer constraints.

The v1 draft has constraints, but the explanation is thinner and less auditable. The reader should be able to check each generated plan against each constraint group.

Required table:

| Constraint group | Formula or rule | Data source | Selected plan value | Pass/fail |
| --- | --- | --- | --- | --- |

### 4. Q2 timetable is present but not contest-grade

The v1 run generated `q2_timetable.xlsx` and a timetable figure, which is important. But the paper body does not yet sufficiently prove how the timetable follows from Q1.

Excellent paper 3 treats Q2 as a separate running-diagram construction problem: it explains how Q1 determines train types and intervals, how station running times and dwell times are used, how tracking constraints are enforced, and how the final timetable is exported.

Needed:

- station-by-station arrival/departure recurrence;
- dwell-time calculation tied to boarding/alighting flow;
- explicit tracking-interval correction logic;
- sample timetable for representative trains plus full attachment output;
- feasibility audit across all stations and all adjacent train pairs;
- Chinese-labeled running diagram, preferably with big/small-route trains visually separated.

### 5. Q3 recommendations need experiment tables

The v1 draft gives quantitative suggestions, but they are still too narrative. Excellent-paper style requires each suggestion to be backed by an experiment, a comparison baseline, and an interpretation.

Required scenario table:

| Strategy | Changed parameter | Cost change | Service change | Capacity risk | Recommendation |
| --- | --- | --- | --- | --- | --- |

Suggested scenarios:

- demand plus/minus 10% and 20%;
- headway from 120s to 360s;
- alternate small-route start/end stations;
- different big/small route ratios;
- dwell-time cap or passenger-exchange assumptions.

### 6. Self-review is too permissive

`runs/current/artifact-ledger.md` marks the run as pass, while `reviews/review-current.md` still says "Needs revision" and is not filled in. This is a serious workflow issue.

The review gate must fail if:

- review sections are empty;
- artifact ledger says pass but no independent evidence was checked;
- generated paper is below the required page target without a documented reason;
- Q1/Q2 required output files are absent or not referenced;
- figures use English labels in a Chinese contest paper;
- references are too few or not method-specific.

### 7. Formatting and presentation need contest polish

The generated paper has a clean LaTeX structure, but several details reduce paper quality:

- 17 pages is short compared with the excellent-paper range of 34-39 pages and the target 20-30 pages;
- figures have English axes/titles and small labels;
- some tables are compact but not deeply interpreted;
- references are too few;
- appendices/code inventory are not yet strong enough;
- the abstract is structured but should more clearly state model names, constraints, and final outputs for each subproblem.

## v1.1 Improvement Tasks

1. Add a rail-timetable problem archetype:
   `problem -> passenger-flow analysis -> big/small route planning -> Pareto/TOPSIS selection -> equal-interval timetable -> feasibility audit -> operation suggestions`.

2. Add mandatory artifacts for timetable problems:
   `q1_operation_plan.xlsx`, `q2_timetable.xlsx`, `capacity_audit.csv`, `tracking_audit.csv`, `scenario_analysis.csv`, and a full artifact ledger.

3. Upgrade Q1 model:
   exhaustive candidate enumeration plus Pareto filtering plus TOPSIS/entropy-weight ranking, with all objective components shown before normalization.

4. Upgrade Q2 model:
   station arrival/departure recurrence, dwell-time from boarding/alighting flow, tracking-interval correction, and complete feasibility audit.

5. Upgrade Q3:
   scenario experiments and a recommendation table, not only prose suggestions.

6. Upgrade paper-generation prompt:
   force each question to have "model construction -> solution algorithm -> result table/figure -> validation" instead of jumping from method to answer.

7. Upgrade quality review:
   make the review prompt inspect generated Excel files, source code assumptions, figure language, page count, empty review fields, and contradiction between ledger and review status.

## Priority Fix for the Next Work Block

Build a dedicated `rail_timetable` example route in the generator. This should become the first real v1.1 case because it has already exposed the toolchain's weakest points: multi-objective rigor, timetable recurrence, feasibility auditing, and result-to-paper explanation.
