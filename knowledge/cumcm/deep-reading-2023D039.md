# Deep Reading: 2023 D039

Source: `D:\2-各比赛Word模板及LaTeX模板\国赛历年论文【公众号：竞赛资料网】整理\2023年高教社全国大学生数学建模竞赛优秀论文【公众号：竞赛资料网】\D039.pdf`

Problem type: spatial optimization and visualization.

Paper title observed from rendered PDF: circled lake sheep space utilization optimization.

Pages: 27 total.

- Pages 1-2: abstract, problem restatement, assumptions.
- Pages 3-4: symbol definitions and modeling overview.
- Pages 5-8: baseline production cycle logic, state tables, yearly output estimate.
- Pages 9-12: first model, fixed-cycle simplification, initial optimization result and plots.
- Pages 13-16: phased modeling for multiple subgroups and transition windows.
- Pages 17-19: iterative optimization, loss-cost curves, and best parameter selection.
- Pages 20-21: model evaluation and references.
- Pages 22-27: appendix code, including MATLAB generation and optimization routines.

Note: this paper is scan-like, so the note is based mainly on rendered-page visual inspection.

## Why This Paper Matters

This paper is a strong route example for spatial/production planning because it transforms a complicated biological process into a staged occupancy model:

```text
reproduction-cycle structure
-> state partitioning
-> yearly-output estimate
-> fixed-cycle simplification
-> batch-size/interval optimization
-> stochastic branch handling
-> loss-cost evaluation
-> visualization and code appendix
```

The useful lesson is that the paper does not try to solve every real-world detail at once. It first establishes a cycle-based abstraction that makes the problem mathematically manageable, then gradually adds stochastic branching and loss-cost analysis.

## Abstract Pattern

The abstract is concise but numeric. It reports:

- a baseline estimation of usable sheep pen count;
- a fixed-cycle simplification that makes the problem solvable;
- a grid-search style improvement to the cycle and batch sizes;
- the resulting annual output and space utilization;
- a stochastic-branch extension for uncertainty;
- a final loss minimum and a corresponding batch size.

Reusable rule:

```text
For optimization papers, the abstract should name the cycle or state abstraction and the final optimal parameter values.
```

## Section Structure

Observed main structure:

1. Abstract
2. Problem restatement
3. Model assumptions
4. Problem analysis
5. Symbol definitions
6. Model establishment and solution
   - problem 1: annual output / pen count estimation
   - problem 2: fixed batch planning
   - problem 3: uncertainty-aware planning
7. Model evaluation and improvement
8. References
9. Appendix code

Generator lesson:

- This paper uses a very contest-friendly structure: definition first, model second, evaluation last.
- The section order is stable and easy to imitate for other spatial/production optimization tasks.

## Model Chain

### Stage 1: State Abstraction

The first important move is to split the sheep life cycle into states such as:

- mating period;
- pregnancy;
- lactation;
- rest period;
- lamb stage.

The paper then defines the duration and capacity constraints for each state.

Generator rule:

```text
For biological or operational cycle problems, define the state space before optimization.
```

### Stage 2: Baseline Capacity Estimate

The paper first estimates yearly output and pen shortage from a simple ratio-based approximation. This gives a rough feasible range and clarifies the scale of the problem.

Observed artifacts:

- state-duration table;
- yearly output estimate table;
- shortage interval table;
- a baseline space-use plot.

Generator rule:

```text
Start with a coarse, auditable estimate before introducing a harder optimization model.
```

### Stage 3: Fixed-Cycle Simplification

Because the full problem is highly nonlinear and discrete, the paper fixes some quantities:

- fixed cycle length;
- fixed batch size per cycle;
- fixed interval length.

It then performs a search over candidate values and finds a better solution.

Observed artifacts:

- piecewise occupancy formulas by state;
- plot of global pen usage;
- optimized batch/interval figures;
- table of annual output versus batch size.

Generator rule:

```text
When the original model is too hard, explicitly state the simplification knobs and search over them.
```

### Stage 4: Subgroup and Transition Modeling

The paper then introduces multiple subgroups for pregnancy, lactation, and rest, because the same batch does not stay in one state forever. It uses piecewise definitions to account for:

- staggered pregnancy endings;
- overlapping lactation windows;
- resting-period carryover;
- the fact that some subgroups can merge.

Generator rule:

```text
For staggered production systems, use subgroup decomposition and time-window formulas instead of one monolithic count.
```

### Stage 5: Uncertainty and Loss-Cost Analysis

The third problem introduces uncertainty in pregnancy termination time and uses random variables to model the spread. The paper then:

- generates batch trajectories;
- computes expected loss cost;
- averages over a large iteration count;
- searches over batch size to minimize average loss.

Observed artifacts:

- loss-cost curve table;
- output curve for full and local stable periods;
- final optimum at batch size 40;
- appendix code that simulates random branching.

Generator rule:

```text
If uncertainty is present, the model must include both a stochastic branch generator and a numerical loss metric.
```

## Figure Inventory

Observed figure types:

- yearly usage curve;
- local stable-period usage curve;
- optimized batch-usage staircase plot;
- parameter search / loss curve;
- occupancy trajectory plots;
- state-flow and schedule visualizations.

Minimum generator requirement for similar problems:

- one diagram for the state structure;
- one plot for the baseline solution;
- one plot for the optimized solution;
- one plot for the sensitivity or search result;
- one plot for any stochastic or branching extension.

## Table Inventory

Observed table types:

- state duration and capacity table;
- batch-state time table;
- yearly output estimate table;
- pen shortage estimate table;
- phase/branch mapping table;
- result table for candidate batch sizes;
- code/file inventory in the appendix.

Generator rule:

```text
Use tables to encode the piecewise logic, especially when the model has many state windows.
```

## Appendix Pattern

The appendix is especially valuable here because it includes runnable support files:

- `f3.m`
- `numjp.m`
- `problem1.xlsx`
- `problem2.m`
- `problem2.xlsx`
- `problem3.m`
- `rdnump.m`

This is a good appendix pattern for the agent:

- list files by subproblem;
- keep MATLAB and spreadsheet dependencies explicit;
- make it easy to trace which file generated which plot or table.

## Quality Signals

Strong signals:

- the simplification is openly stated instead of hidden;
- the paper uses stepwise optimization rather than claiming a direct closed form;
- uncertainty is handled with a separate branch and a cost metric;
- the final answer is a concrete batch size and utilization value, not just a method name;
- appendix code mirrors the staged structure of the paper.

Risk signals:

- the paper is mathematically dense, so the explanation can be hard to follow if the state definitions are not tightened;
- the search-based simplification is practical, but a new generated paper should be more explicit about why the search range is sufficient;
- the appendix is code-rich but not fully self-documenting.

## Reusable Generator Rules

1. Define the process states before modeling.
2. Build a coarse baseline estimate before fine optimization.
3. When a nonlinear model is intractable, simplify with explicit fixed knobs and search them.
4. Use piecewise formulas for state windows and overlapping transitions.
5. For multi-stage production systems, divide subgroups by state transitions.
6. If uncertainty matters, add a stochastic branch and an expected loss metric.
7. Include plots for both the baseline and optimized schedules.
8. Put code files in the appendix with a clean file-to-subproblem mapping.

## Revisions Needed Elsewhere

- Add a spatial/production planning archetype to the problem-type library.
- Strengthen the generation playbook with cycle-based state abstraction and piecewise occupancy formulas.
- Add a rule that simplification choices must be explicit and search ranges must be justified.
