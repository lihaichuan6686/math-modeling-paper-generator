# Environment Setup

Purpose: reduce repeated environment setup time for Claude Code and human testing.

The default recommendation is to use the lightweight environment first. It is intentionally small and only includes the Python packages currently needed by the repository demos and run pipeline.

## Preferred Options

### Option A: Conda Lightweight Environment

Use:

```powershell
conda env create -f environment-lite.yml
conda activate mm-paper-lite
```

### Option B: Existing Python Environment

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
- `scipy`
- `statsmodels`
- `scikit-learn`
- `matplotlib`
- `networkx`
- `pydantic`
- `pyyaml`
- `pillow`

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
