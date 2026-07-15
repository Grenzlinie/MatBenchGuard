#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
export OUTDIR=/app/outputs
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple mpmath

# === solve block: step_01_lambda1_values.json ===
# STEP 1: λ1 limits (ζ=0 and ζ=1)
python3 << 'STEP01'
import json, mpmath as mp

mp.mp.dps = 50
pi = mp.pi
alpha = (9*pi/4)**(-mp.mpf(1)/3)

# closed‑form values for λ1 components at ζ=0
lambda1_a_0 = alpha * (pi**2 - 6) / (24 * pi**3)
lambda1_b_0 = alpha * (pi**2 - 12 * mp.log(2)) / (4 * pi**3)
lambda1_0 = lambda1_a_0 + lambda1_b_0

# ferromagnetic limits
lambda1_a_1 = 2**(-mp.mpf(7)/3) * lambda1_a_0 * (pi**2 + 6) / (pi**2 - 6)
lambda1_b_1 = 2**(-mp.mpf(4)/3) * lambda1_b_0
lambda1_1 = lambda1_a_1 + lambda1_b_1

result = {
    "lambda1_0": float(lambda1_0),
    "lambda1_1": float(lambda1_1),
    "lambda1_a_0": float(lambda1_a_0),
    "lambda1_a_1": float(lambda1_a_1),
    "lambda1_b_0": float(lambda1_b_0),
    "lambda1_b_1": float(lambda1_b_1)
}

with open("/app/outputs/step_01_lambda1_values.json", "w") as f:
    json.dump(result, f)

print("step_01_lambda1_values.json written")
STEP01

# Fix the compute.py that the step_02 and step_03 blocks will call.
# The old version only handled step02; now step03 is also supported.
cat > /solution/compute.py << 'COMPUTE'
import sys, json, mpmath as mp

def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--step':
        sys.exit(1)
    step = sys.argv[2]
    mp.mp.dps = 50
    pi = mp.pi

    if step == 'step02':
        # spin‑resolved fractions at ζ=0.5 (Eqs. 16,17,32,33)
        zeta = mp.mpf('0.5')
        k_up = (1 + zeta)**(mp.mpf(1)/3)
        k_dn = (1 - zeta)**(mp.mpf(1)/3)

        def Li2(x):
            return mp.polylog(2, x)

        # Eq (16) – Λ1^a(ζ)
        term1 = (pi**2/6 + mp.mpf(1)/4) * (k_dn**2 + k_up**2) - mp.mpf(3)/2 * k_dn * k_up
        term2 = -(k_dn**2 + k_up**2) / (k_dn**2 - k_up**2) * k_dn * k_up * mp.log(k_dn / k_up)
        term3 = -(k_dn**2 - k_up**2)/2 * (Li2((k_dn - k_up)/(k_dn + k_up)) - Li2((k_up - k_dn)/(k_dn + k_up)))
        Lambda1_a = mp.mpf(3)/(pi**2 - 6) * (term1 + term2 + term3)

        # Eq (32) – Λ1^{a,↑↑}
        Lambda1_a_upup = mp.mpf(1)/8 * (pi**2 + 6)/(pi**2 - 6) * (1+zeta)**(mp.mpf(2)/3) / Lambda1_a

        # Eq (17) – Λ1^b(ζ)
        term_b1 = pi**2/6 * (k_dn**2 + k_up**2) + (1 - mp.log(2)) * (k_dn - k_up)**2
        term_b2 = -k_dn**2/2 * Li2((k_dn - k_up)/(k_dn + k_up)) - k_up**2/2 * Li2((k_up - k_dn)/(k_dn + k_up))
        term_b3 = (1/(k_dn*k_up)) * (k_dn**4 * mp.log(k_dn/(k_dn+k_up)) + k_dn**2*k_up**2 * mp.log(k_dn*k_up/(k_dn+k_up)**2) + k_up**4 * mp.log(k_up/(k_dn+k_up)))
        Lambda1_b = mp.mpf(3)/(pi**2 - 12*mp.log(2)) * (term_b1 + term_b2 + term_b3)

        # Eq (33) – Λ1^{b,↑↑}
        Lambda1_b_upup = mp.mpf(1)/4 * (1+zeta)**(mp.mpf(2)/3) / Lambda1_b

        result = {
            "Lambda1_a_upup_05": float(Lambda1_a_upup),
            "Lambda1_b_upup_05": float(Lambda1_b_upup)
        }
        json.dump(result, sys.stdout)

    elif step == 'step03':
        # correction term δλ1^a(1) = 2^{-1/3} * α / (8π^3)
        alpha = (9*pi/4)**(-mp.mpf(1)/3)
        delta = 2**(-mp.mpf(1)/3) * alpha / (8 * pi**3)
        result = {"delta_lambda1a_1": float(delta)}
        json.dump(result, sys.stdout)

    else:
        sys.exit(0)

if __name__ == '__main__':
    main()
COMPUTE
chmod +x /solution/compute.py

# === solve block: step_02_spin_resolution.json ===
python3 /solution/compute.py --step step02 > "$OUTDIR/step_02_spin_resolution.json"

# === solve block: step_03_delta_lambda1a.json ===
python3 /solution/compute.py --step step03 > "$OUTDIR/step_03_delta_lambda1a.json"
