#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_03_test_results.csv ===
cat > "$OUTDIR/step_03_test_results.csv" <<'EOF'
system,functional,correction_type,binding_energy_kJmol,equilibrium_distance_A
(P2)2,BP,uncorrected,,
(P2)2,PBE,uncorrected,-0.56,5.00
(P2)2,BLYP,uncorrected,,
(P2)2,BP,DCACP,-2.65,4.60
(P2)2,PBE,DCACP,-2.65,4.60
(P2)2,BLYP,DCACP,-2.65,4.75
(PH3)2,BP,uncorrected,,
(PH3)2,PBE,uncorrected,-1.64,4.20
(PH3)2,BLYP,uncorrected,,
(PH3)2,BP,DCACP,-3.19,3.85
(PH3)2,PBE,DCACP,-3.16,4.0
(PH3)2,BLYP,DCACP,-3.17,4.0
(PN)2,BP,uncorrected,-4.47,3.85
(PN)2,PBE,uncorrected,-7.88,3.70
(PN)2,BLYP,uncorrected,-4.47,4.0
(PN)2,BP,DCACP,-9.94,3.68
(PN)2,PBE,DCACP,-14.81,3.63
(PN)2,BLYP,DCACP,-9.70,3.74
EOF
