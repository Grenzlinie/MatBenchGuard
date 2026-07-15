#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_partial_pressures_vs_T.csv ===
python3 << 'PYEOF'
import csv, math

# Gas constant J/(mol·K)
R = 8.314462618

# Shomate coefficients and standard formation data (JANAF, NIST Chemistry WebBook)
# delta_Hf (kJ/mol), A,B,C,D,E (J/mol·K), F,G,H (kJ/mol)
# NOTE: G is in J/(mol·K), H is formation enthalpy at 298 K
species = {
    'SiO2(cr)':  {'delta_Hf': -909.48, 'A': 64.973,  'B': -11.198, 'C': -37.360, 'D':17.089,  'E':-0.196, 'F':-916.265, 'G':64.801, 'H':-909.48},
    'Si(l)':     {'delta_Hf': 50.2,    'A': 27.136,  'B': 0.0,      'C': 0.0,     'D':0.0,     'E':0.0,    'F':-4.523,   'G':33.023, 'H':50.2},
    'O2':        {'delta_Hf': 0.0,     'A': 31.32234,'B':-20.23531, 'C':57.86644, 'D':-36.50624,'E':-0.007374,'F':-9.59575, 'G':246.794,'H':0.0},
    'SiO':       {'delta_Hf': -100.0,  'A': 37.071,  'B': -5.449,   'C': -3.723,  'D':3.601,   'E':0.017,   'F':-107.48,  'G':229.27, 'H':-100.0},
    'Si3N4':     {'delta_Hf': -743.5,  'A': 76.661,  'B': 45.764,   'C':-57.529,  'D':18.163,  'E':0.0,     'F':-791.640, 'G':113.344,'H':-743.5},
    'Al2O3':     {'delta_Hf': -1675.694,'A': 104.927, 'B': 11.987,   'C':-37.229,  'D':7.221,   'E':-0.882,  'F':-1711.882,'G':64.781, 'H':-1675.694},
    'AlN':       {'delta_Hf': -317.984,'A': 44.620,  'B': 13.444,   'C':-10.465,  'D':3.036,   'E':-0.218,  'F':-326.095, 'G':34.213, 'H':-317.984},
    'Al2O':      {'delta_Hf': -130.0,  'A': 59.307,  'B': 1.275,    'C': -1.063,  'D':0.301,   'E':-0.091,  'F':-136.606, 'G':284.004,'H':-130.0},
    'N2':        {'delta_Hf': 0.0,     'A': 28.98641,'B': 1.853978,'C': -9.647459,'D':16.63537,'E':0.000117,'F':-8.671914,'G':226.4168,'H':0.0},
}

def safe_exp(x):
    """Safe exponential to avoid OverflowError."""
    if x > 700:
        return float('inf')
    if x < -700:
        return 0.0
    return math.exp(x)

def gibbs(spec, T):
    """Gibbs free energy (kJ/mol) relative to elements at 298.15 K"""
    d = species[spec]
    t = T / 1000.0
    # Enthalpy increment H(T)-H(298.15) in kJ/mol
    H_diff = (d['A']*t + d['B']*t*t/2.0 + d['C']*t*t*t/3.0 + d['D']*t*t*t*t/4.0 - d['E']/t) / 1000.0 + (d['F'] - d['H'])
    # Entropy in J/(mol·K)  -- G is already in J/(mol·K), do NOT multiply by 1000
    S = (d['A']*math.log(t) + d['B']*t + d['C']*t*t/2.0 + d['D']*t*t*t/3.0 - d['E']/(2.0*t*t)) + d['G']
    # Gibbs free energy increment G(T)-H(298.15) = H_diff - T*S/1000
    G_rel = H_diff - T * S / 1000.0
    # Absolute G = Hf(298) + G_rel
    return d['delta_Hf'] + G_rel

# Reactions stoichiometry: (id, list of (species, coeff) for reactants, list for products, gas_only list for products, N2 coefficient in products)
reactions = [
    (1, [('SiO2(cr)', 1)], [('Si(l)', 1), ('O2', 1)], [('O2', 1)], 0),
    (2, [('SiO2(cr)', 1)], [('SiO', 1), ('O2', 0.5)], [('SiO', 1), ('O2', 0.5)], 0),
    (3, [('Si3N4', 1), ('SiO2(cr)', 1)], [('SiO', 2), ('Si(l)', 2), ('N2', 2)], [('SiO', 2), ('N2', 2)], 2),
    (4, [('Si3N4', 1), ('Al2O3', 1)], [('SiO', 3), ('AlN', 2), ('N2', 1)], [('SiO', 3), ('N2', 1)], 1),
    (5, [('Si3N4', 1), ('SiO2(cr)', 3)], [('SiO', 6), ('N2', 2)], [('SiO', 6), ('N2', 2)], 2),
    (6, [('AlN', 2), ('SiO2(cr)', 1)], [('SiO', 1), ('Al2O', 1), ('N2', 1)], [('SiO', 1), ('Al2O', 1), ('N2', 1)], 1),
]

