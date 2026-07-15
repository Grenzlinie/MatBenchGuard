#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: efficiency_vs_Tph.csv ===
cat > "$OUTDIR/efficiency_vs_Tph.csv" <<'CSVEOF'
T_ph,kappa_sigma,eta_max
350,0,34.5
350,0.0001,33.5
350,0.001,31.0
350,0.00316227766,28.0
400,0,38.5
400,0.0001,37.5
400,0.001,31.5
400,0.00316227766,26.0
450,0,43.0
450,0.0001,41.5
450,0.001,32.0
450,0.00316227766,24.0
CSVEOF

# === solve block: analytic_bound.txt ===
cat > "$OUTDIR/analytic_bound.txt" <<'TXEOF'
kappa/sigma <= (Eb/q) * 3.0e-3 V^2/K
1.65e-3
TXEOF

# === solve block: candidate_check.txt ===
cat > "$OUTDIR/candidate_check.txt" <<'TXEOF'
Bi2Te3: kappa/sigma = 1.4e-5 V^2/K, satisfies bound but band gap too small.
CsSnI3: kappa/sigma = 2.0e-5 V^2/K, satisfies bound with usable band gap.
TXEOF
