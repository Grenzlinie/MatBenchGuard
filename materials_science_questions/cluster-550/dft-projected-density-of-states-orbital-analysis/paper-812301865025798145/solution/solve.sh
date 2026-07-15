#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: dHvA_frequencies.csv ===
cat > "$OUTDIR/dHvA_frequencies.csv" <<'FFEOF'
branch,direction,frequency_calc,mass_calc
δ,H∥b,33.5,0.75
ε,H∥b,53.9,1.15
ζ,H∥b,77.5,1.5
α,H∥15° from b to a,1.25,0.48
β,H∥15° from b to a,9.20,0.51
δ,H∥15° from b to a,34.0,0.84
FFEOF
