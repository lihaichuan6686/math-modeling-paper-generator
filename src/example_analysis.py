from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from mm_generator.plotting import save_figure


def main() -> None:
    x = np.linspace(0, 10, 200)
    y = np.sin(x) * np.exp(-0.08 * x)

    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot(x, y, label="demo curve")
    ax.set_xlabel("x")
    ax.set_ylabel("response")
    ax.legend()
    ax.grid(True, alpha=0.3)

    repo_root = Path(__file__).resolve().parents[1]
    save_figure(fig, repo_root / "paper" / "figures" / "example_curve.png")


if __name__ == "__main__":
    main()

