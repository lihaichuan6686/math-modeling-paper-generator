# Review Finding Index

Purpose: classify the most common review findings in CUMCM-style papers and map them to the gates they should trigger.

This note helps a reviewer turn observations into consistent actions.

## Common Finding Families

| Finding family | What it usually means | Typical gate | Typical repair |
|---|---|---|---|
| Coverage drift | a subquestion disappears or changes name | completion gate, problem coverage review | restore the stable question map everywhere |
| Method without closure | an algorithm is named but no result or decision follows | model logic review, completion gate | add the missing artifact and decision consequence |
| Traceability gap | a result cannot be tied to code, equation, or ledger | evidence family index, artifact ledger review | record source paths and regenerate the artifact if needed |
| Visual mismatch | a figure or table exists but does not support the claim | visual/table family indexes, figure-plan review | reclassify or replace the artifact and rewrite the caption |
| Validation gap | results look complete but no check proves credibility | completion gate, validation review | add sensitivity, feasibility, comparison, or error evidence |
| Layout residue | the PDF looks long but is polluted by placeholders or clutter | quality rubric, review checklist | remove residue and verify rendered pages again |
| Route ambiguity | the paper mixes route families or uses the wrong one | route index, paper-family matrix | restate the route and rebuild the model plan |
| Reproducibility gap | the paper relies on screenshots or manual edits | evidence family index, review checklist | use generated outputs and trace them in the ledger |
| Responsible-use risk | the draft may overstate provenance or hide constraints | completion gate, responsible-use review | disclose limitations and fix provenance issues |

## How To Read The Findings

### Coverage drift

If a subquestion is renamed, merged, or dropped, treat it as a structural failure, not a wording issue.

### Method without closure

If the paper lists methods but does not produce outputs, treat that as incomplete modeling.

### Traceability gap

If the result cannot be traced, do not accept the number as final evidence.

### Visual mismatch

If a figure or table does not support the claim, the issue is usually one of planning, not rendering.

### Validation gap

If the result lacks a check, the paper may be readable but is not yet review-ready.

### Layout residue

If the PDF looks complete because of blanks, screenshots, or template residue, the paper is not complete.

### Route ambiguity

If the route family is unclear, no amount of local polishing should be treated as completion.

### Reproducibility gap

If the paper cannot be regenerated from files and run outputs, the evidence is not strong enough.

### Responsible-use risk

If provenance or limitations are unclear, the paper should remain in review rather than handoff.

## Review Workflow

Use this order when turning findings into actions:

```text
finding
-> classify family
-> identify gate
-> list evidence missing
-> name repair
-> recheck
```

## Best Use

Read this note together with:

- `evidence-family-index.md`
- `completion-gate.md`
- `quality-rubric-v2.md`
- `../../docs/review-checklist.md`

