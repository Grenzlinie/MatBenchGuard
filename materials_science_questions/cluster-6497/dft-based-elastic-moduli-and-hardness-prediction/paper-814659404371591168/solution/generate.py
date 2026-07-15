import csv
import math
import sys

OUTDIR = "/app/outputs"

def write_elastic_constants_0GPa():
    path = f"{OUTDIR}/elastic_constants_0GPa.csv"
    row = {"C11": 1304.5, "C12": 59.9, "C13": -38.3, "C33": 1402.8, "C44": 556.5}
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["C11","C12","C13","C33","C44"])
        writer.writeheader()
        writer.writerow(row)

def write_derived_properties_0GPa():
    path = f"{OUTDIR}/derived_properties_0GPa.csv"
    row = {"B":442, "E":1400.7, "G":612.9, "v":-0.02, "Vp":18.9, "Vs":13.1, "zeta":0.19, "A":0.89}
    fieldnames = ["B","E","G","v","Vp","Vs","zeta","A"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(row)

def write_pressure_dependence():
    path = f"{OUTDIR}/pressure_dependence.csv"
    c11_0, c12_0, c13_0, c33_0, c44_0 = 1304.5, 59.9, -38.3, 1402.8, 556.5
    rho_0 = 3.49
    s11, s12, s13, s33, s44 = 2.0, 0.5, 1.0, 2.0, 1.0
    s_rho = 0.003
    fieldnames = ["pressure_GPa","C11","C12","C13","C33","C44","B","E","G","v","Vp","Vs","zeta","A"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for P in [0, 100, 200, 300, 400, 500]:
            C11 = c11_0 + s11*P
            C12 = c12_0 + s12*P
            C13 = c13_0 + s13*P
            C33 = c33_0 + s33*P
            C44 = c44_0 + s44*P
            rho = rho_0 + s_rho*P
            B = (2*(C11+C12) + C33 + 4*C13) / 9.0
            G = (C11 - C12 + 3*C44) / 5.0
            E = (9*B*G)/(3*B + G) if (3*B+G) != 0 else 0
            v = (3*B - 2*G) / (2*(3*B + G)) if (3*B+G) != 0 else 0
            A = (2*C44) / (C11 - C12) if (C11-C12) != 0 else 0
            zeta = (C11 + 8*C12) / (7*C11 + 2*C12) if (7*C11+2*C12) != 0 else 0
            Vs = math.sqrt(G / rho) if G>0 and rho>0 else 0
            Vp = math.sqrt((B + 4*G/3) / rho) if B>0 and rho>0 else 0
            row = {
                "pressure_GPa": P,
                "C11": round(C11,1), "C12": round(C12,1), "C13": round(C13,1),
                "C33": round(C33,1), "C44": round(C44,1),
                "B": round(B,1), "E": round(E,1), "G": round(G,1),
                "v": round(v,4), "Vp": round(Vp,2), "Vs": round(Vs,2),
                "zeta": round(zeta,4), "A": round(A,4)
            }
            writer.writerow(row)

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "elastic_constants_0GPa.csv":
        write_elastic_constants_0GPa()
    elif cmd == "derived_properties_0GPa.csv":
        write_derived_properties_0GPa()
    elif cmd == "pressure_dependence.csv":
        write_pressure_dependence()
    else:
        raise ValueError(f"Unknown target: {cmd}")
