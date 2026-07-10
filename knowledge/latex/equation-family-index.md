# Equation Family Index

Purpose: map common CUMCM equation families to their first job in the paper.

This note helps equation planning before drafting the model section.

## Equation Families At A Glance

| Equation family | First job | Typical section | Common form | Typical caption or explanation focus |
|---|---|---|---|---|
| Objective equation | state the optimization target | model establishment | minimize cost, loss, error, or deviation | what the model is trying to improve |
| Constraint equations | define feasible decisions | model establishment | capacity, balance, nonnegativity, logic, or resource bounds | what makes the plan valid |
| Score / weighting equation | combine indicators into one signal | model establishment or data processing | weighted sum, entropy, TOPSIS-style distance | how heterogeneous indicators are merged |
| Forecast equation | describe trend or prediction logic | data processing or model establishment | regression, time-series, fitted value, interval | how historical data become future estimates |
| Classification equation | define feature-to-label mapping | model establishment | discriminant, classifier score, probability rule | how categories are separated |
| Geometry / physics equation | express spatial or physical relation | model establishment | distance, angle, balance, residual, force relation | how the object is represented mathematically |
| Validation equation | measure error or feasibility | validation | residual, deviation, sensitivity, violation | how credibility is checked |
| Update equation | revise a plan or state | solution process | rolling horizon, recurrence, state transition | how the model changes over time |

## First Equation Rule

The first strong equation should usually do one of these jobs:

1. state the objective;
2. define the core score;
3. define the spatial/physical relation;
4. define the update rule.

Do not start with an equation that the paper never returns to.

## Equation-Table Pairing Rule

Where possible, pair equation families with a table companion:

- objective equation -> parameter table;
- constraint equations -> variable/parameter table;
- score equation -> indicator table;
- forecast equation -> data table or feature table;
- classification equation -> preprocessing table;
- geometry equation -> object schematic and parameter table;
- validation equation -> validation table;
- update equation -> baseline/adjusted plan table.

## Equation Numbering Rule

Use equation labels only when the equation is referenced later:

```text
\label{eq:objective}
\label{eq:capacity}
\label{eq:update-rule}
```

Avoid numbering decorative formulas that do not participate in the argument chain.

## Planning Rule

When building `paper/main.tex` and `paper/sections/`, place equations in this order:

```text
objective -> constraints -> score/forecast/classifier -> update/validation
```

## Best Use

Read this note together with:

- `figures-tables-equations-style.md`
- `section-map.md`
- `table-family-index.md`
- `visual-family-index.md`

