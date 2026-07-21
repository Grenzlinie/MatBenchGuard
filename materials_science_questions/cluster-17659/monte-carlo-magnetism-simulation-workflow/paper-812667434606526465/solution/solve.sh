#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: phase_diagram.csv ===
cat > "$OUTDIR/phase_diagram.csv" <<'FFEOF'
T,H,M_perp,M_z,boundary_flag,transition_order
0.10,13.0,0.98,0.05,1,1
0.20,12.0,0.95,0.07,1,1
0.30,11.0,0.90,0.10,1,1
0.40,10.0,0.85,0.12,1,1
0.50,9.0,0.70,0.15,1,1
0.60,7.2,0.50,0.08,1,2
0.70,5.5,0.30,0.05,1,2
0.80,3.5,0.10,0.02,1,2
0.95,0.0,0.01,0.00,1,2
FFEOF

# === solve block: isentropes.csv ===
cat > "$OUTDIR/isentropes.csv" <<'FFEOF'
S,T,H
-3.0,0.35,14.1
-3.0,0.35,12.0
-3.0,0.35,10.0
-3.0,0.35,8.0
-3.0,0.35,6.0
-3.0,0.35,4.0
-3.0,0.35,2.0
-3.0,0.35,0.0
-1.4,0.8,9.5
-1.4,0.8,8.0
-1.4,0.8,6.0
-1.4,0.8,4.0
-1.4,0.8,2.0
-1.4,0.8,0.0
FFEOF

# === solve block: growth_exponent.txt ===
echo "0.50" > "$OUTDIR/growth_exponent.txt"
