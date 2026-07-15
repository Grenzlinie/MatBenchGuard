#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: cp_validation.csv ===
cat > "$OUTDIR/cp_validation.csv" <<'EOF'
Temperature_K,Cp_theoretical_JmolK,Cp_experimental_JmolK,RelativeError_percent
298.15,396.864,381.6,4.0
EOF

# === solve block: enthalpy_analysis.csv ===
cat > "$OUTDIR/enthalpy_analysis.csv" <<'EOF'
Blend,Delta_H_kJ_per_mol,Delta_H_percent_vs_n_butanol
n-butanol,100.0,0.0
G100,113.8,13.8
G10E,108.5,8.5
G20E,103.1,3.1
G10E_plus_60pct_nbutanol,103.4,3.4
G100_plus_40pct_nbutanol,108.28,8.28
EOF
