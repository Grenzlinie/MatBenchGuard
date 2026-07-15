#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: surface_states.json ===
cat > "/app/outputs/surface_states.json" <<'FFEOF'
{
  "B": [
    {
      "label": "sigma1",
      "energy_gamma": -3.0,
      "energy_k": -1.8,
      "energy_m": -1.2,
      "surface_weight_gamma": 0.70,
      "surface_weight_k": 0.68,
      "surface_weight_m": 0.72
    },
    {
      "label": "sp_z",
      "energy_gamma": -2.7,
      "energy_k": -1.5,
      "energy_m": -0.6
    },
    {
      "label": "sigma2",
      "energy_gamma": -0.4,
      "energy_k": 0.2,
      "energy_m": 0.0,
      "topmost_layer_fraction_gamma": 0.95
    },
    {
      "label": "sigma3",
      "energy_gamma": -0.4,
      "energy_k": 0.6,
      "energy_m": 0.4,
      "topmost_layer_fraction_gamma": 0.93
    }
  ],
  "Mg": [
    {
      "label": "sigma1",
      "energy_gamma": -3.9,
      "energy_k": -2.7,
      "energy_m": -2.1
    },
    {
      "label": "sp_z",
      "energy_gamma": -1.78,
      "energy_k": -0.6,
      "energy_m": 0.3
    },
    {
      "label": "sigma2",
      "energy_gamma": -1.2,
      "energy_k": -0.7,
      "energy_m": -0.5
    },
    {
      "label": "sigma3",
      "energy_gamma": -1.2,
      "energy_k": -0.3,
      "energy_m": -0.2
    }
  ],
  "Li": [
    {
      "label": "sigma1",
      "energy_gamma": -3.6,
      "energy_k": -2.4,
      "energy_m": -2.0
    },
    {
      "label": "sp_z",
      "energy_gamma": -0.1,
      "energy_k": 0.3,
      "energy_m": 0.5
    },
    {
      "label": "sigma2",
      "energy_gamma": -0.7,
      "energy_k": -0.2,
      "energy_m": 0.1
    },
    {
      "label": "sigma3",
      "energy_gamma": -0.7,
      "energy_k": 0.2,
      "energy_m": 0.4
    }
  ]
}
FFEOF

# === solve finalize ===
echo "surface_states.json written successfully."
