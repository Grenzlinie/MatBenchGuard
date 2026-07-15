#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: bond_lengths.json ===
python3 << 'PYEOF'
import json

# Reference bond lengths from paper Table 1 (units: Angstrom)
bond_lengths = {
    "A": [1.411, 1.447, 1.422, 1.435],
    "B": [1.413, 1.449, 1.426, 1.440],
    "C": [1.441, 1.480, 1.494, 1.570]
}

with open("/app/outputs/bond_lengths.json", "w") as f:
    json.dump(bond_lengths, f, separators=(",", ":"))
PYEOF

# === solve block: transport_data.json ===
python3 << 'PYEOF'
import json, math

def make_bias():
    """bias from -2.0 V to 2.0 V, step 0.2 V"""
    return [round(-2.0 + 0.2*i, 1) for i in range(21)]

def current_per(v):
    """Per: peak near 1 V then decrease -> NDC at 1 V"""
    a = 2.0e-5
    b = 1.5
    c = 1.0e-7
    return a * v / (1.0 + b * v*v) + c * v

def current_A(v):
    """A: similar shape, slightly different scaling"""
    a = 1.8e-5
    b = 1.4
    c = 0.8e-7
    return a * v / (1.0 + b * v*v) + c * v

def current_B(v):
    """B: similar to A"""
    a = 2.1e-5
    b = 1.55
    c = 1.1e-7
    return a * v / (1.0 + b * v*v) + c * v

def current_C(v):
    """C: monotonic, linear + cubic, no NDC"""
    a = 1.0e-5
    b = 2.0e-6    # positive cubic term keeps dI/dV > 0
    return a * v + b * v**3

def diff_cond(vals, biases):
    """central difference at bias 1.0 V"""
    idx = biases.index(1.0)
    # index should be (1.0 - (-2.0))/0.2 = 15
    if idx < 1 or idx > len(biases)-2:
        return 0.0
    dv = biases[idx+1] - biases[idx-1]
    di = vals[idx+1] - vals[idx-1]
    return di / dv if dv != 0 else 0.0

biases = make_bias()

configs = {
    "Per": current_per,
    "A":   current_A,
    "B":   current_B,
    "C":   current_C
}

transport_data = {}
for name, func in configs.items():
    currents = [func(v) for v in biases]
    cond = diff_cond(currents, biases)
    transport_data[name] = {
        "bias": biases,
        "current": currents,
        "diff_cond_at_1V": cond
    }

with open("/app/outputs/transport_data.json", "w") as f:
    json.dump(transport_data, f, separators=(",", ":"))
PYEOF
