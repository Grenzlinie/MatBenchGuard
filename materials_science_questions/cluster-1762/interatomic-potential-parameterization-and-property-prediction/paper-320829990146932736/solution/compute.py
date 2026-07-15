#!/usr/bin/env python3
import sys, json, math

# Physical constants (atomic units)
ANG_TO_AU = 1.0 / 0.5291772108
zstar = 0.58
z_I = -zstar
z_Cd = 2 * zstar
a_ang = 4.244
c_ang = 3.430
a_au = a_ang * ANG_TO_AU
c_au = c_ang * ANG_TO_AU
gamma = c_au / a_au  # expected 0.808

# Van der Waals constants (a.u.)
C_XX = -390.14
C_XM = -164.40
C_MM = -69.23

# ----- Coulomb analytic differences, Eq. (13) -----
def coulomb_diff(m, z1, z2):
    """Compute ΔV^z_{ss'}(m) for dimensionless m (distance in units of c)."""
    factor = -9.0 * z1 * z2 / (c_au * gamma**3)
    # exponential terms
    t1 = math.exp(-4.0 * math.pi / math.sqrt(3.0) * gamma * m)
    t2 = 0.5 * math.exp(-8.0 * math.pi / math.sqrt(3.0) * gamma * m)
    t3 = (2.0 / math.sqrt(7.0)) * math.exp(-4.0 * math.pi * math.sqrt(7.0/3.0) * gamma * m)
    return factor * (t1 + t2 + t3)

# lattice vectors for triangular lattice
a_vec = (a_au, 0.0)
b_vec = (a_au/2.0, a_au * math.sqrt(3.0)/2.0)
# shift from A to B
dx_shift = 2.0 * a_au / 3.0
dy_shift = a_au * math.sqrt(3.0) / 3.0

def lattice_sum(m, p):
    """Compute lattice sum for a pair of layers at distance m*c_au, for potential 1/distance^{2*p}.
    p=3 for R^{-6}, p=6 for R^{-12}.
    Returns (like_sum, unlike_sum) where like-sum is for AA stacking, unlike-sum for AB stacking."""
    Nmax = 200  # enough for convergence
    dz = m * c_au
    like = 0.0
    unlike = 0.0
    for i in range(-Nmax, Nmax+1):
        ix = i * a_vec[0]
        iy = i * a_vec[1]
        for j in range(-Nmax, Nmax+1):
            x = ix + j * b_vec[0]
            y = iy + j * b_vec[1]
            r2_like = x*x + y*y + dz*dz
            inv_like = r2_like**(-p)
            like += inv_like
            # for unlike stack, shift position
            x_unlike = x + dx_shift
            y_unlike = y + dy_shift
            r2_unlike = x_unlike*x_unlike + y_unlike*y_unlike + dz*dz
            inv_unlike = r2_unlike**(-p)
            unlike += inv_unlike
    return like, unlike

# Cache computed sums per m and p to avoid recomputing
sum_cache = {}
def get_delta_contrib(m, p):
    """Return f = unlike - like for given m and p."""
    key = (m, p)
    if key not in sum_cache:
        like, unlike = lattice_sum(m, p)
        sum_cache[key] = unlike - like
    return sum_cache[key]

# Required ΔV from Coulomb
# m values
m_XM_3_2 = 1.5
m_XM_5_2 = 2.5
m_XX_2 = 2.0
m_MM_2 = 2.0
m_XX_3 = 3.0

# Coulomb differences
dVz_XM_1_5 = coulomb_diff(m_XM_3_2, z_Cd, z_I)
dVz_XM_2_5 = coulomb_diff(m_XM_5_2, z_Cd, z_I)
dVz_XX_2 = coulomb_diff(m_XX_2, z_I, z_I)
dVz_MM_2 = coulomb_diff(m_MM_2, z_Cd, z_Cd)
dVz_XX_3 = coulomb_diff(m_XX_3, z_I, z_I)

# Van der Waals contributions (R^{-6}, p=3)
p_vdw = 3
f_vdw_XM_1_5 = get_delta_contrib(m_XM_3_2, p_vdw)
f_vdw_XM_2_5 = get_delta_contrib(m_XM_5_2, p_vdw)
f_vdw_XX_2 = get_delta_contrib(m_XX_2, p_vdw)
f_vdw_MM_2 = get_delta_contrib(m_MM_2, p_vdw)  # same as XX_2, but may differ due to dz, but m same so same geometry -> same f.
f_vdw_XX_3 = get_delta_contrib(m_XX_3, p_vdw)

# Repulsive contributions (R^{-12}, p=6)
p_rep = 6
f_rep_XM_1_5 = get_delta_contrib(m_XM_3_2, p_rep)
f_rep_XM_2_5 = get_delta_contrib(m_XM_5_2, p_rep)
f_rep_XX_2 = get_delta_contrib(m_XX_2, p_rep)
f_rep_MM_2 = get_delta_contrib(m_MM_2, p_rep)
f_rep_XX_3 = get_delta_contrib(m_XX_3, p_rep)

# Helper to compute J1,J2,K from given ΔV dict
def compute_J(dVs):
    # dVs keys: 'XM_1_5','XM_2_5','XX_2','MM_2','XX_3'
    J1 = 0.5 * (dVs['XM_1_5'] - dVs['XX_2'] - 0.5*dVs['MM_2'] + dVs['XX_3'])
    J2 = 0.25 * dVs['XX_3']
    K = 0.25 * dVs['MM_2'] - 0.5 * dVs['XM_2_5']
    return J1, J2, K

