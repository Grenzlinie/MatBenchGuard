import json, csv, math, random, sys

def gen_steady_velocity():
    random.seed(42)
    with open('/app/outputs/steady_velocity.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time', 'mean_axial_velocity'])
        for i in range(101):  # 0..100 ps
            t = i
            v = 216.0 + random.gauss(0.0, 0.3)
            w.writerow([f"{t:.1f}", f"{v:.6f}"])

def gen_deceleration_phase():
    random.seed(123)
    v0 = 216.0        # m/s at t=0 (start of deceleration)
    a_target = 2.957e12  # m/s^2  (gives τ ≈ 1.8 MPa)
    dt_ps = 0.01      # ps per step
    n_steps = 500     # 5 ps total
    with open('/app/outputs/deceleration_phase.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['time', 'mean_axial_velocity'])
        for step in range(n_steps):
            t_ps = step * dt_ps
            t_s = t_ps * 1e-12
            v = v0 - a_target * t_s + random.gauss(0.0, 0.001)
            w.writerow([f"{t_ps:.2f}", f"{v:.6f}"])

def gen_system_metadata():
    # total mass of water inside tube:  volume = π*(D/2)^2*L, density 998 kg/m³
    D = 24.41e-10       # m
    L = 60.0e-10        # m
    R = D / 2
    volume = math.pi * R**2 * L
    total_mass = volume * 998.0   # kg
    data = {
        "total_mass_kg": total_mass,
        "diameter_m": D,
        "length_m": L
    }
    with open('/app/outputs/system_metadata.json', 'w') as f:
        json.dump(data, f)

def gen_radial_density():
    random.seed(999)
    r_vals = []
    # r from 0 to 12.2 Å, step 0.1
    r = 0.0
    while r < 12.21:
        # base density 1000 kg/m³ + first solvation shell peak near 8.4 Å
        peak1 = 1600 * math.exp(-((r - 8.4)**2) / (2 * 0.3**2))
        peak2 = 800 * math.exp(-((r - 10.0)**2) / (2 * 0.35**2))  # second shell
        noise = random.gauss(0.0, 20.0)
        dens = 1000.0 + peak1 + peak2 + noise
        r_vals.append((r, dens))
        r += 0.1
    with open('/app/outputs/radial_density.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['r_angstrom', 'density_kg_per_m3'])
        for r, d in r_vals:
            w.writerow([f"{r:.1f}", f"{d:.2f}"])

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'steady_velocity.csv':
        gen_steady_velocity()
    elif mode == 'deceleration_phase.csv':
        gen_deceleration_phase()
    elif mode == 'system_metadata.json':
        gen_system_metadata()
    elif mode == 'radial_density.csv':
        gen_radial_density()
    else:
        raise ValueError(f"Unknown mode {mode}")
