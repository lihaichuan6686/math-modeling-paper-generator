# National Problem-Family Methodology Matrix

Purpose: compress recurring CUMCM-style problem families into one practical decision sheet that connects task family, modeled object, decision object, route logic, evidence burden, visual burden, and fake-completion risks.

Use this file after first intake and before route selection becomes fixed.

This note is not a replacement for the deeper archetype and card notes. It is the fastest way to answer:

```text
What kind of paper is this really?
What decision must it end with?
What evidence will a reviewer expect?
What weak shortcut is most tempting here?
```

## How To Use

1. Match the problem to one primary family.
2. Record the modeled object and decision object in `problem-profile.md`.
3. Copy the route logic into `route-decision.md`.
4. Plan the minimum required evidence and visuals before coding.
5. Check the fake-completion column before drafting the abstract.

## Matrix

| Family | Typical problem signals | Modeled object | Decision object | Route logic | Minimum evidence burden | Minimum visual burden | Common fake-completion risk |
|---|---|---|---|---|---|---|---|
| Evaluation and ranking | indicators, alternatives, screening, score comparison | alternative set with indicator system | ranked shortlist or recommendation | indicator design -> normalization -> weighting/ranking -> sensitivity -> recommendation | weight table, ranking table, stability or comparison evidence | indicator figure, ranking figure/table, sensitivity figure | stopping at a score list when the task really asks for a plan or policy |
| Evaluation to planning | ranking must become quantities, schedules, assignments | candidate system under constraints | executable plan or allocation decision | evaluation -> candidate set -> planning model -> feasibility -> scenario comparison | candidate table, decision table, feasibility audit, scenario evidence | route figure, plan table, feasibility table/plot | ranking and planning are disconnected, so the plan looks arbitrary |
| Forecast to decision | time series, trend, uncertainty, future planning | time-evolving demand/risk/process | plan, policy, or capacity decision under forecast | exploration -> forecast comparison -> chosen forecast -> decision model -> uncertainty propagation | train/test or backtest evidence, forecast table, scenario decision evidence | trend plot, fit/forecast plot, scenario figure | treating forecasts as certain and skipping uncertainty propagation |
| Classification and recognition | labels, diagnosis, recognition, abnormality judgment | labeled feature system | judgment rule or classifier-based screening decision | feature diagnosis -> baseline classifier -> comparison -> threshold/policy layer -> error analysis | split policy, comparison table, confusion evidence, threshold logic | feature or distribution figure, ROC/PR or confusion figure | showing one AUC and claiming the decision rule is complete |
| Geometry and engineering mechanics | coordinates, surfaces, reflection, physical constraints | geometric scene or physical system | feasible design, angle, location, or parameter decision | object description -> coordinate frame -> derivation/model -> numeric solution -> residual/feasibility check | parameter table, derivation closure, residual or physical-feasibility evidence | scene diagram, geometry/process figure, residual or comparison plot | optimizing before the object and coordinate frame are clearly defined |
| Production planning and scheduling | batches, machines, capacities, rolling updates | production/resource system over time | executable production or scheduling plan | demand/resource reading -> planning model -> rolling update or abnormal scenario -> comparison | plan table, capacity feasibility, update-rule evidence, scenario comparison | workflow figure, schedule/production table, capacity figure | listing quantities without explaining rolling logic or disturbance response |
| Graph and network | nodes, edges, paths, coverage, flows | network topology with capacity or distance structure | route, path, layout, or coverage decision | network construction -> path/flow logic -> optimization or comparison -> bottleneck audit | network definition, route/path table, bottleneck or coverage evidence | network figure, edge/path table, bottleneck visual | skipping reproducible network construction and jumping to an answer |
| Queue and service systems | arrivals, waiting, congestion, service rate | service queue or congestion system | staffing, service level, or dispatch recommendation | queue description -> utilization/waiting analysis -> intervention plan -> stress check | waiting/utilization table, bottleneck evidence, peak-condition check | service-flow figure, utilization/waiting plot, comparison table | quoting average waiting results without peak-condition evidence |
| Experimental factor optimization | factors, levels, yield, selectivity, process conditions | factor-response system | optimal factor setting or operating condition | factor design -> regression/ANOVA -> response surface -> optimum -> domain validation | coefficient table, significance or fit evidence, optimum verification | factor plot, response surface/contour plot, optimum summary table | reporting a mathematical optimum outside the valid experimental region |
| Rail / timetable service planning | OD, section flow, headway, dwell, route pattern | passenger-flow and service-operation system | selected operation plan and feasible timetable | flow audit -> service candidates -> selected plan -> timetable recurrence -> audits -> recommendation | selected plan artifact, full timetable, capacity/tracking/dwell audits, scenario evidence | early system figure, flow figure, timetable figure, audit table/figure | producing a timetable plot without machine-readable schedule or audits |
| Production-route E | demand, inventory, support rate, rolling production | demand-to-production support system | production quantities, inventory, service-level decision | demand analysis -> forecast -> service/inventory logic -> rolling production plan -> scenario/capacity audit | forecast evidence, production table, service/support evidence, scenario comparison | demand/forecast figure, service/inventory figure, production table | ending at forecasting and never producing an executable production decision |
| Monitoring-route E | monitoring, abruptness, periodicity, sampling, policy effect | monitored system with diagnosis and intervention structure | monitoring rule, sampling scheme, or policy recommendation | diagnosis -> forecast -> monitoring/policy design -> intervention comparison -> long-horizon effect | diagnostic evidence, monitoring/policy table, intervention or comparison evidence | process figure, diagnostic figure, policy-effect or long-horizon figure | stacking diagnostics without closing them into a monitoring or policy scheme |

## Fast Decision Questions

For a new problem, answer these six questions in order:

1. What is the modeled object?
2. What is the decision object?
3. Which family above matches the real task best?
4. What visible artifact will prove the decision was actually produced?
5. What validation artifact will stop the paper from looking shallow?
6. What fake-completion shortcut is most tempting here?

If the answer to question 4 or 5 is still unclear, the route is not ready.

## Best Use

Read this note together with:

- `problem-understanding-framework.md`
- `problem-type-paper-archetypes.md`
- `route-index.md`
- `../algorithms/route-selection-protocol.md`
- `../algorithms/route-method-matrix.md`
