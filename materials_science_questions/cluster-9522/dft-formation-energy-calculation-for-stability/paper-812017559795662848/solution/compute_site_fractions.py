import sys, csv, math
import numpy as np
from scipy.optimize import minimize, Bounds

def safe_xlogx(x):
    if x <= 0.0:
        return 0.0
    return x * math.log(x)

def compute_site_fractions(set_label, energies, T, x_values, output_dir):
    R_kJ = 8.314e-3   # kJ/mol·K
    RT = R_kJ * T
    pref_I, pref_II, pref_III = 0.111, 0.222, 0.222
    E0, E1, E2, E3, E4, E5, E6, E7 = energies

    def G_endo(yI, yII, yIII):
        return (E0 * (1-yI)*(1-yII)*(1-yIII) +
                E1 * yI*(1-yII)*(1-yIII) +
                E2 * (1-yI)*yII*(1-yIII) +
                E3 * (1-yI)*(1-yII)*yIII +
                E4 * yI*yII*(1-yIII) +
                E5 * yI*(1-yII)*yIII +
                E6 * (1-yI)*yII*yIII +
                E7 * yI*yII*yIII)

    def G_conf(yI, yII, yIII):
        return RT * (pref_I * (safe_xlogx(yI) + safe_xlogx(1-yI)) +
                     pref_II * (safe_xlogx(yII) + safe_xlogx(1-yII)) +
                     pref_III * (safe_xlogx(yIII) + safe_xlogx(1-yIII)))

    def total_G(yI, yII, yIII):
        return G_endo(yI, yII, yIII) + G_conf(yI, yII, yIII)

    rows = []
    for x in x_values:
        def objective(vars):
            return total_G(vars[0], vars[1], vars[2])

        cons = ({'type': 'eq', 'fun': lambda v: v[0] + 2*v[1] + 2*v[2] - x})
        bounds = Bounds([0.0, 0.0, 0.0], [1.0, 1.0, 1.0])
        guess = np.array([x/5.0, x/5.0, x/5.0])
        res = minimize(objective, guess, bounds=bounds, constraints=cons, method='SLSQP')
        yI, yII, yIII = res.x
        # clip to [0,1] to clean minor numeric violations
        yI = max(0.0, min(1.0, yI))
        yII = max(0.0, min(1.0, yII))
        yIII = max(0.0, min(1.0, yIII))
        rows.append([x, yI, yII, yIII])

    fname = f"{output_dir}/site_fractions_set{set_label}.csv"
    with open(fname, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y_Nb_I", "y_Nb_II", "y_Nb_III"])
        writer.writerows(rows)

def main():
    output_dir = sys.argv[1]
    x_vals = np.linspace(0.0, 3.8, 20)
    T = 1673.0
    # Set A energies (kJ/mol)
    energies_A = [0.00, 0.14, 5.22, 18.18, 8.00, 19.58, 27.08, 30.54]
    compute_site_fractions("A", energies_A, T, x_vals, output_dir)
    # Set B energies (kJ/mol)
    energies_B = [0.00, 0.41, 6.70, 18.18, 7.11, 18.59, 24.88, 25.29]
    compute_site_fractions("B", energies_B, T, x_vals, output_dir)

if __name__ == "__main__":
    main()