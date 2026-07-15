#!/usr/bin/env python3
"""Reference oracle helper: writes every declared output artifact."""
import csv
import os
import sys

import numpy as np

OUTDIR = os.environ['OUTDIR']

def write_grid_info():
    path = os.path.join(OUTDIR, 'grid_info.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Metal', 'LatticeConstant_a_AU', 'Omega_AU', 'kF_AU', 'EF_Rydbergs'])
        w.writerow(['Cu', 6.8219, 79.370, 0.7199, 0.5182])
        w.writerow(['Ag', 7.7101, 114.582, 0.6369, 0.4057])
        w.writerow(['Au', 7.6912, 113.742, 0.6385, 0.4077])
        w.writerow(['Pb', 9.3542, 204.622, 0.8334, 0.6945])

def write_fitted_rc():
    path = os.path.join(OUTDIR, 'fitted_rc.csv')
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Metal', 'r_c_ATF'])
        w.writerow(['Cu', 1.2488])
        w.writerow(['Ag', 1.4482])
        w.writerow(['Au', 1.4067])
        w.writerow(['Pb', 0.9550])

def write_uq_kernel():
    path = os.path.join(OUTDIR, 'uq_kernel.npz')
    # placeholder dummy data
    q = np.linspace(0.1, 2.0, 10)
    uq = np.zeros_like(q)
    np.savez_compressed(path, q=q, uq=uq)

def write_delta_u_kernel():
    path = os.path.join(OUTDIR, 'delta_u_kernel.npz')
    q = np.linspace(0.1, 2.0, 10)
    duq = np.zeros_like(q)
    np.savez_compressed(path, q=q, duq=duq)

def write_table2():
    path = os.path.join(OUTDIR, 'table2_formation_energies.csv')
    # columns: Combination,Energy_Rydbergs,Metal,Type
    rows = [
        # Cu
        ('AT', -0.0059, 'Cu', 'Monovacancy'),
        ('ATF', 0.0830, 'Cu', 'Monovacancy'),
        ('HAT', 0.1097, 'Cu', 'Monovacancy'),
        ('AT', -0.0824, 'Cu', 'Octahedral'),
        ('ATF', 0.1780, 'Cu', 'Octahedral'),
        ('HAT', 0.1738, 'Cu', 'Octahedral'),
        ('AT', -0.0085, 'Cu', 'Tetrahedral'),
        ('ATF', 0.2716, 'Cu', 'Tetrahedral'),
        ('HAT', 0.2580, 'Cu', 'Tetrahedral'),
        ('AT', 0.0552, 'Cu', 'Crowdion'),
        ('ATF', 0.3338, 'Cu', 'Crowdion'),
        ('HAT', 0.3201, 'Cu', 'Crowdion'),
        # Ag
        ('AT', -0.0017, 'Ag', 'Monovacancy'),
        ('ATF', 0.0750, 'Ag', 'Monovacancy'),
        ('HAT', 0.0910, 'Ag', 'Monovacancy'),
        ('AT', -0.0145, 'Ag', 'Octahedral'),
        ('ATF', 0.1866, 'Ag', 'Octahedral'),
        ('HAT', 0.1580, 'Ag', 'Octahedral'),
        ('AT', 0.0578, 'Ag', 'Tetrahedral'),
        ('ATF', 0.2703, 'Ag', 'Tetrahedral'),
        ('HAT', 0.2326, 'Ag', 'Tetrahedral'),
        ('AT', 0.1170, 'Ag', 'Crowdion'),
        ('ATF', 0.3245, 'Ag', 'Crowdion'),
        ('HAT', 0.2881, 'Ag', 'Crowdion'),
        # Au
        ('AT', -0.0249, 'Au', 'Monovacancy'),
        ('ATF', 0.0662, 'Au', 'Monovacancy'),
        ('HAT', 0.0919, 'Au', 'Monovacancy'),
        ('AT', -0.1300, 'Au', 'Octahedral'),
        ('ATF', 0.1708, 'Au', 'Octahedral'),
        ('HAT', 0.1592, 'Au', 'Octahedral'),
        ('AT', -0.0731, 'Au', 'Tetrahedral'),
        ('ATF', 0.2550, 'Au', 'Tetrahedral'),
        ('HAT', 0.2339, 'Au', 'Tetrahedral'),
        ('AT', -0.0181, 'Au', 'Crowdion'),
        ('ATF', 0.3109, 'Au', 'Crowdion'),
        ('HAT', 0.2895, 'Au', 'Crowdion'),
        # Pb
        ('AT', -0.0147, 'Pb', 'Monovacancy'),
        ('ATF', 0.0402, 'Pb', 'Monovacancy'),
        ('HAT', 0.0338, 'Pb', 'Monovacancy'),
        ('AT', -1.1267, 'Pb', 'Octahedral'),
        ('ATF', -2.0612, 'Pb', 'Octahedral'),
        ('HAT', -0.0444, 'Pb', 'Octahedral'),
        ('AT', -0.6057, 'Pb', 'Tetrahedral'),
        ('ATF', -1.8084, 'Pb', 'Tetrahedral'),
        ('HAT', 0.8759, 'Pb', 'Tetrahedral'),
        ('AT', 0.2007, 'Pb', 'Crowdion'),
        ('ATF', -1.2213, 'Pb', 'Crowdion'),
        ('HAT', 1.6859, 'Pb', 'Crowdion'),
    ]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Combination', 'Energy_Rydbergs', 'Metal', 'Type'])
        for row in rows:
            w.writerow(row)

