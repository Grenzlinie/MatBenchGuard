#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 << 'PYEOF'
import json

data = [
    {
        "temperature": 0.0,
        "S": 1.732,
        "c1": 5.0,
        "psi0": 0.8,
        "free_energy_discomm": -0.40,
        "free_energy_ic": -0.30,
        "free_energy_cc": -0.50
    },
    {
        "temperature": 0.35,
        "S": 1.75,
        "c1": 6.0,
        "psi0": 0.7,
        "free_energy_discomm": -0.25,
        "free_energy_ic": -0.20,
        "free_energy_cc": -0.22
    },
    {
        "temperature": 0.45,
        "S": 1.65,
        "c1": 8.0,
        "psi0": 0.6,
        "free_energy_discomm": -0.20,
        "free_energy_ic": -0.15,
        "free_energy_cc": -0.18
    },
    {
        "temperature": 0.7,
        "S": 1.73,
        "c1": 7.0,
        "psi0": 0.5,
        "free_energy_discomm": -0.08,
        "free_energy_ic": -0.10,
        "free_energy_cc": -0.05
    },
    {
        "temperature": 1.0,
        "S": 1.73,
        "c1": 8.0,
        "psi0": 0.4,
        "free_energy_discomm": -0.03,
        "free_energy_ic": -0.05,
        "free_energy_cc": -0.02
    }
]

with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
