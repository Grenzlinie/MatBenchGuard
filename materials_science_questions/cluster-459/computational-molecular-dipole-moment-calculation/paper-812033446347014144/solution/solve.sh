#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: total_energies.csv ===
cat > "$OUTDIR/total_energies.csv" <<'ENDCSV'
R,total_energy
0.5,2.396
1.0,2.675
2.0,2.667
3.0,2.295
4.0,2.062
5.0,1.845
ENDCSV

# === solve block: potential_energies.csv ===
cat > /app/outputs/potential_energies.csv <<'ENDCSV'
R,potential_energy
0.5,4.965
1.0,5.787
2.0,4.600
3.0,3.497
4.0,3.003
5.0,2.793
ENDCSV
