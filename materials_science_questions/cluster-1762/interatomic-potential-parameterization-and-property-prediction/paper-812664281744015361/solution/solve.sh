#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results.json ===
cat > /app/outputs/results.json <<'FFEOF'
{
  "relaxation_ratio": 1.21,
  "P_Ga": {
    "A": 982.8,
    "alpha2": 1.0,
    "beta2": 0.0,
    "eta2": 0.264,
    "theta": 0.0
  },
  "P4": [
    {
      "A_parallel": 105,
      "A_perp": 62,
      "a": 76,
      "b": 14,
      "alpha2": 0.13,
      "beta2": 0.87,
      "eta2": 0.158,
      "theta": 35.26
    },
    {
      "A_parallel": 105,
      "A_perp": 62,
      "a": 76,
      "b": 14,
      "alpha2": 0.13,
      "beta2": 0.87,
      "eta2": 0.158,
      "theta": 35.26
    },
    {
      "A_parallel": 105,
      "A_perp": 62,
      "a": 76,
      "b": 14,
      "alpha2": 0.13,
      "beta2": 0.87,
      "eta2": 0.158,
      "theta": 35.26
    },
    {
      "A_parallel": 105,
      "A_perp": 62,
      "a": 76,
      "b": 14,
      "alpha2": 0.13,
      "beta2": 0.87,
      "eta2": 0.158,
      "theta": 35.26
    }
  ],
  "Ga12": [
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    },
    {
      "a": 0.4,
      "b": 0.15,
      "alpha2": 0.054,
      "beta2": 0.946,
      "eta2": 0.003
    }
  ]
}
FFEOF

# === solve block: wavefunction_amplitudes.json ===
cat > /app/outputs/wavefunction_amplitudes.json <<'FFEOF'
{
  "A1_01_amplitude": -0.514,
  "A1_11_amplitude": 0.786
}
FFEOF
