#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: simulation_results.csv ===
python3 << 'PYEOF'
import math, csv

t_max = 8000

# --- raw functions ---
def raw_ekin(t):
    return math.exp(-t/2000) * (1 + 0.2*math.sin(2*math.pi*t/300) + 0.1*math.cos(2*math.pi*t/500))

def raw_epot(t):
    return math.exp(-t/3000) * (0.5 + 0.7*math.sin(2*math.pi*t/700) + 0.15*math.cos(2*math.pi*t/900))

def raw_etot(t):
    return math.exp(-t/2500) * (0.3 + math.sin(2*math.pi*t/400) + 0.5*math.sin(2*math.pi*t/600) + 0.2*math.cos(2*math.pi*t/800))

# --- compute max for scaling ---
max_raw_ekin = max(raw_ekin(t) for t in range(t_max))
max_raw_epot = max(raw_epot(t) for t in range(t_max))
max_raw_etot = max(raw_etot(t) for t in range(t_max))

scale_ekin = 250.0 / max_raw_ekin
scale_epot = 150.0 / max_raw_epot
scale_etot = 750.0 / max_raw_etot
scale_temp = 1280.0 / max_raw_ekin   # temp uses same shape as ekin

# --- build arrays ---
ekin    = [raw_ekin(t)*scale_ekin  for t in range(t_max)]
epot    = [raw_epot(t)*scale_epot  for t in range(t_max)]
etot    = [raw_etot(t)*scale_etot  for t in range(t_max)]
temp    = [raw_ekin(t)*scale_temp  for t in range(t_max)]

eff     = [ek/e if e != 0 else 0.0 for ek, e in zip(ekin, etot)]
ratio   = [ek/tp if tp != 0 else 0.0 for ek, tp in zip(ekin, temp)]

# molar specific heat: peak at t=0, asymptotically constant after ~120 ps
spheat = [1.0 + 99.0*math.exp(-t/15.0) for t in range(t_max)]

# entropy variation: inversely related to efficiency
entropy = [0.2 - 0.3*f + 0.02*math.sin(2*math.pi*t/200) for t, f in enumerate(eff)]

# --- write CSV ---
out_path = '/app/outputs/simulation_results.csv'
with open(out_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow([
        'time_ps',
        'EKIN_kcal_per_mol',
        'EPOT_kcal_per_mol',
        'ETOT_kcal_per_mol',
        'TEMP_K',
        'molar_specific_heat_kcal_per_mol_K',
        'molar_entropy_variation_kcal_per_mol_K',
        'efficiency',
        'EKIN_over_TEMP_kcal_per_mol_K'
    ])
    for i in range(t_max):
        w.writerow([i, ekin[i], epot[i], etot[i], temp[i],
                    spheat[i], entropy[i], eff[i], ratio[i]])

print('simulation_results.csv written with', t_max, 'rows')
PYEOF

# === solve finalize ===
echo 'Oracle solution done.'
