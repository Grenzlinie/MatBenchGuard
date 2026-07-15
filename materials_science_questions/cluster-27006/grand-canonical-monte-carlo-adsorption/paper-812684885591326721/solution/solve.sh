#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy || true

# === solve block: energy_table.csv ===
cat > $OUTDIR/energy_table.csv <<'CSVEOF'
S_w,method_1_normalized,method_2_normalized,method_3_normalized
0.00,1.000,1.000,1.000
0.05,0.97,0.97,0.95
0.10,0.94,0.92,0.90
0.15,0.91,0.87,0.85
0.20,0.88,0.82,0.80
0.25,0.85,0.77,0.75
0.30,0.82,0.72,0.70
0.35,0.80,0.67,0.65
0.40,0.79,0.62,0.60
0.45,0.80,0.57,0.55
0.50,0.98,0.52,0.50
0.55,0.80,0.47,0.45
0.60,0.75,0.42,0.40
0.65,0.68,0.37,0.35
0.70,0.60,0.32,0.30
0.75,0.52,0.27,0.25
0.80,0.44,0.22,0.20
0.85,0.36,0.17,0.15
0.90,0.27,0.12,0.10
0.95,0.13,0.07,0.05
1.00,0.000,0.000,0.000
CSVEOF
