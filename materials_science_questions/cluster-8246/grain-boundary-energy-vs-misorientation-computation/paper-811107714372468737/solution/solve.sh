#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: predicted_energies.csv ===
cat > "$OUTDIR/predicted_energies.csv" <<'FFEOF'
boundary_name,misorientation_angle_deg,predicted_energy_Jm2
Sigma13/(230),67.38,0.96
Sigma25/(430),73.74,0.98
Sigma25/(710),16.26,0.91
Sigma29/(520),43.6,1.00
Sigma29/(730),46.4,1.01
Sigma37/(610),18.92,0.94
Sigma37/(750),71.08,0.97
Sigma41/(910),12.68,0.93
Sigma41/(540),77.32,0.99
Sigma53/(720),31.89,0.97
Sigma53/(950),58.11,0.99
Sigma61/(11 1 0),10.39,0.92
Sigma125/(11 2 0),20.61,0.95
FFEOF
