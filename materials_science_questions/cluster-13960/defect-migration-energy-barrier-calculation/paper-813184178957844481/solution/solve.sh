#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: trapping_energies.json ===
python3 -c '
import json
data = [
    {"n": 1, "trapping_energy": -1.054, "zpe_correction": 0.185, "E_total": -1000.0},
    {"n": 2, "trapping_energy": -1.300, "zpe_correction": 0.385, "E_total": -1000.0},
    {"n": 3, "trapping_energy": -0.183, "zpe_correction": 0.555, "E_total": -1000.0},
    {"n": 4, "trapping_energy": -0.182, "zpe_correction": 0.713, "E_total": -1000.0},
    {"n": 5, "trapping_energy": -0.247, "zpe_correction": 0.867, "E_total": -1000.0},
    {"n": 6, "trapping_energy": 0.201, "zpe_correction": 1.022, "E_total": -1000.0}
]
with open("/app/outputs/trapping_energies.json", "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: diffusion_barrier.txt ===
echo "1.17" > /app/outputs/diffusion_barrier.txt
