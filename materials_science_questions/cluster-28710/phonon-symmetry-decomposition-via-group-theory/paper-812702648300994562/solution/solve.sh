#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: decomposition.json ===
python3 << 'PYEOF'
import json
data = {
  "layer": {
    "acoustic": {"A2''": 1, "E'": 1},
    "optical": {"A1'": 2, "A2''": 1, "E'": 1, "E''": 2}
  },
  "gamma": {
    "acoustic": {"A1": 1, "E": 1},
    "optical": {"A1": 3, "E": 3},
    "interlayer": {},
    "intralayer": {"A1": 3, "E": 3}
  },
  "epsilon": {
    "acoustic": {"A2''": 1, "E'": 1},
    "optical": {"A1'": 4, "A2''": 3, "E'": 3, "E''": 4},
    "interlayer": {"A2''": 1, "E'": 1},
    "intralayer": {"A1'": 4, "A2''": 2, "E'": 2, "E''": 4}
  },
  "beta": {
    "acoustic": {"A2u": 1, "E1u": 1},
    "optical": {"A1g": 2, "A2u": 1, "B2g": 2, "B1u": 2, "E2g": 2, "E2u": 2, "E1g": 2, "E1u": 1},
    "interlayer": {"B2g": 1, "E2g": 1},
    "intralayer": {"A1g": 2, "A2u": 1, "B2g": 1, "B1u": 2, "E2g": 1, "E2u": 2, "E1g": 2, "E1u": 1}
  }
}
with open("/app/outputs/decomposition.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
PYEOF
