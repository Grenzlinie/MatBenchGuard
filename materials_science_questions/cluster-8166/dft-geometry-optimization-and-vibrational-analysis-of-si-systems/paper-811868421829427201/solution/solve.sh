#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'CSVEOF'
material,formation_energy
SiC,-14.5
Si,5.8
diamond,105.5
CSVEOF

# === solve block: sf_energies.csv ===
cat > "$OUTDIR/sf_energies.csv" <<'CSVEOF'
n,sf_energy
1,-3.4
2,-25.0
3,-0.5
4,1.2
5,-0.3
6,0.8
7,-0.1
8,0.4
9,-0.05
10,0.15
CSVEOF
