# Demo v1 Problem: Synthetic Production-Route E Planning

This is a synthetic toy problem for testing the v1.0 toolchain. It is not a real contest problem and should not be presented as real evidence.

## Background

A central kitchen tracks weekly demand for three representative material groups. The management team wants a short-term production arrangement for the next four weeks. The arrangement should preserve service level, avoid negative inventory, and compare two capacity-use assumptions. The task is intentionally small, but it is shaped to resemble the production-route E papers summarized from `2022 E014` and `2022 E029`.

## Data

Historical weekly demand for three representative materials:

| Week | M1 | M2 | M3 |
|---:|---:|---:|---:|
| 1 | 32 | 22 | 18 |
| 2 | 35 | 24 | 17 |
| 3 | 31 | 26 | 19 |
| 4 | 38 | 27 | 20 |
| 5 | 40 | 28 | 19 |
| 6 | 39 | 30 | 21 |
| 7 | 43 | 31 | 23 |
| 8 | 45 | 33 | 24 |

Initial inventory and safety stock:

| Material | Inventory | Safety stock |
|---|---:|---:|
| M1 | 15 | 10 |
| M2 | 11 | 8 |
| M3 | 9 | 7 |

Two capacity scenarios:

| Material | Capacity k1 | Capacity k2 |
|---|---:|---:|
| M1 | 38 | 56 |
| M2 | 28 | 40 |
| M3 | 21 | 33 |

## Tasks

1. Select the representative materials and summarize their demand characteristics.
2. Build a short-term demand forecast for the next four weeks and compare it with recent actual behavior.
3. Construct a rolling production plan under a baseline capacity scenario.
4. Evaluate service level and minimum inventory.
5. Compare two capacity-use scenarios and report which one is safer or stronger.

## Expected v1.0 Route

```text
material screening -> forecast check -> rolling production rule -> service-level evaluation -> scenario comparison -> paper draft review
```

This demo intentionally uses a lightweight rolling-rule baseline so that the full production-route E paper chain can be tested quickly.
