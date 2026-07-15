import sys, math
import numpy as np
import sympy as sp
import csv

outpath = sys.argv[1]

# given mesoscopic parameters
a_val = 85e-6
chi_val = 13.1
h0_val = 300e-6
rho0_val = 1.5e-3
n_val = 1e10/(2*math.pi)
mu_shear_val = 1.0
R_val = 2e-3
mu0_val = 4*math.pi*1e-7
H_val = 1.0

# symbolic variables
a, chi, h0, rho0, n_, mu, R, mu0, H, q0 = sp.symbols('a chi h0 rho0 n_ mu R mu0 H q0', positive=True)
z1, z3, z4, z6 = sp.symbols('z1 z3 z4 z6')

# mesoscopic A (Eq 16)
denom_s = sp.sqrt(h0**2 + 4*rho0**2*sp.sin(q0*h0/2)**2)
A_meso = -8*sp.pi*n_*a**6 * (chi/(chi+3))**2 * ( (4*rho0**4*sp.sin(q0*h0/2)**4 - 10*h0**2*rho0**2*sp.sin(q0*h0/2)**2 + h0**4) / (mu * denom_s) ) * mu0*H**2

# mesoscopic tau (Eq 17)
tau_meso = -96*sp.pi*n_*a**6 * (chi/(chi+3))**2 * h0*rho0**2 * ( (h0**2 - rho0**2*sp.sin(q0*h0/2)**2) * sp.sin(q0*h0) / (mu * R**2 * denom_s) ) * mu0*H**2

# mesoscopic M_phi coefficients (Eq 18)
M0_meso = 24*sp.pi*n_*a**6*(chi/(chi+3))**2 * (h0*rho0*sp.sin(q0*h0)/denom_s) * H
MA_meso = 36*sp.pi*n_*a**6*(chi/(chi+3))**2 * h0*rho0 * ( (8*rho0**2*sp.sin(q0*h0/2)**2 - 3*h0**2) / denom_s ) * sp.sin(q0*h0) * H
Mtau_meso = 12*sp.pi*n_*a**6*(chi/(chi+3))**2 * h0**2*rho0 * ( (2*h0**2*sp.cos(q0*h0) - rho0**2*(9*sp.sin(q0*h0/2) + sp.sin(3*q0*h0/2)) ) / denom_s ) * H

MA_meso_coeff = MA_meso / H   # coefficient of H*A
Mtau_meso_coeff = Mtau_meso / H

# macroscopic alpha_parallel, alpha_perp (Eqs 47‑48)
term_a = 4*sp.pi*n_*chi*a**3 * (q0*R - sp.atan(q0*R)) * ( (chi+3)*denom_s + 4*chi*a**3*(h0**2 - rho0**2 + rho0**2*sp.cos(q0*h0)) )
term_b = 3*chi*a**3*rho0*h0*sp.sin(q0*h0) * ( q0**2*R**2 - sp.log(1+q0**2*R**2) )
term_c = 3*chi*a**3*rho0*h0*sp.sin(q0*h0) * sp.log(1+q0**2*R**2)
alpha_parallel = mu0*(chi+3)**2 * (q0*R - sp.atan(q0*R)) * denom_s / (term_a + term_b)
alpha_perp    = mu0*(chi+3)**2 * (q0*R - sp.atan(q0*R)) * denom_s / (term_a - term_c)

# common numerator used in macroscopic expressions
num_zeta = z1*alpha_perp**2 + z3*(alpha_perp**2 - alpha_parallel**2) + 2*z4*alpha_perp*(alpha_perp - alpha_parallel) + z6*(alpha_perp - alpha_parallel)**2

