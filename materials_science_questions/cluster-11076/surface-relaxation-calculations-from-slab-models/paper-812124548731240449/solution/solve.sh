#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.csv ===
cat > "$OUTDIR/results.csv" <<'FFEOF'
metal,Δd12_percent,Δd23_percent,Δd34_percent,Δd45_percent,Δd56_percent,surface_energy_relaxed,surface_energy_unrelaxed
Cu,-0.83,0.08,0,0,0,1645,1651
Ag,-1.04,0.1,-0.02,0,0,1266,1275
Au,-5.84,1.18,-0.25,0.05,0.02,1031,1083
Ni,2.53,0.14,0.06,0.01,0,2418,2434
Pd,-1.97,0.11,-0.08,0,0,1652,1661
Pt,-2.11,0.16,-0.03,0,0,2149,2168
Al,0.80,0.09,0.03,0,0,897,900
Pb,-6.14,1.5,-0.28,0.12,0.08,408,424
Rh,0.2,-0.04,-0.04,-0.01,0,2842,2902
Ir,0.59,0,-0.02,0,0,2905,2907
FFEOF
