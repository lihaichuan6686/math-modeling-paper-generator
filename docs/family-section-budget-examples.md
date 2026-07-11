# Family Section Budget Examples

Purpose: provide ready-to-adapt `section-budget.md` examples for high-frequency CUMCM families.

Use this after choosing the route family and before filling `runs/current/section-budget.md`.

These are examples, not fixed laws. Adjust them to the actual number of subquestions and the real artifact burden.

## Example 1: Evaluation To Planning

Typical fit:

- supplier/material screening;
- candidate evaluation followed by ordering, assignment, or transport plan;
- final answer must be executable.

### Target

- target paper tier: `v1.2`
- target total body length: `19-22 pages`
- target appendix length: `4-6 pages`
- route family: `evaluation to planning`
- paper family: `evaluation -> planning -> feasibility audit`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close score, plan, and validation | abstract-level result sentences | ending at ranking only |
| Problem restatement | 1.0 | task decomposition is needed but should stay compact | task decomposition table | restatement padding |
| Method overview | 0.8 | route bridge from evaluation to planning should appear early | route flow figure | too generic |
| Problem analysis | 2.2 | must explain why ranking alone is insufficient | route comparison table | formula jump too early |
| Assumptions | 0.8 | planning constraints need explicit assumptions | assumption-impact table | generic assumptions |
| Symbols | 0.8 | variables split into score layer and decision layer | symbol table | undefined decision variables |
| Data processing | 2.5 | indicator cleaning and normalization earn real space | raw indicator table, normalized score table | skipping preprocessing logic |
| Model establishment | 5.8 | evaluation model and planning model both need mathematical body | weight table, objective/constraint equations | one layer too short |
| Solution process | 2.2 | candidate flow and solver settings matter | algorithm steps, parameter table | only saying `solved by Python` |
| Results | 3.3 | ranking, selected candidates, and final plan all need interpretation | ranking table, selected-candidate table, plan table | artifact dumping |
| Validation and sensitivity | 2.4 | feasibility and scenario evidence are required | feasibility audit, scenario table | token validation |
| Strengths and limitations | 0.8 | should tie strengths to executable outputs | limitation-remedy table | generic praise |
| Conclusion | 0.7 | must close with actionable recommendation | conclusion summary | repeating abstract |
| References | 0.5 | methods and background only | bibliography | placeholder refs |
| Appendix | 4.5 | code inventory and extra scenario outputs support trust | file inventory, extra tables | replacing body logic |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 candidate screening | route fit and indicator design | evaluation model | weight and ranking table | rank stability table |
| Q2 executable planning | score-to-plan bridge | planning model | final decision table | feasibility audit |
| Q3 strategy comparison | scenario assumptions | scenario comparison logic | scenario recommendation table | sensitivity summary |

### Final Check

- strongest mathematical density expected: `model establishment`
- section most likely to stay thin: `validation`
- artifacts that prevent filler growth: `selected-candidate table`, `plan table`, `feasibility audit`, `scenario comparison`
- family-specific abstract closure pattern: `score -> plan -> audit`

## Example 2: Forecast To Decision

Typical fit:

- demand/load/sales/traffic forecast drives later planning;
- uncertainty matters to the final answer.

### Target

