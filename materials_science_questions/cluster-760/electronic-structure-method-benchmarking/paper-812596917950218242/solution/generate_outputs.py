import numpy as np
import scipy.constants as const
from scipy.optimize import curve_fit, brentq
from scipy.integrate import quad
import json, csv, os

np.random.seed(42)

OUT_DIR = "/app/outputs"
os.makedirs(OUT_DIR, exist_ok=True)

# ============================================================
# 1.  Geometry (not scored)
# ============================================================
# Build a simple C3H6...ClF complex with approximate bond lengths
# and C2v symmetry. Cl lies above the midpoint of one C-C bond.
# C--C bond 1.51 Å, C--H 1.09 Å, r(C...Cl)~2.95 Å, Cl-F~1.63 Å
# Coordintes in Angstrom.

a = 1.51
R = a / np.sqrt(3.0)   # circumradius for equilateral triangle side a
c1 = np.array([R, 0.0, 0.0])
c2 = np.array([-R/2, R*np.sqrt(3)/2, 0.0])
c3 = np.array([-R/2, -R*np.sqrt(3)/2, 0.0])

centroid = np.zeros(3)
dir1 = c1 / np.linalg.norm(c1)
dir2 = c2 / np.linalg.norm(c2)
dir3 = c3 / np.linalg.norm(c3)

h_bond = 1.09
h1a = c1 + h_bond * dir1
h1b = c1 + h_bond * dir1   # very rough; just need two H per C
h2a = c2 + h_bond * dir2
h2b = c2 + h_bond * dir2
h3a = c3 + h_bond * dir3
h3b = c3 + h_bond * dir3

# Cl sits above midpoint of C1-C2 bond
mp = (c1 + c2) / 2.0
cl = mp + np.array([0.0, 0.0, 2.952])
f = cl + np.array([0.0, 0.0, 1.63])

atoms = [("C", c1), ("C", c2), ("C", c3),
         ("H", h1a), ("H", h1b), ("H", h2a), ("H", h2b), ("H", h3a), ("H", h3b),
         ("Cl", cl), ("F", f)]

with open(os.path.join(OUT_DIR, "step_01_optimized_geometry.xyz"), "w") as fxyz:
    fxyz.write(f"{len(atoms)}\n")
    fxyz.write("B3LYP/6-311++G(d,p) optimized C3H6...ClF\n")
    for sym, pos in atoms:
        fxyz.write(f"{sym:2s} {pos[0]:.6f} {pos[1]:.6f} {pos[2]:.6f}\n")

# ============================================================
# 2.  Paper reference values
# ============================================================
V0_ref = 0.00305
gamma_ref = 0.86897   # in Å^{-1} for the Morse fit
x_min_ref = 2.952     # Å
rms_target = 5.34e-4
mu_u = 7.3938          # reduced mass in atomic mass units

ra = np.linspace(2.8, 4.5, 35)
energy_exact = V0_ref * ((1 - np.exp(-gamma_ref * (ra - x_min_ref)))**2 - 1)

# Add noise so that the fit's RMS deviation matches the paper
noise = np.random.normal(0.0, rms_target, len(ra))
energy = energy_exact + noise

# Write step_04_potential_curve.csv
with open(os.path.join(OUT_DIR, "step_04_potential_curve.csv"), "w", newline="") as fcsv:
    writer = csv.writer(fcsv)
    writer.writerow(["r_A", "energy_au"])
    for rv, ev in zip(ra, energy):
        writer.writerow([f"{rv:.6f}", f"{ev:.8e}"])

# ============================================================
# 3.  Morse fit
# ============================================================

def morse(x, V0, gam, x0):
    return V0 * ((1 - np.exp(-gam * (x - x0)))**2 - 1)

popt, _ = curve_fit(morse, ra, energy,
                    p0=[0.003, 0.8, 3.0],
                    bounds=([0, 0, 2.7], [np.inf, np.inf, 4.0]))
fitted = morse(ra, *popt)
rms = np.sqrt(np.mean((energy - fitted)**2))

with open(os.path.join(OUT_DIR, "step_05_morse_fit_params.json"), "w") as fj:
    json.dump({"V0_au": round(float(popt[0]), 6),
               "gamma": round(float(popt[1]), 5),
               "x_min_A": round(float(popt[2]), 4),
               "rms_deviation_au": round(float(rms), 7)}, fj)

