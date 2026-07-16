# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `19-22 pages`
- target appendix length: `4-5 pages`
- route family: `geometry / spatial design`
- paper family: `scene setup -> derivation -> design result -> feasibility`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close geometric result and feasibility | method-result closure sentences | ending with formulas |
| Problem restatement | 1.0 | scene/task rewrite should be compact | task table | copied statement |
| Method overview | 0.8 | scene-to-derivation route should appear early | route figure | no route visibility |
| Problem analysis | 2.2 | scene interpretation and subquestion map need explanation | scene note, dependency table | formula jump too early |
| Assumptions | 0.8 | geometric simplifications matter | assumption-impact table | hidden simplifications |
| Symbols | 1.0 | dense symbol world must stay stable | symbol table | symbol overload |
| Data processing | 1.2 | known parameters and scene setup still need space | known-parameter table | underdescribed setup |
| Model establishment | 6.7 | derivation is the technical center | coordinate schematic, equation blocks | weak mathematical body |
| Solution process | 2.3 | numerical path and case split need explanation | process figure, parameter table | hidden computation path |
| Results | 2.8 | final design/location outputs need readable presentation | result table, final scene figure | no physical interpretation |
| Validation and sensitivity | 2.5 | replay, residual, or feasibility closes the loop | replay figure, feasibility table | token validation |
| Strengths and limitations | 0.8 | should define geometric scope honestly | limitation-remedy table | vague claims |
| Conclusion | 0.7 | must return to engineering meaning | conclusion summary | pure math wrap-up |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.0 | extra derivations and support outputs belong here | file inventory, extra cases | too much body logic moved out |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 scene construction | coordinate choice and simplification | base geometry model | parameter/symbol table | consistency check |
| Q2 main design result | case split and constraints | derivation model | result summary table | replay or residual figure |
| Q3 recommendation | alternative setup comparison | comparison logic | design comparison table | feasibility summary |

## Final Check

- Where is the strongest mathematical density expected? `Model establishment`
- Which section is most likely to stay too thin? `Result interpretation`
- What artifacts will prevent filler growth? `scene schematic`, `equation group`, `result table`, `replay/feasibility artifact`
- Which family-specific abstract closure pattern should be used? `scene -> derivation -> design -> feasibility`
