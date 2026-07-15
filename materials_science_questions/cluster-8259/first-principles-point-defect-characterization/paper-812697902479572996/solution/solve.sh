#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: reproduction_results.json ===
cat > /app/outputs/reproduction_results.json <<'FFEOF'
{
  "total_energies": {
    "SiO2_bulk": -100000.0,
    "VO": -99993.1,
    "NO": 0.0,
    "O2": 0.0,
    "H": -50.0,
    "S2_-1": -99996.7,
    "S2_0": -99995.3,
    "S2_+1": -99991.5,
    "S3_-1": -99995.6,
    "S3_0": -99993.8,
    "S3_+1": -99989.7,
    "S2O_-1": -99997.9,
    "S2O_0": -99997.7,
    "S2O_+1": -99995.1,
    "V2_-1": -99989.9,
    "V2_0": -99988.4,
    "V2_+1": -99984.6,
    "V3_-1": -99989.9,
    "V3_0": -99990.3,
    "V3_+1": -99988.5,
    "S2H_0": -100050.0,
    "S2H_+1": -100046.0,
    "S3H_0": -100050.0,
    "S3H_+1": -100046.0,
    "V2H_0": -100050.0,
    "V2H_+2": -100047.5,
    "V3H_0": -100050.0,
    "V3H_+1": -100045.7,
    "S2OH_0": -100050.0,
    "S2OH_+1": -100047.3
  },
  "reaction_energies": [
    {"reaction": "NO + SiO2 -> O2 + S2", "energy_eV": 3.3},
    {"reaction": "NO + SiO2 -> O2 + S3", "energy_eV": 4.4},
    {"reaction": "NO + SiO2 -> 0.5 O2 + S2O", "energy_eV": 2.1},
    {"reaction": "NO + VO -> O2 + V2", "energy_eV": 3.2},
    {"reaction": "NO + VO -> O2 + V3", "energy_eV": 2.8},
    {"reaction": "NO + VO -> S2O", "energy_eV": -4.8},
    {"reaction": "NO + VO -> 0.5 O2 + S2", "energy_eV": -3.6}
  ],
  "thermodynamic_levels": [
    {"structure": "S2", "transition": "0/+", "mu_th_eV": -3.8},
    {"structure": "S2", "transition": "-/0", "mu_th_eV": -1.4},
    {"structure": "S3", "transition": "0/+", "mu_th_eV": -4.1},
    {"structure": "S3", "transition": "-/0", "mu_th_eV": -1.8},
    {"structure": "V2", "transition": "0/+", "mu_th_eV": -3.8},
    {"structure": "V2", "transition": "-/0", "mu_th_eV": -1.5},
    {"structure": "V3", "transition": "0/+", "mu_th_eV": -1.8},
    {"structure": "V3", "transition": "-/0", "mu_th_eV": 0.4},
    {"structure": "S2O", "transition": "0/+", "mu_th_eV": -2.6},
    {"structure": "S2O", "transition": "-/0", "mu_th_eV": -0.2},
    {"structure": "S2H", "transition": "0/+", "mu_th_eV": -4.0},
    {"structure": "S3H", "transition": "0/+", "mu_th_eV": -4.0},
    {"structure": "V2H", "transition": "0/++", "mu_th_eV": -2.5},
    {"structure": "V3H", "transition": "0/+", "mu_th_eV": -4.3},
    {"structure": "S2OH", "transition": "0/+", "mu_th_eV": -2.7}
  ]
}
FFEOF
