#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: tip_deflections.json ===
cat > "$OUTDIR/tip_deflections.json" <<'FFEOF'
{
  "voltages_V": [50.0, 100.0, 150.0],
  "deflections_micrometer": [5.8, 11.7, 17.5]
}
FFEOF
