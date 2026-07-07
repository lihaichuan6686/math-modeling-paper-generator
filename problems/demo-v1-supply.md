# Demo v1 Problem: Campus Supply Planning

This is a synthetic toy problem for testing the v1.0 toolchain. It is not a real contest problem and should not be presented as real evidence.

## Background

A campus cafeteria needs to purchase one raw material for the next 8 weeks. There are three suppliers. Each supplier has a weekly capacity, unit price, and estimated loss rate during transport. The cafeteria wants to meet weekly demand while controlling purchase cost, loss, and inventory fluctuation.

## Data

Weekly demand forecast:

| Week | Demand |
|---:|---:|
| 1 | 120 |
| 2 | 135 |
| 3 | 128 |
| 4 | 150 |
| 5 | 160 |
| 6 | 155 |
| 7 | 142 |
| 8 | 130 |

Supplier data:

| Supplier | Capacity | Unit price | Loss rate | Reliability |
|---|---:|---:|---:|---:|
| A | 90 | 10.0 | 0.03 | 0.93 |
| B | 80 | 9.5 | 0.06 | 0.88 |
| C | 70 | 10.8 | 0.02 | 0.96 |

Initial inventory: 20 units.

Safety inventory target: at least 15 units after each week.

## Tasks

1. Build an interpretable supplier evaluation score.
2. Design an 8-week ordering plan that meets demand and safety inventory.
3. Generate at least one figure and one table to support the plan.
4. Discuss limitations and what would be needed for a real CUMCM-scale problem.

## Expected v1.0 Route

```text
supplier evaluation -> greedy planning baseline -> inventory validation -> paper draft review
```

This demo intentionally uses a simple baseline so that the full paper-generation chain can be tested quickly.
