#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: second_order_NAC_H3.json ===
cat > /app/outputs/second_order_NAC_H3.json <<'EOF'
{
  "atoms": [
    {"atom": 1, "x": 1085.88, "y": -1074.36, "z": 12.75},
    {"atom": 2, "x": 0.30,   "y": 0.00,    "z": 0.00},
    {"atom": 3, "x": -1085.30, "y": 1073.36, "z": -12.68}
  ]
}
EOF
