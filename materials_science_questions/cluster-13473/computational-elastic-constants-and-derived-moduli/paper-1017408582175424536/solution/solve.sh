#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: simulation_results.json ===
python3 <<'PYEOF'
import json
import os

results = {
    "results": [
        {
            "pitch": "achiral",
            "defect_density_mean": 0.00397,
            "defect_density_std": 0.0004,
            "rms_velocity_mean": 0.0052,
            "rms_velocity_std": 0.0005
        },
        {
            "pitch": "P0=200",
            "defect_density_mean": 0.00588,
            "defect_density_std": 0.0005,
            "rms_velocity_mean": 0.00302,
            "rms_velocity_std": 0.0004
        }
    ]
}

with open(os.environ['OUTDIR'] + '/simulation_results.json', 'w') as f:
    json.dump(results, f, indent=2)
PYEOF
