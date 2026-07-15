#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: relative_enthalpies.json ===
cat > "$OUTDIR/relative_enthalpies.json" <<'EOF'
{
  "SiH2+HCl": 0.0,
  "ylid_anti": -22.5,
  "ylid_syn": -22.6,
  "TS1": -2.9,
  "TS2": -2.0,
  "SiH3Cl": -308.5,
  "TS3": -31.3,
  "SiHCl+H2": -119.5,
  "SiH2Cl_radical+H": 75.7
}
EOF
