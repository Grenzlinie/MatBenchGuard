#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: cohesive_parameters.json ===
python3 -c "
import json, math

# Input constants
epsilon_eV = 0.00239
sigma_nm = 0.3415
l0_nm = 0.142

# Convert to SI
epsilon_J = epsilon_eV * 1.602176634e-19
sigma_m = sigma_nm * 1e-9
l0_m = l0_nm * 1e-9

# Area density of graphene
rho_c_m2 = 4.0 / (3.0 * math.sqrt(3.0) * l0_m**2)

# Total cohesive energy Φ_total (J/m^2)
Phi_total = 6.0 * math.pi * rho_c_m2**2 * epsilon_J * sigma_m**2 / 5.0

# Tensile cohesive strength σ_max (Pa)
sigma_max_Pa = (48.0 * math.pi / 11.0) * ((5.0/11.0)**(5.0/6.0)) * rho_c_m2**2 * epsilon_J * sigma_m
sigma_max_GPa = sigma_max_Pa / 1e9

# Critical separation δ_0 (m)
delta_0_m = ((11.0/5.0)**(1.0/6.0) - 1.0) * sigma_m
delta_0_nm = delta_0_m * 1e9

result = {
    'Phi_total': Phi_total,
    'sigma_max': sigma_max_GPa,
    'delta_0': delta_0_nm,
    'epsilon': epsilon_eV,
    'sigma': sigma_nm
}

with open('/app/outputs/cohesive_parameters.json', 'w') as f:
    json.dump(result, f)
"

# === solve block: stress_displacement_data.csv ===
python3 -c "
import csv, math

# Input constants
epsilon_eV = 0.00239
sigma_nm = 0.3415
l0_nm = 0.142

# Convert to SI
epsilon_J = epsilon_eV * 1.602176634e-19
sigma_m = sigma_nm * 1e-9
l0_m = l0_nm * 1e-9

# Area density
rho_c_m2 = 4.0 / (3.0 * math.sqrt(3.0) * l0_m**2)

# Finite overlap parameters
L_u_m = 10.0e-9   # current overlap length L−u = 10 nm
u = 0.0            # sliding displacement

with open('/app/outputs/stress_displacement_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['v_nm', 'sigma_cohesive_GPa', 'tau_cohesive_GPa'])

    for i in range(51):
        v_nm = i * 0.01
        v_m = v_nm * 1e-9

        # Tensile cohesive stress (infinite graphene) – eq (7)
        sigma_Pa = 8.0 * math.pi * rho_c_m2**2 * epsilon_J * sigma_m \
                   * ( (sigma_m**5 / (sigma_m + v_m)**5)
                      - (sigma_m**11 / (sigma_m + v_m)**11) )
        sigma_GPa = sigma_Pa / 1e9

        # Average shear cohesive stress (finite overlap) – eq (22)
        tau_Pa = 2.0 * math.pi * rho_c_m2**2 * epsilon_J * sigma_m**2 / L_u_m \
                 * ( (sigma_m**4 / (sigma_m + v_m)**4)
                    - (2.0/5.0) * (sigma_m**10 / (sigma_m + v_m)**10) )
        tau_GPa = tau_Pa / 1e9

        writer.writerow([f'{v_nm:.2f}', f'{sigma_GPa:.6f}', f'{tau_GPa:.6f}'])
"

# === solve block: cohesive_law_expressions.txt ===
cat > /app/outputs/cohesive_law_expressions.txt << 'EOF'
Infinite graphene (cohesive energy per unit area and tensile cohesive stress):

  Φ(v) = 2π ρ_c^2 ε σ^2 [ 2 σ^10 / (5 (σ+v)^10) - σ^4 / (σ+v)^4 ]
  σ_cohesive(v) = 8π ρ_c^2 ε σ [ σ^5 / (σ+v)^5 - σ^11 / (σ+v)^11 ]

Finite overlap (line energy and average shear cohesive stress):

  Φ_line(L-u, σ+v) ≈ 2π ρ_c^2 ε σ^2 [ 2 σ^10 / (5 (σ+v)^10) - σ^4 / (σ+v)^4 ] (L-u)
  τ_cohesive(v) ≈ 2π ρ_c^2 ε σ^2 / (L-u) * [ σ^4 / (σ+v)^4 - 2 σ^10 / (5 (σ+v)^10) ]
EOF
