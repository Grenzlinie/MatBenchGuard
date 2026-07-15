#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: adsorption_results.csv ===
cat > /app/outputs/adsorption_results.csv <<'FFEOF'
fr,type,distance_Angstrom,adsorption_energy_kcal_mol,charge_transfer,displacement_Angstrom
CH,I,3.44,-2.07,0.0060,
CH,II,2.48,-2.59,0.0905,
CH,III,0.95,-41.65,0.1805,1.84
CH,IV,1.24,-47.91,0.1810,1.07
CH3,I,3.29,-2.41,0.0023,
CH3,II,3.04,-2.68,0.0032,
CH3,III,1.56,-27.92,-0.0250,0.84
C2H,I,1.50,-44.26,0.1082,0.87
C2H3,I,3.33,-4.86,0.0358,
C2H3,II,1.54,-28.37,0.0034,0.84
C2H5,I,3.24,-2.74,0.0018,
C2H5,II,3.22,-3.39,0.0028,
C2H5,III,1.59,-21.71,-0.0450,0.85
OH,I,3.21,-7.54,0.2145,
OH,II,2.35,-10.05,0.2799,
OH,III,1.51,-30.11,0.1672,0.78
FFEOF
