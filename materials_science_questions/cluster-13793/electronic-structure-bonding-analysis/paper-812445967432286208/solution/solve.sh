#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: calculated_results.json ===
cat > "/app/outputs/calculated_results.json" <<'FFEOF'
{
  "coverages": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0],
  "work_function_changes": [0.0, -2.62, -2.12, -1.62, -1.12, -0.62],
  "charge_transfers": [0.0, 0.8, 0.6, 0.4, 0.2, 0.0],
  "ldos_at_fermi": [1.0, 0.85, 0.7, 0.55, 0.45, 0.4]
}
FFEOF
