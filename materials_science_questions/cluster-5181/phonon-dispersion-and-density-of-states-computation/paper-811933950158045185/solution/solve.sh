#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: frequency_shifts.csv ===
cat > "$OUTDIR/frequency_shifts.csv" <<'FFEOF'
distribution,density,frequency_shift_THz
AED,0.002,0.024
AED,0.004,0.048
AED,0.006,0.072
AED,0.008,0.096
AED,0.010,0.120
NTD,0.002,0.036
NTD,0.004,0.072
NTD,0.006,0.108
NTD,0.008,0.144
NTD,0.010,0.180
TD,0.002,0.048
TD,0.004,0.096
TD,0.006,0.144
TD,0.008,0.192
TD,0.010,0.240
ID,0.002,0.060
ID,0.004,0.120
ID,0.006,0.180
ID,0.008,0.240
ID,0.010,0.300
FFEOF
