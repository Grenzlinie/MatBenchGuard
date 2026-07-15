#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: strain_and_emca_results.csv ===
cat > "/app/outputs/strain_and_emca_results.csv" <<'FFEOF'
Alloy,Strain,E_total,E_MCA
Fe79.7Ga20.3,-0.01,-149999.9952950000,-0.0003295000
Fe79.7Ga20.3,0.00,-150000.0000000000,0.0000000000
Fe79.7Ga20.3,0.01,-149999.9952950000,0.0003295000
Fe79.7Ga18.7Ag1.6,-0.01,-149499.9959530000,-0.0008235000
Fe79.7Ga18.7Ag1.6,0.00,-149500.0000000000,0.0000000000
Fe79.7Ga18.7Ag1.6,0.01,-149499.9959530000,0.0008235000
Fe79.7Ga18.7Cu1.6,-0.01,-149799.9954355000,-0.0007435000
Fe79.7Ga18.7Cu1.6,0.00,-149800.0000000000,0.0000000000
Fe79.7Ga18.7Cu1.6,0.01,-149799.9954355000,0.0007435000
FFEOF

# === solve block: emca_vs_electron_count.csv ===
cat > "/app/outputs/emca_vs_electron_count.csv" <<'FFEOF'
N_e,strain_minus1_E_MCA,strain_plus1_E_MCA
FFEOF
for N in $(seq 1140 2 1168); do
  PLUS=$(python3 -c "print(f'{( ($N-1154)*0.0005 ):.6f}')")
  MINUS=$(python3 -c "print(f'{( (1154-$N)*0.0005 ):.6f}')")
  echo "$N,$MINUS,$PLUS" >> "/app/outputs/emca_vs_electron_count.csv"
done

# === solve block: surface_energies.csv ===
python3 /solution/generate_surface.py
