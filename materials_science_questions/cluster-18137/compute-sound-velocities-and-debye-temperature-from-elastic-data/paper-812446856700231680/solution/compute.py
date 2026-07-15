import json
import math

# Public inputs from the paper and standard references
a_KBr = 6.600   # Å
 a_KI = 7.066    # Å
M_KBr = 119.002   # g/mol
M_KI = 166.0028   # g/mol
N_A = 6.02214076e23  # mol^{-1}
thetaD_KBr = 172.0  # K
thetaD_KI  = 132.0  # K

# Three crystalline phases from Nair & Walker: (KBr fraction, volume fraction)
phases = [
    (0.26, 0.43),
    (0.50, 0.24),
    (0.87, 0.33),
]

lattice_constants = []
densities = []
theta_Ds = []

for x, v in phases:
    # Vegard's law: linear interpolation of lattice constant
    a = x * a_KBr + (1.0 - x) * a_KI

    # Molar mass of the phase
    M = x * M_KBr + (1.0 - x) * M_KI

    # Mass density: rocksalt structure, 4 formula units per conventional cell
    a_cm3 = a**3 * 1e-24          # convert Å^3 to cm^3
    rho = (4.0 * M) / (N_A * a_cm3)

    # Phase Debye temperature via inverse‑square mixing rule
    inv_sq = x / (thetaD_KBr**2) + (1.0 - x) / (thetaD_KI**2)
    theta = 1.0 / math.sqrt(inv_sq)

    lattice_constants.append(round(a, 6))
    densities.append(round(rho, 5))
    theta_Ds.append(round(theta, 3))

# Effective Debye temperature from low‑T heat capacity weighting
# C_V ∝ ρ / θ_D^3   →   volume‑fraction‑weighted average
rho_avg = sum(v * d for (_, v), d in zip(phases, densities))
sum_weighted_heatcap = sum(v * d / (t**3) for (_, v), d, t in zip(phases, densities, theta_Ds))
theta_eff = (rho_avg / sum_weighted_heatcap) ** (1.0 / 3.0)

output = {
    "phase_compositions": [phases[0][0], phases[1][0], phases[2][0]],
    "volume_fractions": [phases[0][1], phases[1][1], phases[2][1]],
    "phase_lattice_constants_A": lattice_constants,
    "phase_densities_g_per_cc": densities,
    "phase_theta_D_K": theta_Ds,
    "theta_D_effective_K": round(theta_eff, 2),
}

with open("/app/outputs/computed_values.json", "w") as f:
    json.dump(output, f, indent=2)
