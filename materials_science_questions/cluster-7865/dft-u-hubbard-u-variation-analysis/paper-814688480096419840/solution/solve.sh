#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: output_table_2_and_3.csv ===
cat > "/app/outputs/output_table_2_and_3.csv" <<'CSVEOF'
configuration,method,a,c,B,B_prime,magnetic_moment_Fe
NF,GGA,3.8268,,189,4.9,0.0
FM,GGA,3.9557,,139,4.3,3.18
FM,LSDA+U,3.9295,,198,7.2,3.90
FM,GGA+U,4.0263,,116,4.5,3.97
A-AFM,GGA,3.9078,3.6094,169,5.5,2.72
A-AFM,LSDA+U,3.9131,3.6681,177,5.7,2.95
A-AFM,GGA+U,4.1034,3.7884,131,5.4,3.1
G-AFM,GGA,3.9015,,144,3.2,2.82
G-AFM,LSDA+U,3.8849,,194,4.7,4.07
G-AFM,GGA+U,3.9155,,179,3.8,4.15
CSVEOF
