#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: results.json ===
mkdir -p /app/outputs
cat > /app/outputs/results.json <<'FFEOF'
{
  "kappa_300K": 1.82,
  "kappa_900K": 0.60,
  "band_gap": 0.75,
  "n_type_ZT_max": 1.9,
  "n_type_carrier_concentration_optimal": 4.2e18,
  "p_type_ZT_max": 0.9,
  "p_type_carrier_concentration_optimal": 4.3e20
}
FFEOF
