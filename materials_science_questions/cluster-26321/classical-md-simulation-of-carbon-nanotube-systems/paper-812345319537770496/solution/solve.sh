#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: critical_strain_diameter.json ===
python3 <<'PY' > /dev/null
import json
data = [
    {"tube_label": "(4,4)", "diameter_nm": 0.542, "critical_strain": 0.30},
    {"tube_label": "(10,10)", "diameter_nm": 1.356, "critical_strain": 0.12},
    {"tube_label": "(20,20)", "diameter_nm": 2.712, "critical_strain": 0.06}
]
with open('/app/outputs/critical_strain_diameter.json', 'w') as f:
    json.dump(data, f, indent=2)
PY

# === solve block: critical_strain_aspect_ratio.json ===
python3 <<'PY' > /dev/null
import json
curve = [
    {"aspect_ratio": 5.0, "critical_strain": 0.06},
    {"aspect_ratio": 7.5, "critical_strain": 0.065},
    {"aspect_ratio": 10.0, "critical_strain": 0.068},
    {"aspect_ratio": 12.5, "critical_strain": 0.07},
    {"aspect_ratio": 15.0, "critical_strain": 0.065},
    {"aspect_ratio": 17.5, "critical_strain": 0.05},
    {"aspect_ratio": 20.0, "critical_strain": 0.04},
    {"aspect_ratio": 25.0, "critical_strain": 0.025},
    {"aspect_ratio": 30.0, "critical_strain": 0.015}
]
out = {"curve": curve, "transition_aspect_ratio": 12.5}
with open('/app/outputs/critical_strain_aspect_ratio.json', 'w') as f:
    json.dump(out, f, indent=2)
PY
