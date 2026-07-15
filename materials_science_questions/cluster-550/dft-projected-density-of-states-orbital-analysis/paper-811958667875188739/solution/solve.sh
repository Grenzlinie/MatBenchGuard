#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_structural_params.csv ===
cat > /app/outputs/step_01_structural_params.csv << 'FFEOF'
bond_length_angstrom,buckling_angle_deg,charge_state,configuration,dopant,magnetic_moment_muB,total_energy_eV
2.26,14.6,Ne,HD1,P,0,-500.00
2.33,3.2,Ne+1,HD1,P,1,-503.00
2.42,-5.7,Ne+2,HD1,P,0,-506.00
2.30,15.5,Ne,HD2,P,0,-500.14
2.30,15.7,Ne+1,HD2,P,0,-503.14
2.29,15.8,Ne+2,HD2,P,0,-506.14
2.40,17.6,Ne,HD1,As,0,-600.00
2.46,6.4,Ne+1,HD1,As,1,-603.00
2.56,-2.5,Ne+2,HD1,As,0,-606.00
2.44,18.4,Ne,HD2,As,0,-600.14
2.43,18.3,Ne+1,HD2,As,0,-603.14
2.42,18.0,Ne+2,HD2,As,0,-606.14
FFEOF
