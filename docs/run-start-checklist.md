# Run Start Checklist

Purpose: give Claude Code a short, repeatable start sequence for a new CUMCM-style paper run.

This is the first working checklist, not the full workflow manual.

## Before You Start

1. Read `knowledge/README.md`.
2. Read `docs/README.md`.
3. Read `knowledge/cumcm/README.md`.
4. Read `knowledge/cumcm/route-index.md`.
5. Read `knowledge/cumcm/route-example-matrix.md`.
6. Read `knowledge/cumcm/paper-family-matrix.md`.
7. Read `knowledge/cumcm/generation-loop.md`.
8. Read `knowledge/quality/completion-gate.md`.
9. If the user wants a stronger human-like paper, read `docs/v1.2-runbook.md`.

## First Decisions

Write down, in this order:

1. problem signal;
2. route family;
3. paper family;
4. positive sample;
5. contrast sample;
6. deep-reading anchor;
7. risk gate.

If the route is unclear, do not start implementation yet.

## First Outputs

For a fresh run, produce these before polishing prose:

- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `runs/current/method-depth-plan.md`
- `runs/current/section-budget.md`
- `runs/current/writing-style-plan.md`

## First Paper Shape

The first draft should already have:

- abstract;
- problem restatement;
- problem analysis;
- assumptions;
- symbols;
- data processing;
- model establishment;
- solution process;
- results;
- validation;
- strengths and limitations;
- conclusion;
- references;
- appendix.

## First Quality Check

Before treating the run as usable, confirm that:

- the object appears before the method stack;
- at least one figure and one table are planned or generated;
- claims can be tied to a file, equation, code output, figure, table, or review note;
- the chosen route matches the problem type;
- the review gate has evidence, not just prose.
- if the target is v1.2, the method chain and section budget are written down before polishing.

## Route-Specific Reminder

For E-type problems, decide whether the run is:

- production-route E; or
- monitoring-route E.

For timetable/service-style cases, make sure the route, operation plan, full timetable, capacity audit, and scenario outputs are visible early.
