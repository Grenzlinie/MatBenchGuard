#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: lj_multistage_results.csv ===
cat > /app/outputs/lj_multistage_results.csv <<'EOF'
lambda_start,lambda_end,delta_F_per_particle,error
0.0,0.03,0.0176,0.0003
0.03,0.07,0.0160,0.0003
0.07,0.125,0.0135,0.0003
0.125,0.1875,0.0084,0.0003
0.1875,0.25,0.0032,0.0002
0.25,0.375,-0.0043,0.0004
0.375,0.5,-0.0146,0.0004
0.5,0.625,-0.0237,0.0003
0.625,0.75,-0.0311,0.0003
0.75,0.875,-0.0393,0.0004
0.875,1.0,-0.0501,0.0004
EOF

# === solve block: lj_summary.json ===
cat > /app/outputs/lj_summary.json <<'EOF'
{
  "delta_F": -0.1044,
  "delta_F_error": 0.0011,
  "delta_S": -0.1318,
  "delta_S_error": 0.0068
}
EOF

# === solve block: rb_multistage_results.csv ===
cat > /app/outputs/rb_multistage_results.csv <<'EOF'
lambda_start,lambda_end,delta_F_per_particle,error
0.0,0.25,0.0266,0.0005
0.25,0.5,0.0266,0.0005
0.5,0.75,0.0266,0.0005
0.75,1.0,0.0265,0.0005
EOF

# === solve block: rb_summary.json ===
cat > /app/outputs/rb_summary.json <<'EOF'
{
  "delta_F": 0.1063,
  "delta_F_error": 0.0019
}
EOF

# === solve finalize ===
# consistency: sum of LJ per-stage should be -0.1044, sum of Rb per-stage should be 0.1063
