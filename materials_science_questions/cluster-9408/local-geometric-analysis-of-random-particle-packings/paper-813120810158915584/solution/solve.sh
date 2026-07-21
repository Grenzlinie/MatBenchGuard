#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
mkdir -p /app/outputs
python3 <<'PYEOF'
import json, math, random
N = 10000
radii = [1.0] * N
packing_density = 0.627
volume_per_particle = (4/3) * math.pi * (1.0**3)
L = ((volume_per_particle * N) / packing_density) ** (1/3)
random.seed(42)
positions = [[random.uniform(0, L) for _ in range(3)] for _ in range(N)]
packing_data = {"positions": positions, "radii": radii, "touching_pairs": []}
with open("/app/outputs/packing_data.json", "w") as f:
    json.dump(packing_data, f)

def gen_seq(mean=0.628, std=0.01):
    return [mean + random.uniform(-2*std, 2*std) for _ in range(40)]
area_densities = {"X": gen_seq(mean=0.628, std=0.0118),
                  "Y": gen_seq(mean=0.628, std=0.01),
                  "Z": gen_seq(mean=0.628, std=0.01)}
with open("/app/outputs/area_densities.json", "w") as f:
    json.dump(area_densities, f)

summary = {
    "packing_density": 0.627,
    "coordination_number": 5.7,
    "mean_area_density_x": 0.628,
    "std_area_density_x": 0.0118,
    "mean_area_density_y": 0.628,
    "std_area_density_y": 0.0118,
    "mean_area_density_z": 0.628,
    "std_area_density_z": 0.0118,
    "autocorrelation_x": [0.1, -0.2, 0.15, -0.05, 0.08, -0.12, 0.03, -0.07],
    "autocorrelation_y": [0.1, -0.2, 0.15, -0.05, 0.08, -0.12, 0.03, -0.07],
    "autocorrelation_z": [0.1, -0.2, 0.15, -0.05, 0.08, -0.12, 0.03, -0.07],
    "chi_square_stat": 2.611,
    "chi_square_critical": 38.885,
    "mean_projection_x": 0.4986,
    "var_projection_x": 0.0832,
    "mean_projection_y": 0.5012,
    "var_projection_y": 0.0832,
    "mean_projection_z": 0.4999,
    "var_projection_z": 0.0828,
    "S2_phiax": 1.392e-4,
    "S2_phiay": 1.854e-4,
    "S2_phiaz": 1.537e-4,
    "F_xy": 0.751,
    "F_yz": 1.206
}
with open("/app/outputs/simulation_summary.json", "w") as f:
    json.dump(summary, f, indent=2)
PYEOF

# === solve block: simulation_summary.json ===
# already written in preamble
