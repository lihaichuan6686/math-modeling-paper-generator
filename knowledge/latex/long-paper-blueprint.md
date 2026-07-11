# Long Paper Blueprint

Purpose: summarize how a strong 20-30 page CUMCM-style paper grows through structure, evidence, and repeated subquestion closure rather than filler.

Use this as the LaTeX-layer counterpart to the broader CUMCM page blueprint.

## Main Lesson

A long paper should not feel padded. It should feel like the route naturally required:

```text
question restatement
-> route analysis
-> assumptions and symbols
-> data or scene setup
-> model establishment
-> solution process
-> results
-> validation
-> conclusion
-> reproducibility appendix
```

## Recommended Length Logic

| Part | Typical pages | Why it earns space |
|---|---:|---|
| Abstract | 1 | closes the whole paper in compressed form |
| Problem restatement | 1-2 | rewrites the contest statement into model tasks |
| Problem analysis | 2-4 | justifies route choice and subquestion decomposition |
| Assumptions | 0.5-1 | makes the model auditable |
| Symbols | 0.5-1 | stabilizes formulas and code language |
| Data / scene setup | 2-4 | turns raw input into model-ready structure |
| Model establishment and solving | 8-14 | usually the technical center |
| Results and validation | 3-5 | converts computation into defended conclusions |
| Strengths / limitations / extension | 1-2 | shows scope control |
| References | 0.5-1 | ties methods to real sources |
| Appendix | 3-8 | supports reproducibility and traceability |

## Strong Body Shape

Recommended body structure:

```text
1 problem restatement
2 problem analysis
  2.1 question 1 analysis
  2.2 question 2 analysis
3 assumptions
4 symbols
5 data processing or scene setup
6 model establishment and solving
  6.1 question 1 model
    6.1.1 modeling idea
    6.1.2 equations / derivation
    6.1.3 solver / algorithm
    6.1.4 result interpretation
  6.2 question 2 model
7 validation and sensitivity
8 strengths, limitations, and extension
9 conclusion
appendix
```

## Abstract Rule

Write the abstract last.

It should usually include:

- one overall problem sentence;
- one method-result closure per major subquestion;
- one validation or comparison sentence;
- one final recommendation or summary sentence;
- 4-6 keywords that match the true route.

Avoid:

- background-only openings that consume half the abstract;
- method lists without results;
- abstract numbers that do not match the body.

## Figure And Table Density

For a full paper, expect at least:

- 1 route or workflow figure;
- 1 early object/scene/mechanism figure when the route needs it;
- 3-6 evidence or result figures;
- 3-8 parameter/result tables;
- 1 validation or sensitivity figure/table;
- 1 appendix inventory table.

Different families earn this density differently:

- geometry and engineering: scene, coordinate, residual, sensitivity;
- data/forecast: trend, fit, forecast, residual, scenario;
- optimization/scheduling: workflow, result comparison, capacity or schedule artifact;
- classification: preprocessing, feature, confusion, error analysis.

## Formula And Algorithm Rule

Do not chase formula count for its own sake.

Good formula density means:

- symbols are defined;
- the objective/constraints match the task;
- intermediate variables do not appear and vanish unexplained;
- advanced algorithms explain inputs, outputs, and parameters.

Good algorithm rhythm:

```text
variable definition
-> objective / prediction target
-> constraints or mechanism
-> solving steps
-> parameter settings
-> validation
```

## Appendix Rule

The appendix should contain:

- support-file or artifact inventory;
- environment or run notes;
- selected code excerpts;
- extra tables/figures;
- data-field explanation when needed.

But the runnable source should still live in the repository, not only inside the PDF.

## Quality Gate

Before treating the paper as complete, check:

- every subquestion has model, result, and validation presence;
- the abstract closes each subquestion;
- figures and tables are cited and interpreted;
- body numbers can be traced to outputs;
- there is no equation decoration, algorithm stacking, or conclusion overreach.

## Best Use

Read this note together with:

- `human-style-soft-rules.md`
- `local-awarded-paper-structure-rules.md`
- `national-family-section-budget-playbook.md`
- `section-writing-patterns.md`
- `../cumcm/20-30-page-paper-blueprint.md`
