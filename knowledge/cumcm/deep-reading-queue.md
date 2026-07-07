# CUMCM Deep Reading Queue

Purpose: organize long-term, batch-by-batch reading of CUMCM papers. Each deep read should produce generator rules, review criteria, algorithm-card updates, or LaTeX structure guidance.

## Completed

| Sample | Status | Output |
| --- | --- | --- |
| User awarded paper `LATEX/model1.pdf` | case study complete | `knowledge/latex/model1-case-study.md` |
| 2021 D017 | deep read complete | `knowledge/cumcm/deep-reading-2021D017.md` |
| 2021 A028 | deep read complete | `knowledge/cumcm/deep-reading-2021A028.md` |
| 2021 C066 | deep read complete | `knowledge/cumcm/deep-reading-2021C066.md` |
| 2021 E014 | deep read complete | `knowledge/cumcm/deep-reading-2021E014.md` |
| 2022 B030 | deep read complete | `knowledge/cumcm/deep-reading-2022B030.md` |
| 2022 C155 | deep read complete | `knowledge/cumcm/deep-reading-2022C155.md` |
| 2023 C050 | deep read complete | `knowledge/cumcm/deep-reading-2023C050.md` |
| 2023 D039 | deep read complete | `knowledge/cumcm/deep-reading-2023D039.md` |
| 2023 E176 | deep read complete | `knowledge/cumcm/deep-reading-2023E176.md` |
| 2021 A-E first pass | first pass complete | `knowledge/cumcm/2021-official-first-pass.md` |
| 2022 A-E first pass | first pass complete | `knowledge/cumcm/2022-official-first-pass.md` |
| 2023 A-E first pass | first pass complete | `knowledge/cumcm/2023-official-first-pass.md` |

## Priority Queue

### P0: One Official Excellent Paper Per Problem Type

Goal: build reliable route examples across A-E problem types.

| Priority | Sample | Reason | Expected extraction |
| ---: | --- | --- | --- |
| 1 | 2023 E same-problem comparison | learn structural variation within the same hydrology route | section-allocation differences, validation strength, appendix structure |

### P1: Same-Problem Comparison

Goal: compare multiple papers for the same problem to learn acceptable structural variation.

Recommended batches:

- 2021 D problem: compare D017 against another D paper if available.
- 2021 C problem: compare multiple supply-chain papers.
- 2023 C problem: compare dynamic pricing papers.
- 2023 E problem: compare monitoring/data-analysis papers.

Extraction focus:

- section order differences
- page allocation differences
- figure/table density
- validation strength
- appendix and code evidence
- how similar methods are written differently

### P2: Recent Complete Drafts and Code-Linked Materials

Goal: learn generator risks and paper-code consistency from recent complete artifacts.

Targets:

- 2024 A complete paper drafts
- 2024 B complete paper drafts
- 2024 C complete paper drafts
- 2024 D complete paper drafts
- 2024 E complete paper drafts
- any attached code or idea documents

Extraction focus:

- reproducibility gaps
- template/date/identity risks
- figure source traceability
- appendix-code alignment
- signs of generated-draft weakness

## Deep Reading Template

Every deep read should extract:

1. problem year and type
2. page count and section structure
3. abstract pattern
4. model chain
5. core algorithms and equations
6. data processing steps
7. figure and table inventory
8. validation and sensitivity strategy
9. strengths/limitations writing pattern
10. appendix and code reproducibility
11. reusable generator rules
12. review signals for paper-quality checking

## Output Naming

Use:

```text
knowledge/cumcm/deep-reading-<year><problem><paper-id>.md
```

Examples:

```text
deep-reading-2021A028.md
deep-reading-2021C066.md
deep-reading-2023C050.md
```

## Reading Order

1. Read horizontally across problem types: one A, B, C, D, E paper each.
2. Read vertically across years: compare how similar problem types change from 2021 to 2023.
3. Read recent complete drafts and code-linked materials to learn generator-risk patterns.
4. Convert each finding into one of:
   - route rule
   - model-chain pattern
   - algorithm-card update
   - figure/table requirement
   - LaTeX structure rule
   - quality-rubric item
