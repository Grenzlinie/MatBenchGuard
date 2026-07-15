#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: optimized_structure.csv ===
cat > $OUTDIR/optimized_structure.csv <<'EOF'
lattice_parameter_a_angstrom,element,x_frac,y_frac,z_frac
3.9885,lattice,0.0,0.0,0.0
3.9885,O,0.0,0.5,0.25
3.9885,O,0.0,0.5,0.752189
3.9885,O,0.5,0.0,0.25
3.9885,O,0.5,0.0,0.748394
3.9885,O,0.5,0.5,0.0
3.9885,O,0.5,0.5,0.5
3.9885,Fe,0.5,0.5,0.745723
3.9885,Nb,0.5,0.5,0.246352
3.9885,Pb,0.0,0.0,-0.039843
3.9885,Pb,0.0,0.0,0.531113
EOF

# === solve block: polarization_values.csv ===
cat > /app/outputs/polarization_values.csv <<'EOF'
subcell,polarization_muC_per_cm2
PbFeO3,18.0
PbNbO3,58.0
EOF
