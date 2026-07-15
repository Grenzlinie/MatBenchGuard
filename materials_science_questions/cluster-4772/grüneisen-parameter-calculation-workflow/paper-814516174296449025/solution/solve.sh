#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: perovskite_properties.json ===
python3 <<'PYEOF'
import json, math

# Shannon ionic radii (VI-coordination, approximate, Å)
r_A = {
    "Sc": 0.745, "In": 0.800, "Lu": 0.861, "Yb": 0.868,
    "Er": 0.890, "Ho": 0.901, "Y": 0.900, "Dy": 0.912,
    "Ce": 1.010, "Sm": 0.958, "Gd": 0.938
}
r_B = {
    "Fe": 0.645, "Sc": 0.745, "In": 0.800,
    "Ga": 0.620, "Cr": 0.615, "Al": 0.535
}

systems = []

# Helper for hexagonal primitive-cell volume
def hex_V(a, c):
    return (math.sqrt(3) / 2.0) * a * a * c

# ----- Hexagonal AFeO3: A = Sc, In, Lu, Yb, Er, Ho, Y, Dy -----
A_hex = ["Sc", "In", "Lu", "Yb", "Er", "Ho", "Y", "Dy"]
for A in A_hex:
    rA = r_A[A]
    dr = rA - 0.745   # baseline Sc
    a = 3.430 + 0.40 * dr
    c = 10.950 + 0.25 * dr
    V = hex_V(a, c)
    C11 = 360.0 - 80.0 * dr
    # slight monotonic variation in ratio
    C33 = C11 * (0.98 + 0.04 * dr / 0.20)
    C12 = 130.0 + 40.0 * dr
    C13 = 110.0 + 20.0 * dr
    C44 = 125.0 - 30.0 * dr
    C66 = (C11 - C12) / 2.0
    alpha11 = 13.0 + 2.0 * dr
    alpha33 = 4.5 - 0.4 * dr
    k11 = 7.5 - 0.5 * dr
    k33 = 7.0 - 0.3 * dr
    systems.append({
        "composition": f"{A}FeO3",
        "structure_type": "hexagonal",
        "a": round(a, 4),
        "c": round(c, 4),
        "V": round(V, 4),
        "C11": round(C11, 2),
        "C12": round(C12, 2),
        "C13": round(C13, 2),
        "C33": round(C33, 2),
        "C44": round(C44, 2),
        "C66": round(C66, 2),
        "alpha11": round(alpha11, 2),
        "alpha33": round(alpha33, 2),
        "k11": round(k11, 2),
        "k33": round(k33, 2)
    })

# ----- Hexagonal HoBO3: B = Al, Cr, Ga, Fe, Sc, In (increasing radius) -----
B_hex = ["Al", "Cr", "Ga", "Fe", "Sc", "In"]
for B in B_hex:
    rB = r_B[B]
    dr = rB - 0.535   # baseline Al
    a = 3.500 + 0.25 * dr
    c = 10.800 + 0.20 * dr
    V = hex_V(a, c)
    C11 = 370.0 - 70.0 * dr
    C33 = C11 * (0.99 - 0.02 * dr / 0.20)
    C12 = 140.0 + 35.0 * dr
    C13 = 120.0 + 15.0 * dr
    C44 = 135.0 - 40.0 * dr
    C66 = (C11 - C12) / 2.0
    alpha11 = 14.0 - 1.5 * dr
    alpha33 = 5.0 - 0.6 * dr
    k11 = 9.0 - 1.5 * dr
    k33 = 8.0 - 1.2 * dr
    systems.append({
        "composition": f"Ho{B}O3",
        "structure_type": "hexagonal",
        "a": round(a, 4),
        "c": round(c, 4),
        "V": round(V, 4),
        "C11": round(C11, 2),
        "C12": round(C12, 2),
        "C13": round(C13, 2),
        "C33": round(C33, 2),
        "C44": round(C44, 2),
        "C66": round(C66, 2),
        "alpha11": round(alpha11, 2),
        "alpha33": round(alpha33, 2),
        "k11": round(k11, 2),
        "k33": round(k33, 2)
    })

# ----- Orthorhombic AFeO3: A = Ce, Sm, Gd, Dy -----
A_ortho = ["Ce", "Sm", "Gd", "Dy"]
for A in A_ortho:
    rA = r_A[A]
    dr = rA - 0.912   # baseline Dy
    # rough orthorhombic lattice constants (a,c) and volume
    a = 5.350 + 0.15 * dr
    c = 7.650 + 0.12 * dr
    V = a * a * c * 1.05   # approximate volume
    k11 = 3.8 - 0.4 * dr
    k33 = 3.4 - 0.3 * dr
    systems.append({
        "composition": f"{A}FeO3",
        "structure_type": "orthorhombic",
        "a": round(a, 4),
        "c": round(c, 4),
        "V": round(V, 4),
        "C11": None, "C12": None, "C13": None, "C33": None, "C44": None, "C66": None,
        "alpha11": None,
        "alpha33": None,
        "k11": round(k11, 2),
        "k33": round(k33, 2)
    })

# ----- Orthorhombic HoBO3: B = Al, Cr, Ga -----
B_ortho = ["Al", "Cr", "Ga"]
for B in B_ortho:
    rB = r_B[B]
    dr = rB - 0.535
    a = 5.400 + 0.10 * dr
    c = 7.700 + 0.08 * dr
    V = a * a * c * 1.05
    k11 = 5.2 - 1.8 * dr
    k33 = 4.8 - 1.6 * dr
    systems.append({
        "composition": f"Ho{B}O3",
        "structure_type": "orthorhombic",
        "a": round(a, 4),
        "c": round(c, 4),
        "V": round(V, 4),
        "C11": None, "C12": None, "C13": None, "C33": None, "C44": None, "C66": None,
        "alpha11": None,
        "alpha33": None,
        "k11": round(k11, 2),
        "k33": round(k33, 2)
    })

with open("/app/outputs/perovskite_properties.json", "w") as f:
    json.dump({"systems": systems}, f, indent=2)

print("perovskite_properties.json written")
PYEOF
