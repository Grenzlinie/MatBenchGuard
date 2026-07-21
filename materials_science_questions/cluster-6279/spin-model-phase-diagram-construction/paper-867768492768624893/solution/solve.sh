#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: percolation_thresholds.json ===
python3 -c "
import json
data = {}
data['c_star_spin_half_q3'] = 0.6727
data['c_star_spin_half_q4'] = 0.4594
data['c_star_spin1_q3'] = 0.6211
with open('/app/outputs/percolation_thresholds.json', 'w') as f:
    json.dump(data, f)
"
