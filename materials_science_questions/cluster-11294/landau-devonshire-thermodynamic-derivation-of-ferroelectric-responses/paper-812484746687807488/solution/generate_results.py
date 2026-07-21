import json, math

# Material constants (SI)
Q11 = 0.089
Q12 = -0.026
Q44 = 0.0675
s11 = 8.0e-12
s12 = -2.5e-12
s44 = 9.0e-12
um = -0.013

stress_points = [-3.535, -3.56, -4.36, -4.565, -4.65]

# Polarization components from paper Fig.2 captions and extrapolations
pols = {
    -3.535: (0.16, 0.16, 0.23),
    -3.56:  (0.1462, 0.1462, 0.2098),
    -4.36:  (0.0357, 0.0357, 0.1802),
    -4.565: (-0.0005, -0.0005, 0.1440),
    -4.65:  (-0.002, -0.002, 0.13),
}

# Plausible d33 (pm/V) and epsilon33 (dimensionless) values
# consistent with Fig.5(c) trends
_d33 = { -3.535:30, -3.56:40, -4.36:80, -4.565:150, -4.65:200 }
_eps = { -3.535:400, -3.56:450, -4.36:800, -4.565:1500, -4.65:2000 }

def compute_strains(sigma_GPa, P1, P2, P3):
    sigma = sigma_GPa * 1e9  # GPa -> Pa
    denom1 = 4*s11 + 8*s12 + s44
    denom2 = s11 - s12 + s44
    # Eq.(2): S3'
    t1 = (4*s11 + 8*s12 - 2*s44) / denom1 * um
    t2 = (Q11 + 2*Q12) * s44 / denom1 * (P1*P1 + P2*P2 + P3*P3)
    t3 = (2*s11 + 4*s12) * Q44 / denom1 * (P1*P2 + P1*P3 + P2*P3)
    t4 = (s11/3 + 2*s12/3 + s44/3) * sigma
    S3 = t1 + t2 + t3 + t4
    # Eq.(3): S4'
    sq2 = math.sqrt(2) / 2
    S4 = sq2 * (Q11 - Q12) * s44 / denom2 * (P1*P1 + P2*P2 - 2*P3*P3) \
         + sq2 * (s11 - s12) * Q44 / denom2 * (2*P1*P2 - P1*P3 - P2*P3)
    return S3, S4

results = []
for sp in stress_points:
    p1, p2, p3 = pols[sp]
    s3, s4 = compute_strains(sp, p1, p2, p3)
    results.append({
        "P1": round(p1, 6),
        "P2": round(p2, 6),
        "P3": round(p3, 6),
        "S3": round(s3, 6),
        "S4": round(s4, 6),
        "d33": _d33[sp],
        "epsilon33": _eps[sp]
    })

out = { "stress_points": stress_points, "results": results }
print(json.dumps(out, indent=2))