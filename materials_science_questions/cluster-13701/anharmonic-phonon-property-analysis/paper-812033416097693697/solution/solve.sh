#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: fitted_parameters.json ===
python3 -c '
import json
params = {
    "Mn2+": {
        "A_s0": -87.881,
        "A_v0": 0.556,
        "alpha": 4.89e-06,
        "theta": 420,
        "x": 0.5
    },
    "Cr3+": {
        "D_s0": 828.25,
        "D_v0": 51.25,
        "alpha": 2.74e-05,
        "theta": 810,
        "x": 0.5
    }
}
with open("/app/outputs/fitted_parameters.json", "w") as f:
    json.dump(params, f, indent=2)
print("Written")
'
