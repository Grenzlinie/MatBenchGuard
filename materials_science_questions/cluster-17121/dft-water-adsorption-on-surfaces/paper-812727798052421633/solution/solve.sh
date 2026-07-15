#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR=/app/outputs

# === solve block: bilayer_thickness.json ===
mkdir -p "$OUTDIR"
cat > "$OUTDIR/bilayer_thickness.json" <<'FFEOF'
{
  "top_L": 23.5,
  "bottom_L": 22.9
}
FFEOF
