#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: barrier_heights.csv ===
cat > "$OUTDIR/barrier_heights.csv" <<'EOF'
rotation,barrier_height
C4-C5,12.73
C3-C4,3.20
EOF

# === solve block: conformer_energies_populations.csv ===
python3 /solution/generate.py conformer_energies_populations "$OUTDIR/conformer_energies_populations.csv"

# === solve block: ensemble_enthalpy.txt ===
python3 /solution/generate.py ensemble_enthalpy "$OUTDIR/ensemble_enthalpy.txt"
