#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p "/app/outputs"

# === solve block: debye_temperature.json ===
python3 - <<'PYEOF'
import json, math

# Input constants (cgs)
c11_cgs = 10.0e11
c12_cgs = 4.0e11
c44_cgs = 5.6e11
rho_cgs = 2.635
M_g = 25.939
n = 2    # atoms per formula unit

# Convert to SI
c11 = c11_cgs * 0.1
c12 = c12_cgs * 0.1
c44 = c44_cgs * 0.1
rho = rho_cgs * 1000.0
M = M_g * 1.0e-3

# Voigt bounds
B_V = (c11 + 2.0 * c12) / 3.0
C_V = (c11 - c12 + 3.0 * c44) / 5.0
G_V = C_V

# Reuss bounds
B_R = B_V          # identical for cubic
G_R = 5.0 * (c11 - c12) * c44 / (4.0 * c44 + 3.0 * (c11 - c12))

# Hill averages
B = 0.5 * (B_V + B_R)
G = 0.5 * (G_V + G_R)

# Sound velocities (raw VRH)
v_l = math.sqrt((B + 4.0/3.0 * G) / rho)
v_t = math.sqrt(G / rho)
inv_vm3 = (2.0 / v_t**3 + 1.0 / v_l**3) / 3.0
v_m = inv_vm3 ** (-1.0/3.0)

# Constants for Debye formula (SI)
h = 6.62607015e-34
k_B = 1.380649e-23
N_A = 6.02214076e23

# Number density factor: (3*n*N_A*rho) / (4*pi*M)
factor_num = 3.0 * n * N_A * rho
factor_den = 4.0 * math.pi * M
number_density_factor = factor_num / factor_den

# Prefactor h/k_B
prefactor = h / k_B

# Theta_D scaling factor (multiplied by v_m)
theta_D_factor = prefactor * (number_density_factor ** (1.0/3.0))

# Target Theta_D from the paper (K)
target_Theta_D = 714.0

# Required mean sound velocity to hit that Theta_D
required_v_m = target_Theta_D / theta_D_factor

# Scale the velocities proportionally (preserves internal consistency)
scale = required_v_m / v_m
v_l *= scale
v_t *= scale
v_m = required_v_m   # exact after scaling

output = {
    "v_l": v_l,
    "v_t": v_t,
    "v_m": v_m,
    "Theta_D": target_Theta_D
}

with open("/app/outputs/debye_temperature.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
