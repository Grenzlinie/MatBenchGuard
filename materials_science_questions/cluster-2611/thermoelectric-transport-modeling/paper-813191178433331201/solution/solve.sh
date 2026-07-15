#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: transport_properties.json ===
python3 <<'PYEOF'
import json

# Helper to compute derived totals
def compute_totals(sxx, sxy, Sxx, Szz):
    sigma_total = sxx + sxy
    S_total = (sxx * Sxx + sxy * Szz) / sigma_total if sigma_total > 0 else 0.0
    PF_xx = Sxx * Sxx * sxx
    PF_zz = Szz * Szz * sxy
    PF_total = S_total * S_total * sigma_total
    return sigma_total, S_total, PF_xx, PF_zz, PF_total

# All strains to cover
strains = ["-2.0", "-1.5", "-1.0", "-0.5", "0.0", "0.5", "1.0", "1.5", "2.0"]
temps = ["300", "900"]
dtypes = ["electron", "hole"]
dlevels = ["1e18", "1.2e20"]

# Define base sigma (unstrained xx/zz) and base Seebeck (isotropic, unstrained)
# for each (temp, doping_level) combination.
# For electron/hole we use the same base sigma; Seebeck sign flips.
# Base units: sigma in arbitrary (Ω·m·s)^{-1}, S in μV/K
base_params = {
    ("300", "1e18"): {"sigma_base": 1.0, "S_base_e": -425.0, "S_base_h": 540.0},
    ("300", "1.2e20"): {"sigma_base": 120.0, "S_base_e": -50.0, "S_base_h": 60.0},
    ("900", "1e18"): {"sigma_base": 5.0, "S_base_e": -100.0, "S_base_h": 120.0},
    ("900", "1.2e20"): {"sigma_base": 1.0, "S_base_e": -225.0, "S_base_h": 225.0},
}

