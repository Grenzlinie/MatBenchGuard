#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: reduced_fermi_energies.json ===
python3 -c "
import json
data = {'y_0.85': -1.6, 'y_0.8': -2.25, 'y_0.6': -3.7}
with open('$OUTDIR/reduced_fermi_energies.json', 'w') as f:
    json.dump(data, f, indent=4)
"
