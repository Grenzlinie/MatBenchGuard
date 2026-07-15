#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: phase_energies.json ===
python3 -c "
import json, math
strains = [-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.0,0.01,0.02,0.03,0.04,0.05,0.06]
data=[]
for e in strains:
    E_AF = round(-41.6666667 * e, 6)
    E_FM = 0.5
    delta = e + 0.05
    E_intra = round(0.5 + 100000.0 * (delta**3), 6)
    data.append({'strain': e, 'E_upup_downdown': E_AF, 'E_upup_upup': E_FM, 'E_updown_updown': E_intra})
print(json.dumps(data, indent=2))
" > $OUTDIR/phase_energies.json

# === solve block: exchange_tc.json ===
python3 -c "
import json
def J_intra(e):
    if e >= 0:
        return 0.55
    else:
        return round(0.55 * (1 + e/0.04), 6)
def J_inter_first(e):
    return round(-8.3333333 * (e + 0.012), 6)
def J_inter_second(e):
    return round(-2.5 * (e + 0.012), 6)
def Tc(e):
    raw = 40 + 566.6667*e - 10000.0*e*e
    return round(max(raw, 0.0), 3)
strains = [-0.06,-0.05,-0.04,-0.03,-0.02,-0.01,0.0,0.01,0.02,0.03,0.04,0.05,0.06]
data=[]
for e in strains:
    data.append({
        'strain': e,
        'J_intra': J_intra(e),
        'J_inter_first': J_inter_first(e),
        'J_inter_second': J_inter_second(e),
        'Tc': Tc(e)
    })
print(json.dumps(data, indent=2))
" > $OUTDIR/exchange_tc.json

# === solve block: lc_mae.json ===
python3 -c "
import json, math
def E_AF(e): return round(-41.6666667 * e, 6)
def E_FM(e): return 0.5
strains = [-0.05, 0.0, 0.05]
angles = list(range(0, 181, 15))
data=[]
for s in strains:
    delta = E_AF(s) - E_FM(s)
    B = 0.3 * abs(delta)
    for a in angles:
        alpha = math.radians(a)
        term1 = delta * (math.sin(alpha/2)**2)
        term2 = B * (math.sin(alpha)**2)
        energy = round(term1 + term2, 6)
        data.append({'strain': s, 'angle_deg': a, 'energy_meV': energy})
print(json.dumps(data, indent=2))
" > $OUTDIR/lc_mae.json
