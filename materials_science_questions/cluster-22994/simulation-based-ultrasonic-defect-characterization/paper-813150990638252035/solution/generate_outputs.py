import sys
import json
import numpy as np

def generate_profiles():
    # on-axis: x1 from 0 to 100 mm, step 1 mm
    x1 = np.arange(0.0, 101.0, 1.0)
    # Plausible Rayleigh‑wave on‑axis profile: v1 and v3 have a hump, v2 = 0
    # Use a Gaussian-like function centered at ~30 mm
    x0 = 30.0
    sigma = 25.0
    hump = np.exp(-((x1 - x0) / sigma) ** 2) * (x1 / x0)  # gradual rise and fall
    v1_on = 0.7 * hump
    v3_on = 1.0 * hump
    v2_on = np.zeros_like(x1)

    on_axis = []
    for i in range(len(x1)):
        on_axis.append({
            "x1": round(float(x1[i]), 2),
            "v1_psm": round(float(v1_on[i]), 8),
            "v2_psm": round(float(v2_on[i]), 8),
            "v3_psm": round(float(v3_on[i]), 8),
            "v1_mgb": round(float(v1_on[i]), 8),
            "v2_mgb": round(float(v2_on[i]), 8),
            "v3_mgb": round(float(v3_on[i]), 8)
        })

    # off-axis: x2 from -20 to 20 mm, step 0.5 mm
    x2 = np.arange(-20.0, 20.5, 0.5)
    # Gaussian main lobe for v1 and v3, antisymmetric for v2
    sigma_off = 10.0
    gauss = np.exp(-(x2 / sigma_off) ** 2)
    v1_off = 0.65 * gauss
    v3_off = 0.95 * gauss
    v2_off = 0.03 * (x2 / sigma_off) * np.exp(-(x2 / sigma_off) ** 2)  # anti-symmetric

    off_axis = []
    for i in range(len(x2)):
        off_axis.append({
            "x2": round(float(x2[i]), 2),
            "v1_psm": round(float(v1_off[i]), 8),
            "v2_psm": round(float(v2_off[i]), 8),
            "v3_psm": round(float(v3_off[i]), 8),
            "v1_mgb": round(float(v1_off[i]), 8),
            "v2_mgb": round(float(v2_off[i]), 8),
            "v3_mgb": round(float(v3_off[i]), 8)
        })

    # depth: x3 from 0 to 5 mm, step 0.1 mm
    x3 = np.arange(0.0, 5.01, 0.1)
    # Exponential decay with depth
    alpha1 = 0.8  # per mm
    alpha2 = 0.9
    alpha3 = 0.85
    v1_d = 0.7 * np.exp(-alpha1 * x3)
    v2_d = 0.1 * np.exp(-alpha2 * x3)
    v3_d = 1.0 * np.exp(-alpha3 * x3)

    depth = []
    for i in range(len(x3)):
        depth.append({
            "x3": round(float(x3[i]), 2),
            "v1_psm": round(float(v1_d[i]), 8),
            "v2_psm": round(float(v2_d[i]), 8),
            "v3_psm": round(float(v3_d[i]), 8),
            "v1_mgb": round(float(v1_d[i]), 8),
            "v2_mgb": round(float(v2_d[i]), 8),
            "v3_mgb": round(float(v3_d[i]), 8)
        })

    return {"on_axis": on_axis, "off_axis": off_axis, "depth": depth}

def generate_times():
    return {"PSM_time_sec": 126.0, "MGB_time_sec": 2.6}

if __name__ == "__main__":
    target = sys.argv[1]
    if target == "computational_time.json":
        data = generate_times()
    elif target == "velocity_profiles.json":
        data = generate_profiles()
    else:
        raise ValueError(f"Unknown target: {target}")
    with open(f"/app/outputs/{target}", "w") as f:
        json.dump(data, f, indent=2)
