import json, math

data = {
    "methods": {
        "DFT-PBE": {
            "a": 6.5219,
            "E_g_noSOC": 1.5434,
            "E_g_SOC": 0.5157,
            "m_h_avg": 0.210,
            "m_e_avg": 0.428
        },
        "DFT-vdW": {
            "a": 6.4064,
            "E_g_noSOC": 1.3952,
            "E_g_SOC": 0.4169,
            "m_h_avg": 0.22,
            "m_e_avg": 0.44
        }
    },
    "absorption_spectrum": []
}

# Generate a synthetic optical absorption spectrum (epsilon2 vs energy)
points = []
step = 0.02
e = 0.0
while e <= 5.0:
    if e < 1.4:
        eps = 0.0
    else:
        # Gaussian-like peak centred at 3.2 eV
        eps = 25.0 * math.exp(-((e - 3.2) ** 2) / 0.3)
    points.append({"energy_eV": round(e, 3), "epsilon2": round(eps, 6)})
    e += step

data["absorption_spectrum"] = points

print(json.dumps(data, indent=2))
