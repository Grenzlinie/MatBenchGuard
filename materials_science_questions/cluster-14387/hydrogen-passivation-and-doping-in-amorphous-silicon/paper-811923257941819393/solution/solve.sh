#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
set -euo pipefail

# === solve block: defect_densities.json ===
cat > "$OUTDIR/defect_densities.json" <<'FFEOF'
{
  "a_Se_D": 2.3e16,
  "a_Si_N_av": 3.8,
  "a_Si_D": 1.2e18
}
FFEOF
