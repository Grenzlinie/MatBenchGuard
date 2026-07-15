#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: fitted_k_coefficients.json ===
python3 << 'EOF'
import json
import os

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")
out_path = os.path.join(OUTDIR, "fitted_k_coefficients.json")

# Cu k-coefficients from Table 1 (erg/cm^2)
data = {
    "k0": 1666.87,
    "k1": 733.621,
    "k2": -1873.19,
    "k3": -3260.43
}

with open(out_path, "w") as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: computed_epsilon_coefficients.json ===
python3 /solution/write_artifacts.py "$OUTDIR/computed_epsilon_coefficients.json"

# === solve block: phasefield_vs_wulff_deviation.txt ===
python3 /solution/write_artifacts.py "$OUTDIR/phasefield_vs_wulff_deviation.txt"
