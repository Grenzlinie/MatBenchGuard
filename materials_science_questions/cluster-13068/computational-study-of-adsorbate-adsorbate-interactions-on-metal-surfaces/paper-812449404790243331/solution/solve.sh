#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_field_enhancement_factors.csv ===
cat > '/app/outputs/step_01_field_enhancement_factors.csv' <<'BFEOF'
b_E_value,lattice_type,beta_A
2.00,hexagonal,1.085000
7.00,hexagonal,1.155000
BFEOF

# === solve block: step_02_binding_energies.csv ===
cat > '/app/outputs/step_02_binding_energies.csv' <<'BEEOF'
b_E_value,lattice_type,Delta_B_conv,Delta_B_diff
2.00,hexagonal,0.039735,0.024470
7.00,hexagonal,0.074902,0.043949
BEEOF
