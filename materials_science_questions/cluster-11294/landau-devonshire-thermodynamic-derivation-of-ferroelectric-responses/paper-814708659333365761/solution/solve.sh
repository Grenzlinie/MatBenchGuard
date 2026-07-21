#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# Install required packages from Tsinghua mirror
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: pto_on_si.csv ===
# Overwrite thermo.py with a corrected version that uses scipy.integrate.quad
cat > /solution/thermo.py << 'EOTHERM'
import csv, math
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

# Material constants from Table II
T0 = 479.0
a1_const = 3.8e5
alpha11 = -7.3e7
alpha111 = 2.6e8
s11 = 8.0e-12
s12 = -2.5e-12
Q11 = 0.089
Q12 = -0.026
eps0 = 8.854e-12
T_RT = 25.0
s_sum = s11 + s12

alpha11_star = alpha11 + Q12**2 / s_sum
alpha1_0 = a1_const * (T_RT - T0)

alpha_PTO = 11.86e-6
alpha_MgO = 13.47e-6  # MgO TEC from Table I

def alpha_Si(T):
    return (3.725*(1 - math.exp(-5.88e3*(T+149))) + 5.548e-4*(T+273))*1e-6

def alpha_c_sapphire(T):
    return (8.026 + 8.17e-4*T - 3.279*math.exp(-2.91e-3*T))*1e-6

def alpha_a_sapphire(T):
    return (7.419 + 6.43e-4*T - 3.211*math.exp(-2.59e-3*T))*1e-6

def compute_u_T_iso(alpha_sub_func, TG):
    if TG == T_RT:
        return 0.0
    return quad(lambda T: alpha_PTO - alpha_sub_func(T), T_RT, TG)[0]

def free_energy_G(P, a1s):
    return a1s*P**2 + alpha11_star*P**4 + alpha111*P**6

def properties(P, a1s):
    d2G = 2*a1s + 12*alpha11_star*P**2 + 30*alpha111*P**4
    eps = 1.0/(eps0 * d2G)
    K = Q11 - (2*s12*Q12)/s_sum
    d33 = 2.0*eps0*eps*K*P
    return eps, d33

def process_substrate(substrate_name, TG_values):
    ROWS = []
    E = 1e8  # 1000 kV/cm
    
    if substrate_name == 'c-sapphire':
        sub_func = alpha_c_sapphire
        is_anisotropic = False
    elif substrate_name == 'a-sapphire':
        sub_func_c = alpha_c_sapphire
        sub_func_a = alpha_a_sapphire
        is_anisotropic = True
    elif substrate_name == 'MgO':
        sub_func = lambda T: 13.47e-6
        is_anisotropic = False
    else:
        raise ValueError(f"Unknown substrate: {substrate_name}")
    
    for TG in TG_values:
        if is_anisotropic:
            uT1 = quad(lambda T: alpha_PTO - sub_func_c(T), T_RT, TG)[0]
            uT2 = quad(lambda T: alpha_PTO - sub_func_a(T), T_RT, TG)[0]
            uT_sum = uT1 + uT2
            a1s = alpha1_0 - (Q12/s_sum)*uT_sum
        else:
            uT = compute_u_T_iso(sub_func, TG)
            a1s = alpha1_0 - (2*Q12/s_sum)*uT
        
        # equilibrium P at E=0
        res0 = minimize_scalar(lambda P: free_energy_G(P, a1s), bounds=(-5,5), method='bounded')
        P0 = res0.x
        eps0_val, d33_0 = properties(P0, a1s)
        
        # equilibrium P at E=1e8 V/m
        resE = minimize_scalar(lambda P: free_energy_G(P, a1s) - E*P, bounds=(-5,5), method='bounded')
        PE = resE.x
        epsE, d33_E = properties(PE, a1s)
        
        phi = (eps0_val - epsE)/eps0_val * 100.0 if eps0_val != 0 else 0.0
        phi_prime = (1.0 - (epsE/eps0_val)*(PE/P0)) * 100.0 if P0 != 0 else 0.0
        ROWS.append([TG, P0, eps0_val, d33_0, phi, phi_prime])
    return ROWS

def compute_and_write(substrate_name, output_path):
    TG_values = list(range(25, 801))
    rows = process_substrate(substrate_name, TG_values)
    with open(output_path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['TG','P','epsilon33','d33','phi','phi_prime'])
        w.writerows(rows)
EOTHERM

python3 << PYEOF
import csv, math
from scipy.optimize import minimize_scalar
from scipy.integrate import quad

# Material constants from Table II
T0 = 479.0
a1_const = 3.8e5
alpha11 = -7.3e7
alpha111 = 2.6e8
s11 = 8.0e-12
s12 = -2.5e-12
Q11 = 0.089
Q12 = -0.026
eps0 = 8.854e-12
T_RT = 25.0
s_sum = s11 + s12

# Renormalized alpha11* is constant (no uT dependence)
alpha11_star = alpha11 + Q12**2 / s_sum

# Bulk alpha1 at room temperature
alpha1_0 = a1_const * (T_RT - T0)

# Thermal expansion coefficients (x 1e-6 /°C, Table I)
alpha_PTO = 11.86e-6
def alpha_Si(T):
    return (3.725*(1 - math.exp(-5.88e3*(T+149))) + 5.548e-4*(T+273)) * 1e-6

def compute_uT(TG):
    if TG == T_RT:
        return 0.0
    return quad(lambda T: alpha_PTO - alpha_Si(T), T_RT, TG)[0]

def G(P, a1s):
    return a1s*P**2 + alpha11_star*P**4 + alpha111*P**6

def properties(P, a1s):
    d2G = 2*a1s + 12*alpha11_star*P**2 + 30*alpha111*P**4
    eps = 1.0 / (eps0 * d2G)
    K = Q11 - (2*s12*Q12) / s_sum
    d33 = 2.0 * eps0 * eps * K * P
    return eps, d33

TG_values = list(range(25, 801))
rows = []
E = 1e8  # 1000 kV/cm in V/m

for TG in TG_values:
    uT = compute_uT(TG)
    a1s = alpha1_0 - (2*Q12/s_sum) * uT

    # equilibrium P at E=0
    res0 = minimize_scalar(lambda P: G(P, a1s), bounds=(-5, 5), method='bounded')
    P0 = res0.x
    eps0_val, d33_0 = properties(P0, a1s)

    # equilibrium P at E=1e8 V/m
    resE = minimize_scalar(lambda P: G(P, a1s) - E*P, bounds=(-5, 5), method='bounded')
    PE = resE.x
    epsE, d33_E = properties(PE, a1s)

    phi = (eps0_val - epsE) / eps0_val * 100.0
    phi_prime = (1.0 - (epsE/eps0_val)*(PE/P0)) * 100.0
    rows.append([TG, P0, eps0_val, d33_0, phi, phi_prime])

with open('$OUTDIR/pto_on_si.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['TG','P','epsilon33','d33','phi','phi_prime'])
    w.writerows(rows)
PYEOF

# === solve block: pto_on_c_sapphire.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from thermo import compute_and_write; compute_and_write('c-sapphire', '/app/outputs/pto_on_c_sapphire.csv')"

# === solve block: pto_on_a_sapphire.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from thermo import compute_and_write; compute_and_write('a-sapphire', '/app/outputs/pto_on_a_sapphire.csv')"

# === solve block: pto_on_mgo.csv ===
python3 -c "import sys; sys.path.insert(0,'/solution'); from thermo import compute_and_write; compute_and_write('MgO', '/app/outputs/pto_on_mgo.csv')"
