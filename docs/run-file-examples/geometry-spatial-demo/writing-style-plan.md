# Writing Style Plan

## Style Target

- target version: `v1.2`
- route family: `geometry / spatial design`
- selected style variant: `local awarded-paper dense style + route-heavy analytical style`
- positive sample: `spatial-measurement-comparison-B030-B086-B311.md`
- contrast sample: `official-style-vs-modern-draft-risk.md`

## Core Writing Choices

- abstract density target: `one dense page with scene -> derivation -> design -> feasibility closure`
- paragraph-driven vs bullet-driven balance: `paragraph-driven around equations, with list-like details moved to tables`
- tone target: `precise, technically calm, scene-aware`
- how results will be interpreted in prose: `every numeric design output should be translated into visible physical meaning`
- how limitations will be stated: `state scene simplifications and feasibility scope plainly`
- family-specific abstract skeleton: `scene setup -> geometric route -> computed design -> replay or feasibility`
- preferred subquestion close-out pattern: `geometric result -> physical meaning -> feasibility check -> carry-forward configuration`
- family-specific density cue: `derivation should be dense, but the first paragraph after each major equation block must explain physical meaning`

## Section Notes

| Section | Intended feel | What must not happen |
| --- | --- | --- |
| Abstract | names the visible design result | ending with formulas only |
| Problem analysis | scene and task decomposition appear early | abstract geometry talk |
| Model establishment | equations are explained in words | prestige derivation without interpretation |
| Results | design outputs are visually concrete | one final number with no scene meaning |
| Validation | replay/overlap/residual language is visible | symbolic-only validation |
| Conclusion | returns to engineering meaning | pure mathematical summary |

## Paragraph Rhythm

- preferred rhythm: `scene or equation reference -> geometric meaning -> design implication -> transition`
- maximum tolerance for stacked micro-paragraphs: `avoid long runs of symbol-only paragraphs`
- list-risk zones: `assumptions and symbols`
- required interpretation zones: `after the scene figure`, `after the main result table`, `after replay/residual artifacts`
- family-specific bridge paragraphs that must exist: `scene-to-coordinate paragraph`, `numeric result-to-physical meaning paragraph`
- section most likely to become artifact-stacked: `results`
- section that should stay intentionally compact: `problem restatement`

## Human-Team Soft Rules

- the first figure should make the scene legible before heavy derivation begins;
- the symbol world should stay stable through all subquestions;
- each subquestion should end by stating what physical or geometric conclusion has been obtained;
- recommendation language should stay inside the tested assumptions.

## Thinness Risks

- sections likely to become too short: `result interpretation`
- sections likely to become too bullet-heavy: `assumptions`
- sections likely to overuse generic prose: `limitations`
- subquestions most likely to end without a real close-out sentence: `middle derivation subsection`
