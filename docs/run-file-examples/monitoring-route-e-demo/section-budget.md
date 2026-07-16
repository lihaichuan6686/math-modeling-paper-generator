# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `19-22 pages`
- target appendix length: `4-6 pages`
- route family: `monitoring-route E`
- paper family: `diagnosis -> policy design -> consequence comparison`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close diagnosis, policy, and consequence evidence | method-result closure sentences | diagnostics-only summary |
| Problem restatement | 1.0 | task decomposition should stay compact | task table | copied statement |
| Method overview | 0.8 | diagnosis-to-policy route should appear early | workflow figure | route ambiguity |
| Problem analysis | 2.1 | policy burden and trigger burden need justification | dependency table, route note | descriptive setup only |
| Assumptions | 0.8 | signal and policy assumptions matter | assumption-impact table | hidden threshold assumptions |
| Symbols | 0.8 | diagnostic and rule variables must stay stable | symbol table | variable drift |
| Data processing | 2.9 | signal cleaning and feature reading earn real space | signal summary, feature table, diagnostic setup | decorative EDA |
| Model establishment | 5.8 | diagnosis and policy-rule layers both need technical body | diagnostic logic, rule equations or rule table | policy layer too short |
| Solution process | 2.0 | rule construction and comparison flow should be visible | algorithm steps, parameter table | black-box policy formation |
| Results | 2.8 | diagnostic and policy outputs both need interpretation | diagnostic artifact, policy table | policy bolted on |
| Validation and sensitivity | 3.0 | intervention or long-horizon comparison is central | consequence comparison artifact, robustness note | one-sentence validation |
| Strengths and limitations | 0.8 | should define horizon and assumption scope honestly | limitation-remedy table | broad management claims |
| Conclusion | 0.7 | must state the rule or policy and its studied scope | conclusion summary | detected-pattern-only close |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.2 | extra scenarios and support outputs belong here | file inventory, extra comparisons | appendix replacing body |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 diagnosis | signal behavior and pattern burden | diagnostic model | diagnostic artifact | stability or fit note |
| Q2 policy rule | diagnosis-to-policy bridge | monitoring/policy model | rule/policy table | trigger or threshold note |
| Q3 recommendation | consequence interpretation | comparison logic | recommendation summary table | intervention or long-horizon comparison |

## Final Check

- Where is the strongest mathematical density expected? `Data processing + model establishment`
- Which section is most likely to stay too thin? `Diagnosis-to-policy bridge`
- What artifacts will prevent filler growth? `diagnostic artifact`, `policy table`, `consequence comparison`, `recommendation summary`
- Which family-specific abstract closure pattern should be used? `diagnosis -> policy -> consequence`
