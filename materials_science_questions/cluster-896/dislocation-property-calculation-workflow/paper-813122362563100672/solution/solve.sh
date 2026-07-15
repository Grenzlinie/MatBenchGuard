#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy
cp /solution/generate_outputs.py /app/

# === solve block: equilibrium_n.csv ===
#!/bin/bash
set -euo pipefail
cd /app/outputs
python3 /app/generate_outputs.py equilibrium_n

# === solve block: stress_profiles.csv ===
#!/bin/bash
set -euo pipefail
cd /app/outputs
python3 /app/generate_outputs.py stress_profiles

# === solve block: resistance_curve.csv ===
#!/bin/bash
set -euo pipefail
cd /app/outputs
python3 /app/generate_outputs.py resistance_curve
