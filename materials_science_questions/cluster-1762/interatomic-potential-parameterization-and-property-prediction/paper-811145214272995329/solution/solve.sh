#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
# ensure /solution/generate.py exists (provided as extra file)
if [ ! -f /solution/generate.py ]; then
  echo "ERROR: generate.py not found at /solution/generate.py" >&2
  exit 1
fi

# === solve block: ground_state_energies.csv ===
python3 /solution/generate.py csv > "$OUTDIR/ground_state_energies.csv"

# === solve block: geometric_magic_numbers.json ===
python3 /solution/generate.py magic > "$OUTDIR/geometric_magic_numbers.json"

# === solve finalize ===
# No further steps needed
