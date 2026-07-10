# Finding Gate Matrix

Purpose: connect common review findings to the gate they should trigger and the kind of repair that usually fixes them.

This is a review-action bridge, not a rubric.

## Finding To Gate Map

| Finding family | Gate to trigger | Evidence to check first | Usual repair |
|---|---|---|---|
| Coverage drift | completion gate, problem coverage review | problem-analysis, model-plan, conclusion | restore the stable question map across the paper |
| Method without closure | model logic review, completion gate | model establishment, results, artifact ledger | add the missing output and decision consequence |
| Traceability gap | evidence family index, artifact ledger review | artifact ledger, generated tables/figures, code outputs | record source paths and regenerate the artifact if needed |
| Visual mismatch | visual/table family indexes, figure-plan review | caption, label, text reference, plotted content | replace or reclassify the artifact and rewrite the caption |
| Validation gap | completion gate, validation review | validation section, scenario or sensitivity evidence | add feasibility, sensitivity, error, or comparison checks |
| Layout residue | quality rubric, review checklist | rendered PDF pages, page count, template residue | remove residue and re-render the PDF |
| Route ambiguity | route index, paper-family matrix | route selection, problem analysis, model candidates | restate the route and rebuild the model plan |
| Reproducibility gap | evidence family index, review checklist | source paths, run outputs, artifact ledger | replace screenshots/manual edits with generated outputs |
| Responsible-use risk | completion gate, responsible-use review | provenance, limitations, task framing | disclose limits and fix provenance issues |

## Reading Rule

Use this order:

```text
finding
-> gate
-> missing evidence
-> repair
-> recheck
```

## Best Use

Read this note together with:

- `review-finding-index.md`
- `evidence-family-index.md`
- `completion-gate.md`
- `../docs/review-checklist.md`
