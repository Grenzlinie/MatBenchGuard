#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > "/app/outputs/dft_results.json" <<'FFEOF'
{
  "delta_U_mV": 17.2,
  "Q_left_e": 0.134,
  "Q_right_e": -0.005
}
FFEOF
