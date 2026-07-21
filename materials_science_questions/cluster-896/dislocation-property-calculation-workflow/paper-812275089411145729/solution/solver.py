import numpy as np
from scipy.optimize import minimize, brentq
import sys, json, csv, os

# material parameters (all units consistent: GPa, nm)
lambda_ = 60.0
mu_ = 60.0
b = 0.23       # Burgers vector, nm
beta = 4.0     # core factor

def E_overlayer(B, C, D, alpha, f, Ro):
    """Eq. 11 in the paper"""
    term_lambda = lambda_ * (3*C**2 + 8*C*(D - 4*B*alpha) + 6*(D - 4*B*alpha)**2)
    term_mu = mu_ * (-16*B*C*alpha + B**2*(3 + 96*alpha**2) + 2*(3*C**2*(1 + 4*alpha**2) + 8*C*D + 6*D**2))
    prefactor = np.pi * Ro**3 / (48 * alpha)
    return prefactor * (term_lambda + term_mu)

def E_underlayer(B, C, D, alpha, f, Ro):
    """Eq. 12 in the paper"""
    delta = B - f
    fac = 1.0 - f  # (1-f)
    term_lambda = lambda_ * (3*C**2 + 8*C*(D + 4*delta*fac*alpha) + 6*(D + 4*delta*fac*alpha)**2)
    term_mu = mu_ * (16*C*delta*fac*alpha + delta**2*(3 + 96*fac**2*alpha**2) +
                     2*(8*C*D + 6*D**2 + 3*C**2*(1 + 4*fac**2*alpha**2)))
    prefactor = np.pi * Ro**3 / (48 * (1.0 - f)**4 * alpha)
    return prefactor * (term_lambda + term_mu)

def E_el_total(params, f, Ro):
    B, C, D, alpha = params
    return E_overlayer(B, C, D, alpha, f, Ro) + E_underlayer(B, C, D, alpha, f, Ro)

def coherent_energy_min(f, Ro):
    """
    Minimize the total coherent elastic energy over B, C, D, alpha.
    Returns (minimum energy, optimal params).
    """
    B0 = f / 2.0
    C0 = 0.0
    D0 = 0.0
    alpha0 = 0.5
    bounds = [(0.0, f), (None, None), (None, None), (1e-6, 10.0)]
    res = minimize(E_el_total, [B0, C0, D0, alpha0], args=(f, Ro),
                   bounds=bounds, method='L-BFGS-B')
    if not res.success:
        # fallback to Nelder-Mead
        res = minimize(E_el_total, [B0, C0, D0, alpha0], args=(f, Ro),
                       method='Nelder-Mead')
    return res.fun, res.x

def dislocation_energy(Ro):
    """
    Energy of one perpendicular edge dislocation pair (n=1) – Eq. 18.
    """
    prefactor = 4.0 * Ro * (b**2 / (2.0 * np.pi)) * (mu_ * (lambda_ + mu_)) / (lambda_ + 2.0 * mu_)
    return prefactor * np.log(Ro * beta / b)

def energy_difference(Ru, f):
    """
    E1(Ru) - E0(Ru) for a given underlayer radius.
    Used for root-finding to locate the critical radius.
    """
    Ro = (1.0 - f) * Ru
    E0, _ = coherent_energy_min(f, Ro)
    f_res = f - b / (2.0 * Ro)
    if f_res < 0.0:
        f_res = 0.0
    E_coh_res, _ = coherent_energy_min(f_res, Ro)
    E1 = E_coh_res + dislocation_energy(Ro)
    return E1 - E0

def compute_critical_radii(output_dir):
    f_values = [0.01, 0.02, 0.03]
    results = []
    for f in f_values:
        # brackets informed by the paper’s approximate values: 60, 25, 15 nm
        if f == 0.01:
            low, high = 30.0, 100.0
        elif f == 0.02:
            low, high = 15.0, 50.0
        else:
            low, high = 8.0, 30.0
        try:
            Ru_star = brentq(lambda Ru: energy_difference(Ru, f), low, high, xtol=1e-6)
        except ValueError:
            # bracket too narrow; widen
            Ru_star = brentq(lambda Ru: energy_difference(Ru, f), 0.1, 200.0, xtol=1e-6)
        results.append((f, Ru_star))
    filepath = os.path.join(output_dir, 'critical_radii.csv')
    with open(filepath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['f', 'R_u_star'])
        for f_val, r_val in results:
            writer.writerow([f_val, r_val])
    print(f'written {filepath}')

def compute_validation_energy(output_dir):
    f = 0.01
    Ru = 30.0
    Ro = (1.0 - f) * Ru
    E0_star, opt_params = coherent_energy_min(f, Ro)
    data = {"f": f, "R_u": Ru, "E0_star": E0_star}
    filepath = os.path.join(output_dir, 'coherent_energy_validation.json')
    with open(filepath, 'w') as fh:
        json.dump(data, fh)
    print(f'written {filepath}')

if __name__ == '__main__':
    target = sys.argv[1]
    outdir = sys.argv[2]
    if target == 'critical_radii':
        compute_critical_radii(outdir)
    elif target == 'validation_energy':
        compute_validation_energy(outdir)
    else:
        print(f'unknown target {target}', file=sys.stderr)
        sys.exit(1)
