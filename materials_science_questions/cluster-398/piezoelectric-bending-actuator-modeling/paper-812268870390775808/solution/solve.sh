#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_theoretical_estimates.json ===
python3 -c "import json; data = {'sigma_max': 6.6e-5, 'Q\u207b\u00b9_max': 0.015, 'dispersion_rate': 1.5}; json.dump(data, open('${OUTDIR}/step_01_theoretical_estimates.json', 'w'))"
