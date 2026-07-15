#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_01_moderate_temp_tau0.json ===
cat > "${OUTDIR}/step_01_moderate_temp_tau0.json" <<'FFEOF'
{
  "tau0_edge": 5.4,
  "tau0_screw": 3.1
}
FFEOF

# === solve block: step_02_low_temp_tau0.json ===
cat > "${OUTDIR}/step_02_low_temp_tau0.json" <<'FFEOF'
{
  "beta": 7.0,
  "tau0_screw_low": 9.5
}
FFEOF

# === solve block: step_03_hall_petch_k.json ===
cat > "${OUTDIR}/step_03_hall_petch_k.json" <<'FFEOF'
{
  "tau_c": 1449.0,
  "k": 0.33
}
FFEOF
