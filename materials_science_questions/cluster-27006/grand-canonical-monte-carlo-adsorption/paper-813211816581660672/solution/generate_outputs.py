#!/usr/bin/env python3
"""
Hidden oracle – writes approximate reference outputs for the GCMC task.
All numbers are synthesised from the paper's Table 2, reported saturation
loadings, and description of isosteric heats.
"""
import csv, sys, math

# -----------------------------------------------------------------
# Helper: log‑log linear interpolation from a few control points
# -----------------------------------------------------------------
def interp_loglog(x, x_points, y_points):
    """x_points and y_points are in log10 space."""
    if x <= x_points[0]:
        idx = 0
        t = 0.0
    elif x >= x_points[-1]:
        idx = len(x_points) - 2
        t = 1.0
    else:
        for i in range(len(x_points) - 1):
            if x_points[i] <= x <= x_points[i+1]:
                idx = i
                t = (x - x_points[i]) / (x_points[i+1] - x_points[i])
                break
    logy = y_points[idx] + t * (y_points[idx+1] - y_points[idx])
    return 10 ** logy

# -----------------------------------------------------------------
# Control points for CO2 and N2 isotherms at each Si/Al ratio.
# Points are given as (log10(Pressure/bar), log10(Loading/uc)).
# -----------------------------------------------------------------

isotherm_controls = {}

# CO2 -------------------------
co2_base = {'inf': [(-3.0, -2.0),  # P=1e-3 bar, N~0.01
                    (-1.0, 0.0),   # P=0.1 bar, N=1
                    (0.0, 0.9479), # P=1 bar, N~8.87 (log10=0.9479)
                    (1.0, 1.1461), # P=10 bar, N~14
                    (1.3, 1.1461)]}# 20 bar, same saturation

# Na‑ZSM‑5 95 (1 Na+) -> control points to give N≈1 at P=5e-4 bar (logP=-3.301)
co2_95 = [(-3.3010, 0.0),   # P=5e‑4 bar, N=1
          (-3.0, 0.0792),   # P=1e-3 bar, N~1.2
          (-1.0, 0.69897),  # P=0.1 bar, N~5
          (0.0, 1.105),     # P=1 bar, N~12.74
          (1.0, 1.1761),    # P=10 bar, N~15
          (1.3, 1.1761)]
co2_47 = [(-3.0, 0.0),      # P=1e-3 bar, N=1 (but P_1molec for 47 is 1e-4, so shift)
          (-3.3010, -0.0458), # 5e-4 bar, N~0.9
          (-1.0, 0.7782),    # P=0.1 bar, N~6
          (0.0, 1.0888),     # P=1 bar, 12.27
          (1.0, 1.1761),     # 15
          (1.3, 1.1761)]
co2_31 = [(-4.0, 0.0),      # P=1e-7 bar, N=1
          (-3.0, 0.3010),   # P=1e-3 bar, N~2
          (-1.0, 0.9031),   # P=0.1 bar, N~8
          (0.0, 1.1139),    # P=1 bar, N~13
          (1.0, 1.2041),    # 16
          (1.3, 1.2041)]
co2_23 = [(-4.5229, 0.0),   # P=3e-9 bar, N=1
          (-3.0, 0.3979),   # P=1e-3 bar, N~2.5
          (-1.0, 0.9542),   # P=0.1 bar, N~9
          (0.0, 1.1303),    # P=1 bar, N~13.5
          (1.0, 1.2041),    # 16
          (1.3, 1.2041)]
co2_13 = [(-3.69897, 0.0),  # P=2e-7 bar, N=1
          (-3.0, 0.4771),   # P=1e-3 bar, N~3
          (-1.0, 1.0792),   # P=0.1 bar, N~12
          (0.0, 1.1761),    # P=1 bar, N~15
          (1.0, 1.2553),    # P=10 bar, N~18
          (1.3, 1.2553)]

isotherm_controls['CO2'] = {'inf': co2_base['inf'], '95': co2_95, '47': co2_47,
                            '31': co2_31, '23': co2_23, '13': co2_13}

# N2 -------------------------
# Silicalite-1: P_1mol=1.75 bar (logP≈0.243), so at P=1 bar N<1.
n2_inf = [(-3.0, -2.0),      # P=1e-3 bar, ~0
          (-1.0, -1.0),      # P=0.1 bar, ~0.1
          (-0.243, 0.0),     # P≈0.57 bar? Actually 1.75 bar is log10(1.75)=0.243, so (0.243,0)
          (0.0, -0.0969),    # P=1 bar, N~0.8 (log10= -0.0969)
          (1.0, 0.9031),     # P=10 bar, N~8
          (2.4771, 1.1461)]  # P=300 bar, N~14

