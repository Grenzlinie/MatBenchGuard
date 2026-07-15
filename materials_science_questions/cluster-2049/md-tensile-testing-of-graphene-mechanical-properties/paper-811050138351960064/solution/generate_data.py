#!/usr/bin/env python3
"""Generate synthetic stress–strain curves for the hidden oracle.
The shapes and approximate values match the paper's descriptions:
  graphene tensile (armchair): 0–15% strain, virgin = ~1 TPa modulus,
    5 defects fails at strain ~0.085, 10 defects fails at ~0.10.
  composite longitudinal shear: 0 defects plateaus low (~5 MPa),
    5 defects rises to ~20 MPa, 10 defects rises to ~30 MPa.
"""
import sys, math, csv

STRAIN_END = 0.15
SHEAR_END = 0.16

def gen_graphene():
    n = 31
    strains = [i * STRAIN_END / (n-1) for i in range(n)]
    # pristine: linear 1000 GPa, no failure in this range
    s0 = [1000.0 * e for e in strains]
    # 5 defects: modulus ~800 GPa, fail at 0.085, then drop to 0
    fail_5 = 0.085
    s5 = []
    for e in strains:
        if e <= fail_5:
            s5.append(800.0 * e)
        else:
            s5.append(0.0)
    # 10 defects: modulus ~700 GPa, fail at 0.10
    fail_10 = 0.10
    s10 = []
    for e in strains:
        if e <= fail_10:
            s10.append(700.0 * e)
        else:
            s10.append(0.0)
    return strains, s0, s5, s10

def gen_shear():
    n = 33
    strains = [i * SHEAR_END / (n-1) for i in range(n)]
    # 0 defects: nearly flat plateau around 5 MPa after small rise
    s0 = [min(5.0 * math.tanh(40.0 * e), 5.0) for e in strains]
    # 5 defects: plateau ~20 MPa
    s5 = [min(20.0 * math.tanh(50.0 * e), 20.0) for e in strains]
    # 10 defects: plateau ~30 MPa
    s10 = [min(30.0 * math.tanh(60.0 * e), 30.0) for e in strains]
    return strains, s0, s5, s10

mode = sys.argv[1]
if mode == "graphene":
    strains, s0, s5, s10 = gen_graphene()
    writer = csv.writer(sys.stdout)
    writer.writerow(["strain", "stress_0defects", "stress_5defects", "stress_10defects"])
    for i in range(len(strains)):
        writer.writerow([f"{strains[i]:.6f}", f"{s0[i]:.4f}", f"{s5[i]:.4f}", f"{s10[i]:.4f}"])
elif mode == "shear":
    strains, s0, s5, s10 = gen_shear()
    writer = csv.writer(sys.stdout)
    writer.writerow(["shear_strain", "stress_0defects", "stress_5defects", "stress_10defects"])
    for i in range(len(strains)):
        writer.writerow([f"{strains[i]:.6f}", f"{s0[i]:.4f}", f"{s5[i]:.4f}", f"{s10[i]:.4f}"])
else:
    raise SystemExit("unknown mode")
