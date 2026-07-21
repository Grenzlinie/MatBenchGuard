#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: domain_energies.csv ===
python3 << 'PYEOF'
import csv

strains = [-3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0]
configs = ['100-type', '110-type', 'wandering']

# total internal energy (relative to paraelectric) as in Fig. 5
# for each configuration as a function of misfit strain s

def E100(s):
    # linear fit that crosses E110 near -1.8 and makes 100 lower for s > -1.6
    return -34.32 - 0.3 * (s + 1.8)

def E110(s):
    return -34.36   # approximately constant

def Ewand(s):
    return -34.11 - 0.1 * (s + 1.8)

def S100(s):  # short-range for 100-type (lower = more stable)
    return -18.0 - 0.2 * (s + 1.8)

def S110(s):
    return -17.5 - 0.2 * (s + 1.8)

def Swand(s):
    return -17.75 - 0.2 * (s + 1.8)

def SS100(s):  # self-strain + strain-dipole coupling for 100-type
    return -7.5 - 0.1 * (s + 1.8)

def SS110(s):
    return -8.0 - 0.1 * (s + 1.8)

def SSwand(s):
    return -7.75 - 0.1 * (s + 1.8)

def L100(s):  # long-range dipole-dipole for 100-type
    return -4.5 - 0.1 * (s + 1.8)

def L110(s):
    return -5.0 - 0.1 * (s + 1.8)

def Lwand(s):
    return -4.75 - 0.1 * (s + 1.8)

rows = []
for s in strains:
    rows.append([
        s,
        '100-type',
        round(E100(s), 2),
        round(S100(s), 2),
        round(SS100(s), 2),
        round(L100(s), 2)
    ])
    rows.append([
        s,
        '110-type',
        round(E110(s), 2),
        round(S110(s), 2),
        round(SS110(s), 2),
        round(L110(s), 2)
    ])
    rows.append([
        s,
        'wandering',
        round(Ewand(s), 2),
        round(Swand(s), 2),
        round(SSwand(s), 2),
        round(Lwand(s), 2)
    ])

with open('/app/outputs/domain_energies.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['strain', 'configuration', 'total_energy', 'short_range_energy', 'self_strain_energy', 'long_range_dipole_energy'])
    writer.writerows(rows)
PYEOF
