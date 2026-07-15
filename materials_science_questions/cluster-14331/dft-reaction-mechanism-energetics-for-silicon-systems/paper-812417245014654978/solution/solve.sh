#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: energies.json ===
cat > "$OUTDIR/energies.json" <<'EOF'
{
  "ICN1": -54.2,
  "ICN2": -192.9,
  "SiNC": -344.5,
  "SiCN": -376.7,
  "TS1": -38.4,
  "TS2": -29.7,
  "TS3": -116.2,
  "TS4": -255.6,
  "TS5": -30.6,
  "isomerization_barrier": 88.9,
  "INC1_stable": false,
  "TS6_found": false
}
EOF
