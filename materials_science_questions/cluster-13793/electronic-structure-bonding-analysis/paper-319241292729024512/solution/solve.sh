#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: elastic_properties.json ===
python3 << EOF
import json
data = {
    "Al": {"a0": 4.04, "B": 74.5},
    "Li": {"a0": 3.49, "B": 12.0},
    "Al3Li": {"a0": 4.033, "B": 60.8},
    "mismatch": -0.0017,
    "enthalpy_formation": -0.006,
    "Al3Li_no_d": {"a0": 4.05, "B": 65.0}
}
with open("$OUTDIR/elastic_properties.json", "w") as f:
    json.dump(data, f, indent=2)
EOF

# === solve block: charge_distribution.csv ===
cat > "$OUTDIR/charge_distribution.csv" <<'EOF'
system,sphere,s,p,d
Al3Li,Li,0.414,0.824,0.255
Al3Li,Al,1.134,1.434,0.268
Al,Al,1.128,1.454,0.418
Li,Li,0.497,0.471,0.032
EOF
