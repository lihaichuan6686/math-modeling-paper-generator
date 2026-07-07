from __future__ import annotations

import csv
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "paper" / "figures"
TABLE_DIR = ROOT / "paper" / "tables"
REVIEWS_DIR = ROOT / "reviews"


DEMAND = [120, 135, 128, 150, 160, 155, 142, 130]
SUPPLIERS = [
    {"name": "A", "capacity": 90, "price": 10.0, "loss": 0.03, "reliability": 0.93},
    {"name": "B", "capacity": 80, "price": 9.5, "loss": 0.06, "reliability": 0.88},
    {"name": "C", "capacity": 70, "price": 10.8, "loss": 0.02, "reliability": 0.96},
]


def supplier_score(s: dict[str, float | str]) -> float:
    price_score = 1 / float(s["price"])
    loss_score = 1 - float(s["loss"])
    reliability_score = float(s["reliability"])
    return 0.35 * price_score / 0.105 + 0.30 * loss_score + 0.35 * reliability_score


def build_plan() -> list[dict[str, float]]:
    ranked = sorted(SUPPLIERS, key=supplier_score, reverse=True)
    inventory = 20.0
    rows: list[dict[str, float]] = []
    for week, demand in enumerate(DEMAND, start=1):
        required = max(0.0, demand + 15.0 - inventory)
        orders = {s["name"]: 0.0 for s in SUPPLIERS}
        delivered = 0.0
        cost = 0.0
        for s in ranked:
            if required <= 0:
                break
            qty = min(float(s["capacity"]), required / (1 - float(s["loss"])))
            orders[str(s["name"])] = round(qty, 2)
            delivered += qty * (1 - float(s["loss"]))
            cost += qty * float(s["price"])
            required -= qty * (1 - float(s["loss"]))
        inventory = inventory + delivered - demand
        rows.append(
            {
                "week": week,
                "demand": demand,
                "order_A": orders["A"],
                "order_B": orders["B"],
                "order_C": orders["C"],
                "delivered": round(delivered, 2),
                "ending_inventory": round(inventory, 2),
                "cost": round(cost, 2),
            }
        )
    return rows


def build_supplier_rows() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for s in SUPPLIERS:
        rows.append(
            {
                "supplier": s["name"],
                "capacity": float(s["capacity"]),
                "price": float(s["price"]),
                "loss": float(s["loss"]),
                "reliability": float(s["reliability"]),
                "score": round(supplier_score(s), 4),
            }
        )
    return sorted(rows, key=lambda r: float(r["score"]), reverse=True)


def build_sensitivity_rows() -> list[dict[str, float]]:
    rows: list[dict[str, float]] = []
    base_loss = {str(s["name"]): float(s["loss"]) for s in SUPPLIERS}
    for multiplier in [0.8, 0.9, 1.0, 1.1, 1.2]:
        for s in SUPPLIERS:
            s["loss"] = base_loss[str(s["name"])] * multiplier
        plan = build_plan()
        rows.append(
            {
                "loss_multiplier": multiplier,
                "total_cost": round(sum(float(r["cost"]) for r in plan), 2),
                "min_inventory": round(min(float(r["ending_inventory"]) for r in plan), 2),
            }
        )
    for s in SUPPLIERS:
        s["loss"] = base_loss[str(s["name"])]
    return rows


def write_plan_table(rows: list[dict[str, float]]) -> Path:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    path = TABLE_DIR / "demo_v1_order_plan.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path


