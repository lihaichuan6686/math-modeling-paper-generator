# Environment Setup

Purpose: reduce repeated environment setup time for Claude Code and human testing.

The default recommendation is to use the lightweight environment first. It is intentionally small and only includes the Python packages currently needed by the repository demos and run pipeline.

## Preferred Options

### Option A: uv / venv Lightweight Environment

Preferred for Claude Code runs because it reuses `.venv` and avoids repeated conda solves:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\setup.ps1
powershell -ExecutionPolicy Bypass -File .\scripts\check-env.ps1
```

After setup, use:

```text
.venv\Scripts\python.exe
```

Do not create a new temporary environment for every script.

### Option B: Conda Lightweight Environment

Use:

```powershell
conda env create -f environment-lite.yml
conda activate mm-paper-lite
```

Use conda only when the local machine already prefers conda. Do not run a heavy solve during every paper generation.

### Option C: Existing Python Environment

If Python `3.11+` already exists, use:

```powershell
pip install -r requirements-lite.txt
```

## Why This File Exists

The project should not require rebuilding a heavy conda environment from scratch for every run.

This lightweight environment is intended to cover:

- demo generation scripts;
- table and figure generation;
- review helpers that depend on the current Python stack.

It does **not** attempt to install a full TeX distribution or other heavy desktop tools.

## Current Python Package Scope

The lightweight environment currently includes:

- `numpy`
- `pandas`
- `openpyxl`
- `scipy`
- `statsmodels`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `networkx`
- `pypdf`
- `pydantic`
- `pyyaml`
- `pillow`

## Environment Check Gate

Before a long generation run, use:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\check-env.ps1
```

If it fails, run `scripts/setup.ps1` once. If it passes, reuse the same `.venv` Python for exploration, plotting, Excel reading, PDF checks, and review helpers.

## Tooling Boundary

Keep this environment small.

Add a package only when:

1. the repository actually imports it in active scripts; or
2. a new demo/run pipeline truly depends on it.

Do not turn this into a giant everything-environment.

## File Discipline For Runs

Local experience notes repeatedly emphasize preparation, synchronized files, and ready-to-use tools. For this repository, that means:

- one active run folder under `runs/`;
- generated figures under `paper/figures/`;
- generated tables under `paper/tables/`;
- source scripts under `src/`;
- all body-critical outputs listed in `runs/current/artifact-ledger.md`;
- LaTeX references checked against actual filenames before review.

This is more important than installing every possible package. A small environment plus synchronized artifacts is better than a large environment with disconnected outputs.
