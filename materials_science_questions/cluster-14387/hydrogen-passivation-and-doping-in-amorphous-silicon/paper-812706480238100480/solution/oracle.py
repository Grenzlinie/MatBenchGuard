#!/usr/bin/env python3
import sys, json, math

def gaussian(x, mu, sigma, height):
    return height * math.exp(-0.5 * ((x - mu) / sigma) ** 2)

def make_pair_corr_sisi():
    """Synthetic Si-Si pair correlation resembling the paper's Model1 curve."""
    pts = []
    for i in range(0, 600, 2):
        r = i / 100.0  # 0.00 .. 5.98 step 0.02
        g = 0.0
        # first peak around 2.50 A
        g += gaussian(r, 2.50, 0.12, 6.0)
        g += gaussian(r, 2.50, 0.25, 1.5)
        # additional shoulders
        g += gaussian(r, 3.8, 0.15, 2.0)
        g += gaussian(r, 4.8, 0.2, 1.5)
        g += gaussian(r, 5.6, 0.3, 1.0)
        # small background
        g += 0.3 * math.exp(-((r - 2.0) / 1.5) ** 2) + 0.4
        # keep non-negative
        g = max(g, 0.01)
        pts.append([round(r, 2), round(g, 4)])
    return pts

def make_pair_corr_sih():
    """Synthetic Si-H pair correlation resembling Fig.2 sharp first peak at ~1.55 A and second at ~3.2 A."""
    pts = []
    for i in range(0, 500, 2):
        r = i / 100.0  # 0.00 .. 4.98 step 0.02
        g = 0.0
        g += gaussian(r, 1.55, 0.05, 25.0)
        g += gaussian(r, 3.15, 0.12, 5.0)
        g += gaussian(r, 3.30, 0.2, 3.0)
        g += gaussian(r, 4.2, 0.3, 2.0)
        g += 0.2 * math.exp(-((r - 2.0) / 1.0) ** 2) + 0.1
        g = max(g, 0.01)
        pts.append([round(r, 2), round(g, 4)])
    return pts

MODEL1_STRUCT = {
    "Si-Si_pair_corr": make_pair_corr_sisi(),
    "Si-H_pair_corr": make_pair_corr_sih(),
    "rms_bond_angle_deviation_degrees": 10.4,
    "average_Si-H_bond_length_A": 1.55,
    "mass_density_relative_to_cSi": 0.92
}

MODEL2_STRUCT = {
    "Si-Si_pair_corr": make_pair_corr_sisi(),           # same shape
    "Si-H_pair_corr": make_pair_corr_sih(),
    "rms_bond_angle_deviation_degrees": 9.51,
    "average_Si-H_bond_length_A": 1.56,                # slightly larger
    "mass_density_relative_to_cSi": 0.90              # 10% less than c-Si
}

MODEL1_DEFECT_OUTCOME = {
    "excitation_energies_eV": [1.7, 3.0, 5.0, 7.0],
    "dangling_bonds_created": False,
    "structural_changes": "none"
}

MODEL2_EXCITATION_49_50 = {
    "final_49_50_distance_A": 4.25,
    "energy_difference_eV": 0.64,
    "annealing_barrier_eV": 0.11,
    "number_of_dangling_bonds": 4
}

MODEL2_EXCITATION_32_54 = {
    "energy_difference_eV": 0.15,
    "annealing_barrier_eV": 0.04,
    "number_of_dangling_bonds": 2
}

def make_dos():
    """Generate synthetic DOS arrays: initial with gap ~1.3 eV, defect with mid-gap states."""
    energies = []
    dos_ini = []
    dos_def = []
    for i in range(-40, 41):
        e_ev = i / 10.0
        energies.append(round(e_ev, 1))
        # initial: clear gap around 0, band edges at -0.65 and 0.65
        if abs(e_ev) < 0.6:
            d_i = 0.02
        else:
            d_i = 0.3 + 0.5 * math.exp(-(abs(e_ev) - 0.7) ** 2 / 0.3)
        dos_ini.append(round(d_i, 5))
        # defect: add mid-gap peaks at -0.1, 0.1
        if abs(e_ev) < 0.6:
            d_d = 0.02 + 0.8 * gaussian(e_ev, -0.1, 0.08, 1.5) + 0.8 * gaussian(e_ev, 0.1, 0.08, 1.5)
        else:
            d_d = 0.3 + 0.5 * math.exp(-(abs(e_ev) - 0.7) ** 2 / 0.3) + 0.2 * gaussian(e_ev, -0.1, 0.12, 0.6)
        dos_def.append(round(d_d, 5))
    return {
        "initial_gap_eV": 1.3,
        "defect_gap_states_present": True,
        "DOS_energy_values": energies,
        "DOS_initial": dos_ini,
        "DOS_defect": dos_def
    }

MODEL2_DOS = make_dos()

DISPATCH = {
    "model1_structural_properties.json": MODEL1_STRUCT,
    "model2_structural_properties.json": MODEL2_STRUCT,
    "model1_defect_outcome.json": MODEL1_DEFECT_OUTCOME,
    "model2_excitation_49_50_defect.json": MODEL2_EXCITATION_49_50,
    "model2_excitation_32_54_defect.json": MODEL2_EXCITATION_32_54,
    "model2_defect_dos.json": MODEL2_DOS
}

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 oracle.py <output_filename>", file=sys.stderr)
        sys.exit(1)
    fname = sys.argv[1]
    if fname not in DISPATCH:
        print(f"Unknown output: {fname}", file=sys.stderr)
        sys.exit(1)
    outpath = f"/app/outputs/{fname}"
    with open(outpath, "w") as f:
        json.dump(DISPATCH[fname], f, indent=2)
