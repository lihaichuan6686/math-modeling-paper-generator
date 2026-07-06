# CUMCM LaTeX Section Contract

Purpose: define what every CUMCM-style paper section must do before the agent writes LaTeX. A 20-30 page paper should emerge from a complete section structure, not from padded prose.

## Global Contract

Every final paper should satisfy:

```text
section purpose -> required evidence -> figures/tables -> LaTeX artifact -> review check
```

Rules:

- Each section must have a distinct job.
- Each subquestion must appear in problem analysis, model establishment, results, and validation.
- Figures and tables must be planned before final writing.
- Abstract and conclusion are written after all results are verified.
- Long sections should be long because they contain formulas, algorithms, figures, tables, and explanation.

## Main File Contract

`paper/main.tex` should:

- use `\documentclass[withoutpreface]{cumcmthesis}` for research/electronic copies unless a cover page is intentionally reviewed
- define title, problem number, and dates explicitly
- include section files in stable order
- keep abstract near the top
- keep references and appendix at the end
- avoid template default names, school names, team numbers, and stale dates

Recommended section order:

```latex
\input{sections/01_problem}
\input{sections/02_analysis}
\input{sections/03_assumptions}
\input{sections/04_symbols}
\input{sections/05_data}
\input{sections/06_model}
\input{sections/07_solution}
\input{sections/08_results}
\input{sections/09_validation}
\input{sections/10_strengths_limitations}
\input{sections/11_conclusion}
```

## Abstract

Target length: about 1 page.

Must include:

- overall problem target
- method and result for each subquestion
- validation method
- most important quantified conclusions
- 4-6 keywords

Must avoid:

- unsupported numbers
- generic background-only writing
- algorithm lists without results
- results that differ from later tables

LaTeX notes:

- Use concise paragraphs, usually one paragraph per subquestion.
- Write the final abstract after `08_results` and `09_validation` are stable.

## 01 Problem Restatement

Target length: 1-2 pages.

Purpose:

- rewrite the problem in the paper's own language
- identify tasks, inputs, outputs, and constraints
- prepare the reader for the modeling route

Must include:

- background in 1-2 compact paragraphs
- numbered restatement of subquestions
- known data and required outputs
- main constraints and evaluation indicators

Useful table:

| Subquestion | Input | Output | Constraint | Evaluation |
|---|---|---|---|---|

Must avoid:

- copying the full problem statement
- adding model details too early
- vague task descriptions

## 02 Problem Analysis

Target length: 2-4 pages.

Purpose:

- explain why the chosen model chain fits each subquestion
- connect problem signals to routes in `knowledge/algorithms/cumcm-routing-rules.md`
- introduce the planned figure/table logic

Must include:

- route overview figure
- subquestion-by-subquestion analysis
- rejected alternatives or model comparison when useful
- expected data processing and validation plan

Useful figure:

- model route diagram
- subquestion dependency graph

Must avoid:

- jumping directly into formulas
- saying only "we use algorithm X"
- ignoring why simpler alternatives are insufficient

## 03 Assumptions

Target length: 0.5-1 page.

Purpose:

- make simplifications explicit
- show why the model is tractable

Must include:

- 5-8 assumptions
- reason for each assumption
- possible effect if the assumption fails

Preferred format:

| No. | Assumption | Reason | Possible impact |
|---|---|---|---|

Must avoid:

- generic assumptions that apply to every problem
- assumptions that contradict the problem statement
- assumptions never used later

## 04 Symbols

Target length: 0.5-1 page.

Purpose:

- prevent formulas from becoming unreadable
- enforce variable consistency between text, equations, code, and tables

Must include:

- symbols for core variables and parameters
- units when applicable
- index sets and dimensions

Preferred format:

| Symbol | Meaning | Unit/Domain |
|---|---|---|

Must avoid:

- symbols that never appear later
- formulas using undefined variables
- multiple symbols for the same concept

## 05 Data Processing and Exploratory Analysis

Target length: 2-4 pages.

Purpose:

- show what data exist and how they become model inputs
- provide early evidence through plots and descriptive statistics

Must include:

- data source and fields
- cleaning rules
- missing/outlier handling
- feature construction
- exploratory figures/tables

Useful figures/tables:

- data inventory table
- distribution plot
- time-series plot
- correlation heatmap
- sample cleaning table

Must avoid:

- unexplained deletion of data
- figures with no modeling purpose
- preprocessing steps that leak future/test information

