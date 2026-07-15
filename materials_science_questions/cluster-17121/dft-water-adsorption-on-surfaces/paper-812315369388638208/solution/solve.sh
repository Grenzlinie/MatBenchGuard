#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: single_crystal_properties.json ===
cat > "$OUTDIR/single_crystal_properties.json" <<'EOF'
{
  "density": 0.959,
  "a": 17.38,
  "b": 11.74,
  "c": 7.81,
  "alpha": 90.0,
  "beta": 90.0,
  "gamma": 115.0
}
EOF

# === solve block: absorption_counts.csv ===
cat > "$OUTDIR/absorption_counts.csv" <<'EOF'
interface,solvent,count
(100),benzene,4
(100),chloroform,13
(010),benzene,0
(010),chloroform,0
EOF
