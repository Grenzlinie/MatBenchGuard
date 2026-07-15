#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_03_ler_vs_ky.csv ===
python3 /solution/generate_ler_data.py

# === solve block: step_04_peaks.json ===
cat > /app/outputs/step_04_peaks.json <<'FFEOF'
{
  "baseline_ler": 20.0,
  "peaks": [
    {"center_ky": 51.0, "fwhm": 14.0, "relative_increase": 1.10},
    {"center_ky": 93.0, "fwhm": 28.0, "relative_increase": 2.67},
    {"center_ky": 165.0, "fwhm": 19.0, "relative_increase": 1.72}
  ]
}
FFEOF
