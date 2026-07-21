#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python - <<'PY'
import json
from pathlib import Path
Path("/app/outputs/labels.json").write_text(json.dumps({"phase":"metal","stability":"stable"}))
PY