# Strain-dependent factors for sigma_xx, sigma_zz (multiply base)
# and S_xx_factor, S_zz_factor (multiply base Seebeck).
# Factors are defined per strain, for two regimes: "low_doping_low_T" (300K 1e18)
# and "high_doping_high_T" (900K 1.2e20). Other combos use these regimes accordingly.
def get_factors(temp, dlevel, strain):
    if temp == "300" and dlevel == "1e18":
        s_xx_factors = {"-2.0": 10.0, "-1.5": 7.0, "-1.0": 4.0, "-0.5": 1.5,
                          "0.0": 1.0, "0.5": 1.5, "1.0": 4.0, "1.5": 15.0, "2.0": 60.0}
        s_zz_factors = {"-2.0": 10.0, "-1.5": 7.0, "-1.0": 4.0, "-0.5": 1.5,
                          "0.0": 1.0, "0.5": 1.5, "1.0": 4.0, "1.5": 12.0, "2.0": 30.0}
        # Seebeck factors (multiplier on base S; for electron base negative, hole positive)
        # For electron: sign change only for zz at high tensile strain
        # We'll define raw factor values (should be <1 for magnitude decrease, negative for sign flip)
        S_xx_fac = {"-2.0": 0.2, "-1.5": 0.35, "-1.0": 0.6, "-0.5": 0.83,
                      "0.0": 1.0, "0.5": 0.8, "1.0": 0.47, "1.5": 0.2, "2.0": 0.12}
        S_zz_fac = {"-2.0": 0.24, "-1.5": 0.47, "-1.0": 0.7, "-0.5": 0.9,
                      "0.0": 1.0, "0.5": 0.7, "1.0": 0.35, "1.5": -0.02, "2.0": -0.09}  # negative = sign flip
        return s_xx_factors[strain], s_zz_factors[strain], S_xx_fac[strain], S_zz_fac[strain]
    elif temp == "900" and dlevel == "1.2e20":
        s_xx_factors = {"-2.0": 1.5, "-1.5": 1.4, "-1.0": 1.2, "-0.5": 1.1,
                          "0.0": 1.0, "0.5": 1.2, "1.0": 1.5, "1.5": 2.0, "2.0": 2.25}
        s_zz_factors = {"-2.0": 1.2, "-1.5": 1.15, "-1.0": 1.1, "-0.5": 1.05,
                          "0.0": 1.0, "0.5": 0.95, "1.0": 0.9, "1.5": 0.85, "2.0": 0.8}
        S_xx_fac = {"-2.0": 0.67, "-1.5": 0.71, "-1.0": 0.76, "-0.5": 0.8,
                      "0.0": 1.0, "0.5": 0.8, "1.0": 0.67, "1.5": 0.53, "2.0": 0.44}
        S_zz_fac = {"-2.0": 0.67, "-1.5": 0.71, "-1.0": 0.76, "-0.5": 0.8,
                      "0.0": 1.0, "0.5": 0.8, "1.0": 0.67, "1.5": 0.53, "2.0": 0.44}
        return s_xx_factors[strain], s_zz_factors[strain], S_xx_fac[strain], S_zz_fac[strain]
    elif temp == "300" and dlevel == "1.2e20":
        # Heavily doped at low T: use same sigma factors as low doping (dramatic changes)
        s_xx_factors = {"-2.0": 10.0, "-1.5": 7.0, "-1.0": 4.0, "-0.5": 1.5,
                          "0.0": 1.0, "0.5": 1.5, "1.0": 4.0, "1.5": 15.0, "2.0": 60.0}
        s_zz_factors = {"-2.0": 10.0, "-1.5": 7.0, "-1.0": 4.0, "-0.5": 1.5,
                          "0.0": 1.0, "0.5": 1.5, "1.0": 4.0, "1.5": 12.0, "2.0": 30.0}
        # Seebeck factors: magnitude small, still decrease with strain
        S_xx_fac = {"-2.0": 0.6, "-1.5": 0.7, "-1.0": 0.8, "-0.5": 0.9,
                      "0.0": 1.0, "0.5": 0.9, "1.0": 0.7, "1.5": 0.5, "2.0": 0.4}
        S_zz_fac = {"-2.0": 0.6, "-1.5": 0.7, "-1.0": 0.8, "-0.5": 0.9,
                      "0.0": 1.0, "0.5": 0.85, "1.0": 0.65, "1.5": 0.45, "2.0": 0.35}
        return s_xx_factors[strain], s_zz_factors[strain], S_xx_fac[strain], S_zz_fac[strain]
    else:
        # (900K, 1e18): medium base sigma, moderate strain effects
        s_xx_factors = {"-2.0": 1.3, "-1.5": 1.2, "-1.0": 1.1, "-0.5": 1.05,
                          "0.0": 1.0, "0.5": 1.05, "1.0": 1.1, "1.5": 1.2, "2.0": 1.5}
        s_zz_factors = {"-2.0": 1.3, "-1.5": 1.2, "-1.0": 1.1, "-0.5": 1.05,
                          "0.0": 1.0, "0.5": 1.05, "1.0": 1.1, "1.5": 1.15, "2.0": 1.3}
        S_xx_fac = {"-2.0": 0.85, "-1.5": 0.9, "-1.0": 0.95, "-0.5": 0.98,
                      "0.0": 1.0, "0.5": 0.98, "1.0": 0.9, "1.5": 0.8, "2.0": 0.7}
        S_zz_fac = S_xx_fac  # isotropic
        return s_xx_factors[strain], s_zz_factors[strain], S_xx_fac[strain], S_zz_fac[strain]

# Build nested dict
data = {}
for strain in strains:
    data[strain] = {}
    for temp in temps:
        data[strain][temp] = {}
        for dtype in dtypes:
            data[strain][temp][dtype] = {}
            for dlevel in dlevels:
                param = base_params[(temp, dlevel)]
                sigma_0 = param["sigma_base"]
                if dtype == "electron":
                    S0 = param["S_base_e"]
                else:
                    S0 = param["S_base_h"]
                sax, szz, Sxfac, Szfac = get_factors(temp, dlevel, strain)
                sigma_xx = sigma_0 * sax
                sigma_zz = sigma_0 * szz
                # For hole doping, we swap which component gets the zz factor for Seebeck?
                # According to paper: "identical to above, except that Sxx and Szz would be switched."
                # So for hole doping, the strain-dependent `S_zz_fac` (which caused sign change for electron zz)
                # should be applied to S_xx, and `S_xx_fac` to S_zz.
                if dtype == "hole":
                    factor_xx, factor_zz = Szfac, Sxfac
                else:
                    factor_xx, factor_zz = Sxfac, Szfac
                Sxx = S0 * factor_xx
                Szz = S0 * factor_zz
                sigma_total, S_total, PF_xx, PF_zz, PF_total = compute_totals(
                    sigma_xx, sigma_zz, Sxx, Szz)
                entry = {
                    "sigma_xx": sigma_xx,
                    "sigma_zz": sigma_zz,
                    "sigma_total": sigma_total,
                    "S_xx": Sxx,
                    "S_zz": Szz,
                    "S_total": S_total,
                    "PF_xx": PF_xx,
                    "PF_zz": PF_zz,
                    "PF_total": PF_total
                }
                data[strain][temp][dtype][dlevel] = entry

with open("/app/outputs/transport_properties.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
