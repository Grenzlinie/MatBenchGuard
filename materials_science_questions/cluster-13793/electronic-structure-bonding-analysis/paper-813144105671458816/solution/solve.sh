#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: band_gaps_GGA.csv ===
cat > "$OUTDIR/band_gaps_GGA.csv" <<'FFEOF'
Compound,Eg_GGA (eV)
MgSiN2,4.8
MgGeN2,2.5
MgSiP2,2.08
MgGeP2,1.5
FFEOF

# === solve block: band_gaps_EV.csv ===
cat > "$OUTDIR/band_gaps_EV.csv" <<'FFEOF'
Compound,Eg_EV (eV)
MgSiN2,4.87
MgGeN2,2.54
MgSiP2,2.18
MgGeP2,1.6
FFEOF

# === solve block: optical_static.csv ===
cat > "$OUTDIR/optical_static.csv" <<'FFEOF'
Compound,n_par_0,n_perp_0,R_par_0 (%),R_perp_0 (%),critical_point (eV)
MgSiN2,1.90,1.9013,9.71,9.65,4.71
MgGeN2,2.16,2.18,13.61,13.77,2.55
MgSiP2,2.826,2.952,22.78,24.40,2.20
MgGeP2,3.065,3.030,25.81,25.38,1.92
FFEOF
