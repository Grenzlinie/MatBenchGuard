#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: structural_params.json ===
python3 << 'PYEOF'
import json

data_2x2 = {
  "pristine": {"a": 8.282, "d_range": [2.886, 2.887], "d_prime": None, "h": None},
  "Cr-doped": {"a": 8.125, "d_range": [2.841, 2.906], "d_prime": 2.598, "h": 1.271},
  "Cu-doped": {"a": 8.207, "d_range": [2.841, 2.855], "d_prime": 2.621, "h": 0.762},
  "Sc-doped": {"a": 8.206, "d_range": [2.867, 2.885], "d_prime": 2.882, "h": 1.634},
  "Fe-doped": {"a": 8.083, "d_range": [2.841, 2.894], "d_prime": 2.541, "h": 1.193},
  "Ni-doped": {"a": 8.042, "d_range": [2.832, 2.868], "d_prime": 2.547, "h": 1.155},
  "V-doped": {"a": 8.125, "d_range": [2.844, 2.889], "d_prime": 2.678, "h": 1.373},
  "Zn-doped": {"a": 8.360, "d_range": [2.858, 2.890], "d_prime": 2.664, "h": 0.559},
  "Ti-doped": {"a": 8.132, "d_range": [2.843, 2.892], "d_prime": 2.753, "h": 1.509}
}

data_3x3 = {
  "pristine": {"a": 12.423, "d_range": [2.886, 2.888], "d_prime": None, "h": None},
  "Cr-doped": {"a": 12.285, "d_range": [2.866, 2.908], "d_prime": 2.598, "h": 1.233},
  "Cu-doped": {"a": 12.187, "d_range": [2.825, 2.903], "d_prime": 2.599, "h": 0.799},
  "Sc-doped": {"a": 12.333, "d_range": [2.867, 2.897], "d_prime": 2.877, "h": 1.591},
  "Fe-doped": {"a": 12.262, "d_range": [2.863, 2.905], "d_prime": 2.539, "h": 1.161},
  "Ni-doped": {"a": 12.212, "d_range": [2.859, 2.898], "d_prime": 2.548, "h": 1.158},
  "V-doped": {"a": 12.324, "d_range": [2.871, 2.899], "d_prime": 2.664, "h": 1.287},
  "Zn-doped": {"a": 12.406, "d_range": [2.840, 2.897], "d_prime": 2.646, "h": 0.596},
  "Ti-doped": {"a": 12.236, "d_range": [2.860, 2.881], "d_prime": 2.756, "h": 1.435}
}

result = {"2x2": data_2x2, "3x3": data_3x3}
with open("/app/outputs/structural_params.json", "w") as f:
    json.dump(result, f, indent=2)
print("structural_params.json written")
PYEOF

# === solve block: youngs_moduli.json ===
python3 << 'PYEOF'
import json

data_2x2 = {
  "pristine": {"longitudinal_Y": 41.54, "transverse_Y": 41.55, "long_reduction_percent": 0.0, "trans_reduction_percent": 0.0},
  "Cr-doped": {"longitudinal_Y": 16.15, "transverse_Y": 16.20, "long_reduction_percent": -61.12, "trans_reduction_percent": -60.99},
  "Cu-doped": {"longitudinal_Y": 24.78, "transverse_Y": 24.85, "long_reduction_percent": -40.34, "trans_reduction_percent": -40.19},
  "Sc-doped": {"longitudinal_Y": 21.67, "transverse_Y": 21.89, "long_reduction_percent": -47.82, "trans_reduction_percent": -47.31},
  "Fe-doped": {"longitudinal_Y": 27.66, "transverse_Y": 27.58, "long_reduction_percent": -33.42, "trans_reduction_percent": -33.61},
  "Ni-doped": {"longitudinal_Y": 30.98, "transverse_Y": 31.01, "long_reduction_percent": -25.41, "trans_reduction_percent": -25.37},
  "V-doped": {"longitudinal_Y": 25.89, "transverse_Y": 25.88, "long_reduction_percent": -37.66, "trans_reduction_percent": -37.71},
  "Zn-doped": {"longitudinal_Y": 26.82, "transverse_Y": 26.58, "long_reduction_percent": -35.43, "trans_reduction_percent": -36.03},
  "Ti-doped": {"longitudinal_Y": 20.85, "transverse_Y": 20.80, "long_reduction_percent": -49.80, "trans_reduction_percent": -49.93}
}

data_3x3 = {
  "pristine": {"longitudinal_Y": 41.77, "transverse_Y": 41.81, "long_reduction_percent": 0.0, "trans_reduction_percent": 0.0},
  "Cr-doped": {"longitudinal_Y": 30.42, "transverse_Y": 30.47, "long_reduction_percent": -27.18, "trans_reduction_percent": -27.12},
  "Cu-doped": {"longitudinal_Y": 29.69, "transverse_Y": 30.17, "long_reduction_percent": -28.91, "trans_reduction_percent": -27.83},
  "Sc-doped": {"longitudinal_Y": 31.50, "transverse_Y": 31.51, "long_reduction_percent": -24.60, "trans_reduction_percent": -24.62},
  "Fe-doped": {"longitudinal_Y": 35.76, "transverse_Y": 35.80, "long_reduction_percent": -14.38, "trans_reduction_percent": -14.37},
  "Ni-doped": {"longitudinal_Y": 35.49, "transverse_Y": 35.42, "long_reduction_percent": -15.04, "trans_reduction_percent": -15.28},
  "V-doped": {"longitudinal_Y": 17.14, "transverse_Y": 17.20, "long_reduction_percent": -58.97, "trans_reduction_percent": -58.84},
  "Zn-doped": {"longitudinal_Y": 31.85, "transverse_Y": 32.04, "long_reduction_percent": -23.74, "trans_reduction_percent": -23.37},
  "Ti-doped": {"longitudinal_Y": 22.22, "transverse_Y": 22.75, "long_reduction_percent": -46.81, "trans_reduction_percent": -45.58}
}

