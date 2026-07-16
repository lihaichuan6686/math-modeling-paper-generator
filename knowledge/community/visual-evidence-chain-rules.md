# Visual Evidence Chain Rules

Purpose: make figures and tables part of the v1.4 reasoning chain, not decoration added after writing.

Local experience materials repeatedly emphasize that mathematical modeling relies on software, data processing, charts, and clear result presentation. Recent award-paper sampling also shows that strong papers expose artifacts early and keep them recurring through the model body.

## Core Rule

Every major figure or table must answer at least one of these questions:

- What is the problem structure?
- What data pattern or constraint matters?
- What model object is being built?
- What result answers a subquestion?
- What comparison proves the chosen route is better or at least reasonable?
- What validation, sensitivity, or robustness check supports trust?

If a figure or table answers none of these, remove it or replace it.

## Minimum Visual Set For v1.4

For a complete 20-30 page CUMCM-style draft, plan at least:

- one route/workflow figure near problem analysis or model overview;
- one data, parameter, or symbol table before heavy formulas;
- one result table for each major subquestion unless the answer is purely qualitative;
- one evidence/result figure for each data-heavy or computational subquestion;
- one validation, comparison, sensitivity, or error artifact when the route permits it.

For a stronger 30-45 page award-feel draft, add:

- baseline-vs-improved comparison artifacts;
- scenario or robustness figures;
- compact parameter and constraint audit tables;
- richer middle-body figures and tables with nearby interpretation.

## Placement Rules

Use this order:

```text
route figure
-> data/parameter/symbol table
-> model or algorithm artifact
-> result table/figure
-> validation or comparison artifact
-> final answer table
-> appendix support
```

Avoid:

- all figures appearing after the model is already finished;
- final answers appearing only in appendix code;
- a beautiful route diagram with no later result evidence;
- multiple charts that show the same thing without adding interpretation;
- AI-generated images that look polished but carry no modeling information.

## Evidence Status Labels

Label each visual artifact in `figure-plan.md` and `artifact-ledger.md`:

- `reproducible evidence`: generated from data, code, solver output, or simulation;
- `validation evidence`: generated from residuals, sensitivity, robustness, feasibility, or comparison checks;
- `schematic`: explanatory route, process, geometry, or algorithm diagram;
- `layout/review`: PDF screenshot or rendering check;
- `supplement`: appendix or support-file material.

Only `reproducible evidence` and `validation evidence` can support numeric claims.

`schematic` can support understanding, but not prove a result.

## Caption And Nearby Prose

Each caption should state:

- what is shown;
- where it came from;
- which subquestion or model step it supports.

Each important figure or table needs nearby interpretation.

Good nearby prose pattern:

```text
Figure/Table X shows ...
This supports Problem Y because ...
The main difference/trend/constraint violation is ...
Therefore the next model step is ...
```

Weak nearby prose:

```text
The result is shown in the following figure.
```

## AI Image Generation Boundary

AI image generation may be used for:

- conceptual route illustrations;
- clean process diagrams;
- simplified mechanism sketches;
- non-data explanatory schematics.

It must not be used for:

- fake data plots;
- invented experimental scenes;
- numeric result charts;
- official-looking diagrams that imply measurement or authority.

When AI image generation is used:

- record the prompt or source description;
- label the output as schematic;
- check labels and symbols manually;
- prefer Mermaid, TikZ, or code-drawn diagrams when exact structure matters.

## Review Failures

Fail the visual layer if:

- a major subquestion has no visible result artifact;
- final answer artifacts are not in the body;
- validation is claimed but no validation figure/table exists;
- charts have unreadable axes, units, legends, or labels;
- figures are cited but not interpreted;
- schematic images are presented as evidence;
- appendix visuals replace body explanation.

## Generator Instruction

Before drafting the paper, Claude Code should build `figure-plan.md` and decide:

- which artifacts are body-critical;
- which are appendix-only;
- which are reproducible from code;
- which are schematic;
- which subquestion each artifact supports;
- where each artifact should appear in the page rhythm.

After drafting, the review must compare `figure-plan.md`, `artifact-ledger.md`, and `paper/main.tex` to ensure every planned body-critical artifact exists, is cited, and is interpreted.
