#!/usr/bin/env python3
"""Oracle helper: writes standard-answer artifacts to /app/outputs."""
import sys, os, json, csv, math
import numpy as np

OUTDIR = os.environ.get("OUTDIR", "/app/outputs")

def write_parameters():
    # Lithium parameters from paper
    n = 4.6e22          # cm^-3
    k_F = 1.1e8         # cm^-1
    epsilon_F_eV = 4.7  # eV
    hbar_omega0_eV = 0.07  # 70 meV
    a0_cm = 5.29e-9     # Bohr radius in cm (0.529 Å = 5.29e-9 cm)
    # Reduced bulk modulus of electrons b_F = pi * k_F * a0 / 4
    b_F = math.pi * k_F * a0_cm / 4.0
    param = {
        "n_cm_3": n,
        "k_F_cm_1": k_F,
        "epsilon_F_eV": epsilon_F_eV,
        "hbar_omega0_eV": hbar_omega0_eV,
        "b_F": b_F,
        "k_F_s_sq": 0.23   # (k_F s)^2 fixed
    }
    with open(os.path.join(OUTDIR, "parameters.json"), "w") as f:
        json.dump(param, f, indent=2)

def write_interaction_data():
    """Generate dummy v^s(omega) for each b0, saved as .npz."""
    b0_values = [-0.2, -0.1, 0.0, 0.1, 0.2, 0.5]
    data = {}
    omega = np.linspace(0, 0.1, 100)   # eV
    for b0 in b0_values:
        # Simple dummy: negative constant for negative b0, positive for positive b0
        if b0 < 0:
            v_s = -0.1 * np.ones_like(omega)
        elif b0 == 0:
            v_s = np.zeros_like(omega)
        else:
            v_s = 0.1 * np.ones_like(omega)
        data[f"b0_{b0}_omega"] = omega
        data[f"b0_{b0}_v_s"] = v_s
    np.savez(os.path.join(OUTDIR, "interaction_data.npz"), **data)

def write_gap_solutions():
    """Generate dummy gap functions and condensation energies for each b0."""
    b0_values = [-0.2, -0.1, 0.0, 0.1, 0.2, 0.5]
    # Tc values we hardcode
    Tc_map = {
        -0.2: 8.0,
        -0.1: 0.8,
         0.0: 0.005,
         0.1: 0.0005,
         0.2: 5e-5,
         0.5: 1e-6
    }
    epsilon_F_eV = 4.7
    k_B_eV_per_K = 8.617333262145e-5
    data = {}
    epsilon = np.linspace(0, 0.5, 200)  # eV
    for b0 in b0_values:
        Tc = Tc_map[b0]
        # Condensation energy from Tc formula: E_c = (k_B Tc / 0.925)^2 / epsilon_F
        E_c = (k_B_eV_per_K * Tc / 0.925) ** 2 / epsilon_F_eV
        # Gap function: Delta(epsilon) approx Delta0 * exp(-epsilon/0.05) with Delta0 = 1.76*k_B*Tc
        Delta0 = 1.76 * k_B_eV_per_K * Tc
        Delta = Delta0 * np.exp(-epsilon / 0.05)  # dummy decay
        data[f"b0_{b0}_epsilon"] = epsilon
        data[f"b0_{b0}_Delta"] = Delta
        data[f"b0_{b0}_E_c"] = np.array([E_c])
    np.savez(os.path.join(OUTDIR, "gap_solutions.npz"), **data)

def write_tc_csv():
    b0_values = [-0.2, -0.1, 0.0, 0.1, 0.2, 0.5]
    Tc_map = {
        -0.2: 8.0,
        -0.1: 0.8,
         0.0: 0.005,
         0.1: 0.0005,
         0.2: 5e-5,
         0.5: 1e-6
    }
    path = os.path.join(OUTDIR, "tc_vs_b0.csv")
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["b0", "Tc"])
        for b0 in b0_values:
            writer.writerow([b0, Tc_map[b0]])

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "--help"
    if cmd == "--output":
        target = sys.argv[2]
        if target == "parameters.json":
            write_parameters()
        elif target == "interaction_data.npz":
            write_interaction_data()
        elif target == "gap_solutions.npz":
            write_gap_solutions()
        elif target == "tc_vs_b0.csv":
            write_tc_csv()
        else:
            raise SystemExit(f"Unknown output: {target}")
    else:
        raise SystemExit("Usage: python helper.py --output <basename>")

if __name__ == "__main__":
    main()
