#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
python3 -c "
import json
data = {'BST': 3.02, 'SST': 3.38, 'CST': 3.45}
with open('/app/outputs/band_gaps.json', 'w') as f:
    json.dump(data, f, indent=2)
"

# === solve block: dos_analysis.txt ===
cat > /app/outputs/dos_analysis.txt <<'EOF'
Orbital character analysis for double perovskites A2SmTaO6 (A = Ba, Sr, Ca):

BST: Valence band maximum is dominated by O 2p hybridized with Sm 4f and Ta 5d. Conduction band minimum is dominated by Ta 5d.
SST: VBM is O 2p + Sm 4f + Ta 5d; CBM is Ta 5d.
CST: VBM is O 2p + Sm 4f + Ta 5d; CBM is Ta 5d.
EOF
