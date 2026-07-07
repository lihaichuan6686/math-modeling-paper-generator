from __future__ import annotations

import csv
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "paper" / "figures"
TABLE_DIR = ROOT / "paper" / "tables"
REVIEWS_DIR = ROOT / "reviews"


MATERIALS = {
    "M1": {
        "label": "Leafy vegetables",
        "history": [32, 35, 31, 38, 40, 39, 43, 45],
        "current_inventory": 15.0,
        "safety_stock": 10.0,
        "capacity_k1": 38.0,
        "capacity_k2": 56.0,
    },
    "M2": {
        "label": "Prepared meals",
        "history": [22, 24, 26, 27, 28, 30, 31, 33],
        "current_inventory": 11.0,
        "safety_stock": 8.0,
        "capacity_k1": 28.0,
        "capacity_k2": 40.0,
    },
    "M3": {
        "label": "Frozen items",
        "history": [18, 17, 19, 20, 19, 21, 23, 24],
        "current_inventory": 9.0,
        "safety_stock": 7.0,
        "capacity_k1": 21.0,
        "capacity_k2": 33.0,
    },
}

PLANNING_WEEKS = 4


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


def weighted_forecast(history: list[float]) -> list[float]:
    values = history[:]
    forecast: list[float] = []
    for _ in range(PLANNING_WEEKS):
        pred = round(0.5 * values[-1] + 0.3 * values[-2] + 0.2 * values[-3], 2)
        forecast.append(pred)
        values.append(pred)
    return forecast


def backtest_forecast(history: list[float]) -> tuple[list[float], float]:
    preds: list[float] = []
    errors: list[float] = []
    for idx in range(3, len(history)):
        pred = 0.5 * history[idx - 1] + 0.3 * history[idx - 2] + 0.2 * history[idx - 3]
        preds.append(round(pred, 2))
        errors.append(abs(pred - history[idx]) / history[idx])
    mape = round(sum(errors) / len(errors), 4)
    return preds, mape


def build_material_summary_rows() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for code, data in MATERIALS.items():
        rows.append(
            {
                "material": code,
                "label": data["label"],
                "avg_history": round(sum(data["history"]) / len(data["history"]), 2),
                "latest_history": float(data["history"][-1]),
                "inventory": float(data["current_inventory"]),
                "safety_stock": float(data["safety_stock"]),
                "cap_k1": float(data["capacity_k1"]),
                "cap_k2": float(data["capacity_k2"]),
            }
        )
    return rows


def build_forecast_rows() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for code, data in MATERIALS.items():
        preds, mape = backtest_forecast(data["history"])
        future = weighted_forecast(data["history"])
        rows.append(
            {
                "material": code,
                "last_actual": float(data["history"][-1]),
                "pred_t1": future[0],
                "pred_t2": future[1],
                "pred_t3": future[2],
                "pred_t4": future[3],
                "mape": mape,
            }
        )
    return rows


def rolling_alpha(gap: float) -> float:
    if gap >= 8:
        return 0.95
    if gap >= 3:
        return 0.8
    if gap >= -2:
        return 0.6
    if gap >= -6:
        return 0.45
    return 0.3


def plan_scenario(capacity_key: str) -> tuple[list[dict[str, float | str]], list[dict[str, float | str]]]:
    rows: list[dict[str, float | str]] = []
    summary: list[dict[str, float | str]] = []
    for code, data in MATERIALS.items():
        inventory = float(data["current_inventory"])
        safety = float(data["safety_stock"])
        cap = float(data[capacity_key])
        forecasts = weighted_forecast(data["history"])
        supported = 0
        total_demand = 0.0
        min_inventory = inventory
        total_prod = 0.0
        for week_idx, demand in enumerate(forecasts, start=1):
            gap = demand + safety - inventory
            alpha = rolling_alpha(gap)
            production = round(max(0.0, min(cap, alpha * max(gap, 0.0))), 2)
            ending_inventory = round(inventory + production - demand, 2)
            support_qty = round(min(demand, inventory + production), 2)
            service = round(support_qty / demand, 4) if demand > 0 else 1.0
            if service >= 0.95:
                supported += 1
            total_demand += demand
            total_prod += production
            min_inventory = min(min_inventory, ending_inventory)
            rows.append(
                {
                    "scenario": capacity_key,
                    "material": code,
                    "week": week_idx,
                    "forecast": demand,
                    "production": production,
                    "ending_inventory": ending_inventory,
                    "service_level": service,
                }
            )
            inventory = ending_inventory
        summary.append(
            {
                "scenario": capacity_key,
                "material": code,
                "avg_forecast": round(total_demand / PLANNING_WEEKS, 2),
                "avg_production": round(total_prod / PLANNING_WEEKS, 2),
                "min_inventory": round(min_inventory, 2),
                "support_weeks": supported,
                "avg_service_level": round(
                    sum(float(r["service_level"]) for r in rows if r["scenario"] == capacity_key and r["material"] == code)
                    / PLANNING_WEEKS,
                    4,
                ),
            }
        )
    return rows, summary


