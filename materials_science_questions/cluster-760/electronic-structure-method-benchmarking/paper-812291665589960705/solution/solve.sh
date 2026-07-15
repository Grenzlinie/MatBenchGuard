#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: b2_frequency.json ===
python3 -c '
import json
data = {"b2_frequency": 139.0, "unit": "cm^-1"}
with open("/app/outputs/b2_frequency.json", "w") as f:
    json.dump(data, f)
'
