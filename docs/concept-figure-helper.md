# Concept Figure Helper

Purpose: provide a reproducible first draft for early concept, mechanism, and model-route figures.

Script:

```text
scripts/generate-concept-figure.py
```

This helper belongs to Path B in `knowledge/visuals/v1-6-visual-generation-decision.md`: code-native schematic.

## When To Use

Use it when the paper needs an early figure showing:

```text
data objects -> modeling route -> result artifacts -> validation -> final decision
```

Do not use it for:

- numeric result charts;
- validation plots;
- response surfaces;
- confusion matrices;
- any figure that supports a numeric claim.

Those must come from reproducible analysis code.

## Quick Start

Create a starter JSON spec:

```powershell
python .\scripts\generate-concept-figure.py --write-example .\runs\current\concept-figure-spec.json
```

New v1.6 run scaffolds already create `runs/current/concept-figure-spec.json`; use `--write-example` only when the file is missing or you need a fresh sample outside a run.

Edit the JSON so labels name the actual problem objects, variables, result artifacts, and validation checks.

Generate the figure:

```powershell
python .\scripts\generate-concept-figure.py --spec .\runs\current\concept-figure-spec.json --out .\paper\figures\concept_route.png
```

If the current Python environment lacks `matplotlib`, generate a source-controlled SVG draft first:

```powershell
python .\scripts\generate-concept-figure.py --spec .\runs\current\concept-figure-spec.json --out .\paper\figures\concept_route.svg
```

Use PNG for the final LaTeX insert when possible. Use SVG as a reviewable source draft or as input for later vector editing / external schematic polish.

Then record the figure in:

- `runs/current/figure-style-spec.md`
- `runs/current/figure-plan.md`
- `runs/current/artifact-ledger.md`

## JSON Shape

The spec has four main parts:

```json
{
  "title": "Model route concept figure",
  "subtitle": "schematic only",
  "zones": [
    {"id": "data", "title": "Data objects"}
  ],
  "nodes": [
    {"id": "input", "zone": "data", "label": "Problem data", "highlight": false}
  ],
  "edges": [
    {"source": "input", "target": "model", "label": "clean"}
  ]
}
```

## Review Standard

Before inserting the image into LaTeX:

- labels are readable after PDF insertion;
- nodes name problem objects, not project workflow tasks;
- arrows describe modeling transformations;
- highlighted nodes are key result or validation artifacts;
- the caption states that the figure is schematic when needed;
- the artifact ledger records the script, spec, output path, and review notes.

If the code-native output is structurally correct but visually too crude, use it as the source draft for an external image-model polish pass and record that decision in the artifact ledger.
