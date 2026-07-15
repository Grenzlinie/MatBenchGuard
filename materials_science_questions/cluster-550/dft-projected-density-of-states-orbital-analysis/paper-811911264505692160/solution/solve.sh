#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: electronic_properties.json ===
cat > "$OUTDIR/electronic_properties.json" << 'EOF'
{
  "sc": {
    "Eg": 1.21,
    "gap_type": "indirect",
    "VBM_kpoint": "M",
    "CBM_kpoint": "X",
    "Eb": -1.27
  },
  "bcc": {
    "Eg": 1.32,
    "gap_type": "direct",
    "VBM_kpoint": "H",
    "CBM_kpoint": "H",
    "Eb": -0.95
  },
  "fcc": {
    "Eg": 1.40,
    "gap_type": "indirect",
    "VBM_kpoint": "W",
    "CBM_kpoint": "Γ",
    "Eb": -0.52
  }
}
EOF
