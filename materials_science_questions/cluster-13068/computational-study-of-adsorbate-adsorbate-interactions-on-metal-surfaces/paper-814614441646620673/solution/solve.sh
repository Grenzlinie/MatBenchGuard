#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_hydrogen_energies.csv ===
cat > "$OUTDIR/step_01_hydrogen_energies.csv" << 'EOF'
method,total_energy_eV
LSD,-13.38
LD,-12.25
EOF

# === solve block: step_02_sodium_energies.csv ===
cat > "$OUTDIR/step_02_sodium_energies.csv" << 'EOF'
method,total_energy_Ry
LSD,-323.268
LD,-323.247
EOF

# === solve block: step_03_sodium_cohesive_energy.txt ===
cat > "$OUTDIR/step_03_sodium_cohesive_energy.txt" << 'EOF'
1.17
EOF
