#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: moments_and_spectral_function.json ===
python3 -c '
import json
data = {
    "M0": [1.0, 1.0],
    "M1": [-0.5, 0.5],
    "M2": [1.5, 2.5],
    "M3": [0.5, 3.5],
    "M4": [3.5, 8.5],
    "localized_A_sigma": {
        "sigma_plus": {
            "p1": 1/6,
            "p2": 5/6,
            "epsilon1": 2.0,
            "epsilon2": -1.0
        },
        "sigma_minus": {
            "p1": 0.5,
            "p2": 0.5,
            "epsilon1": 2.0,
            "epsilon2": -1.0
        }
    }
}
with open("/app/outputs/moments_and_spectral_function.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: large_radius_condition.json ===
python3 -c '
import json
data = {
    "epsilon_1": 1.0,
    "epsilon_2": -1.0,
    "condition_holds": True,
    "zero_temp_E1": -1.0,
    "zero_temp_E2": 1.0
}
with open("/app/outputs/large_radius_condition.json", "w") as f:
    json.dump(data, f, indent=2)
'
