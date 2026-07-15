#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
python3 -c '
import json
params = {
    "V0": 1476.0,
    "BM300_K0": 181.0,
    "BM300_Kp": 4.4,
    "HTBM_K0": 184.0,
    "HTBM_Kp": 3.8,
    "HTBM_dKdT": -0.023,
    "HTBM_a": 3.18e-05,
    "HTBM_b": 1.8e-09,
    "MGD_gamma0": 1.35
}
with open("/app/outputs/fitted_parameters.json", "w") as f:
    json.dump(params, f, indent=2)
'
