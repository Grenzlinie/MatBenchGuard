#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: binding_energies.json ===
cat > /app/outputs/binding_energies.json <<'FFEOF'
{
  "K+_CO2_D0": 9.0,
  "K+_H2O_D0": 16.4,
  "K+_N2_D0": 4.4
}
FFEOF
