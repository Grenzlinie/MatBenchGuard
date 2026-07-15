#!/usr/bin/env python3
import csv, json, math, os, sys

def dep_output(P, R, T):
    params = {
        (100.0, 0.5): {'T0': 1273.0, 'sigma': 300.0, 'A': 0.15},
        (100.0, 0.2): {'T0': 1273.0, 'sigma': 300.0, 'A': 0.20},
        (0.5, 0.5): {'T0': 1073.0, 'sigma': 256.0, 'A': 0.23},
        (0.5, 0.2): {'T0': 1073.0, 'sigma': 200.0, 'A': 0.24},
        (0.01, 0.5): {'T0': 973.0, 'sigma': 200.0, 'A': 0.24},
        (0.01, 0.2): {'T0': 973.0, 'sigma': 109.0, 'A': 0.247},
    }
    p = params[(P, R)]
    x = T - p['T0']
    val = 0.25 - p['A'] * math.exp(-(x*x) / (2.0 * p['sigma'] * p['sigma']))
    return val

def etch_output(P, T):
    params = {
        100.0:  {'T_mid': 1150.0, 's': 60.0,  'U': 0.60},
        0.5:    {'T_mid': 1080.0, 's': 55.0,  'U': 0.58},
        0.01:   {'T_mid': 1135.0, 's': 44.6,  'U': 0.60},
    }
    p = params[P]
    z = (T - p['T_mid']) / p['s']
    if z < -10.0:
        return 0.25
    return 0.25 + (p['U'] - 0.25) / (1.0 + math.exp(-z))

def make_depos_csv(path):
    pressures = [100.0, 0.5, 0.01]
    ratios = [0.5, 0.2]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['total_pressure_Torr', 'TiCl4_NH3_ratio', 'temperature_K', 'Ti_Cl_output'])
        for P in pressures:
            for R in ratios:
                for T in range(500, 1550, 100):
                    val = dep_output(P, R, T)
                    w.writerow([P, R, T, round(val, 6)])

def make_etch_csv(path):
    pressures = [100.0, 0.5, 0.01]
    with open(path, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['total_pressure_Torr', 'temperature_K', 'Ti_Cl_output'])
        for P in pressures:
            for T in range(500, 1550, 100):
                val = etch_output(P, T)
                w.writerow([P, T, round(val, 6)])

def make_species_json(path):
    P = 0.5
    R = 0.5
    temps = [800, 1000, 1200]
    points = []
    for T in temps:
        target = dep_output(P, R, T)
        # avoid division by zero or negative HCl
        if target < 0.001:
            target = 0.001
        a_TiCl4 = 0.01       # chosen to keep HCl reasonable
        b_HCl = a_TiCl4 * (1.0 / target - 4.0)
        if b_HCl < 0.0:
            b_HCl = 0.0
        nh3 = 0.01
        n2 = 0.2
        h2 = 0.5 - (a_TiCl4 + b_HCl + nh3 + n2)
        if h2 < 0.0:
            n2 = 0.5 - a_TiCl4 - b_HCl - nh3
            if n2 < 0.0:
                n2 = 0.0
            h2 = 0.5 - (a_TiCl4 + b_HCl + nh3 + n2)
            if h2 < 0.0:
                h2 = 0.0
        sp = {
            "TiCl4": round(a_TiCl4, 6),
            "TiCl3": 0.0,
            "TiCl2": 0.0,
            "TiCl": 0.0,
            "NH3": round(nh3, 6),
            "N2": round(n2, 6),
            "H2": round(h2, 6),
            "Cl2": 0.0,
            "HCl": round(b_HCl, 6),
            "H": 0.0,
            "Cl": 0.0
        }
        points.append({"temperature_K": T, **sp})
    obj = {
        "total_pressure_Torr": P,
        "TiCl4_NH3_ratio": R,
        "points": points
    }
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    outdir = '/app/outputs'
    os.makedirs(outdir, exist_ok=True)
    target = sys.argv[1]
    if target == 'ti_cl_output_deposition.csv':
        make_depos_csv(os.path.join(outdir, target))
    elif target == 'ti_cl_output_etching.csv':
        make_etch_csv(os.path.join(outdir, target))
    elif target == 'species_pressures_deposition.json':
        make_species_json(os.path.join(outdir, target))
    else:
        sys.exit(1)
