#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: oer_free_energies.csv ===
cat > $OUTDIR/oer_free_energies.csv <<'FFEOF'
Step,dG_CoP,dG_complex
OH*,0.6,0.5
O*,1.6,0.01
OOH*,4.39,2.34
O2*,4.92,4.92
FFEOF

# === solve block: bader_charge.txt ===
echo '3.44' > $OUTDIR/bader_charge.txt
