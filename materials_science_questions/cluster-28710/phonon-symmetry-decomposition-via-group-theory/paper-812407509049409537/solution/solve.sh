#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: phonon_mode_counts.json ===
python3 <<'PYEOF'
import json

data = {
    "undistorted": {
        "Raman": {"Ag": 4, "B1g": 4, "B2g": 3, "B3g": 1},
        "IR": {"B1u": 3, "B2u": 5, "B3u": 5},
        "Raman_total": 12,
        "IR_total": 13
    },
    "distorted": {
        "Raman": {"Ag": 8, "B1g": 9, "B2g": 7, "B3g": 6},
        "IR": {"B1u": 5, "B2u": 9, "B3u": 8},
        "Raman_total": 30,
        "IR_total": 22
    }
}

with open("/app/outputs/phonon_mode_counts.json", "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")
PYEOF
