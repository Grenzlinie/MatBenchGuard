#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: bulk_thermal_conductivity.csv ===
OUTDIR=/app/outputs
cat > $OUTDIR/bulk_thermal_conductivity.csv <<'CSVEOF'
T,kappa_parallel,kappa_perp
2,0.1000,0.0387
10,20.0000,7.7419
20,16.0000,6.1935
30,12.0000,4.6452
40,9.0000,3.4839
50,7.0000,2.7097
60,5.5000,2.1290
70,4.5000,1.7419
80,3.8000,1.4710
90,3.2000,1.2387
100,2.8000,1.0839
150,2.2000,0.8516
200,1.9000,0.7355
250,1.7000,0.6581
300,1.5500,0.6000
350,1.3000,0.5032
400,1.1000,0.4258
CSVEOF

# === solve block: thin_film_thermal_conductivity.csv ===
cat > /app/outputs/thin_film_thermal_conductivity.csv <<'CSVEOF'
thickness_nm,kappa_perp
18,0.19
30,0.32
53,0.33
105,0.36
191,0.48
CSVEOF
