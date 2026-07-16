from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[3]
RUN_DIR = Path(__file__).resolve().parents[1]
OUT_DIR = RUN_DIR / "artifacts"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def find_source_dir() -> Path:
    matches = list(ROOT.parent.rglob("CUMCM2021-E.pdf"))
    if not matches:
        raise FileNotFoundError("CUMCM2021-E.pdf not found under workspace")
    return matches[0].parent


def load_workbooks() -> list[Path]:
    files = sorted(find_source_dir().glob("*.xlsx"), key=lambda p: p.name)
    if len(files) != 4:
        raise RuntimeError(f"Expected 4 xlsx attachments, found {len(files)}")
    return files


def read_sheet(path: Path, sheet_index: int = 0) -> pd.DataFrame:
    return pd.read_excel(path, sheet_name=sheet_index, header=0)


def feature_columns(df: pd.DataFrame) -> list:
    return [c for c in df.columns if str(c) not in {"No", "Class", "OP"}]


def clean_label_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().replace({"nan": "", "None": "", "": np.nan})


def zscore_matrix(x: np.ndarray) -> np.ndarray:
    mean = np.nanmean(x, axis=0)
    std = np.nanstd(x, axis=0)
    std[std == 0] = 1.0
    z = (x - mean) / std
    return np.nan_to_num(z)


def nearest_centroid_predict(train_x: np.ndarray, train_y: np.ndarray, test_x: np.ndarray) -> np.ndarray:
    labels = np.array(sorted(set(train_y.astype(str))))
    centroids = []
    for label in labels:
        centroids.append(train_x[train_y.astype(str) == label].mean(axis=0))
    centroids = np.vstack(centroids)
    dists = ((test_x[:, None, :] - centroids[None, :, :]) ** 2).mean(axis=2)
    return labels[dists.argmin(axis=1)]


def leave_one_out_accuracy(x: np.ndarray, y: np.ndarray) -> float:
    if len(y) < 3 or len(set(y.astype(str))) < 2:
        return float("nan")
    preds = []
    for i in range(len(y)):
        mask = np.ones(len(y), dtype=bool)
        mask[i] = False
        pred = nearest_centroid_predict(x[mask], y[mask], x[[i]])[0]
        preds.append(pred)
    return float(np.mean(np.array(preds).astype(str) == y.astype(str)))


def prepare_xy(df: pd.DataFrame, label_col: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, pd.Series]:
    feats = feature_columns(df)
    labels = clean_label_series(df[label_col])
    labeled = labels.notna().to_numpy()
    x_all = zscore_matrix(df[feats].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float))
    y = labels[labeled].to_numpy(dtype=str)
    return x_all, y, labeled, labels


def predict_targets(df: pd.DataFrame, label_col: str, target_ids: list[int]) -> tuple[float, list[dict[str, str]]]:
    x_all, y, labeled, labels = prepare_xy(df, label_col)
    x_labeled = x_all[labeled]
    acc = leave_one_out_accuracy(x_labeled, y)
    no = pd.to_numeric(df["No"], errors="coerce")
    target_mask = no.isin(target_ids).to_numpy()
    preds = nearest_centroid_predict(x_labeled, y, x_all[target_mask])
    rows = []
    for sample_no, existing, pred in zip(no[target_mask].astype(int), labels[target_mask], preds):
        rows.append(
            {
                "No": str(sample_no),
                "label": label_col,
                "existing_value": "" if pd.isna(existing) else str(existing),
                "baseline_prediction": str(pred),
            }
        )
    return acc, rows


def predict_targets_with_matrix(df: pd.DataFrame, x_all: np.ndarray, label_col: str, target_ids: list[int]) -> tuple[float, list[dict[str, str]]]:
    labels = clean_label_series(df[label_col])
    labeled = labels.notna().to_numpy()
    y = labels[labeled].to_numpy(dtype=str)
    acc = leave_one_out_accuracy(x_all[labeled], y)
    no = pd.to_numeric(df["No"], errors="coerce")
    target_mask = no.isin(target_ids).to_numpy()
    preds = nearest_centroid_predict(x_all[labeled], y, x_all[target_mask])
    return acc, [
        {
            "No": str(sample_no),
            "label": label_col,
            "existing_value": "" if pd.isna(existing) else str(existing),
            "baseline_prediction": str(pred),
        }
        for sample_no, existing, pred in zip(no[target_mask].astype(int), labels[target_mask], preds)
    ]


