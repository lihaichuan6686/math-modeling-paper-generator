# CUMCM Atlas

Purpose: provide a single navigation page for the long-term CUMCM knowledge base. This file is the index layer that connects problem types, algorithm cards, LaTeX rules, paper-reading notes, and the next iteration plan.

## How To Use

1. Identify the problem type or route family first.
2. Jump to the matching route notes and algorithm cards.
3. Use the page blueprint to budget evidence, not prose.
4. Use the review rubric to reject fake completion signals.
5. Use the iteration plan to decide what to read or build next.

## Route Index

### Evaluation And Ranking

Typical signs:

- many indicators;
- no direct physical law;
- result must still feed a recommendation or plan.

Core artifacts:

- [problem-type-paper-archetypes.md](problem-type-paper-archetypes.md)
- [deep-reading-2021C066.md](deep-reading-2021C066.md)
- [2021C-comparison-C066-C085-C169-C283.md](2021C-comparison-C066-C085-C169-C283.md)
- algorithm cards: `ahp.md`, `entropy-weight.md`, `topsis.md`, `pca-lda.md`

Required evidence:

- indicator table;
- weight or score table;
- ranking table;
- sensitivity or stability check.

### Evaluation To Planning

Typical signs:

- ranking or screening is only the first stage;
- final answer must be executable.

Core artifacts:

- [deep-reading-2021C066.md](deep-reading-2021C066.md)
- [2021C-comparison-C066-C085-C169-C283.md](2021C-comparison-C066-C085-C169-C283.md)
- algorithm cards: `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md`, `graph-algorithms.md`

Required evidence:

- selected candidate table;
- executable plan table;
- feasibility audit;
- baseline comparison.

### Forecast To Decision

Typical signs:

- historical data;
- forecast must drive a decision;
- uncertainty should propagate.

Core artifacts:

- [deep-reading-2022E014.md](deep-reading-2022E014.md)
- [deep-reading-2022E029.md](deep-reading-2022E029.md)
- [deep-reading-2023E176.md](deep-reading-2023E176.md)
- [e-route-comparison-2022-2023.md](e-route-comparison-2022-2023.md)
- algorithm cards: `time-series.md`, `regression.md`, `simulation.md`

Required evidence:

- historical trend figure;
- model comparison table;
- forecast table;
- decision table under scenarios.

#### Production-Route E

Best-fit cases:

- demand, service level, inventory, support rate, or production quantity decisions.

Key lessons:

- [2022 E014](deep-reading-2022E014.md) shows conservative service-level-first planning;
- [2022 E029](deep-reading-2022E029.md) shows dynamic forecasting-to-production planning;
- [2024B-modern-draft-risk-reading.md](2024B-modern-draft-risk-reading.md) warns that page count and code appendices can fake completeness.

#### Monitoring-Route E

Best-fit cases:

- diagnosis, monitoring, policy, intervention, or long-horizon consequence decisions.

Key lessons:

- [2023 E176](deep-reading-2023E176.md) shows layered diagnosis to policy design;
- [2024E-modern-draft-risk-reading.md](2024E-modern-draft-risk-reading.md) warns that traffic-control papers need a stable question map and a visible action layer.

### Classification Or Recognition

Typical signs:

- labels or categories;
- feature extraction and model comparison matter;
- evaluation needs confusion-level evidence.

Core artifacts:

- algorithm cards: `random-forest.md`, `svm.md`, `pca-lda.md`
- routing rules: `model-chain-patterns.md`, `problem-type-to-method.md`

Required evidence:

- preprocessing table;
- feature table;
- model comparison table;
- error-analysis figure or confusion matrix.

### Geometry And Engineering Mechanics

Typical signs:

- coordinate frame;
- physical relation;
- visible geometry before optimization.

Core artifacts:

- [deep-reading-2021A028.md](deep-reading-2021A028.md)
- [2024D-modern-draft-risk-reading.md](2024D-modern-draft-risk-reading.md)
- algorithm cards: `simulation.md`, `nonlinear-programming.md`, `response-surface.md`

Required evidence:

- schematic figure;
- variable and unit table;
- formula-to-number closure;
- feasibility or stability check.

### Online Optimization And Process Update

Typical signs:

- baseline plan;
- abnormal event or update trigger;
- revised plan;
- comparison of initial and adjusted outcomes.

Core artifacts:

- [deep-reading-2021D017.md](deep-reading-2021D017.md)
- [2021D-comparison-D017-D026-D034.md](2021D-comparison-D017-D026-D034.md)
- algorithm cards: `linear-integer-programming.md`, `dynamic-programming.md`, `simulation.md`

Required evidence:

- baseline table;
- adjusted table;
- loss or cost comparison;
- explanation of reuse across scenarios.

## LaTeX Index

Use these documents when writing or checking layout:

- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `knowledge/latex/section-writing-patterns.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`

The practical rule is simple:

```text
object first -> evidence second -> decision third -> validation fourth
```

## Quality And Risk Index

Use these documents when checking whether a draft is truly complete:

- `knowledge/quality/quality-rubric-v2.md`
- `docs/review-checklist.md`
- `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
- `knowledge/cumcm/2024B-modern-draft-risk-reading.md`
- `knowledge/cumcm/2024C-modern-draft-risk-reading.md`
- `knowledge/cumcm/2024D-modern-draft-risk-reading.md`
- `knowledge/cumcm/2024E-modern-draft-risk-reading.md`

Current risk gates to remember:

- stable question map;
- effective body length, not inflated PDF length;
- object-first explanatory figure;
- method-to-output closure;
- screenshot-only evidence rejection;
- residue and placeholder rejection.

## Iteration Plan

### v1 Current State

- paper-generation workflow exists;
- review gates now include fake-completion checks;
- route families for E papers are split;
- same-problem comparisons exist for 2021 C and 2021 D;
- modern-draft risk notes exist for 2024 B/C/D/E;
- an official-versus-risk synthesis note links the two halves together.

### Next Best Work

1. Test the strengthened prompts and review gates on a fresh real problem run.
2. Add more same-problem comparisons for one A/B/C route family.
3. Continue route coverage for any gap that still lacks a high-quality official anchor.
4. Extend the LaTeX side with more concrete section-writing patterns if a draft reveals a recurring weakness.
5. Once a fresh run exists, compare its artifact ledger against this atlas and tighten any missing gate.

## Companion Plan

- [next-iteration-plan.md](next-iteration-plan.md)

## Status

This atlas is a navigation layer, not a final paper artifact. It should be updated whenever a new route anchor, comparison note, or quality gate becomes important enough to change how the generator is used.
