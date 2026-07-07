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
- Deep reads exist for:
  - 2021 D017: online scheduling and abnormal-scenario adjustment
  - 2021 A028: geometry and engineering mechanics
  - 2021 C066: supply-chain evaluation and planning

Next tasks:

- Deep-read selected papers by type:
  - chemistry/material statistics
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

- Detailed algorithm cards, an algorithm-card index, routing rules, and model-chain patterns exist.
- Current cards cover LP/IP, nonlinear programming, dynamic programming, time-series forecasting, regression, PCA/LDA, random forest, SVM, response surface methodology, queuing models, graph algorithms, and simulation.

Next tasks:

- Add or refine cards for:
  - TOPSIS and entropy weighting
  - AHP and subjective/objective combined weighting
  - clustering families
  - grey prediction and small-sample forecasting
  - genetic algorithm and simulated annealing
  - domain-specific chemistry/material modeling methods
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

- visual-generation pipeline: initial version complete
- figure-plan and artifact-ledger fields: initial version complete
- example scripts
- example generated figures/tables
- demo ledger update convention

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
- `knowledge/quality/quality-rubric-v2.md`: initial version complete
- eventually a script or agent prompt for automated review

## Track C: Responsible Use and Governance

Next tasks:

- Keep repository private unless user explicitly decides otherwise.
- Do not auto-push to GitHub more than once per day unless the user explicitly requests an immediate upload.
- Prefer local commits during unattended learning; batch GitHub uploads into a daily sync.
- During long unattended work, stop when the visible five-hour work window reaches the final 10% reserve. OpenAI's Codex pricing page describes Plus local-message limits as a five-hour window with model-dependent ranges, not a fixed token total. If exact account quota is not visible in this environment, use 4.5 hours of visible goal time as the conservative stopping point and resume after the quota refresh.
- Treat image generation as a higher-cost step. OpenAI's Codex pricing page says image generation counts against the same included usage limits and uses them faster on average, so visual generation should be batched and used when it materially improves figures, diagrams, or review artifacts.
- Maintain `SECURITY.md` and responsible-use warnings.
- Record limitations and human verification requirements.
- Ensure generated outputs are clearly research drafts unless human-reviewed.

## Near-Term Priority Order

1. Expand the bundled `v1-demo` from a 6-page smoke test toward a 20-30 page CUMCM-style research draft.
2. Add more generated visual artifacts: model-chain diagram, sensitivity plot, feasibility audit, and comparison table.
3. Harden the demo runner so ledger/review files are generated with real evidence instead of reset placeholders.
4. Package the runbook into a Claude Code skill-style workflow.
5. Convert review checklist/rubric into a stricter reusable review prompt or script.
6. Resume deep reading with `2021 E014` for the spectral/classification route.

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
