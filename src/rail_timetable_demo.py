from __future__ import annotations

import csv
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
RUNS_DIR = ROOT / "runs"
FIG_DIR = ROOT / "paper" / "figures"
TABLE_DIR = ROOT / "paper" / "tables"
REVIEWS_DIR = ROOT / "reviews"


STATIONS = [f"站{i}" for i in range(1, 13)]
SECTION_FLOW = [5200, 6800, 9100, 12600, 16800, 21400, 20600, 17200, 13300, 9800, 6100]
DISTANCE_KM = [1.2, 1.0, 1.4, 1.1, 1.5, 1.3, 1.2, 1.4, 1.1, 1.3, 1.0]
RUN_TIME_S = [115, 100, 130, 105, 140, 125, 115, 135, 105, 120, 100]
TRAIN_CAPACITY = 1200
HEADWAY_MIN = 120
HEADWAY_MAX = 360
TRACKING_MIN = 105
DWELL_MIN = 20
DWELL_MAX = 60
PEAK_START = "07:00:00"


def ensure_dirs(run_dir: Path) -> None:
    for d in [run_dir, FIG_DIR, TABLE_DIR, REVIEWS_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def load_fonts() -> tuple[ImageFont.ImageFont, ImageFont.ImageFont, ImageFont.ImageFont]:
    for p in [
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/msyh.ttc"),
        Path("C:/Windows/Fonts/simsun.ttc"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]:
        if p.exists():
            return (
                ImageFont.truetype(str(p), 30),
                ImageFont.truetype(str(p), 22),
                ImageFont.truetype(str(p), 17),
            )
    fallback = ImageFont.load_default()
    return fallback, fallback, fallback


def sec_to_time(seconds: float) -> str:
    seconds = int(round(seconds))
    h = 7 + seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return path


def latex_escape(value: object) -> str:
    return str(value).replace("_", "\\_")


def write_latex_table(path: Path, caption: str, label: str, headers: list[str], rows: list[list[object]], align: str) -> Path:
    lines = [
        "\\begin{table}[H]",
        "\\centering",
        f"\\caption{{{caption}}}",
        f"\\label{{{label}}}",
        "\\small",
        f"\\begin{{tabular}}{{{align}}}",
        "\\toprule",
        " & ".join(headers) + " \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(" & ".join(latex_escape(x) for x in row) + " \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}", "\\end{table}", ""])
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def evaluate_candidates() -> list[dict[str, object]]:
    big_len = sum(DISTANCE_KM)
    candidates: list[dict[str, object]] = []
    for s in range(2, 6):
        for e in range(s + 3, min(s + 7, len(STATIONS))):
            outside = SECTION_FLOW[:s] + SECTION_FLOW[e:]
            overlap = SECTION_FLOW[s:e]
            min_big = max(math.ceil(max(outside) / TRAIN_CAPACITY), 1)
            min_total = max(math.ceil(max(overlap) / TRAIN_CAPACITY), min_big + 1)
            for n_big in range(min_big, 25):
                for n_small in range(max(1, min_total - n_big), 25):
                    total = n_big + n_small
                    h_total = 3600 / total
                    h_big = 3600 / n_big
                    if not (HEADWAY_MIN <= h_total <= HEADWAY_MAX and h_big <= HEADWAY_MAX):
                        continue
                    ratio = n_big / n_small
                    if min(abs(ratio - k) for k in [0.5, 1, 2, 3]) > 0.08:
                        continue
                    small_len = sum(DISTANCE_KM[s:e])
                    train_km = 2 * (n_big * big_len + n_small * small_len)
                    fixed_cost = total * 18.0
                    variable_cost = train_km * 2.6
                    fleet_cost = total * 35.0
                    raw_cost = fixed_cost + variable_cost + fleet_cost
                    wait = h_total / 2
                    crowding = max(max(overlap) / (total * TRAIN_CAPACITY), max(outside) / (n_big * TRAIN_CAPACITY))
                    service = wait + 160 * crowding
                    candidates.append(
                        {
                            "rank": 0,
                            "small_start": s + 1,
                            "small_end": e + 1,
                            "n_big": n_big,
                            "n_small": n_small,
                            "total_trains": total,
                            "headway_s": round(h_total, 1),
                            "big_headway_s": round(h_big, 1),
                            "train_km": round(train_km, 1),
                            "fixed_cost": round(fixed_cost, 1),
                            "variable_cost": round(variable_cost, 1),
                            "fleet_cost": round(fleet_cost, 1),
                            "raw_cost": round(raw_cost, 1),
                            "service_score": round(service, 1),
                            "crowding": round(crowding, 3),
                        }
                    )
    min_cost = min(float(c["raw_cost"]) for c in candidates)
    max_cost = max(float(c["raw_cost"]) for c in candidates)
    min_service = min(float(c["service_score"]) for c in candidates)
    max_service = max(float(c["service_score"]) for c in candidates)
    for c in candidates:
        c["norm_cost"] = round((float(c["raw_cost"]) - min_cost) / (max_cost - min_cost), 4)
        c["norm_service"] = round((float(c["service_score"]) - min_service) / (max_service - min_service), 4)
        c["score"] = round(0.52 * float(c["norm_cost"]) + 0.48 * float(c["norm_service"]), 4)
    candidates.sort(key=lambda x: float(x["score"]))
    for i, c in enumerate(candidates, start=1):
        c["rank"] = i
    return candidates


def build_capacity_audit(plan: dict[str, object]) -> list[dict[str, object]]:
    s = int(plan["small_start"]) - 1
    e = int(plan["small_end"]) - 1
    rows: list[dict[str, object]] = []
    for idx, flow in enumerate(SECTION_FLOW, start=1):
        in_overlap = s <= idx - 1 < e
        trains = int(plan["n_big"]) + int(plan["n_small"]) if in_overlap else int(plan["n_big"])
        cap = trains * TRAIN_CAPACITY
        rows.append(
            {
                "section": f"{idx}-{idx+1}",
                "flow": flow,
                "service_zone": "大小交路重叠" if in_overlap else "大交路独立",
                "train_count": trains,
                "capacity": cap,
                "margin": cap - flow,
                "status": "Pass" if cap >= flow else "Fail",
            }
        )
    return rows


def station_exchange(station_idx: int) -> float:
    peak = max(0, 1 - abs(station_idx - 6) / 6)
    return 220 + 780 * peak


def build_timetable(plan: dict[str, object]) -> list[dict[str, object]]:
    s = int(plan["small_start"]) - 1
    e = int(plan["small_end"]) - 1
    n_big = int(plan["n_big"])
    n_small = int(plan["n_small"])
    total = n_big + n_small
    h = 3600 / total
    travel_to_s = sum(RUN_TIME_S[:s]) + s * DWELL_MIN
    rows: list[dict[str, object]] = []
    big_left = n_big
    small_left = n_small
    last_dep_by_station: dict[int, float] = {}

    for k in range(total):
        if big_left / max(1, big_left + small_left) >= 0.5:
            train_type = "B"
            big_left -= 1
        else:
            train_type = "S"
            small_left -= 1

        overlap_dep = travel_to_s + k * h
        current_time = overlap_dep - travel_to_s if train_type == "B" else overlap_dep
        start_station = 0 if train_type == "B" else s
        end_station = len(STATIONS) - 1 if train_type == "B" else e

        for sta in range(start_station, end_station + 1):
            if sta == start_station:
                arr = current_time
            else:
                arr = current_time + RUN_TIME_S[sta - 1]
            exchange = station_exchange(sta) / total
            dwell = max(DWELL_MIN, min(DWELL_MAX, 14 + 0.16 * exchange))
            dep = arr + dwell
            min_dep = last_dep_by_station.get(sta, -1e9) + TRACKING_MIN
            if dep < min_dep:
                dep = min_dep
                arr = dep - dwell
            last_dep_by_station[sta] = dep
            rows.append(
                {
                    "train": f"T{k+1:02d}",
                    "type": "大交路" if train_type == "B" else "小交路",
                    "station_no": sta + 1,
                    "station": STATIONS[sta],
                    "arrival_s": round(arr, 1),
                    "departure_s": round(dep, 1),
                    "arrival": sec_to_time(arr),
                    "departure": sec_to_time(dep),
                    "dwell_s": round(dwell, 1),
                    "served": "Y",
                }
            )
            current_time = dep
    return rows


def build_tracking_audit(timetable: list[dict[str, object]]) -> list[dict[str, object]]:
    by_station: dict[int, list[dict[str, object]]] = {}
    for r in timetable:
        by_station.setdefault(int(r["station_no"]), []).append(r)
    rows: list[dict[str, object]] = []
    for station_no, events in by_station.items():
        events.sort(key=lambda x: float(x["departure_s"]))
        for prev, cur in zip(events, events[1:]):
            gap = float(cur["departure_s"]) - float(prev["departure_s"])
            rows.append(
                {
                    "station": STATIONS[station_no - 1],
                    "prev_train": prev["train"],
                    "next_train": cur["train"],
                    "gap_s": round(gap, 1),
                    "tracking_min_s": TRACKING_MIN,
                    "status": "Pass" if gap >= TRACKING_MIN else "Fail",
                }
            )
    return rows


def build_dwell_audit(timetable: list[dict[str, object]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for r in timetable:
        dwell = float(r["dwell_s"])
        if dwell <= DWELL_MIN + 0.1 or dwell >= DWELL_MAX - 0.1:
            rows.append(
                {
                    "train": r["train"],
                    "station": r["station"],
                    "dwell_s": round(dwell, 1),
                    "lower_s": DWELL_MIN,
                    "upper_s": DWELL_MAX,
                    "status": "Pass" if DWELL_MIN <= dwell <= DWELL_MAX else "Fail",
                }
            )
    return rows[:30]


def build_scenarios(plan: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for factor in [0.8, 0.9, 1.0, 1.1, 1.2]:
        scaled = [f * factor for f in SECTION_FLOW]
        required = math.ceil(max(scaled) / TRAIN_CAPACITY)
        total = max(required, int(plan["total_trains"]))
        h = 3600 / total
        rows.append(
            {
                "scenario": f"需求{factor:.1f}倍",
                "max_flow": round(max(scaled), 1),
                "required_trains": required,
                "planned_trains": total,
                "headway_s": round(h, 1),
                "recommendation": "保持方案" if factor <= 1.0 else "缩短间隔或增开小交路",
            }
        )
    for headway in [120, 150, 180, 210, 240]:
        total = math.floor(3600 / headway)
        capacity = total * TRAIN_CAPACITY
        rows.append(
            {
                "scenario": f"间隔{headway}s",
                "max_flow": max(SECTION_FLOW),
                "required_trains": math.ceil(max(SECTION_FLOW) / TRAIN_CAPACITY),
                "planned_trains": total,
                "headway_s": headway,
                "recommendation": "容量充足" if capacity >= max(SECTION_FLOW) else "容量不足",
            }
        )
    return rows


def draw_section_flow(path: Path) -> Path:
    font_title, font_label, font_tick = load_fonts()
    width, height, margin = 1100, 620, 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    max_y = max(SECTION_FLOW) * 1.15
    bar_w = (width - 2 * margin) / len(SECTION_FLOW) * 0.62
    for i, value in enumerate(SECTION_FLOW):
        x = margin + (i + 0.5) * (width - 2 * margin) / len(SECTION_FLOW)
        y = height - margin - value / max_y * (height - 2 * margin)
        color = (90 + int(120 * value / max(SECTION_FLOW)), 90, 110)
        draw.rectangle((x - bar_w / 2, y, x + bar_w / 2, height - margin), fill=color, outline=(70, 60, 80))
        draw.text((x - 17, height - margin + 16), f"{i+1}-{i+2}", fill="black", font=font_tick)
    for tick in [0, 6000, 12000, 18000, 24000]:
        y = height - margin - tick / max_y * (height - 2 * margin)
        draw.line((margin - 8, y, margin, y), fill="black", width=2)
        draw.text((margin - 76, y - 10), str(tick), fill="black", font=font_tick)
    draw.text((width // 2 - 190, 32), "断面客流分布示例", fill="black", font=font_title)
    draw.text((width // 2 - 40, height - 42), "区间", fill="black", font=font_label)
    draw.text((margin, margin - 34), "人次/小时", fill="black", font=font_label)
    img.save(path)
    return path


def draw_tradeoff(path: Path, candidates: list[dict[str, object]]) -> Path:
    font_title, font_label, font_tick = load_fonts()
    width, height, margin = 1100, 650, 95
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    xs = [float(c["raw_cost"]) for c in candidates[:60]]
    ys = [float(c["service_score"]) for c in candidates[:60]]
    min_x, max_x = min(xs) * 0.98, max(xs) * 1.02
    min_y, max_y = min(ys) * 0.98, max(ys) * 1.02

    def xy(x: float, y: float) -> tuple[float, float]:
        return (
            margin + (x - min_x) / (max_x - min_x) * (width - 2 * margin),
            height - margin - (y - min_y) / (max_y - min_y) * (height - 2 * margin),
        )

    for c in candidates[:60]:
        x, y = xy(float(c["raw_cost"]), float(c["service_score"]))
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=(80, 130, 180))
    bx, by = xy(float(candidates[0]["raw_cost"]), float(candidates[0]["service_score"]))
    draw.ellipse((bx - 10, by - 10, bx + 10, by + 10), fill=(210, 60, 60))
    draw.text((bx + 12, by - 18), "选定方案", fill=(170, 40, 40), font=font_tick)
    draw.text((width // 2 - 210, 32), "成本-服务水平权衡示例", fill="black", font=font_title)
    draw.text((width // 2 - 70, height - 42), "运营成本", fill="black", font=font_label)
    draw.text((margin, margin - 34), "服务指标", fill="black", font=font_label)
    img.save(path)
    return path


def draw_timetable(path: Path, timetable: list[dict[str, object]]) -> Path:
    font_title, font_label, font_tick = load_fonts()
    width, height, margin = 1200, 760, 90
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)
    draw.rectangle((margin, margin, width - margin, height - margin), outline="black")
    by_train: dict[str, list[dict[str, object]]] = {}
    for r in timetable:
        train_no = str(r["train"])
        if int(train_no[1:]) <= 18:
            by_train.setdefault(train_no, []).append(r)
    max_t = max(float(r["departure_s"]) for r in timetable if int(str(r["train"])[1:]) <= 18)

    def xy(t: float, station_no: int) -> tuple[float, float]:
        x = margin + t / max_t * (width - 2 * margin)
        y = height - margin - (station_no - 1) / (len(STATIONS) - 1) * (height - 2 * margin)
        return x, y

    for train, events in by_train.items():
        events.sort(key=lambda r: int(r["station_no"]))
        pts = [xy(float(r["departure_s"]), int(r["station_no"])) for r in events]
        color = (45, 115, 180) if events[0]["type"] == "大交路" else (180, 70, 120)
        if len(pts) > 1:
            draw.line(pts, fill=color, width=3)
        draw.text((pts[0][0] - 8, pts[0][1] + 5), train, fill=color, font=font_tick)
    for i, sta in enumerate(STATIONS, start=1):
        _, y = xy(0, i)
        draw.line((margin - 5, y, width - margin, y), fill=(230, 230, 230), width=1)
        draw.text((margin - 48, y - 9), sta, fill="black", font=font_tick)
    draw.text((width // 2 - 170, 32), "列车运行图示例", fill="black", font=font_title)
    draw.text((width // 2 - 72, height - 42), "7:00 后分钟", fill="black", font=font_label)
    draw.text((margin, margin - 34), "车站", fill="black", font=font_label)
    img.save(path)
    return path


def write_artifacts(run_name: str, run_dir: Path) -> None:
    candidates = evaluate_candidates()
    plan = candidates[0]
    capacity = build_capacity_audit(plan)
    timetable = build_timetable(plan)
    tracking = build_tracking_audit(timetable)
    dwell = build_dwell_audit(timetable)
    scenarios = build_scenarios(plan)

    write_csv(run_dir / "rail_operation_candidates.csv", candidates[:30], list(candidates[0].keys()))
    write_csv(run_dir / "rail_selected_operation_plan.csv", [plan], list(plan.keys()))
    write_csv(run_dir / "rail_capacity_audit.csv", capacity, list(capacity[0].keys()))
    write_csv(run_dir / "rail_full_timetable.csv", timetable, list(timetable[0].keys()))
    write_csv(run_dir / "rail_tracking_audit.csv", tracking, list(tracking[0].keys()))
    write_csv(run_dir / "rail_dwell_audit.csv", dwell, list(dwell[0].keys()))
    write_csv(run_dir / "rail_scenario_analysis.csv", scenarios, list(scenarios[0].keys()))

    write_latex_table(
        TABLE_DIR / "rail_operation_candidates.tex",
        "轨道交通候选运营方案前五名",
        "tab:rail-operation-candidates",
        ["排名", "小交路", "大交路", "小交路", "总间隔(s)", "成本", "服务指标", "综合分"],
        [
            [
                c["rank"],
                f"{c['small_start']}-{c['small_end']}",
                c["n_big"],
                c["n_small"],
                c["headway_s"],
                c["raw_cost"],
                c["service_score"],
                c["score"],
            ]
            for c in candidates[:5]
        ],
        "ccccrrrr",
    )
    write_latex_table(
        TABLE_DIR / "rail_capacity_audit.tex",
        "选定方案断面容量审查节选",
        "tab:rail-capacity-audit",
        ["区间", "客流", "服务区段", "列车数", "能力", "裕度", "状态"],
        [[r["section"], r["flow"], r["service_zone"], r["train_count"], r["capacity"], r["margin"], r["status"]] for r in capacity],
        "crcrrrc",
    )
    write_latex_table(
        TABLE_DIR / "rail_timetable_sample.tex",
        "列车时刻表节选",
        "tab:rail-timetable-sample",
        ["车次", "类型", "车站", "到达", "出发", "停站(s)"],
        [[r["train"], r["type"], r["station"], r["arrival"], r["departure"], r["dwell_s"]] for r in timetable[:28]],
        "cclccc",
    )
    write_latex_table(
        TABLE_DIR / "rail_scenario_analysis.tex",
        "运营建议场景分析",
        "tab:rail-scenario-analysis",
        ["场景", "最大客流", "所需列车", "计划列车", "间隔(s)", "建议"],
        [[r["scenario"], r["max_flow"], r["required_trains"], r["planned_trains"], r["headway_s"], r["recommendation"]] for r in scenarios],
        "lrrrrl",
    )

    flow_fig = draw_section_flow(FIG_DIR / "rail_section_flow.png")
    tradeoff_fig = draw_tradeoff(FIG_DIR / "rail_cost_service_tradeoff.png", candidates)
    timetable_fig = draw_timetable(FIG_DIR / "rail_timetable_diagram.png", timetable)

    min_capacity_margin = min(int(r["margin"]) for r in capacity)
    min_tracking_gap = min(float(r["gap_s"]) for r in tracking)
    max_dwell = max(float(r["dwell_s"]) for r in timetable)
    pass_status = "Pass" if min_capacity_margin >= 0 and min_tracking_gap >= TRACKING_MIN and max_dwell <= DWELL_MAX else "Needs revision"

    (run_dir / "rail-timetable-summary.md").write_text(
        "\n".join(
            [
                "# Rail Timetable Demo Summary",
                "",
                "This is a synthetic rail-timetable route demo for research and toolchain testing.",
                "",
                f"- Selected small route: station {plan['small_start']} to station {plan['small_end']}",
                f"- Big/small route train counts: {plan['n_big']} / {plan['n_small']}",
                f"- Combined headway: {plan['headway_s']} s",
                f"- Train-km: {plan['train_km']}",
                f"- Minimum capacity margin: {min_capacity_margin}",
                f"- Minimum tracking gap: {min_tracking_gap:.1f} s",
                f"- Maximum dwell time: {max_dwell:.1f} s",
                f"- Overall generated-artifact status: {pass_status}",
                "",
                "Generated artifacts:",
                "",
                "- `rail_operation_candidates.csv`",
                "- `rail_selected_operation_plan.csv`",
                "- `rail_capacity_audit.csv`",
                "- `rail_full_timetable.csv`",
                "- `rail_tracking_audit.csv`",
                "- `rail_dwell_audit.csv`",
                "- `rail_scenario_analysis.csv`",
                f"- `{flow_fig.relative_to(ROOT)}`",
                f"- `{tradeoff_fig.relative_to(ROOT)}`",
                f"- `{timetable_fig.relative_to(ROOT)}`",
            ]
        ),
        encoding="utf-8",
    )

    (run_dir / "artifact-ledger.md").write_text(
        "\n".join(
            [
                "# Artifact Ledger",
                "",
                f"Run: {run_name}",
                "Date: 2026-07-07",
                "Purpose: synthetic rail-timetable route demo for the math-modeling paper generator.",
                "",
                "## Run Metadata",
                "",
                "| Field | Value |",
                "|---|---|",
                f"| Run ID | {run_name} |",
                "| Problem type | Type I: Rail Transit Timetable And Service Planning |",
                "| Code entry point | `src/rail_timetable_demo.py` |",
                "| Data | Synthetic line, section flow, and operating parameters embedded in script |",
                "| Research status | Demo route, not contest evidence |",
                "",
                "## Required Type I Artifacts",
                "",
                "| Artifact | Path | Status |",
                "|---|---|---|",
                "| operation candidates | `runs/" + run_name + "/rail_operation_candidates.csv` | generated |",
                "| selected operation plan | `runs/" + run_name + "/rail_selected_operation_plan.csv` | generated |",
                "| full timetable | `runs/" + run_name + "/rail_full_timetable.csv` | generated |",
                "| capacity audit | `runs/" + run_name + "/rail_capacity_audit.csv` | generated |",
                "| tracking audit | `runs/" + run_name + "/rail_tracking_audit.csv` | generated |",
                "| dwell audit | `runs/" + run_name + "/rail_dwell_audit.csv` | generated |",
                "| scenario analysis | `runs/" + run_name + "/rail_scenario_analysis.csv` | generated |",
                "",
                "## Figures",
                "",
                "| ID | Role | File | Paper label | Status |",
                "|---|---|---|---|---|",
                "| F01 | evidence | `paper/figures/rail_section_flow.png` | `fig:rail-section-flow` | generated |",
                "| F02 | evidence | `paper/figures/rail_cost_service_tradeoff.png` | `fig:rail-cost-service` | generated |",
                "| F03 | evidence | `paper/figures/rail_timetable_diagram.png` | `fig:rail-timetable` | generated |",
                "",
                "## Tables",
                "",
                "| ID | File | Paper label | Status |",
                "|---|---|---|---|",
                "| T01 | `paper/tables/rail_operation_candidates.tex` | `tab:rail-operation-candidates` | generated |",
                "| T02 | `paper/tables/rail_capacity_audit.tex` | `tab:rail-capacity-audit` | generated |",
                "| T03 | `paper/tables/rail_timetable_sample.tex` | `tab:rail-timetable-sample` | generated |",
                "| T04 | `paper/tables/rail_scenario_analysis.tex` | `tab:rail-scenario-analysis` | generated |",
                "",
                "## Key Results",
                "",
                "| ID | Statement | Value | Evidence |",
                "|---|---|---:|---|",
                f"| K01 | selected small route start | {plan['small_start']} | candidate table |",
                f"| K02 | selected small route end | {plan['small_end']} | candidate table |",
                f"| K03 | big route train count | {plan['n_big']} | selected plan |",
                f"| K04 | small route train count | {plan['n_small']} | selected plan |",
                f"| K05 | minimum capacity margin | {min_capacity_margin} | capacity audit |",
                f"| K06 | minimum tracking gap | {min_tracking_gap:.1f} | tracking audit |",
                f"| K07 | maximum dwell time | {max_dwell:.1f} | timetable and dwell audit |",
                "",
                "## Review Summary",
                "",
                f"Generated-artifact status: {pass_status}. PDF writing and final review remain separate steps.",
            ]
        ),
        encoding="utf-8",
    )

    (REVIEWS_DIR / f"review-{run_name}.md").write_text(
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
                "| C01 | full paper | Unknown | This script generates Type I artifacts but does not write a full paper by itself. | Artifact demo alone is not a contest-style paper. | Insert generated tables/figures into LaTeX and compile before pass. |",
                "",
                "## Important Findings",
                "",
                "| ID | Location | Status | Evidence | Risk | Required repair |",
                "|---|---|---|---|---|---|",
                "| I01 | Type I artifacts | Pass | Operation plan, full timetable, capacity audit, tracking audit, dwell audit, and scenario analysis were generated. | Low risk for missing core timetable artifacts. | Check against real problem statement in production runs. |",
                "| I02 | data source | Warn | Data are synthetic and embedded in `src/rail_timetable_demo.py`. | Results cannot support a real contest conclusion. | Replace with parsed attachment data for real runs. |",
                "| I03 | PDF evidence | Unknown | No compile/render check is done by this script. | Layout quality is unverified. | Run `scripts/compile.ps1` and render pages after writing paper sections. |",
                "",
                "## Warnings",
                "",
                "| ID | Location | Status | Evidence | Risk | Suggested repair |",
                "|---|---|---|---|---|---|",
                "| W01 | figures | Pass | Chinese-labeled section-flow, tradeoff, and timetable figures are generated. | Low visual-route risk. | Inspect rendered PDF size and readability. |",
                "",
                "## Evidence Checked",
                "",
                "- Required Type I machine-readable artifacts exist.",
                "- Capacity and tracking audits have pass/fail fields.",
                "- Scenario table exists for Q3-style recommendations.",
                "",
                "## Evidence Missing Or Not Checked",
                "",
                "- Full LaTeX paper integration.",
                "- PDF compile and rendered-page inspection.",
                "- Real-data parsing from a contest attachment.",
                "",
                "## Required Repairs Before Pass",
                "",
                "1. Use the generated artifacts in paper sections.",
                "2. Compile and render the PDF.",
                "3. Replace synthetic data with real problem data for research cases.",
                "",
                "## Human Verification Needed",
                "",
                "- Confirm whether this demo route should become the next packaged v1.1 example.",
                "",
                "## Responsible-Use Notes",
                "",
                "- Synthetic research demo only.",
                "- Do not present outputs as official contest results.",
            ]
        ),
        encoding="utf-8",
    )


def main() -> int:
    run_name = sys.argv[1] if len(sys.argv) > 1 else "rail-demo"
    run_dir = RUNS_DIR / run_name
    ensure_dirs(run_dir)
    write_artifacts(run_name, run_dir)
    print(f"Rail timetable demo artifacts generated in {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
