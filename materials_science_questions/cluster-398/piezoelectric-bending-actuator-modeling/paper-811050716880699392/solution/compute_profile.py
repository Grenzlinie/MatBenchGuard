import numpy as np
from scipy.integrate import quad
import csv

# Geometry and material parameters for the bimorph (SI units)
r1 = 15e-3           # passive layer radius (15 mm)
r2 = 12e-3           # PZT/bonding layer radius (12 mm)
tp = 150e-6          # passive layer thickness (150 um)
tb = 20e-6           # bonding layer thickness (20 um)
tpzt = 100e-6        # PZT layer thickness (100 um)
E_p = 100e9          # Young's modulus of brass (passive)
v_p = 0.27           # Poisson's ratio of brass
E_b = 5.17e9         # Young's modulus of epoxy (bonding)
v_b = 0.3            # Poisson's ratio of epoxy
s11E = 16.4e-12      # PZT compliance constant (m^2/N)
s12E = -5.75e-12     # PZT compliance constant
v_pzt = -s12E / s11E # PZT effective Poisson's ratio
d31 = -171e-12       # piezoelectric constant (m/V)
eps33 = 7.346e-9    # PZT permittivity (F/m)
h = tp / 2.0         # neutral plane distance for symmetric bimorph
V = 100.0            # applied voltage (V)

# ---------- trial basis functions ----------
# w(r) = sum_{i=1}^{4} C_i * phi_i, where phi_i = (1 - x)^{i+1}, x = r^2/r1^2
def S_i(x, i):
    # S_i = (i+1)*(1-x)^i   (used for w' and w'')
    return (i+1) * (1.0 - x)**i

def T_i(x, i):
    # T_i = S_i + 2x dS_i/dx  (appears in w'')
    return (i+1) * (1.0 - x)**(i-1) * (1.0 - (2*i+1)*x)

def kappa_i(x, i):
    # curvature = w'' + (1/r) w'
    return - (4.0 / r1**2) * (i+1) * (1.0 - x)**(i-1) * (1.0 - (i+1)*x)

# ---------- elastic stiffness K ----------
def compute_K_el(XR, nu, factor_el):
    K = np.zeros((4,4))
    for i in range(4):
        for j in range(i,4):
            def integrand(x):
                return (T_i(x, i+1)*T_i(x, j+1) +
                        nu*(S_i(x, i+1)*T_i(x, j+1) + S_i(x, j+1)*T_i(x, i+1)) +
                        S_i(x, i+1)*S_i(x, j+1))
            I_ij, _ = quad(integrand, 0, XR)
            val = factor_el * (2.0 / r1**2) * I_ij
            K[i,j] = val
            K[j,i] = val
    return K

# thickness parameters
I_p = (tp - h)**3 + h**3               # = tp^3/4
I_b = (tp + tb - h)**3 - (tp - h)**3
I_pzt = (tp + tb + tpzt - h)**3 - (tp + tb - h)**3

factor_p = np.pi * E_p * I_p / (3.0 * (1 - v_p**2))
factor_b = np.pi * E_b * I_b / (3.0 * (1 - v_b**2))
factor_pzt_el = np.pi * I_pzt / (3.0 * s11E * (1 - v_pzt**2))

K_p = compute_K_el(1.0, v_p, factor_p)
XR2 = (r2 / r1)**2
K_b = compute_K_el(XR2, v_b, factor_b)
K_pzt_el = compute_K_el(XR2, v_pzt, factor_pzt_el)

# ---------- electro-mechanical coupling ----------
def compute_K_kappa(XR):
    K = np.zeros((4,4))
    for i in range(4):
        for j in range(i,4):
            def integrand(x):
                return kappa_i(x, i+1) * kappa_i(x, j+1)
            I_ij, _ = quad(integrand, 0, XR)
            val = (r1**2 / 2.0) * I_ij
            K[i,j] = val
            K[j,i] = val
    return K
K_kappa = compute_K_kappa(XR2)

def compute_I2(XR):
    I2 = np.zeros(4)
    for i in range(4):
        def integrand(x):
            return kappa_i(x, i+1)
        int_val, _ = quad(integrand, 0, XR)
        I2[i] = (r1**2 / 2.0) * int_val
    return I2
I2_vec = compute_I2(XR2)

z_b = tp/2 + tb
z_t = tp/2 + tb + tpzt
Z1 = tpzt
Z2_coeff_a1a2 = 2.0 * (z_t**2 - z_b**2)
Z3_coeff_a2a2 = (4.0/3.0) * (z_t**3 - z_b**3)

I_z1 = (z_t**2 - z_b**2) / 2.0
I_z2 = 2.0 * (z_t**3 - z_b**3) / 3.0
t_off = tp/2 + tb + tpzt/2

thick1 = (tp/2 + tb + tpzt)**3 - (tp/2 + tb)**3
thick2 = (tp/2 + tb + tpzt)**2 - (tp/2 + tb)**2

alpha = d31 / (4.0 * d31**2 - 2.0 * s11E * eps33 * (1.0 - v_pzt))

C1 = np.pi * eps33 - 2.0 * np.pi * d31**2 / (s11E * (1.0 - v_pzt))
C2 = np.pi * d31**2 / (s11E * (1.0 - v_pzt))

coef_a2 = (2.0 * np.pi * d31 * thick1) / (3.0 * s11E * (1.0 - v_pzt))
coef_a1 = (np.pi * d31 * thick2) / (2.0 * s11E * (1.0 - v_pzt))

quad_coeff = alpha**2 * (4.0 * t_off**2 * Z1 - 4.0 * t_off * (z_t**2 - z_b**2) + Z3_coeff_a2a2)
linear_coeff = (V / tpzt) * ( -4.0 * t_off * alpha * Z1 + 2.0 * alpha * (z_t**2 - z_b**2) )

Q_extra_per_PZT = (- coef_a2 * alpha +
                   coef_a1 * 2.0 * t_off * alpha -
                   C1 * quad_coeff -
                   C2 * alpha * (I_z2 - 2.0 * t_off * I_z1))

K_extra = (2.0 * Q_extra_per_PZT) * K_kappa   # two PZT layers

# total stiffness
K_total = K_p + 2.0 * K_b + 2.0 * K_pzt_el + K_extra

# total linear term
b_total = -2.0 * I2_vec * (coef_a1 * V / tpzt + C1 * linear_coeff + C2 * V / tpzt * I_z1)

# solve linear system  2 K_total C + b_total = 0  => C = -0.5 inv(K) b
C = -0.5 * np.linalg.solve(K_total, b_total)

# ---------- deflection profile ----------
r_vals = np.linspace(0, r1, 20)
w = np.zeros_like(r_vals)
for idx, r in enumerate(r_vals):
    x = (r / r1)**2
    val = 0.0
    for i in range(4):
        val += C[i] * (1.0 - x)**(i+2)   # phi_i = (1-x)^{i+1}
    w[idx] = val

r_mm = r_vals * 1e3
w_um = w * 1e6

with open('/app/outputs/deflection_profile.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['r_mm', 'w_um'])
    for rm, wm in zip(r_mm, w_um):
        writer.writerow([rm, wm])

print(f'Center displacement = {w_um[0]:.3f} µm')
