# Phase 4 Prompt: Writing

Read:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`

Write:

- `paper/sections/*.tex`
- update `paper/main.tex` only when needed

## Writing Order

Write in this order:

```text
problem restatement
-> problem analysis
-> assumptions
-> symbols
-> data processing
-> model establishment
-> solution process
-> results
-> validation
-> strengths and limitations
-> conclusion
-> abstract
```

The abstract is written last.

## Structure Rule

A full CUMCM paper reaches 20-30 pages through structure:

- each subquestion has analysis, model, solution, result, and validation
- figures and tables carry real content
- formulas are explained and referenced
- appendix supports reproducibility

Do not pad with generic background.

## Figure and Table Rule

Every figure/table inserted into LaTeX must:

- exist under `paper/figures/` or `paper/tables/`
- have a caption
- have a label
- be cited and interpreted in text
- be listed in the artifact ledger

## Result Rule

Every important number in:

- abstract
- results
- conclusion

must appear in `runs/current/artifact-ledger.md` as a key result.

## Citation Rule

- Use real, relevant references only.
- Do not fabricate citations.
- Keep placeholder references visibly marked until replaced.

## Build Preparation

Before compiling:

- no missing figure paths
- no obvious placeholder names/dates/team fields
- no unsupported abstract claims
- no table too wide by design
