#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.json ===
python3 -c "
import json
data = {
    'MnO2_clean': {'NH3': -1.59, 'SO2': -0.79, 'NO': -0.46, 'K': -6.28},
    'TiO2_clean': {'NH3': -1.28, 'SO2': -1.11, 'NO': -1.10, 'K': -4.34},
    'K_MnO2':    {'NH3': -0.77, 'SO2': -1.21, 'NO': -0.27},
    'K_TiO2':    {'NH3': -0.74, 'SO2': -1.61, 'NO': -0.45}
}
with open('/app/outputs/adsorption_energies.json', 'w') as f:
    json.dump(data, f, indent=2)
"
