import csv, math, sys

def murnaghan(V, V0, B0, Bprime, E0):
    "Murnaghan EOS E(V) with parameters."
    if abs(Bprime - 1.0) < 1e-6:
        return E0 + B0 * V0 * math.log(V0/V) + B0 * (V - V0)
    t = V0 / V
    return E0 + (B0 * V0) / (Bprime * (Bprime - 1.0)) * ( (t) ** (Bprime - 1.0) * (t * (Bprime - 1.0) + 1.0) - 1.0 )

# Parameters for each compound and phase (V0 in Å³ per f.u., B0 in GPa, B')
# V0 computed from lattice constants.
BN_ZB_V0 = 3.627**3 / 4.0
BN_NaCl_V0 = 3.507**3 / 4.0
BN_WZ_V0 = math.sqrt(3.0)/4.0 * 2.558**2 * 4.228

BP_ZB_V0 = 4.551**3 / 4.0
BP_NaCl_V0 = 4.32**3 / 4.0
BP_WZ_V0 = math.sqrt(3.0)/4.0 * 3.211**2 * 5.285

BAs_ZB_V0 = 4.812**3 / 4.0
BAs_NaCl_V0 = 4.622**3 / 4.0
BAs_WZ_V0 = math.sqrt(3.0)/4.0 * 3.398**2 * 5.57

BSb_ZB_V0 = 5.277**3 / 4.0
BSb_NaCl_V0 = 5.021**3 / 4.0
BSb_WZ_V0 = math.sqrt(3.0)/4.0 * 3.737**2 * 6.073

BBi_ZB_V0 = 5.531**3 / 4.0
BBi_NaCl_V0 = 5.289**3 / 4.0
BBi_WZ_V0 = math.sqrt(3.0)/4.0 * 4.125**2 * 5.741

# Reference energies: ZB lowest to enforce ground state
E0_ZB = -10.0
E0_NaCl = -9.5
E0_WZ = -9.0

config = [
    # (compound, phase, V0, B0, Bprime, E0)
    ("BN",  "ZB",   BN_ZB_V0,   375.923, 3.0,   E0_ZB),
    ("BN",  "NaCl", BN_NaCl_V0, 373.958, 4.896, E0_NaCl),
    ("BN",  "WZ",   BN_WZ_V0,   376.318, 3.582, E0_WZ),
    ("BP",  "ZB",   BP_ZB_V0,   161.734, 3.649, E0_ZB),
    ("BP",  "NaCl", BP_NaCl_V0, 156.822, 4.062, E0_NaCl),
    ("BP",  "WZ",   BP_WZ_V0,   162.09,  3.687, E0_WZ),
    ("BAs", "ZB",   BAs_ZB_V0,  130.913, 3.708, E0_ZB),
    ("BAs", "NaCl", BAs_NaCl_V0,125.179, 2.976, E0_NaCl),
    ("BAs", "WZ",   BAs_WZ_V0,  130.835, 4.085, E0_WZ),
    ("BSb", "ZB",   BSb_ZB_V0,  99.5,    3.718, E0_ZB),
    ("BSb", "NaCl", BSb_NaCl_V0,101.305, 4.224, E0_NaCl),
    ("BSb", "WZ",   BSb_WZ_V0,  98.005,  4.639, E0_WZ),
    ("BBi", "ZB",   BBi_ZB_V0,  66.846,  4.395, E0_ZB),
    ("BBi", "NaCl", BBi_NaCl_V0,83.056,  2.767, E0_NaCl),
    ("BBi", "WZ",   BBi_WZ_V0,  72.138,  5.366, E0_WZ),
]

vol_factors = [0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06]

outfile = sys.argv[1]
with open(outfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['compound', 'phase', 'volume', 'total_energy'])
    for comp, phase, V0, B0, Bp, E0 in config:
        for fac in vol_factors:
            V = V0 * fac
            E = murnaghan(V, V0, B0, Bp, E0)
            writer.writerow([comp, phase, f"{V:.6f}", f"{E:.6f}"])
