#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/write_outputs.py "$OUTDIR"

# === solve block: backscattering_coefficients.csv ===
cat > "$OUTDIR/backscattering_coefficients.csv" <<'CSVEOF'
material,foil_thickness_in_s0_or_inf,incident_energy_MeV,backscattering_coefficient
graphite,inf,1.0,0.17
aluminium,inf,1.0,0.20
silver,inf,1.0,0.40
lead,inf,1.0,0.34
aluminium,0.1,0.25,0.05
aluminium,0.2,0.25,0.09
aluminium,0.3,0.25,0.12
aluminium,0.4,0.25,0.135
aluminium,0.5,0.25,0.14
aluminium,0.6,0.25,0.145
aluminium,0.7,0.25,0.148
aluminium,0.8,0.25,0.149
aluminium,0.9,0.25,0.15
aluminium,1.0,0.25,0.15
CSVEOF

# === solve block: transmission_coefficients.csv ===
echo 'transmission_coefficients.csv written'

# === solve block: energy_deposition_al_1MeV.csv ===
echo 'energy_deposition_al_1MeV.csv written'
