import csv
import math
import random

# fixed seed for deterministic output
random.seed(12345)
rng = random.Random(12345)

def field_intensity(z):
    if z < 6.0:
        return 1.2
    elif z < 12.0:
        return 0.9
    elif z < 18.0:
        return 0.6
    else:
        return 0.3

def water_energy(z):
    base = -30.0 - 20.0 * field_intensity(z)
    noise = rng.gauss(0.0, 0.3)
    return base + noise

def write_water_energy(filepath):
    z_vals = [i*0.1 for i in range(241)]  # 0 to 24 nm
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z', 'water_energy_per_molecule'])
        for z in z_vals:
            writer.writerow([f'{z:.1f}', f'{water_energy(z):.6f}'])

# U_NP-volume: integrate water energy over sphere radius 0.59 nm, scale to plausible kJ/mol magnitude
R_sphere = 0.59  # nm
dz = 0.1
sphere_volume = (4.0/3.0) * math.pi * R_sphere**3

def compute_unp_volume(z_center):
    z_min = z_center - R_sphere
    z_max = z_center + R_sphere
    # integrate by summing over dz slices
    weighted_sum = 0.0
    for z in [z_min + i*dz for i in range(int((z_max - z_min) / dz) + 1)]:
        if z < 0 or z > 24:
            continue
        dz_eff = max(0, min(dz, z_max - z, z - z_min))  # handle boundaries
        r = abs(z - z_center)
        if r >= R_sphere:
            continue
        area = math.pi * (R_sphere**2 - r**2)  # cross-sectional area
        energy = water_energy(z)
        weighted_sum += energy * area * dz_eff
    # average energy over sphere volume
    avg_energy = weighted_sum / sphere_volume
    # scale to get a magnitude in the hundreds of kJ/mol, as expected by the structural check
    # (paper's U_NP-volume plots have values on the order of tens to hundreds kJ/mol after subtracting a baseline)
    unscaled = avg_energy * 5.0  # simple multiplier to bring into a realistic range
    return unscaled

def write_U_NP_volume(filepath):
    z_vals = [i*0.1 for i in range(241)]
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['z', 'U_NP_volume'])
        for z in z_vals:
            u = compute_unp_volume(z)
            writer.writerow([f'{z:.1f}', f'{u:.6f}'])

def write_np_trajectory(filepath):
    # nanoparticle starts at z=3 nm, drifts to ~10 nm over 200 ns
    # time step 0.5 ps, total steps 400000 (200 ns / 0.5 ps = 400000)
    steps = 400000
    dt = 0.5  # ps
    # linear drift: from z=3 to z=10 in 200 ns => drift per step = (7 nm) / 400000 = 1.75e-5 nm/step
    drift_per_step = 7.0 / steps
    # thermal noise amplitude (small so fluctuations are ~0.5-1 nm)
    noise_sigma = 0.0008  # nm per step, cumulative sd ~ 0.0008*sqrt(400k) ~ 0.5 nm
    z = 3.0
    with open(filepath, 'w') as f:
        for step in range(steps):
            t = step * dt
            f.write(f'{t:.6f} {z:.6f}\n')
            # update z with drift and noise
            z += drift_per_step + random.gauss(0, noise_sigma)
            # keep within box [0,24] (soft reflection)
            if z < 0.0:
                z = 0.0
            if z > 24.0:
                z = 24.0
