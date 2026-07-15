#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 /solution/write_outputs.py

# === solve block: gamma_B_values.csv ===
# already written by preamble
true

# === solve block: alpha_conditions.csv ===
# already written by preamble
true
