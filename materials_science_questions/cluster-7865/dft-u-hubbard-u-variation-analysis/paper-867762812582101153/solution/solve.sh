#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: dos_peak_positions.json ===
cat > "$OUTDIR/dos_peak_positions.json" <<'FFEOF'
{
  "bulk": -2.5,
  "film_1layer": -0.8,
  "film_5layer": -1.5
}
FFEOF
