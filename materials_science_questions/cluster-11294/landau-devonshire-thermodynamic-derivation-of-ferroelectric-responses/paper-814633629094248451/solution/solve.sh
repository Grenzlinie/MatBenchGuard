#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: predictions.csv ===
# Write the predicted strain and lattice parameter for the three compositions.
cat > /app/outputs/predictions.csv <<'EOF'
x,predicted_strain_percent,predicted_lattice_parameter_nm
0.25,1.18,0.4012
0.50,1.18,0.4012
0.75,-0.68,0.3938
EOF
