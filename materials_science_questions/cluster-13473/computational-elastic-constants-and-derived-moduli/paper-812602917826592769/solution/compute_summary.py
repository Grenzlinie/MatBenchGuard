#!/usr/bin/env python3
import csv, json, math

def linear_slope(x, y):
    n = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumxy = sum(xi*yi for xi, yi in zip(x, y))
    sumx2 = sum(xi*xi for xi in x)
    denom = n*sumx2 - sumx*sumx
    if denom == 0:
        return 0.0
    return (n*sumxy - sumx*sumy) / denom

def process_csv(filename, mode):
    strains = []
    stresses = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            strains.append(float(row['strain']))
            stresses.append(float(row['stress']))
    # elastic modulus from strain <= 0.005
    idx = [i for i, s in enumerate(strains) if s <= 0.005]
    x = [strains[i] for i in idx]
    y = [stresses[i] for i in idx]
    E = linear_slope(x, y)
    if mode == 'tension':
        peak_idx = max(range(len(stresses)), key=lambda i: stresses[i])
        peak_stress = stresses[peak_idx]
        fail_idx = None
        for i in range(peak_idx+1, len(strains)):
            if stresses[i] <= 0.8 * peak_stress:
                fail_idx = i
                break
        fail_strain = strains[fail_idx] if fail_idx is not None else strains[peak_idx]
        return E, fail_strain
    else:  # compression
        peak_idx = max(range(len(stresses)), key=lambda i: stresses[i])
        fail_strain = strains[peak_idx]
        return E, fail_strain

modes = ['tension','tension','tension','compression','compression','compression']
dirs = ['X','Y','Z']
files = {
    ('tension','X'): '/app/outputs/stress_strain_curve_tension_X.csv',
    ('tension','Y'): '/app/outputs/stress_strain_curve_tension_Y.csv',
    ('tension','Z'): '/app/outputs/stress_strain_curve_tension_Z.csv',
    ('compression','X'): '/app/outputs/stress_strain_curve_compression_X.csv',
    ('compression','Y'): '/app/outputs/stress_strain_curve_compression_Y.csv',
    ('compression','Z'): '/app/outputs/stress_strain_curve_compression_Z.csv',
}

res = {'tension': {}, 'compression': {}}
for md in set(modes):
    for d in dirs:
        E, fail = process_csv(files[(md, d)], md)
        if md == 'tension':
            res['tension'][d] = {'E_modulus_GPa': round(E, 6), 'failure_strain': round(fail, 6)}
        else:
            res['compression'][d] = {'E_modulus_GPa': round(E, 6), 'failure_strain_abs': round(fail, 6)}

print(json.dumps(res, indent=2))
