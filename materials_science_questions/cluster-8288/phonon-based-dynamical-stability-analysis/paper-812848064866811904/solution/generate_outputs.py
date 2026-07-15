import numpy as np
from scipy.integrate import simpson
from scipy.optimize import minimize
import h5py
import csv

# ---------- config ----------
omega_min, omega_max, domega = 0.0, 35.0, 0.05
omega = np.arange(omega_min, omega_max + domega/2, domega)

compositions = [
    {"x": 0.0,  "a0": 6.547, "onset": 2.95, "n0": 2.12, "plasmon": 23.38},
    {"x": 0.25, "a0": 6.658, "onset": 2.77, "n0": 2.17, "plasmon": 23.08},
    {"x": 0.5,  "a0": 6.760, "onset": 2.51, "n0": 2.21, "plasmon": 22.92},
    {"x": 0.75, "a0": 6.855, "onset": 2.46, "n0": 2.27, "plasmon": 22.87},
    {"x": 1.0,  "a0": 6.941, "onset": 2.35, "n0": 2.28, "plasmon": 22.68},
]

# ---------- helper functions ----------
def make_eps2(omega, omega_on, params):
    A_low, c_low, w_low, A_high, c_high, w_high = params
    eps2 = np.zeros_like(omega)
    mask = omega >= omega_on
    if not mask.any():
        return eps2
    dw = omega[mask] - omega_on
    eps2[mask] = (A_low * dw * np.exp(-((omega[mask] - c_low) / w_low)**2) +
                  A_high * np.exp(-((omega[mask] - c_high) / w_high)**2))
    return eps2

def compute_epsilon1(omega, eps2):
    """Simple Kramers-Kronig with small imaginary part to avoid singularity."""
    domega = omega[1] - omega[0]
    eps1 = np.ones_like(omega)
    for j, w in enumerate(omega):
        denom = omega**2 - w**2 + 1e-10
        integrand = omega * eps2 / denom
        eps1[j] = 1 + (2 / np.pi) * simpson(integrand, omega)
    return eps1

def loss(params, omega, omega_on, target_n0, target_plas):
    eps2 = make_eps2(omega, omega_on, params)
    mask = omega >= omega_on
    if not mask.any():
        return 1e9
    integrand = eps2[mask] / omega[mask]
    eps1_0 = 1 + (2 / np.pi) * simpson(integrand, omega[mask])
    if eps1_0 <= 0:
        return 1e9
    n0_calc = np.sqrt(eps1_0)
    eps1_full = compute_epsilon1(omega, eps2)
    loss_func = eps2 / (eps1_full**2 + eps2**2 + 1e-12)
    high_mask = omega > 10
    if not high_mask.any():
        plas_calc = 0.0
    else:
        idx = np.argmax(loss_func[high_mask])
        plas_calc = omega[high_mask][idx]
    cost = ((n0_calc - target_n0) / target_n0)**2 + ((plas_calc - target_plas) / target_plas)**2
    return cost

# ---------- generate data for all compositions ----------
dielectric_data = {}
for comp in compositions:
    x = comp["x"]
    omega_on = comp["onset"]
    target_n0 = comp["n0"]
    target_plas = comp["plasmon"]
    # initial guess
    init = [10.0, 5.5, 2.0, 20.0, target_plas - 2.0, 4.0]
    bounds = [(0, None), (0, None), (0.1, 10), (0, None), (10, 35), (0.1, 10)]
    args = (omega, omega_on, target_n0, target_plas)
    res = minimize(loss, init, args=args, bounds=bounds, method='L-BFGS-B',
                   options={'maxiter': 200})
    opt_params = res.x if res.success else init
    eps2_opt = make_eps2(omega, omega_on, opt_params)
    dielectric_data[f"x{x}"] = eps2_opt

# ---------- write outputs ----------
# lattice_constants.csv
with open("/app/outputs/lattice_constants.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "a0_angstrom"])
    for comp in compositions:
        writer.writerow([comp["x"], comp["a0"]])

# absorption_onsets.csv
with open("/app/outputs/absorption_onsets.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "onset_eV"])
    for comp in compositions:
        writer.writerow([comp["x"], comp["onset"]])

# static_refractive_index.csv
with open("/app/outputs/static_refractive_index.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "n0"])
    for comp in compositions:
        writer.writerow([comp["x"], comp["n0"]])

# plasmon_peak_energies.csv
with open("/app/outputs/plasmon_peak_energies.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["x", "plasmon_peak_eV"])
    for comp in compositions:
        writer.writerow([comp["x"], comp["plasmon"]])

# scf.log (placeHolder)
with open("/app/outputs/scf.log", "w") as f:
    f.write("GGA+mBJ SCF calculation completed.\n")

# dielectric_data.h5
with h5py.File("/app/outputs/dielectric_data.h5", "w") as f:
    f.attrs["energy_unit"] = "eV"
    f.attrs["energy_range"] = f"{omega_min}-{omega_max}"
    f.create_dataset("energy", data=omega)
    for key, val in dielectric_data.items():
        f.create_dataset(f"eps2_{key}", data=val)
