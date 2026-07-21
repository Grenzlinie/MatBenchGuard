#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: energies_and_barrier.json ===
OUTDIR=/app/outputs
python3 -c "
import json
J = -25.0
energies = [-5*abs(J)/4, -3*abs(J)/4, -abs(J)/4, abs(J)/4, 3*abs(J)/4, 5*abs(J)/4]
energies.sort()
barrier = abs(J)/2
print(json.dumps({'J': J, 'energies': energies, 'barrier': barrier}, indent=2))
" > "${OUTDIR}/energies_and_barrier.json"
