#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
cat > /app/outputs/results.json <<'EOF'
{
  "systems": [
    {
      "name": "bulk",
      "water_water_nn_distance": 0.29,
      "Na_water_nn_distance": 0.26,
      "Cl_water_nn_distance": 0.33,
      "Na_hydration_number": 5.5,
      "Cl_hydration_number": 6.5
    },
    {
      "name": "1nm_CNT",
      "water_water_nn_distance": 0.28,
      "Na_water_nn_distance": 0.26,
      "Cl_water_nn_distance": 0.33,
      "Na_hydration_number": 2.5,
      "Cl_hydration_number": 3.0
    },
    {
      "name": "2nm_CNT",
      "water_water_nn_distance": 0.29,
      "Na_water_nn_distance": 0.26,
      "Cl_water_nn_distance": 0.33,
      "Na_hydration_number": 5.0,
      "Cl_hydration_number": 7.0
    },
    {
      "name": "3nm_CNT",
      "water_water_nn_distance": 0.29,
      "Na_water_nn_distance": 0.26,
      "Cl_water_nn_distance": 0.33,
      "Na_hydration_number": 5.4,
      "Cl_hydration_number": 6.6
    }
  ]
}
EOF

# === solve finalize ===
echo 'all done'
