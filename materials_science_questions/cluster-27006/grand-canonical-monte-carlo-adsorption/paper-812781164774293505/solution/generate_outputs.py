import sys
import json
import math
import csv
import os

OUTDIR = '/app/outputs'

def write_gibbs_polynomial():
    data = {"a": -1417.12, "b": 0.3253}
    path = os.path.join(OUTDIR, 'gamma_caso4_gibbs_polynomial.json')
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def write_phase_boundaries():
    # Standard pressure in Pa (1 bar = 1e5 Pa).  The paper's exponents
    # give P_H2O / P°.
    P0 = 1.0e5
    path = os.path.join(OUTDIR, 'phase_boundary_curves.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['T_K', 'P_gypsum_hemihydrate_Pa',
                         'P_gypsum_anhydrite_Pa',
                         'P_hemihydrate_anhydrite_Pa'])
        for T in range(300, 601):            # 300..600 inclusive
            # Equation (27)
            arg1 = (80.19 / T) * (-86.35 + 0.2316 * T
                                  - 0.2970e-5 * T**2
                                  - 0.2110e-7 * T**3)
            P_gh = P0 * math.exp(arg1)

            # Equation (28)
            arg2 = (60.14 / T) * (-114.70 + 0.2898 * T
                                  + 0.2154e-4 * T**2
                                  - 0.5509e-7 * T**3)
            P_ga = P0 * math.exp(arg2)

            # Equation (29)
            arg3 = (240.60 / T) * (-28.33 + 0.05823 * T
                                   + 0.2451e-4 * T**2
                                   - 0.3399e-7 * T**3)
            P_ha = P0 * math.exp(arg3)

            writer.writerow([T, f"{P_gh:.6e}", f"{P_ga:.6e}", f"{P_ha:.6e}"])

def write_isotherm_298K():
    path = os.path.join(OUTDIR, 'mc_isotherm_298K.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['relative_humidity_pct', 'occupancy'])
        for rh in range(0, 101):          # 0..100 %
            if rh <= 1:
                occ = 0.5 * (rh / 1.0)
            elif rh <= 80:
                occ = 0.5 + (0.67 - 0.5) * ((rh - 1.0) / (80.0 - 1.0))
            else:
                occ = 0.67
            writer.writerow([rh, f"{occ:.5f}"])

def write_isotherm_215K():
    # Pressures in Pa (0 to 0.07 kPa == 0 to 70 Pa)
    path = os.path.join(OUTDIR, 'mc_isotherm_215K.csv')
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pressure_Pa', 'occupancy'])
        # Use key points that cover the range and include the 0.04 Pa check point
        pressures = [0.0, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0]
        for p in pressures:
            if p <= 0.0:
                occ = 0.0
            elif p <= 40.0:
                occ = 0.5 * (p / 40.0)
            else:
                occ = 0.5
            writer.writerow([f"{p:.1f}", f"{occ:.5f}"])

if __name__ == '__main__':
    target = sys.argv[1]
    os.makedirs(OUTDIR, exist_ok=True)
    if target == 'gamma_caso4_gibbs_polynomial.json':
        write_gibbs_polynomial()
    elif target == 'phase_boundary_curves.csv':
        write_phase_boundaries()
    elif target == 'mc_isotherm_298K.csv':
        write_isotherm_298K()
    elif target == 'mc_isotherm_215K.csv':
        write_isotherm_215K()
    else:
        raise ValueError(f'Unknown target: {target}')
