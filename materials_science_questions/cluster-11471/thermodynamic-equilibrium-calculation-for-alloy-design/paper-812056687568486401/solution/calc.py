import csv, math

R = 8.314
T = 423.15          # K
sigma = 0.235        # J/m^2
Vm = 16.26e-6        # m^3/mol

# known flat-interface Sn solubility in fcc
X_Sn_fcc_flat = 0.1929

# Lattice stability differences (J/mol)
DG_Sn_fcc_to_bct = 4150.0   # G(Sn,fcc) - G(Sn,bct) ≈ 4150
DG_Pb_fcc_to_bct = 10000.0  # G(Pb,bct) - G(Pb,fcc), estimated

# Interaction parameters in bct (regular solution)
L0_bct = 0.0

# ----------------------------------------------------------------------
def mu_Sn_fcc(x, L0):
    """RT ln a_Sn for fcc, reference pure Sn fcc"""
    return R*T*math.log(x) + (1-x)**2 * L0

def mu_Pb_fcc(x, L0):
    return R*T*math.log(1-x) + x**2 * L0

def mu_Sn_bct(y, L0):
    return R*T*math.log(y) + (1-y)**2 * L0

def mu_Pb_bct(y, L0):
    return R*T*math.log(1-y) + y**2 * L0

# derivatives
def dmu_Sn_fcc_dx(x, L0):
    return R*T/x - 2*(1-x)*L0

def dmu_Sn_bct_dy(y, L0):
    return R*T/y - 2*(1-y)*L0

def dmu_Pb_fcc_dx(x, L0):
    return -R*T/(1-x) + 2*x*L0

def dmu_Pb_bct_dy(y, L0):
    return -R*T/(1-y) + 2*y*L0

def flat_equilibrium(L0_fcc, L0_bct, DG_Sn, DG_Pb):
    """Solve x (X_Sn_fcc), y (X_Sn_bct) for flat interface"""
    x, y = 0.19, 0.98
    for _ in range(50):
        F1 = mu_Sn_fcc(x, L0_fcc) - mu_Sn_bct(y, L0_bct) + DG_Sn
        F2 = mu_Pb_fcc(x, L0_fcc) - mu_Pb_bct(y, L0_bct) - DG_Pb
        d11 = dmu_Sn_fcc_dx(x, L0_fcc)
        d12 = -dmu_Sn_bct_dy(y, L0_bct)
        d21 = dmu_Pb_fcc_dx(x, L0_fcc)
        d22 = -dmu_Pb_bct_dy(y, L0_bct)
        det = d11*d22 - d12*d21
        if det == 0:
            break
        dx = (-F1*d22 + F2*d12) / det
        dy = (-d11*F2 + d21*F1) / det
        x += dx
        y += dy
        if abs(dx)+abs(dy) < 1e-12:
            break
    return x, y

def curved_equilibrium(L0_fcc, L0_bct, DG_Sn, DG_Pb, DG_excess):
    """Solve for curved interface (DG_excess added to β phase)"""
    x, y = 0.20, 0.98
    for _ in range(50):
        # μ_Sn^α - μ_Sn^β = -ΔG_Sn + ΔG_excess
        F1 = mu_Sn_fcc(x, L0_fcc) - mu_Sn_bct(y, L0_bct) + DG_Sn - DG_excess
        # μ_Pb^α - μ_Pb^β = ΔG_Pb + ΔG_excess
        F2 = mu_Pb_fcc(x, L0_fcc) - mu_Pb_bct(y, L0_bct) - DG_Pb - DG_excess
        d11 = dmu_Sn_fcc_dx(x, L0_fcc)
        d12 = -dmu_Sn_bct_dy(y, L0_bct)
        d21 = dmu_Pb_fcc_dx(x, L0_fcc)
        d22 = -dmu_Pb_bct_dy(y, L0_bct)
        det = d11*d22 - d12*d21
        if det == 0:
            break
        dx = (-F1*d22 + F2*d12) / det
        dy = (-d11*F2 + d21*F1) / det
        x += dx
        y += dy
        if abs(dx)+abs(dy) < 1e-12:
            break
    return x, y

# --- Calibrate L0_fcc so that flat X_Sn^fcc = 0.1929 ---------------
L0_fcc = 10000.0
target = 0.1929
for _ in range(30):
    x_flat, y_flat = flat_equilibrium(L0_fcc, L0_bct, DG_Sn_fcc_to_bct, DG_Pb_fcc_to_bct)
    err = x_flat - target
    if abs(err) < 1e-8:
        break
    # finite-difference derivative
    dx = 1.0
    x2, _ = flat_equilibrium(L0_fcc + dx, L0_bct, DG_Sn_fcc_to_bct, DG_Pb_fcc_to_bct)
    deriv = (x2 - x_flat) / dx
    if deriv == 0:
        deriv = 1e-6
    L0_fcc -= err / deriv
    L0_fcc = max(0.0, min(5e4, L0_fcc))

# --- Produce output for radii 1–100 nm ----------------------------
radii_nm = [1,2,3,4,5,6,7,8,9,10,15,20,25,30,40,50,60,70,80,90,100]
with open('/app/outputs/pb_sn_gibbs_thomson.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['radius_nm', 'X_Sn_fcc'])
    for r_nm in radii_nm:
        r_m = r_nm * 1e-9
        dG = 2 * sigma * Vm / r_m
        X_Sn_fcc, _ = curved_equilibrium(L0_fcc, L0_bct, DG_Sn_fcc_to_bct, DG_Pb_fcc_to_bct, dG)
        w.writerow([r_nm, X_Sn_fcc])
