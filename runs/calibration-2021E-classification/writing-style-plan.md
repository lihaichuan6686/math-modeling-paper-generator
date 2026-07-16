# Writing Style Plan Template

Use this file as the starting shape for `runs/current/writing-style-plan.md`.

Before filling it in, read:

- `knowledge/latex/paper-style-plan.md`
- `knowledge/latex/human-style-soft-rules.md`
- `knowledge/latex/national-abstract-and-closeout-playbook.md`
- `knowledge/latex/national-problem-family-paragraph-density-playbook.md`
- `docs/v1.2-draft-contract.md`
- `docs/family-writing-style-examples.md`

## Style Target

- target version: `v1.2`
- route family: `classification-recognition`
- selected style variant: `technical student-team classification paper`
- positive sample: `knowledge/cumcm/deep-reading-2021E014.md`
- contrast sample: `metric-only machine draft with one accuracy table`
- target reader impression: `serious student team, not polished marketing copy and not scaffold notes`

## Core Writing Choices

- abstract density target: `about one dense page with method-result closure for each major subquestion`
- paragraph-driven vs bullet-driven balance: `main body paragraph-driven; bullets reserved for assumptions, symbols, and short inventories`
- tone target: `calm, analytical, route-aware`
- how results will be interpreted in prose: `artifact -> conclusion -> task meaning -> transition`
- how limitations will be stated: `specific and non-dramatic`
- family-specific abstract skeleton: `global task -> Q1 closure -> Q2 closure -> Q3 closure -> validation -> final recommendation`
- preferred subquestion close-out pattern: `main finding -> why credible -> what next subquestion now requires`
- transition rule: `explain why the next model step is needed, not just that it exists`
- family-specific density cue: `each modeling subsection should close preprocessing -> representation -> classifier -> class-level evidence, not stop at method names`

## Section Notes

| Section | Intended feel | What must not happen |
| --- | --- | --- |
| Abstract | dense, method-result closure | half-page summary, method names without results |
| Problem analysis | route-aware, comparative | restatement padding |
| Model establishment | technical and explanatory | prestige algorithm stacking |
| Results | evidence plus interpretation | artifact dumping |
| Validation | calm and explicit | one-sentence token check |
| Conclusion | concise and numeric | new methods or unsupported claims |

## Paragraph Rhythm

- preferred rhythm: `topic sentence -> model/artifact reference -> interpretation -> transition`
- maximum tolerance for stacked micro-paragraphs: `avoid long runs of one-sentence paragraphs`
- list-risk zones: `analysis, model, and results sections`
- required interpretation zones: `after every important figure/table and at the end of each major subquestion`
- family-specific bridge paragraphs that must exist:
- preprocessing choice to feature representation;
- feature representation to classifier comparison;
- classifier comparison to final identification conclusion.
- section most likely to become artifact-stacked: results and validation, especially if confusion evidence is not interpreted.
- section that should stay intentionally compact: problem restatement and generic assumptions.

## Human-Team Signals To Deliberately Include

- one early sentence that explains why the chosen route fits better than nearby alternatives;
- one close-out paragraph after each major subquestion;
- one limitation sentence that points to a real model boundary rather than generic humility;
- one explicit explanation of what the validation evidence actually confirms.

## Human-Team Soft Rules

- first explanatory figure should identify the modeled object early;
- each subquestion should close a full loop before the next one starts;
- important tables and figures should be interpreted immediately after citation;
- long sections should be long because they contain equations, artifacts, and validation, not repeated narration.

## Thinness Risks

- sections likely to become too short: validation, preprocessing comparison, class-level interpretation.
- sections likely to become too bullet-heavy: problem analysis and model-candidate comparison.
- sections likely to overuse generic prose: model evaluation and conclusion.
- subquestions most likely to end without a real close-out sentence: classifier comparison and origin/category identification.
- places where method names may appear before route explanation: PCA/LDA/SVM/random forest descriptions.
- places where validation may look decorative instead of necessary: confusion matrix and sensitivity analysis.
