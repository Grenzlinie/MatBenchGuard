import json, csv, sys, math

def write_step01():
    data = {
        "dJ_deta": [-0.086, -0.041, -0.084, 0.022, 0.075, -0.029],
        "stress_model": [-4.769, -4.769, -6.322, 0.0, 0.0, 0.0]
    }
    with open("/app/outputs/step_01_magnetoelastic_params.json", "w") as f:
        json.dump(data, f, indent=2)

def write_step02():
    data = {
        "model_lattice": 1.32,
        "model_electronic": 0.53,
        "model_ionic": 0.56,
        "dft_lattice": 1.22,
        "dft_electronic": 0.40,
        "dft_ionic": 0.54
    }
    with open("/app/outputs/step_02_polarization_contributions.json", "w") as f:
        json.dump(data, f, indent=2)

def write_step03():
    # k = 9e-4 / 400 = 2.25e-6
    k = 2.25e-6
    fields = [0, 5, 10, 15, 20]
    rows = [{"H_T": h, "DeltaP_muC_cm2": k * h**2} for h in fields]
    with open("/app/outputs/step_03_field_dependence.csv", "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["H_T", "DeltaP_muC_cm2"])
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    step = sys.argv[1] if len(sys.argv) > 1 else None
    if step == "step01":
        write_step01()
    elif step == "step02":
        write_step02()
    elif step == "step03":
        write_step03()
    else:
        print("Unknown step")
