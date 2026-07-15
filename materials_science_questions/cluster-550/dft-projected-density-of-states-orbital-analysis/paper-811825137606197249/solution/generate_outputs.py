import csv, json, sys

def generate_csv():
    data = [
        ("T1", 0.6, "thiol-Au"),
        ("T2", 0.6, "thiol-Au"),
        ("T3", 2.2, "S-Au"),
        ("T4", 1.5, "H-Au"),
        ("T5", 1.5, "H-Au"),
    ]
    writer = csv.writer(sys.stdout)
    writer.writerow(["junction_type", "breaking_force_nN", "breaking_bond"])
    writer.writerows(data)

def generate_json():
    nN_to_eVA = 1.0/1.602  # 1 nN ≈ 0.624 eV/Å
    junction_params = {
        "T1": {"initial_length": 28.3, "breaking_step": 20, "force_nN": 0.6, "total_steps": 25},
        "T2": {"initial_length": 29.1, "breaking_step": 20, "force_nN": 0.6, "total_steps": 25},
        "T3": {"initial_length": 28.3, "breaking_step": 35, "force_nN": 2.2, "total_steps": 40},
        "T4": {"initial_length": 29.7, "breaking_step": 31, "force_nN": 1.5, "total_steps": 36},
        "T5": {"initial_length": 28.3, "breaking_step": 20, "force_nN": 1.5, "total_steps": 25},
    }
    step_size = 0.2
    result = {}
    for jtype, params in junction_params.items():
        L0 = params["initial_length"]
        break_step = params["breaking_step"]
        total_steps = params["total_steps"]
        slope = params["force_nN"] * nN_to_eVA  # eV per Å
        steps = []
        for i in range(total_steps):
            length = L0 + i * step_size
            energy = (i * step_size * slope) if i <= break_step else (break_step * step_size * slope)
            steps.append({
                "step_number": i,
                "length_angstrom": round(length, 2),
                "total_energy_eV": round(energy, 6)
            })
        result[jtype] = steps
    json.dump(result, sys.stdout, indent=2)

if __name__ == "__main__":
    if "--csv" in sys.argv:
        generate_csv()
    elif "--json" in sys.argv:
        generate_json()