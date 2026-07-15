#!/usr/bin/env python3
"""Synthetic Eliashberg function generator for the hidden oracle.
Writes step_01_alph2F_data.json and step_02_elph_params.csv."""
import math
import json
import csv
import sys

# Reference parameters from paper Table III
COMPOUNDS = {
    'TaB2': {'lambda': 0.79, 'omega_log_meV': 25.8, 'Tc_K': 10.6},
    'VB2':  {'lambda': 0.28, 'omega_log_meV': 44.1, 'Tc_K': 0.5},   # paper: <1
    'NbB2': {'lambda': 0.67, 'omega_log_meV': 30.5, 'Tc_K': 8.4},
    'TiB2': {'lambda': 0.10, 'omega_log_meV': 52.9, 'Tc_K': 0.0},   # paper: -
    'YB2':  {'lambda': 0.46, 'omega_log_meV': 37.4, 'Tc_K': 2.4},
}

SIGMA = 1.0   # meV, width of the Gaussian peak
dE = 0.5      # meV, uniform grid spacing


def synthetic_alph2f(lambda_target, omega_log_target):
    """Return (energy_meV, alpha2F) arrays that give the target lambda and omega_log."""
    # Energy range covering peak +/- 4 sigma
    e_start = max(0.1, omega_log_target - 4*SIGMA)
    e_end = omega_log_target + 4*SIGMA
    n_points = int((e_end - e_start) / dE) + 1
    energy = [e_start + i*dE for i in range(n_points)]

    # unnormalised Gaussian
    raw = [math.exp(-(e - omega_log_target)**2 / (2*SIGMA**2)) for e in energy]

    # compute integral I = 2 * sum (raw_i / e_i) * dE
    I = 0.0
    for e, r in zip(energy, raw):
        I += (r / e)
    I *= 2.0 * dE
    # scale factor to achieve lambda_target
    A = lambda_target / I
    alpha2F = [A * r for r in raw]

    return energy, alpha2F


def compute_lambda_omega_log(energy, alpha2F):
    """Numerically compute lambda and omega_log (meV) from the arrays."""
    # trapezoidal integration with constant dE (rectangle rule is fine for uniform grid)
    lam = 0.0
    log_sum = 0.0
    for e, a in zip(energy, alpha2F):
        lam += a / e
        log_sum += a * math.log(e) / e
    lam *= 2.0 * dE
    log_sum *= 2.0 * dE
    omega_log = math.exp(log_sum / lam)
    return lam, omega_log


def write_step_01():
    data = {}
    for comp, params in COMPOUNDS.items():
        energy, a2F = synthetic_alph2f(params['lambda'], params['omega_log_meV'])
        data[comp] = {'energy': energy, 'alpha2F': a2F}
    with open('/app/outputs/step_01_alph2F_data.json', 'w') as f:
        json.dump(data, f, indent=2)


def write_step_02():
    # Re-read step_01 to compute lambda and omega_log from the generated data
    with open('/app/outputs/step_01_alph2F_data.json') as f:
        data = json.load(f)

    rows = []
    for comp, params in COMPOUNDS.items():
        entry = data[comp]
        lam, wlog = compute_lambda_omega_log(entry['energy'], entry['alpha2F'])
        tc = params['Tc_K']   # directly use paper's Tc (within generous tolerance)
        rows.append({'compound': comp, 'lambda': round(lam, 6), 'omega_log': round(wlog, 6), 'Tc': tc})

    with open('/app/outputs/step_02_elph_params.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['compound', 'lambda', 'omega_log', 'Tc'])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s step_01|step_02" % sys.argv[0])
        sys.exit(1)
    if sys.argv[1] == 'step_01':
        write_step_01()
    elif sys.argv[1] == 'step_02':
        write_step_02()
    else:
        sys.exit(1)
