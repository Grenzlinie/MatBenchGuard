#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: reproduced_properties.json ===
python3 /solution/write_reproduced.py > /app/outputs/reproduced_properties.json