def downsample_curve(x: np.ndarray, y: np.ndarray, n: int = 300) -> tuple[np.ndarray, np.ndarray]:
    if len(x) <= n:
        return x, y
    idx = np.linspace(0, len(x) - 1, n).astype(int)
    return x[idx], y[idx]


def polyline(points: list[tuple[float, float]], color: str) -> str:
    pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in points)
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="1.4" />'


def plot_mean_curves(groups: list[tuple[str, np.ndarray, np.ndarray]], title: str, path: Path) -> None:
    width, height = 920, 420
    margin = 55
    all_x = np.concatenate([g[1] for g in groups])
    all_y = np.concatenate([g[2] for g in groups])
    xmin, xmax = float(all_x.min()), float(all_x.max())
    ymin, ymax = float(all_y.min()), float(all_y.max())
    if math.isclose(ymin, ymax):
        ymax = ymin + 1
    colors = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#ff7f0e", "#17becf"]
    elements = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white" />',
        f'<text x="{width/2}" y="26" text-anchor="middle" font-family="Arial" font-size="18">{title}</text>',
        f'<line x1="{margin}" y1="{height-margin}" x2="{width-margin}" y2="{height-margin}" stroke="#444" />',
        f'<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height-margin}" stroke="#444" />',
        f'<text x="{width/2}" y="{height-12}" text-anchor="middle" font-family="Arial" font-size="13">wave number (cm^-1)</text>',
        f'<text x="18" y="{height/2}" transform="rotate(-90 18 {height/2})" text-anchor="middle" font-family="Arial" font-size="13">absorbance</text>',
    ]
    for i, (label, x, y) in enumerate(groups):
        x, y = downsample_curve(x, y)
        sx = margin + (x - xmin) / (xmax - xmin) * (width - 2 * margin)
        sy = height - margin - (y - ymin) / (ymax - ymin) * (height - 2 * margin)
        elements.append(polyline(list(zip(sx, sy)), colors[i % len(colors)]))
        elements.append(
            f'<text x="{width-margin-150}" y="{margin + 20*i}" font-family="Arial" font-size="12" fill="{colors[i % len(colors)]}">{label}</text>'
        )
    elements.append("</svg>")
    path.write_text("\n".join(elements), encoding="utf-8")


def mean_curves_by_label(df: pd.DataFrame, label_col: str, max_groups: int = 5) -> list[tuple[str, np.ndarray, np.ndarray]]:
    feats = feature_columns(df)
    wave = np.array([float(c) for c in feats])
    labels = clean_label_series(df[label_col])
    groups = []
    for label in sorted(labels.dropna().unique().astype(str))[:max_groups]:
        mask = labels.astype(str) == label
        values = df.loc[mask, feats].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)
        groups.append((f"{label_col} {label}", wave, np.nanmean(values, axis=0)))
    return groups


