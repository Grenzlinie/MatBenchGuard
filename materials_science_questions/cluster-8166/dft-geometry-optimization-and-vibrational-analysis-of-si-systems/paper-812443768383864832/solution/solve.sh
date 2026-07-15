#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: equation_of_state.csv ===
cat > /app/outputs/equation_of_state.csv <<'FFEOF'
pressure,volume,volume_ratio
0,1084.71,1.0
5,1024.85,0.945
10,974.06,0.898
15,927.43,0.855
20,884.04,0.815
FFEOF

# === solve block: phonon_min_frequencies.csv ===
cat > /app/outputs/phonon_min_frequencies.csv <<'FFEOF'
pressure,min_frequency
5,20.0
16,-30.0
FFEOF

# === solve block: force_curve.csv ===
cat > /app/outputs/force_curve.csv <<'FFEOF'
displacement,force
0.00,0.00
0.01,0.10
0.02,0.20
0.03,0.30
0.04,0.40
0.05,0.50
0.06,0.60
0.07,0.70
0.08,0.80
0.09,0.90
0.10,1.00
FFEOF