- target paper tier: `v1.2`
- target total body length: `20-23 pages`
- target appendix length: `4-6 pages`
- route family: `forecast to decision`
- paper family: `forecast -> decision -> uncertainty propagation`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close forecast, decision, and uncertainty | abstract-level result sentences | reporting forecast only |
| Problem restatement | 1.0 | task map should be compact | task table | background drift |
| Method overview | 0.8 | route from forecast to decision needs early visibility | workflow figure | model names only |
| Problem analysis | 2.0 | uncertainty burden needs justification | route comparison paragraph, dependency table | weak route explanation |
| Assumptions | 0.8 | temporal assumptions should be auditable | assumption table | hidden time assumptions |
| Symbols | 0.8 | forecast and decision variables both need stable naming | symbol table | symbol drift |
| Data processing | 3.5 | trend, seasonality, cleaning, and feature setup earn space | trend plot, cleaning table, feature table | skipping exploratory evidence |
| Model establishment | 5.4 | forecast model and decision model must both be explicit | forecast equations, decision equations | forecast body too thin |
| Solution process | 2.0 | train/test split and scenario generation should be visible | algorithm steps, parameter settings | black-box training |
| Results | 2.8 | forecast output and decision output both need interpretation | forecast table, decision table | no downstream explanation |
| Validation and sensitivity | 3.0 | backtest and scenario propagation are central | residual plot, backtest table, scenario table | weak uncertainty layer |
| Strengths and limitations | 0.8 | should state what uncertainty was and was not covered | limitation-remedy table | overclaiming |
| Conclusion | 0.7 | must state decision plus uncertainty boundary | conclusion summary | introducing new numbers |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.2 | extra scenarios and run notes belong here | file inventory, extra outputs | appendix-only evidence |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 trend diagnosis | signal reading and uncertainty role | forecast model | trend/forecast figure | backtest or residual table |
| Q2 decision output | forecast-to-decision bridge | planning / policy model | decision table | scenario comparison |
| Q3 recommendation | scenario interpretation | recommendation logic | strategy summary table | sensitivity summary |

### Final Check

- strongest mathematical density expected: `data processing + model establishment`
- section most likely to stay thin: `decision interpretation`
- artifacts that prevent filler growth: `trend figure`, `forecast table`, `decision table`, `scenario comparison`
- family-specific abstract closure pattern: `forecast -> decision -> uncertainty`

## Example 3: Geometry / Spatial Design

Typical fit:

- positioning, angle-only measurement, coverage design, geometric configuration.

### Target

- target paper tier: `v1.2`
- target total body length: `19-22 pages`
- target appendix length: `4-5 pages`
- route family: `geometry / spatial design`
- paper family: `scene setup -> derivation -> design result -> feasibility`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close geometric result and feasibility | abstract-level result sentences | ending with formulas |
| Problem restatement | 1.0 | scene/task rewrite should be concise | task decomposition table | copied statement |
| Method overview | 0.8 | scene-to-derivation route should be shown early | scene workflow figure | no route visibility |
| Problem analysis | 2.2 | needs scene interpretation and subquestion map | scene note, dependency table | skipping question logic |
| Assumptions | 0.8 | geometric simplifications matter | assumption table | unspoken simplifications |
| Symbols | 1.0 | symbol world is dense and must be stable | symbol table | symbol overload |
| Data processing | 1.2 | lighter than data-heavy families but still needed | known-parameter table | underdescribed setup |
| Model establishment | 6.8 | derivation is the technical center | coordinate schematic, equation blocks | weak mathematical body |
| Solution process | 2.4 | numerical procedure and case split need explanation | search/process figure, parameter table | hidden computation path |
| Results | 2.8 | final design/location outputs need readable presentation | result summary table, final scene figure | no physical interpretation |
| Validation and sensitivity | 2.5 | replay, overlap, residual, or feasibility closes the loop | replay figure, feasibility table | token check |
| Strengths and limitations | 0.8 | should define geometric scope honestly | limitation-remedy table | vague claims |
| Conclusion | 0.7 | should return to engineering meaning | conclusion summary | abstract repetition |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.0 | extra derivations and support outputs | file inventory, extra cases | too much body logic moved out |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 scene construction | coordinate choice and simplification | base geometry model | symbol/parameter table | consistency check |
| Q2 design computation | case split and constraints | main derivation | result summary table | replay or residual figure |
| Q3 comparative recommendation | alternative setup comparison | comparison logic | design comparison table | feasibility summary |

### Final Check

- strongest mathematical density expected: `model establishment`
- section most likely to stay thin: `result interpretation`
- artifacts that prevent filler growth: `scene schematic`, `equation group`, `result table`, `replay/feasibility figure`
- family-specific abstract closure pattern: `scene -> derivation -> design -> feasibility`

## Example 4: Rail / Timetable Service Planning

Typical fit:

