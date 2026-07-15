#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: step_01_variant_report.json ===
python3 - <<'PYEOF'
import json
report = {
    "variants_on_free_surface": ["ABC", "AB\\bar{C}", "BAC", "BA\\bar{C}"],
    "junction_planes": [
        {"variant_pair": ["ABC", "BAC"], "plane_indices": [1, 0, 0]},
        {"variant_pair": ["ABC", "AB\\bar{C}"], "plane_indices": [0, 1, 0]},
        {"variant_pair": ["BAC", "BA\\bar{C}"], "plane_indices": [1, 1, 0]},
        {"variant_pair": ["AB\\bar{C}", "BA\\bar{C}"], "plane_indices": [1, -1, 0]}
    ]
}
with open("/app/outputs/step_01_variant_report.json", "w") as f:
    json.dump(report, f, indent=2)
PYEOF
