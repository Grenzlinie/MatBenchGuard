import math
import csv
import sys

# Constants from the paper
L0 = 2.45e-8
M0 = 1.90 * 0.85e-5   # k * rho = 1.90 * 0.85e-5 = 1.615e-5 (W*Ohm/K^2)
eta = 0.19e-3          # Seebeck coefficient V/K
Cp = 1.04               # J/(g K)
CL = 199                # J/g
u = Cp / CL
Tc = 77.0
Tr = 300.0

# Optimal parameters from the paper's Table I for f=0 and f=1
params = {
    0: {
        'PCL': {'Z1': 5900, 'Z2': 3207, 'Tj': 216.97},
        'Cu':  {'Z1': 8380}
    },
    1: {
        'PCL': {'Z1': 7100, 'Z2': 3659, 'Tj': 205.12},
        'Cu':  {'Z1': 10700}
    }
}

# Pre-computed values for f=0
beta0 = math.sqrt(L0)

# For f=1, heat leak values from the table (mW/A -> V)
q_pcl_f1 = 0.021160  # 21.160 mW/A
q_cu_f1  = 0.025433  # 25.433 mW/A
alpha_pcl = 1.0 * q_pcl_f1 * u / 2.0
beta_pcl  = math.sqrt(L0 - alpha_pcl**2)
alpha_cu  = 1.0 * q_cu_f1 * u / 2.0
beta_cu   = math.sqrt(L0 - alpha_cu**2)

def T_cu_f0(z, Z1, Tj):
    """Eq (12) in the paper, Cu lead f=0."""
    bz = beta0 * z
    bZ = beta0 * Z1
    return Tj * math.sin(bz) / math.sin(bZ) + Tc * (math.cos(bz) - math.sin(bz) * math.cos(bZ) / math.sin(bZ))

def T_te_f0(z, Z2, _Tj):
    """Eq (18) in the paper, TE element f=0."""
    return Tr - M0 * (z - Z2)**2 / 2.0

def T_cu_f1(z, Z1, Tj, alpha, beta):
    """Eq (9) in the paper, Cu lead f>0."""
    e_az = math.exp(alpha * z)
    e_aZ = math.exp(alpha * Z1)
    s_z  = math.sin(beta * z)
    s_Z  = math.sin(beta * Z1)
    c_z  = math.cos(beta * z)
    c_Z  = math.cos(beta * Z1)
    return Tj * e_az * s_z / (e_aZ * s_Z) + Tc * e_az * (c_z - s_z * c_Z / s_Z)

def T_te_f1(z, Z2, _Tj, alpha):
    """Eq (15) in the paper, TE element f>0."""
    term = z - Z2
    return Tr + (M0 / (2*alpha)) * term + (M0 / (4*alpha*alpha)) * (1.0 - math.exp(2*alpha*term))

def generate_profiles():
    writer = csv.writer(sys.stdout)
    writer.writerow(['f', 'lead_type', 'normalized_position', 'temperature_K'])
    N = 101  # number of points per segment
    for f_val in (0, 1):
        p = params[f_val]
        # ---- PCL ----
        Z1, Z2, Tj = p['PCL']['Z1'], p['PCL']['Z2'], p['PCL']['Tj']
        # Cu segment: normalized_position from -1 to 0, z in [0, Z1]
        for i in range(N):
            z = Z1 * i / (N-1)
            norm = z / Z1 - 1.0
            if f_val == 0:
                T = T_cu_f0(z, Z1, Tj)
            else:
                T = T_cu_f1(z, Z1, Tj, alpha_pcl, beta_pcl)
            writer.writerow([f_val, 'PCL', norm, T])
        # TE segment: normalized_position from 0 to 1, z in [0, Z2]
        for i in range(N):
            z = Z2 * i / (N-1)
            norm = z / Z2
            if f_val == 0:
                T = T_te_f0(z, Z2, Tj)
            else:
                T = T_te_f1(z, Z2, Tj, alpha_pcl)
            writer.writerow([f_val, 'PCL', norm, T])
        # ---- All-Cu lead ----
        Z1cu = p['Cu']['Z1']
        for i in range(N):
            z = Z1cu * i / (N-1)
            norm = z / Z1cu - 1.0
            if f_val == 0:
                T = T_cu_f0(z, Z1cu, Tr)
            else:
                T = T_cu_f1(z, Z1cu, Tr, alpha_cu, beta_cu)
            writer.writerow([f_val, 'Cu', norm, T])

if __name__ == '__main__':
    generate_profiles()
