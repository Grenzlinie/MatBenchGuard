#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_acf_time_averages.json ===
cat > /tmp/write_step_01.py << 'PYEOF'
from fractions import Fraction
import json, os

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)

half_int_data = [
    ("1/2", "5/9"),
    ("3/2", "779/1575"),
    ("5/2", "986093/2027025"),
    ("7/2", "21117673/43648605"),
    ("9/2", "302812778207/627448696875"),
    ("11/2", "2796327017071/5801928464475"),
    ("13/2", "19699872589701257/40906818968140125"),
]
int_data = [
    ("1", "40/81"),
    ("2", "5473/11250"),
    ("3", "59747/123480"),
    ("4", "464441/962280"),
    ("5", "26536/55055"),
    ("6", "33240299/69020952"),
    ("7", "11459968711/23808330000"),
]

def make_entry(spin_str, frac_str):
    s_frac = Fraction(spin_str)
    avg_frac = Fraction(frac_str)
    return {"s": float(s_frac), "average": float(avg_frac)}

half_ints = [make_entry(spin, frac) for spin, frac in half_int_data]
ints = [make_entry(spin, frac) for spin, frac in int_data]

with open(os.path.join(outdir, "step_01_acf_time_averages.json"), "w") as f:
    json.dump({"half_integer": half_ints, "integer": ints}, f, indent=2)
PYEOF
python3 /tmp/write_step_01.py

# === solve block: step_02_levin_estimates.json ===
cat > /tmp/write_step_02.py << 'PYEOF'
from fractions import Fraction
import math, json, os

half_fracs = [
    "5/9",
    "779/1575",
    "986093/2027025",
    "21117673/43648605",
    "302812778207/627448696875",
    "2796327017071/5801928464475",
    "19699872589701257/40906818968140125",
]

int_fracs = [
    "40/81",
    "5473/11250",
    "59747/123480",
    "464441/962280",
    "26536/55055",
    "33240299/69020952",
    "11459968711/23808330000",
]

def levin_m(frac_strs, M):
    U = [Fraction(s) for s in frac_strs]
    u = [U[0]] + [U[k] - U[k-1] for k in range(1, len(U))]
    sum_num = Fraction(0, 1)
    sum_den = Fraction(0, 1)
    for k in range(1, M+1):
        coeff_val = ((-1)**(k-1)) * math.comb(M, k) * (k**(M-2))
        coeff = Fraction(coeff_val, 1)
        sum_num += coeff * U[k-1] / u[k-1]
        sum_den += coeff / u[k-1]
    return float(sum_num / sum_den) if sum_den != 0 else float('nan')

half_est = levin_m(half_fracs, 7)
int_est = levin_m(int_fracs, 7)
classical = 9/40 * math.log(3) + 7/30

outdir = os.environ.get('OUTDIR', '/app/outputs')
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "step_02_levin_estimates.json"), "w") as f:
    json.dump({"half_integer_estimate": half_est, "integer_estimate": int_est, "classical_result": classical}, f, indent=2)
PYEOF
python3 /tmp/write_step_02.py
