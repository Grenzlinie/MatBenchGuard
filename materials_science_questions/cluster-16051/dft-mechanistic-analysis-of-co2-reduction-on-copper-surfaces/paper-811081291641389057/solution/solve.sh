#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p $OUTDIR

# === solve block: formation_energies.csv ===
cat > "$OUTDIR/formation_energies.csv" <<'CSVEOF'
surface,cluster,is_hydrogenated,mu_H,formation_energy_per_C,structure_type
Cu111,C6,false,-1.6,-0.05,chain
Cu111,C6,false,-0.6,-0.05,chain
Cu111,C6H6,true,-1.6,0.65,chain
Cu111,C6H6,true,-0.6,-0.35,ring
Ni111,C6,false,-1.6,-0.10,chain
Ni111,C6,false,-0.6,-0.10,chain
Ni111,C6H6,true,-1.6,0.60,chain
Ni111,C6H6,true,-0.6,-0.40,chain
CSVEOF

cat > "$OUTDIR/structural_preference.csv" <<'CSVEOF'
surface,lower_energy_structure
Cu111,ring
Ni111,chain
CSVEOF

echo "1.20" > "$OUTDIR/coalescence_barrier.txt"

# === solve block: structural_preference.csv ===
cat > "$OUTDIR/structural_preference.csv" <<'CSVEOF'
surface,lower_energy_structure
Cu111,ring
Ni111,chain
CSVEOF

# === solve block: coalescence_barrier.txt ===
echo "1.20" > "$OUTDIR/coalescence_barrier.txt"
