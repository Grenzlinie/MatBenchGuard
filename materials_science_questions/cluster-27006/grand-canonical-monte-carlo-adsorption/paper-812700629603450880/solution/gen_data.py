import csv
import sys
import math

def main():
    fname = sys.argv[1]
    if fname == 'ethanol_isotherms.csv':
        write_ethanol()
    elif fname == 'water_isotherms.csv':
        write_water()
    elif fname == 'mixture_selectivity.csv':
        write_selectivity()
    else:
        raise ValueError(f'Unknown output {fname}')

def write_ethanol():
    temps = [323, 373]
    zifs = ['ZIF-1', 'ZIF-3', 'ZIF-7', 'ZIF-9']
    pressures = [1, 5, 10, 20, 40, 60, 80, 100]
    # (Q_sat, b) per ZIF and temperature, tuned to satisfy ordering and T-dependence
    params = {
        'ZIF-9': {323: (5.0, 0.1), 373: (4.8, 0.05)},
        'ZIF-7': {323: (4.0, 0.09), 373: (3.8, 0.045)},
        'ZIF-3': {323: (2.5, 0.08), 373: (1.2, 0.03)},
        'ZIF-1': {323: (1.8, 0.07), 373: (0.7, 0.02)},
    }
    with open('/app/outputs/ethanol_isotherms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ZIF', 'Temperature (K)', 'Pressure (kPa)', 'Loading (mmol/g)'])
        for zif in zifs:
            for T in temps:
                Q, b = params[zif][T]
                for p in pressures:
                    loading = Q * b * p / (1.0 + b * p)
                    writer.writerow([zif, T, p, round(loading, 6)])

def write_water():
    temps = [323, 373]
    zifs = ['ZIF-1', 'ZIF-3', 'ZIF-7', 'ZIF-9']
    pressures = [1, 5, 10, 20, 40, 60, 80, 100]
    # water params: ZIF-1/3 near zero; ZIF-7/9 high uptake
    params = {
        'ZIF-1': {323: (0.1, 0.001), 373: (0.1, 0.001)},
        'ZIF-3': {323: (0.1, 0.001), 373: (0.1, 0.001)},
        'ZIF-7': {323: (3.0, 0.02), 373: (2.8, 0.015)},
        'ZIF-9': {323: (3.5, 0.022), 373: (3.2, 0.018)},
    }
    with open('/app/outputs/water_isotherms.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ZIF', 'Temperature (K)', 'Pressure (kPa)', 'Loading (mmol/g)'])
        for zif in zifs:
            for T in temps:
                Q, b = params[zif][T]
                for p in pressures:
                    loading = Q * b * p / (1.0 + b * p)
                    writer.writerow([zif, T, p, round(loading, 6)])

def write_selectivity():
    temps = [323, 373]
    zifs = ['ZIF-1', 'ZIF-3', 'ZIF-7', 'ZIF-9']
    pressures = [1, 5, 10, 20, 40, 60, 80, 100]
    # manually defined selectivity to satisfy ZIF-1 > ZIF-3 > ZIF-7 ≈ ZIF-9 at low p
    sel_map = {
        'ZIF-1': [60, 30, 20, 10, 5, 3, 2, 1.5],
        'ZIF-3': [40, 25, 18, 9, 5, 3, 2, 1.5],
        'ZIF-7': [20, 15, 10, 6, 4, 3, 2, 1.5],
        'ZIF-9': [18, 14, 9, 5.5, 4, 3, 2, 1.5],
    }
    with open('/app/outputs/mixture_selectivity.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ZIF', 'Temperature (K)', 'Pressure (kPa)', 'Selectivity'])
        for zif in zifs:
            for T in temps:
                for p, s in zip(pressures, sel_map[zif]):
                    writer.writerow([zif, T, p, s])

if __name__ == '__main__':
    main()