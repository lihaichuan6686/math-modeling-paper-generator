from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 5:
        print("Usage: render-pdf-pages.py PDF_PATH OUTPUT_PREFIX FIRST_PAGE LAST_PAGE")
        return 2

    pdf_path = Path(sys.argv[1]).resolve()
    output_prefix = Path(sys.argv[2]).resolve()
    first_page = sys.argv[3]
    last_page = sys.argv[4]

    poppler = (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "native"
        / "poppler"
        / "Library"
        / "bin"
        / "pdftoppm.exe"
    )

    output_prefix.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            str(poppler),
            "-png",
            "-f",
            first_page,
            "-l",
            last_page,
            str(pdf_path),
            str(output_prefix),
        ],
        check=True,
    )
    print(f"Rendered pages {first_page}-{last_page} from {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

