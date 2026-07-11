# Rail-Timetable Caption Map

Purpose: show how figure/table captions and nearby interpretation paragraphs should read in a rail/timetable v1.2 paper.

## Caption Rule

For this route family, every important figure or table should answer three things:

1. what service, timetable, or audit object is shown;
2. why it belongs to the current subquestion;
3. what operational conclusion the reader should notice.

## Figure Caption Map

| Artifact role | Weak caption pattern | Strong caption pattern | What the nearby prose should explain |
|---|---|---|---|
| route figure | rail workflow | Overall route from passenger-flow audit to service-pattern selection, timetable generation, and feasibility verification. | why the route begins with flow evidence instead of timetable drawing |
| service-pattern schematic | service pattern | Candidate large-small-route service structure before timetable recurrence. | how the selected service structure is logically organized |
| section-flow figure | passenger flow | Section passenger-flow profile used to identify the overlap zone and justify differentiated service. | where the burden is concentrated and why it motivates the service split |
| timetable/result figure | timetable result | Timetable consequence of the selected large-small-route service pattern. The figure shows how the overlap-zone reinforcement appears in the final service structure. | how the selected plan materializes into visible timetable behavior |
| capacity validation figure | capacity check | Capacity validation of the selected timetable under the audited service pattern. The remaining margin indicates whether the overlap zone is still adequately served. | whether the timetable satisfies the key burden requirement |
| scenario validation figure | scenario result | Scenario comparison of the final recommendation under disturbed demand or interval settings. | where the recommendation remains feasible and where risk begins to grow |

## Table Caption Map

| Artifact role | Weak caption pattern | Strong caption pattern | What the nearby prose should explain |
|---|---|---|---|
| candidate-plan table | candidate results | Candidate operation plans for the large-small-route service comparison. | which alternatives are being compared before selection |
| selected-plan table | final plan | Selected operation plan balancing service burden and operating cost under the overlap-zone requirement. | why this plan is preferred over nearby alternatives |
| timetable sample table | timetable | Representative timetable extract generated from the selected operation plan. | how the selected service structure appears in station-level output |
| capacity audit table | capacity audit | Section-capacity audit for the selected timetable and service pattern. | which sections are tight and whether the main burden is covered |
| tracking audit table | tracking audit | Tracking-interval audit of the generated timetable. | whether train separation remains operationally feasible |
| dwell audit table | dwell audit | Station dwell-time audit of the generated timetable. | whether station handling assumptions remain acceptable |
| scenario table | scenario result | Scenario comparison of timetable feasibility and service burden under disturbed conditions. | whether the recommendation survives beyond the baseline setting |

## Interpretation Paragraph Pattern

Use this rhythm after an important figure or table:

```text
identify the artifact's role
-> state the main operational pattern
-> connect the pattern to the subquestion
-> state what the audit or next layer must still confirm
```

Example rhythm:

```text
Figure X is not merely a timetable picture; it is the concrete consequence of the selected service pattern.
The denser overlap-zone service indicates that the chosen plan is responding to the central passenger burden rather than distributing trains uniformly.
This answers the operation-plan question, but not yet the feasibility question.
The next audit tables therefore test whether the same timetable still satisfies capacity, tracking, and dwell constraints.
```

## Common Failure Checks

Fail the draft if:

- a timetable caption says only that a timetable exists;
- the section-flow figure is not interpreted as route evidence;
- the selected-plan table is not connected to a timetable or audit consequence;
- audit captions do not state what constraint is being checked.
