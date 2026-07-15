#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: iam_breakdown.csv ===
cat > "$OUTDIR/iam_breakdown.csv" <<'EOF'
cluster,OO,OC,CC_rep,CC_attr,MO
Mn2(CO)10,-1.64,-5.08,4.37,-0.66,-1.49
Fe3(CO)12,-2.23,-5.26,7.52,-1.18,-2.75
EOF

# === solve block: iem_total.csv ===
cat > /app/outputs/iem_total.csv <<'EOF'
IEM_total
-29.2
EOF
