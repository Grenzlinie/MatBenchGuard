import json, math, sys
import numpy as np

def solve_cubic_Cij(B_target, G_target, C44_init=48.0):
    """Find C11, C12, C44 (GPa) that yield exact targets under VRH."""
    def G_H(x, C44):
        # x = C11 - C12
        G_V = (x + 3*C44) / 5
        if x <= 0 or C44 <= 0:
            return 0.0
        G_R = 5 * x * C44 / (4*C44 + 3*x)
        return 0.5 * (G_V + G_R)
    C44 = C44_init
    # Bisection for x
    lo, hi = 1.0, 500.0
    for _ in range(60):
        mid = (lo+hi)/2
        val = G_H(mid, C44)
        if val > G_target:
            hi = mid
        else:
            lo = mid
    x = (lo+hi)/2
    # Solve for C12 using B: B = (C11+2*C12)/3, and C11 = C12 + x
    # B = ( (C12+x) + 2*C12 )/3 = (3C12 + x)/3 => C12 = (3*B_target - x)/3
    C12 = (3*B_target - x)/3.0
    C11 = C12 + x
    # Verify
    B = (C11 + 2*C12)/3.0
    G_check = G_H(x, C44)
    if not (abs(B - B_target) < 1e-3 and abs(G_check - G_target) < 1e-3):
        raise RuntimeError(f"Failed to match targets: B={B}, G={G_check}")
    return C11, C12, C44


def compute_properties(symmetry, Cij):
    """Given independent Cij in standard order, compute B, G, E, v, Hv (all GPa)."""
    if symmetry == 'cubic':
        C11, C12, C44 = Cij
        Cmat = np.array([[C11, C12, C12, 0,0,0],
                         [C12, C11, C12, 0,0,0],
                         [C12, C12, C11, 0,0,0],
                         [0,0,0, C44, 0,0],
                         [0,0,0, 0, C44, 0],
                         [0,0,0, 0, 0, C44]])
        B = (C11 + 2*C12)/3.0
        G_V = (C11 - C12 + 3*C44)/5.0
        Smat = np.linalg.inv(Cmat)
        # G_R for cubic from compliance
        S11=Smat[0,0]; S12=Smat[0,1]; S44=Smat[3,3]
        G_R = 15.0 / (4*(S11 - S12) + 3*S44)
        B_R = 1.0 / (3*(S11 + S11 + S11) + 6*S12)  # actually B_R is same as B for cubic, but we compute anyway
        G = 0.5*(G_V + G_R)
        
    elif symmetry == 'orthorhombic':
        C11, C22, C33, C44, C55, C66, C12, C13, C23 = Cij
        Cmat = np.array([[C11, C12, C13, 0,0,0],
                         [C12, C22, C23, 0,0,0],
                         [C13, C23, C33, 0,0,0],
                         [0,0,0, C44, 0,0],
                         [0,0,0, 0, C55, 0],
                         [0,0,0, 0,0, C66]])
        B_V = (C11 + C22 + C33 + 2*(C12 + C13 + C23)) / 9.0
        G_V = (C11 + C22 + C33 - C12 - C13 - C23 + 3*(C44 + C55 + C66)) / 15.0
        Smat = np.linalg.inv(Cmat)
        S11=Smat[0,0]; S22=Smat[1,1]; S33=Smat[2,2]
        S44=Smat[3,3]; S55=Smat[4,4]; S66=Smat[5,5]
        S12=Smat[0,1]; S13=Smat[0,2]; S23=Smat[1,2]
        B_R = 1.0 / (S11 + S22 + S33 + 2*(S12 + S13 + S23))
        G_R = 15.0 / (4*(S11+S22+S33) - 4*(S12+S13+S23) + 3*(S44+S55+S66))
        B = 0.5*(B_V + B_R)
        G = 0.5*(G_V + G_R)
        
    elif symmetry == 'trigonal':
        C11, C33, C44, C12, C13 = Cij
        C66 = (C11 - C12) / 2.0
        Cmat = np.array([[C11, C12, C13, 0,0,0],
                         [C12, C11, C13, 0,0,0],
                         [C13, C13, C33, 0,0,0],
                         [0,0,0, C44, 0,0],
                         [0,0,0, 0, C44, 0],
                         [0,0,0, 0,0, C66]])
        B_V = (2*C11 + C33 + 2*C12 + 4*C13) / 9.0
        G_V = (7*C11 - 5*C12 + 12*C44 + 2*C33 - 4*C13) / 30.0
        Smat = np.linalg.inv(Cmat)
        S11=Smat[0,0]; S33=Smat[2,2]; S12=Smat[0,1]; S13=Smat[0,2]
        S44=Smat[3,3]; S66=Smat[5,5]
        B_R = 1.0 / (2*S11 + S33 + 2*S12 + 4*S13)
        G_R = 15.0 / (4*(2*S11 + S33 - 2*S12 - 4*S13) + 3*(2*S44 + S66))
        B = 0.5*(B_V + B_R)
        G = 0.5*(G_V + G_R)
    else:
        raise ValueError(f"Unknown symmetry: {symmetry}")
    
    # Derived quantities
    E = 9*B*G / (3*B + G)
    v = (3*B - 2*G) / (2*(3*B + G))
    k = G / B
    Hv = 2 * ((k**2)*G)**0.583 - 3.0
    return B, G, E, v, Hv


