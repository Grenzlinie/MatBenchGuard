#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: heats_of_fusion.csv ===
cat > /app/outputs/heats_of_fusion.csv <<'FFEOF'
sample,delta_h_cal_per_g
air-quenched,3.6
slow-cooled,8.4
FFEOF

# === solve block: crystallinity_vs_temperature.csv ===
cat > /app/outputs/crystallinity_vs_temperature.csv <<'FFEOF'
temperature_C,air_quenched_crystallinity,slow_cooled_crystallinity
0,0.350,0.816
50,0.345,0.815
100,0.342,0.778
150,0.380,0.660
190,0.370,0.507
200,0.295,0.410
210,0.030,0.124
212,0.0,0.0
FFEOF
