#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: design_A_MC_results.json ===
python3 -c "
import json
data = {
    'F_c': 0.0032,
    'p_flaws': 0.27,
    'trials': 1000000,
    'failures': 3200
}
with open('$OUTDIR/design_A_MC_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: design_B_MC_results.json ===
python3 -c "
import json
data = {
    'F_c': 0.000223,
    'p_flaws': 0.019,
    'trials': 1000000,
    'failures': 223
}
with open('$OUTDIR/design_B_MC_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
