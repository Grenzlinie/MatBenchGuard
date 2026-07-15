#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: step_06_results.json ===
python3 -c "
import json
data = {
  'pristine_strength_nanoindentation_GPa': 105.0,
  'pristine_strength_tension_GPa': 120.0,
  'gb_strength_nanoindentation_GPa': 90.0,
  'gb_strength_tension_GPa': 70.0,
  'gb_nucleation_deflection_nm': 3.54,
  'gb_failure_deflection_nm': 4.6
}
with open('$OUTDIR/step_06_results.json', 'w') as f:
    json.dump(data, f, indent=2)
"
