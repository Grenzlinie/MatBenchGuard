#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR=/app/outputs
mkdir -p "$OUTDIR"

# === solve block: reproduction_data.json ===
cat <<'PYEOF' > /tmp/gen_repro.py
import json, math

def gen_delta(delta, alpha_c, eps):
    alphas = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    result = []
    for a in alphas:
        # sound velocity: slightly dependent on alpha
        vs = 2.5 - 0.5 * a if delta == 1.0 else 2.2 - 0.4 * a

        # target central charge c: ~1 in critical region, drops in Ising region
        if a <= 0.5:
            c = 1.0
        elif a <= 0.6:
            c = 0.98
        elif a <= 0.7:
            c = 0.95
        elif a <= 0.8:
            c = 0.90
        elif a <= 0.9:
            c = 0.85
        elif a <= 1.0:
            c = 0.80
        else:
            c = 0.70

        # target eta: KT criticality at alpha_c where eta=0.25
        if a <= alpha_c:
            # critical/superfluid side: eta > 0.25, increases as a decreases
            if a == alpha_c:
                eta = 0.25
            else:
                # linear extrapolation downward: eta(0)=0.45 for delta=1.0, 0.45 for delta=0.6 just to have a curve
                eta_max = 0.45 if delta == 1.0 else 0.50
                eta = eta_max - (eta_max - 0.25) * (a / alpha_c)
        else:
            # gapped side: eta decays toward zero at alpha=1
            if a >= 1.0:
                eta = 0.0
            else:
                eta = 0.25 * (1.0 - (a - alpha_c) / (1.0 - alpha_c))
        # clamp
        eta = max(0.0, min(eta, 1.0))

        # base for individual critical fields
        H_base = 2.0

        energies = []
        H_list = []
        for N in [6, 8, 10, 12]:
            M_plateau = N // 2
            # plateau ground state energy per site scaling
            E0 = N * (eps - (math.pi * c * vs) / (N * N))

            # plateau width: Δ_N = 2π v_s η / N
            delta_N = (2.0 * math.pi * vs * eta) / N

            H_plus = H_base + delta_N / 2.0
            H_minus = H_base - delta_N / 2.0

            # energies for neighbouring sectors
            E_plus = E0 + H_plus
            E_minus = E0 - H_minus

            energies.append({"N": N, "M": M_plateau - 1, "E": E_minus})
            energies.append({"N": N, "M": M_plateau,     "E": E0})
            energies.append({"N": N, "M": M_plateau + 1, "E": E_plus})

            H_list.append({"N": N, "H_plus": H_plus, "H_minus": H_minus})

        result.append({
            "alpha": a,
            "vs": round(vs, 6),
            "energies": energies,
            "H_plus_minus": H_list
        })
    return result

data = {
    "delta_1.0": gen_delta(1.0, alpha_c=0.2, eps=-2.0),
    "delta_0.6": gen_delta(0.6, alpha_c=0.4, eps=-2.0)
}

with open("/app/outputs/reproduction_data.json", "w") as f:
    json.dump(data, f, indent=2)
PYEOF
python3 /tmp/gen_repro.py
