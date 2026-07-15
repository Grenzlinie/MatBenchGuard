#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: activation_barriers.json ===
cat > $OUTDIR/activation_barriers.json <<'FFEOF'
{
  "intrinsic_activation_free_energies": [126.7, 129.5, 137.3, 136.5]
}
FFEOF
