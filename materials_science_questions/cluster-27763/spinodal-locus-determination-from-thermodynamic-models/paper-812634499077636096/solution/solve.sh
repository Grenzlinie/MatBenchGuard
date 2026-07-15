#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# Run the fast helper script that writes all artifacts
python3 /solution/compute_phase_diagram.py "$OUTDIR"

# === solve block: spinodal.csv ===
#!/bin/bash
set -euo pipefail
# File already written by preamble; verify existence.
[ -f "/app/outputs/spinodal.csv" ] || exit 1

# === solve block: critical_point.json ===
#!/bin/bash
set -euo pipefail
# File already written by preamble; verify existence.
[ -f "/app/outputs/critical_point.json" ] || exit 1

# === solve block: binodal.csv ===
#!/bin/bash
set -euo pipefail
# File already written by preamble; verify existence.
[ -f "/app/outputs/binodal.csv" ] || exit 1
