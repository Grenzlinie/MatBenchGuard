
import json
from pathlib import Path
def grade(outputs_dir: Path):
    data = json.loads((outputs_dir / "metrics.json").read_text())
    target = {"R2": 0.9, "RMSE": 0.1, "MAE": 0.05}
    scores = []
    for key, expected in target.items():
        value = float(data[key])
        if key == "R2":
            scores.append(max(0.0, 1.0 - abs(value - expected) / 0.5))
        else:
            scores.append(max(0.0, 1.0 - abs(value - expected) / max(expected, 1e-6)))
    reward = sum(scores) / len(scores)
    return {"reward": reward, "breakdown": {k: s for k, s in zip(target, scores)}}
