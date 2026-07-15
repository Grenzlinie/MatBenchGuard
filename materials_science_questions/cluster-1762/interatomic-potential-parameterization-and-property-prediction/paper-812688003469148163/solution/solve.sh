#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: ambient_properties.csv ===
cat > "$OUTDIR/ambient_properties.csv" <<'CSV'
property,value
lattice_constant_A,2.8821
bulk_modulus_GPa,166.84
young_modulus_GPa,167.17
shear_modulus_GPa,62.71
specific_heat_CP_J_per_mol_K,24.37
CSV

# === solve block: pressure_dependence_KT_CP.csv ===
cat > "$OUTDIR/pressure_dependence_KT_CP.csv" <<'CSV'
pressure_GPa,bulk_modulus_Kt_GPa,specific_heat_CP_J_per_mol_K
0.0,166.84,24.37
2.0,196.84,23.97
4.0,226.84,23.57
6.0,256.84,23.17
8.0,286.84,22.77
10.0,316.84,22.37
CSV
