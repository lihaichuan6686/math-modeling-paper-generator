from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


def clean_sample(text: str, limit: int = 240) -> str:
    text = " ".join(text.split())
    text = text.encode("utf-8", errors="replace").decode("utf-8")
    return text[:limit]


def extract_utf16_runs(data: bytes) -> list[str]:
    runs: list[str] = []
    pattern = re.compile(rb"(?:[\x09\x0a\x0d\x20-\xff]\x00){4,}")
    for match in pattern.finditer(data):
        text = match.group(0).decode("utf-16le", errors="ignore")
        text = clean_sample(text, 500)
        if len(text) < 8:
            continue
        printable_ratio = sum(ch.isprintable() for ch in text) / max(1, len(text))
        if printable_ratio < 0.8:
            continue
        runs.append(text)

    unique: list[str] = []
    seen: set[str] = set()
    for run in runs:
        key = run[:80]
        if key in seen:
            continue
        seen.add(key)
        unique.append(run)
    return unique


def classify_readability(runs: list[str]) -> str:
    if not runs:
        return "blocked"

    lower = "\n".join(runs[:30]).lower()
    metadata_terms = [
        "worddocument",
        "powerpoint document",
        "summaryinformation",
        "documentsummaryinformation",
        "times new roman",
        "courier new",
        "root entry",
        "current user",
        "style.visibility",
    ]
    useful_runs = [
        run
        for run in runs
        if not any(term in run.lower() for term in metadata_terms)
    ]

    if len(useful_runs) >= 20:
        return "partial"
    if len(useful_runs) >= 5:
        return "weak-partial"
    if any(term in lower for term in ["dijkstra", "matlab", "lingo", "sars"]):
        return "weak-partial"
    return "blocked"


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: probe-binary-office-text.py INPUT_DIR OUTPUT_CSV")
        return 2

    input_dir = Path(sys.argv[1]).resolve()
    output_csv = Path(sys.argv[2]).resolve()
    output_csv.parent.mkdir(parents=True, exist_ok=True)

    rows: list[dict[str, str | int]] = []
    for path in sorted(input_dir.glob("*")):
        if path.suffix.lower() not in {".doc", ".ppt"}:
            continue

        try:
            data = path.read_bytes()
            runs = extract_utf16_runs(data)
            readability = classify_readability(runs)
            samples = " | ".join(clean_sample(run) for run in runs[:6])
            error = ""
        except Exception as exc:
            runs = []
            readability = "blocked"
            samples = ""
            error = f"{type(exc).__name__}: {exc}"

        rows.append(
            {
                "file": path.name,
                "bytes": path.stat().st_size if path.exists() else 0,
                "readable_runs": len(runs),
                "readability": readability,
                "sample": samples,
                "error": error,
            }
        )

    with output_csv.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "file",
                "bytes",
                "readable_runs",
                "readability",
                "sample",
                "error",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} Office-binary probe rows to {output_csv}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
