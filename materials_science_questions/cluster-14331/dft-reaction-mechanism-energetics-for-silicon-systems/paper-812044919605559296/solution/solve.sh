#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: relative_energies.json ===
cat > /app/outputs/relative_energies.json <<'FFEOF'
{
  "cSiNSiO_1": 0.0,
  "cSiNSiO_1_prime": 11.9,
  "SiNSiO_3": 5.1,
  "TS1_3": 12.5,
  "TS4_7": 64.2
}
FFEOF
