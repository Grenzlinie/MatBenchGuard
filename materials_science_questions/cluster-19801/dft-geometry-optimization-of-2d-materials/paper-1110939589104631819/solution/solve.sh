#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: critical_expansion.json ===
cat > /app/outputs/critical_expansion.json <<'FFEOF'
{
  "critical_delta_d_d0": 0.0034,
  "critical_delta_V_V0": -0.0068
}
FFEOF

# === solve block: wavefunction_distribution.csv ===
python3 /solution/generate_wavefunction.py /app/outputs/wavefunction_distribution.csv

# === solve block: spatial_spectrum.json ===
cat > /app/outputs/spatial_spectrum.json <<'FFEOF'
{
  "blocking_ratio_100BL": 0.49,
  "surface_peak_weight_relaxed": 0.49,
  "surface_peak_weight_unrelaxed": 1.0
}
FFEOF
