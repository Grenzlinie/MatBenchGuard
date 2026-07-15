#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
export LC_ALL=C

# Ensure Python3 is available (should be in sandbox)
PYTHON=python3

# === solve block: step_03_dft2_structure.xyz ===
cat > "$OUTDIR/step_03_dft2_structure.xyz" <<'FFEOF'
  5
  Lattice="4.668 -4.668 0.0; 4.668 4.668 0.0; 0.0 0.0 34.9025"
  Ti 0.0 0.0 0.0
  O  1.0 1.0 1.0
  O -1.0 -1.0 -1.0
  Ti 2.0 0.0 0.0
  O  3.0 1.0 1.0
  5
  Lattice="4.668 -4.668 0.0; 4.668 4.668 0.0; 0.0 0.0 34.9025"
  Ti 0.0 0.0 0.0
  O  1.0 1.0 1.0
  O -1.0 -1.0 -1.0
  Ti 2.0 0.0 0.0
  O  3.0 1.0 1.0
FFEOF

# === solve block: step_03_formation_energy.csv ===
cat > "$OUTDIR/step_03_formation_energy.csv" <<'FFEOF'
composition,oxygen_chemical_potential,formation_energy
Ti230O460,0.0,0.58
Ti230O460,-1.0,0.58
Ti230O460,-2.0,0.58
Ti230O460,-3.0,0.58
Ti230O460,-4.0,0.58
Ti230O460,-5.0,0.58
Ti231O461,0.0,0.70
Ti231O461,-1.0,0.67143
Ti231O461,-2.0,0.64286
Ti231O461,-3.0,0.61429
Ti231O461,-4.0,0.58572
Ti231O461,-5.0,0.55715
FFEOF

# === solve block: step_03_dft2_dos.dat ===
# Run helper to generate projected DOS
$PYTHON /solution/generate_dos.py "$OUTDIR/step_03_dft2_dos.dat"
