#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: magnetic_moments.json ===
python3 -c "import json; data = {'Co3C_ambient': 1.14, 'Co2C_ambient': 0.00126, 'Co3C_pressurized': 1.02}; json.dump(data, open('$OUTDIR/magnetic_moments.json', 'w'))"
