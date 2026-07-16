# Common Mistakes And Taboo Patterns

Purpose: prevent generated papers from sounding like weak contest submissions.

## Strategic Mistakes

### Template Forcing

Bad pattern:

```text
This looks like an optimization problem, so use a generic optimization model.
```

Repair:

```text
Name the decision object first, then choose the model.
```

### Advanced-Algorithm Decoration

Bad pattern:

```text
Use neural network / genetic algorithm / particle swarm because it sounds advanced.
```

Repair:

```text
Use a baseline, then justify the advanced method by comparison or necessity.
```

### Answer Chasing

Bad pattern:

```text
Online sources say a different number, so abandon the current route immediately.
```

Repair:

```text
Treat external numbers as sanity signals; inspect assumptions before changing route.
```

### Appendix Inflation

Bad pattern:

```text
Put most real work in appendix and leave the body vague.
```

Repair:

```text
Put main result, main table, and main validation in the body; appendix supports reproducibility.
```

## Writing Mistakes

### Method-Only Abstract

Bad pattern:

```text
We use A, B, and C models to solve the problem.
```

Repair:

```text
For each subquestion: method -> result -> answer.
```

### Ceremonial Validation

Bad pattern:

```text
The model is accurate and feasible.
```

Repair:

```text
State what was checked, what number or comparison supports it, and what remains weak.
```

### Generic Advantages

Bad pattern:

```text
The model has high accuracy, strong applicability, and good robustness.
```

Repair:

```text
Tie each advantage to one artifact: error table, comparison result, feasibility audit, or sensitivity result.
```

### Long Restatement Padding

Bad pattern:

```text
Rewrite the whole problem statement in different words.
```

Repair:

```text
Restate the task in modelable terms: inputs, outputs, decisions, constraints.
```

## Phrases To Avoid Or Control

Avoid unsupported:

- "显著提高"
- "具有较高准确性"
- "具有较强鲁棒性"
- "模型合理有效"
- "结果较好"
- "具有推广价值"

Allowed only when followed by evidence:

- comparison number;
- error value;
- sensitivity range;
- feasibility check;
- class-level or scenario-level result.

## Review Cues

Flag a draft when:

- the abstract has no numeric result;
- the conclusion introduces new claims;
- every section begins with the same mechanical phrase;
- validation is shorter than the result table it is supposed to justify;
- figures have captions like "Result chart" or "Model diagram";
- references are fewer than the methods and data sources require.
