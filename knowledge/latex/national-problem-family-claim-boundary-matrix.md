# National Problem-Family Claim Boundary Matrix

Purpose: define what each common CUMCM problem family can safely claim in the abstract and conclusion, what quantified closure is expected, and what overclaim patterns should trigger a rewrite.

Use this note after:

- the route is chosen;
- the artifact ledger is populated;
- the abstract and conclusion are being drafted or repaired.

This file complements two nearby layers:

- the methodology matrix answers what the paper must model and decide;
- the evidence matrix answers what proof artifacts the paper must show;
- this note answers what the paper is allowed to say once those artifacts exist.

## How To Use

1. Identify the primary problem family.
2. Check the safe-claim row before drafting the abstract.
3. Verify that each closing sentence is backed by an artifact-ledger result.
4. Rewrite any sentence that exceeds the evidence actually shown.

## Matrix

| Problem family | Safe abstract claim | Safe conclusion claim | Expected quantified closure | Overclaim risk to avoid | Family-specific closeout warning |
|---|---|---|---|---|---|
| Evaluation and ranking | the paper constructs an indicator system, compares alternatives, and obtains a stable shortlist under tested weights | the recommended shortlist is credible within the tested weighting scheme and can support later human selection | top ranks, score gaps, and at least one sensitivity range or rank-stability statement | claiming the top-ranked option is objectively best in all settings | if the real task needs planning or policy, do not let the paper stop at ranking language |
| Evaluation to planning | the paper first screens candidates and then derives an executable allocation, ordering, or assignment plan | the recommended plan satisfies the stated constraints and performs better than the compared baseline or scenario | plan totals, feasibility counts, utilization/service metrics, and at least one comparison delta | claiming the plan is globally optimal or universally deployable without scenario limits | the conclusion must close on the plan, not on the candidate score table |
| Forecast to decision | the paper forecasts the key variable and uses the forecast to produce a downstream decision | the recommendation remains reasonable within the tested prediction-error or scenario range | forecast error metrics, main decision quantities, and at least one uncertainty or scenario statement | treating the forecast as certain or claiming long-term accuracy beyond the tested horizon | the closing sentence must say what the forecast changed in the decision layer |
| Classification and recognition | the paper extracts features, compares classifiers, and selects a recognition route with acceptable multi-metric performance | the selected rule is usable for the studied classes under the reported error tradeoff | accuracy plus precision/recall/F1 or confusion-level evidence, and when relevant a threshold statement | claiming near-human diagnosis or general clinical/field deployment from one benchmark split | the conclusion should mention error structure, not only headline accuracy |
| Geometry and engineering mechanics | the paper models the geometric or physical scene and derives a feasible design or parameter set | the final configuration satisfies the main geometric or physical constraints under the tested assumptions | final parameters, residual/coverage/feasibility numbers, and when relevant comparison with alternative designs | calling the design exact, unique, or engineering-ready when only contest-level assumptions were tested | never close with formula prestige; close with the physical meaning of the design |
| Production planning and scheduling | the paper builds a constrained planning model and produces an executable schedule or production table | the recommended plan is feasible and remains operationally acceptable under the tested disturbance or rolling-update cases | production/schedule quantities, capacity feasibility, tardiness/cost/service metrics, and disturbance comparison | claiming real-world dispatch robustness without abnormal-case evidence | if rolling updates matter, the paper must close on adaptation quality, not only the base plan |
| Graph and network | the paper constructs the network object and derives a route, layout, or coverage decision | the recommended network decision is supported by the stated topology and the reported bottleneck/coverage audit | route lengths, coverage/connectivity metrics, and at least one bottleneck or comparison statement | claiming best network performance without showing how the graph was built or checked | conclusions should name the chosen structure and why it is acceptable, not just list nodes or paths |
| Queue and service systems | the paper models the service mechanism and derives a staffing or dispatch recommendation | the recommendation improves waiting, utilization, or congestion behavior under the studied demand conditions | waiting/utilization indicators, peak-period metrics, and before/after or peak/off-peak comparison | claiming full congestion elimination or system-wide optimality from average metrics only | the closeout must mention peak-condition behavior if peak load is part of the task |
| Experimental factor optimization | the paper fits a factor-response relation and identifies a candidate operating region or optimal setting | the recommended factor setting is valid within the tested domain and supported by fit or residual evidence | fitted coefficients or significance cues, optimum settings, and domain-validation or residual numbers | claiming the mathematical optimum is physically reliable outside the experimental domain | conclusions must include domain validity, not just the optimum coordinate |
| Rail / timetable service planning | the paper designs service candidates, selects one, and generates a feasible timetable under recurrence constraints | the recommended service pattern and timetable balance service and operating metrics within the audited assumptions | service frequencies, timetable outputs, capacity/headway/dwell audit values, and scenario tradeoff numbers | claiming deployable timetable quality without full schedule artifacts or audits | the final paragraph should end on the timetable policy or service pattern, not only passenger-flow analysis |
| Production-route E | the paper links demand analysis and forecasting to production or inventory decisions | the proposed production strategy maintains the reported support/service performance within the tested capacity and scenario range | forecast error, production quantities, support/service/inventory metrics, and scenario comparison numbers | claiming supply assurance without service-level or inventory consequence evidence | do not stop at demand forecasting; the closeout must contain the production consequence |
| Monitoring-route E | the paper links diagnosis and forecasting to a monitoring rule, sampling plan, or policy scheme | the proposed monitoring or policy route reduces risk or improves detection behavior within the studied horizon | diagnostic metrics, rule/policy parameters, intervention or long-horizon comparison numbers | claiming broad management effectiveness when only descriptive diagnostics were shown | the last sentence must state the policy or monitoring rule, not only the detected pattern |

## Sentence-Level Guardrails

When drafting the abstract or conclusion, prefer:

- `within the tested scenario range`
- `under the stated assumptions`
- `the results indicate`
- `the recommended strategy`
- `the reported comparison suggests`

Use with caution and only when the evidence is unusually strong:

- `robust`
- `effective`
- `optimal`
- `reliable`

Avoid unless the paper truly proves them:

- `best in all cases`
- `fully solves`
- `universally applicable`
- `can be directly deployed`
- `guarantees`

## Fast Rewrite Prompts

If a closing sentence feels too strong, repair it by asking:

1. What exact artifact proves this sentence?
2. Is the claim about ranking, decision, feasibility, or deployment?
3. Does the sentence need a scope limiter such as tested horizon, scenario range, or stated assumptions?
4. Would a cautious human team make this same sentence after seeing only the current evidence?

## Best Use

Read this note together with:

- `national-abstract-and-closeout-playbook.md`
- `human-style-soft-rules.md`
- `../cumcm/national-problem-family-methodology-matrix.md`
- `../quality/national-problem-family-evidence-matrix.md`
- `../../docs/v1.2-draft-contract.md`
