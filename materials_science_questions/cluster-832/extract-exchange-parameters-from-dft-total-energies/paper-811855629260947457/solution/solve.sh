#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: exchange_ratio.json ===
cat > "$OUTDIR/exchange_ratio.json" <<'FFEOF'
{
  "eta": 0.00008,
  "J_prime": 0.0005
}
FFEOF
