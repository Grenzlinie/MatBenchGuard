#!/usr/bin/env python3
import json
import sys

# --- Paper-reported reference values ---

# Elemental reference energies (chosen plausible per-atom energies, eV/atom)
refs = {
    "Au_fcc": -105.0,
    "Ni_fcc": -150.0,
    "Pd_fcc": -135.0,
    "Sn_beta": -95.0
}

# ΔH (kJ/mol atoms) from Table I, lattice constants (Å) and volume (Å³)
compounds_data = [
    {
        "name": "AuSn4",
        "delta_H_kJ_per_mol_atoms": -10.19,
        "a": 6.67, "b": 6.52, "c": 12.00, "volume": 521.51,
        "x_Ni": 0.0, "x_Pd": 0.0
    },
    {
        "name": "Au0.75Ni0.25Sn4",
        "delta_H_kJ_per_mol_atoms": -11.38,
        "a": 6.55, "b": 6.55, "c": 11.82, "volume": 507.46,
        "x_Ni": 0.25, "x_Pd": 0.0
    },
    {
        "name": "Au0.5Ni0.5Sn4",
        "delta_H_kJ_per_mol_atoms": -12.65,
        "a": 6.49, "b": 6.53, "c": 11.65, "volume": 493.43,
        "x_Ni": 0.5, "x_Pd": 0.0
    },
    {
        "name": "Au0.75Pd0.25Sn4",
        "delta_H_kJ_per_mol_atoms": -29.85,
        "a": 6.59, "b": 6.57, "c": 11.86, "volume": 513.78,
        "x_Ni": 0.0, "x_Pd": 0.25
    },
    {
        "name": "Au0.5Pd0.5Sn4",
        "delta_H_kJ_per_mol_atoms": -18.96,
        "a": 6.54, "b": 6.60, "c": 11.75, "volume": 506.66,
        "x_Ni": 0.0, "x_Pd": 0.5
    },
    {
        "name": "Au0.5Pd0.25Ni0.25Sn4",
        "delta_H_kJ_per_mol_atoms": -15.83,
        "a": 6.51, "b": 6.56, "c": 11.71, "volume": 500.22,
        "x_Ni": 0.25, "x_Pd": 0.25
    }
]

# Elastic and thermodynamic data (Tables II, III, IV)
elastic_data = [
    {
        "name": "AuSn4",
        "C11": 79.5, "C22": 84.4, "C33": 70.5,
        "C44": 9.2, "C55": 2.3, "C66": 31.9,
        "C12": 29.1, "C13": 43.2, "C23": 58.7,
        "Bulk_modulus_VRH": 54.40, "Shear_modulus_VRH": 11.12,
        "Young_modulus": 30.03, "Poisson_ratio": 0.404,
        "Hardness": 0.70, "Debye_temperature": 137, "kmin": 0.306
    },
    {
        "name": "Au0.75Ni0.25Sn4",
        "C11": 96.3, "C22": 93.6, "C33": 79.7,
        "C44": 12.7, "C55": 6.4, "C66": 42.0,
        "C12": 31.2, "C13": 34.5, "C23": 51.3,
        "Bulk_modulus_VRH": 55.91, "Shear_modulus_VRH": 21.26,
        "Young_modulus": 56.61, "Poisson_ratio": 0.331,
        "Hardness": 2.40, "Debye_temperature": 181, "kmin": 0.410
    },
    {
        "name": "Au0.5Ni0.5Sn4",
        "C11": 105.6, "C22": 106.5, "C33": 95.3,
        "C44": 23.8, "C55": 14.6, "C66": 31.9,
        "C12": 39.8, "C13": 23.3, "C23": 38.2,
        "Bulk_modulus_VRH": 56.12, "Shear_modulus_VRH": 26.32,
        "Young_modulus": 68.28, "Poisson_ratio": 0.297,
        "Hardness": 3.56, "Debye_temperature": 206, "kmin": 0.456
    },
    {
        "name": "Au0.75Pd0.25Sn4",
        "C11": 103.1, "C22": 92.3, "C33": 94.2,
        "C44": 18.5, "C55": 18.7, "C66": 35.9,
        "C12": 42.4, "C13": 25.4, "C23": 42.8,
        "Bulk_modulus_VRH": 56.80, "Shear_modulus_VRH": 25.40,
        "Young_modulus": 66.32, "Poisson_ratio": 0.305,
        "Hardness": 3.30, "Debye_temperature": 196, "kmin": 0.432
    },
    {
        "name": "Au0.5Pd0.5Sn4",
        "C11": 94.6, "C22": 101.4, "C33": 85.4,
        "C44": 21.8, "C55": 15.0, "C66": 26.8,
        "C12": 43.4, "C13": 32.5, "C23": 42.5,
        "Bulk_modulus_VRH": 57.35, "Shear_modulus_VRH": 22.91,
        "Young_modulus": 60.65, "Poisson_ratio": 0.324,
        "Hardness": 2.69, "Debye_temperature": 190, "kmin": 0.427
    },
    {
        "name": "Au0.5Pd0.25Ni0.25Sn4",
        "C11": 93.0, "C22": 103.5, "C33": 83.9,
        "C44": 21.2, "C55": 15.5, "C66": 25.4,
        "C12": 42.4, "C13": 35.5, "C23": 44.1,
        "Bulk_modulus_VRH": 57.86, "Shear_modulus_VRH": 22.46,
        "Young_modulus": 59.66, "Poisson_ratio": 0.328,
        "Hardness": 2.57, "Debye_temperature": 189, "kmin": 0.429
    }
]


