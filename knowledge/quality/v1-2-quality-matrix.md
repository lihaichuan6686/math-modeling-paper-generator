# v1.2 Quality Matrix

Purpose: compress the current v1.2 paper-quality rules into one compact matrix that connects each quality dimension to its main signal, the strongest files to inspect, and the usual repair direction.

This is a synthesis bridge, not a replacement for the full rubric or checklist.

## How To Use

Use this matrix when:

- a draft already exists;
- you need a fast quality snapshot;
- you want to know which layer to read next;
- you want the shortest path from a weak signal to a repair direction.

## v1.2 Quality Matrix

| Quality dimension | Main signal to check | Strongest files to inspect | Typical fail smell | Usual repair direction |
|---|---|---|---|---|
| Question map stability | abstract, body headings, tables, and conclusion all track the same subquestions | `docs/review-checklist.md`, `docs/v1.2-final-pass-guide.md`, `paper/sections/` | subquestion drift, silent renumbering, one question disappears | restore one stable question map across abstract, sections, captions, and conclusion |
| Section density | abstract is dense, model section is central, results and validation are both visible | `knowledge/latex/human-style-soft-rules.md`, `knowledge/latex/local-awarded-paper-structure-rules.md`, `runs/current/section-budget.md` | thin abstract, demo-sized body, validation collapsed into one paragraph | add missing subquestion loops and rebalance section roles before polishing wording |
| Method depth | each major subquestion has support layer -> main model -> result -> check layer | `knowledge/algorithms/method-depth-ladder.md`, `runs/current/method-depth-plan.md`, `runs/current/model-plan.md` | `method -> result` only, prestige algorithm names with no support | add preprocessing, executable decision layer, baseline comparison, or sensitivity check |
| Route credibility | chosen route fits the problem and rejected alternatives are visible when needed | `knowledge/cumcm/route-index.md`, `knowledge/cumcm/problem-type-paper-archetypes.md`, `runs/current/model-candidates.md` | route ambiguity, mixed route voices, wrong artifact family | restate the route and rebuild the model plan and artifact plan |
| Visual evidence distribution | early object figure exists and each major subquestion owns visible artifacts | `knowledge/latex/visual-family-index.md`, `knowledge/latex/local-figure-table-conventions.md`, `runs/current/figure-plan.md` | all visuals cluster at the end, object never shown early | redistribute figures/tables across subquestions and add missing object-first figure |
| Figure and caption quality | captions say what is shown, why it matters, and what to notice | `knowledge/latex/figures-tables-equations-style.md`, `docs/visual-generation-pipeline.md`, `paper/figures/` | generic captions, raw filenames, unlabeled evidence | rewrite captions, stabilize artifact names, and reclassify weak visuals |
| Table quality | tables carry executable values, readable headers, units, and precision | `knowledge/latex/table-family-index.md`, `paper/tables/`, rendered PDF | decorative summaries, clipped or overwide tables, inconsistent precision | move detail to appendix, keep summary table in body, tighten headers and decimals |
| Result traceability | every key number in abstract/conclusion exists in the ledger and outputs | `runs/current/artifact-ledger.md`, generated tables/figures, `src/` entry points | unsupported body numbers, appendix-only evidence, screenshot stand-ins | regenerate outputs, trace paths in the ledger, and remove unsupported claims |
| Validation strength | each major result has a real credibility check | `runs/current/verification-plan.md`, `knowledge/quality/completion-gate.md`, validation section | token validation, no perturbation range, no feasibility audit | add sensitivity, scenario, residual, baseline, or feasibility evidence |
| Human-team prose feel | paragraph-driven reasoning, method-fit explanation, result interpretation | `knowledge/latex/section-writing-patterns.md`, `knowledge/latex/human-style-soft-rules.md`, `prompts/09_revision_v1_2.md` | scaffold rhythm, bullet-stack feel, method praise with no evidence | merge fragments into analytical paragraphs and restore full subquestion loops |
| Appendix boundary | body is complete before code, support-file inventory exists, appendix is clearly support-only | `knowledge/latex/final-polish-and-appendix-rules.md`, `docs/v1.2-final-pass-guide.md`, appendix pages | paper feels complete only because of code pages | move missing logic back to the body and shorten appendix excerpts if needed |
| PDF finish | rendered copy is clean, readable, and free of residue | `docs/review-checklist.md`, rendered PDF pages, compile log | watermark residue, clipped tables, placeholder metadata, empty tail pages | clean metadata, fix layout, rerender, and recheck final pages |

## Fast Reading Order

If the draft already exists and time is tight, use:

```text
v1.2 final pass guide
-> review checklist
-> quality matrix
-> finding-gate matrix
-> revision prompt
```

## Best Use

Read this note together with:

- `quality-rubric-v2.md`
- `review-finding-index.md`
- `finding-gate-matrix.md`
- `../../docs/v1.2-final-pass-guide.md`
- `../../prompts/09_revision_v1_2.md`
