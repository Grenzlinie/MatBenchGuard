#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 /solution/write_outputs.py

# === solve block: optimized_structure.cif ===
# file already created by preamble; verify existence
test -f "$OUTDIR/optimized_structure.cif"

# === solve block: calculated_properties.json ===
# file already created by preamble; verify existence
test -f "$OUTDIR/calculated_properties.json"
