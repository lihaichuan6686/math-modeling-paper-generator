# Section Budget

## Target

- target paper tier: `v1.2`
- target total body length: `18-21 pages`
- target appendix length: `4-5 pages`
- route family: `classification / recognition`
- paper family: `preprocessing -> feature extraction -> classifier comparison -> error interpretation`

## Section Budget

| Section | Target pages | Why this section deserves the space | Main planned artifacts | Thinness risk |
| --- | ---: | --- | --- | --- |
| Abstract | 0.9-1.0 | must close preprocessing, recognition result, and class-level validation | method-result closure sentences | accuracy-only summary |
| Problem restatement | 1.0 | task decomposition is usually compact | task table | copied statement |
| Method overview | 0.7 | preprocessing-to-classifier route should appear early | workflow figure | weak route visibility |
| Problem analysis | 1.8 | data type and recognition burden need explanation | route note, task table | superficial analysis |
| Assumptions | 0.7 | sampling and label assumptions should be explicit | assumption-impact table | hidden data assumptions |
| Symbols | 0.7 | lighter than optimization families but still needed | symbol table | undefined metrics |
| Data processing | 3.5 | cleaning, normalization, and feature construction earn major space | preprocessing table, feature artifact, exploratory figure | skipped preprocessing detail |
| Model establishment | 4.8 | classifier comparison and final selection need technical body | comparison setup, metric definitions | one-model shortcut |
| Solution process | 1.8 | train/test or cross-validation flow should be visible | algorithm steps, split table | black-box training |
| Results | 2.5 | class-level findings need interpretation | classifier comparison table, confusion artifact | metric dumping |
| Validation and sensitivity | 2.5 | leakage check, split policy, and error analysis are central | confusion artifact, error-case figure, robustness note | weak class-level validation |
| Strengths and limitations | 0.8 | should state sample and generalization scope honestly | limitation-remedy table | inflated accuracy claims |
| Conclusion | 0.7 | must summarize recognition meaning, not just score | conclusion summary | repeating metrics only |
| References | 0.5 | methods and domain background | bibliography | placeholder refs |
| Appendix | 4.0 | extra metrics and support outputs belong here | file inventory, extra plots | appendix-only evidence |

## Per-Subquestion Closure

| Subquestion | Analysis | Model | Result artifact | Validation artifact |
| --- | --- | --- | --- | --- |
| Q1 preprocessing and features | data quality and feature burden | preprocessing/feature route | preprocessing table, feature artifact | split/leakage note |
| Q2 classifier selection | comparison rationale | classifier comparison model | model comparison table | confusion artifact |
| Q3 recognition conclusion | error interpretation | recommendation logic | recognition summary table | error-case or robustness summary |

## Final Check

- Where is the strongest mathematical density expected? `Data processing + model establishment`
- Which section is most likely to stay too thin? `Error interpretation`
- What artifacts will prevent filler growth? `preprocessing table`, `feature artifact`, `classifier comparison`, `confusion artifact`
- Which family-specific abstract closure pattern should be used? `preprocessing -> classifier -> class-level result`
