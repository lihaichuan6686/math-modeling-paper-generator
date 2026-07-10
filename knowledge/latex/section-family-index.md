# LaTeX Section Family Index

Purpose: connect section roles to the most useful paragraph pattern, artifact type, and common failure mode.

This is a writing aid, not a style showcase.

## Section Families

| Section | Best paragraph pattern | First artifact | Typical failure |
|---|---|---|---|
| Problem restatement | background -> subquestions -> input/output table -> transition to route | task decomposition table | copies the contest statement instead of rewriting it |
| Problem analysis | signal -> route family -> rejected alternatives -> evidence plan | route diagram or route comparison table | jumps to formulas too early |
| Assumptions | assumption -> reason -> impact | assumption-impact table | assumptions are generic or never used again |
| Symbols | symbol -> meaning -> unit/domain | symbol table | symbols are undefined or duplicated |
| Data processing | source -> cleaning -> feature construction -> exploratory evidence | data inventory / cleaning table | preprocessing is narrated but not traceable |
| Model establishment | target -> variables -> equations -> constraints -> solver -> limitations | equation block + explanatory figure if needed | method names are listed without a mathematical body |
| Solution process | input -> algorithm steps -> parameters -> output files -> reproducibility note | algorithm or solver-setting table | code logic is hidden or seeds/settings are missing |
| Results | artifact -> interpretation -> link back to task | result table or figure | tables are dumped without explanation |
| Validation | metric -> perturbation/baseline -> conclusion | sensitivity / residual / feasibility plot | "robust" is claimed without evidence |
| Strengths and limitations | strength tied to evidence -> limitation -> future fix | limitation-remedy table | generic praise without scope control |
| Conclusion | answer each subquestion -> key numbers -> final recommendation -> caveat | conclusion summary tied to results | repeats the abstract or introduces new claims |
| Abstract | verified subquestion result sentences in compact form | method-result sentence per subquestion | written too early or filled with unsupported numbers |

## Section Order Rule

The most reliable order for drafting is:

```text
problem analysis -> assumptions -> symbols -> data processing -> model establishment -> solution process -> results -> validation -> strengths and limitations -> conclusion -> abstract
```

Do not start with the abstract unless the results and validation already exist.

## Cross-Section Stability

Keep these stable across the paper:

- subquestion numbering;
- route family name;
- symbol names;
- figure and table labels;
- decision output names;
- validation metric names.

If one changes, update the whole chain and the artifact ledger.

## Common Repair Moves

If a section feels thin, add one of these before adding filler text:

- a table;
- a figure;
- an equation block;
- a validation check;
- a file or artifact inventory row;
- a limitation tied to a concrete assumption.

## Best Use

Read this note together with:

- `cumcm-section-contract.md`
- `section-writing-patterns.md`
- `section-map.md`
- `figures-tables-equations-style.md`
- `../cumcm/20-30-page-paper-blueprint.md`
