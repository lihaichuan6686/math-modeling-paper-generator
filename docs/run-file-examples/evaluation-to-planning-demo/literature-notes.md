# Literature Notes

Run family: evaluation-to-planning-demo

This is an example shape, not a real citation list. Replace placeholder sources with real sources during a live run.

## Search Purpose

- domain vocabulary: define evaluation object, criteria layer, intervention object, and planning decision.
- variable definitions: normalize indicator direction, weights, scores, constraints, and decision variables.
- method candidates: compare entropy weight, AHP, TOPSIS, PCA, clustering, linear/integer programming, and scenario simulation.
- data-source hints: identify official statistical yearbooks, policy standards, or domain datasets.
- validation ideas: use rank stability, weight sensitivity, scenario comparison, and feasibility checks.
- citation requirements: support nontrivial weighting, evaluation, planning, and validation methods.

Do not use this note to collect final rankings or copied plans.

## Source Table

| Source | Type | Role | Extracted idea | Used in run file | Citation needed? |
|---|---|---|---|---|---|
| Official statistical or policy source | data/domain | Defines indicator meaning, units, and policy constraints | Data definitions should come before normalization | `data-inventory.md`, `problem-analysis.md` | yes |
| Multi-criteria evaluation method source | method | Supports TOPSIS or weighted scoring assumptions | Candidate evaluation route should state why distance/ranking is appropriate | `model-candidates.md`, `route-decision.md` | yes |
| Weighting method source | method | Supports entropy/AHP/combined-weight choice | Weighting route should match data reliability and subjective criterion need | `model-plan.md` | yes |
| Planning or optimization method source | method/validation | Supports turning evaluation results into allocation or intervention decisions | Planning model must have objective, constraints, and scenario comparison | `model-plan.md`, `verification-plan.md` | yes |
| Similar domain evaluation paper | domain/validation | Shows typical validation such as sensitivity of weights or rank robustness | Use as validation idea, not as copied indicator system | `verification-plan.md` | maybe |

## Depth-First Source Trail

| Anchor source | What it simplifies | Main variables | Method chain | Validation style | Follow-up references or method names |
|---|---|---|---|---|---|
| A relevant multi-criteria evaluation paper | It turns a many-indicator domain problem into normalized scores and ranks | indicator matrix, weights, positive/negative ideal values, comprehensive score | indicator selection -> normalization -> weighting -> ranking -> sensitivity | weight perturbation and rank stability | TOPSIS, entropy weight, AHP, CRITIC, PCA |
| A relevant planning/optimization source | It turns ranked needs into resource allocation or intervention choice | decision variable, budget, capacity, benefit, risk, fairness constraint | score input -> objective function -> constraints -> scenario comparison | feasibility and trade-off comparison | linear programming, integer programming, goal programming |

## Run-File Conversions

| Signal | Run file changed | Change made | Reason |
|---|---|---|---|
| Evaluation route needs defensible indicators | `problem-analysis.md` | Add indicator source and direction check before modeling | Prevent scoring from looking arbitrary |
| Weighting method must match evidence | `route-decision.md` | Compare entropy-only, AHP-only, and combined weights | Avoid decorative weighting formulas |
| Planning decision needs constraints | `model-plan.md` | Add objective, decision variable, budget/capacity constraints, and feasibility output | Evaluation score alone is not a decision |
| Validation should test rank stability | `verification-plan.md` | Add weight perturbation and top-k rank stability check | Makes ranking credible |
| Citations should support method and data claims | `paper/main.tex` | Place citations next to indicator source, weighting method, and planning method claims | Avoid bibliography padding |

## Citation Duties

| Citation duty | Planned source | Paper location |
|---|---|---|
| method | Weighting/evaluation method source | evaluation model subsection |
| data | Official statistics, standard, or contest attachment | data preprocessing subsection |
| domain | Domain policy or background source | problem analysis or indicator construction |
| validation | Similar evaluation/planning paper or method source | validation subsection |
| software | Solver/library documentation only when material | appendix or implementation note |

## Rejected Or Deferred Sources

| Source | Reason rejected or deferred |
|---|---|
| Answer-only blog with final rank list | Answer-copying risk; no transferable method reasoning |
| Generic textbook citation with no body use | Decorative unless a specific formula or method is used |
| Similar paper with different indicator meaning | Deferred unless the indicator definitions match the current problem |

## Review Gate

- no source is used as copied solution text: yes
- every nontrivial method/data/domain/validation claim has citation support or is marked unsupported: planned
- decorative references are removed: planned
- unresolved placeholders remain visibly marked: planned
- literature signals and online-consensus signals are not mixed together: yes
