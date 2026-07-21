#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: divacancy_contributions.json ===
mkdir -p /app/outputs
python3 -c "
import json
high = 260*0.1/(100+260*0.1)*100
low = 4*0.1/(1+4*0.1)*100
d = {'high_temperature_percent': high, 'low_temperature_percent': low}
print(json.dumps(d, indent=2))
" > /app/outputs/divacancy_contributions.json
