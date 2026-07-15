#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_thermochemistry.csv ===
cat > /app/outputs/step_01_thermochemistry.csv <<'EOF'
species,T,H,S,Cp
SiH4,298.15,-90.0,220.0,35.0
C3H8,298.15,-190.0,270.0,70.0
H2,298.15,-45.0,130.0,29.0
SiC2,298.15,-290.0,240.0,45.0
Si2C,298.15,-390.0,300.0,60.0
SiCl4,298.15,-790.0,350.0,80.0
SiCl2,298.15,-490.0,280.0,55.0
HCl,298.15,-140.0,186.0,29.0
Si,298.15,10.0,18.0,20.0
CH4,298.15,-170.0,186.0,35.0
C2H2,298.15,-140.0,200.0,44.0
Cl2,298.15,0.0,223.0,34.0
EOF

# === solve block: step_02_deltaG.csv ===
python3 <<'PYEOF'
import csv
def parse_side(s, g0):
    parts = s.strip().split('+')
    total = 0.0
    for p in parts:
        p = p.strip()
        if not p:
            continue
        tokens = p.split()
        coeff = 1
        if tokens[0].isdigit():
            coeff = int(tokens[0])
            species = ' '.join(tokens[1:])
        else:
            species = ' '.join(tokens)
        total += coeff * g0[species]
    return total

g0 = {}
with open('/solution/species_G0.csv', newline='') as f:
    for row in csv.DictReader(f):
        g0[row['species'].strip()] = float(row['G0_kJmol'])

rows = []
with open('/solution/reactions.csv', newline='') as f:
    for row in csv.DictReader(f):
        rid = row['reaction_id']
        react = row['reactants']
        prod = row['products']
        dG = parse_side(prod, g0) - parse_side(react, g0)
        rows.append([rid, react, prod, dG])

with open('/app/outputs/step_02_deltaG.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reaction_id','reactants','products','DeltaG_0K'])
    for r in rows:
        w.writerow(r)
PYEOF

# === solve block: step_03_LFER_fit.csv ===
python3 <<'PYEOF'
import csv

dg = {}
with open('/app/outputs/step_02_deltaG.csv', newline='') as f:
    for row in csv.DictReader(f):
        dg[row['reaction_id']] = float(row['DeltaG_0K'])

ea = {}
with open('/solution/literature_Ea.csv', newline='') as f:
    for row in csv.DictReader(f):
        ea[row['reaction_id']] = float(row['Ea_kJmol'])

points = [(dg[rid], ea[rid]) for rid in ea if rid in dg and dg[rid] > 0]
n = len(points)
if n < 2:
    raise ValueError('Not enough positive dG for LFER')
sx = sum(p[0] for p in points)
sy = sum(p[1] for p in points)
sxy = sum(p[0]*p[1] for p in points)
sxx = sum(p[0]*p[0] for p in points)
denom = n*sxx - sx*sx
slope = (n*sxy - sx*sy) / denom
intercept = (sy - slope*sx) / n
with open('/app/outputs/step_03_LFER_fit.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['parameter','value'])
    w.writerow(['slope', slope])
    w.writerow(['intercept', intercept])
PYEOF

# === solve block: step_04_rate_constants.csv ===
python3 <<'PYEOF'
import csv, math

with open('/app/outputs/step_03_LFER_fit.csv', newline='') as f:
    params = {row['parameter']: float(row['value']) for row in csv.DictReader(f)}
slope = params['slope']
intercept = params['intercept']

dg = {}
with open('/app/outputs/step_02_deltaG.csv', newline='') as f:
    for row in csv.DictReader(f):
        dg[row['reaction_id']] = float(row['DeltaG_0K'])

R = 0.0083144621  # kJ/mol*K
A = 1e14
temps = [2000.0, 2500.0]
rows = []
for rid, dg_val in dg.items():
    Ea = slope*dg_val + intercept if dg_val > 0 else 0.0
    for T in temps:
        k = A * math.exp(-Ea/(R*T))
        rows.append([rid, T, Ea, A, k])

with open('/app/outputs/step_04_rate_constants.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reaction_id','T','Ea','A','k'])
    for r in rows:
        w.writerow(r)
PYEOF
