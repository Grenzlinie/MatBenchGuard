#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: peak_positions.json ===
python3 -c "
import json, math
a0 = (1+math.sqrt(5))/2   # golden ratio
a1 = 1+math.sqrt(2)        # silver mean
q_j0 = 2*math.pi*(1 - 1/a0)
q_j1 = 2*math.pi / a1
data = {'q_j0': round(q_j0, 8), 'q_j1': round(q_j1, 8)}
with open('/app/outputs/peak_positions.json', 'w') as f:
    json.dump(data, f, indent=2)
"
