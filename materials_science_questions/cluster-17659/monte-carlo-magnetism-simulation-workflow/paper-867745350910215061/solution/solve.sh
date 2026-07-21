#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: lifetime_data.csv ===
cat > /app/outputs/lifetime_data.csv << 'CSVEOF'
H_z,inv_field,lifetime
-1.25,0.8,10000
-1.11111,0.9,9000
-1.0,1.0,8000
-0.90909,1.1,5500
-0.83333,1.2,3000
CSVEOF

# === solve block: slope_ratio.txt ===
echo '2.5' > /app/outputs/slope_ratio.txt