- passenger flow, OD, headway, timetable, operation pattern, service-cost tradeoff.

### Target

- target paper tier: `v1.2`
- target total body length: `21-24 pages`
- target appendix length: `4-7 pages`
- route family: `rail / timetable service planning`
- paper family: `flow audit -> service design -> timetable -> feasibility`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close service pattern, timetable, and audits | abstract-level result sentences | timetable claim without feasibility |
| Problem restatement | 1.0 | task map should be clear and compact | task decomposition table | repeated statement |
| Method overview | 0.9 | multi-layer route needs early visibility | route workflow figure | late route clarity |
| Problem analysis | 2.6 | passenger-flow and service split need explanation | dependency table, route note | weak bridge to timetable |
| Assumptions | 0.9 | operation constraints must be explicit | assumption table | hidden operation assumptions |
| Symbols | 1.0 | operation variables and recurrence variables are dense | symbol table | symbol inconsistency |
| Data processing | 3.0 | OD, section flow, and parameters deserve real space | OD summary, section-flow figure, parameter table | underdeveloped flow audit |
| Model establishment | 6.4 | service design and timetable recurrence need depth | objective equations, recurrence equations | one layer underexplained |
| Solution process | 2.3 | selection and timetable generation should be transparent | algorithm steps, solver settings | black-box recurrence |
| Results | 3.4 | operation plan and timetable outputs must both appear | operation plan table, timetable figure | artifact dumping |
| Validation and sensitivity | 3.0 | capacity, tracking, dwell, and scenario checks are required | capacity audit, tracking/dwell audit, scenario table | one-token validation |
| Strengths and limitations | 0.8 | should state service scope honestly | limitation-remedy table | inflated claims |
| Conclusion | 0.7 | must summarize service-cost tradeoff | conclusion summary | unsupported recommendation |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 5.0 | full timetable and extra outputs belong here | file inventory, extra audit tables | appendix replacing body |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 service design | flow reading and service pattern logic | operation-plan model | selected operation-plan table | baseline comparison |
| Q2 timetable generation | operation-to-timetable bridge | recurrence/timetable model | timetable figure/table | tracking and dwell audit |
| Q3 recommendations | scenario interpretation | scenario logic | scenario recommendation table | capacity and sensitivity summary |

### Final Check

- strongest mathematical density expected: `model establishment`
- section most likely to stay thin: `operation-to-timetable bridge`
- artifacts that prevent filler growth: `section-flow figure`, `operation-plan table`, `timetable artifact`, `audit tables`
- family-specific abstract closure pattern: `flow -> service pattern -> timetable -> feasibility`

## Example 5: Dynamic Scheduling / Update

Typical fit:

- production scheduling, rolling planning, abnormal event response, cutting, batching, or disruption handling;
- the plan must change after a disturbance or update trigger.

### Target

- target paper tier: `v1.2`
- target total body length: `20-23 pages`
- target appendix length: `4-6 pages`
- route family: `dynamic scheduling / update`
- paper family: `baseline plan -> update rule -> adjusted plan -> comparison`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close baseline plan, update rule, and after-update result | abstract-level result sentences | mentioning baseline only |
| Problem restatement | 1.0 | static and dynamic tasks should be separated clearly | task decomposition table | mixed task description |
| Method overview | 0.8 | baseline-to-update route should be visible early | workflow figure | route ambiguity |
| Problem analysis | 2.2 | disturbance logic and update trigger need justification | dependency table, scenario note | weak update motivation |
| Assumptions | 0.8 | resource and disturbance assumptions matter to feasibility | assumption-impact table | hidden scenario assumptions |
| Symbols | 0.8 | baseline and update variables must stay consistent | symbol table | variable drift |
| Data processing | 2.0 | job/resource/scenario setup deserves real space | task-resource table, scenario table | underdescribed setup |
| Model establishment | 6.0 | baseline model and update logic both need mathematical body | baseline equations, update constraints | update layer too short |
| Solution process | 2.4 | rolling logic or solver flow needs explanation | algorithm steps, parameter table | black-box scheduling |
| Results | 3.0 | baseline and adjusted plans must both appear and be compared | baseline schedule, adjusted schedule, loss table | one-sided presentation |
| Validation and sensitivity | 2.8 | before/after audit and stress scenarios are central | constraint audit, scenario stress table | token robustness |
| Strengths and limitations | 0.8 | should say what type of disturbance is really covered | limitation-remedy table | overclaiming adaptability |
| Conclusion | 0.7 | must summarize update value and operational meaning | conclusion summary | abstract repetition |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.5 | extra scenarios and run logs support reproducibility | file inventory, extra schedules | appendix replacing argument |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 baseline schedule | resource/task logic | baseline scheduling model | baseline schedule table | feasibility audit |
| Q2 update rule | disturbance and trigger logic | update or rolling model | adjusted schedule table | before/after loss comparison |
| Q3 strategy recommendation | scenario interpretation | recommendation logic | strategy summary table | stress-test summary |

