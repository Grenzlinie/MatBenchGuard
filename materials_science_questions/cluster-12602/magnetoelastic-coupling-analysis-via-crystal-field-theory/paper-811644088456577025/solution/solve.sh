#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: phase_diagram_results.json ===
python3 -c '
import json
result = {
    "tricritical_pressure_GPa": 1.5,
    "zero_T_AFH_AFM_transition_pressure_GPa": 0.6,
    "phase_boundary_first_order": True,
    "ambient_pressure_T_HO_K": 17.5
}
print(json.dumps(result))
' > "$OUTDIR/phase_diagram_results.json"
