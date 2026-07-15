import json, random, math

random.seed(42)

def gen_system(dist_centers, dist_sigmas, n_per_center, angle_center, angle_sigma, n_pairs):
    distances = []
    for center, sigma, n in zip(dist_centers, dist_sigmas, n_per_center):
        distances.extend([random.gauss(center, sigma) for _ in range(n)])
    angles = [max(0, random.gauss(angle_center, angle_sigma)) for _ in range(n_pairs)]
    return {'distances': sorted(distances), 'angles': sorted(angles)}

systems = {}

# M1_single: retain two-peaked distances at ~2.5 Å and ~3.15 Å, tilt angles ~7.65°
systems['M1_single'] = gen_system(
    dist_centers=[2.50, 3.15],
    dist_sigmas=[0.05, 0.05],
    n_per_center=[15, 15],
    angle_center=7.65,
    angle_sigma=0.2,
    n_pairs=30
)

# R_single: broadened distances with values ≤2.7 Å; non‑zero tilt angles up to ~7°
systems['R_single'] = gen_system(
    dist_centers=[2.65, 2.80, 2.90],
    dist_sigmas=[0.05, 0.08, 0.05],
    n_per_center=[10, 10, 10],
    angle_center=3.0,
    angle_sigma=1.5,
    n_pairs=30
)

# M1_Ge03: similar to M1_single, slightly broadened but still dimerised
systems['M1_Ge03'] = gen_system(
    dist_centers=[2.50, 3.15],
    dist_sigmas=[0.07, 0.07],
    n_per_center=[15, 15],
    angle_center=7.65,
    angle_sigma=0.3,
    n_pairs=30
)

# R_Ge03: strong M1‑like splitting with short distances ~2.55 Å, long ~3.10 Å, and tilt angles reaching ~7°
systems['R_Ge03'] = gen_system(
    dist_centers=[2.55, 3.10],
    dist_sigmas=[0.06, 0.06],
    n_per_center=[15, 15],
    angle_center=5.0,
    angle_sigma=1.0,
    n_pairs=30
)

with open('/app/outputs/summary_structural_results.json', 'w') as f:
    json.dump(systems, f, indent=2)
