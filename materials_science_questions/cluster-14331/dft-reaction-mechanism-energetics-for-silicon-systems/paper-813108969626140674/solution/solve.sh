#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: gammaH_barriers.csv ===
cat > "$OUTDIR/gammaH_barriers.csv" <<'FFEOF'
ligand,barrier_kcal_per_mol
CH2SiMe3,11.8
CH2CMe3,16.2
CH2Ph,17.3
FFEOF
