#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_energies.csv ===
# Write reference singlet and triplet energies for both models
cat > "$OUTDIR/step_01_energies.csv" <<'CSVEOF'
model,E_singlet,E_triplet
t-J-K,0.15,-0.15
t-J2-J3-J4,-0.15,0.15
CSVEOF
