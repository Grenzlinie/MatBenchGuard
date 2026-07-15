#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: clean_surface_properties.csv ===
cat > "$OUTDIR/clean_surface_properties.csv" <<'EOF'
surface,termination,surface_energy_J_per_m2,work_function_eV
Mg(0001),,0.568,3.740
Ca(100),,0.451,2.753
Ca(110),,0.531,2.845
Ca(111),,0.460,2.983
MgCa(100)-I,I,0.388,2.928
MgCa(100)-II,II,0.906,3.412
MgCa(110),,0.563,3.147
MgCa(111)-I,I,0.498,2.705
MgCa(111)-II,II,0.796,3.242
EOF

# === solve block: adsorption_properties.csv ===
cat > "$OUTDIR/adsorption_properties.csv" <<'EOF'
surface,adsorption_site,adsorption_energy_eV,work_function_eV
Mg(0001),top,-3.557,5.510
Mg(0001),hcp,-4.147,4.01
Mg(0001),fcc,-4.156,4.057
Ca(111),hcp,-5.326,2.995
Ca(111),fcc,-5.299,3.031
MgCa(110),top Ca,-4.218,4.832
MgCa(110),top Mg,-4.237,3.691
MgCa(110),long,-4.989,3.805
MgCa(110),short,-4.614,2.995
EOF

# === solve block: dimer_properties.csv ===
cat > "$OUTDIR/dimer_properties.csv" <<'EOF'
dimer,bond_length_angstrom,bond_energy_kJ_per_mol
Mg-Cl,2.24,308.1
Ca-Cl,2.42,429.1
EOF
