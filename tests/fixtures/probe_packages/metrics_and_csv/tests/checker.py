
import csv, json
from pathlib import Path
def grade(outputs_dir: Path):
    with (outputs_dir / "predictions.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    required = ["true_oxidation_state", "predicted_mean", "predicted_std"]
    structural = 1.0 if rows and all(col in rows[0] for col in required) else 0.0
    metrics = json.loads((outputs_dir / "metrics.json").read_text())
    r2 = float(metrics["R2"]); rmse = float(metrics["RMSE"])
    metric_score = max(0.0, 1.0 - abs(r2 - 0.85)/0.5) * 0.5 + max(0.0, 1.0 - abs(rmse - 0.24)/0.5) * 0.5
    reward = 0.2 * structural + 0.8 * metric_score
    return {"reward": reward, "breakdown": {"structural": structural, "metrics": metric_score}}
