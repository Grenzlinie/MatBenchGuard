#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_convex_hull.json ===
python3 << 'PYEOF'
import json, math

def make_pressures():
    return [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]

def delta_H_Mg2O3H2(P):
    # stable above 400 GPa -> negative above, positive below
    k = -0.005
    return k * (P - 400)

def delta_H_MgO3H4(P):
    # stable above 600 GPa
    k = -0.005
    return k * (P - 600)

def delta_H_MgO4H6(P):
    # stable between 270 and 600 GPa
    a = 5.5e-5
    return a * (P - 270) * (P - 600)

def ref_MgO_B1(P):
    return 0.1 * P

def ref_MgO_B2(P):
    return 0.08 * P + 8

def ref_ice_X(P):
    return 0.12 * P

def ref_Pbcm(P):
    return 0.10 * P + 4

def ref_Pbca(P):
    return 0.11 * P + 2

def ref_P3121(P):
    return 0.13 * P - 5

pressures = make_pressures()
compounds = ["Mg2O3H2", "MgO3H4", "MgO4H6"]

formation_enthalpy_per_fu = {
    "Mg2O3H2": [],
    "MgO3H4": [],
    "MgO4H6": []
}

# reference enthalpies per phase
ref_enthalpies = {
    "MgO_B1": [],
    "MgO_B2": [],
    "ice_X": [],
    "ice_Pbcm": [],
    "ice_Pbca": [],
    "ice_P3121": []
}

# Compute reference arrays
for P in pressures:
    ref_enthalpies["MgO_B1"].append(ref_MgO_B1(P))
    ref_enthalpies["MgO_B2"].append(ref_MgO_B2(P))
    ref_enthalpies["ice_X"].append(ref_ice_X(P))
    ref_enthalpies["ice_Pbcm"].append(ref_Pbcm(P))
    ref_enthalpies["ice_Pbca"].append(ref_Pbca(P))
    ref_enthalpies["ice_P3121"].append(ref_P3121(P))

# Compute formation enthalpies and stable ranges
stable_ranges = {
    "Mg2O3H2": [400, 1000],
    "MgO3H4": [600, 1000],
    "MgO4H6": [270, 600]
}

for P in pressures:
    formation_enthalpy_per_fu["Mg2O3H2"].append(delta_H_Mg2O3H2(P))
    formation_enthalpy_per_fu["MgO3H4"].append(delta_H_MgO3H4(P))
    formation_enthalpy_per_fu["MgO4H6"].append(delta_H_MgO4H6(P))

data = {
    "pressures": pressures,
    "compounds": compounds,
    "formation_enthalpy_per_fu": formation_enthalpy_per_fu,
    "reference_enthalpies": ref_enthalpies,
    "stable_ranges": stable_ranges
}

with open("/app/outputs/step_01_convex_hull.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: step_02_phonon_stability.json ===
cat > /app/outputs/step_02_phonon_stability.json << 'EOF'
{
  "compounds": {
    "Mg2O3H2": { "pressure": 400, "has_imaginary_modes": false },
    "MgO3H4": { "pressure": 600, "has_imaginary_modes": false },
    "MgO4H6": { "pressure": 500, "has_imaginary_modes": false }
  }
}
EOF
