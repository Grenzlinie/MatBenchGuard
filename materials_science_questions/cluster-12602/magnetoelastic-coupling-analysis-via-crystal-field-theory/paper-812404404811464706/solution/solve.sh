#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: tc_vs_strain.json ===
python3 << 'PYEOF'
import json
data = [{"epsilon33": e, "Tc": 89.0 + 8000.0 * e} for e in [-0.005, -0.0025, 0.0, 0.0025, 0.005]]
json.dump(data, open("/app/outputs/tc_vs_strain.json", "w"))
PYEOF
