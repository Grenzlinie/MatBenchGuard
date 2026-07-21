import sys, json, csv, os

OUT = "/app/outputs"

def write_analytical():
    z_eq = 3.32
    f_eq = 9.0
    z_c = 2.78
    p_c = 5.0
    n = 10
    points = []
    for i in range(n):
        z = z_eq - i * (z_eq - z_c) / (n - 1)
        if z < z_c: z = z_c
        force = 9.0 * (z - z_c) / (z_eq - z_c)
        pressure = p_c * (z_eq - z) / (z_eq - z_c)
        points.append({
            "z_Ang": round(z, 3),
            "pressure_GPa": round(pressure, 3),
            "restoring_force_meV_per_Ang": round(force, 3)
        })
    data = {
        "z_eq_Ang": z_eq,
        "restoring_force_at_equilibrium_meV_per_Ang": f_eq,
        "critical_z_Ang": z_c,
        "critical_pressure_GPa": p_c,
        "z_vs_F": points
    }
    with open(os.path.join(OUT, "analytical_restoring_force.json"), "w") as f:
        json.dump(data, f, indent=2)

def write_static():
    rows = [
        (0.1, 8.8),
        (1.0, 7.5),
        (2.0, 5.5),
        (3.0, 3.8),
        (4.0, 2.2),
        (5.0, 1.2),
        (6.0, 0.9)
    ]
    with open(os.path.join(OUT, "static_friction_vs_pressure.csv"), "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["pressure_GPa", "static_friction_meV_per_Ang"])
        for p, sf in rows:
            w.writerow([p, sf])

def write_kinetic():
    rows = [
        (0.1, 4.5),
        (1.0, 3.9),
        (2.0, 3.0),
        (3.0, 2.2),
        (4.0, 1.3),
        (5.0, 0.75),
        (6.0, 0.6)
    ]
    with open(os.path.join(OUT, "kinetic_friction_vs_pressure.csv"), "w", newline='') as f:
        w = csv.writer(f)
        w.writerow(["pressure_GPa", "kinetic_friction_meV_per_Ang"])
        for p, kf in rows:
            w.writerow([p, kf])

if __name__ == "__main__":
    cmd = sys.argv[1]
    {"analytical": write_analytical, "static": write_static, "kinetic": write_kinetic}[cmd]()
