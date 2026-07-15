#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: concentration_gradients.csv ===
python3 /solution/compute_gradients.py

# === solve block: capacity_fade.csv ===
cat > /app/outputs/capacity_fade.csv << 'FFEOF'
cycle_number,C_rate,discharge_capacity_Ah
1,2,2.60
2,2,2.55
3,2,2.50
4,2,2.47
5,2,2.44
1,4,2.10
2,4,2.05
3,4,2.00
4,4,1.97
5,4,1.95
FFEOF
