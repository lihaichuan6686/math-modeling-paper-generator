# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `20-23 pages`
- target appendix length: `4-6 pages`
- route family: `dynamic scheduling / update`
- paper family: `baseline plan -> update rule -> adjusted plan -> comparison`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close baseline plan, update rule, and revised result | method-result closure sentences | baseline-only summary |
| Problem restatement | 1.0 | static and dynamic tasks should be separated clearly | task table | mixed task narration |
| Method overview | 0.8 | baseline-to-update route should appear early | workflow figure | route ambiguity |
| Problem analysis | 2.2 | disturbance logic and update trigger need justification | dependency table, disturbance note | weak update motivation |
| Assumptions | 0.8 | resource and disturbance assumptions matter | assumption-impact table | hidden scenario assumptions |
| Symbols | 0.8 | baseline and updated variables must stay consistent | symbol table | variable drift |
| Data processing | 2.0 | task/resource/scenario setup deserves real space | task-resource table, scenario table | underdescribed setup |
| Model establishment | 6.0 | baseline model and update logic both need mathematical body | baseline equations, update constraints | update layer too short |
| Solution process | 2.4 | rolling logic or solver flow needs explanation | algorithm steps, parameter table | black-box scheduling |
| Results | 3.0 | baseline and revised plans must both appear and be compared | baseline schedule, revised schedule, comparison table | one-sided presentation |
| Validation and sensitivity | 2.8 | feasibility audit and stress scenarios are central | constraint audit, stress table | token robustness |
| Strengths and limitations | 0.8 | should say what disturbance scope is really covered | limitation-remedy table | overclaiming adaptability |
| Conclusion | 0.7 | must summarize update value and operational meaning | conclusion summary | abstract repetition |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.5 | extra scenarios and run logs support traceability | file inventory, extra schedules | appendix replacing argument |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 baseline schedule | resource/task logic | baseline scheduling model | baseline schedule table | feasibility audit |
| Q2 update rule | disturbance and trigger logic | update or rolling model | revised schedule table | before/after loss comparison |
| Q3 strategy recommendation | scenario interpretation | recommendation logic | recommendation summary table | stress-test summary |

## Final Check

- Where is the strongest mathematical density expected? `Model establishment`
- Which section is most likely to stay too thin? `Abnormal-scenario comparison`
- What artifacts will prevent filler growth? `baseline schedule`, `revised schedule`, `comparison table`, `stress audit`
- Which family-specific abstract closure pattern should be used? `baseline -> update -> comparison`
