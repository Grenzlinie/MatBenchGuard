import json, math

J = 1.0
S = 1.0
gmuB_HA = 0.05
ck = 0.005

bulk = math.sqrt(gmuB_HA * (gmuB_HA + 16 * S * J))
surf = math.sqrt(gmuB_HA * (gmuB_HA + 8 * S * J))
ratio = 4 * math.pi * ck * math.sqrt(S * J / gmuB_HA)

data = {
    "bulk_energy": bulk,
    "surface_energy": surf,
    "intensity_ratio": ratio
}
with open("/app/outputs/results.json", "w") as f:
    json.dump(data, f)
