#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: stress_strain_data.csv ===
python3 /solution/gen_stress_strain.py /app/outputs/stress_strain_data.csv

# === solve block: properties_summary.csv ===
cat > /app/outputs/properties_summary.csv <<'EOF'
thickness_nm,temperature_K,young_modulus_GPa,ultimate_tensile_strength_GPa
1,200,260,42
1,300,250,40
1,500,230,35
1,700,200,28
1,900,150,18
2,300,130,26
3,300,110,22
4,300,100,20
5,300,98,19.8
6,300,97,19.7
EOF
