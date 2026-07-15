#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: lattice_constants.csv ===
cat > "$OUTDIR/lattice_constants.csv" <<'EOF'
x,lattice_constant
0,6.300
0.125,6.350
0.25,6.400
0.75,6.600
0.875,6.650
1,6.700
EOF

# === solve block: phonon_gamma_frequencies.csv ===
cat > "$OUTDIR/phonon_gamma_frequencies.csv" <<'EOF'
x,highest_optical_frequency
0,350.0
1,200.0
EOF

# === solve block: heat_capacity.csv ===
python3 /solution/heat_capacity.py
