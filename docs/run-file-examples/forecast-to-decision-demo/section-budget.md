# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `20-23 pages`
- target appendix length: `4-6 pages`
- route family: `forecast to decision`
- paper family: `forecast -> decision -> uncertainty propagation`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 1.0 | must close forecast, decision, and uncertainty | method-result closure sentences | forecast-only summary |
| Problem restatement | 1.0 | compact task decomposition is enough | task table | copied statement |
| Method overview | 0.8 | forecast-to-decision bridge should appear early | workflow figure | model names only |
| Problem analysis | 2.0 | must justify why uncertainty matters | dependency table, route note | weak route logic |
| Assumptions | 0.8 | temporal and scenario assumptions matter | assumption-impact table | hidden time assumptions |
| Symbols | 0.8 | forecast and decision variables must stay stable | symbol table | symbol drift |
| Data processing | 3.4 | cleaning, trend reading, and feature setup earn real space | trend plot, feature table, cleaning table | decorative EDA |
| Model establishment | 5.5 | forecast and decision layers both need mathematical body | forecast equations, decision equations | disconnected layers |
| Solution process | 2.0 | train/test and scenario generation should be visible | algorithm steps, parameter table | black-box solution |
| Results | 2.9 | forecast and decision outputs both need interpretation | forecast artifact, decision table | no downstream explanation |
| Validation and sensitivity | 3.0 | backtest and scenario propagation are central | residual/backtest artifact, scenario table | one-metric validation |
| Strengths and limitations | 0.8 | should define uncertainty boundary honestly | limitation-remedy table | overclaiming |
| Conclusion | 0.7 | must close with decision plus uncertainty boundary | conclusion summary | certainty overreach |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.3 | extra scenarios and run notes support traceability | file inventory, extra outputs | appendix replacing body |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 trend and forecast | signal reading and forecast burden | forecast model | forecast table/plot | residual or backtest summary |
| Q2 decision output | forecast-to-decision bridge | decision model | recommendation table | constraint/feasibility check |
| Q3 stability of recommendation | scenario logic | propagation reruns | scenario comparison table | sensitivity summary |

## Final Check

- Where is the strongest mathematical density expected? `Data processing + model establishment`
- Which section is most likely to stay too thin? `Decision interpretation`
- What artifacts will prevent filler growth? `trend figure`, `forecast table`, `decision table`, `scenario comparison`
- Which family-specific abstract closure pattern should be used? `forecast -> decision -> uncertainty`
