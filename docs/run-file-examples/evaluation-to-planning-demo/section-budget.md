# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `20-22 pages`
- target appendix length: `4-6 pages`
- route family: `evaluation to planning`
- paper family: `evaluation -> planning -> feasibility audit`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close score, plan, and validation | method-result closure sentences | ending at ranking |
| Problem restatement | 1.0 | compact task decomposition is enough | task table | copied statement |
| Method overview | 0.8 | route bridge should appear early | route flow figure | too generic |
| Problem analysis | 2.2 | must justify why ranking alone is incomplete | route comparison table | weak route logic |
| Assumptions | 0.8 | planning assumptions affect feasibility | assumption-impact table | generic assumptions |
| Symbols | 0.8 | score and decision variables must stay stable | symbol table | symbol drift |
| Data processing | 2.4 | indicator cleaning and normalization earn space | raw indicator table, normalized score table | skipped preprocessing |
| Model establishment | 5.8 | both score and planning layers need mathematical body | score equations, objective/constraints | disconnected layers |
| Solution process | 2.2 | candidate flow and solver settings should be visible | algorithm steps, parameter table | black-box solution |
| Results | 3.2 | ranking, candidates, and final plan all need interpretation | ranking table, candidate table, plan table | artifact dumping |
| Validation and sensitivity | 2.5 | feasibility and scenario checks are required | feasibility audit, scenario table | one-sentence validation |
| Strengths and limitations | 0.8 | should tie scope control to evidence | limitation-remedy table | generic praise |
| Conclusion | 0.7 | must close with executable recommendation | conclusion summary | soft wrap-up only |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.5 | extra scenarios and file inventory support traceability | file inventory, extra outputs | appendix replacing body |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 evaluation and screening | route fit and indicator design | evaluation model | score and ranking tables | rank stability table |
| Q2 executable plan | score-to-plan bridge | planning model | final plan table | feasibility audit |
| Q3 recommendation robustness | scenario logic | perturbation reruns | scenario summary table | sensitivity comparison |

## Final Check

- Where is the strongest mathematical density expected? `Model establishment`
- Which section is most likely to stay too thin? `Validation and sensitivity`
- What artifacts will prevent filler growth? `candidate table`, `plan table`, `feasibility audit`, `scenario table`
- Which family-specific abstract closure pattern should be used? `score -> plan -> audit`
