#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: alpha_D_table.csv ===
cat > /app/outputs/alpha_D_table.csv << 'EOF'
molecule_id,HF,B3LYP,CC2,CCSD
1,-13.8,-17.5,-38.4,-29.2
2,53.4,78.6,101.8,78.3
3,78.4,53.1,66.6,69.0
4,162.9,167.1,170.1,156.0
5,48.6,59.0,43.2,41.2
6,-21.6,3.4,-14.5,-2.6
7,65.9,103.1,123.0,93.5
8,-60.4,-28.4,-27.2,-29.9
9,42.8,78.6,60.0,61.3
10,-133.3,-133.2,-114.8,-117.1
11,-129.2,-171.7,-154.3,-128.9
13,117.4,135.4,104.1,79.2
14,-606.7,-1215.8,-1000.0,-740.6
EOF
