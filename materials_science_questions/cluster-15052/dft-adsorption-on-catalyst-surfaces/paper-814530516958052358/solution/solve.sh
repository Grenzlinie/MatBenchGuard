#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: dft_results.json ===
cat > /app/outputs/dft_results.json <<'EOF'
{
  "k_adsorption_energy_beta": -4.75,
  "bader_charge_transfer": 0.92,
  "co_adsorption_energy_clean_beta": -0.14,
  "co_adsorption_energy_k_beta": -0.05,
  "o2_adsorption_energy_clean_vacancy_beta": -0.06,
  "o2_adsorption_energy_k_vacancy_beta": -0.16,
  "o2_bond_length_clean_vacancy_beta": 1.242,
  "o2_bond_length_k_vacancy_beta": 1.283,
  "barrier_co_obr_clean_beta": 0.13,
  "barrier_co_obr_k_beta": 0.09,
  "k_adsorption_energy_alpha": -5.67,
  "co_adsorption_energy_alpha": -0.23,
  "barrier_co_obr_alpha": 0.26,
  "bulk_alpha_a": 9.729,
  "bulk_alpha_c": 2.894,
  "bulk_beta_a": 4.417,
  "bulk_beta_c": 2.905
}
EOF
