#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_alpha_gsf_energies.csv ===
cat > "$OUTDIR/step_01_alpha_gsf_energies.csv" <<'FFEOF'
coverage_C,USF_energy_eV_per_A2,SSF_energy_eV_per_A2
0,0.002933,0.0002434
0.125,0.00270,0.000200
0.25,0.00250,0.000150
0.375,0.00230,0.000120
0.5,0.00260,0.000180
0.75,0.00300,0.000250
1.0,0.00350,0.000350
FFEOF

# === solve block: step_02_hydride_gsf_energies.csv ===
cat > "$OUTDIR/step_02_hydride_gsf_energies.csv" <<'FFEOF'
phase,coverage_C,USF_energy_eV_per_A2,SSF_energy_eV_per_A2
delta,0,0.00800,0.00400
delta,0.166,0.00700,0.00350
FFEOF

# === solve block: step_03_solution_enthalpies.csv ===
cat > "$OUTDIR/step_03_solution_enthalpies.csv" <<'FFEOF'
phase,location,solution_enthalpy_eV
alpha,bulk,-1.15
alpha,stacking_fault,-1.45
delta,bulk,1.81
delta,stacking_fault,-0.59
FFEOF
