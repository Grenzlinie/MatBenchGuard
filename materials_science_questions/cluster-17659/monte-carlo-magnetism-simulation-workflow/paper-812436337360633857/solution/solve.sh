#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_betas.json ===
cat > "$OUTDIR/critical_betas.json" <<'FFEOF'
{
  "N3": {"beta_c": 6.40, "uncertainty": 0.10},
  "N4": {"beta_c": 12.00, "uncertainty": 0.35},
  "N5": {"beta_c": 19.5, "uncertainty": 1.1},
  "N6": {"beta_c": 32.0, "uncertainty": 1.0}
}
FFEOF
