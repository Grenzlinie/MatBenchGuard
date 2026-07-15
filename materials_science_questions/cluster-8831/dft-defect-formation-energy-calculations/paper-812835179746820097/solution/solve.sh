#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv <<'FFEOF'
system,condition,formation_energy
ZnO,Zn-rich,-3.43
ZnO,O-rich,-3.43
Al0.0312Zn0.9688O,Zn-rich,-5.09
Al0.0312Zn0.9688O,O-rich,-8.58
Ga0.0312Zn0.9688O,Zn-rich,-2.71
Ga0.0312Zn0.9688O,O-rich,-6.20
Al0.0312Zn0.9376Ga0.0312O,Zn-rich,-4.94
Al0.0312Zn0.9376Ga0.0312O,O-rich,-11.92
FFEOF

# === solve block: optical_gap.csv ===
cat > /app/outputs/optical_gap.csv <<'FFEOF'
system,optical_gap
Al0.0312Zn0.9688O,3.59
Ga0.0312Zn0.9688O,3.54
Al0.0312Zn0.9376Ga0.0312O,4.20
FFEOF
