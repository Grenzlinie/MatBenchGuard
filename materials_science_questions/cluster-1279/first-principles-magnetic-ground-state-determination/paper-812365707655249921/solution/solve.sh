#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: magnetic_results.csv ===
cat > "$OUTDIR/magnetic_results.csv" <<'CSVEOF'
configuration,energy_diff_mRy,Fe_moment_muB,Mn_moment_muB
Fe↑Mn↑,0.0,2.85,3.61
Fe↑Mn↓,17,2.39,-3.69
Fe↓Mn↑,43,-2.63,3.33
Fe↓Mn↓,88,-2.51,-3.37
CSVEOF
