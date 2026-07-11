# National Family Section Budget Playbook

Purpose: give Claude Code family-level section-budget and abstract-closure guidance for strong CUMCM-style 20-30 page papers.

Use this after route selection and before finalizing `runs/current/section-budget.md` or drafting the abstract.

This file is a practical bridge from problem family to page rhythm.

## How To Use

1. identify the primary family;
2. copy the matching section-emphasis pattern into `runs/current/section-budget.md`;
3. copy the matching abstract closure pattern into `runs/current/writing-style-plan.md`;
4. check the result against `human-style-soft-rules.md` and `20-30-page-paper-blueprint.md`.

## Family Quick Map

| Family | Core page center | Section most likely to go thin | Abstract center | Best fix when short |
|---|---|---|---|---|
| Evaluation to planning | model establishment plus executable results | validation | score -> plan -> audit | add feasibility and scenario layers |
| Forecast to decision | data processing plus model establishment | decision interpretation | forecast -> decision -> uncertainty | add scenario propagation and decision contrast |
| Geometry / spatial design | model establishment plus scene explanation | result interpretation | scene -> derivation -> design result | add replay/feasibility interpretation |
| Dynamic scheduling / update | baseline model plus update logic | abnormal-scenario comparison | baseline -> update -> loss/result change | add before/after evidence |
| Classification / recognition | preprocessing plus model comparison | error interpretation | preprocessing -> classifier -> class-level result | add confusion and error analysis |
| Rail / timetable service planning | service design plus timetable feasibility | operation-to-timetable bridge | passenger flow -> service pattern -> timetable -> feasibility | add audit tables and scenario notes |

## Family Playbooks

### 1. Evaluation to Planning

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 1.0 | multiple subquestions usually need score, plan, and audit closure |
| Problem restatement + analysis | 2.5-3.5 | must explain why ranking alone is insufficient |
| Assumptions + symbols | 1.0-1.5 | decision variables and constraints need clear setup |
| Data processing | 2.0-3.0 | indicator construction and normalization need visible evidence |
| Model establishment | 5.0-7.0 | evaluation model and planning model both need mathematical body |
| Solution process | 2.0-3.0 | candidate flow and solver steps should be explicit |
| Results | 3.0-4.0 | candidate, selected, executable plan, and audit should all appear |
| Validation | 2.0-3.0 | feasibility and scenario checks are required |
| Conclusion + limitations | 1.0-1.5 | should close with executable recommendation |

Abstract closure pattern:

```text
problem goal
-> evaluation route and key ranking signal
-> planning model and executable decision result
-> feasibility or scenario validation
-> final recommendation
```

Soft rule:

- the abstract should not end at ranking;
- the body should feel longer in the planning layer than in the evaluation layer.

### 2. Forecast to Decision

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 1.0 | needs method-result closure for forecast and downstream decision |
| Problem restatement + analysis | 2.0-3.0 | must explain why uncertainty matters |
| Assumptions + symbols | 1.0-1.5 | forecast variables and decision variables need stable naming |
| Data processing | 3.0-4.0 | trend, seasonality, cleaning, and feature setup deserve space |
| Model establishment | 4.5-6.5 | forecast model plus decision model need separate but linked treatment |
| Solution process | 1.5-2.5 | scenario generation and parameter flow should be visible |
| Results | 2.5-3.5 | forecast result and decision result both need artifacts |
| Validation | 2.5-3.5 | backtest, residuals, and scenario propagation should be visible |
| Conclusion + limitations | 1.0-1.5 | must state both decision and uncertainty boundary |

Abstract closure pattern:

```text
problem goal
-> forecast model and key trend/result
-> decision model and chosen strategy
-> uncertainty or scenario validation
-> final policy / plan recommendation
```

Soft rule:

- if the abstract names a forecast, it should also name what that forecast changes downstream.

### 3. Geometry / Spatial Design

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 0.9-1.0 | should close every subquestion with geometric result, not just formulas |
| Problem restatement + analysis | 2.0-3.0 | must set the scene and task decomposition clearly |
| Assumptions + symbols | 1.0-1.5 | symbol world is crucial |
| Data / scene setup | 1.0-2.0 | often lighter than data-driven families but still needed |
| Model establishment | 6.0-8.0 | derivation is usually the technical center |
| Solution process | 2.0-3.0 | numerical steps, case split, or search process need explanation |
| Results | 2.5-3.5 | design/location outputs need visible presentation |
| Validation | 2.0-3.0 | replay, residual, overlap, or feasibility checks complete the route |
| Conclusion + limitations | 1.0-1.5 | should return to the scene and final design meaning |

