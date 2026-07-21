import sys
import csv
import json
import math

def generate_cooling(output_path):
    # Cooling curve: temperature in ε/kB, specularity.
    # Knee at T_knee = 0.18. Use logistic function.
    T_min = 0.0
    T_max = 0.4
    n_points = 200
    step = (T_max - T_min) / (n_points - 1)
    knee = 0.18
    slope = 0.02
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'specularity'])
        for i in range(n_points):
            T = T_max - i * step
            # Specularity high at low T (ordered), low at high T (disordered).
            # Logistic: S(T) = S_max - (S_max - S_min) / (1 + exp(-(T - knee)/slope))
            S_max = 0.75
            S_min = 0.50
            spec = S_max - (S_max - S_min) / (1.0 + math.exp(-(T - knee) / slope))
            writer.writerow([f"{T:.3f}", f"{spec:.6f}"])

def generate_recovery(output_path):
    # Recovery curves for 5% coverage at temperatures 0.18, 0.20, 0.22 ε/kB.
    # Each curve: specularity vs iteration_per_molecule.
    temperatures = [0.18, 0.20, 0.22]
    # Equilibrium specularity (higher at lower T)
    equil = {0.18: 0.74, 0.20: 0.72, 0.22: 0.70}
    # Rough recovery rate (per iteration) tuned to give plausible rise
    # Paper experimental rates: r_exp = (r_mod / tau0) * exp(-E_c/(k_B T_phys))
    # With E_c=0.3 eV, ε=0.10 eV, T_phys = T * (ε/k_B) ≈ T * 1160 K.
    # Not needed for synthetic curve; we pick a time constant.
    rate = {0.18: 0.0001, 0.20: 0.0003, 0.22: 0.0008}
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['temperature', 'iteration_per_molecule', 'specularity'])
        for T in temperatures:
            eq = equil[T]
            r = rate[T]
            start_spec = eq - 0.15  # initial disordered
            for it in range(0, 2001, 20):
                spec = eq - (eq - start_spec) * math.exp(-r * it)
                writer.writerow([f"{T:.2f}", f"{it}", f"{spec:.6f}"])

def generate_potentials(output_path):
    data = {
        "epsilon_eV": 0.10,
        "corrugation_eV": 0.3
    }
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=2)
        f.write('\n')

if __name__ == '__main__':
    mode = ""
    output = ""
    args = sys.argv[1:]
    if '-mode' in args or '--mode' in args:
        idx = args.index('--mode') if '--mode' in args else args.index('-mode')
        mode = args[idx + 1]
    if '-output' in args or '--output' in args:
        idx = args.index('--output') if '--output' in args else args.index('-output')
        output = args[idx + 1]
    if mode == 'cooling':
        generate_cooling(output)
    elif mode == 'recovery':
        generate_recovery(output)
    elif mode == 'potentials':
        generate_potentials(output)
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(1)
