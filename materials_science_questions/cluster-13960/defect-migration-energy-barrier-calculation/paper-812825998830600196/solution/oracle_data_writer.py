import csv, json, sys, os

OUTDIR = "/app/outputs"
os.makedirs(OUTDIR, exist_ok=True)

# formation_energies.csv data (Table 1)
fe_data = [
    (1, 3.07, 3.33),
    (2, 6.08, 5.69),
    (3, 9.04, 8.21),
    (4, 11.90, 10.74),
    (5, 14.80, 13.09),
    (6, 17.65, 15.24),
    (7, 20.25, 17.85),
    (8, 23.41, 20.55),
    (9, 26.20, 23.17),
]

# binding_energies.csv data (incremental, from Eq. 2 with E_f(1) = 3.07)
be_data = [
    (2, 0.06, 0.71),
    (3, 0.11, 0.55),
    (4, 0.21, 0.54),
    (5, 0.17, 0.72),
    (6, 0.22, 0.92),
    (7, 0.47, 0.46),
    (8, -0.09, 0.37),
    (9, 0.28, 0.45),
]

# migration_barriers.csv data
mb_data = [
    (1, 0.35),
    (2, 0.45),
    (3, 0.54),
]

# max_occupancy.json data
mo_data = {
    "max_He_in_vacancy": 7,
    "spillover_observed": True
}


def write_formation_energies():
    path = os.path.join(OUTDIR, "formation_energies.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N_He", "E_f_groove_eV", "E_f_vacancy_eV"])
        for n, eg, ev in fe_data:
            w.writerow([n, f"{eg:.2f}", f"{ev:.2f}"])

def write_binding_energies():
    path = os.path.join(OUTDIR, "binding_energies.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N_He", "E_b_groove_eV", "E_b_vacancy_eV"])
        for n, ebg, ebv in be_data:
            w.writerow([n, f"{ebg:.2f}", f"{ebv:.2f}"])

def write_migration_barriers():
    path = os.path.join(OUTDIR, "migration_barriers.csv")
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["N_He", "barrier_eV"])
        for n, bar in mb_data:
            w.writerow([n, f"{bar:.2f}"])

def write_max_occupancy():
    path = os.path.join(OUTDIR, "max_occupancy.json")
    with open(path, "w") as f:
        json.dump(mo_data, f, indent=2)

if __name__ == "__main__":
    target = sys.argv[1]
    if target == "formation_energies.csv":
        write_formation_energies()
    elif target == "binding_energies.csv":
        write_binding_energies()
    elif target == "migration_barriers.csv":
        write_migration_barriers()
    elif target == "max_occupancy.json":
        write_max_occupancy()
    else:
        raise ValueError(f"Unknown target {target}")
