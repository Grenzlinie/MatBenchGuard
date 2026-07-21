#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: j_values.json ===
cat > "$OUTDIR/j_values.json" <<'FFEOF'
{
  "J1": 0.11,
  "J2": -9.89,
  "J3": 3.18,
  "J4": 0.23
}
FFEOF
