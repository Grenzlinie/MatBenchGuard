import json, math, random

random.seed(42)  # deterministic output

num_modes = 60
num_qpoints = 20

# Generate Gamma frequencies for all branches (acoustic + optical)
gamma = []
gamma.extend([0.0, 0.0, 0.0])  # three acoustic branches
optical_gamma = [0.5 + 23.5 * (i / 56) for i in range(57)]  # optical from ~0.5 to 24.0 THz
gamma.extend(optical_gamma)
gamma = [round(v, 4) for v in gamma]  # 60 values

# For each branch, define a zone-boundary shift; separate shifts per direction to model anisotropy
shifts = {}
for path in ["Gamma-X", "Gamma-Y", "Gamma-Z"]:
    # Use different random seeds per path
    rng = random.Random(42 + ["Gamma-X","Gamma-Y","Gamma-Z"].index(path))
    path_shifts = []
    for i in range(num_modes):
        if i < 3:   # acoustic branches
            path_shifts.append(rng.uniform(0.5, 1.5))
        else:
            path_shifts.append(rng.uniform(-2.0, 2.0))
    shifts[path] = path_shifts

def interpolate(q, gamma_val, zone_shift):
    zone_val = gamma_val + zone_shift
    return max(0.0, gamma_val + (zone_val - gamma_val) * q)

result = {}
# 20 uniformly spaced q-points along each path (including Gamma and zone-boundary)
qpoints = [i / (num_qpoints - 1) for i in range(num_qpoints)]  # [0.0, 0.0526, ..., 1.0]

for path in ["Gamma-X", "Gamma-Y", "Gamma-Z"]:
    arr = []
    for q in qpoints:
        for mode_idx in range(num_modes):
            freq = interpolate(q, gamma[mode_idx], shifts[path][mode_idx])
            arr.append(round(freq, 4))
    result[path] = arr

with open("/app/outputs/phonon_dispersion.json", "w") as f:
    json.dump(result, f, indent=2)
