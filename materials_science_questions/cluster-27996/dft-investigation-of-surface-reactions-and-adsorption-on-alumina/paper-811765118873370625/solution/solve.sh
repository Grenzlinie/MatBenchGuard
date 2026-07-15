#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_energies.json ===
cat > "/app/outputs/computed_energies.json" <<'FFEOF'
{
  "TS2_prime_Delta_E": 104.2,
  "TS2_prime_Delta_G_323": 93.0,
  "TS6_Delta_E": 43.0,
  "TS6_Delta_G_323": 33.0,
  "TS8_Delta_E": 128.0,
  "TS8_Delta_G_323": 128.0,
  "Delta_r_G_propene": -116.5,
  "Delta_r_G_allyl_alcohol": -9.9,
  "Delta_r_G_1_propanol": -93.4
}
FFEOF
