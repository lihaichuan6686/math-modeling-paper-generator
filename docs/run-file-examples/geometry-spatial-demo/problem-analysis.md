# Problem Analysis

Run: example-geometry-spatial

## Problem Summary

The task is not only a derivation exercise. The paper must turn the scene into a stable coordinate description, compute the target configuration, and then explain what the final result means physically or geometrically.

## Subquestions

1. Build the scene description and the coordinate/geometric relations.
2. Solve for the design, positioning, or coverage result under the stated constraints.
3. Validate or compare the resulting configuration.

## Inputs

- known coordinates, distances, or angles;
- scene assumptions and simplifications;
- design or feasibility constraints;
- optional comparison settings for alternative configurations.

## Outputs

- coordinate system and relation set;
- numeric or visual design result;
- feasibility, residual, replay, or comparison evidence;
- final engineering-style recommendation.

## Constraints

- symbols must remain consistent across subquestions;
- geometric relations must reflect the visible scene;
- design variables must remain interpretable;
- feasibility checks must use the same assumptions as the derivation.

## Evaluation Metrics

- residual or consistency error;
- coverage / overlap / distance / angle indicators;
- feasibility under stated constraints.

## Routing Signals

- the scene must be visible before optimization;
- the body needs alternation between derivation and interpretation;
- a design result without replay or feasibility evidence will look shallow.

## Selected Route

Primary route:

```text
scene setup -> coordinate model -> derivation -> numeric solution -> feasibility/replay
```

Rejected route:

- symbolic derivation only: too weak because the final configuration is not made visible;
- numerical search only: too weak because the geometry burden becomes opaque.

## Artifact Intent

- analysis section: task decomposition table and scene note;
- model section: coordinate schematic and grouped equations;
- result section: final design table and scene result figure;
- validation section: replay, residual, or feasibility artifact.

## Risks and Missing Information

- scene simplifications may distort the final design;
- multiple feasible solutions may need comparison;
- physical interpretation may be lost if only equations are emphasized.

## Questions for Human Confirmation

- Is the final recommendation expected to prioritize precision, coverage, or implementation simplicity?
- Are alternative configurations worth comparing even if one main solution already satisfies the constraints?
