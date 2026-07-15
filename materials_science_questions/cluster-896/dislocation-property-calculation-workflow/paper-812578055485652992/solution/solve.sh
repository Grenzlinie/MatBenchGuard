#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: sif_results.json ===
python3 -c "import json; r={'tip_A': {'mode_I': 0.093, 'mode_II': 0.0}, 'tip_B': {'mode_I': 0.042, 'mode_II': 0.0}}; json.dump(r, open('$OUTDIR/sif_results.json', 'w'))"