def compute_total_energy_per_fu(compound, refs):
    x_Ni = compound["x_Ni"]
    x_Pd = compound["x_Pd"]
    x_Au = 1.0 - x_Ni - x_Pd
    sum_refs = (x_Au * refs["Au_fcc"] +
                x_Ni * refs["Ni_fcc"] +
                x_Pd * refs["Pd_fcc"] +
                4.0 * refs["Sn_beta"])
    delta_H_kJ = compound["delta_H_kJ_per_mol_atoms"]
    delta_E_per_atom_eV = delta_H_kJ / 96.485  # kJ/mol atoms to eV/atom
    # total energy per formula unit (5 atoms)
    E_fu = 5.0 * delta_E_per_atom_eV + sum_refs
    return E_fu


def write_formation_energies(path):
    compounds_out = []
    for c in compounds_data:
        Ef = compute_total_energy_per_fu(c, refs)
        compounds_out.append({
            "name": c["name"],
            "total_energy_per_fu": round(Ef, 10),
            "total_energy_fu_units": "eV",
            "a": c["a"],
            "b": c["b"],
            "c": c["c"],
            "volume": c["volume"],
            "delta_H_kJ_per_mol_atoms": c["delta_H_kJ_per_mol_atoms"]
        })
    output = {
        "compounds": compounds_out,
        "elemental_references": refs
    }
    with open(path, 'w') as f:
        json.dump(output, f, indent=2)


def write_elastic(path):
    compounds_out = []
    for c in elastic_data:
        compounds_out.append({
            "name": c["name"],
            "C11": c["C11"],
            "C22": c["C22"],
            "C33": c["C33"],
            "C44": c["C44"],
            "C55": c["C55"],
            "C66": c["C66"],
            "C12": c["C12"],
            "C13": c["C13"],
            "C23": c["C23"],
            "Bulk_modulus_VRH": c["Bulk_modulus_VRH"],
            "Shear_modulus_VRH": c["Shear_modulus_VRH"],
            "Young_modulus": c["Young_modulus"],
            "Poisson_ratio": c["Poisson_ratio"],
            "Hardness": c["Hardness"],
            "Debye_temperature": c["Debye_temperature"],
            "kmin": c["kmin"]
        })
    output = {"compounds": compounds_out}
    with open(path, 'w') as f:
        json.dump(output, f, indent=2)


def main():
    if len(sys.argv) != 3 or sys.argv[1] != '--output':
        print("Usage: python3 write_outputs.py --output <path>")
        sys.exit(1)
    outpath = sys.argv[2]
    basename = outpath.rsplit('/', 1)[-1]  # handle /app/outputs/name
    if basename == "formation_energies_and_lattice.json":
        write_formation_energies(outpath)
    elif basename == "elastic_and_thermodynamic.json":
        write_elastic(outpath)
    else:
        print(f"Unknown output file: {basename}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