result = {"2x2": data_2x2, "3x3": data_3x3}
with open("/app/outputs/youngs_moduli.json", "w") as f:
    json.dump(result, f, indent=2)
print("youngs_moduli.json written")
PYEOF

# === solve block: bulk_moduli.json ===
python3 << 'PYEOF'
import json

data_2x2 = {
  "pristine": {"B": 24.25, "reduction_percent": 0.0},
  "Cr-doped": {"B": 12.12, "reduction_percent": -50.00},
  "Cu-doped": {"B": 17.68, "reduction_percent": -27.12},
  "Sc-doped": {"B": 14.60, "reduction_percent": -39.78},
  "Fe-doped": {"B": 17.19, "reduction_percent": -29.14},
  "Ni-doped": {"B": 20.72, "reduction_percent": -14.57},
  "V-doped": {"B": 17.83, "reduction_percent": -26.49},
  "Zn-doped": {"B": 20.76, "reduction_percent": -14.42},
  "Ti-doped": {"B": 12.10, "reduction_percent": -50.11}
}

data_3x3 = {
  "pristine": {"B": 24.28, "reduction_percent": 0.0},
  "Cr-doped": {"B": 19.97, "reduction_percent": -17.76},
  "Cu-doped": {"B": 20.76, "reduction_percent": -14.50},
  "Sc-doped": {"B": 18.81, "reduction_percent": -22.53},
  "Fe-doped": {"B": 21.58, "reduction_percent": -11.12},
  "Ni-doped": {"B": 22.50, "reduction_percent": -7.32},
  "V-doped": {"B": 18.98, "reduction_percent": -21.84},
  "Zn-doped": {"B": 22.64, "reduction_percent": -6.78},
  "Ti-doped": {"B": 18.66, "reduction_percent": -23.15}
}

result = {"2x2": data_2x2, "3x3": data_3x3}
with open("/app/outputs/bulk_moduli.json", "w") as f:
    json.dump(result, f, indent=2)
print("bulk_moduli.json written")
PYEOF

# === solve block: critical_strains.json ===
python3 << 'PYEOF'
import json

data_2x2 = {
  "uniaxial": {
    "pristine": {"eps_c1": 0.15, "eps_c2": 0.57},
    "Cr-doped": {"eps_c1": 0.09, "eps_c2": 0.18},
    "Cu-doped": {"eps_c1": 0.12, "eps_c2": 0.15},
    "Sc-doped": {"eps_c1": 0.21, "eps_c2": 0.27},
    "Fe-doped": {"eps_c1": 0.12, "eps_c2": 0.21},
    "Ni-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "V-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "Zn-doped": {"eps_c1": 0.12, "eps_c2": 0.15},
    "Ti-doped": {"eps_c1": 0.12, "eps_c2": 0.21}
  },
  "biaxial": {
    "pristine": {"eps_c1": 0.24, "eps_c2": 0.27},
    "Cr-doped": {"eps_c1": 0.18, "eps_c2": 0.24},
    "Cu-doped": {"eps_c1": 0.09, "eps_c2": 0.12},
    "Sc-doped": {"eps_c1": 0.27, "eps_c2": 0.33},
    "Fe-doped": {"eps_c1": 0.21, "eps_c2": 0.24},
    "Ni-doped": {"eps_c1": 0.24, "eps_c2": 0.27},
    "V-doped": {"eps_c1": 0.12, "eps_c2": 0.24},
    "Zn-doped": {"eps_c1": 0.12, "eps_c2": 0.21},
    "Ti-doped": {"eps_c1": 0.24, "eps_c2": 0.27}
  }
}

data_3x3 = {
  "uniaxial": {
    "pristine": {"eps_c1": 0.15, "eps_c2": 0.57},
    "Cr-doped": {"eps_c1": 0.09, "eps_c2": 0.12},
    "Cu-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "Sc-doped": {"eps_c1": 0.18, "eps_c2": 0.21},
    "Fe-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "Ni-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "V-doped": {"eps_c1": 0.15, "eps_c2": 0.18},
    "Zn-doped": {"eps_c1": 0.15, "eps_c2": 0.27},
    "Ti-doped": {"eps_c1": 0.18, "eps_c2": 0.21}
  },
  "biaxial": {
    "pristine": {"eps_c1": 0.24, "eps_c2": 0.27},
    "Cr-doped": {"eps_c1": 0.18, "eps_c2": 0.21},
    "Cu-doped": {"eps_c1": 0.12, "eps_c2": 0.15},
    "Sc-doped": {"eps_c1": 0.18, "eps_c2": 0.21},
    "Fe-doped": {"eps_c1": 0.12, "eps_c2": 0.15},
    "Ni-doped": {"eps_c1": 0.18, "eps_c2": 0.21},
    "V-doped": {"eps_c1": 0.18, "eps_c2": 0.21},
    "Zn-doped": {"eps_c1": 0.12, "eps_c2": 0.15},
    "Ti-doped": {"eps_c1": 0.21, "eps_c2": 0.24}
  }
}

result = {"2x2": data_2x2, "3x3": data_3x3}
with open("/app/outputs/critical_strains.json", "w") as f:
    json.dump(result, f, indent=2)
print("critical_strains.json written")
PYEOF
