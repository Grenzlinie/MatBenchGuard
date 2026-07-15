#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple scipy numpy

# === solve block: verification_results.json ===
mkdir -p /app/outputs
python3 << 'PYEOF'
import json, math
import scipy.integrate as integrate

R = 8.31446261815324
h = 6.62607015e-34
k = 1.380649e-23
pi = math.pi

def debye_d(x):
    if x <= 0.0:
        return 1.0
    val, _ = integrate.quad(lambda y: y**3 / (math.exp(y) - 1.0), 0.0, x)
    return 3.0 / (x**3) * val

def cv(mu, L, T, Td):
    x = Td * (1.0 + L) / T
    d = debye_d(x)
    a = 4.0*d - 3.0*x/(math.exp(x) - 1.0)
    b = 1.0 - (L/(4.0*(L + 1.0)))*(3.0 - L/(L + 1.0))
    return (3.0*R/mu) * a * b

def sgen(mu, L, T, Td):
    x = Td * (1.0 + L) / T
    d = debye_d(x)
    fac = 1.0 - (3.0*L)/(8.0*(L + 1.0))
    return (R/mu) * (4.0*d*fac - 3.0*math.log(1.0 - math.exp(-x)))

def sig(mu, T, v, m_atom, ga):
    arg = h**3 / ((2.0*pi*m_atom*k*T)**1.5 * ga * m_atom * v)
    return (R/mu) * (2.5 - math.log(arg))

mu = 1.0
T_high = 1000.0
Td_small = 0.1

# solid limit
L_solid = 0.001
solid_Cv = cv(mu, L_solid, T_high, Td_small)
expected_solid = 3.0*R/mu
re_solid = abs(solid_Cv - expected_solid) / expected_solid

# gas limit
L_gas = 100.0
gas_Cv = cv(mu, L_gas, T_high, Td_small)
expected_gas = 1.5*R/mu
re_gas = abs(gas_Cv - expected_gas) / expected_gas

# entropy check – pick consistent parameters
v_val = 0.0821      # m³/mol
m_atom = 1.6605e-27 # kg
ga = 1.0
# compute Td so that L=100 satisfies the matching condition
Td_ent = (h / L_gas) * math.sqrt(T_high / (2.0*pi*m_atom*k)) * (ga*m_atom*v_val)**(-1.0/3.0)
s_comp = sgen(mu, L_gas, T_high, Td_ent)
s_ref = sig(mu, T_high, v_val, m_atom, ga)
re_s = abs(s_comp - s_ref) / s_ref

res = {
  "solid_limit": {
    "mu": mu,
    "L": L_solid,
    "T": T_high,
    "Theta_D": Td_small,
    "computed_Cv": round(solid_Cv, 6),
    "expected_Cv": round(expected_solid, 6),
    "relative_error": round(re_solid, 10)
  },
  "gas_limit": {
    "mu": mu,
    "L": L_gas,
    "T": T_high,
    "Theta_D": Td_small,
    "computed_Cv": round(gas_Cv, 6),
    "expected_Cv": round(expected_gas, 6),
    "relative_error": round(re_gas, 10)
  },
  "entropy_check": {
    "L": L_gas,
    "T": T_high,
    "v": v_val,
    "mu": mu,
    "m": m_atom,
    "g_a": ga,
    "computed_S": round(s_comp, 6),
    "ideal_gas_S": round(s_ref, 6),
    "relative_error": round(re_s, 10)
  }
}

with open('/app/outputs/verification_results.json', 'w') as f:
    json.dump(res, f, indent=2)
print("verification_results.json written")
PYEOF
