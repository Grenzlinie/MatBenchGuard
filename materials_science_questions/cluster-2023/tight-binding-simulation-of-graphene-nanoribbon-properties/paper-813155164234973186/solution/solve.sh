#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: cooling_power.json ===
cat > "$OUTDIR/cooling_power.json" <<'EOF'
{
  "theta_x_pi_over_2": 0.3,
  "theta_x_2pi_over_3": 0.5
}
EOF
