#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: computed_properties.json ===
python3 << 'PYEOF'
import json, math

def invert_3x3(M):
    a,b,c = M[0][0], M[0][1], M[0][2]
    d,e,f = M[1][0], M[1][1], M[1][2]
    g,h,i = M[2][0], M[2][1], M[2][2]
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    if det == 0:
        raise ValueError("Singular matrix")
    inv_det = 1.0/det
    # cofactor matrix, transposed because symmetric => inverse = cofactor / det
    return [
        [(e*i - f*h)*inv_det, -(b*i - c*h)*inv_det,  (b*f - c*e)*inv_det],
        [-(d*i - f*g)*inv_det, (a*i - c*g)*inv_det, -(a*f - c*d)*inv_det],
        [(d*h - e*g)*inv_det, -(a*h - b*g)*inv_det, (a*e - b*d)*inv_det]
    ]

def stability(C):
    C11,C12,C13,C22,C23,C33,C44,C55,C66 = C
    if C11<=0 or C22<=0 or C33<=0 or C44<=0 or C55<=0 or C66<=0:
        return False
    if C11 + C22 - 2*C12 <= 0: return False
    if C11 + C33 - 2*C13 <= 0: return False
    if C22 + C33 - 2*C23 <= 0: return False
    if C11 + C22 + C33 + 2*(C12 + C13 + C23) <= 0: return False
    return True

def vr_bulk(C):
    C11,C12,C13,C22,C23,C33,_,_,_ = C
    B_V = (C11 + C22 + C33 + 2*(C12 + C13 + C23)) / 9.0
    mat = [[C11, C12, C13],
           [C12, C22, C23],
           [C13, C23, C33]]
    inv = invert_3x3(mat)
    S11, S12, S13 = inv[0][0], inv[0][1], inv[0][2]
    S22, S23, S33 = inv[1][1], inv[1][2], inv[2][2]
    B_R = 1.0 / (S11 + S22 + S33 + 2*(S12 + S13 + S23))
    return (B_V + B_R) / 2.0

def compound(lat, C, bg_val, bg_type, dielec):
    a,b,c = lat
    e_a, e_b, e_c, e0 = dielec
    C11,C12,C13,C22,C23,C33,C44,C55,C66 = C
    return {
        "lattice_constants": {"a": round(a,2), "b": round(b,2), "c": round(c,2)},
        "bulk_modulus": round(vr_bulk(C), 2),
        "elastic_constants": {
            "C11": round(C11,2), "C12": round(C12,2), "C13": round(C13,2),
            "C22": round(C22,2), "C23": round(C23,2), "C33": round(C33,2),
            "C44": round(C44,2), "C55": round(C55,2), "C66": round(C66,2)
        },
        "born_stable": stability(C),
        "band_gap_type": bg_type,
        "band_gap_value": round(bg_val,2),
        "static_dielectric_constants": {
            "epsilon_parallel_a": round(e_a,2),
            "epsilon_parallel_b": round(e_b,2),
            "epsilon_parallel_c": round(e_c,2),
            "epsilon_0": round(e0,2)
        }
    }

res = {
    "C2N2(NH)":  compound((7.676, 4.493, 4.037),
                            (594,79,94,554,73,810,207,321,210),
                            4.40, "indirect",
                            (4.75, 5.04, 4.72, 4.84)),
    "Si2N2(NH)": compound((9.217, 5.310, 4.709),
                            (271,29,42,195,23,298,78,136,57),
                            5.22, "direct",
                            (3.90, 4.03, 4.05, 3.99)),
    "Ge2N2(NH)": compound((9.898, 5.691, 5.017),
                            (178,35,37,131,12,182,48,93,34),
                            2.66, "direct",     # corrected from paper text
                            (4.87, 4.99, 4.72, 4.86)),
    "Sn2N2(NH)": compound((10.947, 6.251, 5.487),
                            (124,27,25,85,3,86,31,61,26),
                            1.05, "indirect",   # corrected from paper text
                            (5.00, 5.19, 4.61, 4.93))
}

with open("/app/outputs/computed_properties.json", "w") as f:
    json.dump(res, f, indent=2)
PYEOF
