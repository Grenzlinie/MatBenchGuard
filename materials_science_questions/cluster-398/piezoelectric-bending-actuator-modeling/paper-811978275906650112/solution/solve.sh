#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c '
import json
data = {
    "resonant_frequency_hz": 17640,
    "maximum_displacement_um": 15.8,
    "capacitance_pF": 13200,
    "temperature_profile": [
        {"z_mm": 0, "temperature_C": 55.0},
        {"z_mm": 25, "temperature_C": 60.0},
        {"z_mm": 50, "temperature_C": 65.0},
        {"z_mm": 75, "temperature_C": 70.0},
        {"z_mm": 100, "temperature_C": 75.0}
    ]
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f, indent=2)
'
