import csv
import json
import math
import sys

# ----------------------------------------------------------------------
# 1.  Element data  (Table 1 of the paper, plus Pd and Os for alloys)
#     Columns: symbol, IP (eV), EA (eV), chi_paper (eV), Tc (K or empty)
#     For Pd and Os we only need IP,EA to compute general‐chi; Tc not needed here.
# ----------------------------------------------------------------------
ELEMENTS = [
    # symbol, IP, EA, chi, Tc
    ('Cs', 3.90, 0.472, 2.19, ''),
    ('Rb', 4.18, 0.486, 2.33, ''),
    ('K',  4.34, 0.502, 2.42, ''),
    ('Na', 5.14, 0.548, 2.84, ''),
    ('Li', 5.40, 0.618, 3.01, ''),
    ('In', 5.79, 0.3,   3.05, '3.408'),
    ('Ga', 6.00, 0.3,   3.15, '1.038'),
    ('Tl', 6.11, 0.2,   3.16, '2.38'),
    ('Al', 5.99, 0.441, 3.22, '1.75'),
    ('Sc', 6.54, 0.188, 3.36, ''),
    ('Hf', 6.78, 0,     3.39, '0.128'),
    ('Zr', 6.84, 0.426, 3.63, '0.65'),
    ('V',  6.74, 0.525, 3.63, '5.40'),
    ('Cr', 6.77, 0.666, 3.72, ''),
    ('W',  6.90, 0.815, 3.86, '0.0154'),
    ('Pb', 7.42, 0.364, 3.89, '7.196'),
    ('Nb', 6.89, 0.893, 3.89, '9.25'),
    ('Tc', 7.28, 0.55,  3.91, '7.8'),
    ('Mo', 7.10, 0.746, 3.92, '0.915'),
    ('Re', 7.89, 0.15,  4.02, '1.697'),
    ('Fe', 7.87, 0.163, 4.02, ''),
    ('Ta', 7.89, 0.322, 4.11, '4.47'),
    ('Ti', 6.82, 0.079, 4.11, '0.40'),
    ('Bi', 7.29, 0.946, 4.12, ''),
    ('Ru', 7.37, 1.05,  4.21, '0.49'),
    ('Co', 7.86, 0.661, 4.26, ''),
    ('Sn', 7.35, 1.2,   4.28, '3.722'),
    ('B',  8.30, 0.277, 4.29, ''),
    ('Rh', 7.46, 1.14,  4.30, ''),
    ('Ni', 7.64, 1.16,  4.40, ''),
    ('Ag', 7.58, 1.30,  4.44, ''),
    ('Ge', 7.90, 1.2,   4.46, ''),
    ('Cu', 7.73, 1.23,  4.48, ''),
    ('Si', 8.16, 1.39,  4.77, ''),
    ('Sb', 8.62, 1.07,  4.85, ''),
    ('As', 9.79, 0.81,  5.30, ''),
    ('Ir', 9.12, 1.57,  5.34, '0.1125'),
    ('Te', 9.01, 1.97,  5.49, ''),
    ('Pt', 9.02, 2.13,  5.57, ''),
    ('P',  10.5, 0.747, 5.62, ''),
    ('Au', 9.23, 2.31,  5.77, ''),
    ('Se', 9.76, 2.02,  5.89, ''),
    ('C',  11.3, 1.263, 6.36, ''),
    ('H',  13.6, 0.754, 7.18, ''),
    ('N',  14.5, -0.07, 7.23, ''),
    ('O',  13.6, 1.46,  7.54, ''),
    # additional elements needed for alloys (Os, Pd) – not in Table 1
    ('Pd', 8.3369, 0.56, 4.44845, ''),   # computed chi = 0.5*(8.3369+0.56) = 4.44845
    ('Os', 8.4382, 1.046, 4.7421, ''),    # chi = 0.5*(8.4382+1.046) = 4.7421
]

