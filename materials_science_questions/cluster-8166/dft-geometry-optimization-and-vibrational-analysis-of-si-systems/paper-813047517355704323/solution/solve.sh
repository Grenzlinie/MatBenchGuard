#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: frequencies.json ===
cat > "$OUTDIR/frequencies.json" <<'FFEOF'
{
  "hexagonal_out_of_plane_cm-1": 143.0,
  "pentamer_pair_out_of_plane_cm-1": 207.0
}
FFEOF
