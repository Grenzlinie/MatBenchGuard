#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: magnetic_moment.json ===
cat > /app/outputs/magnetic_moment.json <<'FFEOF'
{
  "mu_B_per_cell": 1.0
}
FFEOF

# === solve block: exchange_integrals.json ===
cat > /app/outputs/exchange_integrals.json <<'FFEOF'
{
  "J_01_D_meV": 21.9,
  "J_02_D_meV": 1.9
}
FFEOF
