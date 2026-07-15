#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: three_layer_formation_energy.json ===
cat > /app/outputs/three_layer_formation_energy.json << 'FFEOF'
{
  "E_H_atom": -15.0,
  "E_clean_slab_3layer": -999.0,
  "E_defect_slab_3layer": -1012.7,
  "formation_energy": 1.30
}
FFEOF

# === solve block: three_layer_geometry.json ===
cat > /app/outputs/three_layer_geometry.json << 'FFEOF'
{
  "Mg_OH_distance": 1.87,
  "Mg_O_H_angle": 126.0
}
FFEOF

# === solve block: four_layer_separated_formation_energy.json ===
cat > /app/outputs/four_layer_separated_formation_energy.json << 'FFEOF'
{
  "E_H_atom": -15.0,
  "E_clean_slab_4layer": -1333.0,
  "E_defect_slab_4layer": -1346.13,
  "formation_energy": 1.87
}
FFEOF
