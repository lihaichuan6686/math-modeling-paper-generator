# Phase 4 Prompt: Writing

Read:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `docs/visual-generation-pipeline.md`

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
Use `knowledge/cumcm/20-30-page-paper-blueprint.md` to check page budget, visual density, per-subquestion coverage, and anti-filler rules before finalizing section drafts.

If the chosen route is E-type, also check:

- production-route E papers include forecast -> service/inventory -> production action;
- monitoring-route E papers include diagnosis -> forecast -> monitoring/policy action;
- route-specific tables and figures from the blueprint are actually present.

## Figure and Table Rule

Every figure/table inserted into LaTeX must:

- exist under `paper/figures/` or `paper/tables/`
- have a caption
- have a label
- be cited and interpreted in text
- be listed in the artifact ledger

For AI-generated or hand-drawn schematics, follow `docs/visual-generation-pipeline.md`: they may explain structure but must not be treated as data evidence.

## Result Rule

Every important number in:

- abstract
- results
- conclusion

must appear in `runs/current/artifact-ledger.md` as a key result.

For E-route drafts:

- production-route key results must include at least one service-level, support-rate, inventory, or production quantity artifact;
- monitoring-route key results must include at least one monitoring/policy decision artifact and, when relevant, one intervention-effect or consequence artifact.

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
