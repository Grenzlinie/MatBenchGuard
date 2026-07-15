#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > "/app/outputs/results.json" <<'FFEOF'
{
  "critical_radius_Rc": 55.0,
  "Tm_cl_3000": 101.0,
  "Tm_cl_6000": 113.0,
  "Ts": 129.0,
  "inequality_holds": true
}
FFEOF
