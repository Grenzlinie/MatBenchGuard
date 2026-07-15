#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: debye_temperature.json ===
python3 -c "import json; json.dump({'theta_infinity_K': 402.0}, open('/app/outputs/debye_temperature.json', 'w'))"
