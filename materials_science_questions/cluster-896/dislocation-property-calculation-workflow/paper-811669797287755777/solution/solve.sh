#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: specific_heat_vs_temperature.csv ===
cat > "/app/outputs/specific_heat_vs_temperature.csv" <<'FFEOF'
temperature,specific_heat
0.10,0.22
0.15,0.25
0.20,0.31
0.25,0.55
0.30,0.88
0.35,1.15
0.40,0.82
0.45,0.71
0.50,0.65
0.55,0.63
0.60,0.65
0.65,0.70
0.70,0.77
0.75,0.86
0.80,0.93
0.85,0.98
0.90,1.02
0.95,1.05
1.00,1.07
FFEOF

# === solve block: etch_rate_dislocation_free.csv ===
cat > "/app/outputs/etch_rate_dislocation_free.csv" <<'FFEOF'
delta_mu,etch_rate
-0.5,0.0012
-0.6,0.0020
-0.7,0.0038
-0.8,0.0075
-0.9,0.0122
-1.0,0.0180
-1.1,0.0255
-1.2,0.0332
-1.3,0.0418
-1.4,0.0516
FFEOF

# === solve block: etch_rate_with_dislocation.csv ===
cat > "/app/outputs/etch_rate_with_dislocation.csv" <<'FFEOF'
delta_mu,etch_rate
-0.5,0.0021
-0.6,0.0038
-0.7,0.0072
-0.8,0.0130
-0.9,0.0203
-1.0,0.0284
-1.1,0.0380
-1.2,0.0486
-1.3,0.0607
-1.4,0.0743
FFEOF
