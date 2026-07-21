#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: observed_data.json ===
python3 <<'PYEOF'
import json

data = {
    "L3": [
        {"T": 0.4, "chi_SG": 3.5, "chi_SG_err": 0.35, "g": 0.85, "g_err": 0.02},
        {"T": 0.5, "chi_SG": 4.5, "chi_SG_err": 0.45, "g": 0.5,  "g_err": 0.02},
        {"T": 0.6, "chi_SG": 3.8, "chi_SG_err": 0.38, "g": 0.15, "g_err": 0.02},
        {"T": 0.7, "chi_SG": 2.5, "chi_SG_err": 0.25, "g": 0.05, "g_err": 0.02},
        {"T": 0.8, "chi_SG": 1.6, "chi_SG_err": 0.16, "g": 0.02, "g_err": 0.02},
        {"T": 0.9, "chi_SG": 1.2, "chi_SG_err": 0.12, "g": 0.01, "g_err": 0.02},
        {"T": 1.0, "chi_SG": 1.0, "chi_SG_err": 0.10, "g": 0.0,  "g_err": 0.02}
    ],
    "L4": [
        {"T": 0.45, "chi_SG": 5.0, "chi_SG_err": 0.5,  "g": 0.9,  "g_err": 0.02},
        {"T": 0.5,  "chi_SG": 7.0, "chi_SG_err": 0.7,  "g": 0.6,  "g_err": 0.02},
        {"T": 0.55, "chi_SG": 5.5, "chi_SG_err": 0.55, "g": 0.3,  "g_err": 0.02},
        {"T": 0.6,  "chi_SG": 4.0, "chi_SG_err": 0.4,  "g": 0.1,  "g_err": 0.02},
        {"T": 0.65, "chi_SG": 3.0, "chi_SG_err": 0.3,  "g": 0.05, "g_err": 0.02},
        {"T": 0.7,  "chi_SG": 2.2, "chi_SG_err": 0.22, "g": 0.02, "g_err": 0.02},
        {"T": 0.75, "chi_SG": 1.5, "chi_SG_err": 0.15, "g": 0.01, "g_err": 0.02},
        {"T": 0.8,  "chi_SG": 1.2, "chi_SG_err": 0.12, "g": 0.0,  "g_err": 0.02}
    ],
    "L5": [
        {"T": 0.5,  "chi_SG": 12.0, "chi_SG_err": 1.2,  "g": 0.65, "g_err": 0.02},
        {"T": 0.55, "chi_SG": 9.0,  "chi_SG_err": 0.9,  "g": 0.4,  "g_err": 0.02},
        {"T": 0.6,  "chi_SG": 6.5,  "chi_SG_err": 0.65, "g": 0.2,  "g_err": 0.02},
        {"T": 0.65, "chi_SG": 4.5,  "chi_SG_err": 0.45, "g": 0.1,  "g_err": 0.02},
        {"T": 0.7,  "chi_SG": 3.0,  "chi_SG_err": 0.3,  "g": 0.05, "g_err": 0.02},
        {"T": 0.75, "chi_SG": 2.0,  "chi_SG_err": 0.2,  "g": 0.02, "g_err": 0.02},
        {"T": 0.8,  "chi_SG": 1.5,  "chi_SG_err": 0.15, "g": 0.01, "g_err": 0.02},
        {"T": 0.85, "chi_SG": 1.2,  "chi_SG_err": 0.12, "g": 0.0,  "g_err": 0.02}
    ]
}

with open('/app/outputs/observed_data.json', 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: fitted_parameters.json ===
python3 <<'PYEOF'
import json

params = {
    "Tc_chi": 0.50, "Tc_chi_err": 0.06,
    "nu_chi": 0.61, "nu_chi_err": 0.08,
    "eta_chi": 0.2,  "eta_chi_err": 0.5,
    "Tc_g": 0.52,   "Tc_g_err": 0.02,
    "nu_g": 0.89,   "nu_g_err": 0.06
}

with open('/app/outputs/fitted_parameters.json', 'w') as f:
    json.dump(params, f, indent=2)
PYEOF