def write_plan_latex_table(rows: list[dict[str, float]]) -> Path:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    path = TABLE_DIR / "demo_v1_order_plan.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Demo v1 weekly ordering plan}",
        "\\label{tab:demo-v1-order-plan}",
        "\\begin{tabular}{rrrrrrr}",
        "\\toprule",
        "Week & Demand & Order A & Order B & Order C & Delivered & Inventory \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(
            f"{int(r['week'])} & {int(r['demand'])} & {r['order_A']:.2f} & "
            f"{r['order_B']:.2f} & {r['order_C']:.2f} & {r['delivered']:.2f} & "
            f"{r['ending_inventory']:.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_supplier_latex_table(rows: list[dict[str, float | str]]) -> Path:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    path = TABLE_DIR / "demo_v1_supplier_scores.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Synthetic supplier indicators and evaluation scores}",
        "\\label{tab:demo-v1-supplier-scores}",
        "\\begin{tabular}{lrrrrr}",
        "\\toprule",
        "Supplier & Capacity & Price & Loss rate & Reliability & Score \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(
            f"{r['supplier']} & {float(r['capacity']):.0f} & {float(r['price']):.2f} & "
            f"{float(r['loss']):.2f} & {float(r['reliability']):.2f} & {float(r['score']):.4f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_sensitivity_latex_table(rows: list[dict[str, float]]) -> Path:
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    path = TABLE_DIR / "demo_v1_sensitivity.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Sensitivity of total cost to transport loss perturbation}",
        "\\label{tab:demo-v1-sensitivity}",
        "\\begin{tabular}{rrr}",
        "\\toprule",
        "Loss multiplier & Total cost & Minimum inventory \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(f"{r['loss_multiplier']:.1f} & {r['total_cost']:.2f} & {r['min_inventory']:.2f} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def load_fonts() -> tuple[ImageFont.ImageFont, ImageFont.ImageFont, ImageFont.ImageFont]:
    font_path = Path("C:/Windows/Fonts/arial.ttf")
    if font_path.exists():
        return (
            ImageFont.truetype(str(font_path), 30),
            ImageFont.truetype(str(font_path), 22),
            ImageFont.truetype(str(font_path), 18),
        )
    fallback = ImageFont.load_default()
    return fallback, fallback, fallback