n2_95 = [(-3.0, -1.0),       # P=1e-3 bar, N~0.1
         (-0.8239, 0.0),     # P=0.15 bar, N=1
         (-1.0, 0.3010),     # P=0.1 bar, N~2
         (0.0, 0.69897),     # P=1 bar, N~5
         (1.0, 0.9542),      # P=10 bar, N~9
         (2.4771, 1.1761)]   # 300 bar, N≈15
n2_47 = [(-3.0, -0.5229),    # P=1e-3 bar, N~0.3
         (-1.8239, 0.0),     # P=0.015 bar, N=1
         (-1.0, 0.4771),     # P=0.1 bar, N~3
         (0.0, 0.7782),      # P=1 bar, N~6
         (1.0, 1.0),         # P=10 bar, N~10
         (2.4771, 1.2041)]
n2_31 = [(-3.0, 0.0),        # P=1e-3 bar, N=1 (P_1mol 2.5e-5 so earlier)
         (-1.0, 0.4771),     # P=0.1 bar, N~3
         (0.0, 0.8129),      # P=1 bar, N~6.5
         (1.0, 1.0414),      # P=10 bar, N~11
         (2.4771, 1.2304)]
n2_23 = [(-3.0, 0.1761),     # P=1e-3 bar, N~1.5
         (-1.0, 0.5441),     # P=0.1 bar, N~3.5
         (0.0, 0.8451),      # P=1 bar, N~7
         (1.0, 1.0792),      # P=10 bar, N~12
         (2.4771, 1.2304)]
n2_13 = [(-3.0, 0.3979),     # P=1e-3 bar, N~2.5
         (-1.0, 0.69897),    # P=0.1 bar, N~5
         (0.0, 0.9243),      # P=1 bar, N~8.4
         (1.0, 1.1139),      # P=10 bar, N~13
         (2.4771, 1.2553)]

isotherm_controls['N2'] = {'inf': n2_inf, '95': n2_95, '47': n2_47,
                           '31': n2_31, '23': n2_23, '13': n2_13}

# -----------------------------------------------------------------
# Isosteric heat parameters: Qst(loading) = Q_base + (Q0 - Q_base)*exp(-k*L)
# -----------------------------------------------------------------
heat_params = {
    'CO2': {'Q_base': 22.0, 'k': 0.3,
            'inf': 22.0,
            '95': 50.0, '47': 55.0, '31': 60.0, '23': 65.0, '13': 80.0},
    'N2':  {'Q_base': 14.0, 'k': 0.35,
            'inf': 14.0,
            '95': 30.0, '47': 35.0, '31': 40.0, '23': 45.0, '13': 65.0}
}

# -----------------------------------------------------------------
# Generation functions
# -----------------------------------------------------------------

