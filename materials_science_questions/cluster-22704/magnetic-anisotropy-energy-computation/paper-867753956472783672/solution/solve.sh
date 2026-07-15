#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: mae_vs_field.csv ===
cat > /app/outputs/mae_vs_field.csv <<'EOF'
field_V_per_nm,mae_mJ_per_m2
-0.26,3.7343
-0.21,3.73215
-0.16,3.73
-0.1,3.7386
0.0,3.753
0.21,3.78324
0.42,3.81348
EOF

# === solve block: noe_fe3_vs_field.csv ===
cat > /app/outputs/noe_fe3_vs_field.csv <<'EOF'
field_V_per_nm,noe_fe3
-0.26,7.81
-0.21,7.82
-0.16,7.83
-0.1,7.82
0.0,7.8
0.21,7.79
0.42,7.78
EOF
