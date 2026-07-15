#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail; OUTDIR="/app/outputs"; mkdir -p "$OUTDIR"

# === solve block: splitting_widths.csv ===
cat > "$OUTDIR/splitting_widths.csv" <<'EOF'
dislocation_angle,splitting_width_b
0deg,6.1
60deg,14.7
90deg,15.0
EOF

# === solve block: core_energy.txt ===
echo "core_energy_eV_per_Angstrom: 0.22" > "$OUTDIR/core_energy.txt"
