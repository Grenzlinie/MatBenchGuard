#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: adsorption_energies.csv ===
cat > /app/outputs/adsorption_energies.csv <<'FFEOF'
slab,model,E_ads
3,R,10.70
3,H1,8.86
3,H2,8.96
6,R,7.12
6,H1,6.58
6,H2,7.72
9,R,7.86
9,H1,6.58
9,H2,6.62
FFEOF

cat > /app/outputs/spin_analysis.csv <<'FFEOF'
slab,max_abs_spin_Ti,max_abs_spin_H
3,1.481,0.006
6,0.879,0.019
FFEOF

cat > /app/outputs/nh3_adsorption.csv <<'FFEOF'
slab,system,E_ads_NH3
3,clean,1.40
3,H_covered,0.18
6,clean,0.74
6,H_covered,0.21
FFEOF

# === solve block: spin_analysis.csv ===
cat > /app/outputs/spin_analysis.csv <<'FFEOF'
slab,max_abs_spin_Ti,max_abs_spin_H
3,1.481,0.006
6,0.879,0.019
FFEOF

# === solve block: nh3_adsorption.csv ===
cat > /app/outputs/nh3_adsorption.csv <<'FFEOF'
slab,system,E_ads_NH3
3,clean,1.40
3,H_covered,0.18
6,clean,0.74
6,H_covered,0.21
FFEOF
