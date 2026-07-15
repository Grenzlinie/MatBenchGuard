import json
import sys


def write_dft(out_path):
    data = [
        {"system": "V_Sn", "magnetic_moment": 4.00, "epsilon": 433.0, "binding_energy": 5.91},
        {"system": "V_S",  "magnetic_moment": 0.00, "epsilon": 0.0,   "binding_energy": 0.0},
        {"system": "Li",   "magnetic_moment": 3.00, "epsilon": 83.0,  "binding_energy": 3.19},
        {"system": "Na",   "magnetic_moment": 3.00, "epsilon": 75.0,  "binding_energy": 2.85},
        {"system": "K",    "magnetic_moment": 3.00, "epsilon": 153.0, "binding_energy": 2.39},
        {"system": "Mg",   "magnetic_moment": 1.71, "epsilon": 10.0,  "binding_energy": 5.30},
        {"system": "Ca",   "magnetic_moment": 2.00, "epsilon": 31.0,  "binding_energy": 6.10},
        {"system": "Sr",   "magnetic_moment": 2.00, "epsilon": 36.0,  "binding_energy": 5.77},
        {"system": "Al",   "magnetic_moment": 0.00, "epsilon": 0.0,   "binding_energy": 6.37},
        {"system": "Ga",   "magnetic_moment": 1.00, "epsilon": 2.0,   "binding_energy": 4.96},
        {"system": "In",   "magnetic_moment": 1.00, "epsilon": 3.0,   "binding_energy": 5.07}
    ]
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)


def write_strain(out_path):
    data = [
        {"system": "Mg", "strain": 0.0,  "epsilon": 10.0},
        {"system": "Mg", "strain": 5.0,  "epsilon": 20.0},
        {"system": "Mg", "strain": 10.0, "epsilon": 35.0},
        {"system": "Mg", "strain": 15.0, "epsilon": 55.0},
        {"system": "Al", "strain": 0.0,  "epsilon": 0.0},
        {"system": "Al", "strain": 5.0,  "epsilon": 5.0},
        {"system": "Al", "strain": 10.0, "epsilon": 15.0},
        {"system": "Al", "strain": 15.0, "epsilon": 30.0}
    ]
    with open(out_path, 'w') as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    meas = sys.argv[1]
    out_path = sys.argv[2]
    if meas == "dft":
        write_dft(out_path)
    elif meas == "strain":
        write_strain(out_path)
    else:
        sys.exit(1)
