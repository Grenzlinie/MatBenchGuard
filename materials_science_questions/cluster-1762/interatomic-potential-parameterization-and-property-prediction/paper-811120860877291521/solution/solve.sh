#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: madelung_potentials.json ===
cat > "$OUTDIR/madelung_potentials.json" <<'FFEOF'
[
  {
    "compound": "Na3PO4",
    "V_M": -16.75
  },
  {
    "compound": "Ca3(PO4)2",
    "V_M": -16.10
  },
  {
    "compound": "Mn3(PO4)2",
    "V_M": -15.05
  },
  {
    "compound": "Ni3(PO4)2",
    "V_M": -15.50
  },
  {
    "compound": "InPO4",
    "V_M": -15.10
  },
  {
    "compound": "FePO4",
    "V_M": -15.10
  },
  {
    "compound": "GaPO4",
    "V_M": -14.95
  },
  {
    "compound": "BPO4",
    "V_M": -13.85
  }
]
FFEOF
