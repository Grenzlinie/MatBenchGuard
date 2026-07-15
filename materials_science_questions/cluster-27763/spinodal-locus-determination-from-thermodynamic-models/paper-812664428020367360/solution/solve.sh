#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: binodal_result.json ===
python3 > "$OUTDIR/binodal_result.json" <<'PYEOF'
import json, math

N = 1000
u = 0.1
U = u * N
Rg = math.sqrt(N / 6.0)

def NPhi_flower(phi, a):
    """Landau free energy for z0>0, φ>-1."""
    if phi <= -1.0 or phi >= 1.0:
        return float('inf')
    return (math.log(N * math.pi / 2.0) + 0.5 * math.log(1 - phi * phi)
            + 2 * a * a / (1 - phi) + U * (1 - phi) / 2.0)

def NPhi_coil(a):
    """Coil minimum at φ=-1 for z0>0."""
    return -math.log(math.erf(a)) + U

def find_flower_minimum(a):
    """Return (φ_min, NΦ_min) for the flower state."""
    # Coarse scan
    best_phi = 0.0
    best_val = float('inf')
    n = 500
    for i in range(n + 1):
        phi = -0.999 + i * 1.998 / n
        val = NPhi_flower(phi, a)
        if val < best_val:
            best_val = val
            best_phi = phi
    # Refine around the minimum
    window = 0.02
    n_fine = 1000
    lo = max(-0.999, best_phi - window)
    hi = min(0.999, best_phi + window)
    for i in range(n_fine + 1):
        phi = lo + i * (hi - lo) / n_fine
        val = NPhi_flower(phi, a)
        if val < best_val:
            best_val = val
            best_phi = phi
    return best_phi, best_val

def delta_NPhi(a):
    """NΦ_flower - NΦ_coil."""
    _, val_fl = find_flower_minimum(a)
    val_coil = NPhi_coil(a)
    return val_fl - val_coil

# Find a_star where delta_NPhi = 0 by bisection
a_lo, a_hi = 0.01, 10.0
d_lo = delta_NPhi(a_lo)
d_hi = delta_NPhi(a_hi)
# Extend range if same sign
while d_lo * d_hi > 0:
    if d_lo < 0:
        a_lo = a_hi
        a_hi *= 2.0
        d_lo = d_hi
        d_hi = delta_NPhi(a_hi)
    else:
        a_hi = a_lo
        a_lo *= 0.5
        d_hi = d_lo
        d_lo = delta_NPhi(a_lo)

for _ in range(60):
    a_mid = (a_lo + a_hi) / 2.0
    d_mid = delta_NPhi(a_mid)
    if abs(d_mid) < 1e-6:
        a_star = a_mid
        break
    if d_lo * d_mid < 0:
        a_hi = a_mid
        d_hi = d_mid
    else:
        a_lo = a_mid
        d_lo = d_mid
else:
    a_star = (a_lo + a_hi) / 2.0

z0_star = a_star * 2.0 * Rg
phi_flower, NPhi_flower_val = find_flower_minimum(a_star)
NPhi_coil_val = NPhi_coil(a_star)

result = {
    "N": N,
    "u": u,
    "z0_star": z0_star,
    "coil_minimum": {
        "phi": -1.0,
        "NPhi": NPhi_coil_val
    },
    "flower_minimum": {
        "phi": phi_flower,
        "NPhi": NPhi_flower_val
    }
}
print(json.dumps(result, indent=2))
PYEOF