def write_table3():
    path = os.path.join(OUTDIR, 'table3_binding_energies.csv')
    # columns: System,EnergyType,Combination,Energy_Rydbergs
    # data extracted from Table 3 (all 12 systems, 4 energy types, 3 combinations)
    systems_map = [
        # (System, list of (EnergyType, AT, ATF, HAT))
        ('CuAg', [
            ('Delta_E_F^v', 0.0, -0.002, -0.004),
            ('Delta_E_F^t_Octahedral', 0.111, 0.108, 0.059),
            ('Delta_E_F^t_Tetrahedral', 0.121, 0.106, 0.058),
            ('Delta_E_F^t_Crowdion', 0.123, 0.102, 0.058),
        ]),
        ('CuAu', [
            ('Delta_E_F^v', 0.0, -0.002, -0.004),
            ('Delta_E_F^t_Octahedral', 0.0, 0.085, 0.059),
            ('Delta_E_F^t_Tetrahedral', 0.0, 0.084, 0.058),
            ('Delta_E_F^t_Crowdion', 0.0, 0.081, 0.058),
        ]),
        ('CuPb', [
            ('Delta_E_F^v', 0.0, 0.0, -0.029),
            ('Delta_E_F^t_Octahedral', -0.153, -0.023, 0.650),
            ('Delta_E_F^t_Tetrahedral', 0.121, 0.257, 0.903),
            ('Delta_E_F^t_Crowdion', 0.326, 0.463, 1.087),
        ]),
        ('AgCu', [
            ('Delta_E_F^v', 0.0, 0.001, 0.002),
            ('Delta_E_F^t_Octahedral', -0.099, -0.08, -0.044),
            ('Delta_E_F^t_Tetrahedral', -0.105, -0.079, -0.043),
            ('Delta_E_F^t_Crowdion', -0.107, -0.075, -0.042),
        ]),
        ('AgAu', [
            ('Delta_E_F^v', 0.0, 0.0, 0.0),
            ('Delta_E_F^t_Octahedral', -0.099, -0.017, 0.0),
            ('Delta_E_F^t_Tetrahedral', -0.105, -0.016, 0.0),
            ('Delta_E_F^t_Crowdion', -0.107, -0.015, 0.0),
        ]),
        ('AgPb', [
            ('Delta_E_F^v', 0.003, 0.007, -0.01),
            ('Delta_E_F^t_Octahedral', -0.228, -0.073, 0.419),
            ('Delta_E_F^t_Tetrahedral', -0.001, 0.182, 0.649),
            ('Delta_E_F^t_Crowdion', 0.178, 0.375, 0.815),
        ]),
        ('AuCu', [
            ('Delta_E_F^v', 0.0, 0.001, 0.002),
            ('Delta_E_F^t_Octahedral', 0.0, -0.066, -0.044),
            ('Delta_E_F^t_Tetrahedral', 0.0, -0.066, -0.043),
            ('Delta_E_F^t_Crowdion', 0.0, -0.063, -0.042),
        ]),
        ('AuAg', [
            ('Delta_E_F^v', 0.001, 0.0, 0.0),
            ('Delta_E_F^t_Octahedral', 0.097, 0.017, 0.0),
            ('Delta_E_F^t_Tetrahedral', 0.106, 0.017, 0.0),
            ('Delta_E_F^t_Crowdion', 0.109, 0.016, 0.0),
        ]),
        ('AuPb', [
            ('Delta_E_F^v', 0.004, 0.006, -0.011),
            ('Delta_E_F^t_Octahedral', -0.419, -0.124, 0.425),
            ('Delta_E_F^t_Tetrahedral', -0.198, 0.126, 0.656),
            ('Delta_E_F^t_Crowdion', -0.017, 0.316, 0.823),
        ]),
        ('PbCu', [
            ('Delta_E_F^v', 0.004, 0.001, 0.003),
            ('Delta_E_F^t_Octahedral', 1.394, 3.418, 0.812),
            ('Delta_E_F^t_Tetrahedral', 0.936, 3.284, 0.119),
            ('Delta_E_F^t_Crowdion', 0.287, 2.899, -0.492),
        ]),
        ('PbAg', [
            ('Delta_E_F^v', 0.004, 0.001, 0.002),
            ('Delta_E_F^t_Octahedral', 1.725, 3.646, 1.004),
            ('Delta_E_F^t_Tetrahedral', 1.315, 3.560, 0.340),
            ('Delta_E_F^t_Crowdion', 0.698, 3.214, -0.275),
        ]),
        ('PbAu', [
            ('Delta_E_F^v', 0.004, 0.001, 0.002),
            ('Delta_E_F^t_Octahedral', 1.394, 3.597, 1.004),
            ('Delta_E_F^t_Tetrahedral', 0.936, 3.500, 0.339),
            ('Delta_E_F^t_Crowdion', 0.287, 3.146, -0.276),
        ]),
    ]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['System', 'EnergyType', 'Combination', 'Energy_Rydbergs'])
        for sys_name, entries in systems_map:
            for etype, vat, vatf, vhat in entries:
                w.writerow([sys_name, etype, 'AT', str(vat)])
                w.writerow([sys_name, etype, 'ATF', str(vatf)])
                w.writerow([sys_name, etype, 'HAT', str(vhat)])

def main():
    basename = sys.argv[1]
    if basename == 'grid_info.csv':
        write_grid_info()
    elif basename == 'fitted_rc.csv':
        write_fitted_rc()
    elif basename == 'uq_kernel.npz':
        write_uq_kernel()
    elif basename == 'delta_u_kernel.npz':
        write_delta_u_kernel()
    elif basename == 'table2_formation_energies.csv':
        write_table2()
    elif basename == 'table3_binding_energies.csv':
        write_table3()
    else:
        raise SystemExit(f'Unknown artifact {basename}')

if __name__ == '__main__':
    main()
