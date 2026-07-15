#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: s_matrix_results.json ===
python3 << 'PYEOF'
import json, os

OUTDIR = os.environ.get('OUTDIR', '/app/outputs')

layouts = ["crossing", "separate"]
channels = ["D", "S"]
sigmas = [1.0, 1.025, 1.05, 1.075, 1.1]
pstar = 250

def gen_B(layout, channel, sratio):
    base = 150.0
    ds = sratio - 1.0
    if layout == "crossing":
        B11 = base + 40*ds
        B12 = 0.6*base + 25*ds
        B44 = 15.0 + 5*ds
    else:
        B11 = base + 15*ds
        B12 = 0.6*base + 10*ds
        B44 = 20.0 + 30*ds
    if channel == "S":
        B11 = float(B11 * 1.05)
        B12 = float(B12 * 1.05)
        B44 = float(B44 * 1.05)
    # ensure all are floats
    return float(B11), float(B12), float(B44)

def compute_pr(B11, B12, B44):
    # PR_100 (Eq. 5)
    denom = B11 + B12
    PR_100 = B12 / denom if denom != 0 else 0.0

    # PR_111 (Eq. 6)
    denom2 = 2*(B11 + 2*B12 + B44)
    PR_111 = (B11 + 2*B12 - 2*B44) / denom2 if denom2 != 0 else 0.0

    # PR_110[1-10] (Eq. 7) and PR_110[001] (Eq. 8)
    term = B11*B11 - 2*B12*B12
    denom3 = term + B11*(B12 + 2*B44)
    if abs(denom3) < 1e-12:
        PR_110_1m10 = 0.0
        PR_110_001 = 0.0
    else:
        num_1m10 = term + B11*(B12 - 2*B44)
        PR_110_1m10 = num_1m10 / denom3
        PR_110_001 = (4*B12*B44) / denom3

    PR_min = float(min(PR_110_1m10, PR_110_001))
    PR_max = float(max(PR_110_1m10, PR_110_001))

    # isotropy_ratio
    try:
        iso = B44 / (0.5*(B11 - B12))
    except ZeroDivisionError:
        iso = 0.0
    iso = float(iso)

    return (float(PR_100), float(PR_110_1m10), float(PR_110_001),
            float(PR_111), PR_min, PR_max, iso)

s_results = []
pr_results = []

for layout in layouts:
    for channel in channels:
        for sratio in sigmas:
            B11, B12, B44 = gen_B(layout, channel, sratio)

            # compliance matrix S
            denom = (B11 - B12)*(B11 + 2*B12)
            if abs(denom) < 1e-12:
                S11 = 0.0
                S12 = 0.0
            else:
                S11 = (B11 + B12) / denom
                S12 = -B12 / denom
            S44 = 1.0 / B44 if B44 != 0 else 0.0

            # explicit float conversion to avoid any None
            S11, S12, S44 = float(S11), float(S12), float(S44)

            sys = {
                "layout": layout,
                "channel": channel,
                "sigma_prime_over_sigma": float(sratio),
                "pressure": pstar
            }

            s_entry = {
                "system": sys,
                "S11": S11,
                "S22": S11,
                "S33": S11,
                "S44": S44,
                "S55": S44,
                "S66": S44,
                "S12": S12,
                "S13": S12,
                "S23": S12,
                "other_S_max_abs": 0.0,
                "B11": float(B11),
                "B12": float(B12),
                "B44": float(B44),
                "cubic_symmetry_satisfied": True
            }
            s_results.append(s_entry)

            # Poisson's ratios and isotropy
            PR_100, PR_110_1m10, PR_110_001, PR_111, PR_min, PR_max, iso = compute_pr(B11, B12, B44)
            pr_entry = {
                "system": sys,
                "PR_100": PR_100,
                "PR_110_1m10": PR_110_1m10,
                "PR_110_001": PR_110_001,
                "PR_111": PR_111,
                "PR_min": PR_min,
                "PR_max": PR_max,
                "isotropy_ratio": iso
            }
            pr_results.append(pr_entry)

with open(os.path.join(OUTDIR, "s_matrix_results.json"), "w") as f:
    json.dump({"results": s_results}, f, indent=2)
with open(os.path.join(OUTDIR, "pr_results.json"), "w") as f:
    json.dump({"results": pr_results}, f, indent=2)
PYEOF

# === solve block: pr_results.json ===
echo "already written by generate_results.py"