### Final Check

- strongest mathematical density expected: `model establishment`
- section most likely to stay thin: `abnormal-scenario comparison`
- artifacts that prevent filler growth: `baseline schedule`, `adjusted schedule`, `loss comparison`, `stress table`
- family-specific abstract closure pattern: `baseline -> update -> comparison`

## Example 6: Classification / Recognition

Typical fit:

- spectra, diagnosis, sample recognition, authenticity testing, high-dimensional feature classification;
- the final answer depends on preprocessing, feature extraction, and class-level evaluation.

### Target

- target paper tier: `v1.2`
- target total body length: `18-21 pages`
- target appendix length: `4-5 pages`
- route family: `classification / recognition`
- paper family: `preprocessing -> feature extraction -> classifier comparison -> error interpretation`

### Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 0.9-1.0 | must close preprocessing, recognition result, and class-level validation | abstract-level result sentences | accuracy-only summary |
| Problem restatement | 1.0 | task decomposition is usually compact | task decomposition table | copying the prompt |
| Method overview | 0.7 | preprocessing-to-classifier route should appear early | workflow figure | weak route visibility |
| Problem analysis | 1.8 | data type and recognition burden need explanation | route note, task table | superficial analysis |
| Assumptions | 0.7 | sampling and label assumptions should be explicit | assumption-impact table | hidden data assumptions |
| Symbols | 0.7 | lighter than optimization families but still needed | symbol table | undefined metrics |
| Data processing | 3.5 | cleaning, normalization, and feature construction earn major space | preprocessing table, feature table, exploratory figure | skipping preprocessing details |
| Model establishment | 4.8 | classifier comparison and final model selection need technical body | model comparison setup, metric definitions | one-model shortcut |
| Solution process | 1.8 | train/test or cross-validation flow should be visible | algorithm steps, split table | black-box training |
| Results | 2.5 | class-level findings need interpretation | classifier comparison table, confusion matrix | metric dumping |
| Validation and sensitivity | 2.5 | leakage check, split policy, and error analysis are central | confusion matrix, error-case figure, robustness note | weak class-level validation |
| Strengths and limitations | 0.8 | should state sample and generalization scope honestly | limitation-remedy table | inflated accuracy claims |
| Conclusion | 0.7 | must summarize recognition meaning, not just score | conclusion summary | repeating metrics only |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.0 | extra metrics and support outputs belong here | file inventory, extra plots | appendix-only evidence |

### Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 preprocessing and features | data quality and feature burden | preprocessing/feature route | preprocessing table, feature artifact | split/leakage note |
| Q2 classifier selection | comparison rationale | classifier comparison model | model comparison table | confusion matrix |
| Q3 recognition conclusion | error interpretation | recommendation logic | recognition summary table | error-case or robustness summary |

### Final Check

- strongest mathematical density expected: `data processing + model establishment`
- section most likely to stay thin: `error interpretation`
- artifacts that prevent filler growth: `preprocessing table`, `feature artifact`, `classifier comparison`, `confusion matrix`
- family-specific abstract closure pattern: `preprocessing -> classifier -> class-level result`
