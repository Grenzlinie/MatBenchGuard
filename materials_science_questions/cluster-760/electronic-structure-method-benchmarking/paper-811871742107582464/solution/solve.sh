#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: geometries_and_energies.csv ===
cat > /app/outputs/geometries_and_energies.csv <<'EOF'
ZPE_corrected_energy_Hartree,multiplicity,relative_energy_kcal_mol,species
0.0,5,0.0,Fe
0.0,1,0.0,CCl4
-0.004781,5,-3.0,Fe_CCl4_complex
-0.030281,5,-19.0,FeCl_CCl3_complex
-0.129059,5,-81.0,ClFeCCl3
-0.087640,5,-55.0,FeCl2_plus_CCl2
-0.151391,5,-95.0,Cl2FeCCl2
-0.105172,3,-66.0,Cl3FeCCl
-0.239022,5,-150.0,Cl2FeCFeCl2
EOF
