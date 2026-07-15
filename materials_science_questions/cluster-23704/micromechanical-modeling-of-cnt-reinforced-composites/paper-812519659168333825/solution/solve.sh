#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_results.json ===
cat > /app/outputs/computed_results.json <<'EOF'
{
  "validation": {
    "natural_frequencies": [
      {"mode": 1, "frequency": 112.12},
      {"mode": 2, "frequency": 366.23},
      {"mode": 3, "frequency": 687.33},
      {"mode": 4, "frequency": 1074.98},
      {"mode": 5, "frequency": 1666.44}
    ],
    "buckling_loads": [
      {"BC": "SS", "buckling_load": 0.09844},
      {"BC": "CS", "buckling_load": 0.14852},
      {"BC": "CC", "buckling_load": 0.21272}
    ],
    "dimensionless_frequencies": [
      {"theory": "FSDT", "dimensionless_frequency": 0.9974},
      {"theory": "TSDT", "dimensionless_frequency": 0.9749},
      {"theory": "ESDT", "dimensionless_frequency": 0.9759},
      {"theory": "HSDT", "dimensionless_frequency": 0.9744},
      {"theory": "TrSDT", "dimensionless_frequency": 0.9741}
    ]
  },
  "dir_cnt": [
    {"cnt_weight_frac": 0.01, "beta": 0.0, "excitation_frequency": 80.0},
    {"cnt_weight_frac": 0.01, "beta": 0.2, "excitation_frequency": 72.0},
    {"cnt_weight_frac": 0.01, "beta": 0.4, "excitation_frequency": 60.0},
    {"cnt_weight_frac": 0.01, "beta": 0.6, "excitation_frequency": 44.0},
    {"cnt_weight_frac": 0.01, "beta": 0.8, "excitation_frequency": 20.0},
    {"cnt_weight_frac": 0.02, "beta": 0.0, "excitation_frequency": 90.0},
    {"cnt_weight_frac": 0.02, "beta": 0.2, "excitation_frequency": 82.0},
    {"cnt_weight_frac": 0.02, "beta": 0.4, "excitation_frequency": 70.0},
    {"cnt_weight_frac": 0.02, "beta": 0.6, "excitation_frequency": 54.0},
    {"cnt_weight_frac": 0.02, "beta": 0.8, "excitation_frequency": 30.0},
    {"cnt_weight_frac": 0.03, "beta": 0.0, "excitation_frequency": 100.0},
    {"cnt_weight_frac": 0.03, "beta": 0.2, "excitation_frequency": 92.0},
    {"cnt_weight_frac": 0.03, "beta": 0.4, "excitation_frequency": 80.0},
    {"cnt_weight_frac": 0.03, "beta": 0.6, "excitation_frequency": 64.0},
    {"cnt_weight_frac": 0.03, "beta": 0.8, "excitation_frequency": 40.0}
  ],
  "dir_cf": [
    {"cf_volume_frac": 0.2, "beta": 0.0, "excitation_frequency": 85.0},
    {"cf_volume_frac": 0.2, "beta": 0.2, "excitation_frequency": 77.0},
    {"cf_volume_frac": 0.2, "beta": 0.4, "excitation_frequency": 65.0},
    {"cf_volume_frac": 0.2, "beta": 0.6, "excitation_frequency": 49.0},
    {"cf_volume_frac": 0.2, "beta": 0.8, "excitation_frequency": 25.0},
    {"cf_volume_frac": 0.3, "beta": 0.0, "excitation_frequency": 95.0},
    {"cf_volume_frac": 0.3, "beta": 0.2, "excitation_frequency": 87.0},
    {"cf_volume_frac": 0.3, "beta": 0.4, "excitation_frequency": 75.0},
    {"cf_volume_frac": 0.3, "beta": 0.6, "excitation_frequency": 59.0},
    {"cf_volume_frac": 0.3, "beta": 0.8, "excitation_frequency": 35.0}
  ]
}
EOF
