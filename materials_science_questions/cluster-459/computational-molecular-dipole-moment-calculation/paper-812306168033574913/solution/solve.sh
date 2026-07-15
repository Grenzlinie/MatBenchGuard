#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: dipole_moments.json ===
python3 -c "
import json
data = {
    'mu_Si_O': 1.12,
    'mu_Si_O_Si_0': 0.17,
    'mu_critical': 0.318
}
with open('$OUTDIR/dipole_moments.json', 'w') as f:
    json.dump(data, f)
"
