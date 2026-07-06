# Figure Plan Template

Use this template at:

```text
runs/current/figure-plan.md
```

Purpose: plan figures before writing the full CUMCM-style paper. A modeling paper without figures is usually not persuasive enough, and a figure added after writing often fails to support the logic.

For LaTeX placement and caption rules, also follow:

```text
knowledge/latex/figures-tables-equations-style.md
docs/visual-generation-pipeline.md
```

## Figure Strategy

Target count for a full 20-30 page paper:

- 1 route/workflow figure
- 2-4 explanatory figures
- 3-6 evidence/result figures
- 1-2 validation or sensitivity figures

## Planned Figures

| ID | Role | Purpose | Paper section | Source type | Tool | Input data/source/prompt | Output path | Caption draft | Status |
|---|---|---|---|---|---|---|---|---|---|
| F01 | route | Show overall model chain | Method overview | schematic | Mermaid/Python/TikZ | | paper/figures/ | | planned |
| F02 | explanatory | Explain key model structure | Model section | schematic | | | paper/figures/ | | planned |
| F03 | evidence | Show data/result pattern | Results | reproducible code | Python/R/MATLAB | | paper/figures/ | | planned |
| F04 | validation | Show robustness/error | Validation | reproducible code | Python/R/MATLAB | | paper/figures/ | | planned |

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

Before final PDF:

1. Does every figure file exist?
2. Is every figure cited in text?
3. Are captions specific?
4. Are labels, units, and legends readable?
5. Are generated schematic prompts or source files recorded in the artifact ledger?

Allowed statuses:

- planned
- generated
- inserted
- rendered
- needs revision
- accepted
