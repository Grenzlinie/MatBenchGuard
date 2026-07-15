#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: results.json ===
python3 -c '
import json, math

rates_data = {
    0: {"13_to_2": 2.582e-1, "2_to_13": 8.053e-4, "1_to_3": 6.805e2, "3_to_1": 6.805e2, "1_to_d": 1.094e-2, "2_to_d": 3.067e-5, "3_to_d": 1.096e-2},
    -2: {"13_to_2": 2.881e-1, "2_to_13": 2.274e-3, "1_to_3": 4.967e3, "3_to_1": 4.967e3, "1_to_d": 3.270e-3, "2_to_d": 2.581e-5, "3_to_d": 3.261e-3},
    -4: {"13_to_2": 1.065e0, "2_to_13": 3.358e-3, "1_to_3": 4.038e3, "3_to_1": 4.038e3, "1_to_d": 3.938e-3, "2_to_d": 1.242e-5, "3_to_d": 3.929e-3},
    -6: {"13_to_2": 1.928e-2, "2_to_13": 6.323e-4, "1_to_3": 4.864e2, "3_to_1": 4.864e2, "1_to_d": 2.247e-5, "2_to_d": 7.371e-7, "3_to_d": 2.245e-5},
    -8: {"13_to_2": 1.698e-2, "2_to_13": 2.085e-3, "1_to_3": 3.793e2, "3_to_1": 3.793e2, "1_to_d": 9.532e-7, "2_to_d": 1.170e-7, "3_to_d": 9.528e-7},
    -10: {"13_to_2": 1.750e-2, "2_to_13": 6.028e-3, "1_to_3": 2.118e2, "3_to_1": 2.118e2, "1_to_d": 6.234e-8, "2_to_d": 2.147e-8, "3_to_d": 6.226e-8},
    -12: {"13_to_2": 1.441e-2, "2_to_13": 1.973e-3, "1_to_3": 3.536e2, "3_to_1": 3.536e2, "1_to_d": 5.965e-8, "2_to_d": 8.168e-9, "3_to_d": 5.965e-8}
}

d = 2.46e-10

def invert_3x3(mat):
    a = [row[:] for row in mat]
    for i in range(3):
        a[i] += [1 if i==j else 0 for j in range(3)]
    for col in range(3):
        pivot = None
        for row in range(col, 3):
            if abs(a[row][col]) > 1e-12:
                pivot = row
                break
        if pivot is None:
            raise ValueError("Singular matrix")
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
        val = a[col][col]
        for j in range(6):
            a[col][j] /= val
        for row in range(3):
            if row != col:
                factor = a[row][col]
                for j in range(6):
                    a[row][j] -= factor * a[col][j]
    inv = [[a[i][j+3] for j in range(3)] for i in range(3)]
    return inv

results = []
for q in [0, -2, -4, -6, -8, -10, -12]:
    r = rates_data[q]
    Q = [[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]]
    Q[0][0] = -(r["1_to_d"] + r["13_to_2"] + r["1_to_3"])
    Q[0][1] = r["13_to_2"]
    Q[0][2] = r["1_to_3"]
    Q[1][0] = r["2_to_13"] / 2.0
    Q[1][1] = -(r["2_to_d"] + r["2_to_13"])
    Q[1][2] = r["2_to_13"] / 2.0
    Q[2][0] = r["3_to_1"]
    Q[2][1] = r["13_to_2"]
    Q[2][2] = -(r["3_to_d"] + r["13_to_2"] + r["3_to_1"])
    M = [[ -Q[i][j] for j in range(3)] for i in range(3)]
    N = invert_3x3(M)
    start = 1
    lifetime_ns = N[0][start] + N[1][start] + N[2][start]
    lifetime_s = lifetime_ns * 1e-9
    num_13 = r["1_to_3"] * N[0][start]
    num_31 = r["3_to_1"] * N[2][start]
    total_hops = num_13 + num_31
    migration_distance_m = total_hops * d
    results.append({
        "charge_e": q,
        "lifetime_s": lifetime_s,
        "migration_distance_m": migration_distance_m
    })

results.sort(key=lambda x: abs(x["charge_e"]))
with open("/app/outputs/results.json", "w") as f:
    json.dump(results, f, indent=2)
'
