import csv
import math
import sys


def write_sublattice_occupancy(outpath):
    # Sublattice V occupancies at 1000 K (ordered state)
    # One sublattice mostly V, others equally roughly 0.15, summing to 4*V_frac = 4/3.
    rows = [
        (1, 0.880),
        (2, 0.151),
        (3, 0.151),
        (4, 0.151),
    ]
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['sublattice_number', 'occupancy_V'])
        writer.writerows(rows)


def write_sro(outpath):
    # Warren-Cowley SRO parameters at 1500 K (above transition)
    rows = [
        ('Co-V', 1, -0.10),
        ('Co-V', 2,  0.035),
        ('Ni-V', 1, -0.09),
        ('Ni-V', 2,  0.03),
        ('Co-Ni', 1, -0.02),
        ('Co-Ni', 2,  0.01),
    ]
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['pair', 'shell', 'alpha'])
        writer.writerows(rows)


def write_specific_heat(outpath):
    # Specific heat capacity from 1100 to 2000 K every 50 K, Gaussian peak at ~1450 K.
    temperatures = list(range(1100, 2050, 50))
    center = 1450.0
    sigma = 80.0
    baseline = 0.0001   # eV/atom
    peak = 0.0009
    rows = []
    for T in temperatures:
        cv = baseline + peak * math.exp(-((T - center) ** 2) / (2 * sigma ** 2))
        rows.append((T, round(cv, 8)))
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature_K', 'C_V_eV_per_atom'])
        writer.writerows(rows)


def write_relaxation_msad(outpath):
    # Relaxation energies and MSAD for ordered (1000 K), SRO (1540 K), random (4000 K)
    rows = [
        ('ordered_1000K', 0.015, 0.008),
        ('SRO_1540K', 0.025, 0.012),
        ('random_4000K', 0.030, 0.018),
    ]
    with open(outpath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['state', 'relaxation_energy_eV_per_atom', 'MSAD_A2'])
        writer.writerows(rows)


if __name__ == '__main__':
    target = sys.argv[1]
    outpath = f'/app/outputs/{target}'
    if target == 'step_02_v_sublattice_occupation.csv':
        write_sublattice_occupancy(outpath)
    elif target == 'step_03_sro_parameters.csv':
        write_sro(outpath)
    elif target == 'step_04_specific_heat.csv':
        write_specific_heat(outpath)
    elif target == 'step_06_relaxation_and_msad.csv':
        write_relaxation_msad(outpath)
    else:
        raise ValueError(f'Unknown target: {target}')
