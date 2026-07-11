# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `21-24 pages`
- target appendix length: `5-7 pages`
- route family: `rail / timetable service planning`
- paper family: `flow audit -> service design -> timetable -> feasibility`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close service pattern, timetable, and audits | method-result closure sentences | timetable claim without feasibility |
| Problem restatement | 1.0 | task decomposition should stay compact | task table | repeated statement |
| Method overview | 0.9 | multi-layer route needs early visibility | route workflow figure | late route clarity |
| Problem analysis | 2.6 | passenger-flow and service split need explanation | dependency table, route note | weak bridge to timetable |
| Assumptions | 0.9 | operation constraints must be explicit | assumption-impact table | hidden operation assumptions |
| Symbols | 1.0 | operation and recurrence variables are dense | symbol table | symbol inconsistency |
| Data processing | 3.0 | OD, section flow, and parameters deserve real space | OD summary, section-flow figure, parameter table | underdeveloped flow audit |
| Model establishment | 6.4 | service design and timetable recurrence need depth | objective equations, recurrence equations | one layer underexplained |
| Solution process | 2.3 | selection and timetable generation should be transparent | algorithm steps, solver settings | black-box recurrence |
| Results | 3.4 | operation plan and timetable outputs must both appear | operation plan table, timetable figure | artifact dumping |
| Validation and sensitivity | 3.0 | capacity, tracking, dwell, and scenario checks are required | audit tables, scenario table | one-token validation |
| Strengths and limitations | 0.8 | should state service scope honestly | limitation-remedy table | inflated claims |
| Conclusion | 0.7 | must summarize service-cost tradeoff | conclusion summary | unsupported recommendation |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 5.0 | full timetable and extra outputs belong here | file inventory, full timetable excerpt | appendix replacing body |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 service design | flow reading and service-pattern logic | operation-plan candidate model | candidate and selected-plan tables | baseline comparison |
| Q2 timetable generation | operation-to-timetable bridge | recurrence/timetable model | timetable figure/sample | tracking and dwell audits |
| Q3 operating recommendation | scenario interpretation | scenario comparison logic | recommendation summary table | capacity and scenario summary |

## Final Check

- Where is the strongest mathematical density expected? `Model establishment`
- Which section is most likely to stay too thin? `Operation-to-timetable bridge`
- What artifacts will prevent filler growth? `section-flow figure`, `selected-plan table`, `timetable artifact`, `audit tables`
- Which family-specific abstract closure pattern should be used? `flow -> service pattern -> timetable -> feasibility`
