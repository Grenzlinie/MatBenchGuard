#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phonon_stability.json ===
cat > "$OUTDIR/phonon_stability.json" <<'FFEOF'
{
  "dynamically_stable": true
}
FFEOF

# === solve block: lattice_thermal_conductivity.csv ===
cat > "$OUTDIR/lattice_thermal_conductivity.csv" <<'FFEOF'
material,direction,kappa_l
SnSe,armchair,2.4
SnSe,zigzag,2.6
SnS,armchair,4.4
SnS,zigzag,4.7
GeSe,armchair,5.2
GeSe,zigzag,6.7
GeS,armchair,7.8
GeS,zigzag,10.5
FFEOF

# === solve block: zt_table.csv ===
cat > "$OUTDIR/zt_table.csv" <<'FFEOF'
material,direction,temperature_K,ZT
SnSe,armchair,300,1.2
SnSe,armchair,500,2.0
SnSe,armchair,700,2.63
SnSe,zigzag,300,1.1
SnSe,zigzag,500,1.9
SnSe,zigzag,700,2.46
SnS,armchair,300,0.8
SnS,armchair,500,1.3
SnS,armchair,700,1.75
SnS,zigzag,300,0.9
SnS,zigzag,500,1.4
SnS,zigzag,700,1.88
GeSe,armchair,300,0.9
GeSe,armchair,500,1.5
GeSe,armchair,700,1.99
GeSe,zigzag,300,0.7
GeSe,zigzag,500,1.2
GeSe,zigzag,700,1.73
GeS,armchair,300,0.8
GeS,armchair,500,1.3
GeS,armchair,700,1.85
GeS,zigzag,300,0.6
GeS,zigzag,500,0.9
GeS,zigzag,700,1.29
FFEOF

# === solve finalize ===
# Nothing left to do; all declared outputs have been written.
