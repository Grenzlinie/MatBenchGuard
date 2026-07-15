#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: computed_thermodynamic_values.json ===
python3 - << 'PYEOF' > /app/outputs/computed_thermodynamic_values.json
import json, math

R_J = 8.314       # J/(mol K)
P_TT = 14.2
Q_P  = 9.4
P_TN = 12.3
R_OVER_P = 0.0    # neglected for simplicity

# --------------- elemental parameters (298 K) -------------------
# keys: phi [V], nws [arb.], Vm [cm^3/mol], G [GPa], K [GPa], Tm [K], M [g/mol], Z (valence)
els = {
    'Cu': {'phi':4.55, 'nws':1.47, 'Vm':7.11,  'G':48,  'K':140, 'Tm':1358, 'M':63.546,  'Z':1},
    'Cr': {'phi':4.65, 'nws':1.73, 'Vm':7.23,  'G':80,  'K':160, 'Tm':2180, 'M':51.996,  'Z':6},
    'Mo': {'phi':4.60, 'nws':1.77, 'Vm':9.40,  'G':120, 'K':230, 'Tm':2896, 'M':95.94,   'Z':6},
    'Ti': {'phi':3.80, 'nws':1.47, 'Vm':10.64, 'G':44,  'K':110, 'Tm':1941, 'M':47.867,  'Z':4},
    'Ta': {'phi':4.05, 'nws':1.63, 'Vm':10.90, 'G':69,  'K':200, 'Tm':3290, 'M':180.947, 'Z':5},
    'Sn': {'phi':4.15, 'nws':1.24, 'Vm':16.30, 'G':18.4,'K':58,  'Tm':505,  'M':118.71,  'Z':4},
    'Nb': {'phi':4.05, 'nws':1.62, 'Vm':10.80, 'G':38,  'K':170, 'Tm':2750, 'M':92.91,   'Z':5},
    'Co': {'phi':5.10, 'nws':1.75, 'Vm':6.67,  'G':76,  'K':180, 'Tm':1768, 'M':58.933,  'Z':9},
}

def is_transition(sym):
    return sym != 'Sn'

# --------------- chemical contribution (kJ/mol) ---------------
def chemical(xA, xB, eA, eB, M):
    Vm2_3A = eA['Vm'] ** (2/3)
    Vm2_3B = eB['Vm'] ** (2/3)
    nws_invA = eA['nws'] ** (-1/3)
    nws_invB = eB['nws'] ** (-1/3)
    # surface concentrations
    CAS = xA * Vm2_3A / (xA * Vm2_3A + xB * Vm2_3B)
    CBS = 1 - CAS
    f_CS = CAS * CBS
    # volume correction S(x)
    VA = eA['Vm']
    VB = eB['Vm']
    denom_S = xA**2 * VA + xB**2 * VB
    Sx = 1 - M * xA * xB * abs(VA - VB) / denom_S if denom_S != 0 else 1
    num = xA * Vm2_3A + xB * Vm2_3B
    denom_n = nws_invA + nws_invB
    dphi = eA['phi'] - eB['phi']
    dnws = eA['nws'] - eB['nws']
    bracket = - dphi**2 + Q_P * dnws**2 - R_OVER_P
    P_val = P_TT if (is_transition(eA) and is_transition(eB)) else P_TN
    return 2 * P_val * f_CS * Sx * num / denom_n * bracket

# --------------- elastic contribution (kJ/mol) ---------------
def elastic(xA, xB, eA, eB):
    VA = eA['Vm']
    VB = eB['Vm']
    KA = eA['K']
    GA = eA['G']
    KB = eB['K']
    GB = eB['G']
    # ΔE_A_in_B
    denom_AB = 3*KA*VB + 4*GB*VA
    dE_A_in_B = (2*KA*GB*(VB-VA)**2)/denom_AB if denom_AB != 0 else 0
    denom_BA = 3*KB*VA + 4*GA*VB
    dE_B_in_A = (2*KB*GA*(VA-VB)**2)/denom_BA if denom_BA != 0 else 0
    return xA * xB * (xA * dE_A_in_B + xB * dE_B_in_A)

def structural(xA, xB, eA, eB):
    return 0.0   # neglected

# ------------ binary mixing enthalpy (solid solution) ------------
def binary_mix(xA, xB, eA, eB, M=1):
    return chemical(xA, xB, eA, eB, M) + elastic(xA, xB, eA, eB) + structural(xA, xB, eA, eB)

# ----------- Hillert extrapolation for ternary -------------
def hillert(x1, x2, x3, e1, e2, e3, M, include_elastic=True):
    # binary enthalpy for A-B, A-C and B-C
    dH_AB = chemical(x1, 1-x1, e1, e2, M) + (elastic(x1, 1-x1, e1, e2) if include_elastic else 0)
    dH_AC = chemical(x1, 1-x1, e1, e3, M) + (elastic(x1, 1-x1, e1, e3) if include_elastic else 0)
    C_BC = (1 + x2 - x3) / 2
    C_CB = (1 + x3 - x2) / 2
    dH_BC = chemical(C_BC, C_CB, e2, e3, M) + (elastic(C_BC, C_CB, e2, e3) if include_elastic else 0)
    # Hillert formula (asymmetric with element 1 as the key)
    H = (x2/(1-x1)) * dH_AB + (x3/(1-x1)) * dH_AC + (x2*x3/(C_BC*C_CB)) * dH_BC
    return H

