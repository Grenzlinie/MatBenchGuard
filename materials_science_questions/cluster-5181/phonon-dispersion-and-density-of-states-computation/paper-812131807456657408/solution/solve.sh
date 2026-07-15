#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: ziman_results.json ===
cat > "$OUTDIR/ziman_results.json" <<'EOF'
{
  "resistivities": {"164.5": 35.0, "155": 38.6, "147": 42.1, "140": 46.0},
  "thermopowers": {"164.5": 1.73, "155": 2.38, "147": 2.71, "140": 2.88},
  "g2_ambient": 0.35714285714285715,
  "dln_g2_dln_a": -30.0
}
EOF
