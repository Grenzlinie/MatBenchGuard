#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p "$OUTDIR"

# === solve block: activation_barriers.json ===
cat > "$OUTDIR/activation_barriers.json" << 'FFEOF'
{
  "hydrogen_exchange": 118,
  "cracking": 292,
  "dehydrogenation": 297,
  "hydride_transfer": 202
}
FFEOF
