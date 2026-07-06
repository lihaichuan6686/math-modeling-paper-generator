# Phase 5 Prompt: Review

Read:

- `docs/review-checklist.md`
- `runs/current/artifact-ledger.md`
- `runs/current/figure-plan.md`
- `knowledge/quality/reproducibility-and-ai-difference-framework.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `docs/visual-generation-pipeline.md`
- current `paper/`
- current `src/`

Create:

- `reviews/review-current.md`

## Review Scope

Review:

- problem coverage
- section structure
- 20-30 page structure and visual-density contract
- model logic
- code/data reproducibility
- figures and tables
- visual source classification and AI-schematic disclosure
- validation and sensitivity analysis
- LaTeX/PDF quality
- responsible-use constraints

## Required Output

Use this structure:

```text
# Review

## Summary

## Blocking Issues

## Important Issues

## Minor Issues

## Evidence Checked

## Evidence Not Checked

## Required Fixes

## Human Verification Needed

## Final Status
Pass / Needs revision / Reject for research use
```

## Hard Fail Conditions

Mark as blocking if:

- any subquestion is unanswered
- main results cannot be traced to data/code/equations
- figures or tables are used without source/caption/reference
- validation is absent for core results
- PDF cannot compile or has unreadable major content
- fabricated data, references, or experimental evidence are detected
- the request appears to support active contest cheating or concealment of prohibited AI involvement

## Repair Loop

If blocking or important issues are found:

1. fix the source document/code/artifact
2. rebuild if needed
3. update the artifact ledger
4. revise the review
