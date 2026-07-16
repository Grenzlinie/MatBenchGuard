#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: dft_adsorption_energies.json ===
cat > /app/outputs/dft_adsorption_energies.json <<'FFEOF'
{
  "pristine_graphene": -0.40870,
  "stw_graphene": -1.03600
}
FFEOF

# === solve block: graphene_tensile_stress_strain.csv ===
python3 /solution/generate_data.py graphene > /app/outputs/graphene_tensile_stress_strain.csv

# === solve block: composite_longitudinal_shear.csv ===
python3 /solution/generate_data.py shear > /app/outputs/composite_longitudinal_shear.csv

# === solve block: surface_roughness.csv ===
cat > /app/outputs/surface_roughness.csv <<'FFEOF'
defect_count,roughness_angstrom,max_displacement_angstrom
0,0.2640,0.7914
5,0.3539,1.3752
10,0.5242,1.5415
FFEOF
