#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# === solve block: step_01_validation_results.csv ===
python3 "$SCRIPT_DIR/gen_val.py" > "$OUTDIR/step_01_validation_results.csv"

# === solve block: step_02_lithiation_results.csv ===
python3 "$SCRIPT_DIR/gen_lith.py" > "$OUTDIR/step_02_lithiation_results.csv"
