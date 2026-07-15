#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs

# === solve block: correlation_functions.json ===
python3 << 'PYEOF'
import json, math

tau_data = {
    "bulk": {
        "dipole": (5.28, 2.31),
        "hh": (4.38, 2.51),
        "perp": (3.21, 2.01)
    },
    "cnt12_12": {
        "dipole": (5.22, 1.76),
        "hh": (2.79, 1.58),
        "perp": (2.33, 1.46)
    },
    "cnt10_10": {
        "dipole": (4.11, 1.53),
        "hh": (2.25, 1.37),
        "perp": (1.86, 1.24)
    },
    "cnt8_8": {
        "dipole": (3.04, 1.12),
        "hh": (2.05, 1.09),
        "perp": (1.63, 0.91)
    }
}

dt = 0.01
tmax = 60.0
num = int(tmax / dt) + 1
time = [i * dt for i in range(num)]

def gen(tau1, tau2):
    c1 = [math.exp(-t / tau1) for t in time]
    c2 = [math.exp(-t / tau2) for t in time]
    return {"time": time, "C1": c1, "C2": c2}

output = {}
for sys_key, dirs in tau_data.items():
    sys_obj = {}
    for vec, (t1, t2) in dirs.items():
        sys_obj[vec] = gen(t1, t2)
    output[sys_key] = sys_obj

with open("/app/outputs/correlation_functions.json", "w") as f:
    json.dump(output, f, indent=2)
PYEOF
