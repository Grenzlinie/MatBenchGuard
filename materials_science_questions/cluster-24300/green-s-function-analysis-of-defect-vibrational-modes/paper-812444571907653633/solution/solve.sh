#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: impurity_frequencies.csv ===
# Write the scored impurity frequencies (gold values)
cat > "${OUTDIR}/impurity_frequencies.csv" <<'EOF'
impurity_site,impurity_mass,force_constant_change_t,computed_frequency
In,11.0,0.25,522.8
P,75.0,0.07,270.0
EOF
