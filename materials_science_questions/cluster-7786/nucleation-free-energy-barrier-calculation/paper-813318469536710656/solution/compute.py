import sys
import csv
import numpy as np
from scipy import integrate, optimize

R = 8.314
NA = 6.022e23
b = 1.0911    # fcc {111}
psi = 2
xi = 0.5

# ---------- material parameters ----------
metals = {
    'Silver': {
        'Tm': 1234.0,
        'delta_Sf': 9.16,
        'gamma': 2.40,
        'Vs': 11.16e-6,
        'Vl': 11.54e-6,
        'c_pl': 30.56,
        'c_ps_func': lambda T: 21.31 + 8.54e-3*T + 1.51e5 / T**2,
        'nucleation_T': [983.0, 978.0, 974.0]
    },
    'Copper': {
        'Tm': 1356.0,
        'delta_Sf': 9.59,
        'gamma': 1.96,
        'Vs': 7.61e-6,
        'Vl': 7.91e-6,
        'c_pl': 33.00,
        'c_ps_func': lambda T: 22.65 + 6.28e-3*T,
        'nucleation_T': [1090.0, 1079.0]
    },
    'Nickel': {
        'Tm': 1728.0,
        'delta_Sf': 10.22,
        'gamma': 2.01,
        'Vs': 7.11e-6,
        'Vl': 7.56e-6,
        'c_pl': 38.52,
        'c_ps_func': lambda T: np.where(T <= 1400,
                            -10.87 + 54.67e-3*T + 56.48e5 / T**2 - 16.49e-6 * T**2,
                            36.19),
        'nucleation_T': [1387.0, 1362.0]
    }
}

def solve_xstar(alpha):
    """Find x* for alpha > 2. We pick the branch x<0.5."""
    def f(x):
        return (np.log(1-x) - np.log(x)) / (1-2*x) - alpha
    # bracket (0.001, 0.5)
    sol = optimize.root_scalar(f, bracket=[0.001, 0.5], method='brentq')
    return sol.root

def compute_metal(metal, params):
    Tm = params['Tm']
    delta_Sf = params['delta_Sf']
    gamma = params['gamma']
    Vs = params['Vs']
    Vl = params['Vl']
    c_pl = params['c_pl']
    c_ps_func = params['c_ps_func']

    As = b * (Vs**2 * NA) ** (1/3)

    # phi0 (Eq.5)
    phi0 = 1.0 - (3*gamma*R/delta_Sf) * np.log((xi*(Vl+Vs))/Vs)

    rows = []
    temperatures = [Tm] + params['nucleation_T']
    for T in temperatures:
        if T == Tm:
            delta_Sf_T = delta_Sf
        else:
            # integrate (c_pl - c_ps)/T' from T to Tm
            def integrand(Tprime):
                return (c_pl - c_ps_func(Tprime)) / Tprime
            I, _ = integrate.quad(integrand, T, Tm, limit=200)
            delta_Sf_T = delta_Sf - I

        # phi0^T (Eq.9)
        phi0_T = phi0 + (delta_Sf_T - delta_Sf) / delta_Sf

        alpha_T = psi * phi0_T * delta_Sf / R

        if alpha_T <= 2.0:
            xstar = 0.5
        else:
            xstar = solve_xstar(alpha_T)

        # phi^T (Eq.22)
        term1 = (1.0 + (delta_Sf_T - delta_Sf) / (phi0 * delta_Sf)) * (1.0 + psi * xstar * (1-xstar))
        term2 = (R / (phi0 * delta_Sf)) * (xstar * np.log(xstar) + (1-xstar)*np.log(1-xstar))
        phi = phi0 * (term1 + term2)

        # sigma^T (J/m^2)
        sigma = phi * T * delta_Sf / As

        # Turnbull coefficient C (Eq.23)
        C = phi * T / (b * Tm)

        rows.append([metal, f'{T:.6g}', f'{sigma:.7g}', f'{phi:.7g}', f'{C:.7g}'])

    return rows

if __name__ == '__main__':
    out_path = sys.argv[1]
    all_rows = []
    for metal, params in metals.items():
        rows = compute_metal(metal, params)
        all_rows.extend(rows)

    with open(out_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['metal', 'temperature_K', 'sigma_J_per_m2', 'phi', 'C'])
        writer.writerows(all_rows)