def build_scenario_comparison_rows(summary_k1: list[dict[str, float | str]], summary_k2: list[dict[str, float | str]]) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    index_k2 = {str(r["material"]): r for r in summary_k2}
    for row in summary_k1:
        material = str(row["material"])
        other = index_k2[material]
        rows.append(
            {
                "material": material,
                "service_k1": float(row["avg_service_level"]),
                "service_k2": float(other["avg_service_level"]),
                "min_inventory_k1": float(row["min_inventory"]),
                "min_inventory_k2": float(other["min_inventory"]),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_material_latex_table(rows: list[dict[str, float | str]]) -> Path:
    path = TABLE_DIR / "demo_v1_material_summary.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Representative material summary for the production-route demo}",
        "\\label{tab:demo-v1-material-summary}",
        "\\begin{tabular}{lrrrrrr}",
        "\\toprule",
        "Material & Avg. history & Latest demand & Inventory & Safety stock & Cap. $k_1$ & Cap. $k_2$ \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(
            f"{r['material']} & {float(r['avg_history']):.2f} & {float(r['latest_history']):.2f} & "
            f"{float(r['inventory']):.2f} & {float(r['safety_stock']):.2f} & {float(r['cap_k1']):.2f} & {float(r['cap_k2']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_forecast_latex_table(rows: list[dict[str, float | str]]) -> Path:
    path = TABLE_DIR / "demo_v1_forecast_check.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Short-term demand forecast and backtest error for representative materials}",
        "\\label{tab:demo-v1-forecast-check}",
        "\\begin{tabular}{lrrrrrr}",
        "\\toprule",
        "Material & Last actual & $\\hat d_{1}$ & $\\hat d_{2}$ & $\\hat d_{3}$ & $\\hat d_{4}$ & MAPE \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(
            f"{r['material']} & {float(r['last_actual']):.2f} & {float(r['pred_t1']):.2f} & {float(r['pred_t2']):.2f} & "
            f"{float(r['pred_t3']):.2f} & {float(r['pred_t4']):.2f} & {100*float(r['mape']):.2f}\\% \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_plan_latex_table(rows: list[dict[str, float | str]]) -> Path:
    path = TABLE_DIR / "demo_v1_production_plan.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Rolling production plan under scenario $k_1$}",
        "\\label{tab:demo-v1-production-plan}",
        "\\begin{tabular}{lrrrrrr}",
        "\\toprule",
        "Material & Week & Forecast & Production & Ending inv. & Service level \\\\",
        "\\midrule",
    ]
    for r in rows:
        if r["scenario"] != "capacity_k1":
            continue
        lines.append(
            f"{r['material']} & {int(r['week'])} & {float(r['forecast']):.2f} & {float(r['production']):.2f} & "
            f"{float(r['ending_inventory']):.2f} & {100*float(r['service_level']):.2f}\\% \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_service_latex_table(rows: list[dict[str, float | str]]) -> Path:
    path = TABLE_DIR / "demo_v1_service_levels.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Average service level and inventory robustness by scenario}",
        "\\label{tab:demo-v1-service-levels}",
        "\\begin{tabular}{lrrrrr}",
        "\\toprule",
        "Scenario & Material & Avg. forecast & Avg. production & Min. inv. & Avg. service \\\\",
        "\\midrule",
    ]
    for r in rows:
        scenario = "$k_1$" if r["scenario"] == "capacity_k1" else "$k_2$"
        lines.append(
            f"{scenario} & {r['material']} & {float(r['avg_forecast']):.2f} & {float(r['avg_production']):.2f} & "
            f"{float(r['min_inventory']):.2f} & {100*float(r['avg_service_level']):.2f}\\% \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_scenario_latex_table(rows: list[dict[str, float | str]]) -> Path:
    path = TABLE_DIR / "demo_v1_scenario_compare.tex"
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        "\\caption{Service-level comparison between two capacity scenarios}",
        "\\label{tab:demo-v1-scenario-compare}",
        "\\begin{tabular}{lrrrr}",
        "\\toprule",
        "Material & Service $k_1$ & Service $k_2$ & Min. inv. $k_1$ & Min. inv. $k_2$ \\\\",
        "\\midrule",
    ]
    for r in rows:
        lines.append(
            f"{r['material']} & {100*float(r['service_k1']):.2f}\\% & {100*float(r['service_k2']):.2f}\\% & "
            f"{float(r['min_inventory_k1']):.2f} & {float(r['min_inventory_k2']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def draw_forecast_figure(rows: list[dict[str, float | str]]) -> Path:
    path = FIG_DIR / "demo_v1_forecast_compare.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    title_font, label_font, tick_font = load_fonts()
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    history = MATERIALS["M1"]["history"]
    forecast = [float(rows[0]["pred_t1"]), float(rows[0]["pred_t2"]), float(rows[0]["pred_t3"]), float(rows[0]["pred_t4"])]
    all_values = history + forecast
    min_y, max_y = min(all_values) - 3, max(all_values) + 3

    def xy(idx: int, value: float) -> tuple[float, float]:
        x = margin + idx * (width - 2 * margin) / (len(all_values) - 1)
        y = height - margin - (value - min_y) * (height - 2 * margin) / (max_y - min_y)
        return x, y

    actual_points = [xy(i, v) for i, v in enumerate(history)]
    forecast_points = [xy(i + len(history) - 1, v) for i, v in enumerate([history[-1]] + forecast)]
    draw.line(actual_points, fill=(40, 100, 180), width=6)
    draw.line(forecast_points, fill=(200, 80, 60), width=6)
    for p in actual_points:
        draw.ellipse((p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6), fill=(40, 100, 180))
    for p in forecast_points[1:]:
        draw.ellipse((p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6), fill=(200, 80, 60))
    for i in range(len(all_values)):
        draw.text((xy(i, min_y)[0] - 10, height - margin + 15), str(i + 1), fill="black", font=tick_font)
    draw.text((width // 2 - 180, 30), "Representative material forecast path", fill="black", font=title_font)
    draw.text((width // 2 - 30, height - 45), "Week", fill="black", font=label_font)
    draw.text((margin, margin - 35), "Demand", fill="black", font=label_font)
    draw.text((width - 260, margin + 10), "Actual: blue", fill=(40, 100, 180), font=tick_font)
    draw.text((width - 260, margin + 40), "Forecast: red", fill=(200, 80, 60), font=tick_font)
    img.save(path)
    return path


def draw_service_figure(rows: list[dict[str, float | str]]) -> Path:
    path = FIG_DIR / "demo_v1_service_levels.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    title_font, label_font, tick_font = load_fonts()
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    values = [100 * float(r["avg_service_level"]) for r in rows if r["scenario"] == "capacity_k1"]
    labels = [str(r["material"]) for r in rows if r["scenario"] == "capacity_k1"]
    max_y = 105.0
    bar_w = (width - 2 * margin) / len(values) * 0.5
    for i, (label, value) in enumerate(zip(labels, values)):
        x_center = margin + (i + 0.5) * (width - 2 * margin) / len(values)
        bar_h = value / max_y * (height - 2 * margin)
        draw.rectangle((x_center - bar_w / 2, height - margin - bar_h, x_center + bar_w / 2, height - margin), fill=(80, 150, 120))
        draw.text((x_center - 14, height - margin + 15), label, fill="black", font=tick_font)
        draw.text((x_center - 22, height - margin - bar_h - 30), f"{value:.1f}%", fill="black", font=tick_font)
    target_y = height - margin - 95 / max_y * (height - 2 * margin)
    draw.line((margin, target_y, width - margin, target_y), fill=(200, 70, 70), width=4)
    draw.text((width - 250, target_y - 28), "service target = 95%", fill=(200, 70, 70), font=tick_font)
    draw.text((width // 2 - 210, 30), "Average service level under scenario k1", fill="black", font=title_font)
    draw.text((width // 2 - 40, height - 45), "Material", fill="black", font=label_font)
    draw.text((margin, margin - 35), "Service level", fill="black", font=label_font)
    img.save(path)
    return path


def draw_scenario_figure(rows: list[dict[str, float | str]]) -> Path:
    path = FIG_DIR / "demo_v1_scenario_compare.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    title_font, label_font, tick_font = load_fonts()
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    labels = [str(r["material"]) for r in rows]
    vals1 = [100 * float(r["service_k1"]) for r in rows]
    vals2 = [100 * float(r["service_k2"]) for r in rows]
    group_w = (width - 2 * margin) / len(labels)
    bar_w = group_w * 0.22
    max_y = 105.0
    for i, label in enumerate(labels):
        center = margin + (i + 0.5) * group_w
        for j, (value, color) in enumerate(((vals1[i], (80, 120, 200)), (vals2[i], (210, 110, 70)))):
            x_center = center + (-0.18 + j * 0.36) * group_w
            bar_h = value / max_y * (height - 2 * margin)
            draw.rectangle((x_center - bar_w / 2, height - margin - bar_h, x_center + bar_w / 2, height - margin), fill=color)
        draw.text((center - 14, height - margin + 15), label, fill="black", font=tick_font)
    draw.text((width - 260, margin + 10), "k1: blue", fill=(80, 120, 200), font=tick_font)
    draw.text((width - 260, margin + 40), "k2: orange", fill=(210, 110, 70), font=tick_font)
    draw.text((width // 2 - 180, 30), "Service-level scenario comparison", fill="black", font=title_font)
    draw.text((width // 2 - 40, height - 45), "Material", fill="black", font=label_font)
    draw.text((margin, margin - 35), "Service level", fill="black", font=label_font)
    img.save(path)
    return path


def write_summary(run_dir: Path, scenario_rows: list[dict[str, float | str]], summary_rows: list[dict[str, float | str]], comparison_rows: list[dict[str, float | str]]) -> Path:
    run_dir.mkdir(parents=True, exist_ok=True)
    min_inv = min(float(r["min_inventory"]) for r in summary_rows if r["scenario"] == "capacity_k1")
    avg_service = sum(float(r["avg_service_level"]) for r in summary_rows if r["scenario"] == "capacity_k1") / 3
    better_k2 = sum(1 for r in comparison_rows if float(r["service_k2"]) >= float(r["service_k1"]))
    path = run_dir / "demo-v1-summary.md"
    path.write_text(
        "\n".join(
            [
                "# Demo v1 Summary",
                "",
                "This is a synthetic production-route E demo. It is for workflow validation only.",
                "",
                f"- Scenario k1 minimum inventory: {min_inv:.2f}",
                f"- Scenario k1 average service level: {100*avg_service:.2f}%",
                f"- Materials improved or matched by k2: {better_k2}",
                f"- Rolling plan rows generated: {len(scenario_rows)}",
                "",
                "The demo now exercises forecast -> service level -> rolling production -> scenario comparison.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def write_artifact_ledger(
    run_name: str,
    material_rows: list[dict[str, float | str]],
    forecast_rows: list[dict[str, float | str]],
    scenario_rows: list[dict[str, float | str]],
    summary_rows: list[dict[str, float | str]],
    comparison_rows: list[dict[str, float | str]],
    run_dir: Path,
) -> Path:
    min_inv = min(float(r["min_inventory"]) for r in summary_rows if r["scenario"] == "capacity_k1")
    avg_service = sum(float(r["avg_service_level"]) for r in summary_rows if r["scenario"] == "capacity_k1") / 3
    path = run_dir / "artifact-ledger.md"
    path.write_text(
        "\n".join(
            [
                "# Artifact Ledger",
                "",
                f"Run: {run_name}",
                "Date: 2026-07-08",
                "Purpose: production-route E smoke test for the mathematical modeling paper generator.",
                "",
                "## Run Metadata",
                "",
                "| Field | Value |",
                "|---|---|",
                f"| Run ID | {run_name} |",
                "| Contest/year/problem | Synthetic production-route E demo |",
                "| Research purpose | Verify forecast-to-service-to-production paper loop |",
                "| Main problem file | `problems/demo-v1-supply.md` |",
                "| Data directory | Synthetic data embedded in `src/demo_v1.py` |",
                "| Code entry point | `src/demo_v1.py` |",
                "| Route family | production-route E |",
                "| Paper source | `paper/main.tex` |",
                "| PDF output | `paper/main.pdf` |",
                "",
                "## Figures",
                "",
                "| ID | Role | Paper label | Figure file | Generated by | Paper section | Status |",
                "|---|---|---|---|---|---|---|",
                "| F01 | evidence | `fig:demo-v1-forecast` | `paper/figures/demo_v1_forecast_compare.png` | `src/demo_v1.py` | Results | accepted |",
                "| F02 | evidence | `fig:demo-v1-service` | `paper/figures/demo_v1_service_levels.png` | `src/demo_v1.py` | Results | accepted |",
                "| F03 | validation | `fig:demo-v1-scenario` | `paper/figures/demo_v1_scenario_compare.png` | `src/demo_v1.py` | Validation and Sensitivity Analysis | accepted |",
                "",
                "## Tables",
                "",
                "| ID | Paper label | Table file/source | Generated by | Paper section | Status |",
                "|---|---|---|---|---|---|",
                "| T01 | `tab:demo-v1-material-summary` | `paper/tables/demo_v1_material_summary.tex` | `src/demo_v1.py` | Data Processing | accepted |",
                "| T02 | `tab:demo-v1-forecast-check` | `paper/tables/demo_v1_forecast_check.tex` | `src/demo_v1.py` | Results | accepted |",
                "| T03 | `tab:demo-v1-production-plan` | `paper/tables/demo_v1_production_plan.tex` | `src/demo_v1.py` | Results | accepted |",
                "| T04 | `tab:demo-v1-service-levels` | `paper/tables/demo_v1_service_levels.tex` | `src/demo_v1.py` | Results | accepted |",
                "| T05 | `tab:demo-v1-scenario-compare` | `paper/tables/demo_v1_scenario_compare.tex` | `src/demo_v1.py` | Validation and Sensitivity Analysis | accepted |",
                "",
                "## Key Results",
                "",
                "| ID | Result kind | Result statement | Value | Evidence source | Paper location | Verification |",
                "|---|---|---|---:|---|---|---|",
                f"| K01 | validation | Scenario k1 minimum inventory under the stressed baseline | {min_inv:.2f} | `runs/{run_name}/demo-v1-summary.md` | Validation and Sensitivity Analysis | checked by scenario summary table |",
                f"| K02 | service | Scenario k1 average service level across three key materials | {100*avg_service:.2f} | `runs/{run_name}/demo-v1-summary.md` | Results | checked by service-level table and figure |",
                f"| K03 | scenario | Materials improved or matched by k2 service level | {sum(1 for r in comparison_rows if float(r['service_k2']) >= float(r['service_k1']))} | `runs/{run_name}/demo-v1-summary.md` | Validation and Sensitivity Analysis | checked by scenario comparison table |",
                "",
                "## Route-Specific Review Notes",
                "",
                "- Forecast outputs feed rolling production quantities.",
                "- Service-level and minimum-inventory consequences are explicit.",
                "- Two capacity scenarios are compared to simulate a conservative production-route E paper.",
            ]
        )
        + "\n",
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
                "Reviewed: 2026-07-08",
                "",
                "## Overall Status",
                "",
                "Needs revision",
                "",
                "## Critical Findings",
                "",
                "| ID | Location | Status | Evidence | Risk | Required repair |",
                "|---|---|---|---|---|---|",
                "| C01 | `paper/` | Warn | The demo is synthetic and intentionally lightweight. | It cannot stand in for a real contest-grade paper. | Preserve disclosure and replace synthetic demand with real data in future runs. |",
                "",
                "## Important Issues",
                "",
                "| ID | Location | Status | Evidence | Risk | Required repair |",
                "|---|---|---|---|---|---|",
                "| I01 | `paper/sections/06_model.tex` | Warn | The rolling policy is interpretable, but no exact solver baseline is implemented. | The demo may understate optimization depth. | Add an LP/IP comparison in a stronger production-route run. |",
                "| I02 | `paper/main.tex` | Warn | The paper is still shorter than a full 20-30 page research draft. | Route logic is present, but depth is still demo-scale. | Expand derivation, appendix, and scenario material in the next iteration. |",
                "| I03 | `paper/main.pdf` | Warn | PDF compile and rendered-page inspection are outside this generation script. | A run can look complete before layout is checked. | Compile and render key pages after generation before treating the draft as usable. |",
                "",
                "## Warnings",
                "",
                "| ID | Location | Status | Evidence | Risk | Suggested repair |",
                "|---|---|---|---|---|---|",
                "| W01 | `paper/tables/` | Pass | Five route-specific tables are generated. | Low traceability risk for the demo. | Keep production-route artifacts stable. |",
                "| W02 | `paper/figures/` | Pass | Forecast, service-level, and scenario-comparison figures are generated. | Low visual traceability risk for the demo. | Add Chinese-labeled figures in a later pass. |",
                "",
                "## Evidence Checked",
                "",
                "- Production-route E artifact set exists: representative materials, forecast check, production plan, service levels, and scenario comparison.",
                "- The artifact ledger includes route-specific key results and figure/table mapping.",
                "- The review structure matches `prompts/06_quality_review.md`.",
                "",
                "## Evidence Missing Or Not Checked",
                "",
                "- Real problem data.",
                "- Exact solver comparison.",
                "- A generation-script-level PDF compile or rendered-page check.",
                "",
                "## Required Repairs Before Pass",
                "",
                "1. Compile the paper after regenerating artifacts.",
                "2. Render key pages and inspect layout.",
                "3. Add an optimization baseline or stronger derivation for a production-quality route demo.",
                "",
                "## Human Verification Needed",
                "",
                "- Decide whether the next route demo should prioritize solver strength or full-paper expansion.",
                "",
                "## Responsible-Use Notes",
                "",
                "- This run is a research-only synthetic production-route E demo.",
                "- It must not be presented as contest evidence.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def main() -> int:
    run_name = sys.argv[1] if len(sys.argv) > 1 else "current"
    run_dir = ROOT / "runs" / run_name
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)

    material_rows = build_material_summary_rows()
    forecast_rows = build_forecast_rows()
    scenario_rows, summary_k1 = plan_scenario("capacity_k1")
    scenario_rows_k2, summary_k2 = plan_scenario("capacity_k2")
    all_scenario_rows = scenario_rows + scenario_rows_k2
    all_summary_rows = summary_k1 + summary_k2
    comparison_rows = build_scenario_comparison_rows(summary_k1, summary_k2)

    write_csv(TABLE_DIR / "demo_v1_material_summary.csv", material_rows)
    write_csv(TABLE_DIR / "demo_v1_forecast_check.csv", forecast_rows)
    write_csv(TABLE_DIR / "demo_v1_production_plan.csv", all_scenario_rows)
    write_csv(TABLE_DIR / "demo_v1_service_levels.csv", all_summary_rows)
    write_csv(TABLE_DIR / "demo_v1_scenario_compare.csv", comparison_rows)

    material_tex = write_material_latex_table(material_rows)
    forecast_tex = write_forecast_latex_table(forecast_rows)
    plan_tex = write_plan_latex_table(all_scenario_rows)
    service_tex = write_service_latex_table(all_summary_rows)
    scenario_tex = write_scenario_latex_table(comparison_rows)

    forecast_fig = draw_forecast_figure(forecast_rows)
    service_fig = draw_service_figure(all_summary_rows)
    scenario_fig = draw_scenario_figure(comparison_rows)

    summary = write_summary(run_dir, all_scenario_rows, all_summary_rows, comparison_rows)
    ledger = write_artifact_ledger(run_name, material_rows, forecast_rows, all_scenario_rows, all_summary_rows, comparison_rows, run_dir)
    review = write_review(run_name)

    for path in [
        material_tex,
        forecast_tex,
        plan_tex,
        service_tex,
        scenario_tex,
        forecast_fig,
        service_fig,
        scenario_fig,
        summary,
        ledger,
        review,
    ]:
        print(f"Wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
