# Evidence Family Index

Purpose: classify the kinds of evidence that matter when reviewing a CUMCM-style paper.

This note helps review and completion checks decide what counts as proof.

## Evidence Families At A Glance

| Evidence family | What it proves | Typical location | When it is strongest |
|---|---|---|---|
| Problem statement and attachments | what was asked and what inputs existed | `problems/` and source attachments | at intake and route selection |
| Data inventory | what raw fields and units were available | `runs/current/data-inventory.md` | when checking preprocessing and traceability |
| Model plan | which route, model, and validation were chosen | `runs/current/model-plan.md` | when judging model logic and route fit |
| Figure plan | which visuals were expected and why | `runs/current/figure-plan.md` | when checking visual coverage and evidence design |
| Artifact ledger | which outputs support which claims | `runs/current/artifact-ledger.md` | when checking traceability and completion |
| Code run outputs | what the scripts actually generated | `src/` outputs and run folders | when checking reproducibility |
| Generated tables and figures | what the model produced | `paper/tables/`, `paper/figures/` | when checking result and validation evidence |
| LaTeX source | how the paper is assembled | `paper/main.tex`, `paper/sections/` | when checking structure and references |
| Compiled PDF | how the paper renders | `paper/main.pdf` or rendered pages | when checking layout and final readability |
| Review note | what remains risky or incomplete | `reviews/review-*.md` | when checking whether the run is ready to hand off |
| Machine gate output | whether the automated checks passed | `scripts/check-run-quality.ps1` output | when checking minimum completeness |

## Evidence Hierarchy

When evidence conflicts, prefer the following order:

```text
problem/attachments
-> generated outputs
-> artifact ledger
-> LaTeX source
-> rendered PDF
-> review note
-> status summaries
```

Why:

- the problem statement defines the task;
- generated outputs prove the computation;
- the ledger connects outputs to claims;
- the LaTeX source shows how the paper is built;
- the PDF shows whether the structure is readable;
- the review note records remaining risks;
- status summaries are useful, but only as a compressed view of the above.

## Strong Evidence Rules

- Prefer generated tables and figures over screenshots.
- Prefer rendered PDF pages over source-only claims about layout.
- Prefer ledger entries over memory of what was produced.
- Prefer code outputs over narrative descriptions of what code would do.
- Prefer review notes that list specific weaknesses over generic praise.

## Weak Evidence Warnings

Treat these as partial evidence, not final proof:

- a figure with no source recorded;
- a table copied without a code or calculation trace;
- a claim in the abstract not listed in key results;
- a compile success without rendered-page inspection;
- a review note that only says "looks good";
- a status matrix that is not supported by the run artifacts.

## Best Use

Read this note together with:

- `../quality/completion-gate.md`
- `../quality/quality-rubric-v2.md`
- `../../docs/review-checklist.md`
- `../../docs/artifact-ledger-template.md`

