#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: ground_state_results.json ===
python3 -c "import sys; sys.path.insert(0, '/solution'); import helper; helper.write_ground_state_results()"

# === solve block: residual_entropy.txt ===
python3 -c "import sys; sys.path.insert(0, '/solution'); import helper; helper.write_residual_entropy()"
