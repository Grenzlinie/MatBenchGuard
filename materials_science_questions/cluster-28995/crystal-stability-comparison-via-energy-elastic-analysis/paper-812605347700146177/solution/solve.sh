#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: force_constants.json ===
python3 /solution/compute.py force_constants > /app/outputs/force_constants.json
cat > /solution/compute.py << 'PYEOF'
import json, sys, math

if sys.argv[1] == "force_constants":
    with open("/app/outputs/force_constants.json") as f:
        print(f.read())
elif sys.argv[1] == "elastic_moduli":
    with open("/app/outputs/force_constants.json") as f:
        fc = json.load(f)
    Rs = 2.20
    Z = 3
    cube_root_Z = Z ** (1/3)
    R_a = Rs * cube_root_Z
    omega_a = (4 * math.pi / 3) * (R_a ** 3)
    factor = (4 * omega_a) ** (-1/3)
    moduli = {}
    for key, val in fc.items():
        J = val["J"]
        R = val["R"]
        C = factor * (3 * J + R)
        C_prime = factor * (7 * J / 2 + R / 2)
        moduli[key] = {"C_FCC": C, "C_prime_FCC": C_prime}
    json.dump(moduli, sys.stdout, indent=2)
PYEOF

# === solve block: elastic_moduli_groupIII.json ===
python3 /solution/compute.py elastic_moduli > /app/outputs/elastic_moduli_groupIII.json
