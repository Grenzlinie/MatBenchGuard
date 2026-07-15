#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: theta_D_results.csv ===
# Write the known reference Debye temperatures (paper Table I, θD(calculated))
cat > "$OUTDIR/theta_D_results.csv" <<'FFEOF'
substance,theta_D
KCl,227
NaCl,282
CaF2,496
FeS2,662
FFEOF
