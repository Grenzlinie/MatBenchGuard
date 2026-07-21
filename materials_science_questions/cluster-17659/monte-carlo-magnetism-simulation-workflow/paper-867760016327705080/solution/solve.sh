#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "$OUTDIR"

# === solve block: domain_metrics.csv ===
cat > "$OUTDIR/domain_metrics.csv" <<'FFEOF'
temperature,field,time,largest_cluster_fraction,number_of_clusters
2.0,0.1,40,0.01,200000
2.0,0.1,400,0.05,150000
2.0,0.1,4000,0.2,80000
2.0,0.1,40000,0.6,20000
2.0,0.9,40,0.001,250000
2.0,0.9,400,0.001,250000
2.0,0.9,4000,0.002,240000
2.0,0.9,40000,0.005,200000
99.0,0.1,40,0.0005,250000
99.0,0.1,400,0.0006,250000
99.0,0.1,4000,0.0006,250000
99.0,0.1,40000,0.0007,250000
FFEOF
