#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy

# === solve block: surface_energy.json ===
cat > /tmp/compute_surface.py << 'PYEOF'
import json, math, cmath, sys
import scipy.integrate as integrate

a_strs = ['0', '0.6i', '0.8i']
a_values = {}
for a_str in a_strs:
    a_val = complex(a_str.replace('i', 'j'))
    a_imag = a_val.imag
    prefac = (4 * a_val**2 - 1).real / 4.0
    a_values[a_str] = (a_imag, prefac)

def e_b_from_param(p, a_imag):
    p = abs(p)
    def integrand(k):
        # (1-e^{-k}) / (1+e^{-k}) * 2 * e^{-p k} * cos(a_imag*k)
        # factor of 2 from integral identity
        return 2.0 * (1.0 - math.exp(-k)) / (1.0 + math.exp(-k)) * math.exp(-p * k) * math.cos(a_imag * k)
    I, _ = integrate.quad(integrand, 0, math.inf, limit=200)
    return I

def e_b0(a_imag):
    def integrand(k):
        # (1-e^{-k}) * cos(a_imag*k) * 2*(e^{-k} - e^{-k/2})/(1+e^{-k})
        return 2.0 * (1.0 - math.exp(-k)) * (math.exp(-k) - math.exp(-k/2)) / (1.0 + math.exp(-k)) * math.cos(a_imag * k)
    I, _ = integrate.quad(integrand, 0, math.inf, limit=200)
    return I

tuples = [
    ('0', 0.1, 0.1, 0.5),
    ('0', 0.5, 0.5, 1.2),
    ('0.6i', 0.2, 0.3, 0.5),
    ('0.6i', 0.5, 0.5, 1.2),
    ('0.6i', 0.7, 0.7, 1.2),
    ('0.8i', 0.3, 0.4, 0.5),
    ('0.8i', 0.6, 0.6, 1.2),
    ('0.8i', 0.9, 0.9, 1.2),
]

records = []
for a_str, p, q, xi in tuples:
    a_imag, prefac = a_values[a_str]
    q_bar = q / math.sqrt(1.0 + xi * xi)
    ep = e_b_from_param(p, a_imag)
    eq = e_b_from_param(q_bar, a_imag)
    e0 = e_b0(a_imag)
    E_b = prefac * (ep + eq + e0)
    records.append({
        'a': a_str,
        'p': p,
        'q': q,
        'xi': xi,
        'E_b': E_b
    })

outpath = sys.argv[1]
with open(outpath, 'w') as f:
    json.dump(records, f, indent=2)
PYEOF
python3 /tmp/compute_surface.py "$OUTDIR/surface_energy.json"

# === solve block: bulk_excitation.json ===
python3 /solution/compute.py "$OUTDIR/bulk_excitation.json" bulk_excitation

# === solve block: boundary_excitation.json ===
python3 /solution/compute.py "$OUTDIR/boundary_excitation.json" boundary_excitation

# === solve block: ferromagnetic_surface.json ===
python3 /solution/compute.py "$OUTDIR/ferromagnetic_surface.json" ferromagnetic_surface
