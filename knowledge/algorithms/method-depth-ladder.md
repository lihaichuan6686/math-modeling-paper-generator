# Method Depth Ladder

Purpose: prevent the generator from stopping at shallow single-method answers when the target is a contest-grade paper.

This note is about method depth, not method prestige.

## Core Rule

A stronger paper is usually not built by choosing a fancier algorithm name.

It is built by giving each subquestion a deeper chain:

```text
signal
-> main model
-> support layer
-> result
-> check layer
```

## Depth Levels

| Level | Shape | Typical quality |
|---|---|---|
| Level 0 | method name only | too shallow for v1.2 |
| Level 1 | method -> result | can pass a demo, often weak in review |
| Level 2 | preprocessing/support -> main model -> result | structurally acceptable |
| Level 3 | preprocessing/support -> main model -> result -> validation/comparison | v1.2 target |
| Level 4 | route chain -> multiple linked methods -> executable decision -> validation -> limitation discussion | award-leaning pattern |

## Preferred v1.2 Minimum

For most subquestions, aim for Level 3:

- one main model;
- one support layer such as preprocessing, feature construction, ranking, decomposition, or parameter estimation;
- one result artifact;
- one validation, sensitivity, or baseline comparison layer.

## Example Upgrades

### Evaluation route

Too shallow:

```text
TOPSIS -> ranking
```

Better:

```text
indicator construction -> TOPSIS -> supplier ranking -> integer plan -> sensitivity to weights
```

### Forecast route

Too shallow:

```text
ARIMA -> forecast curve
```

Better:

```text
data cleaning -> forecast model -> decision rule -> scenario comparison -> service-level consequence
```

### Classification route

Too shallow:

```text
SVM -> accuracy
```

Better:

```text
preprocessing -> dimension reduction -> classifier comparison -> confusion matrix -> error analysis
```

### Geometry route

Too shallow:

```text
optimization -> best parameter
```

Better:

```text
coordinate setup -> constrained optimization -> geometric figure -> residual map -> sensitivity check
```

## Anti-Prestige Rule

Do not upgrade depth by stacking advanced names with no route role.

Bad upgrade:

```text
LSTM + XGBoost + GA + ACO
```

Good upgrade:

```text
forecast
-> planning
-> scenario audit
```

## Best Use

Read this note together with:

- `README.md`
- `model-chain-patterns.md`
- `route-method-matrix.md`
- `../cumcm/official-paper-paradigms.md`
- `../../docs/v1.2-runbook.md`

