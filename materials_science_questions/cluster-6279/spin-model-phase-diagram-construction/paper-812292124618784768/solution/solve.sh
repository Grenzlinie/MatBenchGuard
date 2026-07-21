#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: phase_diagram_lines.json ===
python3 << 'PYEOF'
import json, math, numpy as np
from scipy.optimize import brentq, fsolve
import os

Ax, Dx, Ay, Dy, mux, k = 1.0, 0.5, 1.0, 0.0, 1.0, 1.0
Sum_AD = Ax + Dx
gamma = (Ax - Dx) / Sum_AD

# ----- existence flags and intercepts (analytic) -----

ap2_exists = (Ax + Dx > 0)
ap2_H = (Ax - Dx) / mux if ap2_exists else None
ap2_T = (Ax + Dx) / k   if ap2_exists else None

ap1_exists = (Dx > 0)
ap1_H = Ax / mux if ap1_exists else None

bp2_exists = (Ax + Ay - Dx + Dy > 0) and (Ay + Dy > 0)
bp2_H = (Ax + Ay - Dx + Dy) / mux if bp2_exists else None
bp2_T = (Ay + Dy) / k             if bp2_exists else None

ab_exists = not (Ay + Dy < Dx)
ab_H = math.sqrt((Ax + Ay - Dx + Dy) * (Ax - Ay + Dx - Dy)) / mux if ab_exists else None

# ----- internal a first-order critical point -----

int_a_exists = (0 < Dx < 3/5 * Ax)
internal_crit = None

if int_a_exists:
    def get_b(a, t, a_min=1e-6, a_max=0.9999):
        """return b < 0 solving a - b = t*(atanh(a) - atanh(b)), or None"""
        if not (a_min < a < a_max):
            return None
        # function F(b) = a - b - t*(atanh(a)-atanh(b))
        def F(b):
            if abs(b) >= 1:
                return np.inf
            return a - b - t*(math.atanh(a) - math.atanh(b))
        # find a negative b
        for b_left, b_right in [(-0.9999, -1e-6), (-0.9999, -0.5), (-0.5, -1e-6)]:
            if b_left >= b_right:
                continue
            try:
                f_left = F(b_left)
                f_right = F(b_right)
                if (f_left > 0 and f_right < 0) or (f_left < 0 and f_right > 0):
                    b = brentq(lambda b: F(b), b_left, b_right, xtol=1e-12)
                    if abs(b) < 1 and b < 0:
                        return b
            except Exception:
                pass
        # fallback: fsolve with initial guess -a
        try:
            sol = fsolve(lambda b: F(b), -a, maxfev=1000, xtol=1e-12)
            b = sol[0]
            if abs(b) < 1 and b < 0:
                return b
        except Exception:
            pass
        return None

    def dh_da(a, t):
        b = get_b(a, t)
        if b is None:
            return None
        u = 1.0/(1.0 - a*a)
        v = 1.0/(1.0 - b*b)
        denom = 1.0 - t*v
        if abs(denom) < 1e-12:
            return None
        db_da = (1.0 - t*u)/denom
        return 0.5*(t*(u + v*db_da) + gamma*(1.0+db_da))

    def find_spinodal_roots(t, a_vals=None):
        if a_vals is None:
            a_vals = np.linspace(0.001, 0.999, 600)
        f = np.full(len(a_vals), np.nan)
        for i, a in enumerate(a_vals):
            val = dh_da(a, t)
            if val is not None and np.isfinite(val):
                f[i] = val
        roots = []
        for i in range(1, len(a_vals)):
            if np.isfinite(f[i-1]) and np.isfinite(f[i]):
                if (f[i-1]>0 and f[i]<0) or (f[i-1]<0 and f[i]>0):
                    try:
                        r = brentq(lambda aa: dh_da(aa, t),
                                   a_vals[i-1], a_vals[i], xtol=1e-12)
                        roots.append(r)
                    except Exception:
                        pass
        return sorted(set(round(r, 14) for r in roots))

    try:
        # crude sweep to locate t where at least 2 roots exist
        t_lo, t_hi = 0.001, 0.75
        have_lo = False
        for t_try in np.arange(t_lo, t_hi, 0.02):
            n_roots = len(find_spinodal_roots(t_try))
            if n_roots >= 2:
                t_lo, have_lo = t_try, True
                break
        if not have_lo:
            raise RuntimeError("No temperature with two spinodal roots found")

        while len(find_spinodal_roots(t_hi)) >= 2 and t_hi < 0.8:
            t_hi += 0.05

        # binary refine down to 1e-7
        for _ in range(80):
            t_mid = (t_lo + t_hi)/2.0
            roots_mid = find_spinodal_roots(t_mid)
            if len(roots_mid) >= 2:
                t_lo = t_mid
            else:
                t_hi = t_mid

        t_crit = t_lo
        roots_crit = find_spinodal_roots(t_crit)
        if len(roots_crit) == 1:
            a_crit = roots_crit[0]
        elif len(roots_crit) >= 2:
            a_crit = (roots_crit[0] + roots_crit[1]) / 2.0
        else:
            a_crit = None

        if a_crit is not None:
            b_crit = get_b(a_crit, t_crit)
            if b_crit is not None:
                m_plus = (a_crit + b_crit)/2.0
                h_plus = (t_crit/2.0)*(math.atanh(a_crit) + math.atanh(b_crit))
                h = h_plus + gamma * m_plus
                internal_crit = {
                    "T_c": t_crit * Sum_AD / k,
                    "H_x_c": h * Sum_AD / mux
                }
    except Exception:
        # leave internal_crit as None; block still writes valid JSON
        pass

# ----- assemble and write output -----

transitions = [
    {"type": "a-p second-order", "exists": ap2_exists,
     "order": "second" if ap2_exists else None,
     "H_x_intercept": ap2_H, "T_intercept": ap2_T, "critical_point": None},
    {"type": "a-p first-order", "exists": ap1_exists,
     "order": "first" if ap1_exists else None,
     "H_x_intercept": ap1_H, "T_intercept": None, "critical_point": None},
    {"type": "internal a first-order", "exists": int_a_exists,
     "order": "first" if int_a_exists else None,
     "H_x_intercept": None, "T_intercept": None,
     "critical_point": internal_crit},
    {"type": "b-p second-order", "exists": bp2_exists,
     "order": "second" if bp2_exists else None,
     "H_x_intercept": bp2_H, "T_intercept": bp2_T, "critical_point": None},
    {"type": "a-b first-order", "exists": ab_exists,
     "order": "first" if ab_exists else None,
     "H_x_intercept": ab_H, "T_intercept": None, "critical_point": None}
]

os.makedirs("/app/outputs", exist_ok=True)
with open("/app/outputs/phase_diagram_lines.json", "w") as f:
    json.dump({"transitions": transitions}, f, indent=2)
PYEOF
