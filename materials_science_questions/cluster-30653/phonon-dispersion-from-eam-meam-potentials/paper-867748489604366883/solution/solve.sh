#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
cp /solution/gen_xyz.py /tmp/gen_xyz.py

# === solve block: structure_4.0.xyz ===
python3 /tmp/gen_xyz.py 4.0 > $OUTDIR/structure_4.0.xyz

# === solve block: structure_6.0.xyz ===
python3 /tmp/gen_xyz.py 6.0 > $OUTDIR/structure_6.0.xyz

# === solve block: structure_12.0.xyz ===
python3 /tmp/gen_xyz.py 12.0 > $OUTDIR/structure_12.0.xyz

# === solve block: summary.json ===
cat > $OUTDIR/summary.json <<'EOF'
{
  "4.0": {
    "radii": [0.0, 2.09],
    "KT_index": "5-1",
    "T_indices": ["(5,0)", "(1,1)"]
  },
  "6.0": {
    "radii": [1.08, 3.08],
    "KT_index": "8-3",
    "T_indices": ["(8,1)", "(3,1)"]
  },
  "12.0": {
    "radii": [0.0, 2.36, 4.40, 6.47],
    "KT_index": "16-11-6-1",
    "T_indices": ["(16,0)", "(11,0)", "(6,0)", "(1,1)"]
  }
}
EOF
