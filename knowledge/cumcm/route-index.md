# CUMCM Route Index

Purpose: give the generator a compact map from problem signal to route family, evidence pattern, and the first notes to read.

This is a classification index, not a full method manual.

## Route Families At A Glance

| Problem signal | Route family | Typical output | First notes |
|---|---|---|---|
| indicators, alternatives, screening, ranking | evaluation and ranking | score table, ranking, sensitivity | `problem-type-paper-archetypes.md` Type A, `official-paper-paradigms.md` |
| ranking that must turn into quantities or schedules | evaluation to planning | executable plan, feasibility audit | `problem-type-paper-archetypes.md` Type B |
| time series, trend, uncertainty, prediction | forecast to decision | forecast table, scenario or policy table | `problem-type-paper-archetypes.md` Type C |
| labels, spectra, many features, recognition | classification and recognition | classifier comparison, confusion evidence | `deep-reading-2021E014.md`, `cumcm-routing-rules.md` |
| coordinates, surfaces, geometry, physical constraints | geometry and engineering mechanics | schematic, formula set, numeric closure | `official-paper-paradigms.md`, `cumcm-routing-rules.md` |
| abnormal event, update rule, rolling adjustment | online optimization and process update | before/after plan, adjustment table | `official-paper-paradigms.md`, `problem-type-paper-archetypes.md` |

## E-Route Split

Use this split whenever an E-style problem mentions forecasting, production, service level, monitoring, or policy design.

| E signal | Route family | Anchor notes | What the final paper must show |
|---|---|---|---|
| demand, order quantity, inventory, support rate, rolling production | production-route E | `deep-reading-2022E014.md`, `deep-reading-2022E029.md` | forecast -> service or inventory -> executable production plan |
| monitoring, sampling, abruptness, periodicity, hydrology, policy effect | monitoring-route E | `deep-reading-2023E176.md` | diagnosis -> forecast -> monitoring or policy decision |

## Route Selection Rule

Use the following order when the problem statement first arrives:

```text
problem signal
-> route family
-> archetype
-> paper shape
-> required figures/tables
-> validation
```

Do not choose a method before the route family is clear.

## Current Coverage

- evaluation and ranking: structurally covered;
- evaluation to planning: structurally covered;
- forecast to decision: structurally covered;
- classification and recognition: covered by the 2021 E014 deep read;
- geometry and engineering mechanics: covered by the 2021 A028 deep read, the 2022 B030 deep read, and the spatial-measurement comparison note;
- online optimization and process update: covered by the 2021 D017 deep read;
- production-route E: covered by the 2022 E014 and 2022 E029 deep reads;
- monitoring-route E: covered by the 2023 E176 deep read.

## Next Reading Targets

The next useful additions are:

1. more same-problem comparison notes for common clusters;
2. a broader classification-route deep read set;
3. more route-specific evidence patterns for real-world contest attachments;
4. more LaTeX polish notes for dense Chinese tables, captions, and appendices.
