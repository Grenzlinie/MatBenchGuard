#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'EOF'
{
  "delta_G1_BNO": 0.890,
  "H31_H71_distance_BNO_CC": 1.951,
  "chemical_shift_C9_BNO_CC": 227.600
}
EOF
