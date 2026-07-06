# Graph Algorithms Card

Purpose: support modeling of networks, routes, flows, matching, connectivity, coverage, and dependency structures.

## Use When

- Entities and relationships naturally form nodes and edges.
- The task asks for shortest path, minimum cost, maximum flow, matching, spanning tree, centrality, or coverage.
- Network constraints are central to the problem.
- Graph outputs can be visualized and audited.

## Avoid When

- Spatial geometry matters more than network topology and should be modeled continuously.
- Edges or weights are invented without data.
- The graph is only a decorative diagram.
- Time dynamics require scheduling or simulation beyond a static graph.

## Required Inputs

- Node set and meaning.
- Edge set and direction.
- Edge weights, capacities, costs, distances, or probabilities.
- Source/sink, demand pairs, or matching requirements.
- Constraints such as connectivity, capacity, coverage, or precedence.

## Mathematical Objects

Examples:

```text
shortest path: minimize sum c_ij x_ij
max flow: maximize sum flow from source subject to conservation and capacity
minimum spanning tree: connect all nodes with minimum total edge weight
matching: select disjoint edges maximizing weight or feasibility
```

## Outputs

- Selected edges or paths.
- Network cost, distance, flow, or coverage.
- Bottleneck nodes/edges.
- Feasibility or connectivity audit.
- Scenario comparison.

## Figure and Table Expectations

- Network diagram with labeled nodes and edge weights.
- Path or selected-edge highlight figure.
- Edge/result table.
- Bottleneck or centrality ranking table.
- Flow distribution plot when relevant.

## Validation

- Check graph construction against raw data.
- Verify conservation, capacity, and connectivity constraints.
- Compare with simple baseline routes or random alternatives.
- Test sensitivity to edge weights.
- If geographic, compare graph distance with spatial distance assumptions.

## CUMCM Writing Pattern

1. Define the network abstraction.
2. State node, edge, weight, and constraint construction.
3. Select the graph algorithm and mathematical formulation.
4. Present result both as diagram and table.
5. Audit feasibility and sensitivity.

## Common Risks

- Graph abstraction hides important real-world constraints.
- Edge weights are arbitrary.
- Diagram and result table disagree.
- Directed and undirected edges are confused.
- A static graph is used for a dynamic problem without explanation.

## Review Checks

- Are nodes and edges reproducible from data?
- Are weights meaningful and unit-consistent?
- Is the selected algorithm matched to the objective?
- Are constraints audited?
- Does the figure show the actual solution?
