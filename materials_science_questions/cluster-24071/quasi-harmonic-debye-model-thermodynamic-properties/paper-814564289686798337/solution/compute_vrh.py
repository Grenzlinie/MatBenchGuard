import sys, json, math

def compute_vrh(C11, C12, C44):
    B = (C11 + 2*C12) / 3.0
    G_V = (C11 - C12 + 3*C44) / 5.0
    denom = 4*C44 + 3*(C11 - C12)
    G_R = 5 * (C11 - C12) * C44 / denom if denom != 0 else 0
    G = (G_V + G_R) / 2.0
    E = 9*B*G / (3*B + G) if (3*B + G) != 0 else 0
    nu = (3*B - 2*G) / (2*(3*B + G)) if (3*B + G) != 0 else 0
    G_B = G / B if B != 0 else 0
    return {
        "B_VRH_GPa": round(B, 3),
        "G_VRH_GPa": round(G, 3),
        "E_VRH_GPa": round(E, 3),
        "Poisson_ratio": round(nu, 3),
        "G_B_ratio": round(G_B, 3)
    }

if __name__ == "__main__":
    C11, C12, C44 = map(float, sys.argv[1:4])
    result = compute_vrh(C11, C12, C44)
    json.dump(result, sys.stdout)
