#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: correlation_results.json ===
python3 -c "
import json, math
x3 = 1.0 / 8.0
corr_3 = 0.25 * (math.tanh(x3) ** 2)
sus = 0.25 * math.cosh(2 * x3)
data = {'corr_1': 0.0, 'corr_2': 0.0, 'corr_3': corr_3, 'susceptibility': sus}
with open('$OUTDIR/correlation_results.json', 'w') as f:
    json.dump(data, f)
"
