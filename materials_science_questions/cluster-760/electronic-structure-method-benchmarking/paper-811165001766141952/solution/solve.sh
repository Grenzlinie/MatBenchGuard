#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: benchmark_results.json ===
mkdir -p /app/outputs
cat > /app/outputs/benchmark_results.json <<'FFEOF'
{
  "SiN": {
    "re": 1.5736,
    "we": 1181.19,
    "T_A2Pi": 2084.94
  },
  "SiN2": {
    "r_NN": 1.1459,
    "r_SiN": 1.7559,
    "we1": 1825.85,
    "we2": 328.63,
    "we3": 515.30
  },
  "Si2N": {
    "r_SiN": 1.6400,
    "we1": 615.76,
    "we2": 172.45,
    "we3": 1065.53
  }
}
FFEOF
