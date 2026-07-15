import json, numpy as np

# elastic constants from Table 2 (GPa)
compounds = {
    "BeSiP2": [183.23, 65.148, 66.06, 176.73, 60.51, 57.98],
    "MgSiP2": [110.59, 55.61, 68.06, 78.61, 35.61, 34.19],
    "ZnSiP2": [113.33, 37.72, 46.24, 84.37, 50.18, 42.87],
    "CdSiP2": [90.57, 41.160, 40.83, 82.91, 34.72, 29.17],
    "HgSiP2": [116.26, 52.76, 58.09, 103.79, 45.33, 38.39],
}

def compute_vrh(C11, C12, C13, C33, C44, C66):
    # Voigt stiffness matrix (Voigt notation)
    C = np.array([
        [C11, C12, C13, 0, 0, 0],
        [C12, C11, C13, 0, 0, 0],
        [C13, C13, C33, 0, 0, 0],
        [0, 0, 0, C44, 0, 0],
        [0, 0, 0, 0, C44, 0],
        [0, 0, 0, 0, 0, C66],
    ])
    # compliance matrix
    S = np.linalg.inv(C)
    S11, S12, S13, S33 = S[0,0], S[0,1], S[0,2], S[2,2]
    S44, S66 = S[3,3], S[5,5]

    # Voigt bounds
    BV = (2*(C11+C12) + C33 + 4*C13) / 9.0
    M = C11 + C12 + 2*C33 - 4*C13
    GV = (M + 3*C11 - 3*C12 + 12*C44 + 6*C66) / 30.0

    # Reuss bounds
    BR = 1.0 / (2*S11 + 2*S12 + 4*S13 + S33)
    GR = 15.0 / (8*S11 + 4*S33 - 4*S12 - 8*S13 + 6*S44 + 3*S66)

    # Hill averages
    B_VRH = (BV + BR) / 2.0
    G_VRH = (GV + GR) / 2.0

    Y_VRH = 9*B_VRH*G_VRH / (3*B_VRH + G_VRH)
    Poisson_VRH = (3*B_VRH - 2*G_VRH) / (2*(3*B_VRH + G_VRH))
    return B_VRH, G_VRH, Y_VRH, Poisson_VRH

results = []
for name, cij in compounds.items():
    B, G, Y, nu = compute_vrh(*cij)
    results.append({
        "compound": name,
        "B_VRH": round(B, 4),
        "G_VRH": round(G, 4),
        "Y_VRH": round(Y, 4),
        "Poisson_VRH": round(nu, 4)
    })

print(json.dumps(results, indent=2))
