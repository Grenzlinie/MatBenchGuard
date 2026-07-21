#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 << 'PYEOF'
import json

data = {
    "z": 1.392,
    "z_err": 0.010,
    "b_uniform": 0.75,
    "b_err_uniform": 0.04,
    "lambda_z_uniform": 1.08,
    "lambda_z_err_uniform": 0.05,
    "b_sigma0.55": 0.77,
    "b_err_sigma0.55": 0.02,
    "lambda_z_sigma0.55": 1.16,
    "lambda_z_err_sigma0.55": 0.07
}

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
print("results.json written")
PYEOF
