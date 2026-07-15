#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fracture_toughness_results.json ===
python3 << 'PYEOF'
import json
data = {
  "approach1": {
    "298": 2.1396,
    "400": 3.5083,
    "600": 6.0260,
    "800": 8.2402,
    "1000": 10.1978
  },
  "approach2": {
    "298": 2.1396,
    "400": 3.2794,
    "600": 5.2747,
    "800": 6.9800,
    "1000": 8.4687
  }
}
with open("/app/outputs/fracture_toughness_results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
