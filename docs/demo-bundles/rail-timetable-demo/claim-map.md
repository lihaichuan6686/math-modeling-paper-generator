# Rail-Timetable Claim Map

Purpose: show how abstract and conclusion claims should be tied to artifacts for a rail/timetable v1.2 paper.

## Claim Rule

No sentence belongs in the abstract or conclusion unless it can be traced to:

1. a generated table, figure, timetable output, or audit result;
2. an entry in `artifact-ledger.md`;
3. a stable subquestion in the paper question map.

## Abstract Claim Map

| Claim slot | Claim type | What the sentence should do | Expected evidence source | Ledger tie |
|---|---|---|---|---|
| A1 | task framing | state that the paper solves demand-to-service-to-timetable planning | `problem-analysis.md`, route note | optional narrative tie |
| A2 | Q1 flow/service signal | state what flow burden or overlap-zone logic motivates the route | section-flow figure or related analysis artifact | supporting evidence entry |
| A3 | Q2 selected plan | state which service pattern was selected and the main operational consequence | selected-plan table, comparison output | K01/K02 or equivalent decision entries |
| A4 | Q3 timetable/audit result | state that the selected plan yielded a feasible timetable and summarize the audit boundary | timetable artifact, capacity/tracking/dwell audits, scenario table | K03-K05 or equivalent validation entries |
| A5 | final recommendation | state the final operating recommendation in bounded form | combined plan and audit evidence | combined ledger references |

## Conclusion Claim Map

| Claim slot | Claim type | What the sentence should do | Expected evidence source | Ledger tie |
|---|---|---|---|---|
| C1 | Q1 close-out | restate what flow concentration pattern supports the chosen route | flow artifact and analysis section | supporting evidence entries |
| C2 | Q2 close-out | restate the selected operation plan and why it was preferred | selected-plan and comparison artifacts | decision entries |
| C3 | Q3 close-out | restate what feasibility and scenario evidence the recommendation survives | timetable artifact and audit/scenario outputs | validation/scenario entries |
| C4 | limitation boundary | name the main operating simplification without inventing new evidence | strengths/limitations section | no unsupported numbers |

## Safe Sentence Pattern

Use this rhythm:

```text
artifact-backed operation result
-> what it means for service and timetable design
-> what the audits confirm or still limit
```

Avoid this rhythm:

```text
selected plan mention
-> timetable mention
-> recommendation with no audit boundary
```

## Common Failure Checks

Fail the draft if:

- the abstract claims timetable feasibility without naming any audit burden;
- the conclusion recommends a service pattern not tied to the selected-plan artifact;
- capacity, tracking, or dwell evidence is silently collapsed away;
- one of the three subquestions disappears between abstract and conclusion.