# macroscopic A (Eq 43)
termA1 = ((alpha_parallel - alpha_perp)/(alpha_parallel*alpha_perp)) * ( (3/(2*q0**2))*sp.log(1+q0**2*R**2) - (3*R**2)/(2*(1+q0**2*R**2)) )
termA2 = ( num_zeta / (alpha_parallel**2*alpha_perp**2) ) * ( (3/4)*(R**2)/(1+q0**2*R**2) - (1/(4*q0**2))*sp.log(1+q0**2*R**2) )
termA3 = ( z3 / alpha_perp**2 ) * ( (sp.Rational(1,4))*R**2 - (3/(4*q0**2))*sp.log(1+q0**2*R**2) )
termA4 = 2 * ( (z4*alpha_parallel*alpha_perp + z6*alpha_parallel*(alpha_perp - alpha_parallel)) / (alpha_parallel**2*alpha_perp**2) ) * (1/(2*q0**2))*sp.log(1+q0**2*R**2)
termA5 = ( z6/alpha_perp**2 ) * (R**2/2)
A_macro = -1/(3*mu*R**2) * ( termA1 - termA2 + termA3 - termA4 - termA5 ) * mu0**2*H**2

# macroscopic tau (Eq 44)
termT1 = ((alpha_parallel - alpha_perp)/(alpha_parallel*alpha_perp)) * ( (1/(2*q0**2))*sp.log(1+q0**2*R**2) - R**2/(2*(1+q0**2*R**2)) )
termT2 = (sp.Rational(1,2)) * ( num_zeta / (alpha_parallel**2*alpha_perp**2) ) * ( (1/(2*q0**2))*sp.log(1+q0**2*R**2) - R**2/(2*(1+q0**2*R**2)) )
termT3 = (sp.Rational(1,2)) * ( z3 / alpha_perp**2 ) * ( R**2/2 - (1/(2*q0**2))*sp.log(1+q0**2*R**2) )
termT4 = (sp.Rational(1,2)) * ( (z4*alpha_parallel*alpha_perp + z6*alpha_parallel*(alpha_perp - alpha_parallel)) / (alpha_parallel**2*alpha_perp**2) ) * ( R**2/2 - (1/(2*q0**2))*sp.log(1+q0**2*R**2) )
tau_macro = (4/(mu*q0*R**4)) * ( termT1 + termT2 + termT3 + termT4 ) * mu0**2*H**2

# macroscopic M_phi linear in A and tau (from Eq 45)
r = sp.symbols('r', positive=True)
MA_macro_coeff_r = ((alpha_parallel - alpha_perp)/(alpha_parallel*alpha_perp)) * (3*q0*r*(1 - q0**2*r**2))/(2*(1+q0**2*r**2)**2) + ( num_zeta / (alpha_parallel**2*alpha_perp**2) ) * (q0*r*(1 - q0**2*r**2/2))/(1+q0**2*r**2)**2 + (sp.Rational(1,2))*((z4+z6)/(alpha_parallel*alpha_perp)) * (q0*r)/(1+q0**2*r**2) - (sp.Rational(1,2))*(z6/alpha_perp**2) * (q0*r)/(1+q0**2*r**2)
MA_int = sp.integrate(r * MA_macro_coeff_r, (r, 0, R))
MA_macro_avg = (2/R**2) * MA_int

MT_coeff_r_per_q0 = ((alpha_perp - alpha_parallel)/(alpha_parallel*alpha_perp)) * (q0*r*(1 - q0**2*r**2))/(1+q0**2*r**2)**2 + ( num_zeta / (alpha_parallel**2*alpha_perp**2) ) * (q0**3 * r**3)/(1+q0**2*r**2)**2 + (sp.Rational(1,2))*((z4+z6)/(alpha_parallel*alpha_perp)) * q0*r
Mtau_macro_coeff_r = MT_coeff_r_per_q0 / q0
Mtau_int = sp.integrate(r * Mtau_macro_coeff_r, (r, 0, R))
Mtau_macro_avg = (2/R**2) * Mtau_int

