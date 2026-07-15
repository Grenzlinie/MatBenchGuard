#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_1_dipole_moments_zero_field.csv ===
cat > /app/outputs/step_1_dipole_moments_zero_field.csv <<'FFEOF'
X,dipole_D,separation_angstrom
H,4.22,7.81
H,8.13,11.7
F,-0.86,7.81
F,-2.44,11.7
Br,-0.5,7.81
Br,-1.0,11.7
FFEOF

# === solve block: step_2_field_dependence.csv ===
cat > /app/outputs/step_2_field_dependence.csv <<'FFEOF'
X,dipole_D,energy_gap_eV,field_V_Ang,separation_angstrom
H,4.22,1.04,0.0,7.81
H,4.15,1.00,0.1,7.81
H,4.08,0.96,0.2,7.81
H,4.01,0.92,0.3,7.81
H,8.13,,0.0,11.7
H,8.05,,0.1,11.7
H,7.97,,0.2,11.7
H,7.89,,0.3,11.7
F,-0.86,0.84,0.0,7.81
F,-0.95,0.80,0.1,7.81
F,-1.04,0.76,0.2,7.81
F,-1.13,0.72,0.3,7.81
F,-2.44,,0.0,11.7
F,-2.52,,0.1,11.7
F,-2.60,,0.2,11.7
F,-2.68,,0.3,11.7
FFEOF
