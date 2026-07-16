# Writing Style Plan

## Style Target

- target version: `v1.2`
- route family: `classification / recognition`
- selected style variant: `official concise closure + evidence-dense research style`
- positive sample: `deep-reading-2021E014.md`
- contrast sample: `official-style-vs-modern-draft-risk.md`

## Core Writing Choices

- abstract density target: `one dense page with preprocessing -> classifier -> class-level validation closure`
- paragraph-driven vs bullet-driven balance: `paragraph-driven in body; feature and metric detail moved into tables`
- tone target: `careful, diagnostic, class-aware`
- how results will be interpreted in prose: `each metric artifact should say what it means at class level`
- how limitations will be stated: `state sample limitations, class imbalance, and generalization scope directly`
- family-specific abstract skeleton: `preprocessing / feature route -> classifier result -> confusion/error validation`
- preferred subquestion close-out pattern: `feature/classifier result -> recognition meaning -> error check -> next-step selection`
- family-specific density cue: `preprocessing explanation, classifier-choice rationale, and confusion-interpretation paragraphs must be heavier than generic ML setup`

## Section Notes

| Section | Intended feel | What must not happen |
| --- | --- | --- |
| Abstract | names recognition meaning, not just metrics | accuracy-only summary |
| Problem analysis | explains why preprocessing and class-level evidence matter | generic ML wording |
| Model establishment | model comparison criteria are explicit | one-model shortcut |
| Results | confusion-level interpretation is visible | metrics dumped without prose |
| Validation | split policy, leakage, and error analysis all appear | validation by one score |
| Conclusion | closes with diagnostic implication and caveat | only repeating best accuracy |

## Paragraph Rhythm

- preferred rhythm: `data/feature fact -> classifier implication -> class-level meaning -> transition`
- maximum tolerance for stacked micro-paragraphs: `avoid long runs of metric-only comments`
- list-risk zones: `data processing and conclusion`
- required interpretation zones: `after preprocessing artifact`, `after classifier comparison artifact`, `after confusion/error artifact`
- family-specific bridge paragraphs that must exist: `preprocessing-to-feature paragraph`, `comparison-table-to-chosen-classifier paragraph`
- section most likely to become artifact-stacked: `results`
- section that should stay intentionally compact: `problem restatement`

## Human-Team Soft Rules

- preprocessing should sound like part of the model, not setup trivia;
- the chosen classifier should be justified in terms of class behavior, not only one global score;
- each subquestion should end by stating what recognition conclusion is now defensible;
- recommendation language should stay inside the tested dataset scope.

## Thinness Risks

- sections likely to become too short: `error interpretation`
- sections likely to become too bullet-heavy: `data processing`
- sections likely to overuse generic prose: `conclusion`
- subquestions most likely to end without a real close-out sentence: `classifier comparison subsection`
