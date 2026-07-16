# Phase 4 Prompt: Writing

Read:

- `runs/current/model-plan.md`
- `runs/current/verification-plan.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`
- `runs/current/section-budget.md`
- `runs/current/writing-style-plan.md`
- `knowledge/cumcm/paper-generation-playbook.md`
- `knowledge/cumcm/20-30-page-paper-blueprint.md`
- `knowledge/cumcm/official-style-vs-modern-draft-risk.md`
- `knowledge/latex/cumcm-section-contract.md`
- `knowledge/latex/human-style-soft-rules.md`
- `knowledge/latex/national-family-section-budget-playbook.md`
- `knowledge/latex/national-abstract-and-closeout-playbook.md`
- `knowledge/latex/v1-4-abstract-closeout-rules.md`
- `knowledge/latex/national-problem-family-claim-boundary-matrix.md`
- `knowledge/latex/national-problem-family-paragraph-density-playbook.md`
- `knowledge/latex/local-awarded-paper-structure-rules.md`
- `knowledge/latex/local-figure-table-conventions.md`
- `knowledge/latex/figures-tables-equations-style.md`
- `docs/v1.2-draft-contract.md`
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

For v1.2, the abstract should usually be written to one dense page unless the problem itself is unusually small.
For v1.4, the abstract must be checked against `knowledge/latex/v1-4-abstract-closeout-rules.md`: every major subquestion should have method-result closure, key results must match the artifact ledger, and the abstract should plausibly fill most of page one without exceeding one page.
Use `docs/v1.2-draft-contract.md` as the default drafting contract when section density, per-subquestion closure, or visual distribution still feel underspecified.

## Structure Rule

A full CUMCM paper reaches 20-30 pages through structure:

- each subquestion has analysis, model, solution, result, and validation
- figures and tables carry real content
- formulas are explained and referenced
- appendix supports reproducibility

Do not pad with generic background.
Use `knowledge/cumcm/20-30-page-paper-blueprint.md` to check page budget, visual density, per-subquestion coverage, and anti-filler rules before finalizing section drafts.
Use `knowledge/latex/national-family-section-budget-playbook.md` to tune section-page emphasis and abstract closure to the active problem family instead of relying only on generic long-paper rules.
Use `knowledge/latex/national-abstract-and-closeout-playbook.md` when abstract sentences, subquestion endings, or transitions still read like scaffolding instead of a human team draft.
Use `knowledge/latex/v1-4-abstract-closeout-rules.md` when the abstract is too short, method-only, missing final answers, or inconsistent with the conclusion and artifact ledger.
Use `knowledge/latex/national-problem-family-claim-boundary-matrix.md` when the abstract or conclusion sounds stronger than the available evidence, especially for claims about optimality, reliability, deployment, or robustness.
Use `knowledge/latex/national-problem-family-paragraph-density-playbook.md` when the body has the right outline but sections still feel too abrupt, too short-winded in the wrong place, or too dependent on artifact stacking.
Use `knowledge/latex/human-style-soft-rules.md` to check whether sections feel proportioned like a human-team paper rather than a thin generated draft.

If the chosen route is E-type, also check:

- production-route E papers include forecast -> service/inventory -> production action;
- monitoring-route E papers include diagnosis -> forecast -> monitoring/policy action;
- route-specific tables and figures from the blueprint are actually present.

For all routes, also check:

- the abstract, body headings, result tables, and conclusion use one stable `question map`;
- the earliest explanatory figure identifies the modeled object before late-stage result figures appear;
- each named method closes into a visible artifact and a decision statement;
- effective body length comes from argument and evidence, not blank pages, promotional residue, or code screenshots.
- paragraphs are carrying explanation, not just stacked bullet fragments;
- each major subquestion closes a full loop before the next one starts;
- the strongest method section is longer because it contains real equations, interpretation, and validation, not just prestige algorithm names.
- when the problem has many numbered tasks, length should usually come from repeating the full subquestion loop rather than one oversized global model block.
- figures and tables should make each subquestion visibly concrete instead of clustering all visuals in one late result section.
- each major subquestion should end with a close-out paragraph that states the finding, the supporting evidence, and why the next step is needed.
- family-level closeout claims should stay inside the proven boundary of the active problem type rather than defaulting to generic `effective` or `optimal` language.
- family-level paragraph density should follow the active problem type, especially around model bridges, result interpretation, and validation explanation.

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

Every important claim about:

- the best strategy
- the best parameter choice
- the effect of intervention
- the comparison of alternatives

must also be backed by at least one table or figure cited in the same subquestion section.

For E-route drafts:

- production-route key results must include at least one service-level, support-rate, inventory, or production quantity artifact;
- monitoring-route key results must include at least one monitoring/policy decision artifact and, when relevant, one intervention-effect or consequence artifact.

For all v1.2 drafts:

- the abstract should contain one method-result closure per major subquestion;
- for v1.4, every abstract and conclusion result should appear in `runs/current/artifact-ledger.md` as a key result or be explicitly qualitative;
- the body should have an early figure or table that identifies the modeled object or route;
- every major subquestion should have at least one explicit validation or comparison artifact unless the paper states why that evidence is unavailable;
- long sections should be long because they contain equations, artifacts, and interpretation, not because they repeat setup prose.

## Citation Rule

- Use real, relevant references only.
- Do not fabricate citations.
- Keep placeholder references visibly marked until replaced.

## Build Preparation

Before compiling:

- no missing figure paths
- no obvious placeholder names/dates/team fields
- no unstable question numbering between abstract and body
- no unsupported abstract claims
- no appendix/code screenshots being used to stand in for missing result sections
- no table too wide by design
