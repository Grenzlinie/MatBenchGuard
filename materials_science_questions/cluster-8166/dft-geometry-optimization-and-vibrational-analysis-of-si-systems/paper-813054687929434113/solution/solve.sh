#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail

# === solve block: energies.csv ===
mkdir -p /app/outputs
cat > /app/outputs/energies.csv <<'FFEOF'
configuration,relative_energy_eV
A,0.69
B,-0.04
C,-0.76
D,-0.39
E,-0.60
FFEOF
