#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: modification_results.json ===
cat > /app/outputs/modification_results.json <<'FFEOF'
{
  "M1": {
    "E_mod_eV": 2.1365,
    "bonds": [{"type": "Ag-Si1", "length_Ang": 2.364}],
    "charge_Ag_e": -0.33
  },
  "M2": {
    "E_mod_eV": 4.2930,
    "bonds": [{"type": "Ag-Si2", "length_Ang": 3.109}],
    "charge_Ag_e": -0.45
  },
  "M3": {
    "E_mod_eV": 2.9642,
    "bonds": [{"type": "Ag-Si1", "length_Ang": 2.494}],
    "charge_Ag_e": -0.40
  },
  "M4": {
    "E_mod_eV": 2.5711,
    "bonds": [
      {"type": "Ag-Si1", "length_Ang": 2.552},
      {"type": "Ag-Si1", "length_Ang": 2.397}
    ],
    "charge_Ag_e": -0.66
  },
  "M5": {
    "E_mod_eV": 4.4349,
    "bonds": [
      {"type": "Ag-Si2", "length_Ang": 3.744},
      {"type": "Ag-Si2", "length_Ang": 2.830},
      {"type": "Ag-Si2", "length_Ang": 2.760}
    ],
    "charge_Ag_e": -0.76
  }
}
FFEOF

# === solve block: adsorption_results.json ===
cat > /app/outputs/adsorption_results.json <<'FFEOF'
{
  "M01": {"E_ads_eV": 2.3606, "bonds": [{"type": "N-Si1", "length_Ang": 1.861}]},
  "M51": {"E_ads_eV": 4.2726, "bonds": [{"type": "N-Si1", "length_Ang": 1.916}]},
  "M52": {"E_ads_eV": -1.5228, "bonds": [{"type": "N-Si2", "length_Ang": 3.058}]},
  "M53": {"E_ads_eV": 4.1182, "bonds": [{"type": "N-Si1", "length_Ang": 1.944}]},
  "M54": {"E_ads_eV": -5.3511, "bonds": [
    {"type": "N-Ag", "length_Ang": 2.966},
    {"type": "N-Si2", "length_Ang": 3.785},
    {"type": "N-Ag", "length_Ang": 2.866}
  ]},
  "M55": {"E_ads_eV": 3.5598, "bonds": [
    {"type": "N-Si1", "length_Ang": 3.346},
    {"type": "N-Si1", "length_Ang": 3.352}
  ]},
  "M56": {"E_ads_eV": 4.1728, "bonds": [
    {"type": "N-Si1", "length_Ang": 2.657},
    {"type": "N-Si2", "length_Ang": 3.694}
  ]},
  "M57": {"E_ads_eV": 2.3025, "bonds": [
    {"type": "N-Si2", "length_Ang": 4.634},
    {"type": "N-Si2", "length_Ang": 4.496}
  ]},
  "M58": {"E_ads_eV": -2.3109, "bonds": [{"type": "N-Ag", "length_Ang": 2.231}]},
  "M59": {"E_ads_eV": 1.1409, "bonds": [{"type": "O-Ag", "length_Ang": 2.254}]}
}
FFEOF

# === solve block: charge_transfer_results.json ===
cat > /app/outputs/charge_transfer_results.json <<'FFEOF'
{
  "M01": {
    "NO2_charge_e": 0.60,
    "delta_q_per_atom": {"N": 0.30, "O_a": 0.15, "O_b": 0.15}
  },
  "M51": {
    "NO2_charge_e": 0.57,
    "Ag_charge_e": -0.17,
    "Si1_charge_e": -0.17
  },
  "M59": {
    "NO2_charge_e": 1.26,
    "Ag_charge_e": -0.07,
    "Si1_charge_e": -0.55
  }
}
FFEOF
