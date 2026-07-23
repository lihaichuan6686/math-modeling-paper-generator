# v1.6 calibration Visual Generation Decision

Purpose: decide how a CUMCM paper generator should create figures when the target is human-team paper feel, not decorative output.

Use this with:

- `knowledge/visuals/v1-6-nature-style-figure-rules.md`
- `docs/visual-generation-pipeline.md`
- `docs/figure-plan-template.md`
- `docs/v1.6-calibration-log-template.md`

## Decision Principle

Every figure must first be classified by evidence role:

```text
numeric evidence -> reproducible code
validation evidence -> reproducible code
concept/mechanism -> controlled schematic
visual polish reference -> external image workflow allowed
```

Do not use image-generation models for numeric evidence. Use them only for schematic or aesthetic support after the modeling content is fixed.

## Tool Decision Matrix

| Figure need | Preferred path | Allowed fallback | Forbidden use |
|---|---|---|---|
| distribution, trend, residual, error, sensitivity | Python/R/MATLAB plotting | none, unless recreated by code later | AI-generated charts |
| confusion matrix, ROC, clustering, network metric | Python/R/MATLAB plotting | Graphviz for network layout with data-derived edges | invented metrics or labels |
| route overview, model chain, subquestion dependency | Graphviz, Mermaid, TikZ, Python patches | external image model for polish after source-controlled draft | decorative workflow with no problem objects |
| geometry or physical mechanism | TikZ, Python patches, CAD-like vector drawing | external image model as schematic reference only | fake measured dimensions or impossible physical objects |
| Nature-style concept figure | source-controlled vector/raster draft from `figure-style-spec.md` | high-quality external image model if prompt and review notes are recorded | unreviewed bitmap dropped into PDF |
| appendix/support-file map | table or Graphviz | none | full-page decorative diagrams |

## Three-Path Workflow

### Path A: Reproducible Evidence Figure

Use for result and validation figures.

Required records:

- input data;
- script path;
- output path;
- caption;
- artifact-ledger entry;
- rendered PDF readability check.

Acceptance standard:

```text
If the figure disappeared, the numerical claim would become weaker.
```

### Path B: Code-Native Schematic

Use for route, mechanism, concept, geometry, and process figures when accuracy and maintainability matter.

Recommended tools:

- Graphviz for graph and route structure;
- Python `matplotlib` patches for grouped zones, arrows, and mechanism diagrams;
- `scripts/generate-concept-figure.py` for a source-controlled first draft from a JSON spec; it can output SVG without `matplotlib` and PNG when the plotting environment is ready;
- TikZ for compact mathematical or geometric diagrams;
- Mermaid only when the final export is verified and does not look like a software workflow.

Acceptance standard:

```text
The figure names problem objects, model transformations, result artifacts, and validation logic.
```

### Path C: External Image Model Polish

Use only when the paper needs a high-quality schematic and code-native output looks too crude.

Required records:

- source draft or `figure-style-spec.md`;
- prompt summary;
- generated image path;
- manual review notes;
- statement that it is schematic, not evidence;
- replacement plan if text is unreadable or content is wrong.

Acceptance standard:

```text
The bitmap improves first-look paper feel without adding claims that the model did not prove.
```

## Prompt Shape For External Image Models

Use compact technical prompts:

```text
Create a clean academic mechanism diagram for a mathematical modeling paper.
Subject: <problem object and decision object>.
Show grouped zones: <2-5 zones>.
Show key variables and transformations: <list>.
Style: white background, restrained 2-4 color palette, thin lines, readable labels, journal-style schematic.
Avoid: decorative background, 3D glamour, fake data, extra text, unreadable small labels, AI workflow boxes.
```

If Chinese labels are likely to render poorly, generate with short English placeholders and replace labels in code/vector editing before insertion.

## Review Gates

A visual fails v1.6 calibration if:

- it is body-critical but not listed in `artifact-ledger.md`;
- it supports a numeric claim but was not generated from code;
- it looks like a generic project workflow rather than a problem mechanism;
- labels are unreadable in the final PDF;
- it contradicts variables, tables, or equations;
- no nearby paragraph interprets why it matters.

## Current Recommendation

For v1.6 calibration, use this default:

1. evidence and validation figures: code only;
2. early concept figure: first create a code-native schematic from `figure-style-spec.md`, preferably with `scripts/generate-concept-figure.py` when a zone-node-edge structure fits;
3. if first-look quality is poor, use an external image model only as a schematic-polish pass;
4. always record the prompt/source and manual review in the artifact ledger;
5. let user-side generated-paper tests decide whether a dedicated helper script is needed.
