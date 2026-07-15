#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: results_Q_inv.json ===
cat > /app/outputs/results_Q_inv.json <<'FFEOF'
{
  "static_charges_SiO2": 1e-06,
  "ohmic_graphene_gate": 0.01,
  "velcro_effect": 0.0,
  "two_level_systems": 1e-22,
  "attachment_losses": 1e-05,
  "thermoelastic_losses": 1e-07,
  "dominant_mechanism": "ohmic_graphene_gate"
}
FFEOF
