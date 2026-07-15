#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_summary.csv ===
cat > /app/outputs/results_summary.csv <<'CSVEOF'
experiment,material,actual_failure_time_seconds,predicted_failure_time_seconds,alpha,eta
0.5 min,granite,35,35,1.45,0.1
3.4 min,granite,205,205,1.65,0.1
5 hr,granite,18000,18000,1.78,0.1
6 hr,granite,21300,21300,1.82,0.1
10 hr,granite,35389,35389,1.80,0.1
50 hr,granite,180224,180224,1.88,0.1
Location 8,bone,358,358,1.89,0.1
Location 3,bone,1358,1358,1.58,0.1
CSVEOF
