#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: migration_barriers_NiCoX.csv ===
cat > /app/outputs/migration_barriers_NiCoX.csv <<'HEOF'
alloy,atom_type,migration_barrier_eV
Ni0.6Co0.2Co0.2,Ni,1.25
Ni0.6Co0.2Co0.2,Ni,1.32
Ni0.6Co0.2Co0.2,Co,1.18
Ni0.6Co0.2Co0.2,Co,1.18
Ni0.6Co0.2Fe0.2,Ni,1.22
Ni0.6Co0.2Fe0.2,Ni,1.28
Ni0.6Co0.2Fe0.2,Co,1.14
Ni0.6Co0.2Fe0.2,Co,1.14
Ni0.6Co0.2Mn0.2,Ni,0.90
Ni0.6Co0.2Mn0.2,Ni,0.95
Ni0.6Co0.2Mn0.2,Co,0.81
Ni0.6Co0.2Mn0.2,Co,0.81
HEOF

# === solve block: migration_barriers_universality.csv ===
cat > /app/outputs/migration_barriers_universality.csv <<'HEOF'
system,atom_type,migration_barrier_eV
pure Cu,Cu,0.78
pure Cu,Cu,0.80
Cu0.8Mn0.2,Cu,0.52
Cu0.8Mn0.2,Cu,0.55
pure Fe,Fe,0.72
pure Fe,Fe,0.76
Fe0.8Mn0.2,Fe,0.48
Fe0.8Mn0.2,Fe,0.52
pure V,V,0.65
pure V,V,0.70
V0.8Mn0.2,V,0.35
V0.8Mn0.2,V,0.40
HEOF