def main() -> None:
    files = load_workbooks()
    a1 = read_sheet(files[0])
    a2 = read_sheet(files[1])
    a3_nir = read_sheet(files[2], 0)
    a3_mir = read_sheet(files[2], 1)
    a4 = read_sheet(files[3])

    q2_ids = [3, 14, 38, 48, 58, 71, 79, 86, 89, 110, 134, 152, 227, 331, 618]
    q3_ids = [4, 15, 22, 30, 34, 45, 74, 114, 170, 209]
    q4_ids = [94, 109, 140, 278, 308, 330, 347]

    baseline_rows = []
    q2_acc, q2_rows = predict_targets(a2, "OP", q2_ids)
    baseline_rows.append({"task": "Q2 OP MIR", "loo_accuracy": q2_acc, "notes": "nearest-centroid baseline"})

    x3_nir = zscore_matrix(a3_nir[feature_columns(a3_nir)].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float))
    x3_mir = zscore_matrix(a3_mir[feature_columns(a3_mir)].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float))
    x3_fused = np.concatenate([x3_nir, x3_mir], axis=1)
    q3_nir_acc, q3_nir_rows = predict_targets_with_matrix(a3_nir, x3_nir, "OP", q3_ids)
    q3_mir_acc, q3_mir_rows = predict_targets_with_matrix(a3_mir, x3_mir, "OP", q3_ids)
    q3_fused_acc, q3_rows = predict_targets_with_matrix(a3_nir, x3_fused, "OP", q3_ids)
    baseline_rows.extend(
        [
            {"task": "Q3 OP NIR", "loo_accuracy": q3_nir_acc, "notes": "nearest-centroid baseline"},
            {"task": "Q3 OP MIR", "loo_accuracy": q3_mir_acc, "notes": "nearest-centroid baseline"},
            {"task": "Q3 OP fused", "loo_accuracy": q3_fused_acc, "notes": "concat NIR+MIR nearest-centroid baseline"},
        ]
    )

    q4_class_acc, q4_class_rows = predict_targets(a4, "Class", q4_ids)
    q4_op_acc, q4_op_rows = predict_targets(a4, "OP", q4_ids)
    baseline_rows.extend(
        [
            {"task": "Q4 Class NIR", "loo_accuracy": q4_class_acc, "notes": "nearest-centroid baseline"},
            {"task": "Q4 OP NIR", "loo_accuracy": q4_op_acc, "notes": "nearest-centroid baseline"},
        ]
    )

    with (OUT_DIR / "baseline_summary.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["task", "loo_accuracy", "notes"])
        writer.writeheader()
        writer.writerows(baseline_rows)

    target_rows = []
    for task, rows in [
        ("Q2 OP MIR", q2_rows),
        ("Q3 OP NIR", q3_nir_rows),
        ("Q3 OP MIR", q3_mir_rows),
        ("Q3 OP fused", q3_rows),
        ("Q4 Class NIR", q4_class_rows),
        ("Q4 OP NIR", q4_op_rows),
    ]:
        for row in rows:
            row = dict(row)
            row["task"] = task
            target_rows.append(row)
    with (OUT_DIR / "target_row_baseline_predictions.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["task", "No", "label", "existing_value", "baseline_prediction"])
        writer.writeheader()
        writer.writerows(target_rows)

    groups = []
    feats_a2 = feature_columns(a2)
    wave_a2 = np.array([float(c) for c in feats_a2])
    labels_a2 = clean_label_series(a2["OP"])
    for label in sorted(labels_a2.dropna().unique().astype(str))[:5]:
        values = a2.loc[labels_a2.astype(str) == label, feats_a2].apply(pd.to_numeric, errors="coerce").to_numpy(dtype=float)
        groups.append((f"OP {label}", wave_a2, np.nanmean(values, axis=0)))
    plot_mean_curves(groups, "Attachment 2 MIR mean spectra by OP", OUT_DIR / "attachment2_mir_mean_by_op.svg")

    plot_mean_curves(mean_curves_by_label(a4, "Class", 3), "Attachment 4 NIR mean spectra by Class", OUT_DIR / "attachment4_nir_mean_by_class.svg")

    md = ["# Minimal EDA Baseline Results", ""]
    md.append("This is a route-calibration baseline, not the final modeling result.")
    md.append("")
    md.append("## Leave-One-Out Baseline")
    md.append("")
    md.append("| Task | LOO accuracy | Notes |")
    md.append("|---|---:|---|")
    for row in baseline_rows:
        value = row["loo_accuracy"]
        acc = "n/a" if math.isnan(value) else f"{value:.3f}"
        md.append(f"| {row['task']} | {acc} | {row['notes']} |")
    md.append("")
    md.append("## Output Files")
    md.append("")
    md.append("- `artifacts/baseline_summary.csv`")
    md.append("- `artifacts/target_row_baseline_predictions.csv`")
    md.append("- `artifacts/attachment2_mir_mean_by_op.svg`")
    md.append("- `artifacts/attachment4_nir_mean_by_class.svg`")
    md.append("")
    md.append("## Calibration Reading")
    md.append("")
    md.append("- A simple nearest-centroid baseline is intentionally weak but useful as a sanity check.")
    md.append("- Any later stronger route must beat this baseline under a comparable split and explain remaining weak classes or origins.")
    md.append("- Q3 must compare NIR-only, MIR-only, and fused routes before claiming fusion is useful.")
    (OUT_DIR / "minimal_eda_baseline.md").write_text("\n".join(md), encoding="utf-8")


if __name__ == "__main__":
    main()
