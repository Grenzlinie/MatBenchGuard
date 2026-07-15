#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
python3 -c "
import json
data = {
    'KOH': {
        'T_tr': 226.7,
        'ΔH_tr': 222,
        'ΔS_tr': 0.121
    },
    'KOD': {
        'T_tr': 253.1,
        'ΔH_tr': 257,
        'ΔS_tr': 0.1258
    }
}
with open('/app/outputs/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