## 06 Model Establishment

Target length: 5-9 pages, sometimes more for hard problems.

Purpose:

- turn each subquestion into a mathematical model

For each subquestion, include:

```text
model idea
variables and parameters
objective or prediction target
constraints or equations
solver/algorithm
expected outputs
applicability and limitations
```

Must include:

- numbered equations when referenced later
- at least one explanatory figure when geometry, workflow, mechanism, or scheduling is involved
- clear connection to symbols and assumptions

Must avoid:

- algorithm names without mathematical formulation
- formulas that do not connect to code
- objectives without constraints for optimization problems

## 07 Solution Process

Target length: 3-5 pages.

Purpose:

- explain how the model is computed
- bridge formulas and implementation

Must include:

- algorithm steps
- parameter settings
- solver configuration
- convergence or termination criteria
- data flow from input to output

Useful artifacts:

- algorithm pseudo-code
- flowchart
- parameter table
- solver setting table

Must avoid:

- hiding important implementation choices
- omitting random seeds or search ranges
- presenting code-only logic without explanation

## 08 Results

Target length: 3-5 pages.

Purpose:

- present answers to the original subquestions
- interpret tables and figures

Must include:

- one result subsection per subquestion
- result tables with units
- result figures where visual comparison helps
- narrative interpretation

Useful artifacts:

- decision table
- ranking table
- prediction curve
- optimization comparison
- classification metric table
- scenario table

Must avoid:

- dumping tables without interpretation
- reporting too many decimals
- results that cannot be traced to code or equations

## 09 Validation and Sensitivity Analysis

Target length: 2-4 pages.

Purpose:

- prove the result is robust enough for research review

Must include at least one:

- residual/error analysis
- sensitivity analysis
- baseline comparison
- historical backtest
- constraint audit
- cross-validation
- scenario stress test

Useful artifacts:

- sensitivity curve
- residual plot
- confusion matrix
- constraint violation table
- baseline comparison table

Must avoid:

- only saying "the model is robust"
- validation without perturbation ranges
- classification metrics without data split details
- optimization result without feasibility checks

## 10 Strengths, Limitations, and Extensions

Target length: 1-2 pages.

Purpose:

- honestly assess the model
- prepare future improvement directions

Must include:

- 2-4 strengths tied to evidence
- 2-4 limitations tied to assumptions or data
- concrete extension ideas

Must avoid:

- generic "the model is simple and accurate"
- hiding important limitations
- claiming universal applicability

## 11 Conclusion

Target length: 0.5-1 page.

Purpose:

- summarize the final answers and decisions

Must include:

- concise answer to each subquestion
- most important quantitative result
- final recommendation or interpretation
- uncertainty or caveat when relevant

Must avoid:

- repeating the abstract word for word
- introducing new models or new results
- overclaiming beyond evidence

## References

Target length: 0.5-1 page.

Rules:

- cite real and relevant references only
- prefer sources tied to methods, data, or domain background
- never fabricate citations
- keep citation style consistent

## Appendix

Target length: 3-8 pages or more if needed.

Purpose:

- support reproducibility without overloading the body

Must include:

- code file inventory
- environment and run notes
- key code excerpts
- extra tables/figures
- data field explanation
- mapping from files to subquestions
- programming language/tool notes

Must avoid:

- appendix-only code with no runnable source in the repository
- unrelated template examples
- dumping huge code blocks when a file inventory is better

Observed official-paper pattern:

- Start appendix with a support-file list.
- Group code by subquestion.
- Name the tool/language used by each file.
- Include selected code excerpts after the file inventory.

## Figure Placement Rules

- Put route/workflow figure in `02_analysis` or method overview.
- Put explanatory diagrams before or near the corresponding model.
- Put evidence/result plots in `08_results`.
- Put robustness/error/sensitivity plots in `09_validation`.
- Every figure must have a caption and a text reference.
- Every figure must be listed in `runs/current/artifact-ledger.md`.

## Page Count Diagnostic

If the paper is too short:

- Check whether each subquestion has analysis, model, solution, result, and validation.
- Add missing data exploration, figures, or validation, not filler prose.
- Expand formula derivation only where it improves traceability.
- Add appendix run notes and code inventory.

If the paper is too long:

- Move implementation details to appendix.
- Merge repetitive explanation.
- Keep problem restatement concise.
- Remove unrelated background and references.
