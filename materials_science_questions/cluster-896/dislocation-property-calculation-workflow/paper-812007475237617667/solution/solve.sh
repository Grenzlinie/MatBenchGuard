#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: core_energies.json ===
cat > /app/outputs/core_energies.json << 'EOF'
{
  "core_energies": {
    "four_atom": 0.92,
    "five_seven_atom": 1.02,
    "eight_atom": 1.18
  },
  "most_stable_core": "four"
}
EOF
