#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: phonon_frequencies.csv ===
cat > "$OUTDIR/phonon_frequencies.csv" <<'FFEOF'
k_point,branch,frequency_cm1
Gamma,LA,0
Gamma,TA,0
Gamma,ZA,0
Gamma,LO,1596
Gamma,TO,1596
Gamma,ZO,861
M,ZA,632
M,TA,1106
M,LA,1289
M,ZO,834
M,LO,1375
M,TO,1317
K,ZA,538
K,TA,1000
K,LA,1215
K,ZO,812
K,LO,1337
K,TO,1261
FFEOF