Abstract closure pattern:

```text
scene and task
-> coordinate/geometry route
-> key design / positioning / coverage result
-> feasibility or replay validation
-> final engineering meaning
```

Soft rule:

- the abstract should mention the visible design or positioning result, not only derivation.

### 4. Dynamic Scheduling / Update

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 1.0 | baseline and adjusted plan both need closure |
| Problem restatement + analysis | 2.0-3.0 | must separate static and dynamic tasks |
| Assumptions + symbols | 1.0-1.5 | update triggers and decision variables should stay stable |
| Data processing | 1.5-2.5 | enough to define jobs, resources, and abnormal scenarios |
| Model establishment | 5.0-7.0 | baseline model plus update logic both need technical space |
| Solution process | 2.0-3.0 | algorithm or rolling logic is central |
| Results | 2.5-3.5 | baseline and revised schedules should both appear |
| Validation | 2.0-3.0 | before/after loss and constraint audit are required |
| Conclusion + limitations | 1.0-1.5 | should summarize update value, not only baseline quality |

Abstract closure pattern:

```text
task and disturbance setting
-> baseline scheduling method and initial result
-> update / adjustment method and revised result
-> constraint or loss comparison
-> final operational recommendation
```

Soft rule:

- if the body has an adjusted plan, the abstract should mention what improved or was preserved.

### 5. Classification / Recognition

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 0.9-1.0 | should include preprocessing and final recognition result |
| Problem restatement + analysis | 2.0-2.5 | task decomposition is usually more compact |
| Assumptions + symbols | 0.8-1.2 | lighter than optimization families |
| Data processing | 3.0-4.0 | preprocessing and feature construction deserve real space |
| Model establishment | 4.0-5.5 | classifier comparison and final model need technical body |
| Solution process | 1.5-2.5 | feature extraction and training flow should be explicit |
| Results | 2.0-3.0 | confusion-level and category-level findings need interpretation |
| Validation | 2.0-3.0 | split policy, leakage check, and error analysis are central |
| Conclusion + limitations | 1.0-1.5 | should state recognition quality with caveats |

Abstract closure pattern:

```text
task and data type
-> preprocessing / feature route
-> classifier and key recognition result
-> confusion/error validation
-> final diagnostic or recognition conclusion
```

Soft rule:

- do not let the abstract report one accuracy number without class-level interpretation in the body.

### 6. Rail / Timetable Service Planning

Recommended body rhythm:

| Section | Suggested pages | Why |
|---|---:|---|
| Abstract | 1.0 | service pattern, timetable result, and feasibility all need closure |
| Problem restatement + analysis | 2.5-3.5 | passenger-flow logic and route split need explanation |
| Assumptions + symbols | 1.0-1.5 | operation variables must stay consistent across sections |
| Data processing | 2.5-3.5 | OD, section flow, and parameter setup deserve visible space |
| Model establishment | 5.5-7.5 | service design objective and timetable recurrence need real depth |
| Solution process | 2.0-3.0 | selection logic and recurrence generation need explanation |
| Results | 3.0-4.0 | service plan and timetable outputs must both appear |
| Validation | 2.5-3.5 | capacity, tracking, dwell, and scenario checks are necessary |
| Conclusion + limitations | 1.0-1.5 | should summarize service-quality and cost tradeoff |

Abstract closure pattern:

```text
passenger-flow and service goal
-> operation-pattern design method
-> timetable generation result
-> capacity / tracking / dwell feasibility
-> final service recommendation
```

Soft rule:

- the abstract should not mention the timetable result without at least one feasibility phrase.

## General Abstract Density Rule

For these high-frequency families, the abstract should usually occupy one dense page because it needs:

- one opening sentence for the full problem;
- one method-result closure for each major subquestion;
- one validation or comparison sentence;
- one closing recommendation sentence.

If the abstract is short, first check whether one of those closures is missing.

## Best Use

Read this note together with:

- `human-style-soft-rules.md`
- `section-writing-patterns.md`
- `../cumcm/20-30-page-paper-blueprint.md`
- `../cumcm/national-priority-problem-playbook.md`
- `../../docs/section-budget-template.md`
