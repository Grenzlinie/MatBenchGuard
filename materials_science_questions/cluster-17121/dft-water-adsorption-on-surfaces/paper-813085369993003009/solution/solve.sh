#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.csv ===
cat > /app/outputs/results.csv << 'HEREDOC'
system,temperature_K,beta_self,beta_exch,alpha
argon,80,0.05,0.00,0.95
argon,100,0.05,0.10,0.85
argon,120,0.15,0.30,0.55
water,350,0.05,0.45,0.50
water,425,0.15,0.65,0.20
water,500,0.25,0.70,0.05
HEREDOC
