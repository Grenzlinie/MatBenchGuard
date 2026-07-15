#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_total_energies.csv ===
cat > /app/outputs/step_01_total_energies.csv <<'FFEOF'
species,total_energy_hartree,relative_energy_kJmol,reference
R1+R2,-732.42938,0.0,R1+R2
INT2,-732.46407,-91.0,R1+R2
TS2,-732.45899,-78.0,R1+R2
P2,-732.52047,-239.0,R1+R2
INT4,-732.49804,-180.0,R1+R2
TS4,-732.49577,-174.0,R1+R2
P4,-732.58323,-404.0,R1+R2
P2+R2,-885.88188,0.0,P2+R2
INT3,-885.89752,-41.0,P2+R2
TS3,-885.85155,80.0,P2+R2
P3,-885.92836,-122.0,P2+R2
INT4+R2,-885.85945,0.0,INT4+R2
INT5,-885.87083,-30.0,INT4+R2
TS5,-885.85005,25.0,INT4+R2
P5,-885.91973,-158.0,INT4+R2
FFEOF

# === solve block: step_02_dominant_barriers.json ===
cat > /app/outputs/step_02_dominant_barriers.json <<'FFEOF'
[
  {"channel": "Reaction3", "barrier_kJmol": 13.0, "exothermicity_kJmol": 91.0},
  {"channel": "Reaction4", "barrier_kJmol": 6.0, "exothermicity_kJmol": 180.0},
  {"channel": "Reaction5", "barrier_kJmol": 55.0, "exothermicity_kJmol": 30.0}
]
FFEOF
