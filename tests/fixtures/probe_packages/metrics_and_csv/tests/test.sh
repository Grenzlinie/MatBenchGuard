#!/bin/bash
set -euo pipefail
python - <<'PY'
from pathlib import Path
import json, checker
print(json.dumps(checker.grade(Path("/app/outputs"))))
PY
