#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: eos_fit_results.json ===
mkdir -p /app/outputs
python3 << 'PYEOF'
import json, csv, sys, io
import numpy as np
from scipy.optimize import curve_fit

# Inline pressure-volume data from Table 2 (Ambient as P=0)
raw = """P,a,V
0.0,9.294,803
1.6,9.263,798
4.5,9.236,788
8.7,9.189,776
12.3,9.152,766
15.7,9.118,758
17.9,9.097,753
20.2,9.071,746
22.7,9.047,740
24.3,9.030,736
"""
reader = csv.DictReader(io.StringIO(raw), skipinitialspace=True)
data = []
for row in reader:
    P = float(row['P'])
    V = float(row['V'])
    a = float(row['a'])
    data.append((P, V, a))
data.sort(key=lambda x: x[0])
P = np.array([d[0] for d in data])
V = np.array([d[1] for d in data])
a = np.array([d[2] for d in data])

# 1. Quadratic fit: a(P) = a0 - ka*a0*P + ka'*a0*P^2
def poly_a(P, a0, ka, kap):
    return a0 - ka*a0*P + kap*a0*P**2
p0_a = [a[0], 1.2e-3, 4e-6]
popt_a, pcov_a = curve_fit(poly_a, P, a, p0=p0_a, maxfev=10000)
a0_fit, ka_fit, kap_fit = popt_a
perr_a = np.sqrt(np.diag(pcov_a))
a0_err, ka_err, kap_err = perr_a
k_V = 3.0 * ka_fit

# 2. Third-order Birch-Murnaghan EOS: P(V)
def bm3(V, V0, KT, KTp):
    fE = 0.5 * ((V0/V)**(2./3.) - 1.0)
    return 3*KT * fE * (1 + 2*fE)**2.5 * (1 + 1.5*(KTp - 4)*fE)

# Unconstrained fit
p0_bm = [V[0], 250.0, 4.0]
bounds = ([0.7*V[0], 50, 0], [1.3*V[0], 500, 10])
popt_bm, pcov_bm = curve_fit(bm3, V, P, p0=p0_bm, bounds=bounds, maxfev=50000)
V0_fit, KT_fit, KTp_fit = popt_bm
perr_bm = np.sqrt(np.diag(pcov_bm))
V0_err_fit, KT_err_fit, KTp_err_fit = perr_bm

# 3. Fixed K_T' = 4
def bm3_fixed4(V, V0, KT):
    return bm3(V, V0, KT, 4.0)
p0_f4 = [V[0], 250.0]
bounds_f4 = ([0.7*V[0], 50], [1.3*V[0], 500])
popt_f4, pcov_f4 = curve_fit(bm3_fixed4, V, P, p0=p0_f4, bounds=bounds_f4, maxfev=50000)
V0_f4, KT_f4 = popt_f4
perr_f4 = np.sqrt(np.diag(pcov_f4))
_ , KT_err_f4 = perr_f4   # ignore V0 error for fixed K_T'=4 case

# Write JSON
res = {
    "V0": float(V0_fit),
    "V0_error": float(V0_err_fit),
    "KT": float(KT_fit),
    "KT_error": float(KT_err_fit),
    "KT_prime": float(KTp_fit),
    "KT_prime_error": float(KTp_err_fit),
    "KT_fixed4": float(KT_f4),
    "KT_fixed4_error": float(KT_err_f4),
    "ka": float(ka_fit),
    "ka_error": float(ka_err),
    "ka_prime": float(kap_fit),
    "ka_prime_error": float(kap_err),
    "k_V": float(k_V)
}
with open("/app/outputs/eos_fit_results.json", "w") as f:
    json.dump(res, f, indent=2)
print("Written eos_fit_results.json")
PYEOF
