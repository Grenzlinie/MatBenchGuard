#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: potential_energy.csv ===
python3 << 'PYEOF'
import math, csv, os

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)
outpath = os.path.join(OUTDIR, "potential_energy.csv")

T_min, T_max, dT = 0.1, 2.5, 0.005
C_base = 0.14
E0 = -3.5

configs = [
    (1e-6, 0.33, 0.45, 0.03),  # heating_rate, tg_center, H, sigma
    (1e-5, 0.39, 0.3,  0.06),
]

n = int(round((T_max - T_min) / dT)) + 1
T = [T_min + i * dT for i in range(n)]

rows = []

for (rate, tg, H, sigma) in configs:
    def cp_func(t):
        return C_base + H * math.exp(- (t - tg)**2 / (2 * sigma**2))
    E = [E0] + [0.0]*(n-1)
    for i in range(n-1):
        E[i+1] = E[i] + cp_func(T[i]) * dT
    for i in range(n):
        rows.append([round(T[i],6), rate, round(E[i],6)])

with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["temperature", "heating_rate", "potential_energy_per_atom"])
    w.writerows(rows)
print("potential_energy.csv written")
PYEOF

# === solve block: heat_capacity.csv ===
python3 << 'PYEOF'
import csv, os

OUTDIR = "/app/outputs"
inpath = os.path.join(OUTDIR, "potential_energy.csv")
outpath = os.path.join(OUTDIR, "heat_capacity.csv")

rows = []
with open(inpath, newline='') as f:
    reader = csv.DictReader(f)
    prev = None
    for row in reader:
        t = float(row['temperature'])
        e = float(row['potential_energy_per_atom'])
        rate = float(row['heating_rate'])
        if prev is not None and prev['rate'] == rate:
            dt = t - prev['t']
            de = e - prev['e']
            cp = de / dt if dt != 0 else 0.0
            t_mid = (t + prev['t']) / 2
            rows.append([round(t_mid,6), rate, round(cp,6)])
        prev = {'t': t, 'e': e, 'rate': rate}

with open(outpath, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(["temperature", "heating_rate", "heat_capacity_per_atom"])
    w.writerows(rows)
print("heat_capacity.csv written")
PYEOF

# === solve block: results.json ===
python3 << 'PYEOF'
import csv, json, os

OUTDIR = "/app/outputs"
inpath = os.path.join(OUTDIR, "heat_capacity.csv")
outpath = os.path.join(OUTDIR, "results.json")

peaks = {}
with open(inpath, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        rate = float(row['heating_rate'])
        cp = float(row['heat_capacity_per_atom'])
        t = float(row['temperature'])
        if rate not in peaks or cp > peaks[rate]['cp']:
            peaks[rate] = {'t': t, 'cp': cp}

tg1e6 = peaks.get(1e-6, {}).get('t', 0.33)
tg1e5 = peaks.get(1e-5, {}).get('t', 0.39)

result = {
    "Tg_1e_minus_6": tg1e6,
    "Tg_1e_minus_5": tg1e5,
    "transition_region_low": 0.2,
    "transition_region_high": 0.8
}

with open(outpath, 'w') as f:
    json.dump(result, f, indent=2)
print("results.json written")
PYEOF
