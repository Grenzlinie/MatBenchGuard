#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_critical_field.txt ===
python3 << 'EOF'
import math
z = 1
n_i = 6.2e14  # cm^{-3}
E0 = 2e-7 * z * math.sqrt(n_i)
with open('/app/outputs/step_01_critical_field.txt', 'w') as f:
    f.write(f'{E0:.8f}\n')
EOF

# === solve block: step_02_transport_coefficients.csv ===
python3 << 'EOF'
import math
# Recompute E0
z = 1
n_i = 6.2e14
E0 = 2e-7 * z * math.sqrt(n_i)
# Constants for t=3
t = 3
G_half = math.gamma(0.5)          # sqrt(pi)
G_onehalf = math.gamma(1.5)       # 0.5*sqrt(pi)
G_4 = 6.0                         # gamma(4) = 6
D_gam = G_half * G_4 / (G_onehalf * G_onehalf) * (1.0/t)  # D(t)
# D(t) simplifies to 8*sqrt(pi)/pi, but use computed
gamma_num = math.gamma((3+t)/(2*t))       # gamma(1) = 1
gamma_den = math.gamma((3+2*t)/(2*t))     # gamma(1.5) = 0.5*sqrt(pi)
J_factor = (1.0/D_gam) * gamma_num / gamma_den * t**(-0.5)
# H/H_i^0 = 1
H_over_H0 = 1.0

with open('/app/outputs/step_02_transport_coefficients.csv', 'w') as f:
    f.write('Ex_ratio,tan_theta,rho_ratio,j_ratio\n')
    for i in range(1, 100):  # 0.01 to 0.99 step 0.01
        Ex_ratio = i / 100.0
        factor = 1.0 / math.sqrt(1.0 - Ex_ratio**2)
        tan_theta = Ex_ratio * factor
        rho_ratio = D_gam * H_over_H0 * Ex_ratio * factor
        j_ratio = J_factor * factor
        f.write(f'{Ex_ratio:.4f},{tan_theta:.6f},{rho_ratio:.6f},{j_ratio:.6f}\n')
EOF

# === solve block: step_03_breakdown_field.txt ===
python3 << 'EOF'
import math
t = 3
c0 = 0.5
r = 1
sigma_ratio = 1.0   # sigma_r^0 / sigma_I^0

# Gamma values
G_1_3 = math.gamma(1.0/3.0)
G_1 = 1.0
G_1half = math.gamma(1.5)   # sqrt(pi)/2
G_half = math.gamma(0.5)     # sqrt(pi)

# Compute Phi2 according to Eq. (17)
# Phi2 = [sigma_ratio * Gamma((2-r)/t) / Gamma(3/(2t)) * c0/(1-c0)]^{1/(2r)} * Gamma((2t+3)/(2t)) / Gamma((t+3)/(2t))
# with Gamma(3/(2t)) = Gamma(0.5), Gamma((2-r)/t) = Gamma(1/3)
bracket = sigma_ratio * G_1_3 / G_half * (c0 / (1 - c0))
Phi2 = bracket**(1.0/(2*r)) * (G_1half / G_1)   # Gamma((2t+3)/(2t)) = Gamma(1.5), Gamma((t+3)/(2t)) = Gamma(1) = 1

# H/H_i^0 = 1 (same as step_02)
H_over_H0 = 1.0
Ex_cr_over_E0 = Phi2 * H_over_H0 / math.sqrt(1 + (Phi2 * H_over_H0)**2)

with open('/app/outputs/step_03_breakdown_field.txt', 'w') as f:
    f.write(f'{Ex_cr_over_E0:.8f}\n')
EOF