# constant substitutions
subs_const = {a: a_val, chi: chi_val, h0: h0_val, rho0: rho0_val, n_: n_val, mu: mu_shear_val, R: R_val, mu0: mu0_val, H: H_val}

# grid of scaled initial twist
q0h0_vals = np.linspace(-2, 2, 201)
rows = []

for q0h0_val in q0h0_vals:
    q0_num = q0h0_val / h0_val
    if abs(q0_num) < 1e-12:
        q0_num = 1e-12
    subs_loop = dict(subs_const)
    subs_loop[q0] = q0_num

    # alpha values
    alpha_p_val  = alpha_parallel.subs(subs_loop).evalf()
    alpha_perp_val = alpha_perp.subs(subs_loop).evalf()

    # mesoscopic targets
    A_meso_val   = A_meso.subs(subs_loop).evalf()
    tau_meso_val = tau_meso.subs(subs_loop).evalf()
    MA_meso_coeff_val = MA_meso_coeff.subs(subs_loop).evalf()
    Mtau_meso_coeff_val = Mtau_meso_coeff.subs(subs_loop).evalf()

    # substitution for large expressions
    subs_known = dict(subs_const)
    subs_known[q0] = q0_num
    subs_known[alpha_parallel] = alpha_p_val
    subs_known[alpha_perp] = alpha_perp_val

    # --- A_macro equation ---
    Am_sub = A_macro.subs(subs_known)
    A0 = Am_sub.subs({z1:0,z3:0,z4:0,z6:0}).evalf()
    rhs_A = A_meso_val - A0
    coeff_A = [Am_sub.diff(v).evalf() for v in (z1,z3,z4,z6)]

    # --- tau_macro equation ---
    Tm_sub = tau_macro.subs(subs_known)
    tau0 = Tm_sub.subs({z1:0,z3:0,z4:0,z6:0}).evalf()
    rhs_tau = tau_meso_val - tau0
    coeff_tau = [Tm_sub.diff(v).evalf() for v in (z1,z3,z4,z6)]

    # --- MA_macro_avg equation ---
    MA_sub = MA_macro_avg.subs(subs_known)
    MA0 = MA_sub.subs({z1:0,z3:0,z4:0,z6:0}).evalf()
    coeff_MA = [MA_sub.diff(v).evalf() for v in (z1,z3,z4,z6)]
    coeff_MA_scaled = [c * mu0_val for c in coeff_MA]
    rhs_MA = MA_meso_coeff_val - mu0_val * MA0

    # --- Mtau_macro_avg equation ---
    Mt_sub = Mtau_macro_avg.subs(subs_known)
    Mt0 = Mt_sub.subs({z1:0,z3:0,z4:0,z6:0}).evalf()
    coeff_Mt = [Mt_sub.diff(v).evalf() for v in (z1,z3,z4,z6)]
    coeff_Mt_scaled = [c * mu0_val for c in coeff_Mt]
    rhs_Mt = Mtau_meso_coeff_val - mu0_val * Mt0

    # solve 4x4 system
    A_mat = np.array([coeff_A, coeff_tau, coeff_MA_scaled, coeff_Mt_scaled], dtype=float)
    rhs_vec = np.array([rhs_A, rhs_tau, rhs_MA, rhs_Mt], dtype=float)
    try:
        zeta_sol = np.linalg.solve(A_mat, rhs_vec)
    except np.linalg.LinAlgError:
        zeta_sol = np.zeros(4)
    z1_v, z3_v, z4_v, z6_v = zeta_sol[0], zeta_sol[1], zeta_sol[2], zeta_sol[3]

    rows.append([q0h0_val, float(A_meso_val), float(tau_meso_val),
                 float(alpha_p_val), float(alpha_perp_val),
                 float(z1_v), float(z3_v), float(z4_v), float(z6_v)])

# write CSV
with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["q0h0","A","tau","alpha_parallel","alpha_perp","zeta1","zeta3","zeta4","zeta6"])
    w.writerows(rows)
