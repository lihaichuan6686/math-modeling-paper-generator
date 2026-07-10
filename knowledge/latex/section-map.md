# LaTeX Section Map

Purpose: connect the CUMCM paper section order to the evidence artifacts each section should produce.

This is a writing-order map, not a style guide.

## Recommended Write Order

Write in this order:

```text
problem analysis
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

## Section Responsibilities

| Section | Main job | Minimum artifact |
|---|---|---|
| Problem restatement | rewrite the task as modelable subquestions | task decomposition table |
| Problem analysis | justify the route family and paper shape | route diagram or route comparison table |
| Assumptions | make simplifications explicit | assumption-impact table |
| Symbols | define variables and units once | symbol table |
| Data processing | convert source data into model inputs | data inventory or feature table |
| Model establishment | define equations and model logic | equation block and explanatory figure when needed |
| Solution process | explain how the model is computed | algorithm steps or solver-setting table |
| Results | answer the subquestions with outputs | result tables and evidence figures |
| Validation | test feasibility, fit, or robustness | validation table or plot |
| Strengths and limitations | state scope honestly | limitation-remedy table |
| Conclusion | summarize final answers and recommendations | conclusion paragraph tied to results |
| Abstract | compress the whole paper last | method-result sentence for each subquestion |

## Body-Length Rule

If a section is thin, expand evidence before adding filler prose:

```text
missing artifact -> missing explanation -> missing cross-reference -> missing limitation
```

Do not use length alone as a success metric. Use section completeness and artifact traceability.

## Cross-Section Stability Rule

Keep these stable across the body:

- subquestion numbering;
- symbol names;
- figure and table labels;
- route family name;
- decision output names.

If a label changes in one section, update all references and the artifact ledger.

## Best Use

Use this note together with:

- `cumcm-section-contract.md`
- `section-writing-patterns.md`
- `figures-tables-equations-style.md`
- `../cumcm/route-index.md`

