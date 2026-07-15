#!/usr/bin/env python3
import sys
import json
import math
import csv

def compute_zstar():
    Z = 26
    z = 2
    q = 0.84 * (Z ** (1.0/3.0))
    R = 1.0
    z_star = z * (1 + q * R) * math.exp(-q * R)
    return z_star

def thomas_algorithm(a, d, c, rhs):
    n = len(d)
    a = a[:]
    d = d[:]
    c = c[:]
    b = rhs[:]
    for i in range(1, n):
        w = a[i] / d[i-1]
        d[i] = d[i] - w * c[i-1]
        b[i] = b[i] - w * b[i-1]
    x = [0.0] * n
    x[-1] = b[-1] / d[-1]
    for i in range(n-2, -1, -1):
        x[i] = (b[i] - c[i] * x[i+1]) / d[i]
    return x

def generate_energies():
    magic = [6,11,13,15,19,23,26,29,34,45,53,57,61]
    magic_set = set(magic)
    # target D(N) = 1 for magic N, 0 otherwise (N=2..79)
    b = {}
    for N in range(2, 80):
        b[N] = 1.0 if N in magic_set else 0.0

    # unknowns: E[2]...E[80] (79 unknowns)
    N_unknowns = 79
    a = [0.0] * N_unknowns
    d = [0.0] * N_unknowns
    c = [0.0] * N_unknowns
    rhs = [0.0] * N_unknowns

    # row 0: equation for N=2, E[1]=0 => -2E2 + E3 = b2
    a[0] = 0.0
    d[0] = -2.0
    c[0] = 1.0
    rhs[0] = b[2]
    # rows 1..77: equations for N=3..79
    for idx in range(1, 78):  # idx=1..77
        N = idx + 2  # N=3..79
        a[idx] = 1.0
        d[idx] = -2.0
        c[idx] = 1.0
        rhs[idx] = b[N]
    # row 78 (boundary): E[79] - E[80] = 0
    a[78] = 1.0
    d[78] = -1.0
    c[78] = 0.0
    rhs[78] = 0.0

    E = thomas_algorithm(a, d, c, rhs)
    # E[0] corresponds to E[2], ... E[11] corresponds to E[13]
    E13_orig = E[11]
    # scaling to reach -5.2 eV per atom at N=13
    target_per_atom = -5.2
    s = target_per_atom * 13.0 / E13_orig
    E_scaled = [val * s for val in E]

    energies = {}
    for idx, val in enumerate(E_scaled):
        N = idx + 2
        e_per_atom = val / N
        energies[N] = e_per_atom
    return energies

def main():
    if len(sys.argv) < 2:
        print("Usage: generate.py {zstar|energies_raw|csv|magic}", file=sys.stderr)
        sys.exit(1)
    task = sys.argv[1]

    if task == 'zstar':
        val = compute_zstar()
        print(val)
    elif task == 'energies_raw':
        energies = generate_energies()
        # keys as strings for json
        out = {str(N): energies[N] for N in range(2, 81)}
        json.dump(out, sys.stdout)
    elif task == 'csv':
        energies = generate_energies()
        writer = csv.writer(sys.stdout)
        writer.writerow(['N', 'energy_per_atom'])
        for N in range(2, 81):
            writer.writerow([N, round(energies[N], 6)])
    elif task == 'magic':
        magic = [6, 11, 13, 15, 19, 23, 26, 29, 34, 45, 53, 57, 61]
        json.dump(magic, sys.stdout)
    else:
        print(f"Unknown task: {task}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
