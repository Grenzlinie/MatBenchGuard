#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: frequencies.json ===
cat > "$OUTDIR/frequencies.json" <<'FFEOF'
{
  "si_h4": [
    {"mode": "T2", "freq": 2153},
    {"mode": "A1", "freq": 2116},
    {"mode": "E", "freq": 929},
    {"mode": "T2", "freq": 818}
  ],
  "h_bc": [
    {"mode": "stretch", "freq": 1891}
  ],
  "h2": [
    {"mode": "stretch", "freq": 3549}
  ],
  "h2_star": [
    {"mode": "H_BC", "freq": 2135},
    {"mode": "H_AB", "freq": 1750}
  ],
  "vh4": [
    {"mode": "T2", "freq": 2205}
  ],
  "o_i": [
    {"mode": "A2u", "freq": 1131}
  ]
}
FFEOF
