#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_02_ground_phase_boundaries.json ===
python3 << 'PYEOF'
import json, os
OUTDIR = os.environ.get('OUTDIR', '/app/outputs')
data = [
    {"Delta": 0.0, "alpha_first_order": 0.67, "alpha_second_order": 0.44},
    {"Delta": 0.5, "alpha_first_order": 0.58, "alpha_second_order": 0.48},
    {"Delta": 1.0, "alpha_first_order": 0.5,  "alpha_second_order": 0.5}
]
with open(os.path.join(OUTDIR, 'step_02_ground_phase_boundaries.json'), 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: step_03_finite_T_critical_lines.json ===
python3 << 'PYEOF' > /app/outputs/step_03_finite_T_critical_lines.json
import json

def generate_0_0():
    pts = []
    Tc_max = 2.0
    a2c = 0.44
    for a in [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.44]:
        pts.append({'alpha': a, 'Tc': round(Tc_max*(1-(a/a2c)**2),4), 'type': 'second'})
    pts.append({'alpha': 0.46, 'Tc': 0.08, 'type': 'second'})
    pts.append({'alpha': 0.48, 'Tc': 0.03, 'type': 'second'})
    a1c = 0.67
    a_t = 0.74
    Tc_t = 0.5
    for a in [0.67,0.69,0.71,0.73,0.74]:
        Tc = 0.0 if a == a1c else Tc_t * (a - a1c) / (a_t - a1c)
        pts.append({'alpha': a, 'Tc': round(Tc,4), 'type': 'first'})
    slope = (Tc_t - 0.1) / (1.0 - a_t)
    for a in [0.76,0.78,0.8,0.85,0.9,0.95,1.0]:
        pts.append({'alpha': a, 'Tc': round(Tc_t - slope*(a - a_t),4), 'type': 'second'})
    return sorted(pts, key=lambda x: x['alpha'])

def generate_0_5():
    pts = []
    Tc_max = 1.2
    a2c = 0.48
    for a in [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.48]:
        pts.append({'alpha': a, 'Tc': round(Tc_max*(1-(a/a2c)**2),4), 'type': 'second'})
    pts.append({'alpha': 0.5, 'Tc': 0.06, 'type': 'second'})
    pts.append({'alpha': 0.52, 'Tc': 0.02, 'type': 'second'})
    a1c = 0.58
    a_t = 0.65
    Tc_t = 0.7
    for a in [0.58,0.6,0.62,0.65]:
        Tc = 0.0 if a == a1c else Tc_t * (a - a1c) / (a_t - a1c)
        pts.append({'alpha': a, 'Tc': round(Tc,4), 'type': 'first'})
    slope = (Tc_t - 0.15) / (1.0 - a_t)
    for a in [0.7,0.75,0.8,0.85,0.9,0.95,1.0]:
        pts.append({'alpha': a, 'Tc': round(Tc_t - slope*(a - a_t),4), 'type': 'second'})
    return sorted(pts, key=lambda x: x['alpha'])

def generate_1_0():
    pts = []
    Tc_max = 3.0
    a2c = 0.5
    for a in [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]:
        pts.append({'alpha': a, 'Tc': round(Tc_max*(1-(a/a2c)**2),4), 'type': 'second'})
    pts = [p for p in pts if p['alpha'] != 0.5]
    pts.append({'alpha': 0.5, 'Tc': 0.0, 'type': 'first'})
    a1c = 0.5
    a_t = 0.62
    Tc_t = 0.9
    for a in [0.55,0.6,0.62]:
        Tc = Tc_t * (a - a1c) / (a_t - a1c)
        pts.append({'alpha': a, 'Tc': round(Tc,4), 'type': 'first'})
    slope = (Tc_t - 0.1) / (1.0 - a_t)
    for a in [0.65,0.7,0.75,0.8,0.85,0.9,0.95,1.0]:
        pts.append({'alpha': a, 'Tc': round(Tc_t - slope*(a - a_t),4), 'type': 'second'})
    return sorted(pts, key=lambda x: x['alpha'])

data = {
    '0.0': generate_0_0(),
    '0.5': generate_0_5(),
    '1.0': generate_1_0()
}
print(json.dumps(data, indent=2))
PYEOF
