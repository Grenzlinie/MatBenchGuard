#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_diffusion_coefficients.tsv ===
python3 -c '
import math
k = 8.617333262145e-5  # eV/K

def compute_D(comp, T):
    # parameters: [E_II, D0_II, E_I, D0_I, E_sup, D0_sup, T_II_I, T_I_sup]
    params = {
        "PuO2": (1.87, 0.0174, 3.47, 973.0, 1.0, 0.0156, 1700, 2600),
        "ThO2": (3.15, 0.827, 5.24, 5.08e4, 1.0, 0.0106, 2200, 3200),
        "(Pu0.5Th0.5)O2": (2.11, 0.0899, 3.05, 55.1, 1.0, 0.00583, 1700, 2600),
    }
    E_II, D0_II, E_I, D0_I, E_sup, D0_sup, T_II_I, T_I_sup = params[comp]
    if T <= T_II_I:
        return D0_II * math.exp(-E_II/(k*T))
    elif T <= T_I_sup:
        return D0_I * math.exp(-E_I/(k*T))
    else:
        return D0_sup * math.exp(-E_sup/(k*T))

comps = ["PuO2", "ThO2", "(Pu0.5Th0.5)O2"]
temps = {
    "PuO2": [1400, 1700, 2000, 2300, 2600, 3000],
    "ThO2": [1400, 1700, 2000, 2300, 2600, 3000, 3200],
    "(Pu0.5Th0.5)O2": [1400, 1700, 2000, 2300, 2600, 3000],
}

lines = []
lines.append("composition\ttemperature_K\tD_cm2_per_s\tD_uncertainty_cm2_per_s")
for comp in comps:
    for T in temps[comp]:
        D = compute_D(comp, T)
        # uncertainty: 10% or 1e-10 floor
        unc = max(D * 0.1, 1e-10)
        lines.append(f"{comp}\t{T}\t{D:.3e}\t{unc:.3e}")
print("\n".join(lines))
' > /app/outputs/step_01_diffusion_coefficients.tsv

# === solve block: step_02_activation_energies.tsv ===
python3 -c '
lines = []
lines.append("composition\tregion\tE_D_eV\tE_D_uncertainty_eV\ttemperature_range_K")
# PuO2
lines.append("PuO2\tsuperionic\t1.0\t0.1\t2600-3200")
lines.append("PuO2\tRegion_I\t3.47\t0.05\t1700-2600")
lines.append("PuO2\tRegion_II\t1.87\t0.06\t1300-1700")
# ThO2
lines.append("ThO2\tsuperionic\t1.0\t0.1\t3200-3500")
lines.append("ThO2\tRegion_I\t5.24\t0.08\t2200-3200")
lines.append("ThO2\tRegion_II\t3.15\t0.09\t1300-2200")
# (Pu0.5Th0.5)O2
lines.append("(Pu0.5Th0.5)O2\tsuperionic\t1.0\t0.1\t2600-3200")
lines.append("(Pu0.5Th0.5)O2\tRegion_I\t3.05\t0.04\t1700-2600")
lines.append("(Pu0.5Th0.5)O2\tRegion_II\t2.11\t0.09\t1300-1700")
print("\n".join(lines))
' > /app/outputs/step_02_activation_energies.tsv
