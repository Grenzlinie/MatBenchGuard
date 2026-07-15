#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: optimized_structures_rutile.csv ===
cat > "$OUTDIR/optimized_structures_rutile.csv" <<'CSVEOF'
pseudopotential,a,c,c/a,u,d
TM,4.555,2.922,0.6414,0.3042,4.377
Teter,4.528,2.918,0.6444,0.3033,4.435
CSVEOF

# === solve block: optimized_structures_anatase.csv ===
cat > "$OUTDIR/optimized_structures_anatase.csv" <<'CSVEOF'
pseudopotential,a,c,c/a,u,d
TM,3.744,9.497,2.536,0.2071,3.987
Teter,3.747,9.334,2.491,0.2100,4.050
CSVEOF

# === solve block: bulk_moduli.csv ===
cat > "$OUTDIR/bulk_moduli.csv" <<'CSVEOF'
pseudopotential,phase,B
TM,rutile,242
TM,anatase,196
Teter,rutile,253
Teter,anatase,187
CSVEOF

# === solve block: band_gaps.csv ===
cat > "$OUTDIR/band_gaps.csv" <<'CSVEOF'
pseudopotential,phase,gap_type,gap_value
TM,rutile,direct,1.88
TM,anatase,indirect,2.05
Teter,rutile,direct,1.88
Teter,anatase,indirect,2.05
CSVEOF

# === solve block: total_energy_difference.csv ===
cat > "$OUTDIR/total_energy_difference.csv" <<'CSVEOF'
pseudopotential,delta_E,stable_phase
TM,-1.4,anatase
Teter,1.1,rutile
CSVEOF

# === solve finalize ===
echo "All oracle artifacts written."