# Build dictionaries for fast lookup
IP_EA = {}   # symbol -> (IP, EA)
CHI_TABLE = {}   # symbol -> chi_paper (the one printed in Table 1)
TC_ELEMENT = {}   # symbol -> Tc as float or None

for sym, ip, ea, chi, tc in ELEMENTS:
    IP_EA[sym] = (ip, ea)
    CHI_TABLE[sym] = chi
    TC_ELEMENT[sym] = float(tc) if tc else None

# ----------------------------------------------------------------------
# 2.  Alloy data  (Table 2, 51 alloys)
#     alloy, Tc (K), chi_eq_low (from paper), (elem1, elem2)
# ----------------------------------------------------------------------
ALLOYS = [
    ('NbN',   16.10, 3.89, ('Nb', 'N')),
    ('NbC',   14,    4.08, ('Nb', 'C')),
    ('MoN',   12,    3.92, ('Mo', 'N')),
    ('TaN',   12,    4.11, ('Ta', 'N')),
    ('MoRu',  10.5,  4.08, ('Mo', 'Ru')),
    ('ZrN',   9.8,   3.63, ('Zr', 'N')),
    ('MoC',   9.26,  4.18, ('Mo', 'C')),
    ('NbB',   8.25,  3.89, ('Nb', 'B')),
    ('NbIr',  7.9,   4.23, ('Nb', 'Ir')),
    ('PbP',   7.8,   4.08, ('Pb', 'P')),
    ('RuW',   7.5,   3.98, ('Ru', 'W')),
    ('PbLi',  7.2,   3.01, ('Pb', 'Li')),
    ('PbIn',  6.65,  3.08, ('Pb', 'In')),
    ('PbSb',  6.6,   4.25, ('Pb', 'Sb')),
    ('GaSb',  5.9,   3.54, ('Ga', 'Sb')),
    ('PbTe',  5.19,  4.70, ('Pb', 'Te')),
    ('IrGe',  4.7,   4.73, ('Ir', 'Ge')),
    ('NiBi',  4.25,  4.22, ('Ni', 'Bi')),
    ('SnAs',  4.10,  4.28, ('Sn', 'As')),
    ('TaB',   4.0,   4.11, ('Ta', 'B')),
    ('SnBi',  3.8,   4.25, ('Sn', 'Bi')),
    ('PdBi',  3.7,   4.12, ('Pd', 'Bi')),
    ('WRh',   3.4,   4.02, ('W', 'Rh')),
    ('ZrB',   3.4,   3.53, ('Zr', 'B')),
    ('HfB',   3.1,   4.48, ('Hf', 'B')),
    ('ZrPt',  3.0,   4.48, ('Zr', 'Pt')),
    ('BiLi',  2.47,  3.17, ('Bi', 'Li')),
    ('BiNa',  2.25,  3.04, ('Bi', 'Na')),
    ('InSb',  2.1,   3.43, ('In', 'Sb')),
    ('RhBi',  2.06,  4.21, ('Rh', 'Bi')),
    ('MoRh',  1.97,  4.12, ('Mo', 'Rh')),
    ('TaOs',  1.95,  4.50, ('Ta', 'Os')),
    ('TlAu',  1.92,  4.21, ('Tl', 'Au')),
    ('GaPt',  1.74,  4.06, ('Ga', 'Pt')),
    ('PdSb',  1.42,  4.71, ('Pd', 'Sb')),
    ('SnSb',  1.42,  4.28, ('Sn', 'Sb')),
    ('CuBi',  1.40,  4.26, ('Cu', 'Bi')),
    ('SnAu',  1.25,  4.83, ('Sn', 'Au')),
    ('NbO',   1.25,  4.18, ('Nb', 'O')),
    ('RhP',   1.22,  4.30, ('Rh', 'P')),
    ('GaAu',  1.2,   4.15, ('Ga', 'Au')),
    ('RuTi',  1.07,  3.94, ('Ru', 'Ti')),
    ('WC',    1.0,   4.08, ('W', 'C')),
    ('TiCo',  0.71,  3.74, ('Ti', 'Co')),
    ('InPd',  0.7,   3.17, ('In', 'Pd')),
    ('InAu',  0.6,   4.05, ('In', 'Au')),
    ('TiO',   0.58,  4.14, ('Ti', 'O')),
    ('RhAs',  0.58,  4.30, ('Rh', 'As')),
    ('MoB',   0.5,   3.92, ('Mo', 'B')),
    ('BiCo',  0.49,  4.12, ('Bi', 'Co')),
    ('SnPd',  0.41,  4.28, ('Sn', 'Pd')),
]

