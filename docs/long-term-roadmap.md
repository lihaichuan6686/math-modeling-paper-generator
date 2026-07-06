# Long-Term Roadmap

Purpose: guide the project toward a research-only CUMCM paper-generation and paper-quality-checking agent. The roadmap separates knowledge absorption from engineering delivery so that the project does not become either a loose note collection or a brittle script.

## Guiding Principles

- Prioritize CUMCM first, then expand to other mathematical modeling contests.
- Treat excellent papers as structure and method evidence, not text to imitate.
- Treat figures, tables, code, and LaTeX as one reproducible chain.
- Keep responsible-use boundaries explicit.
- Do not optimize for active contest misuse.

## Track A: Knowledge Absorption

### A1. CUMCM Excellent Paper Reading

Current status:

- First-pass notes exist for 2021, 2022, and 2023 samples.

Next tasks:

- Deep-read selected papers by type:
  - geometry/engineering
  - chemistry/material statistics
  - supply chain planning
  - online scheduling
  - machine learning classification
  - time-series decision
  - evaluation/ranking
- For each deep-read paper, extract:
  - section structure
  - model chain
  - formulas
  - figures and tables
  - validation method
  - writing pattern
  - reproducibility risks

Deliverables:

- `knowledge/cumcm/deep-reading-*.md`
- updated routing rules
- updated section contract examples

### A2. Algorithm Cards

Current status:

- Initial algorithm cards and routing rules exist.

Next tasks:

- Add detailed cards for:
  - linear programming
  - integer programming
  - nonlinear programming
  - dynamic programming
  - ARIMA/exponential smoothing
  - regression families
  - random forest
  - SVM
  - PCA/LDA
  - response surface methodology
  - queuing models
  - graph algorithms
  - simulation
- Each card should include:
  - when to use
  - when not to use
  - required data
  - variables and equations
  - validation
  - figure/table expectations
  - common CUMCM writing pattern

Deliverables:

- `knowledge/algorithms/cards/*.md` or expanded `algorithm-cards.md`
- updated `cumcm-routing-rules.md`

### A3. LaTeX and Visual Style

Current status:

- Section contract, figure plan, artifact ledger, figure/table/equation style guide, and reusable LaTeX snippets exist.

Next tasks:

- Compare user awarded paper and official templates.
- Expand snippets with compiled examples and problem-type-specific variants.
- Create reusable examples that compile.

Deliverables:

- `knowledge/latex/snippets.md`: initial version complete
- stronger `paper/sections/` placeholders
- rendered PDF inspection notes

## Track B: Engineering Delivery

### B1. Run Workspace Generator

Goal:

Create a command that initializes a new research run.

Current status:

- `scripts/new-run.ps1` now creates the full run scaffold, including analysis files, model planning files, figure plan, artifact ledger, review file, and output directories.

Expected behavior:

- create `runs/current/`
- copy artifact ledger template
- copy figure plan template
- create problem-analysis/model-plan/review placeholders
- prepare output folders

Deliverables:

- `scripts/new-run.ps1` enhancement: initial version complete
- `runs/current/` template behavior

### B2. Figure and Table Pipeline

Goal:

Make figures and tables first-class reproducible outputs.

Expected behavior:

- standard `src/figures/` entry points
- standard `src/tables/` entry points
- stable output naming
- artifact ledger update path

Deliverables:

- example scripts
- example generated figures/tables
- ledger update convention

### B3. LaTeX Build and Visual QA

Goal:

Make PDF compilation and visual inspection routine.

Expected behavior:

- compile with `scripts/compile.ps1`
- render selected PDF pages
- inspect cover, abstract, model section, results, appendix
- record issues in review

Deliverables:

- updated compile instructions
- PDF render helper usage notes
- review checklist integration

### B4. Quality Checker

Goal:

Turn the research framework into a paper-quality assistant.

Expected behavior:

- read paper/source/code/artifact ledger
- check section coverage
- check figure/table traceability
- check model-result consistency
- check LaTeX/PDF quality
- output review report with Pass/Warn/Fail/Unknown

Deliverables:

- `reviews/review-current.md` generated from checklist
- eventually a script or agent prompt for automated review

## Track C: Responsible Use and Governance

Next tasks:

- Keep repository private unless user explicitly decides otherwise.
- Do not auto-push to GitHub.
- Maintain `SECURITY.md` and responsible-use warnings.
- Record limitations and human verification requirements.
- Ensure generated outputs are clearly research drafts unless human-reviewed.

## Near-Term Priority Order

1. Deep-read one official excellent paper end to end and extract a full structure map.
2. Add detailed algorithm cards for LP/IP, regression, PCA/LDA, random forest, SVM, and response surface.
3. Build a small demo run from a toy problem to test the full chain.
4. Compile and visually inspect the demo PDF.
5. Convert review checklist into a stricter quality-check workflow.

## Definition of Progress

Progress is not measured by page count alone. A milestone counts only if it improves at least one of:

- problem understanding
- route selection
- mathematical modeling
- code reproducibility
- figure/table generation
- LaTeX quality
- review rigor
- responsible-use safety
