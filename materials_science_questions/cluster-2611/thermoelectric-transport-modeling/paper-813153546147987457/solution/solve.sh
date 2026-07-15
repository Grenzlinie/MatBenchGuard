#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: seebeck_vs_n.json ===
python3 <<EOF
import json
data = {
    "BaSnO3": {"n1e19": -250.0, "n1e20": -150.0, "n1e21": -80.0},
    "KTaO3": {"n1e19": -350.0, "n1e20": -250.0, "n1e21": -180.0}
}
with open("$OUTDIR/seebeck_vs_n.json", "w") as f:
    json.dump(data, f, indent=2)
EOF