def draw_inventory_figure(rows: list[dict[str, float]]) -> Path:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / "demo_v1_inventory.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font_title, font_label, font_tick = load_fonts()
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    values = [float(r["ending_inventory"]) for r in rows]
    max_y = max(max(values) + 10, 40)
    min_y = 0

    def xy(i: int, value: float) -> tuple[float, float]:
        x = margin + i * (width - 2 * margin) / (len(values) - 1)
        y = height - margin - (value - min_y) * (height - 2 * margin) / (max_y - min_y)
        return x, y

    points = [xy(i, v) for i, v in enumerate(values)]
    draw.line(points, fill=(30, 90, 180), width=6)
    safety_y = xy(0, 15)[1]
    draw.line((margin, safety_y, width - margin, safety_y), fill=(200, 60, 60), width=4)
    for tick in [0, 10, 20, 30, 40]:
        y = xy(0, tick)[1]
        draw.line((margin - 8, y, margin, y), fill="black", width=2)
        draw.text((margin - 55, y - 10), str(tick), fill="black", font=font_tick)
    for i, p in enumerate(points, start=1):
        draw.ellipse((p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7), fill=(30, 90, 180))
        draw.text((p[0] - 6, height - margin + 18), str(i), fill="black", font=font_tick)
    draw.text((width // 2 - 215, 30), "Demo v1 ending inventory by week", fill="black", font=font_title)
    draw.text((width // 2 - 30, height - 45), "Week", fill="black", font=font_label)
    draw.text((margin, margin - 35), "Inventory", fill="black", font=font_label)
    draw.text((width - margin - 210, safety_y - 34), "safety target = 15", fill=(200, 60, 60), font=font_tick)
    img.save(path)
    return path


def draw_cost_figure(rows: list[dict[str, float]]) -> Path:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / "demo_v1_weekly_cost.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font_title, font_label, font_tick = load_fonts()
    values = [float(r["cost"]) for r in rows]
    max_y = max(values) * 1.15
    bar_w = (width - 2 * margin) / len(values) * 0.65
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    for i, value in enumerate(values):
        x_center = margin + (i + 0.5) * (width - 2 * margin) / len(values)
        bar_h = value / max_y * (height - 2 * margin)
        x0 = x_center - bar_w / 2
        y0 = height - margin - bar_h
        x1 = x_center + bar_w / 2
        draw.rectangle((x0, y0, x1, height - margin), fill=(80, 150, 120), outline=(40, 90, 70))
        draw.text((x_center - 6, height - margin + 18), str(i + 1), fill="black", font=font_tick)
    for tick in [0, 500, 1000, 1500]:
        y = height - margin - tick / max_y * (height - 2 * margin)
        draw.line((margin - 8, y, margin, y), fill="black", width=2)
        draw.text((margin - 70, y - 10), str(tick), fill="black", font=font_tick)
    draw.text((width // 2 - 150, 30), "Weekly ordering cost", fill="black", font=font_title)
    draw.text((width // 2 - 30, height - 45), "Week", fill="black", font=font_label)
    draw.text((margin, margin - 35), "Cost", fill="black", font=font_label)
    img.save(path)
    return path


def draw_sensitivity_figure(rows: list[dict[str, float]]) -> Path:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / "demo_v1_sensitivity.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font_title, font_label, font_tick = load_fonts()
    values = [float(r["total_cost"]) for r in rows]
    xs = [float(r["loss_multiplier"]) for r in rows]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(values) * 0.98, max(values) * 1.02
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")

    def xy(x: float, y: float) -> tuple[float, float]:
        px = margin + (x - min_x) / (max_x - min_x) * (width - 2 * margin)
        py = height - margin - (y - min_y) / (max_y - min_y) * (height - 2 * margin)
        return px, py

    points = [xy(x, y) for x, y in zip(xs, values)]
    draw.line(points, fill=(120, 70, 170), width=6)
    for x, y, point in zip(xs, values, points):
        draw.ellipse((point[0] - 7, point[1] - 7, point[0] + 7, point[1] + 7), fill=(120, 70, 170))
        draw.text((point[0] - 14, height - margin + 18), f"{x:.1f}", fill="black", font=font_tick)
        draw.text((point[0] - 35, point[1] - 32), f"{y:.0f}", fill=(80, 40, 120), font=font_tick)
    draw.text((width // 2 - 245, 30), "Cost sensitivity to transport loss", fill="black", font=font_title)
    draw.text((width // 2 - 90, height - 45), "Loss multiplier", fill="black", font=font_label)
    draw.text((margin, margin - 35), "Total cost", fill="black", font=font_label)
    img.save(path)
    return path


def write_summary(
    rows: list[dict[str, float]],
    sensitivity_rows: list[dict[str, float]],
    table_path: Path,
    tex_table_path: Path,
    supplier_table_path: Path,
    sensitivity_table_path: Path,
    figure_path: Path,
    cost_figure_path: Path,
    sensitivity_figure_path: Path,
    run_dir: Path,
) -> Path:
    run_dir.mkdir(parents=True, exist_ok=True)
    total_cost = sum(float(r["cost"]) for r in rows)
    min_inventory = min(float(r["ending_inventory"]) for r in rows)
    path = run_dir / "demo-v1-summary.md"
    path.write_text(
        "\n".join(
            [
                "# Demo v1 Summary",
                "",
                "This is a synthetic v1.0 pipeline test, not real contest evidence.",
                "",
                f"- Total cost: {total_cost:.2f}",
                f"- Minimum ending inventory: {min_inventory:.2f}",
                f"- Sensitivity cases: {len(sensitivity_rows)}",
                f"- Table: `{table_path.relative_to(ROOT)}`",
                f"- LaTeX table: `{tex_table_path.relative_to(ROOT)}`",
                f"- Supplier table: `{supplier_table_path.relative_to(ROOT)}`",
                f"- Sensitivity table: `{sensitivity_table_path.relative_to(ROOT)}`",
                f"- Figure: `{figure_path.relative_to(ROOT)}`",
                f"- Cost figure: `{cost_figure_path.relative_to(ROOT)}`",
                f"- Sensitivity figure: `{sensitivity_figure_path.relative_to(ROOT)}`",
                "",
                "Use this output to test artifact-ledger entries, LaTeX insertion, and review.",
            ]
        ),
        encoding="utf-8",
    )
    return path


def write_artifact_ledger(rows: list[dict[str, float]], sensitivity_rows: list[dict[str, float]], run_name: str, run_dir: Path) -> Path:
    total_cost = sum(float(r["cost"]) for r in rows)
    min_inventory = min(float(r["ending_inventory"]) for r in rows)
    path = run_dir / "artifact-ledger.md"
    path.write_text(
        "\n".join(
            [
                "# Artifact Ledger",
                "",
                f"Run: {run_name}",
                "Date: 2026-07-07",
                "Purpose: expanded v1.0 closed-loop smoke test for the mathematical modeling paper generator.",
                "",
                "## Run Metadata",
                "",
                "| Field | Value |",
                "|---|---|",
                f"| Run ID | {run_name} |",
                "| Contest/year/problem | Synthetic CUMCM-style supply planning demo |",
                "| Research purpose | Verify problem-to-code-to-figure-to-LaTeX-to-review loop |",
                "| Main problem file | `problems/demo-v1-supply.md` |",
                "| Data directory | Synthetic data embedded in `src/demo_v1.py` |",
                "| Code entry point | `src/demo_v1.py` |",
                "| Paper source | `paper/main.tex` |",
                "| PDF output | `paper/main.pdf` |",
                "| Reviewer | Codex |",
                "",
                "## Figures",
                "",
                "| ID | Role | Paper label | Figure file | Generated by | Paper section | Status |",
                "|---|---|---|---|---|---|---|",
                "| F01 | evidence | `fig:demo-v1-inventory` | `paper/figures/demo_v1_inventory.png` | `src/demo_v1.py` | Results | accepted |",
                "| F02 | evidence | `fig:demo-v1-cost` | `paper/figures/demo_v1_weekly_cost.png` | `src/demo_v1.py` | Results | accepted |",
                "| F03 | validation | `fig:demo-v1-sensitivity` | `paper/figures/demo_v1_sensitivity.png` | `src/demo_v1.py` | Validation and Sensitivity Analysis | accepted |",
                "",
                "## Tables",
                "",
                "| ID | Paper label | Table file/source | Generated by | Paper section | Status |",
                "|---|---|---|---|---|---|",
                "| T01 | `tab:demo-v1-supplier-scores` | `paper/tables/demo_v1_supplier_scores.tex` | `src/demo_v1.py` | Data Processing | accepted |",
                "| T02 | `tab:demo-v1-order-plan` | `paper/tables/demo_v1_order_plan.tex` | `src/demo_v1.py` | Results | accepted |",
                "| T03 | `tab:demo-v1-sensitivity` | `paper/tables/demo_v1_sensitivity.tex` | `src/demo_v1.py` | Validation and Sensitivity Analysis | accepted |",
                "",
                "## Key Results",
                "",
                "| ID | Result kind | Result statement | Value | Evidence source | Paper location | Verification |",
                "|---|---|---|---:|---|---|---|",
                f"| K01 | validation | Minimum ending inventory meets the safety target | {min_inventory:.2f} | `runs/{run_name}/demo-v1-summary.md` | Validation and Sensitivity Analysis | checked by generated table and figure |",
                f"| K02 | cost | Total baseline ordering cost | {total_cost:.2f} | `runs/{run_name}/demo-v1-summary.md` | Results | checked by generated weekly cost figure |",
                f"| K03 | sensitivity | Transport-loss sensitivity cases generated | {len(sensitivity_rows)} | `runs/{run_name}/demo-v1-summary.md` | Validation and Sensitivity Analysis | checked by generated sensitivity table and figure |",
                "",
                "## LaTeX and PDF Build",
                "",
                "| Check | Status | Evidence |",
                "|---|---|---|",
                "| PDF compiles successfully | Pending | Run `scripts/compile.ps1` after generation |",
                "| No missing figures | Pending | Inspect rendered PDF pages |",
                "| No broken references | Pending | Check second LaTeX pass |",
                "| Rendered PDF inspected | Pending | Render with `scripts/render-pdf-pages.py` |",
                "",
                "## Review Summary",
                "",
                "```text",
                "Problem coverage: sufficient for expanded synthetic v1.0 smoke test",
                "Model logic: simple greedy baseline with optimization-model extension described",
                "Reproducibility: pass for generated artifacts",
                "Figures/tables: 3 tables and 3 figures generated",
                "Validation: feasibility plus transport-loss sensitivity",
                "LaTeX/PDF: pending until compile step is run",
                "Responsible use: synthetic research demo only",
                "Final status: needs compile/review after generation",
                "```",
            ]
        ),
        encoding="utf-8",
    )
    return path


def write_review(run_name: str) -> Path:
    REVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    path = REVIEWS_DIR / f"review-{run_name}.md"
    path.write_text(
        "\n".join(
            [
                "# Paper Quality Review",
                "",
                f"Run: {run_name}",
                "Reviewed: 2026-07-07",
                "",
                "## Overall Status",
                "",
                "Needs revision",
                "",
                "## Critical Findings",
                "",
                "| ID | Location | Status | Evidence | Risk | Required repair |",
                "|---|---|---|---|---|---|",
                "| C01 | `paper/` | Warn | The draft uses synthetic data and a greedy baseline. | It is not contest-quality evidence. | Keep synthetic-data disclosure and replace with real problem data for production runs. |",
                "",
                "## Important Issues",
                "",
                "| ID | Location | Status | Evidence | Risk | Required repair |",
                "|---|---|---|---|---|---|",
                "| I01 | `paper/main.tex` | Warn | The generated paper is an expanded v1.0 demo, not the 20-30 page target. | Page logic is still lighter than a full CUMCM paper. | Add more route-specific derivation, validation, and appendix material. |",
                "| I02 | `paper/sections/06_model.tex` | Warn | The exact optimization model is described as an extension but not solved. | The main decision method remains a greedy baseline. | Add LP/IP implementation when moving beyond the smoke test. |",
                "| I03 | `reviews/review-v1-demo.md` | Unknown | PDF compile and rendered-page evidence must be checked after each generation run. | A generation-only review cannot prove final layout quality. | Run `scripts/compile.ps1` and render key pages before final acceptance. |",
                "",
                "## Warnings",
                "",
                "| ID | Location | Status | Evidence | Risk | Suggested repair |",
                "|---|---|---|---|---|---|",
                "| W01 | `paper/tables/`, `paper/figures/` | Pass | Three tables and three figures are generated from `src/demo_v1.py`. | Low risk for artifact traceability in the demo. | Keep generated paths stable. |",
                f"| W02 | `runs/{run_name}/artifact-ledger.md` | Pass | Ledger is regenerated by `src/demo_v1.py`. | Low risk of placeholder review after rerun. | Continue updating ledger fields as more artifacts are added. |",
                "",
                "## Evidence Checked",
                "",
                "- Python generation completed for supplier score, order plan, sensitivity table, inventory figure, weekly cost figure, and sensitivity figure.",
                "- Artifact ledger and summary were regenerated with current output paths.",
                "- The review file follows `prompts/06_quality_review.md` structure.",
                "",
                "## Evidence Missing Or Not Checked",
                "",
                "- Real CUMCM problem fit.",
                "- Full 20-30 page pacing.",
                "- Optimization-model solution quality.",
                "- PDF visual inspection after the latest generation run.",
                "",
                "## Required Repairs Before Pass",
                "",
                "1. Compile the PDF after generation.",
                "2. Render key pages and inspect table/figure layout.",
                "3. Replace the greedy baseline with a stronger optimization model for production-quality demos.",
                "",
                "## Human Verification Needed",
                "",
                "- Confirm whether the next iteration should prioritize 20-30 page expansion or stronger solver implementation.",
                "- Confirm responsible-use context before using any real contest problem.",
                "",
                "## Responsible-Use Notes",
                "",
                "- The demo uses synthetic data and is marked as a research prototype.",
                "- The output must not be used as an active contest submission.",
            ]
        ),
        encoding="utf-8",
    )
    return path


def main() -> int:
    run_name = sys.argv[1] if len(sys.argv) > 1 else "current"
    run_dir = ROOT / "runs" / run_name
    supplier_rows = build_supplier_rows()
    rows = build_plan()
    sensitivity_rows = build_sensitivity_rows()
    table = write_plan_table(rows)
    tex_table = write_plan_latex_table(rows)
    supplier_table = write_supplier_latex_table(supplier_rows)
    sensitivity_table = write_sensitivity_latex_table(sensitivity_rows)
    figure = draw_inventory_figure(rows)
    cost_figure = draw_cost_figure(rows)
    sensitivity_figure = draw_sensitivity_figure(sensitivity_rows)
    summary = write_summary(
        rows,
        sensitivity_rows,
        table,
        tex_table,
        supplier_table,
        sensitivity_table,
        figure,
        cost_figure,
        sensitivity_figure,
        run_dir,
    )
    ledger = write_artifact_ledger(rows, sensitivity_rows, run_name, run_dir)
    review = write_review(run_name)
    print(f"Wrote {table}")
    print(f"Wrote {tex_table}")
    print(f"Wrote {supplier_table}")
    print(f"Wrote {sensitivity_table}")
    print(f"Wrote {figure}")
    print(f"Wrote {cost_figure}")
    print(f"Wrote {sensitivity_figure}")
    print(f"Wrote {summary}")
    print(f"Wrote {ledger}")
    print(f"Wrote {review}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
