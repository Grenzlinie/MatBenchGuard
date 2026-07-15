#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gap.json ===
cat > "$OUTDIR/band_gap.json" <<'EOF'
{
  "band_gap_without_soc": 0.37,
  "band_gap_with_soc": 0.04
}
EOF

# === solve block: effective_masses.csv ===
cat > "$OUTDIR/effective_masses.csv" <<'EOF'
direction,effective_mass,angle
X (needle),0.02,12.37
Y (Bi-Bi bonds),1.16,0.97
Z (Cs layers),0.09,12.35
EOF