# ----------------------------------------------------------------------
# 3.  Compute general‐formula equilibrium electronegativity (eqn 8b)
#     χ_eq_general = (η_B * χ_A + η_A * χ_B) / (η_A + η_B)
#     where η = IP − EA,  χ = (IP+EA)/2
# ----------------------------------------------------------------------
def chi_general(elem1, elem2):
    ip1, ea1 = IP_EA[elem1]
    ip2, ea2 = IP_EA[elem2]
    chi1 = 0.5 * (ip1 + ea1)
    chi2 = 0.5 * (ip2 + ea2)
    eta1 = ip1 - ea1
    eta2 = ip2 - ea2
    return (eta2 * chi1 + eta1 * chi2) / (eta1 + eta2)

# ----------------------------------------------------------------------
# 4.  Write the three output artifacts
# ----------------------------------------------------------------------
def write_elements():
    with open('/app/outputs/element_electronegativity.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['element', 'Tc', 'IP', 'EA', 'chi'])
        for sym, ip, ea, chi, tc in ELEMENTS:
            # only output elements that appear in Table 1 (skip Pd, Os)
            if sym in ('Pd', 'Os'):
                continue
            w.writerow([sym, tc, ip, ea, chi])

def write_alloys():
    with open('/app/outputs/alloy_equilibrium_electronegativity.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['alloy', 'Tc', 'chi_eq_low', 'chi_eq_general'])
        for alloy, tc, chi_low, (e1, e2) in ALLOYS:
            chi_gen = chi_general(e1, e2)
            w.writerow([alloy, tc, chi_low, f'{chi_gen:.4f}'])

def weighted_average(nums):
    """nums is list of (value, weight)"""
    total_w = sum(w for v, w in nums)
    if total_w == 0:
        return 0.0
    return sum(v * w for v, w in nums) / total_w

def write_averages():
    # Tc‑weighted average for superconducting metals (those with Tc in Table 1)
    metal_pairs = []
    for sym, _, _, chi, tc in ELEMENTS:
        if sym in ('Pd', 'Os'):
            continue
        tc_val = TC_ELEMENT[sym]
        if tc_val is not None:
            metal_pairs.append((chi, tc_val))
    metals_avg = weighted_average(metal_pairs)

    # Tc‑weighted averages for alloys (low‑T and general)
    low_pairs = []
    gen_pairs = []
    for alloy, tc, chi_low, (e1, e2) in ALLOYS:
        chi_gen = chi_general(e1, e2)
        low_pairs.append((chi_low, tc))
        gen_pairs.append((chi_gen, tc))
    alloys_low_avg = weighted_average(low_pairs)
    alloys_gen_avg = weighted_average(gen_pairs)

    result = {
        'metals_weighted_avg': round(metals_avg, 2),
        'alloys_weighted_avg_low': round(alloys_low_avg, 2),
        'alloys_weighted_avg_general': round(alloys_gen_avg, 2)
    }
    with open('/app/outputs/weighted_averages.json', 'w') as f:
        json.dump(result, f, indent=2)

if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'elements':
        write_elements()
    elif cmd == 'alloys':
        write_alloys()
    elif cmd == 'averages':
        write_averages()
    else:
        print('Usage: compute.py elements|alloys|averages', file=sys.stderr)
        sys.exit(1)
