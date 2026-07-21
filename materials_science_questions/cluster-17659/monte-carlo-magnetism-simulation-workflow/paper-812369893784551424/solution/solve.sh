#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: regimes.json ===
python3 -c '
import json
with open("/app/outputs/regimes.json","w") as f:
    json.dump({"t1":0.09,"t2":0.16,"h_plateau":0.5}, f)
'
