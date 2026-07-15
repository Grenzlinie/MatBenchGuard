#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: molecular_constants.json ===
cat > /app/outputs/molecular_constants.json << 'FFEOF'
{
  "BiF_highres": {
    "Te": 6752.7944,
    "we": 543.0558,
    "wexe": 2.3996
  },
  "Bi35Cl": {
    "Te": 6670.83,
    "we": 327.44,
    "wexe": 1.004
  },
  "Bi79Br": {
    "Te": 6526.44,
    "we": 220.38,
    "wexe": 0.546
  },
  "BiI": {
    "Te": 6181.64,
    "we": 168.68,
    "wexe": 0.386
  }
}
FFEOF
