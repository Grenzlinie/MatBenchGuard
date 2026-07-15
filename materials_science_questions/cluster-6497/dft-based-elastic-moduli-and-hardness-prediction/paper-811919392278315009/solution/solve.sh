#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_ZnO_properties.csv ===
cat > /app/outputs/bulk_ZnO_properties.csv <<'FFEOF'
Method,Property,Units,Value
relaxation,lattice constant a,Å,3.265
relaxation,c/a ratio,-,1.579
relaxation,internal parameter u,-,0.3882
slab calculation,surface energy (10-10),J/m^2,1.14
slab calculation,surface energy (11-20),J/m^2,1.19
energy-strain fitting,Young's modulus energy,GPa,173.86
virial stress,Young's modulus virial,GPa,173.27
FFEOF

# === solve block: NW_young_moduli.csv ===
cat > /app/outputs/NW_young_moduli.csv <<'FFEOF'
Radius,Structure,Young_modulus_energy,Young_modulus_virial
8.707,NW-1,213.0,213.0
28.297,NW-3,196.0,196.0
47.887,NW-5,183.0,183.0
FFEOF

# === solve block: NT_young_moduli.csv ===
cat > /app/outputs/NT_young_moduli.csv <<'FFEOF'
Inner_radius,Outer_radius,Structure,Type,Wall_thickness,Young_modulus_energy,Young_modulus_virial
7.618,15.237,NT-A-1,A,7.619,255.0,255.0
7.618,34.827,NT-A-3,A,27.209,198.0,198.0
46.798,54.417,NT-B-1,B,7.619,253.0,253.0
17.413,54.417,NT-B-4,B,37.004,190.0,190.0
FFEOF