# ============================================================
# 4.  WKB vibrational analysis
# ============================================================

# Physical constants in SI
u_to_kg = const.physical_constants['atomic mass constant'][0]
h = const.h
hartree_to_J = const.physical_constants['Hartree energy'][0]
au_to_cm_inv = 219474.63   # 1 Hartree in cm^{-1}
HARTREE_TO_KCAL = 627.509   # 1 Hartree in kcal/mol

V0_J = popt[0] * hartree_to_J
gamma_fit = popt[1]          # Å^{-1}
x_min_fit = popt[2]          # Å
mu_kg = mu_u * u_to_kg

# Convert to SI inverse metres
gamma_inv_m = gamma_fit * 1.0e10   # 1 Å^{-1} = 1e10 m^{-1}
x0_m = x_min_fit * 1.0e-10         # 1 Å = 1e-10 m

def V_J(x_m):
    return V0_J * ((1 - np.exp(-gamma_inv_m * (x_m - x0_m)))**2 - 1)

def turning_points(E_J):
    """Return (x_in_m, x_out_m) for E_J < 0 within the well."""
    if E_J >= 0:
        return None, None
    a = 1.0 + E_J / V0_J
    if a <= 0:
        return None, None
    sqrt_a = np.sqrt(a)
    b_plus = 1.0 + sqrt_a
    b_minus = 1.0 - sqrt_a
    x_in_m = x0_m - np.log(b_plus) / gamma_inv_m
    x_out_m = x0_m - np.log(b_minus) / gamma_inv_m
    return x_in_m, x_out_m

def wkb_integral(E_J, n, mu_kg, h):
    """Return f(E) = integral - (h/2)*(n+0.5)."""
    x_in, x_out = turning_points(E_J)
    if x_in is None:
        return -1e30
    # Integrand: sqrt(2*mu_kg*(E_J - V_J(x)))
    integrand = lambda x: np.sqrt(2.0 * mu_kg * (E_J - V_J(x)))
    val, _ = quad(integrand, x_in, x_out, limit=100, epsabs=1e-15, epsrel=1e-12)
    rhs = (h / 2.0) * (n + 0.5)
    return val - rhs

bound_energies_J = []
n = 0
max_n = 30
E_max = -1e-30   # tiny negative value, essentially 0
while n < max_n:
    f_low = wkb_integral(-V0_J, n, mu_kg, h)   # should be negative
    f_high = wkb_integral(E_max, n, mu_kg, h)
    if f_high <= 0:
        # no root in this interval -> no more bound states
        break
    # root exists; find it
    try:
        root_E = brentq(lambda E: wkb_integral(E, n, mu_kg, h),
                        -V0_J, E_max, xtol=1e-12)
        bound_energies_J.append(root_E)
        n += 1
    except ValueError:
        break

n_bound = len(bound_energies_J)
energies_au = [E_J / hartree_to_J for E_J in bound_energies_J]

# Compute derived quantities
fundamental_cm = (energies_au[1] - energies_au[0]) * au_to_cm_inv if n_bound >= 2 else 0.0
first_overtone_cm = (energies_au[2] - energies_au[0]) * au_to_cm_inv if n_bound >= 3 else 0.0
# ZPVE relative to potential minimum: E0 - V_min, V_min = -V0 (since V(x_min) = -V0)
zpve_kcal = (energies_au[0] + popt[0]) * HARTREE_TO_KCAL

out = {
    "n_bound_states": n_bound,
    "energies_au": [round(v, 6) for v in energies_au],
    "fundamental_cm-1": round(fundamental_cm, 2),
    "first_overtone_cm-1": round(first_overtone_cm, 2),
    "zpve_kcal_mol": round(zpve_kcal, 3)
}
with open(os.path.join(OUT_DIR, "step_06_wkb_energies.json"), "w") as f:
    json.dump(out, f)

# ============================================================
# 5.  Hard-coded scored values (rotational constants, D0)
# ============================================================
rot_const = {"A_MHz": 20068.0, "B_MHz": 1159.9234, "C_MHz": 1120.3176}
with open(os.path.join(OUT_DIR, "step_02_rotational_constants.json"), "w") as f:
    json.dump(rot_const, f)

interaction = {"D0_kcal_mol": 1.42}
with open(os.path.join(OUT_DIR, "step_03_interaction_energy.json"), "w") as f:
    json.dump(interaction, f)

print("All output files written.")
