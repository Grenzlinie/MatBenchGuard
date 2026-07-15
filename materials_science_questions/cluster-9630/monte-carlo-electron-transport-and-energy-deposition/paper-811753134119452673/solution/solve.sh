#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: depth_dose_profiles.csv ===
python3 -c "import sys; sys.path.insert(0,'/'); from solution.gen_utils import write_depth_dose; write_depth_dose()"

# === solve block: transmission_fractions.json ===
python3 -c "import sys; sys.path.insert(0,'/'); from solution.gen_utils import write_transmission; write_transmission()"
