
import json
from pathlib import Path
def grade(outputs_dir: Path):
    data = json.loads((outputs_dir / "labels.json").read_text())
    target = {"phase": "metal", "stability": "stable"}
    scores = [1.0 if data.get(k) == v else 0.0 for k, v in target.items()]
    reward = sum(scores) / len(scores)
    return {"reward": reward, "breakdown": {k: s for k, s in zip(target, scores)}}
