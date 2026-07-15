#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_first_principles_results.csv ===
cat > "$OUTDIR/step_01_first_principles_results.csv" <<'CSVEOF'
strain_percent,lattice_constant_angstrom,elastic_modulus_GPa,thermal_conductivity_W_mK
0,5.4021,147,141
2,5.5101,136,138
4,5.6182,115,117
6,5.7262,94,91
8,5.8343,76,61
10,5.9423,55,47
CSVEOF

# === solve block: step_02_kappa_results.csv ===
python3 /solution/solve_helper.py > "$OUTDIR/step_02_kappa_results.csv"
