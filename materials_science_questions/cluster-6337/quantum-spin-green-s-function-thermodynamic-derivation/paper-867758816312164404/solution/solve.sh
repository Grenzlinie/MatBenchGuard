#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple sympy
mkdir -p /app/outputs

# === solve block: derivation_output.json ===
python3 -c "
import json, sympy as sp
beta, G, b, t, S = sp.symbols('beta G b t S', positive=True, real=True)
d = 2*S + 1
g = sp.sin(d*b*t) / (d * sp.sin(b*t))
I = (beta**2 * G**2) / (3 * sp.log(2)) * S*(S+1) * (1 - g**2)
C_half = (beta**2 * G**2 * sp.sin(b*t)**2) / (8 * sp.log(2))
D_half = C_half
n = sp.symbols('n', integer=True, nonnegative=True)
f_sum = sp.Sum(sp.binomial(2*S, n) * ((-1)**n) * (sp.sin(b*t)**(2*n)) * (sp.factorial2(2*n) / sp.factorial2(2*n+1)), (n, 0, 2*S))
J = (beta**2 * G**2) / (6 * sp.log(2)) * ( S*(S+1)*(f_sum - g**2) + S**2*(1 - g**2) )
Q = (beta**2 * G**2) / (6 * sp.log(2)) * ( S*(S+1)*(1 - f_sum) + S*(1 - g**2) )
quantum_frac = 1/(S+1)
exprs = {
    'mutual_information': sp.srepr(I),
    'classical_correlation_S_half': sp.srepr(C_half),
    'quantum_correlation_S_half': sp.srepr(D_half),
    'classical_correlation_S_general': sp.srepr(J),
    'quantum_correlation_S_general': sp.srepr(Q),
    'quantum_fraction': sp.srepr(quantum_frac)
}
with open('/app/outputs/derivation_output.json', 'w') as f:
    json.dump(exprs, f, indent=2)
"
