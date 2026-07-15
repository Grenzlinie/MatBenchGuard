#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetic_properties.json ===
cat > /app/outputs/magnetic_properties.json <<'FFEOF'
{
  "magnetic_moment_muB": 2.0,
  "mae_meV": 5.3
}
FFEOF

# === solve block: exchange_parameters.json ===
cat > /app/outputs/exchange_parameters.json <<'FFEOF'
{
  "J1_meV": 26.86,
  "J2_meV": 3.0,
  "J3_meV": 0.12
}
FFEOF

# === solve block: curie_temperature.txt ===
echo "528.0" > /app/outputs/curie_temperature.txt

# === solve block: topological_properties.json ===
cat > /app/outputs/topological_properties.json <<'FFEOF'
{
  "soc_band_gap_meV": 68.6,
  "chern_number": -1
}
FFEOF
