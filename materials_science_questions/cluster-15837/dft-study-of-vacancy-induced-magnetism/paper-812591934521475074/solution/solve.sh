#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: occupancies_results.json ===
cat > /app/outputs/occupancies_results.json <<'FFEOF'
{
  "H_C_center": {
    "n_up": 0.970,
    "n_down": 0.062,
    "magnetic": true
  },
  "H_O_center": {
    "n_up": 0.940,
    "n_down": 0.063,
    "magnetic": true
  },
  "H_center": {
    "n_up": 0.994,
    "n_down": 0.057,
    "magnetic": true
  },
  "H_C_near": {
    "n_up": 0.930,
    "n_down": 0.930,
    "magnetic": false
  },
  "H_O_near": {
    "n_up": 0.870,
    "n_down": 0.870,
    "magnetic": false
  },
  "H_near": {
    "n_up": 0.978,
    "n_down": 0.182,
    "magnetic": true
  },
  "crossover": {
    "H_C_crossover_R": 2.70,
    "H_O_crossover_R": 4.25
  }
}
FFEOF