def gen_isotherms():
    rows = []
    for gas in ['CO2', 'N2']:
        ctrl_dict = isotherm_controls[gas]
        # pressure range
        if gas == 'CO2':
            pressures = [10**p for p in [-9, -8.5, -8, -7.5, -7, -6.5, -6, -5.5, -5, -4.5, -4, -3.5,
                                         -3, -2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.3]]
            # ensure a good spread
            npoints = 50
            logp_list = [math.log10(1e-9) + i*(math.log10(20)-math.log10(1e-9))/49 for i in range(50)]
        else:  # N2 up to 300 bar
            logp_list = [math.log10(1e-6) + i*(math.log10(300)-math.log10(1e-6))/49 for i in range(50)]
        for sia in ['inf', '95', '47', '31', '23', '13']:
            pts_x = [p[0] for p in ctrl_dict[sia]]
            pts_y = [p[1] for p in ctrl_dict[sia]]
            for logP in logp_list:
                P = 10**logP
                loading = interp_loglog(logP, pts_x, pts_y)
                rows.append({'gas': gas, 'SiAl': sia, 'pressure_bar': f'{P:.6g}',
                             'loading_molecules_per_uc': f'{loading:.4f}'})
    # write CSV
    with open('/app/outputs/step_04_isotherms.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['gas','SiAl','pressure_bar','loading_molecules_per_uc'])
        writer.writeheader()
        writer.writerows(rows)

def gen_heats():
    rows = []
    for gas in ['CO2', 'N2']:
        params = heat_params[gas]
        Q_base = params['Q_base']
        k = params['k']
        for sia in ['inf', '95', '47', '31', '23', '13']:
            Q0 = params[sia]
            # loading from 0.1 to 20 step 0.2
            L = 0.1
            while L <= 20.0:
                Qst = Q_base + (Q0 - Q_base) * math.exp(-k * L)
                rows.append({'gas': gas, 'SiAl': sia,
                             'loading_molecules_per_uc': f'{L:.2f}',
                             'Qst_kJ_per_mol': f'{Qst:.2f}'})
                L += 0.2
    with open('/app/outputs/step_05_isosteric_heats.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['gas','SiAl','loading_molecules_per_uc','Qst_kJ_per_mol'])
        writer.writeheader()
        writer.writerows(rows)

def gen_charge():
    rows = []
    # For Si/Al=13 only, three charges
    # We'll generate isotherm points and heat points for each charge.
    # Use the same log-log framework but with modified control points to reflect reduced cation effect.
    # Control points for each charge (CO2 and N2)
    charge_controls = {}
    # CO2
    # 1.0e is the same as co2_13 above.
    co2_13_pts = isotherm_controls['CO2']['13']   # list of (logP, logN)
    # 0.7e: shift low-pressure up (weaker binding) -> loading lower at same P.
    # We'll create new pts by adding 0.5 to logP for the cation contributed region? Simpler: define manually.
    co2_07 = [(-3.0, 0.1461),   # P=1e-3, N~1.4
              (-1.0, 0.8451),   # P=0.1, N~7
              (0.0, 1.0792),    # P=1, N~12
              (1.0, 1.2041),    # P=10, N~16
              (1.3, 1.2041)]
    co2_04 = [(-3.0, 0.0),      # P=1e-3, N~1
              (-1.0, 0.6021),   # P=0.1, N~4
              (0.0, 0.9294),    # P=1, N~8.5
              (1.0, 1.1461),    # P=10, N~14
              (1.3, 1.1461)]
    charge_controls['CO2'] = {1.0: co2_13_pts, 0.7: co2_07, 0.4: co2_04}

    # N2
    n2_13_pts = isotherm_controls['N2']['13']
    n2_07 = [(-3.0, 0.0),       # P=1e-3, N~1
             (-1.0, 0.4771),    # P=0.1, N~3
             (0.0, 0.6532),     # P=1, N~4.5
             (1.0, 0.9243),     # P=10, N~8.4
             (2.4771, 1.0792)]  
    n2_04 = [(-3.0, -0.3010),   # P=1e-3, N~0.5
             (-1.0, 0.3010),    # P=0.1, N~2
             (0.0, 0.4771),     # P=1, N~3
             (1.0, 0.8451),     # P=10, N~7
             (2.4771, 1.0)]
    charge_controls['N2'] = {1.0: n2_13_pts, 0.7: n2_07, 0.4: n2_04}

    # Heat parameters for charges: Q0 values assigned
    heat_charge = {
        'CO2': {1.0: 80.0, 0.7: 52.0, 0.4: 42.0},
        'N2':  {1.0: 65.0, 0.7: 30.0, 0.4: 22.0}
    }

    for gas in ['CO2', 'N2']:
        for charge in [1.0, 0.7, 0.4]:
            # isotherm
            ctrl_pts = charge_controls[gas][charge]
            pts_x = [p[0] for p in ctrl_pts]
            pts_y = [p[1] for p in ctrl_pts]
            if gas == 'CO2':
                logp_list = [math.log10(1e-9) + i*(math.log10(20)-math.log10(1e-9))/49 for i in range(50)]
            else:
                logp_list = [math.log10(1e-6) + i*(math.log10(300)-math.log10(1e-6))/49 for i in range(50)]
            for logP in logp_list:
                P = 10**logP
                loading = interp_loglog(logP, pts_x, pts_y)
                # Qst at this loading
                Q0 = heat_charge[gas][charge]
                Q_base = heat_params[gas]['Q_base']
                k = heat_params[gas]['k']
                Qst = Q_base + (Q0 - Q_base) * math.exp(-k * loading)
                rows.append({'gas': gas, 'Na_charge_e': f'{charge}',
                             'pressure_bar': f'{P:.6g}',
                             'loading_molecules_per_uc': f'{loading:.4f}',
                             'Qst_kJ_per_mol': f'{Qst:.2f}'})

    with open('/app/outputs/step_07_charge_comparison.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['gas','Na_charge_e','pressure_bar',
                                               'loading_molecules_per_uc','Qst_kJ_per_mol'])
        writer.writeheader()
        writer.writerows(rows)

# -----------------------------------------------------------------
# Main dispatcher
# -----------------------------------------------------------------
if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if mode == 'isotherms':
        gen_isotherms()
    elif mode == 'heats':
        gen_heats()
    elif mode == 'charge':
        gen_charge()
    else:
        gen_isotherms()
        gen_heats()
        gen_charge()
