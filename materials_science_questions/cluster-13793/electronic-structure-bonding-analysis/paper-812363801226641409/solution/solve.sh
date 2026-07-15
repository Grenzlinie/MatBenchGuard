#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: relaxed_parameters.csv ===
cat > "$OUTDIR/relaxed_parameters.csv" <<'EOF'
system,composition_x,distribution,relaxed_a_Angstrom,MPn_bond_Angstrom
TiP,3,0,3,5.69,2.33
TiP,7,4,3,5.71,2.37
TiP,7,0,7,5.82,2.38
TiP,9,2,7,5.88,2.52
TiP,11,4,7,5.91,2.56
VP,3,0,3,5.65,2.20
VP,7,4,3,5.65,2.29
VP,7,0,7,5.74,2.30
VP,9,2,7,5.80,2.42
VP,11,4,7,5.85,2.51
VAs,3,0,3,5.84,2.29
VAs,7,4,3,5.85,2.38
VAs,7,0,7,5.94,2.39
VAs,9,2,7,6.01,2.56
VAs,11,4,7,6.06,2.61
EOF
