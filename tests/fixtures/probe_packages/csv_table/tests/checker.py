
import csv
from pathlib import Path
def grade(outputs_dir: Path):
    with (outputs_dir / "predictions.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = ["true_value", "predicted_mean", "predicted_std"]
    if not rows or any(col not in rows[0] for col in required):
        return {"reward": 0.0, "breakdown": {"_errors": {"schema": "missing"}}}
    # score by closeness of predicted_mean to true_value
    errs = []
    for row in rows:
        true = float(row["true_value"]); pred = float(row["predicted_mean"]); std = float(row["predicted_std"])
        if std < 0:
            return {"reward": 0.0, "breakdown": {"_errors": {"std": "negative"}}}
        errs.append(abs(true - pred))
    mae = sum(errs)/len(errs)
    reward = max(0.0, 1.0 - mae)
    return {"reward": reward, "breakdown": {"mae_score": reward}}
