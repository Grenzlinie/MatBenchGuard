#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: computed_band_edges.json ===
python3 -c "
import json
data = {
  'TiO2': -0.01,
  'WO3': -0.54,
  'CdS': 1.27,
  'ZnSe': 1.60,
  'GaAs': 1.07,
  'GaP': 1.29,
  'WO3_GGA+U': -0.34
}
with open('/app/outputs/computed_band_edges.json', 'w') as f:
  json.dump(data, f)
"
