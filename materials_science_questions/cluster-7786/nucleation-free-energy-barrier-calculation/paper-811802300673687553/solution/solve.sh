#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: step_03_kauzmann_temperature.json ===
python3 <<EOF
import os, json
os.makedirs('$OUTDIR', exist_ok=True)
with open('$OUTDIR/step_03_kauzmann_temperature.json', 'w') as f:
    json.dump({"TK": 3.18, "units": "temperature"}, f)
EOF

# === solve block: step_05_nucleation_time.json ===
python3 /solution/helper.py step_05_nucleation_time.json

# === solve block: step_06_crossing_demonstration.json ===
python3 /solution/helper.py step_06_crossing_demonstration.json