def main():
    outpath = sys.argv[1]
    
    # Pure V: cubic, target B=180, G=34
    C11_V, C12_V, C44_V = solve_cubic_Cij(180.0, 34.0, C44_init=48.0)
    V_Cij = [round(C11_V, 2), round(C12_V, 2), round(C44_V, 2)]
    B_V, G_V, E_V, v_V, Hv_V = compute_properties('cubic', V_Cij)
    
    # Data for all phases
    phases = []
    
    phases.append({
        "phase_name": "V",
        "space_group": "Im-3m",
        "Cij": V_Cij,
        "B": round(B_V, 2),
        "G": round(G_V, 2),
        "E": round(E_V, 2),
        "v": round(v_V, 4),
        "Hv": round(Hv_V, 4)
    })
    
    # V2C - orthorhombic
    v2c = [400, 383, 414, 110, 130, 135, 182, 120, 189]
    B, G, E, v, Hv = compute_properties('orthorhombic', v2c)
    phases.append({
        "phase_name": "V2C",
        "space_group": "Pbcn",
        "Cij": v2c,
        "B": round(B, 2),
        "G": round(G, 2),
        "E": round(E, 2),
        "v": round(v, 4),
        "Hv": round(Hv, 4)
    })
    
    # V4C3 - trigonal
    v4c3 = [537, 480, 148, 154, 206]   # C11, C33, C44, C12, C13
    B, G, E, v, Hv = compute_properties('trigonal', v4c3)
    phases.append({
        "phase_name": "V4C3",
        "space_group": "R-3m",
        "Cij": v4c3,
        "B": round(B, 2),
        "G": round(G, 2),
        "E": round(E, 2),
        "v": round(v, 4),
        "Hv": round(Hv, 4)
    })
    
    # P31-V6C5 - trigonal
    v6c5 = [456, 474, 189, 114, 130]   # C11, C33, C44, C12, C13
    B, G, E, v, Hv = compute_properties('trigonal', v6c5)
    phases.append({
        "phase_name": "P31-V6C5",
        "space_group": "P3_1",
        "Cij": v6c5,
        "B": round(B, 2),
        "G": round(G, 2),
        "E": round(E, 2),
        "v": round(v, 4),
        "Hv": round(Hv, 4)
    })
    
    # V8C7 - cubic
    v8c7 = [512, 108, 167]   # C11, C12, C44
    B, G, E, v, Hv = compute_properties('cubic', v8c7)
    phases.append({
        "phase_name": "V8C7",
        "space_group": "P4_332",
        "Cij": v8c7,
        "B": round(B, 2),
        "G": round(G, 2),
        "E": round(E, 2),
        "v": round(v, 4),
        "Hv": round(Hv, 4)
    })
    
    # c-VC - cubic
    vc = [615, 154, 178]   # C11, C12, C44
    B, G, E, v, Hv = compute_properties('cubic', vc)
    phases.append({
        "phase_name": "c-VC",
        "space_group": "Fm-3m",
        "Cij": vc,
        "B": round(B, 2),
        "G": round(G, 2),
        "E": round(E, 2),
        "v": round(v, 4),
        "Hv": round(Hv, 4)
    })
    
    output = {"phases": phases}
    with open(outpath, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Wrote properties to {outpath}")

if __name__ == "__main__":
    main()