def compute_K(rid, T):
    """Return ΔG (kJ/mol) and K for the reaction"""
    reac, prod, _, _ = reactions[rid-1][1:5]
    dG = sum(coeff * gibbs(s, T) for s, coeff in prod) - sum(coeff * gibbs(s, T) for s, coeff in reac)
    K = safe_exp(-dG * 1000.0 / (R * T))
    return dG, K

# Step 1: T vs partial pressures at P_N2 = 101.3 kPa = 1.01325 bar
P_N2_fixed = 1.01325  # bar
temps = range(1400, 2100, 100)  # 1400..2000

rows1 = []
for T in temps:
    for rid, reac, prod, gases, n2_coeff in reactions:
        dG, K = compute_K(rid, T)
        if rid in (1, 2):  # no N2 background
            if rid == 1:
                # SiO2 = Si(l) + O2   K = P_O2
                p_O2 = K
                rows1.append((rid, T, 'O2', p_O2, math.log10(p_O2) if p_O2 > 0 else -99))
            elif rid == 2:
                # SiO2 = SiO + 0.5 O2   K = P_SiO * sqrt(P_O2)  with P_O2 = 0.5 P_SiO
                # => P_SiO^1.5 * sqrt(0.5) = K  => P_SiO = (K^2 * 2)^(1/3)
                if K > 0:
                    p_SiO = (K**2 * 2) ** (1.0/3.0)
                    p_O2 = 0.5 * p_SiO
                    rows1.append((rid, T, 'SiO', p_SiO, math.log10(p_SiO)))
                    rows1.append((rid, T, 'O2', p_O2, math.log10(p_O2)))
                else:
                    rows1.append((rid, T, 'SiO', 0.0, -99))
                    rows1.append((rid, T, 'O2', 0.0, -99))
        else:  # N2 background
            # For these, P_N2 is fixed to P_N2_fixed
            if rid == 3:
                # K = P_SiO^2 * P_N2^2   => P_SiO = sqrt(K) / P_N2
                p_SiO = math.sqrt(K) / P_N2_fixed if K > 0 else 0.0
                rows1.append((rid, T, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
                rows1.append((rid, T, 'N2', P_N2_fixed, math.log10(P_N2_fixed)))
            elif rid == 4:
                # K = P_N2 * P_SiO^3   => P_SiO = (K / P_N2_fixed)^(1/3)
                if K > 0:
                    p_SiO = (K / P_N2_fixed) ** (1.0/3.0)
                else:
                    p_SiO = 0.0
                rows1.append((rid, T, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
                rows1.append((rid, T, 'N2', P_N2_fixed, math.log10(P_N2_fixed)))
            elif rid == 5:
                # K = P_SiO^6 * P_N2^2   => P_SiO = K^(1/6) / P_N2^(1/3)
                if K > 0:
                    p_SiO = K ** (1.0/6.0) / (P_N2_fixed ** (1.0/3.0))
                else:
                    p_SiO = 0.0
                rows1.append((rid, T, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
                rows1.append((rid, T, 'N2', P_N2_fixed, math.log10(P_N2_fixed)))
            elif rid == 6:
                # K = P_N2 * P_SiO * P_Al2O   and P_SiO = P_Al2O (1:1)
                # => P_SiO = sqrt(K / P_N2)
                if K > 0:
                    p_SiO = math.sqrt(K / P_N2_fixed)
                    p_Al2O = p_SiO
                else:
                    p_SiO = p_Al2O = 0.0
                rows1.append((rid, T, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
                rows1.append((rid, T, 'Al2O', p_Al2O, math.log10(p_Al2O) if p_Al2O > 0 else -99))
                rows1.append((rid, T, 'N2', P_N2_fixed, math.log10(P_N2_fixed)))

# Write step_01 CSV
with open('/app/outputs/step_01_partial_pressures_vs_T.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reaction_id', 'temperature_K', 'formula', 'partial_pressure_bar', 'log10_partial_pressure'])
    for row in rows1:
        w.writerow(row)

PYEOF

# === solve block: step_02_partial_pressures_vs_PN2.csv ===
python3 << 'PYEOF'
import csv, math

R = 8.314462618

species = {
    'SiO2(cr)':  {'delta_Hf': -909.48, 'A': 64.973,  'B': -11.198, 'C': -37.360, 'D':17.089,  'E':-0.196, 'F':-916.265, 'G':64.801, 'H':-909.48},
    'Si(l)':     {'delta_Hf': 50.2,    'A': 27.136,  'B': 0.0,      'C': 0.0,     'D':0.0,     'E':0.0,    'F':-4.523,   'G':33.023, 'H':50.2},
    'O2':        {'delta_Hf': 0.0,     'A': 31.32234,'B':-20.23531, 'C':57.86644, 'D':-36.50624,'E':-0.007374,'F':-9.59575, 'G':246.794,'H':0.0},
    'SiO':       {'delta_Hf': -100.0,  'A': 37.071,  'B': -5.449,   'C': -3.723,  'D':3.601,   'E':0.017,   'F':-107.48,  'G':229.27, 'H':-100.0},
    'Si3N4':     {'delta_Hf': -743.5,  'A': 76.661,  'B': 45.764,   'C':-57.529,  'D':18.163,  'E':0.0,     'F':-791.640, 'G':113.344,'H':-743.5},
    'Al2O3':     {'delta_Hf': -1675.694,'A': 104.927, 'B': 11.987,   'C':-37.229,  'D':7.221,   'E':-0.882,  'F':-1711.882,'G':64.781, 'H':-1675.694},
    'AlN':       {'delta_Hf': -317.984,'A': 44.620,  'B': 13.444,   'C':-10.465,  'D':3.036,   'E':-0.218,  'F':-326.095, 'G':34.213, 'H':-317.984},
    'Al2O':      {'delta_Hf': -130.0,  'A': 59.307,  'B': 1.275,    'C': -1.063,  'D':0.301,   'E':-0.091,  'F':-136.606, 'G':284.004,'H':-130.0},
    'N2':        {'delta_Hf': 0.0,     'A': 28.98641,'B': 1.853978,'C': -9.647459,'D':16.63537,'E':0.000117,'F':-8.671914,'G':226.4168,'H':0.0},
}

def safe_exp(x):
    """Safe exponential to avoid OverflowError."""
    if x > 700:
        return float('inf')
    if x < -700:
        return 0.0
    return math.exp(x)

def gibbs(spec, T):
    d = species[spec]
    t = T / 1000.0
    H_diff = (d['A']*t + d['B']*t*t/2.0 + d['C']*t*t*t/3.0 + d['D']*t*t*t*t/4.0 - d['E']/t) / 1000.0 + (d['F'] - d['H'])
    S = (d['A']*math.log(t) + d['B']*t + d['C']*t*t/2.0 + d['D']*t*t*t/3.0 - d['E']/(2.0*t*t)) + d['G']*1000.0
    G_rel = H_diff - T * S / 1000.0
    return d['delta_Hf'] + G_rel

reactions_34_56 = [
    (3, [('Si3N4', 1), ('SiO2(cr)', 1)], [('SiO', 2), ('Si(l)', 2), ('N2', 2)], [('SiO', 2), ('N2', 2)], 2),
    (4, [('Si3N4', 1), ('Al2O3', 1)], [('SiO', 3), ('AlN', 2), ('N2', 1)], [('SiO', 3), ('N2', 1)], 1),
    (5, [('Si3N4', 1), ('SiO2(cr)', 3)], [('SiO', 6), ('N2', 2)], [('SiO', 6), ('N2', 2)], 2),
    (6, [('AlN', 2), ('SiO2(cr)', 1)], [('SiO', 1), ('Al2O', 1), ('N2', 1)], [('SiO', 1), ('Al2O', 1), ('N2', 1)], 1),
]

def compute_K(rid, reac, prod, T):
    dG = sum(coeff * gibbs(s, T) for s, coeff in prod) - sum(coeff * gibbs(s, T) for s, coeff in reac)
    K = safe_exp(-dG * 1000.0 / (R * T))
    return K

T_fixed = 2000.0
N2_pressures_MPa = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]

rows2 = []
for rid, reac, prod, gases, n2_coeff in reactions_34_56:
    K = compute_K(rid, reac, prod, T_fixed)
    for PN2_MPa in N2_pressures_MPa:
        P_N2_bar = PN2_MPa * 10.0
        if rid == 3:
            p_SiO = math.sqrt(K) / P_N2_bar if K > 0 else 0.0
            rows2.append((rid, PN2_MPa, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
            rows2.append((rid, PN2_MPa, 'N2', P_N2_bar, math.log10(P_N2_bar)))
        elif rid == 4:
            if K > 0:
                p_SiO = (K / P_N2_bar) ** (1.0/3.0)
            else:
                p_SiO = 0.0
            rows2.append((rid, PN2_MPa, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
            rows2.append((rid, PN2_MPa, 'N2', P_N2_bar, math.log10(P_N2_bar)))
        elif rid == 5:
            if K > 0:
                p_SiO = K ** (1.0/6.0) / (P_N2_bar ** (1.0/3.0))
            else:
                p_SiO = 0.0
            rows2.append((rid, PN2_MPa, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
            rows2.append((rid, PN2_MPa, 'N2', P_N2_bar, math.log10(P_N2_bar)))
        elif rid == 6:
            if K > 0:
                p_SiO = math.sqrt(K / P_N2_bar)
                p_Al2O = p_SiO
            else:
                p_SiO = p_Al2O = 0.0
            rows2.append((rid, PN2_MPa, 'SiO', p_SiO, math.log10(p_SiO) if p_SiO > 0 else -99))
            rows2.append((rid, PN2_MPa, 'Al2O', p_Al2O, math.log10(p_Al2O) if p_Al2O > 0 else -99))
            rows2.append((rid, PN2_MPa, 'N2', P_N2_bar, math.log10(P_N2_bar)))

with open('/app/outputs/step_02_partial_pressures_vs_PN2.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['reaction_id', 'N2_pressure_MPa', 'formula', 'partial_pressure_bar', 'log10_partial_pressure'])
    for row in rows2:
        w.writerow(row)

PYEOF
