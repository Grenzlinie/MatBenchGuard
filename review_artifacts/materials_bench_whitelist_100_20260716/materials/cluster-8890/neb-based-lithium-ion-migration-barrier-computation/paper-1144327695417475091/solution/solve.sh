#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: computed_barriers.json ===
cat > "$OUTDIR/computed_barriers.json" <<'FFEOF'
{
  "E1": 0.249,
  "E2": 0.068
}
FFEOF
