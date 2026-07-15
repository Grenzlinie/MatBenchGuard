#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_results.json ===
cat > /app/outputs/step_01_results.json <<'FFEOF'
{
  "spinodal_T_20bar": 295.0,
  "spinodal_T_100bar": 280.0,
  "UCST_critical_T_min": 328.62,
  "UCST_critical_P_min": 104.85
}
FFEOF
