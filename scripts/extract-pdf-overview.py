from __future__ import annotations

import csv
import sys
from pathlib import Path

from pypdf import PdfReader


def clean_text(text: str, limit: int = 1200) -> str:
    text = " ".join(text.split())
    text = text.encode("utf-8", errors="replace").decode("utf-8")
    return text[:limit]


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: extract-pdf-overview.py SOURCE_ROOT OUTPUT_CSV")
        return 2

    source_root = Path(sys.argv[1]).resolve()
    output_csv = Path(sys.argv[2]).resolve()
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str | int]] = []
    for pdf in sorted(source_root.rglob("*.pdf")):
        try:
            reader = PdfReader(str(pdf))
            page_count = len(reader.pages)
            first_text = clean_text(reader.pages[0].extract_text() or "")
        except Exception as exc:  # PDF collections often contain damaged scans.
            page_count = -1
            first_text = f"ERROR: {type(exc).__name__}: {exc}"

        rows.append(
            {
                "relative_path": str(pdf.relative_to(source_root)),
                "bytes": pdf.stat().st_size,
                "pages": page_count,
                "first_page_text": first_text,
            }
        )

    with output_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["relative_path", "bytes", "pages", "first_page_text"],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} PDF overviews to {output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
