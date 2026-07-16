#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results.json ===
# Write results.json
cat > /app/outputs/results.json << 'FFEOF'
{
  "junction_formed": true,
  "junction_length_r0": 10.0,
  "jog_direction": "[0-1-1]",
  "critical_breaking_angle_degrees": 70.0,
  "partial_reaction_b2_analysis": {
    "alphaB_deltaA": {
      "reactants": ["alphaB", "deltaA"],
      "product": "alpha_delta_AB",
      "reactant_b2_sum": "12/36",
      "product_b2": "10/36"
    },
    "alphaB_Bdelta": {
      "reactants": ["alphaB", "Bdelta"],
      "product": "alpha_delta",
      "reactant_b2_sum": "12/36",
      "product_b2": "2/36"
    }
  }
}
FFEOF
