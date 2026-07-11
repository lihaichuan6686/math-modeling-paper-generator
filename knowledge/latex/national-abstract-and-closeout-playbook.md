# National Abstract And Closeout Playbook

Purpose: give Claude Code reusable abstract skeletons, subquestion close-out patterns, and paragraph-ending moves for high-frequency CUMCM families.

Use this after section budgeting and before finalizing `runs/current/writing-style-plan.md`, the abstract, or the end of each subquestion section.

## Why This Matters

A draft often feels machine-like not because the methods are wrong, but because:

- the abstract names methods without closing results;
- subquestion sections stop at a table or figure and never close the loop;
- transitions between subquestions are abrupt;
- conclusions repeat headings instead of making a judgment.

This note fixes those problems at sentence level.

## Global Abstract Skeleton

Use this generic order:

```text
overall task
-> subquestion 1 method and result
-> subquestion 2 method and result
-> subquestion 3 method and result
-> validation or comparison
-> final recommendation / overall finding
```

Do not let the abstract stop at:

```text
background -> methods -> keywords
```

## Family Abstract Skeletons

### 1. Evaluation to Planning

Abstract skeleton:

```text
To solve the supplier / scheme selection and executable planning problem, we first construct an evaluation system to screen and rank candidates. Based on the resulting score structure, we then build a planning model to determine the final quantities / assignments / schedules. The obtained plan satisfies the main capacity and demand constraints and remains stable under scenario or sensitivity checks. Therefore, the recommended strategy is ...
```

Best closing move:

- end with the executable recommendation, not with the ranking.

### 2. Forecast to Decision

Abstract skeleton:

```text
To address the future-demand-driven decision problem, we first analyze the historical trend and build a forecasting model for the key variable. The forecast result is then fed into a downstream decision model to obtain the recommended strategy under the expected operating condition. Scenario comparison or residual/backtest analysis shows that the strategy remains credible within the tested uncertainty range. Therefore, the final recommendation is ...
```

Best closing move:

- end with what the forecast changes in the decision layer.

### 3. Geometry / Spatial Design

Abstract skeleton:

```text
For the spatial design / positioning / coverage problem, we establish a coordinate description of the target scene and derive the required geometric relations for each subquestion. Based on the resulting model, we obtain the final location / adjustment / coverage design and evaluate its feasibility through replay, residual, or overlap checks. The results show that the proposed configuration satisfies the main geometric requirement, so the final design suggestion is ...
```

Best closing move:

- end with the design meaning, not with the last formula.

### 4. Dynamic Scheduling / Update

Abstract skeleton:

```text
For the scheduling problem with dynamic disturbance, we first construct a baseline scheduling model and obtain the initial execution plan. We then design an update rule or rolling adjustment mechanism to revise the plan under the abnormal scenario. Comparison of cost / delay / utilization before and after adjustment shows that the revised strategy better preserves system performance under disturbance. Thus, the final operational recommendation is ...
```

Best closing move:

- end with what the update preserved or improved.

### 5. Classification / Recognition

Abstract skeleton:

```text
For the recognition / diagnosis problem, we first preprocess the raw samples and construct effective feature representations. We then compare multiple classifiers and select the model with the best overall recognition behavior. Confusion-level or error analysis shows that the selected route remains reliable across the major classes. Therefore, the final diagnostic / recognition conclusion is ...
```

Best closing move:

- end with the actual diagnostic implication, not only accuracy.

### 6. Rail / Timetable Service Planning

Abstract skeleton:

```text
For the rail transit service planning problem, we first analyze passenger-flow characteristics and design candidate service patterns. On this basis, we determine the selected operation plan and generate the corresponding timetable through the recurrence constraints. Capacity, tracking, and dwell audits confirm the feasibility of the final plan, and scenario analysis further clarifies its service-cost tradeoff. Therefore, the recommended timetable strategy is ...
```

Best closing move:

- end with the recommended service pattern or timetable policy.

## Subquestion Close-Out Pattern

At the end of each subquestion section, prefer this four-step close:

```text
what the artifact shows
-> what decision / conclusion it supports
-> what check confirms it
-> what the next subquestion needs from it
```

Example shape:

```text
Table~\ref{tab:q1_plan} shows that the selected suppliers can satisfy the weekly demand without exceeding capacity. This means the candidate set is sufficient for the downstream ordering problem. The feasibility audit in Table~\ref{tab:q1_audit} further confirms that no constraint is violated under the tested scenario. Therefore, the derived supplier set is used as the fixed input for the ordering model in the next subquestion.
```

## Family-Specific Close-Out Moves

### Evaluation to Planning

Close with:

- the ranking/planning bridge;
- the plan feasibility meaning;
- the exact input passed to the next layer.

### Forecast to Decision

Close with:

- the forecast implication;
- the decision change caused by the forecast;
- the scenario or residual caveat.

### Geometry / Spatial Design

Close with:

- what the derived geometry means physically;
- whether the design is feasible;
- which symbol or configuration continues forward.

### Dynamic Scheduling / Update

Close with:

- the baseline/adaptation comparison;
- what was improved or protected;
- the trigger passed to the next part.

### Classification / Recognition

Close with:

- which classes are well recognized;
- where the errors remain;
- why the selected classifier is still used.

### Rail / Timetable Service Planning

Close with:

- what the service pattern achieves;
- how the timetable or audit confirms it;
- what operating recommendation follows.

## Transition Sentence Moves

When moving between subquestions, use transitions like:

- `The above result resolves the candidate-selection layer; the next task is to convert it into an executable allocation rule.`
- `After determining the forecast interval, the next step is to quantify how this uncertainty changes the final decision.`
- `With the coordinate relation now fixed, the remaining question is how to obtain the final design under the stated constraint set.`

Avoid weak transitions like:

- `Next, we solve Question 2.`

## Conclusion Sentence Moves

For the final conclusion, prefer:

- `In summary, the proposed route not only answers each subquestion but also yields an executable / feasible / interpretable final strategy.`
- `Within the tested scenario range, the recommended solution remains stable enough for research review and subsequent human verification.`

Avoid:

- `The model is scientific and effective.`

## Best Use

Read this note together with:

- `section-writing-patterns.md`
- `human-style-soft-rules.md`
- `national-family-section-budget-playbook.md`
- `local-awarded-paper-structure-rules.md`
- `../../docs/writing-style-plan-template.md`
