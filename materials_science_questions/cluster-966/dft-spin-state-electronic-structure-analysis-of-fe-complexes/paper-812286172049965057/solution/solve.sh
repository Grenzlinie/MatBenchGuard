#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: polarization_results.json ===
python3 -c "
import json
result = {'Na_D2_polarization': 1/3, 'Hg_resonance_polarization': 1.0}
with open('/app/outputs/polarization_results.json', 'w') as f:
    json.dump(result, f, indent=2)
"
