from __future__ import annotations

import csv
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "paper" / "figures"
TABLE_DIR = ROOT / "paper" / "tables"


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


def draw_inventory_figure(rows: list[dict[str, float]]) -> Path:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    path = FIG_DIR / "demo_v1_inventory.png"
    width, height = 1000, 620
    margin = 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    font_path = Path("C:/Windows/Fonts/arial.ttf")
    if font_path.exists():
        font_title = ImageFont.truetype(str(font_path), 30)
        font_label = ImageFont.truetype(str(font_path), 22)
        font_tick = ImageFont.truetype(str(font_path), 18)
    else:
        font_title = ImageFont.load_default()
        font_label = ImageFont.load_default()
        font_tick = ImageFont.load_default()
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


def write_summary(rows: list[dict[str, float]], table_path: Path, tex_table_path: Path, figure_path: Path, run_dir: Path) -> Path:
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
                f"- Table: `{table_path.relative_to(ROOT)}`",
                f"- LaTeX table: `{tex_table_path.relative_to(ROOT)}`",
                f"- Figure: `{figure_path.relative_to(ROOT)}`",
                "",
                "Use this output to test artifact-ledger entries, LaTeX insertion, and review.",
            ]
        ),
        encoding="utf-8",
    )
    return path


def main() -> int:
    run_name = sys.argv[1] if len(sys.argv) > 1 else "current"
    run_dir = ROOT / "runs" / run_name
    rows = build_plan()
    table = write_plan_table(rows)
    tex_table = write_plan_latex_table(rows)
    figure = draw_inventory_figure(rows)
    summary = write_summary(rows, table, tex_table, figure, run_dir)
    print(f"Wrote {table}")
    print(f"Wrote {tex_table}")
    print(f"Wrote {figure}")
    print(f"Wrote {summary}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
