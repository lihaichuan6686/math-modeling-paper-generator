# Launch Prompt v1.2

Use this when you want Claude Code to produce the stronger 1.2 paper style rather than the original small v1.0 draft.

```text
You are working in a research-only mathematical modeling paper generator.

Your target is a v1.2 paper run.
This is not a small demo draft. It should read like a serious human-team CUMCM paper.

First read:
- docs/README.md
- docs/run-start-checklist.md
- docs/v1.2-runbook.md
- docs/continuation-state.md
- knowledge/README.md
- knowledge/cumcm/paper-generation-playbook.md
- knowledge/cumcm/20-30-page-paper-blueprint.md
- knowledge/cumcm/official-paper-paradigms.md
- knowledge/algorithms/README.md
- knowledge/algorithms/method-depth-ladder.md
- knowledge/latex/README.md
- knowledge/latex/section-writing-patterns.md
- knowledge/latex/human-style-soft-rules.md
- knowledge/quality/completion-gate.md

Then inspect problems/problem.md and any attachments.

Your job is to produce a complete v1.2 paper run, not just an outline and not a minimal demo.

Work in this order:
1. intake
2. ideation
3. model plan
4. method-depth plan
5. implementation
6. writing-style plan
7. section budget
8. writing
9. build
10. review
11. quality audit
12. revision if the review still flags thinness, shallow chains, or machine-like prose

Required outputs for the active run:
- runs/current/problem-analysis.md
- runs/current/data-inventory.md
- runs/current/model-candidates.md
- runs/current/model-plan.md
- runs/current/method-depth-plan.md
- runs/current/verification-plan.md
- runs/current/figure-plan.md
- runs/current/section-budget.md
- runs/current/writing-style-plan.md
- runs/current/artifact-ledger.md
- reviews/review-current.md

Hard rules:
- choose the route before choosing the method;
- keep the question map stable from abstract to conclusion;
- make the abstract close each subquestion with method plus result;
- do not let the abstract stop at half a page unless the task is genuinely tiny;
- for each major subquestion, use a method chain with a support layer and a check layer;
- require at least one visible figure and one visible table for every major subquestion when the route reasonably allows it;
- interpret every important table and figure in prose;
- keep the paper body paragraph-driven rather than bullet-driven;
- let paper length come from evidence, validation, comparison, and explanation, not filler;
- if the review still says `Needs revision`, follow prompts/09_revision_v1_2.md and repair the draft before finalizing;
- stop only when the draft is complete enough to plausibly look human-team written and the machine gate has been checked.
```

## Best Use

Read this together with:

- `07_launch.md`
- `02_model_plan.md`
- `04_writing.md`
- `../docs/v1.2-runbook.md`
- `../knowledge/latex/human-style-soft-rules.md`
