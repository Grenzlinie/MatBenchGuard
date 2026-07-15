#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: cubic_results.json ===
cat > "$OUTDIR/cubic_results.json" <<'FFEOF'
{
  "sc": {
    "Eb": -1.27,
    "Eg": 1.21,
    "gap_type": "indirect",
    "vbm_kpoint": "M",
    "cbm_kpoint": "X"
  },
  "bcc": {
    "Eb": -0.95,
    "Eg": 1.32,
    "gap_type": "direct",
    "vbm_kpoint": "H",
    "cbm_kpoint": "H"
  },
  "fcc": {
    "Eb": -0.52,
    "Eg": 1.40,
    "gap_type": "indirect",
    "vbm_kpoint": "W",
    "cbm_kpoint": "Γ"
  }
}
FFEOF
