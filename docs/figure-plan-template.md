# Figure Plan Template

Use this template at:

```text
runs/current/figure-plan.md
```

Purpose: plan figures before writing the full CUMCM-style paper. A modeling paper without figures is usually not persuasive enough, and a figure added after writing often fails to support the logic.

For LaTeX placement and caption rules, also follow:

```text
knowledge/community/visual-evidence-chain-rules.md
knowledge/latex/figures-tables-equations-style.md
knowledge/latex/national-problem-family-visual-matrix.md
knowledge/cumcm/recent-award-paper-visual-rhythm.md
docs/visual-generation-pipeline.md
```

## Figure Strategy

Target count for a full 20-30 page paper:

- 1 route/workflow figure
- 2-4 explanatory figures
- 3-6 evidence/result figures
- 1-2 validation or sensitivity figures

For a stronger v1.4 award-feel draft, plan not only total count but placement rhythm:

- page 1: no decorative figure unless the template requires it; preserve dense abstract space;
- pages 4-6: at least one early model artifact such as symbol table, route/model diagram, data table, parameter table, or equation group;
- pages 8-12: recurring formulas, tables, figures, or model artifacts with interpretation;
- middle body: avoid more than 2-3 consecutive artifact-light pages in model-heavy problems.

## Planned Figures

| ID | Subquestion | Role | Purpose | Body-critical? | Paper section | Source type | Tool | Input data/source/prompt | Output path | Nearby interpretation plan | Caption draft | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F01 | whole paper | route | Show overall model chain | Yes | Method overview | schematic | Mermaid/Python/TikZ | | paper/figures/ | paragraph after first citation explains route choices | | planned |
| F02 | Q1 | explanatory | Explain key model structure | Yes/No | Model section | schematic | | | paper/figures/ | | | planned |
| F03 | Q1 | evidence | Show data/result pattern | Yes | Results | reproducible code | Python/R/MATLAB | | paper/figures/ | | | planned |
| F04 | Q1 | validation | Show robustness/error | Yes | Validation | reproducible code | Python/R/MATLAB | | paper/figures/ | | | planned |

## Planned Tables

| ID | Subquestion | Role | Purpose | Body-critical? | Paper section | Source type | Input data/source | Output path/source | Nearby interpretation plan | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| T01 | whole paper | symbol/parameter | Define variables or parameters before heavy formulas | Yes | Assumptions/Symbols/Model setup | manual + model plan | | paper/tables/ | used later in formulas | planned |
| T02 | Q1 | result | Show direct answer for the subquestion | Yes | Results | code output | | paper/tables/ | interpret immediately after table | planned |
| T03 | Q1 | validation/comparison | Support reasonableness or route choice | Yes | Validation | code output/manual audit | | paper/tables/ | explain what passed/failed | planned |

## Placement Rhythm

| Page band | Required visual/evidence role | Planned artifacts | Risk if missing |
|---|---|---|---|
| Page 1 | dense abstract, no artifact crowding | | weak abstract surface |
| Pages 2-3 | problem restatement/analysis, route preview | | delayed modeling start |
| Pages 4-6 | early model evidence | | paper still looks like prose |
| Pages 8-12 | recurring model/result artifacts | | weak award-paper rhythm |
| Middle body | sustained formulas/tables/figures/algorithms | | artifact drought |
| Final body | validation, comparison, and final answers | | answer hidden in appendix |
| Appendix | code and supplementary tables | | appendix replaces main evidence |

## Body vs Appendix Boundary

Before drafting, decide which artifacts must stay in the body:

- final answer tables;
- key result figures;
- validation/sensitivity evidence;
- comparison artifacts;
- route or model diagrams needed to understand the solution.

Appendix may include:

- code excerpts;
- long intermediate tables;
- supplementary plots;
- raw output logs;
- support-file inventory.

Do not move the only copy of a final answer or validation artifact into the appendix.

## Figure Types

### Route or Workflow Figure

Use for:

- problem decomposition
- model chain
- code-to-paper workflow
- evaluation process

Accepted sources:

- Mermaid
- Python graph libraries
- LaTeX/TikZ
- manually drawn diagram with source file

### Explanatory Figure

Use for:

- geometry setup
- mechanism explanation
- variable relationship
- scheduling structure
- supply-chain structure

Accepted sources:

- Python plotting
- LaTeX/TikZ
- vector drawing
- AI image generation for schematic-only illustrations

Rules:

- Must be labeled as schematic when not data-derived.
- Must not invent data or imply measured evidence.
- Generation prompt or source file must be recorded.

### Evidence Figure

Use for:

- data distribution
- correlation matrix
- prediction curve
- optimization convergence
- simulation result
- confusion matrix
- error map

Accepted sources:

- reproducible code only

Rules:

- Must record input data.
- Must record script path.
- Must be reproducible.
- Must be listed in the artifact ledger.

### Validation Figure

Use for:

- sensitivity analysis
- residual distribution
- baseline comparison
- constraint violation audit
- scenario stress test

Accepted sources:

- reproducible code

Rules:

- Caption must state what is being validated.
- Axes and units must be clear.
- Perturbation range or validation setup must be stated.

## Caption Requirements

Each caption should answer:

```text
What is shown?
What does it support?
Which model/result does it connect to?
```

Weak caption:

```text
Figure 3. Prediction result.
```

Better caption:

```text
Figure 3. Rolling prediction of weekly demand under Model II. The curve shows that the model captures the main seasonal trend, while the residual peaks indicate underestimation during holiday weeks.
```

## Review Questions

Before writing:

1. Does each subquestion have at least one figure or table supporting it?
2. Is there a route/workflow figure near the method overview?
3. Are evidence figures reproducible from code?
4. Are explanatory figures clearly marked as schematic when needed?
5. Does every planned figure have a paper section?
6. Does the placement rhythm avoid delaying all artifacts until late pages?
7. Does every body-critical figure/table have a subquestion link, source, role, and planned nearby interpretation?
8. Are AI-generated visuals limited to schematic roles and excluded from numeric claims?
9. Are final-answer tables explicitly marked as body-critical?
10. Are table-only subquestions intentional, or do they need a figure for interpretation?

Before final PDF:

1. Does every figure file exist?
2. Is every figure cited in text?
3. Are captions specific?
4. Are labels, units, and legends readable?
5. Are generated schematic prompts or source files recorded in the artifact ledger?
6. Would the main paper still answer the problem if appendix code were removed?
7. Do `figure-plan.md`, `artifact-ledger.md`, and `paper/main.tex` agree on body-critical artifacts?

Allowed statuses:

- planned
- generated
- inserted
- rendered
- needs revision
- accepted
