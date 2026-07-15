#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: step_01_adsorption_energies_gas.json ===
cat > "$OUTDIR/step_01_adsorption_energies_gas.json" <<'FFEOF'
[
  {
    "metal": "Pt",
    "configuration_name": "II-Bri-A1",
    "E_ad_vac": -2.91
  },
  {
    "metal": "Pt",
    "configuration_name": "I-Bri-A2",
    "E_ad_vac": -2.78
  },
  {
    "metal": "Pt",
    "configuration_name": "II-Fcc-B1",
    "E_ad_vac": -2.71
  },
  {
    "metal": "Pt",
    "configuration_name": "II-Hcp-B1",
    "E_ad_vac": -2.67
  },
  {
    "metal": "Pt",
    "configuration_name": "I-Fcc-B1",
    "E_ad_vac": -2.55
  },
  {
    "metal": "Pt",
    "configuration_name": "I-Hcp-B1",
    "E_ad_vac": -2.55
  },
  {
    "metal": "Pt",
    "configuration_name": "I-Fcc-A2",
    "E_ad_vac": -2.48
  },
  {
    "metal": "Pd",
    "configuration_name": "II-Bri-A2",
    "E_ad_vac": -2.73
  },
  {
    "metal": "Pd",
    "configuration_name": "I-Bri-A2",
    "E_ad_vac": -2.58
  },
  {
    "metal": "Pd",
    "configuration_name": "II-Fcc-B1",
    "E_ad_vac": -2.63
  },
  {
    "metal": "Pd",
    "configuration_name": "II-Hcp-B1",
    "E_ad_vac": -2.59
  },
  {
    "metal": "Pd",
    "configuration_name": "I-Fcc-B1",
    "E_ad_vac": -2.53
  },
  {
    "metal": "Pd",
    "configuration_name": "I-Hcp-B1",
    "E_ad_vac": -2.45
  },
  {
    "metal": "Pd",
    "configuration_name": "I-Hcp-A2",
    "E_ad_vac": -2.43
  }
]
FFEOF

trap 'cat > "$OUTDIR/step_02_structural_params_gas.json" <<'"'"'FFEOF2'"'"'
{
  "Pt": {
    "d_zmin": 1.94,
    "d_zavg": 2.16,
    "r_C1": 1.49,
    "r_C2": 1.44,
    "r_M1": 2.86,
    "r_M2": 3.10,
    "r_CM1": 2.16,
    "r_CM2": 2.16,
    "r_CM3": 2.30,
    "theta1": 113.9,
    "theta2": 122.5,
    "alpha": 104.4,
    "beta": 108.7
  },
  "Pd": {
    "d_zmin": 1.97,
    "d_zavg": 2.15,
    "r_C1": 1.46,
    "r_C2": 1.44,
    "r_M1": 2.80,
    "r_M2": 2.96,
    "r_CM1": 2.17,
    "r_CM2": 2.20,
    "r_CM3": 2.24,
    "theta1": 115.4,
    "theta2": 122.5,
    "alpha": 95.8,
    "beta": 102.3
  }
}
FFEOF2
cat > "$OUTDIR/step_03_aqueous_0K_results.json" <<'"'"'FFEOF3'"'"'
{
  "Pt": {
    "E_ad_aquo_0K": -2.22,
    "d_zmin": 1.85,
    "d_zavg": 2.08,
    "r_C1": 1.50,
    "r_C2": 1.44,
    "r_M1": 2.84,
    "r_M2": 3.03,
    "r_CM1": 2.12,
    "r_CM2": 2.16,
    "r_CM3": 2.30,
    "theta1": 119.4,
    "theta2": 120.3,
    "alpha": 111.9,
    "beta": 111.2
  },
  "Pd": {
    "E_ad_aquo_0K": -2.12,
    "d_zmin": 1.88,
    "d_zavg": 2.06,
    "r_C1": 1.47,
    "r_C2": 1.43,
    "r_M1": 2.80,
    "r_M2": 2.97,
    "r_CM1": 2.13,
    "r_CM2": 2.15,
    "r_CM3": 2.22,
    "theta1": 121,
    "theta2": 120,
    "alpha": 99.3,
    "beta": 97.3
  }
}
FFEOF3
' EXIT

# === solve block: step_02_structural_params_gas.json ===
cat > "$OUTDIR/step_02_structural_params_gas.json" <<'FFEOF'
{
  "Pt": {
    "d_zmin": 1.94,
    "d_zavg": 2.16,
    "r_C1": 1.49,
    "r_C2": 1.44,
    "r_M1": 2.86,
    "r_M2": 3.10,
    "r_CM1": 2.16,
    "r_CM2": 2.16,
    "r_CM3": 2.30,
    "theta1": 113.9,
    "theta2": 122.5,
    "alpha": 104.4,
    "beta": 108.7
  },
  "Pd": {
    "d_zmin": 1.97,
    "d_zavg": 2.15,
    "r_C1": 1.46,
    "r_C2": 1.44,
    "r_M1": 2.80,
    "r_M2": 2.96,
    "r_CM1": 2.17,
    "r_CM2": 2.20,
    "r_CM3": 2.24,
    "theta1": 115.4,
    "theta2": 122.5,
    "alpha": 95.8,
    "beta": 102.3
  }
}
FFEOF

# === solve block: step_03_aqueous_0K_results.json ===
cat > "$OUTDIR/step_03_aqueous_0K_results.json" <<'FFEOF'
{
  "Pt": {
    "E_ad_aquo_0K": -2.22,
    "d_zmin": 1.85,
    "d_zavg": 2.08,
    "r_C1": 1.50,
    "r_C2": 1.44,
    "r_M1": 2.84,
    "r_M2": 3.03,
    "r_CM1": 2.12,
    "r_CM2": 2.16,
    "r_CM3": 2.30,
    "theta1": 119.4,
    "theta2": 120.3,
    "alpha": 111.9,
    "beta": 111.2
  },
  "Pd": {
    "E_ad_aquo_0K": -2.12,
    "d_zmin": 1.88,
    "d_zavg": 2.06,
    "r_C1": 1.47,
    "r_C2": 1.43,
    "r_M1": 2.80,
    "r_M2": 2.97,
    "r_CM1": 2.13,
    "r_CM2": 2.15,
    "r_CM3": 2.22,
    "theta1": 121,
    "theta2": 120,
    "alpha": 99.3,
    "beta": 97.3
  }
}
FFEOF
