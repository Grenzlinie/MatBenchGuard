import sys
import json
import csv
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

# ----------------------------------------------------------------------
# Global parameters (all in units of midgap frequency omega_o = 1)
# ----------------------------------------------------------------------
OMEGA_O = 1.0
R = 0.15                              # gap ratio
DELTA = R * OMEGA_O                   # 0.15
OMEGA_V = OMEGA_O - DELTA/2           # 0.925
OMEGA_C = OMEGA_O + DELTA/2           # 1.075

# Bound‑state regime
OMEGA10_BS = DELTA / 10               # 0.015
GAMMA20    = DELTA / 100              # 0.0015
GAMMA21    = GAMMA20
OMEGA20_BS = 0.95 * OMEGA_C           # 1.02125

# Continuous‑spectrum regime
OMEGA20_SPEC = 1.2 * OMEGA_C          # 1.29
OMEGA21_LIST = [1.15*OMEGA_C, 1.05*OMEGA_C, OMEGA_C, OMEGA_O]

# Numerical regularisation for FDM (tiny, keeps integrals finite)
KAPPA_FDM = 1e-6

# Integration limits
LARGE = 30.0
# ----------------------------------------------------------------------

# --- Form factors ----------------------------------------------------
def z_pbg(w):
    """Eq. (55) with no phenomenological damping."""
    if OMEGA_V < w < OMEGA_C:
        return 0.0
    if w < OMEGA_V:
        # Both (w-OMEGA_V) and (w-OMEGA_C) negative -> product positive
        return abs(w - OMEGA_O) / np.sqrt((OMEGA_V - w)*(OMEGA_C - w))
    else:
        return abs(w - OMEGA_O) / np.sqrt((w - OMEGA_V)*(w - OMEGA_C))

def z_fdm(w):
    """Eq. (59) with a tiny regularisation kappa."""
    if OMEGA_V < w < OMEGA_C:
        return 0.0
    num = w**2 - 2*OMEGA_V*w + OMEGA_V*OMEGA_C
    den = (w - OMEGA_V)**2 + KAPPA_FDM**2
    return num / den

# --- Self‑energy computation -----------------------------------------
def _compute_Sigma(medium, omega10_val, epsilon):
    """Return (Sigma_prime, Sigma_dprime) for given medium and frequency."""
    if medium == 'pbg':
        z_func = z_pbg
        intervals = [(-LARGE, OMEGA_V), (OMEGA_C, LARGE)]
    else:
        z_func = z_fdm
        intervals = [(-LARGE, OMEGA_V), (OMEGA_C, LARGE)]

    offsets = [epsilon, epsilon - omega10_val]
    gamma   = [GAMMA20, GAMMA21]  # use the same small values for both transitions

    Sigma_prime = 0.0
    for gi, g in enumerate(gamma):
        eps = offsets[gi]
        for a, b in intervals:
            if eps <= a or eps >= b:
                # Regular integral – no pole on contour
                def f_reg(w):
                    return z_func(w) / (w - eps)
                I, _ = quad(f_reg, a, b, limit=200, epsabs=1e-12, epsrel=1e-12)
            else:
                # Cauchy principal value
                def f_cauchy(w):
                    return z_func(w)
                I, _ = quad(f_cauchy, a, b, weight='cauchy', wvar=eps,
                            limit=200, epsabs=1e-12, epsrel=1e-12)
            Sigma_prime += g * I / (2*np.pi)

    # Imaginary part: Eq. (22b)
    zw1 = z_func(epsilon)
    zw2 = z_func(epsilon - omega10_val)
    Sigma_dprime = 0.5 * (GAMMA20*zw1 + GAMMA21*zw2)
    return Sigma_prime, Sigma_dprime

# --- Bound state search ----------------------------------------------
def _find_bound_state(medium):
    """Solve omega20 - eps - Sigma'(eps) = 0 inside G'."""
    omega10_val = OMEGA10_BS
    lo = OMEGA_V + omega10_val
    hi = OMEGA_C
    # Sample on a fine grid to bracket the root
    eps_vals = np.linspace(lo, hi, 1000)
    f = np.array([OMEGA20_BS - ep - _compute_Sigma(medium, omega10_val, ep)[0]
                  for ep in eps_vals])
    sign = np.sign(f)
    crossings = np.where(np.diff(sign))[0]
    if len(crossings) == 0:
        return False, None
    a = eps_vals[crossings[0]]
    b = eps_vals[crossings[0]+1]
    try:
        root = brentq(lambda ep: OMEGA20_BS - ep - _compute_Sigma(medium, omega10_val, ep)[0],
                      a, b, xtol=1e-12)
        _, Sdpp = _compute_Sigma(medium, omega10_val, root)
        if abs(Sdpp) < 1e-12:
            return True, float(root)
        else:
            return False, None
    except Exception:
        return False, None

# --- Spectrum computation --------------------------------------------
def _spectrum(medium, omega20, omega21, det_grid):
    """Return list of (omega21, detuning, sigma_R) rows."""
    omega10_val = omega20 - omega21
    rows = []
    for det in det_grid:
        w = omega20 + det
        Sp, Spp = _compute_Sigma(medium, omega10_val, w)
        if medium == 'pbg':
            zw = z_pbg(w)
        else:
            zw = z_fdm(w)
        den = (omega20 - w - Sp)**2 + Spp**2
        if den == 0:
            sig = 0.0
        else:
            sig = GAMMA20**2 * zw**2 / den
        rows.append([omega21, det, sig])
    return rows

# --- Writers ---------------------------------------------------------
def write_bound_state():
    exists_pbg, eig_pbg = _find_bound_state('pbg')
    exists_fdm, eig_fdm = _find_bound_state('fdm')
    result = {
        "pbg_bound_state_exists": bool(exists_pbg),
        "pbg_eigenvalue": float(eig_pbg) if exists_pbg else None,
        "fdm_bound_state_exists": bool(exists_fdm),
        "fdm_eigenvalue": float(eig_fdm) if exists_fdm else None
    }
    with open('/app/outputs/bound_state_result.json', 'w') as f:
        json.dump(result, f, indent=2)

def write_spectrum(medium, filename):
    det_grid = np.linspace(-0.5, 0.5, 500)
    with open(f'/app/outputs/{filename}', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['omega21', 'omega_minus_omega20', 'sigma_R'])
        for om21 in OMEGA21_LIST:
            rows = _spectrum(medium, OMEGA20_SPEC, om21, det_grid)
            for row in rows:
                writer.writerow(row)

# ----------------------------------------------------------------------
if __name__ == '__main__':
    target = sys.argv[1]
    if target == 'bound_state_result.json':
        write_bound_state()
    elif target == 'rayleigh_spectrum_pbg.csv':
        write_spectrum('pbg', 'rayleigh_spectrum_pbg.csv')
    elif target == 'rayleigh_spectrum_fdm.csv':
        write_spectrum('fdm', 'rayleigh_spectrum_fdm.csv')
    else:
        raise ValueError(f'Unknown output: {target}')
