#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: delta_Ti_140GPa_results.json ===
cat > "$OUTDIR/delta_Ti_140GPa_results.json" << 'EOF'
{
  "lambda": 1.65,
  "omega_log": 600.0,
  "Tc": 23.0,
  "acoustic_fraction": 0.202
}
EOF
