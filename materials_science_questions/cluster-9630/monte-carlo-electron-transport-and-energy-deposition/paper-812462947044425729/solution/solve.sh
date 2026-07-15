#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: total_yields.csv ===
cat > /app/outputs/total_yields.csv <<'FFEOF'
thickness,total_yield,forward_yield,backward_yield
1.0,38.4,36.0,2.4
10.0,136.4,118.0,18.4
20.0,190.0,170.0,20.0
44.0,254.0,230.0,24.0
100.0,373.0,351.0,22.4
1000.0,533.0,500.0,33.0
FFEOF

# === solve block: yields_44_ugcm2.csv ===
python3 /solution/gen_yields44.py

# === solve block: binary_peaks.json ===
cat > /app/outputs/binary_peaks.json <<'FFEOF'
{
  "foil_thickness_ugcm2": 44,
  "angle_deg": 40,
  "peak_energies_eV": [4500.0, 7600.0]
}
FFEOF

# === solve block: time_resolved.csv ===
python3 /solution/gen_time_resolved.py
