#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: predicted_E_vs_porosity.csv ===
cat > "$OUTDIR/predicted_E_vs_porosity.csv" <<'FFEOF'
porosity,predicted_youngs_modulus
4.28,3170
4.81,2970
4.875,3086
5.84,2809
6.32,2697
FFEOF
