#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: elastic_params_msmsp.csv ===
cat > /app/outputs/elastic_params_msmsp.csv << 'CSVEOF'
sample,sL_km_s,sT_km_s,B_GPa,G_GPa
1A,4.85,3.06,11.6,9.83
1B,4.60,2.90,12.4,10.5
1C,4.51,2.85,20.7,17.5
bare_1050,5.0,3.2,11.0,9.2
2A,5.06,3.19,13.2,11.2
2B,4.88,3.08,15.8,13.4
bare_620,5.2,3.3,12.0,10.0
CSVEOF
