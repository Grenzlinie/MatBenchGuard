import sys, json, math
from scipy.optimize import fsolve

# Physical constants (cgs)
l = 2.0e-8          # cm (2 Angstrom)
s = 9
t = 6
e_esu = 4.8032047e-10
n = 2.06              # effective Ti charge
p = 8.668
q = 30.081

# Interatomic coefficients (cgs)
lam_OT = 15.6e-82
lam_OO = 113.5e-82
lam_BO = 99.0e-82
lam_BB = 82.7e-82
lam_BT = 12e-82
lam_TT = 1.1e-82

mu_OT = 31.3e-60
mu_OO = 135.0e-60
mu_BO = 162.0e-60
mu_BB = 239.0e-60
mu_BT = 43e-60
mu_TT = 10e-60

# Ionic polarizabilities (cgs)
two_l3 = (2*l)**3
alpha_Ti = 0.0365 * two_l3 / (4 * math.pi)
alpha_Ba = 0.382  * two_l3 / (4 * math.pi)
alpha_O  = 0.470  * two_l3 / (4 * math.pi)

# Function for d(U_overlap+U_Waals)/dΔa  (Eq. 11)
def dU_ow_da(da, db1, db2):
    d = 0.0
    # O-Ti term
    d += -2*s*lam_OT * l**(-s) * (1 - (s+1)*da) + 2*t*mu_OT * l**(-t) * (1 - (t+1)*da)
    # O-O & Ba-O term (first coordination shell)
    d += -s*(4*lam_OO + 4*lam_BO) * l**(-s) * 2**(-s/2) * (1 - s/2*da - (s+2)/4*(db1+db2))
    d +=  t*(4*mu_OO  + 4*mu_BO)  * l**(-t) * 2**(-t/2) * (1 - t/2*da - (t+2)/4*(db1+db2))
    # Ba-Ti term (nearest Ba)
    d += -8*s*lam_BT * l**(-s) * 3**(-(s+2)/2) * (1 - (s-1)/3*da - (s+2)/3*(db1+db2))
    d +=  8*t*mu_BT  * l**(-t) * 3**(-(t+2)/2) * (1 - (t-1)/3*da - (t+2)/3*(db1+db2))
    # second-neighbour diagonal terms
    d += -s*(3*lam_OO + lam_BB + lam_TT) * (2*l)**(-s) * (1 - (s+1)*da)
    d +=  t*(3*mu_OO  + mu_BB  + mu_TT)  * (2*l)**(-t) * (1 - (t+1)*da)
    return d

# Function for d(U_overlap+U_Waals)/dΔb1  (Eq. 12, i=1, j=2)
def dU_ow_db1(da, db1, db2):
    d = 0.0
    # O-Ti
    d += -2*s*lam_OT * l**(-s) * (1 - (s+1)*db1) + 2*t*mu_OT * l**(-t) * (1 - (t+1)*db1)
    # O-O & Ba-O
    d += -s*(4*lam_OO + 4*lam_BO) * l**(-s) * 2**(-s/2) * (1 - s/2*db1 - (s+2)/4*(db2+da))
    d +=  t*(4*mu_OO  + 4*mu_BO)  * l**(-t) * 2**(-t/2) * (1 - t/2*db1 - (t+2)/4*(db2+da))
    # Ba-Ti
    d += -8*s*lam_BT * l**(-s) * 3**(-(s+2)/2) * (1 - (s-1)/3*db1 - (s+2)/3*(db2+da))
    d +=  8*t*mu_BT  * l**(-t) * 3**(-(t+2)/2) * (1 - (t-1)/3*db1 - (t+2)/3*(db2+da))
    # second neighbour
    d += -s*(3*lam_OO + lam_BB + lam_TT) * (2*l)**(-s) * (1 - (s+1)*db1)
    d +=  t*(3*mu_OO  + mu_BB  + mu_TT)  * (2*l)**(-t) * (1 - (t+1)*db1)
    return d

# Coulomb derivatives (Eq. 13)
def dUc_da(da):
    return (49.1 * e_esu**2 / (6*l)) * (1 - 2*da)
def dUc_db1(db1):
    return (49.1 * e_esu**2 / (6*l)) * (1 - 2*db1)

# Two on-site potential coefficients a(Δa,Δb1,Δb2) and b(...)
# Using the numerical expressions from the paper with db1=db2=db.
def a_coeff(da, db):
    # a = 5.123e5 -7.130e6 da + 6.954e5 db1 + 6.954e5 db2 + 4.340e7 da^2
    #     -4.2605e6 db1^2 -4.2605e6 db2^2
    a = (5.123e5
         - 7.130e6 * da
         + 6.954e5 * db + 6.954e5 * db
         + 4.340e7 * da**2
         - 4.2605e6 * db**2 - 4.2605e6 * db**2)
    return a

def b_coeff(da, db):
    # b = 1.895e22 -2.374e23 da -5.760e21 db1 -5.760e21 db2
    #     + 1.673e24 da^2 +4.087e22 db1^2 +4.087e22 db2^2
    b = (1.895e22
         - 2.374e23 * da
         - 5.760e21 * db - 5.760e21 * db
         + 1.673e24 * da**2
         + 4.087e22 * db**2 + 4.087e22 * db**2)
    return b

