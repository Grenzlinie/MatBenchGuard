#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_03_ts_geometry.csv ===
cat > /app/outputs/step_03_ts_geometry.csv <<'FFEOF'
bond,length_angstrom
Si-H,1.543
Re-O6,1.740
Re-O7,1.663
Re-O8,1.661
Re-O9,2.144
O6-O9,1.817
Si-O9,2.732
O9-H,1.532
FFEOF

# === solve block: step_05_activation_energy.txt ===
cat > /app/outputs/step_05_activation_energy.txt <<'FFEOF'
28.5
FFEOF

# === solve block: step_06_mulliken_charges.csv ===
cat > /app/outputs/step_06_mulliken_charges.csv <<'FFEOF'
atom_label,charge
Re,1.511
Si,0.078
O6,-0.597
O7,-0.632
O8,-0.622
O9,-0.317
H11,-0.021
FFEOF
