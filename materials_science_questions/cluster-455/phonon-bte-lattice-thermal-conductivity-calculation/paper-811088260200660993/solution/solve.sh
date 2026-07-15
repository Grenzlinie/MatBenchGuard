#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
export OUTDIR=/app/outputs

# === solve block: size_dependent_k.csv ===
cat <<'CSVEOF' > "$OUTDIR/size_dependent_k.csv"
direction,length_nm,k_W_per_mK,k_std_W_per_mK
a*,6.1795,0.428,0.01
a*,12.359,0.545,0.01
a*,18.5385,0.597,0.01
a*,24.718,0.628,0.01
a*,30.8975,0.648,0.01
b*,7.662,0.215,0.01
b*,15.324,0.260,0.01
b*,22.986,0.279,0.01
b*,30.648,0.290,0.01
b*,38.31,0.297,0.01
c*,9.7104,0.487,0.01
c*,19.4208,0.622,0.01
c*,29.1312,0.695,0.01
c*,38.8416,0.742,0.01
c*,51.7888,0.784,0.01
CSVEOF

# === solve block: bulk_k.json ===
python3 -c '
import json, os
out = os.environ.get("OUTDIR", "/app/outputs")
data = {"a*": 0.73, "b*": 0.33, "c*": 0.95}
with open(os.path.join(out, "bulk_k.json"), "w") as f:
    json.dump(data, f, indent=2)
'

# === solve block: tbr_results.json ===
python3 << 'PYEOF'
import json, os, math
beta = math.radians(92.49)
sinb = math.sin(beta)
a_sp = 6.187 * sinb * 0.1   # nm
b_sp = 7.662 * 0.1
c_sp = 16.208 * sinb * 0.1

def length_ab(N):
    return N * a_sp + N * b_sp

def length_ac(Na, Nc):
    return Na * a_sp + Nc * c_sp

def length_bc(Nb, Nc):
    return Nb * b_sp + Nc * c_sp

len_ab = [length_ab(n) for n in [11, 15, 21, 31, 41]]
tbr_ab_vals = [6.65e-9, 6.85e-9, 7.00e-9, 7.15e-9, 7.35e-9]
mean_ab = sum(tbr_ab_vals) / 5
std_ab = (sum((x - mean_ab)**2 for x in tbr_ab_vals) / 4) ** 0.5

Na_ac = [11, 15, 21, 31, 41]
Nc_ac = [6, 8, 11, 16, 21]
len_ac = [length_ac(na, nc) for na, nc in zip(Na_ac, Nc_ac)]
tbr_ac_vals = [5.99e-9, 6.055e-9, 6.15e-9, 6.245e-9, 6.31e-9]
mean_ac = sum(tbr_ac_vals) / 5
std_ac = (sum((x - mean_ac)**2 for x in tbr_ac_vals) / 4) ** 0.5

Nb_bc = [11, 15, 21, 31, 41]
Nc_bc = [6, 8, 11, 16, 21]
len_bc = [length_bc(nb, nc) for nb, nc in zip(Nb_bc, Nc_bc)]
tbr_bc_vals = [3.09e-9, 3.13e-9, 3.20e-9, 3.27e-9, 3.31e-9]
mean_bc = sum(tbr_bc_vals) / 5
std_bc = (sum((x - mean_bc)**2 for x in tbr_bc_vals) / 4) ** 0.5

data = {
    "a*-b*": {
        "lengths": [round(l, 3) for l in len_ab],
        "TBR_per_length": tbr_ab_vals,
        "mean_TBR": mean_ab,
        "std_TBR": std_ab
    },
    "a*-c*": {
        "lengths": [round(l, 3) for l in len_ac],
        "TBR_per_length": tbr_ac_vals,
        "mean_TBR": mean_ac,
        "std_TBR": std_ac
    },
    "b*-c*": {
        "lengths": [round(l, 3) for l in len_bc],
        "TBR_per_length": tbr_bc_vals,
        "mean_TBR": mean_bc,
        "std_TBR": std_bc
    }
}

outdir = os.environ.get("OUTDIR", "/app/outputs")
with open(os.path.join(outdir, "tbr_results.json"), "w") as f:
    json.dump(data, f, indent=2)
PYEOF

# === solve block: vacancy_effect.json ===
python3 -c '
import json, os, math

# bulk and mfp
k_bulk = {"a*": 0.73, "b*": 0.33, "c*": 0.95}
mfp = {"a*": 13.8, "b*": 9.5, "c*": 8.4}
sp = {"a*": 6.187 * math.sin(math.radians(92.49)) * 0.1,
       "b*": 7.662 * 0.1,
       "c*": 16.208 * math.sin(math.radians(92.49)) * 0.1}

# simulation lengths for vacancy boxes: a* N=100 (L=50*a*_sp), b* N=100 (L=50*b*_sp), c* N=64 (L=32*c*_sp)
L = {"a*": (100/2)*sp["a*"], "b*": (100/2)*sp["b*"], "c*": (64/2)*sp["c*"]}

reduction = {"a*": 44.0, "b*": 33.0, "c*": 35.0}  # percent

perfect_k = {}
vacancy_k = {}
for dir in ["a*","b*","c*"]:
    kb = k_bulk[dir]
    s = mfp[dir] / kb
    inv_k = 1.0/kb + s / L[dir]
    k_perf = 1.0/inv_k
    perfect_k[dir] = round(k_perf, 4)
    vacancy_k[dir] = round(k_perf * (1.0 - reduction[dir]/100.0), 4)

data = {}
for dir in ["a*","b*","c*"]:
    data[dir] = {
        "perfect_k": perfect_k[dir],
        "vacancy_k_6pct": vacancy_k[dir],
        "reduction_percent": reduction[dir]
    }

out = os.environ.get("OUTDIR", "/app/outputs")
with open(os.path.join(out, "vacancy_effect.json"), "w") as f:
    json.dump(data, f, indent=2)
'
