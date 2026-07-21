import json
from pathlib import Path

value = json.loads(Path("/app/outputs/result.json").read_text())
assert isinstance(value["model"]["metrics"]["rmse"], (int, float))
assert isinstance(value["validation"]["score"], (int, float))
