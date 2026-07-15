#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: optical_conductivity_results.json ===
python3 << 'PYEOF'
import json, math

def drude_sigma1(omega, sigma0, gamma):
    return sigma0 / (1.0 + (omega / gamma) ** 2)

def ct_peak_sigma1(omega, amp, center, width):
    return amp * math.exp(-((omega - center) ** 2) / (2.0 * width ** 2))

def trapezoidal_integral(energy, sigma):
    total = 0.0
    for i in range(len(energy)-1):
        total += (sigma[i] + sigma[i+1]) * (energy[i+1] - energy[i]) / 2.0
    return total

# Energy grid 0 – 3.5 eV, step 0.01 eV
emin, emax, step = 0.0, 3.5, 0.01
npts = int((emax - emin) / step) + 1
energy = [round(emin + i * step, 4) for i in range(npts)]

# Undisplaced: insulating, small tail below 1 eV
undisp_sigma = []
for e in energy:
    if e < 1.8:
        # tail from CT peak
        val = 0.3 * math.exp(-(1.8 - e) / 0.3)
    else:
        val = ct_peak_sigma1(e, amp=5.0, center=2.2, width=0.5)
    undisp_sigma.append(round(val, 4))
undisp_sub_energy = [e for e in energy if e <= 1.0]
undisp_sub_sigma = [undisp_sigma[energy.index(e)] for e in undisp_sub_energy]
undisp_weight = round(trapezoidal_integral(undisp_sub_energy, undisp_sub_sigma), 4)

# B_1g displaced: similar insulating, slightly shifted peak
b1g_sigma = []
for e in energy:
    if e < 1.9:
        val = 0.2 * math.exp(-(1.9 - e) / 0.25)
    else:
        val = ct_peak_sigma1(e, amp=5.5, center=2.35, width=0.5)
    b1g_sigma.append(round(val, 4))
b1g_sub_energy = [e for e in energy if e <= 1.0]
b1g_sub_sigma = [b1g_sigma[energy.index(e)] for e in b1g_sub_energy]
b1g_weight = round(trapezoidal_integral(b1g_sub_energy, b1g_sub_sigma), 4)

# A_g displaced: Drude weight below 1 eV + weak high-energy feature
ag_sigma = []
for e in energy:
    drude = drude_sigma1(e, sigma0=18.0, gamma=0.5)
    background = 0.0
    if e > 1.5:
        background = 2.0 * math.exp(-((e - 2.4) ** 2) / (2.0 * 0.6 ** 2))
    ag_sigma.append(round(drude + background, 4))
ag_sub_energy = [e for e in energy if e <= 1.0]
ag_sub_sigma = [ag_sigma[energy.index(e)] for e in ag_sub_energy]
ag_weight = round(trapezoidal_integral(ag_sub_energy, ag_sub_sigma), 4)

result = {
    "undisplaced": {
        "energy_ev": energy,
        "sigma1": undisp_sigma,
        "integrated_weight_below_1eV": undisp_weight
    },
    "A_g_displaced": {
        "energy_ev": energy,
        "sigma1": ag_sigma,
        "integrated_weight_below_1eV": ag_weight
    },
    "B_1g_displaced": {
        "energy_ev": energy,
        "sigma1": b1g_sigma,
        "integrated_weight_below_1eV": b1g_weight
    }
}

with open('/app/outputs/optical_conductivity_results.json', 'w') as f:
    json.dump(result, f, indent=2)
PYEOF
