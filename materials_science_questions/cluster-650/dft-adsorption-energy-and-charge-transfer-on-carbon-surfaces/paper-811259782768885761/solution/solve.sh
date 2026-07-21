#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: overpotentials.csv ===
cat > /app/outputs/overpotentials.csv <<'FFEOF'
catalyst,overpotential_V,rds
V3C2,0.64,TS1
Nb3C2,0.90,TS2
FFEOF

# === solve block: activation_barriers.csv ===
cat > /app/outputs/activation_barriers.csv <<'FFEOF'
barrier_eV,catalyst,ts_id
0.64,V3C2,TS1
0.32,V3C2,TS2
0.0,V3C2,TS3
0.25,V3C2,TS4
0.85,Nb3C2,TS1
0.90,Nb3C2,TS2
0.0,Nb3C2,TS3
0.79,Nb3C2,TS4
FFEOF
