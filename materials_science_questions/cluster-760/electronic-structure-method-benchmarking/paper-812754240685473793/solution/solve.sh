#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: initial_step_energies.csv ===
cat > "$OUTDIR/initial_step_energies.csv" <<'FFEOF'
Reaction,Energy_barrier_kcal_mol,Reaction_energy_kcal_mol
DBT-C32,94.57,93.26
DBT-C34,85.85,80.04
DBT-C43,90.47,86.32
DBT-C45,92.66,87.85
DBT-C56,90.58,87.10
DBT-C54,93.83,89.56
DBT-C65,86.21,80.46
DBT-C67,94.58,93.47
DBT-I1,120.76,74.51
DBT-I2,109.00,90.28
DBT-I3,116.97,91.10
DBT-I4,117.12,108.98
DBT-I5,116.79,89.84
DBT-I6,111.91,107.54
DBT-BIM3,83.18,81.62
DBT-BIM4,123.02,121.65
FFEOF
