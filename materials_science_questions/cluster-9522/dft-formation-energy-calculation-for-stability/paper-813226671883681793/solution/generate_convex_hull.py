#!/usr/bin/env python3
"""Generate convex_hull_analysis.json by computing the lower convex hull."""
import json
import math

INPUT = "/app/outputs/formation_enthalpies.json"
OUTPUT = "/app/outputs/convex_hull_analysis.json"

with open(INPUT) as f:
    data = json.load(f)

# Build (x, delta_H, name) for all entries (excluding pure elements if needed)
points = []
for entry in data:
    name = entry["compound"]
    if name in ("Ge A4", "Ti A3"):
        continue
    protons = entry["natoms"]
    # derive Ge fraction from name, but safer: we can compute from formula? We'll trust the x from earlier.
    # However this script doesn't directly know x_Ge. We'll parse it from total_energy_per_cell and reference.
    # Better: we know the papers x. We'll hardcode mapping.
    # Actually we have the formation enthalpy, we can compute x from the input? Not needed; we have hardcoded x below.
    pass

# To avoid re-deriving x from arbitrary energies, we hardcode the known x from the paper:
xmap = {
    "Ge3Ti5": 6/16,  # 0.375
    "Ge4Ti5": 16/36, # 0.444444
    "Ge5Ti6": 20/44, # 0.454545
    "Ge2Ti":  16/24, # 0.666667
}

pts = []
for entry in data:
    name = entry["compound"]
    if name not in xmap:
        continue
    x = xmap[name]
    dh = entry["formation_enthalpy_kJ_mol_atom"]
    pts.append((x, dh, name))

# Add pure elements as endpoints for hull construction (they have dh=0)
# But they are on the hull only if no compound is lower; but we need endpoints for hull definition.
# We'll include them as (0,0) Ti and (1,0) Ge
pts.append((0.0, 0.0, "Ti"))
pts.append((1.0, 0.0, "Ge"))

# Sort by x
pts.sort(key=lambda p: p[0])

# Lower convex hull (since low delta_H is better)
def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

lower = []
for p in pts:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

# Filter only intermetallic compounds (exclude Ti, Ge)
hull_names = [p[2] for p in lower if p[2] not in ("Ti", "Ge")]
ge4ti5_on_hull = "Ge4Ti5" in hull_names

result = {
    "on_hull": hull_names,
    "ge4ti5_on_hull": ge4ti5_on_hull
}

with open(OUTPUT, "w") as f:
    json.dump(result, f, indent=2)
print(f"Written {OUTPUT}")
