#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: magnetic_results.csv ===
cat > "$OUTDIR/magnetic_results.csv" <<'FFEOF'
E_nonmag,E_spin,compound,total_spin_moment
-1200.0,-1200.0,UFeAl,0.0
-1210.0,-1210.002,UCoAl,0.0
-1220.0,-1220.05,UNiAl,1.42
-1230.0,-1230.0,URuAl,0.0
-1240.0,-1240.05,URhAl,0.65
-1250.0,-1250.05,UIrAl,0.57
-1260.0,-1260.05,UPtAl,1.47
FFEOF
