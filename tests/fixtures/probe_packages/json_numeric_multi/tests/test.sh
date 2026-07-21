#!/bin/bash
set -euo pipefail
python - <<'PY'
from pathlib import Path
import json, checker
result = checker.grade(Path("/app/outputs"))
print(json.dumps(result))
PY
