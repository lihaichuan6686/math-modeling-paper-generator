# Spatial Measurement Comparison: B030, B086, B311

Purpose: capture the stable paper backbone shared by strong CUMCM-style spatial measurement papers, especially the kind that begin from geometry, visibility, coverage, direction, or measurement design rather than from generic optimization.

This is a route comparison note, not a full transcription.

## Sources

Official-paper anchors reviewed:

```text
2022 B030: 无人机纯方位无源定位
2022 B086: 基于局部最优模型的无人机位置调整策略与仿真定位
2023 B311: 基于主要目标法的测线设计问题
```

Rendered-page evidence used in this note:

```text
knowledge/_generated/b030_review/b030-01.png ... b030-09.png
knowledge/_generated/b086_review/b086-01.png ... b086-04.png
knowledge/_generated/b311_review/b311-01.png ... b311-04.png
```

## Why This Comparison Matters

These papers are not the same contest question, but they belong to one reusable family:

```text
spatial object or measurement scene
-> reference frame or scene geometry
-> per-question derivation or case split
-> numeric positioning / coverage / design result
-> feasibility, error, or comparison check
```

For the generator, this family is important because it teaches how a geometry-heavy paper grows into a full paper without relying on long code appendices or generic optimizer stacking.

## Shared Route Backbone

Across the three papers, the stable route is:

```text
object figure
-> problem restatement by subquestion
-> geometric variables and symbols
-> local derivation for each subquestion
-> computed design or positioning result
-> plausibility / comparison / boundary check
```

What changes between papers is the scene:

- `B030`: pure bearing and case-based positioning;
- `B086`: formation adjustment and local-optimal repositioning under directional constraints;
- `B311`: survey-line coverage design under seabed slope and overlap constraints.

The writing backbone stays surprisingly stable.

## Stable Structural Lessons

### 1. The first real page after the abstract identifies the scene

None of these papers can survive on prose-only problem restatement.

Observed early-page habits:

- `B030` shows the aircraft arrangement and angular relation right after restatement.
- `B086` quickly gives the formation scene, question map, and a problem-analysis flow figure.
- `B311` turns the problem restatement directly into geometric quantities like depth, coverage width, slope, overlap, and line direction.

Generator rule:

```text
For spatial measurement papers, the first strong figure should identify the measured object, vehicle arrangement, or coverage scene before the main equations expand.
```

### 2. Question-by-question derivation is more natural than one giant model block

These papers do not pretend every subquestion comes from one universal formula.

Observed pattern:

- `B030` splits by geometric case.
- `B086` treats static localization, adjustment logic, and simulation as linked but distinct loops.
- `B311` treats each question as a controlled extension of the previous geometry model.

Generator rule:

```text
If later subquestions are extensions of the same scene, keep the same symbol world but let each subquestion own its local derivation and result artifact.
```

This is a strong human-paper signal. It feels like a team solving the paper step by step rather than dropping one opaque global model.

### 3. Symbol tables are not optional in this family

`B311` makes this especially clear: assumptions, symbol explanation, and schematic come before the full derivation page.

`B030` and `B086` also rely on dense directional and positional notation, even when the symbol table is lighter.

Generator rule:

```text
If the route uses angles, coordinates, coverage widths, direction vectors, or multiple indexed objects, provide a symbol table before the longest derivation section.
```

### 4. Geometry papers still need a visible validation layer

The validation is not always a statistical error table.

Observed forms:

- `B030`: case consistency and scenario-based position interpretation;
- `B086`: adjustment effect, simulation-based verification, and before/after logic;
- `B311`: overlap-rate interpretation, boundary coverage logic, and design-feasibility checks.

Generator rule:

```text
For spatial measurement papers, validation may be geometric consistency, coverage feasibility, simulation replay, or before-after comparison, but it must still be visible.
```

Do not stop at "formula derived successfully".

## What Strong Human-Like B-Family Papers Do

### B030 lesson: make the case split carry the paper

This paper shows that when directional ordering changes the algebra, the case split is not a side note. It is the paper skeleton.

Generator upgrade:

- add a case-classification subsection;
- pair each case with one figure or equation group;
- close with a table or concise interpretation that says what each case means operationally.

### B086 lesson: add adjustment logic after localization

This paper is useful because it does not stop at "where are the drones".
It adds:

```text
position estimate -> local adjustment strategy -> simulation verification
```

Generator upgrade:

- if the scene includes formation, coordination, or movement, do not end at static coordinates;
- add one decision or adjustment layer;
- add one simulation or replay layer that tests whether the adjustment is credible.

### B311 lesson: turn geometry into full-paper length through layered closure

This paper is especially useful for `v1.2` because it shows how a geometry-heavy paper reaches full structure:

- one dense abstract that closes all questions;
- question-by-question restatement;
- problem analysis before assumptions;
- explicit assumptions;
- explicit symbol table;
- long derivation section;
- design interpretation and optimization closure.

Generator upgrade:

- use the same scene variables across questions;
- let each new question be an extension, not a reset;
- convert geometric derivation into design decisions, not just formulas.

## Shared Figure And Table Contract

For this family, the minimum strong-paper artifact set should usually include:

### Figures

- one global scene schematic;
- one question-map or workflow figure when the task has several linked subquestions;
- one case or local-geometry figure when the algebra changes by scene;
- one final design / trajectory / coverage / arrangement figure;
- one validation figure when simulation, overlap, or comparison is central.

### Tables

- symbol explanation table;
- parameter or known-condition table;
- per-question result summary table;
- validation or comparison table when several strategies or cases exist.

## v1.2 Writing Implications

This family is one of the best reminders that 20-30 pages do not have to come from filler.

The extra length should come from:

```text
scene explanation
-> assumptions
-> symbol table
-> per-question derivation
-> intermediate geometric interpretation
-> final design/result table
-> feasibility or comparison check
```

Not from:

- repeated generic modeling language;
- pages of equations with no scene figure nearby;
- results stated without explaining what they mean in the physical scene.

## Generator Rules Added

1. For spatial measurement papers, begin with an object-first scene figure before the longest derivation.
2. Keep one stable symbol world across subquestions, then extend it locally instead of restarting the model voice.
3. If geometry changes by case, let the case split structure the paper.
4. Add a post-positioning decision layer when the task includes adjustment, coordination, or design.
5. Use feasibility, overlap, replay, or geometric consistency as the validation layer when classic predictive error metrics do not fit.
6. In `v1.2`, use assumptions plus symbol table plus interpretation paragraphs to grow a geometry paper into contest-grade length without filler.

## Best Use

Read this note together with:

- `deep-reading-2022B030.md`
- `deep-reading-2021A028.md`
- `official-paper-paradigms.md`
- `route-index.md`
- `route-example-matrix.md`
