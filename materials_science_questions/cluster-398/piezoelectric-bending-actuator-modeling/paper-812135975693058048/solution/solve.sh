#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: step_01_efficiency.json ===
python3 - << 'EOF'
import json
out = {"G_zero": 0.05, "G_supersonic": 1.5}
with open("/app/outputs/step_01_efficiency.json", "w") as f:
    json.dump(out, f)
EOF