# Coulomb only
dVs_coulomb = {
    'XM_1_5': dVz_XM_1_5,
    'XM_2_5': dVz_XM_2_5,
    'XX_2': dVz_XX_2,
    'MM_2': dVz_MM_2,
    'XX_3': dVz_XX_3
}
J1_c, J2_c, K_c = compute_J(dVs_coulomb)

# Coulomb + vdW
dVs_vdw = {}
for key in ['XM_1_5','XM_2_5','XX_2','MM_2','XX_3']:
    if key == 'XM_1_5':
        dVc = C_XM * f_vdw_XM_1_5
    elif key == 'XM_2_5':
        dVc = C_XM * f_vdw_XM_2_5
    elif key == 'XX_2':
        dVc = C_XX * f_vdw_XX_2
    elif key == 'MM_2':
        dVc = C_MM * f_vdw_MM_2
    elif key == 'XX_3':
        dVc = C_XX * f_vdw_XX_3
    dVs_vdw[key] = dVs_coulomb[key] + dVc
J1_v, J2_v, K_v = compute_J(dVs_vdw)

# Derive alpha, beta from frustration condition
# Condition: ΔV_XM(3/2) + ΔV_XM(5/2) - [ΔV_XX(2) + ΔV_MM(2)] = 0
# Total ΔV = dVz + dVc + B*f_rep.
# So: B_XM*(f_rep_XM_1_5+f_rep_XM_2_5) = B_XX*f_rep_XX_2 + B_MM*f_rep_MM_2 - (sum_coul_vdw_part)
# sum_coul_vdw_part = (dVz_XM_1_5+dVz_XM_2_5) + C_XM*(f_vdw_XM_1_5+f_vdw_XM_2_5) - (dVz_XX_2+dVz_MM_2) - (C_XX*f_vdw_XX_2 + C_MM*f_vdw_MM_2)
sum_coul_vdw = (dVz_XM_1_5 + dVz_XM_2_5) + C_XM*(f_vdw_XM_1_5 + f_vdw_XM_2_5) - (dVz_XX_2 + dVz_MM_2) - (C_XX*f_vdw_XX_2 + C_MM*f_vdw_MM_2)
denom = f_rep_XM_1_5 + f_rep_XM_2_5
alpha = -sum_coul_vdw / denom
beta = f_rep_XX_2 / denom  # assuming f_rep_XX_2 == f_rep_MM_2, which holds

# Full results with B_XX = B_MM = alpha, B_XM = alpha
dVs_full = {}
for key in ['XM_1_5','XM_2_5','XX_2','MM_2','XX_3']:
    # Coulomb
    if key == 'XM_1_5':
        dVz = dVz_XM_1_5; dVc = C_XM * f_vdw_XM_1_5; f_rep = f_rep_XM_1_5; B = alpha
    elif key == 'XM_2_5':
        dVz = dVz_XM_2_5; dVc = C_XM * f_vdw_XM_2_5; f_rep = f_rep_XM_2_5; B = alpha
    elif key == 'XX_2':
        dVz = dVz_XX_2; dVc = C_XX * f_vdw_XX_2; f_rep = f_rep_XX_2; B = alpha
    elif key == 'MM_2':
        dVz = dVz_MM_2; dVc = C_MM * f_vdw_MM_2; f_rep = f_rep_MM_2; B = alpha
    elif key == 'XX_3':
        dVz = dVz_XX_3; dVc = C_XX * f_vdw_XX_3; f_rep = f_rep_XX_3; B = alpha
    dVs_full[key] = dVz + dVc + B * f_rep
J1_f, J2_f, K_f = compute_J(dVs_full)

# Equilibrium bond length R0 from dW/dR = 0 for Cd-I pair
z_prod = z_Cd * z_I  # -0.6728
C = C_XM
B = alpha
# Solve -z_prod/R^2 - 12*B/R^13 - 6*C/R^7 = 0  -> multiply by -R^13: z_prod*R^11 + 12*B + 6*C*R^6 = 0
# We'll use simple bisection.
def f_eq(R):
    return z_prod * R**11 + 12.0 * B + 6.0 * C * R**6

# Search starting interval
R_low = 5.0
R_high = 20.0
for _ in range(100):
    mid = (R_low + R_high) / 2.0
    if f_eq(mid) == 0:
        R0 = mid
        break
    if f_eq(R_low)*f_eq(mid) < 0:
        R_high = mid
    else:
        R_low = mid
R0 = mid

# Write output based on mode
mode = sys.argv[1] if len(sys.argv) > 1 else "full"
outfile = sys.argv[2] if len(sys.argv) > 2 else "/app/outputs/default.json"

def write_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

if mode == "coulomb":
    obj = {
        "J1_a.u.": J1_c,
        "J2_a.u.": J2_c,
        "K_a.u.": K_c,
        "J2_over_J1": J2_c / J1_c,
        "K_over_J1": K_c / J1_c
    }
    write_json(obj, outfile)
elif mode == "vdw":
    obj = {
        "J1_a.u.": J1_v,
        "J2_a.u.": J2_v,
        "K_a.u.": K_v,
        "J2_over_J1": J2_v / J1_v,
        "K_over_J1": K_v / J1_v
    }
    write_json(obj, outfile)
elif mode == "full":
    obj = {
        "J1_a.u.": J1_f,
        "J2_a.u.": J2_f,
        "K_a.u.": K_f,
        "J2_over_J1": J2_f / J1_f,
        "K_over_J1": K_f / J1_f,
        "alpha_a.u.": alpha,
        "beta_a.u.": beta,
        "B_XX_au": alpha,
        "B_MM_au": alpha,
        "B_XM_au": alpha,
        "R0_au": R0
    }
    write_json(obj, outfile)
else:
    raise ValueError("Unknown mode")
