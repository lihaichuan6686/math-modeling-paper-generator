# Route Decision

Run: example-geometry-spatial

## Selected Route Family

Geometry / spatial design.

## Question Map

- Q1 defines the scene and builds the coordinate layer
- Q2 computes the target design or positioning result
- Q3 validates or compares the configuration

## Route Chain By Subquestion

### Q1

scene reading -> coordinate choice -> geometric relations

### Q2

relations -> derivation or search -> numeric solution -> design artifact

### Q3

replay or residual check -> alternative comparison -> final recommendation

## Why This Route Fits The Decision Object

The final object is a feasible geometric configuration. Therefore the paper must begin with the scene, continue through the derivation, and close on a visible design plus a feasibility explanation.

## Why Rejected Routes Are Weaker

- derivation-only route: leaves the design meaning underexplained
- pure search route: weakens the transparency of geometric structure
- comparison-only route: cannot stand without one main feasible configuration

## Required Evidence Chain

- scene artifact
- relation or parameter summary
- final design artifact
- replay / residual / feasibility artifact

## Required Visuals

- scene schematic
- geometry/process figure if helpful
- result table or design figure
- feasibility or replay artifact

## Expected Failure Modes

- scene assumptions are too implicit
- symbols drift across subsections
- the final result is numerically correct but physically underexplained
