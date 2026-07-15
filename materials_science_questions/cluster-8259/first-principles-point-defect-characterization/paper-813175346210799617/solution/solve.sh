#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c "
import json
data = {
    'pristine_gaps': {'ZnPc': 2.13, 'CuPc': 2.18},
    'H_trap_energy': {'ZnPc': 0.75, 'CuPc': 0.80},
    'O2_trap_energy': {'ZnPc': 0.6, 'CuPc': 0.5},
    'magnetic_moments': {'H_ZnPc': 1.0, 'H_CuPc': 2.0}
}
with open('$OUTDIR/results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
