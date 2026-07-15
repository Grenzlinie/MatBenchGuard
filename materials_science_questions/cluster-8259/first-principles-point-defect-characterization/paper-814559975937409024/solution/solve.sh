#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: band_gaps.json ===
cat > "$OUTDIR/band_gaps.json" <<'EOF'
{
  "I": {
    "PBE-GGA": {"gap_eV": 3.34, "type": "indirect"},
    "mBJ_proxy": {"gap_eV": 3.56, "type": "indirect"}
  },
  "II": {
    "PBE-GGA": {"gap_eV": 1.10, "type": "direct"},
    "mBJ_proxy": {"gap_eV": 1.61, "type": "direct"}
  }
}
EOF

# === solve block: integrated_pdos.json ===
cat > "$OUTDIR/integrated_pdos.json" <<'EOF'
{
  "I": {
    "Pb1": 3.8,
    "Pb2": 7.8,
    "Pb3": 9.2,
    "O1": 6.0,
    "O2": 9.0,
    "O3": 12.0,
    "O4": 14.5,
    "O5": 16.0,
    "C1": 6.0,
    "B1": 1.8,
    "H1": 0.6
  },
  "II": {
    "Pb1": 1.8,
    "Pb2": 3.9,
    "Pb3": 2.3,
    "O2": 8.0,
    "O3": 13.5,
    "O4": 11.0,
    "O5": 12.5,
    "C1": 2.4,
    "B1": 1.2,
    "H1": 0.3
  }
}
EOF
