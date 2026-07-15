import math
import csv
import sys

R = 8.314

# material parameters: h (nm), Tm (K), DeltaS_vib (J/molK) for free
params = {
    "Fe": {"h": 0.2482, "Tm": 1811.00, "DSvib": 6.42},
    "β-Sn": {"h": 0.3181, "Tm": 505.08, "DSvib": 9.25},
    "Se": {"h": 0.4366, "Tm": 494.00, "DSvib": 10.93},
    "Cu": {"h": 0.2556, "Tm": 1357.77, "DSvib": 8.08},
    "Co": {"h": 0.2507, "Tm": 1768.00, "DSvib": 7.83},
    "Au": {"h": 0.2884, "Tm": 1337.33, "DSvib": 7.74},
    "Pb": {"h": 0.3500, "Tm": 600.61, "DSvib": 6.71},
    "Ar": {"h": 0.3650, "Tm": 83.80, "DSvib": None}  # not used
}

# embedded matrix parameters for Ar
h_M = 0.2863
T_M = 933.47

# Test cases: (material, dimension, size_nm, interface_type)
test_cases = [
    # Fe free d0 sizes 5,10,20,50 + d1, d2
    ("Fe", 0, 5.0, "free"),
    ("Fe", 0, 10.0, "free"),
    ("Fe", 0, 20.0, "free"),
    ("Fe", 0, 50.0, "free"),
    ("Fe", 1, 10.0, "free"),
    ("Fe", 1, 20.0, "free"),
    ("Fe", 1, 50.0, "free"),
    ("Fe", 2, 10.0, "free"),
    ("Fe", 2, 20.0, "free"),
    ("Fe", 2, 50.0, "free"),
    # β-Sn free d0
    ("β-Sn", 0, 10.0, "free"),
    ("β-Sn", 0, 20.0, "free"),
    ("β-Sn", 0, 50.0, "free"),
    # Se free d0
    ("Se", 0, 10.0, "free"),
    ("Se", 0, 20.0, "free"),
    ("Se", 0, 50.0, "free"),
    # Cu free d0 + d1, d2
    ("Cu", 0, 10.0, "free"),
    ("Cu", 0, 20.0, "free"),
    ("Cu", 0, 50.0, "free"),
    ("Cu", 1, 10.0, "free"),
    ("Cu", 1, 20.0, "free"),
    ("Cu", 1, 50.0, "free"),
    ("Cu", 2, 10.0, "free"),
    ("Cu", 2, 20.0, "free"),
    ("Cu", 2, 50.0, "free"),
    # Co free d0
    ("Co", 0, 10.0, "free"),
    ("Co", 0, 20.0, "free"),
    ("Co", 0, 50.0, "free"),
    # Au free d0
    ("Au", 0, 10.0, "free"),
    ("Au", 0, 20.0, "free"),
    ("Au", 0, 50.0, "free"),
    # Pb free d0
    ("Pb", 0, 10.0, "free"),
    ("Pb", 0, 20.0, "free"),
    ("Pb", 0, 50.0, "free"),
    # Ar embedded d0 sizes 5,10,20,50
    ("Ar", 0, 5.0, "embedded"),
    ("Ar", 0, 10.0, "embedded"),
    ("Ar", 0, 20.0, "embedded"),
    ("Ar", 0, 50.0, "embedded"),
]

def compute_D0(d, h):
    return 2 * (3 - d) * h

def compute_alpha_free(DSvib):
    return 2 * DSvib / (3 * R) + 1

def compute_alpha_embedded(h_material, Tm_material, h_M, T_M):
    return ((h_M / h_material) ** 2 * (Tm_material / T_M) + 1) / 2

writer = csv.writer(sys.stdout)
writer.writerow(["material", "dimension", "size_nm", "interface_type", "ThetaD_ratio", "ThetaE_ratio", "alphav_ratio"])

for material, d, size_nm, itype in test_cases:
    p = params[material]
    h = p["h"]
    D0 = compute_D0(d, h)
    D_ratio = size_nm / D0
    if D_ratio <= 1.0:
        raise ValueError(f"D/D0 <= 1 for {material} D={size_nm}, D0={D0}")
    denom = D_ratio - 1
    if itype == "free":
        alpha = compute_alpha_free(p["DSvib"])
    else:  # embedded
        alpha = compute_alpha_embedded(h, p["Tm"], h_M, T_M)
    exp_arg = (alpha - 1) / denom
    ThetaD_ratio = math.sqrt(math.exp(-exp_arg))
    ThetaE_ratio = ThetaD_ratio
    alphav_ratio = math.exp(exp_arg)
    writer.writerow([material, d, size_nm, itype, ThetaD_ratio, ThetaE_ratio, alphav_ratio])
