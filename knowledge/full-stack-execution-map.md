# Full Stack Execution Map

Purpose: show the shortest usable path from a problem statement to a review-ready CUMCM draft.

This is the top synthesis layer above the route, archetype, method, section, and quality bridges.

## Main Path

```text
problem signal
-> route index
-> archetype-section matrix
-> route-method matrix
-> section-family index
-> generation loop
-> finding-gate matrix
-> completion gate
```

## What Each Step Decides

| Step | Main question | Primary file |
|---|---|---|
| Route index | What route family does the problem belong to? | `cumcm/route-index.md` |
| Archetype section matrix | What section emphasis and first artifact does the archetype need? | `cumcm/archetype-section-matrix.md` |
| Route-method matrix | Which method family and first cards should be read? | `algorithms/route-method-matrix.md` |
| Section family index | What should each section do and what is the first artifact? | `latex/section-family-index.md` |
| Generation loop | How do route, section, artifacts, and writing connect? | `cumcm/generation-loop.md` |
| Finding-gate matrix | What gate should a weakness trigger and what evidence repairs it? | `quality/finding-gate-matrix.md` |
| Completion gate | Is the paper ready for research review? | `quality/completion-gate.md` |

## First Files To Read

If time is tight, read these first:

1. `cumcm/route-index.md`
2. `cumcm/archetype-section-matrix.md`
3. `algorithms/route-method-matrix.md`
4. `latex/section-family-index.md`
5. `cumcm/generation-loop.md`
6. `quality/finding-gate-matrix.md`
7. `quality/completion-gate.md`

## Output Ladder

The full-stack path should leave these artifacts in order:

```text
problem-analysis.md
data-inventory.md
model-candidates.md
model-plan.md
verification-plan.md
figure-plan.md
artifact-ledger.md
paper/sections/
paper/main.tex
paper/main.pdf
reviews/review-*.md
```

## Maintenance Rule

When any of the linked bridge layers changes, update this map first so the shortest route stays honest.

## Best Use

Read this note together with:

- `knowledge/master-map.md`
- `knowledge/learning-status.md`
- `docs/run-start-checklist.md`
- `prompts/07_launch.md`
- `docs/continuation-state.md`
