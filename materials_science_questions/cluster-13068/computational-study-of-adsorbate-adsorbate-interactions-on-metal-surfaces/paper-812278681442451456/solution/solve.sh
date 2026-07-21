#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: verification_results.json ===
python3 -c "
import sys, json, math, cmath

test_cases = [
    {
        'alpha': 1/math.sqrt(2),
        'beta': 1/math.sqrt(2),
        'V': 1.0,
        'time_points': [0.0, 1.0, 2.0, 3.0, 4.0]
    },
    {
        'alpha': -1/math.sqrt(2),
        'beta': 1/math.sqrt(2),
        'V': 1.0,
        'time_points': [0.0, 1.0, 2.0, 3.0, 4.0]
    },
    {
        'alpha': 0.6,
        'beta': 0.8,
        'V': 0.5,
        'time_points': [0.0, 0.5, 1.0, 1.5]
    },
    {
        'alpha': 0.8,
        'beta': -0.6,
        'V': 2.0,
        'time_points': [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
    }
]

results = []
for c in test_cases:
    a = float(c['alpha'])
    b = float(c['beta'])
    V = float(c['V'])
    ts = [float(t) for t in c['time_points']]
    psi1_list = []
    psi2_list = []
    for t in ts:
        em = cmath.exp(-1j * V * t)
        ep = cmath.exp(1j * V * t)
        psi1 = ((a+b) * em + (a-b) * ep) / 2.0
        psi2 = ((a+b) * em - (a-b) * ep) / 2.0
        psi1_list.append([psi1.real, psi1.imag])
        psi2_list.append([psi2.real, psi2.imag])
    avg_energy = 2.0 * V * a * b
    results.append({
        'alpha': a,
        'beta': b,
        'V': V,
        'time_points': ts,
        'psi1': psi1_list,
        'psi2': psi2_list,
        'average_energy': avg_energy
    })

with open(sys.argv[1], 'w') as f:
    json.dump({'test_cases': results}, f, indent=2)
" "$OUTDIR/verification_results.json"
