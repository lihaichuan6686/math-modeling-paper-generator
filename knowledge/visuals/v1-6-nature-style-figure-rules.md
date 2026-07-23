# v1.6 Nature-Style Figure Rules

Purpose: make concept and mechanism figures look like serious paper figures, not generic AI flowcharts.

## Visual Target

A v1.6 concept figure should resemble a compact journal mechanism diagram:

- grouped zones with dashed or lightly framed boundaries;
- clear left-to-right or top-to-bottom information flow;
- readable module labels after insertion into the PDF;
- restrained color palette with 2-4 soft accent colors;
- local highlights for key variables, decisions, or outputs;
- concise labels, not paragraph text inside boxes;
- caption and body prose that explain the figure's modeling role.

## Required Figure Spec

Before generating the concept figure, create `runs/current/figure-style-spec.md` with:

| Field | Required content |
|---|---|
| Figure role | concept / mechanism / model route / result explanation |
| Zones | 2-5 grouped regions and their titles |
| Nodes | node label, node role, zone |
| Edges | source, target, meaning |
| Highlights | key variables, thresholds, objective functions, or final decisions |
| Style | palette, frame style, font size, export size |
| PDF check | expected readable size in final paper |

## Preferred Generation Paths

Use deterministic or source-controlled generation first:

1. Python `matplotlib` patches and arrows for mechanism diagrams.
2. Graphviz for directed model route diagrams.
3. TikZ only when the model is simple enough to keep maintainable.
4. Mermaid or draw.io XML only when the final export is verified in the PDF.

Image-generation models may be used later for bitmap polish, but v1.6 should not depend on a private web UI. The first stable implementation must be reproducible by local code.

## Figure Design Rules

- Use 16:9 or 2:1 aspect ratio for concept figures.
- Export at least 2400 px wide for PNG or use PDF/SVG where the template supports it.
- Keep body labels above 8 pt after insertion.
- Avoid dense paragraphs inside boxes.
- Use English acronyms only when common in the problem domain; otherwise use Chinese labels.
- Avoid default plot titles such as `ROC Curve`, `Feature Importance`, or `Correlation Heatmap`.
- Use figure captions to interpret, not only name.

## Required Early Concept Figure

The first six pages should include one figure that shows:

```text
data objects -> modeling route -> result artifacts -> validation -> final decision
```

It should not look like a project workflow. It must be written in contest-paper language, focused on the problem mechanism.

## Common Repairs

| Problem | Repair |
|---|---|
| Labels too small | reduce nodes, split zones, or increase export size |
| Looks like a workflow checklist | rename nodes to domain objects and mathematical relations |
| Too many colors | use one neutral base plus two accents |
| Generic arrows | label key transitions, e.g. "risk scoring", "threshold optimization" |
| No interpretation | add a paragraph explaining how the figure motivates the model route |