# Derivatives of a and b with respect to Δa and Δb (db1=db2=db)
def d_a_dDa(da, db):
    # ∂a/∂Δa = -7.130e6 + 2*4.340e7*da
    return -7.130e6 + 2*4.340e7*da
def d_a_dDb(da, db):
    # ∂a/∂Δb = 2*6.954e5 - 2*4.2605e6*db - 2*4.2605e6*db  ???
    # Actually a = ... + 6.954e5*(db1+db2) -4.2605e6*(db1^2+db2^2)
    # ∂a/∂db1 = 6.954e5 -2*4.2605e6*db1, same for db2.
    # With db1=db2=db, total derivative wrt db (treating both equal) is 2*(6.954e5 - 2*4.2605e6*db) ?? 
    # But equilibrium equation uses ∂U/∂Δb1, not total. So we need derivative of a with respect to Δb1 only, treating db2 as independent.
    # In the residual for R1 (Δa eq), we have ∂a/∂Δa, ∂b/∂Δa. Those are straightforward.
    # For R2 (Δb1 eq), we need ∂a/∂Δb1, ∂b/∂Δb1. So we implement for db1 only.
    # So we need functions for db1 specifically.
    # We'll implement separate functions for db1 and db2.
    pass

# We'll therefore implement a and b as functions of da, db1, db2, and their derivatives wrt db1.
# Re-define:

def a_coeff_full(da, db1, db2):
    a = (5.123e5
         - 7.130e6 * da
         + 6.954e5 * db1 + 6.954e5 * db2
         + 4.340e7 * da**2
         - 4.2605e6 * db1**2 - 4.2605e6 * db2**2)
    return a

def b_coeff_full(da, db1, db2):
    b = (1.895e22
         - 2.374e23 * da
         - 5.760e21 * db1 - 5.760e21 * db2
         + 1.673e24 * da**2
         + 4.087e22 * db1**2 + 4.087e22 * db2**2)
    return b

def d_a_dDa_full(da, db1, db2):
    return -7.130e6 + 2*4.340e7*da

def d_b_dDa_full(da, db1, db2):
    return -2.374e23 + 2*1.673e24*da

def d_a_dDb1_full(da, db1, db2):
    return 6.954e5 - 2*4.2605e6*db1

def d_b_dDb1_full(da, db1, db2):
    return -5.760e21 + 2*4.087e22*db1

# Dipole coefficient a0' and a'(Δa)
a0_prime = 0.1974 * (n * e_esu)**2 / (2 * alpha_Ti)

def a_prime(da):
    return a0_prime * (1 - 7.30 * da)

def d_aprime_dDa():
    return -7.30 * a0_prime

# Equilibrium equations residuals (Eqs. 27A and 27B with Δb1=Δb2=Δb)
def residuals(vars):
    da, db = vars
    db1 = db
    db2 = db

    # Non-polar part gradients
    G_a = dU_ow_da(da, db1, db2) + dUc_da(da)
    G_b = dU_ow_db1(da, db1, db2) + dUc_db1(db1)

    # On-site coefficients
    a_val = a_coeff_full(da, db1, db2)
    b_val = b_coeff_full(da, db1, db2)
    ap_val = a_prime(da)

    sum_a = ap_val + a_val
    if b_val == 0:
        return [1e10, 1e10]  # degenerate

    factor1 = sum_a / (2 * b_val)
    factor2 = sum_a**2 / (4 * b_val**2)

    # Derivatives
    da_da = d_a_dDa_full(da, db1, db2)
    db_da = d_b_dDa_full(da, db1, db2)
    da_db = d_a_dDb1_full(da, db1, db2)
    db_db = d_b_dDb1_full(da, db1, db2)
    daprima_da = d_aprime_dDa()
    daprima_db = 0.0

    # Residuals
    R_a = G_a - factor1 * (daprima_da + da_da) + factor2 * db_da
    R_b = G_b - factor1 * (daprima_db + da_db) + factor2 * db_db
    return [R_a, R_b]

# Solve
initial_guess = [0.00811, 0.00811]   # cubic equilibrium
sol = fsolve(residuals, initial_guess, maxfev=1000, xtol=1e-12)
sol = fsolve(residuals, sol, maxfev=1000, xtol=1e-12)  # refine

da_opt, db_opt = sol

# Compute Ti shift x
ap_opt = a_prime(da_opt)
a_opt  = a_coeff_full(da_opt, db_opt, db_opt)
b_opt  = b_coeff_full(da_opt, db_opt, db_opt)
if ap_opt + a_opt >= 0:
    # Should not happen for n=2.06, but fallback
    x_cm = 0.0
else:
    x_cm = math.sqrt( -(ap_opt + a_opt) / (2 * b_opt) )

x_ang = x_cm / 1e-8  # convert cm to Angstrom

output = {
    "delta_a": round(da_opt, 8),
    "delta_b": round(db_opt, 8),
    "ti_shift": round(x_ang, 8)
}

json.dump(output, sys.stdout, indent=2)
