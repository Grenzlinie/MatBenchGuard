#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: downward_power_ratio.csv ===
python3 /solution/generate_artifacts.py downward_power_ratio.csv

# === solve block: coupling_efficiency.json ===
python3 -c "
import json
data = {
    'TM': {'peak_efficiency': 0.70, 'peak_wavelength_nm': 1550},
    'TE': {'peak_efficiency': 0.78, 'peak_wavelength_nm': 1550},
    'tolerance_3dB_um': 8.0
}
with open('$OUTDIR/coupling_efficiency.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: mode_overlap_upper_bound.txt ===
python3 /solution/generate_artifacts.py mode_overlap_upper_bound.txt
