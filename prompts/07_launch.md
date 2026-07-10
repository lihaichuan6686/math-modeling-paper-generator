# Launch Prompt

Use this when starting a new CUMCM-style paper run in Claude Code.

```text
You are working in a research-only mathematical modeling paper generator.

First read:
- docs/README.md
- docs/run-start-checklist.md
- docs/v1-runbook.md
- knowledge/README.md
- knowledge/cumcm/README.md
- knowledge/cumcm/route-index.md
- knowledge/cumcm/route-example-matrix.md
- knowledge/cumcm/paper-family-matrix.md
- knowledge/cumcm/generation-loop.md
- knowledge/quality/completion-gate.md

Then inspect problems/problem.md and any attachments.

Your job is to produce a complete v1.0 paper run, not just an outline.

Work in this order:
1. intake
2. ideation
3. model plan
4. implementation
5. writing
6. build
7. review
8. quality audit

Required outputs for the active run:
- runs/current/problem-analysis.md
- runs/current/data-inventory.md
- runs/current/model-candidates.md
- runs/current/model-plan.md
- runs/current/verification-plan.md
- runs/current/figure-plan.md
- runs/current/artifact-ledger.md
- reviews/review-current.md

Rules:
- choose the route before choosing the method;
- keep the question map stable from abstract to conclusion;
- require at least one visible figure and one visible table;
- trace every important claim to data, code, equation, figure, table, or review evidence;
- separate production-route E from monitoring-route E when the problem is E-type;
- do not hide synthetic data, fabricated citations, or unsupported claims;
- stop only when the draft is complete enough for review and the machine gate has been checked.
```

## Best Use

Read this together with:

- `README.md`
- `flow-map.md`
- `00_intake.md`
- `01_ideation.md`
- `02_model_plan.md`
- `03_implementation.md`
- `04_writing.md`
- `05_review.md`
- `06_quality_review.md`
