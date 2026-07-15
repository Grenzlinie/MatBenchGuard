#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_data.json ===
python3 -c '
import json

data = {
    "Ni2MnGa": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, -0.30, -0.45, -0.20, 0.0],
        "T2g_at_Gamma": 0.80
    },
    "Ni2MnAl": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, -0.25, -0.35, -0.15, 0.0],
        "T2g_at_Gamma": 0.75
    },
    "Ni2MnIn": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, -0.20, -0.30, -0.10, 0.0],
        "T2g_at_Gamma": 0.85
    },
    "Ni2MnGe": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, -0.05, -0.15, -0.05, 0.0],
        "T2g_at_Gamma": 0.78
    },
    "Co2MnGa": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, 0.30, 0.60, 0.90, 1.20],
        "T2g_at_Gamma": 1.55
    },
    "Co2MnGe": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, 0.35, 0.70, 1.05, 1.40],
        "T2g_at_Gamma": 1.60
    },
    "Ni2TiGa": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, -0.10, -0.20, -0.05, 0.0],
        "T2g_at_Gamma": 0.72
    },
    "Fe2MnGa": {
        "zeta": [0.0, 0.25, 0.5, 0.75, 1.0],
        "TA2": [0.0, 0.25, 0.50, 0.75, 1.00],
        "T2g_at_Gamma": 1.45
    }
}

with open("/app/outputs/phonon_data.json", "w") as f:
    json.dump(data, f, indent=2)
'
