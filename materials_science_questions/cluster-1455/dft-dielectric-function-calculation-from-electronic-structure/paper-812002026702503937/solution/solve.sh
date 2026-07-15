#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_properties.json ===
cat > /app/outputs/band_properties.json <<'FFEOF'
{
  "Li2CO3": {
    "band_I_width_eV": 0.22,
    "band_II_width_eV": 0.72,
    "band_V_width_eV": 4.0,
    "band_gap_eV": 4.4
  },
  "Na2CO3": {
    "band_I_width_eV": 0.10,
    "band_II_width_eV": 0.33,
    "band_V_width_eV": 0.0,
    "band_gap_eV": 2.6
  }
}
FFEOF

# === solve block: dielectric_function_eps2.csv ===
python3 /solution/generate_eps2.py
