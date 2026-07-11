from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


TYPE_I_REQUIRED = [
    "rail_operation_candidates.csv",
    "rail_selected_operation_plan.csv",
    "rail_full_timetable.csv",
    "rail_capacity_audit.csv",
    "rail_tracking_audit.csv",
    "rail_dwell_audit.csv",
    "rail_scenario_analysis.csv",
]


PLACEHOLDER_MARKERS = [
    "Not reviewed yet",
    "Evidence Checked\n\n- \n",
    "Evidence Missing Or Not Checked\n\n- \n",
]


V12_PLAN_FILES = [
    "method-depth-plan.md",
    "section-budget.md",
    "writing-style-plan.md",
]


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def csv_row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return sum(1 for _ in csv.DictReader(f))


def status_counts(path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            key = row.get("status", "").strip() or "(missing)"
            counts[key] = counts.get(key, 0) + 1
    return counts


def add(ok: list[str], issues: list[str], condition: bool, pass_msg: str, fail_msg: str) -> None:
    if condition:
        ok.append(pass_msg)
    else:
        issues.append(fail_msg)


def overall_status_block(review: str) -> str:
    if "## Overall Status" not in review:
        return ""
    tail = review.split("## Overall Status", 1)[1]
    return tail.split("##", 1)[0].strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Check minimum generated-run quality gates.")
    parser.add_argument("--run", default="current", help="Run name under runs/.")
    parser.add_argument("--paper", default=None, help="Optional paper tex path relative to paper/.")
    args = parser.parse_args()

    run_dir = ROOT / "runs" / args.run
    review_path = ROOT / "reviews" / f"review-{args.run}.md"
    if args.run == "current":
        review_path = ROOT / "reviews" / "review-current.md"
    ledger_path = run_dir / "artifact-ledger.md"

    ok: list[str] = []
    issues: list[str] = []

    add(ok, issues, run_dir.exists(), f"Run directory exists: {run_dir}", f"Missing run directory: {run_dir}")
    add(ok, issues, ledger_path.exists(), f"Ledger exists: {ledger_path}", f"Missing artifact ledger: {ledger_path}")
    add(ok, issues, review_path.exists(), f"Review exists: {review_path}", f"Missing review file: {review_path}")

    ledger = read_text(ledger_path)
    review = read_text(review_path)
    is_type_i = "Type I" in ledger or "Rail Transit Timetable" in ledger or "rail timetable" in ledger.lower()
    has_any_v12_file = any((run_dir / name).exists() for name in V12_PLAN_FILES)
    review_status = overall_status_block(review)

    if review:
        add(
            ok,
            issues,
            "## Overall Status" in review,
            "Review has Overall Status section.",
            "Review lacks Overall Status section.",
        )
        add(
            ok,
            issues,
            not any(marker in review for marker in PLACEHOLDER_MARKERS),
            "Review does not look like an untouched placeholder.",
            "Review appears to contain placeholder or empty evidence fields.",
        )
        if has_any_v12_file:
            add(
                ok,
                issues,
                "Needs revision" not in review_status,
                "Review Overall Status is not blocking.",
                "Review Overall Status still says Needs revision.",
            )

    if ledger:
        add(
            ok,
            issues,
            "Code entry point" in ledger,
            "Ledger records a code entry point.",
            "Ledger does not record a code entry point.",
        )
        if "Final status: Pass" in ledger or "Overall Status: Pass" in ledger:
            add(
                ok,
                issues,
                review and "Needs revision" not in review_status,
                "Ledger final pass is not contradicted by review Overall Status.",
                "Ledger says final status is Pass while review Overall Status is Needs revision.",
            )

    if has_any_v12_file:
        ok.append("Detected v1.2-style run planning files.")
        for name in V12_PLAN_FILES:
            path = run_dir / name
            add(
                ok,
                issues,
                path.exists(),
                f"v1.2 planning file exists: {name}",
                f"Missing v1.2 planning file: {name}",
            )
            if path.exists():
                text = read_text(path)
                add(
                    ok,
                    issues,
                    "Unknown" not in text,
                    f"{name} no longer looks untouched.",
                    f"{name} still contains untouched placeholder values.",
                )

    if args.paper:
        paper_path = ROOT / "paper" / args.paper
        add(ok, issues, paper_path.exists(), f"Paper source exists: {paper_path}", f"Missing paper source: {paper_path}")
        if paper_path.exists():
            paper = read_text(paper_path)
            for token in ["\\begin{abstract}", "\\section", "\\end{document}"]:
                add(ok, issues, token in paper, f"Paper contains {token}.", f"Paper missing {token}.")

    if is_type_i:
        ok.append("Detected Type I rail/timetable run.")
        for name in TYPE_I_REQUIRED:
            path = run_dir / name
            add(ok, issues, path.exists(), f"Type I artifact exists: {name}", f"Missing Type I artifact: {name}")
            if path.exists():
                try:
                    rows = csv_row_count(path)
                    add(ok, issues, rows > 0, f"{name} has {rows} data rows.", f"{name} has no data rows.")
                except Exception as exc:  # noqa: BLE001
                    issues.append(f"Could not read CSV {name}: {exc}")

        for name in ["rail_capacity_audit.csv", "rail_tracking_audit.csv", "rail_dwell_audit.csv"]:
            path = run_dir / name
            if path.exists():
                try:
                    counts = status_counts(path)
                    add(
                        ok,
                        issues,
                        "Fail" not in counts and "(missing)" not in counts,
                        f"{name} status counts: {counts}",
                        f"{name} has failing or missing status values: {counts}",
                    )
                except Exception as exc:  # noqa: BLE001
                    issues.append(f"Could not inspect status values in {name}: {exc}")

    print("# Run Quality Check")
    print(f"Run: {args.run}")
    print("")
    print("## Passes")
    for msg in ok:
        print(f"- {msg}")
    print("")
    print("## Issues")
    if issues:
        for msg in issues:
            print(f"- {msg}")
        return 1
    print("- None")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
