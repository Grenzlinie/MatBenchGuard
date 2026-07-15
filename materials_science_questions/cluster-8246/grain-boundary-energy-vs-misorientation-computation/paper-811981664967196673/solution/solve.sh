#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: grain_boundary_energies.json ===
cat > /tmp/compute_gb_energy.py <<'EOF'
import json
import math
import sys

# Parameters
b = 2.86
nu = 0.33
r0 = b / 4.0
mu = 1.0
e = math.e

angles_deg = [1.0, 2.0, 3.0, 4.0, 5.0]
angles_rad = [math.radians(d) for d in angles_deg]

# Pre-factor constants
const_wa = mu * b / (4.0 * math.pi * (1.0 - nu))
const_wbprime = mu * b * math.sqrt(2.0) * (4.0 - nu) / (16.0 * math.pi * (1.0 - nu))
const_wb = mu * b * (4.0 - nu) / (8.0 * math.pi * math.sqrt(3.0) * (1.0 - nu))

log2 = math.log(2.0)
u = math.exp(3.0 / (4.0 - nu) - nu * log2 / (4.0 - nu))
v = math.exp(3.0 / (4.0 - nu) - (2.0 + nu) * log2 / (4.0 - nu))

def compute_wa(theta):
    return const_wa * theta * math.log(e * b / (2.0 * math.pi * r0 * theta))

def compute_wbprime(theta):
    return const_wbprime * theta * math.log(u * b / (math.sqrt(2.0) * math.pi * r0 * theta))

def compute_wb(theta):
    return const_wb * theta * math.log(v * b * math.sqrt(3.0) / (2.0 * math.pi * r0 * theta))

A_type = [compute_wa(th) for th in angles_rad]
B_prime_type = [compute_wbprime(th) for th in angles_rad]
B_type = [compute_wb(th) for th in angles_rad]

# Ratio W_B′ / W_A at θ = 3° (index 2)
ratio_WBprime_WA = B_prime_type[2] / A_type[2]

result = {
    "tilt_angles_deg": angles_deg,
    "energies": {
        "A_type": A_type,
        "B_type": B_type,
        "B_prime_type": B_prime_type
    },
    "ratio_WBprime_WA": ratio_WBprime_WA
}

outfile = sys.argv[1] if len(sys.argv) > 1 else "/app/outputs/grain_boundary_energies.json"
with open(outfile, "w") as f:
    json.dump(result, f, indent=2)
EOF

python3 /tmp/compute_gb_energy.py /app/outputs/grain_boundary_energies.json
