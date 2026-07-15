#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
python3 <<'PYEOF'
import json
data = {
    "anhydrous_band_gap": 3.72,
    "free_proton_band_gaps": {
        "[100]": 0.942,
        "[010]": 1.007,
        "[001]": 0.693
    }
}
with open("/app/outputs/band_gaps.json", "w") as f:
    json.dump(data, f)
PYEOF
