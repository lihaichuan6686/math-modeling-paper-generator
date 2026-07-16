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
10. If the user wants a stronger reusable method, read `docs/v1.3-methodology-runbook.md`.
11. If the user wants contest-circle feel, online sanity checking, or v1.4 behavior, read `docs/v1.4-runbook.md`, `knowledge/community/math-modeling-soft-rules.md`, `knowledge/community/contest-workflow-and-team-execution.md`, `knowledge/community/section-duty-soft-rules.md`, `knowledge/community/visual-evidence-chain-rules.md`, `knowledge/community/paper-polish-and-feel.md`, and `knowledge/cumcm/recent-award-paper-visual-rhythm.md`.

## First Decisions

Write down, in this order:

1. problem signal;
2. modeled object;
3. decision object;
4. route family;
5. paper family;
6. positive sample;
7. contrast sample;
8. deep-reading anchor;
9. online consensus need;
10. team-execution plan;
11. risk gate.
12. `what/where/how/why` preparation note;
13. cross-question dependency note.
14. first-pass family: prediction, optimization, evaluation, or mixed;
15. required first result artifact.

If the route is unclear, do not start implementation yet.

## First Outputs

For a fresh run, produce these before polishing prose:

- `runs/current/problem-profile.md`
- `runs/current/problem-analysis.md`
- `runs/current/data-inventory.md`
- `runs/current/model-candidates.md`
- `runs/current/route-decision.md`
- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `runs/current/method-depth-plan.md`
- `runs/current/section-budget.md`
- `runs/current/writing-style-plan.md`
- `runs/current/methodology-checklist.md`
- `runs/current/literature-notes.md`
- `runs/current/online-consensus-notes.md`

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
- the review gate has evidence, not just prose;
- if the target is v1.2, the method chain and section budget are written down before polishing;
- if the target is v1.3, the modeled object, decision object, and route-decision logic are written down before implementation.
- if the target is v1.4, the online-consensus note exists or the skip reason is written down before final paper writing.
- if the target is v1.4, `literature-notes.md` records method/data/domain/validation support separately from online consensus.
- if the target is v1.4, `problem-analysis.md`, `model-plan.md`, and `methodology-checklist.md` show modeling, programming, and writing roles rather than a single prose-only draft.
- if the target is v1.4, the abstract rewrite is scheduled after final result tables and figures stabilize.
- if the target is v1.4, `figure-plan.md` and `writing-style-plan.md` record page-one abstract density, pages 4-6 early model evidence, pages 8-12 artifact/prose alternation, and middle-body artifact rhythm.
- if the target is v1.4, `figure-plan.md`, `artifact-ledger.md`, and `paper/main.tex` agree on body-critical figures/tables, subquestion links, captions, and nearby interpretation.
- if the target is v1.4, AI-generated images are labeled as schematic and excluded from numeric evidence.
- if the target is v1.4, `problem-profile.md` or `problem-analysis.md` records the objective, decision variables or answer object, constraints, data needs, and cross-question dependencies before model implementation.
- if the target is v1.4, a practical route with visible evidence is preferred over a clever route that cannot produce interpretable tables, figures, validation, or paper-ready answers.

## Route-Specific Reminder

For E-type problems, decide whether the run is:

- production-route E; or
- monitoring-route E.

For timetable/service-style cases, make sure the route, operation plan, full timetable, capacity audit, and scenario outputs are visible early.