# ---------- configurational entropy (J/mol/K) ----------
def S_config(*xs):
    s = 0.0
    for x in xs:
        if x > 0:
            s -= x * math.log(x)
    return s * R_J

# ============= compute results ==============

# 1) Cu-7Cr-7Mo (at.%) solid solution @ 298 K
x_Cu1, x_Cr, x_Mo = 0.86, 0.07, 0.07
H_mix_1 = hillert(x_Cu1, x_Cr, x_Mo, els['Cu'], els['Cr'], els['Mo'], M=1, include_elastic=True)
T1 = 298
S1 = S_config(x_Cu1, x_Cr, x_Mo)
dGm_CuCrMo = H_mix_1 - T1 * S1 / 1000  # kJ/mol

# 2) Ti-13Ta-12Sn (at.%) @ 298 K -- solid solution + amorphous
x_Ti, x_Ta, x_Sn = 0.75, 0.13, 0.12
T2 = 298
# solid solution
H_mix_ss = hillert(x_Ti, x_Ta, x_Sn, els['Ti'], els['Ta'], els['Sn'], M=1, include_elastic=True)
S2 = S_config(x_Ti, x_Ta, x_Sn)
dGm_TiTaSn = H_mix_ss - T2 * S2 / 1000
# amorphous: chemical only (M=1) + topological term
H_chem_am = hillert(x_Ti, x_Ta, x_Sn, els['Ti'], els['Ta'], els['Sn'], M=1, include_elastic=False)
H_topo = 3.5 * (x_Ti*els['Ti']['Tm'] + x_Ta*els['Ta']['Tm'] + x_Sn*els['Sn']['Tm']) / 1000  # kJ/mol
H_am = H_chem_am + H_topo
dGam_TiTaSn = H_am - T2 * S2 / 1000

# 3) Cu-7Nb-7Co (at.%) @ 298 K -- solid solution + intermetallic ΔHf
x_Cu3, x_Nb, x_Co = 0.86, 0.07, 0.07
T3 = 298
H_mix_3 = hillert(x_Cu3, x_Nb, x_Co, els['Cu'], els['Nb'], els['Co'], M=1, include_elastic=True)
S3 = S_config(x_Cu3, x_Nb, x_Co)
dGm_CuNbCo = H_mix_3 - T3 * S3 / 1000
# intermetallic ΔHf: chemical only with M=2 (ordered)
Hf = hillert(x_Cu3, x_Nb, x_Co, els['Cu'], els['Nb'], els['Co'], M=2, include_elastic=False)

# 4) Cu-50Cr (wt%) convert to at%
M_Cu = els['Cu']['M']
M_Cr = els['Cr']['M']
# 50 wt% each: mass fractions w_Cu=w_Cr=0.5
w_Cu = 0.5
w_Cr = 0.5
# atoms per 100 g
mol_Cu = 50 / M_Cu
mol_Cr = 50 / M_Cr
tot = mol_Cu + mol_Cr
x_Cu_4 = mol_Cu / tot
x_Cr_4 = mol_Cr / tot
# compute mixing enthalpy (binary)
H_mix_4 = binary_mix(x_Cu_4, x_Cr_4, els['Cu'], els['Cr'], M=1)
S4 = S_config(x_Cu_4, x_Cr_4)
dGm_298 = H_mix_4 - 298 * S4 / 1000
dGm_503 = H_mix_4 - 503 * S4 / 1000
# centrifugal field parameters
rho_m = 0.15       # 150 mm
omega = 628        # rad/s
time_h = 4         # not used in energy calculation
# average atomic mass
M_avg_g = x_Cu_4 * M_Cu + x_Cr_4 * M_Cr   # g/mol
M_avg_kg = M_avg_g / 1000.0               # kg/mol
G_ef_J = 0.5 * M_avg_kg * rho_m**2 * omega**2   # J/mol
G_ef = G_ef_J / 1000.0                             # kJ/mol
# compute dGm at 453 K without field, then subtract
dGm_453_no = H_mix_4 - 453 * S4 / 1000
dGm_cf_453 = dGm_453_no - G_ef
dGm_cf_503 = dGm_503 - G_ef

# assemble JSON
result = {
    "Cu_7Cr_7Mo": {"dGm": round(dGm_CuCrMo, 6)},
    "Ti_13Ta_12Sn": {"dGm": round(dGm_TiTaSn, 6), "dGam": round(dGam_TiTaSn, 6)},
    "Cu_7Nb_7Co": {"dGm": round(dGm_CuNbCo, 6), "dHf": round(Hf, 6)},
    "Cu_50Cr": {
        "dGm_298K": round(dGm_298, 6),
        "dGm_503K": round(dGm_503, 6),
        "dGm_cf_453K": round(dGm_cf_453, 6),
        "dGm_cf_503K": round(dGm_cf_503, 6)
    }
}
print(json.dumps(result, indent=2))
PYEOF
