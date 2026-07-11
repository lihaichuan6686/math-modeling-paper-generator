# Visual Generation Pipeline

Purpose: make figures a controlled part of the mathematical-modeling paper chain. A CUMCM paper needs figures, but each figure must have a role, source, and review status.

## Figure Classes

| Class | Source | Allowed tools | Evidence status |
| --- | --- | --- | --- |
| Evidence figure | data, code output, solver output, simulation output | Python, MATLAB, R, plotting libraries | reproducible evidence |
| Validation figure | residuals, errors, sensitivity, feasibility, uncertainty | Python, MATLAB, R, plotting libraries | reproducible evidence |
| Explanatory schematic | workflow, mechanism, geometry idea, algorithm flow | Mermaid, TikZ, vector drawing, image generation | schematic only |
| Format figure | route overview, paper navigation, appendix map | Mermaid, TikZ, vector drawing | schematic only |
| Review figure | PDF screenshots, layout inspection, comparison image | render tools, screenshots | review evidence |

AI image generation may be used for schematic and explanatory figures, but not to invent data-driven results.

## Pipeline

```text
figure need
-> classify figure role
-> choose source/tool
-> record in figure plan
-> generate file
-> save to paper/figures/
-> write caption
-> reference in LaTeX
-> inspect rendered PDF
-> update artifact ledger
```

## Tool Selection Rules

Use code-generated plots for:

- distributions
- time-series curves
- regression residuals
- optimization convergence
- confusion matrices
- sensitivity heatmaps
- simulation histograms
- network outputs derived from data

Use Mermaid, TikZ, vector drawing, or image generation for:

- model-route diagrams
- process flows
- algorithm workflows
- conceptual mechanism diagrams
- simplified geometry sketches when exact coordinates are not yet known

Use rendered PDF screenshots for:

- layout review
- table overflow detection
- figure caption readability
- page-by-page inspection

## AI-Generated Schematic Rules

An AI-generated schematic must:

- be labeled as schematic in the artifact ledger;
- have a prompt or source description recorded;
- not show numerical results unless those numbers come from code outputs;
- not imply experimental evidence;
- be checked for wrong symbols, unreadable labels, and invented objects;
- be replaceable by Mermaid/TikZ/vector drawing if accuracy matters.

## Artifact Ledger Fields

Every figure entry should include:

```text
figure_id:
paper_section:
role:
source_type:
source_file_or_prompt:
generation_tool:
output_path:
caption_draft:
status:
review_notes:
```

Recommended statuses:

- planned
- generated
- inserted
- rendered
- needs revision
- accepted

## Figure Prompt Template

For schematic image generation:

```text
Create a clean academic schematic for a CUMCM mathematical modeling paper.
Subject: [model/process/geometry]
Must show: [required objects]
Must avoid: numerical claims, decorative background, extra labels, unreadable text
Style: simple technical diagram, white background, thin lines, clear Chinese/English labels if needed
Output role: schematic explanation, not data evidence
```

For route diagrams, prefer Mermaid or TikZ before raster image generation.

## Caption Contract

A useful caption should answer:

- What is shown?
- Which data/model produced it?
- What should the reader notice?
- Which subquestion does it support?

Bad caption:

```text
Figure 3: Result.
```

Good caption pattern:

```text
Figure 3: Sensitivity of total transport loss to carrier capacity. The curve is generated from the integer-planning model under five capacity scenarios and supports the robustness check for Problem 2.
```

Contest-style upgrade note:

- local awarded samples often use shorter captions, but the generator should usually prefer more explicit captions when the paper is intended for `v1.2` review and later research use.
- for route-specific caption and nearby-prose examples, prefer the `caption-map.md` notes inside `docs/demo-bundles/`.

## Review Checklist

Before accepting a figure:

- Is the role clear: evidence, validation, explanatory, format, or review?
- Is the source recorded?
- If evidence, can it be regenerated?
- If schematic, is it clearly non-evidential?
- Is the caption specific?
- Is the figure referenced and interpreted in text?
- Does the rendered PDF show readable labels at final size?
- Does the figure avoid contradicting tables, equations, or code outputs?
