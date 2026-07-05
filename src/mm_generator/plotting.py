from pathlib import Path

import matplotlib.pyplot as plt


def save_figure(fig: plt.Figure, path: str | Path) -> None:
    """Save a figure with consistent settings for LaTeX papers."""
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=300, bbox_inches="tight")

