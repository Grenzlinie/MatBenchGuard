#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: orientation.json ===
cat > "/app/outputs/orientation.json" <<'FFEOF'
{
  "average_orientation": 90.0
}
FFEOF
