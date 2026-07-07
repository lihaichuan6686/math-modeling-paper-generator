# Algorithm Card: Rail Timetable And Service Operation Planning

Use when a problem asks for train/bus operation plans, headways, large/small route patterns, timetables, or running diagrams under passenger demand.

This is a domain model chain rather than a single algorithm. Combine it with TOPSIS, integer programming, simulation, or Pareto filtering as needed.

## Problem Signals

- OD passenger-flow matrix;
- section passenger flow;
- train capacity;
- headway range;
- minimum tracking interval;
- station dwell-time rule;
- large/small route, express/local service, or turn-back station;
- requirement to output arrival/departure times.

## Core Objects

Decision variables:

- candidate small-route start/end stations;
- big-route and small-route train counts or frequencies;
- train type sequence;
- departure time, arrival time, and dwell time at each station;
- optional passenger assignment or service pattern.

Objective components:

- operating cost: train-km, fleet use, energy or unit operating cost;
- service level: waiting time, in-vehicle time, transfer/penalty time, crowding or capacity margin;
- robustness: demand sensitivity and tracking-margin reserve.

## Standard Model Chain

1. Build section passenger-flow profile from OD or provided section data.
2. Enumerate feasible service patterns, such as large-only, large/small route, or alternative turn-back stations.
3. For each pattern, compute raw objective components before normalization.
4. Filter infeasible plans using capacity, headway, ratio, and station-turnback rules.
5. Select a plan with Pareto dominance plus TOPSIS/entropy-weight scoring, or a clearly justified exhaustive weighted search.
6. Generate timetable using station arrival/departure recurrence.
7. Audit capacity, dwell time, tracking interval, and output-file completeness.
8. Run scenario analysis for demand, headway, route endpoints, and service ratio changes.

## Recurrence Skeleton

For train `k` and station `i`:

```text
arr[k,i] = dep[k,i-1] + run_time[i-1,i]
dwell[k,i] = clamp(base + passenger_exchange[k,i] * boarding_time, dwell_min, dwell_max)
dep[k,i] = arr[k,i] + dwell[k,i]
dep[k,i] >= dep[k-1,i] + tracking_min
```

If train `k` does not serve station `i`, document whether it passes through, turns back, or is absent from that station. Do not silently fill a passenger-stop dwell time for a non-stopping train.

## Required Outputs

Files:

- operation plan table, preferably `.xlsx` or `.csv`;
- full timetable output required by the problem;
- capacity audit by section;
- tracking/dwell audit by train and station;
- scenario analysis table.

Paper tables:

- parameter table with units;
- top candidate service plans;
- selected plan and raw objective components;
- timetable sample;
- feasibility audit;
- recommendation scenario table.

Figures:

- section passenger-flow bar chart;
- OD heatmap when OD data exist;
- cost-service Pareto or tradeoff plot;
- running diagram/timetable plot;
- sensitivity plot.

## Validation Checks

- Max section demand <= supplied capacity for every segment.
- Big-route-only sections are checked separately from overlap sections.
- Headway is within the stated lower/upper bounds.
- Minimum tracking interval is satisfied at every checked station.
- Dwell time remains within allowed range.
- Timetable file contains required rows/columns and station coverage.
- Selected plan is compared with at least one baseline, not only ranked internally.

## Review Risks

- Normalized objective values hide raw business meaning.
- Timetable is shown as a figure but no machine-readable output is saved.
- Small-route trains are treated inconsistently outside their service interval.
- The route-pattern choice is asserted without enumerating alternatives.
- Q3 advice is generic and not tied to scenario experiments.
- Axis labels remain in English in a Chinese contest paper.
