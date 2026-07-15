#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_values.json ===
python3 -c '
import json, math, os

a_KBr = 6.600
a_KI = 7.066
theta_KBr = 172.0
theta_KI = 132.0
M_KBr = 119.002
M_KI = 166.0028
NA = 6.02214076e23

kbr_fracs = [0.26, 0.50, 0.87]
vol_fracs = [0.43, 0.24, 0.33]

# Vegard lattice constants
a_phases = [x * a_KBr + (1.0 - x) * a_KI for x in kbr_fracs]

# Densities (rocksalt, 4 formula units per cell)
rhos = []
for i, x in enumerate(kbr_fracs):
    a_cm = a_phases[i] * 1e-8
    M = x * M_KBr + (1.0 - x) * M_KI
    density = (4.0 * M) / (NA * a_cm**3)
    rhos.append(density)

# Inverse‑square mixing rule
th_phases = []
for x in kbr_fracs:
    inv = x / (theta_KBr**2) + (1.0 - x) / (theta_KI**2)
    th_phases.append(1.0 / math.sqrt(inv) if inv > 0 else 0.0)

# Effective Debye temperature
rho_avg = sum(v * r for v, r in zip(vol_fracs, rhos))
c_sum = sum(v * r / t**3 for v, r, t in zip(vol_fracs, rhos, th_phases))
theta_eff = (rho_avg / c_sum) ** (1.0 / 3.0)

output = {
    "phase_compositions": kbr_fracs,
    "volume_fractions": vol_fracs,
    "phase_lattice_constants_A": a_phases,
    "phase_densities_g_per_cc": rhos,
    "phase_theta_D_K": th_phases,
    "theta_D_effective_K": theta_eff
}

os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/computed_values.json", "w") as f:
    json.dump(output, f, indent=2)
'
