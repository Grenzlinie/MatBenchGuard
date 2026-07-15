#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
OUTDIR=/app/outputs

# === solve block: bond_lengths_angles.csv ===
cat > "$OUTDIR/bond_lengths_angles.csv" <<'FFEOF'
parameter,value,unit
Mg8-O1,2.02,Å
O8-Mg1,1.97,Å
Mg1-O2,2.06,Å
O1-Mg2,2.09,Å
Mg2-O3,2.09,Å
O2-Mg3,2.13,Å
Mg8-O1-Mg2,95.5,°
O8-Mg1-O2,100.1,°
Mg1-O2-Mg3,108.2,°
O1-Mg2-O3,106.3,°
FFEOF

# === solve block: rumpling.csv ===
cat > "$OUTDIR/rumpling.csv" <<'FFEOF'
position,out_of_plane_rumpling,in_plane_rumpling
1,0.071,0.072
2,-0.037,-0.023
3,0.056,-0.014
4,0.049,0.004
5,0.050,0.000
6,0.050,-0.001
7,0.053,0.006
8,0.040,-0.025
FFEOF

# === solve block: step_energies.csv ===
cat > "$OUTDIR/step_energies.csv" <<'FFEOF'
energy_type,gamma
relaxed,-188
unrelaxed,-305
FFEOF
