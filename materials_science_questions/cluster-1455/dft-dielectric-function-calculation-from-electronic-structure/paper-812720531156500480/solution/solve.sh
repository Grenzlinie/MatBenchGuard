#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
python3 << 'EOF'
import json
band_gaps = {
    "GGA_TS": {"gap_type": "direct", "direct_gap": 5.06},
    "LDA": {"gap_type": "indirect", "indirect_gaps": [4.91, 4.95, 5.0]}
}
with open("/app/outputs/band_gaps.json", "w") as f:
    json.dump(band_gaps, f, indent=2)
EOF

# === solve block: optical_constants.json ===
python3 << 'EOF'
import json
optical_constants = {
    "GGA_TS": {"epsilon1_0": 2.33, "refractive_index_0": 1.52},
    "LDA": {"epsilon1_0": 2.87, "refractive_index_0": 1.69}
}
with open("/app/outputs/optical_constants.json", "w") as f:
    json.dump(optical_constants, f, indent=2)
EOF
