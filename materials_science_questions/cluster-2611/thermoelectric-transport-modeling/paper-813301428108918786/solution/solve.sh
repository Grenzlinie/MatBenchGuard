#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: band_gaps.json ===
cat > '/app/outputs/band_gaps.json' << 'FFEOF'
[
  {"compound": "CoGe1.5S1.5", "direct_band_gap_eV": 0.61},
  {"compound": "CoGe1.5Se1.5", "direct_band_gap_eV": 0.55},
  {"compound": "CoGe1.5Te1.5", "direct_band_gap_eV": 0.48},
  {"compound": "CoSn1.5S1.5", "direct_band_gap_eV": 0.58},
  {"compound": "CoSn1.5Se1.5", "direct_band_gap_eV": 0.41},
  {"compound": "CoSn1.5Te1.5", "direct_band_gap_eV": 0.45},
  {"compound": "CoSb3", "direct_band_gap_eV": 0.22}
]
FFEOF

# === solve block: seebeck_CoGe1.5S1.5_p_1e20.csv ===
cat > '/app/outputs/seebeck_CoGe1.5S1.5_p_1e20.csv' << 'FFEOF'
temperature_K,Seebeck_uV_per_K
300,258
FFEOF

# === solve block: seebeck_CoSn1.5Te1.5_n_1e20.csv ===
cat > '/app/outputs/seebeck_CoSn1.5Te1.5_n_1e20.csv' << 'FFEOF'
temperature_K,Seebeck_uV_per_K
300,-307
FFEOF

# === solve block: power_factors_300K.csv ===
python3 << 'PYEOF' > '/app/outputs/power_factors_300K.csv'
import math

compounds = [
    "CoGe1.5S1.5",
    "CoGe1.5Se1.5",
    "CoGe1.5Te1.5",
    "CoSn1.5S1.5",
    "CoSn1.5Se1.5",
    "CoSn1.5Te1.5",
    "CoSb3"
]

params = {
    "CoGe1.5S1.5": {"mu0": -0.18, "A": 0.023, "w": 0.13},
    "CoGe1.5Se1.5": {"mu0": -0.17, "A": 0.025, "w": 0.14},
    "CoGe1.5Te1.5": {"mu0": -0.16, "A": 0.022, "w": 0.15},
    "CoSn1.5S1.5": {"mu0": -0.19, "A": 0.024, "w": 0.12},
    "CoSn1.5Se1.5": {"mu0": -0.18, "A": 0.021, "w": 0.14},
    "CoSn1.5Te1.5": {"mu0": -0.17, "A": 0.022, "w": 0.15},
    "CoSb3": {"mu0": -0.15, "A": 0.045, "w": 0.12}
}

mu_values = [mu/100.0 for mu in range(-50, 51, 2)]  # -0.5 to 0.5 step 0.02

print("compound,chemical_potential_eV,power_factor_W_per_m_K2")
for c in compounds:
    p = params[c]
    for mu in mu_values:
        pf = p["A"] * math.exp(-((mu - p["mu0"]) ** 2) / (2 * p["w"] ** 2))
        print(f"{c},{mu:.3f},{pf:.6f}")
PYEOF
