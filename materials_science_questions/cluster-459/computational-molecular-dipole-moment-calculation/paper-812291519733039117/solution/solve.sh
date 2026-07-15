#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_electrostatic_results.csv ===
cat > /app/outputs/step_01_electrostatic_results.csv <<'EOF'
molecule,R_ion_N,E_dip,E_ind,E_dis,E_rep,E_t
H2O,2.59,-17.79,-3.36,-1.72,5.95,-16.92
NH3,2.58,-17.48,-6.05,-2.97,8.97,-17.53
CH3NH2,2.52,-16.06,-8.16,-5.23,11.19,-18.26
(CH3)2NH,2.46,-15.96,-10.51,-7.56,13.91,-20.12
(CH3)3N,2.43,-16.08,-12.62,-8.90,15.71,-21.89
EOF
