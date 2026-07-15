#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"

# === solve block: results.json ===
cat > "$OUTDIR/results.json" <<'FFEOF'
{
  "R_md": 3.8e-07,
  "Delta_log_t": -2.64
}
FFEOF
