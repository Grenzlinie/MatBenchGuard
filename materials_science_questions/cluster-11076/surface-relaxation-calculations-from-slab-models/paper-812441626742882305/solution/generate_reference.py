#!/usr/bin/env python3
import csv
import math
import sys

def solve_linear3(A, b):
    """Solve 3x3 linear system A x = b via Gaussian elimination."""
    M = [A[i] + [b[i]] for i in range(3)]
    for i in range(3):
        # pivot
        max_row = max(range(i, 3), key=lambda r: abs(M[r][i]))
        if max_row != i:
            M[i], M[max_row] = M[max_row], M[i]
        if abs(M[i][i]) < 1e-12:
            raise ValueError("Singular matrix")
        for j in range(i + 1, 3):
            factor = M[j][i] / M[i][i]
            for k in range(i, 4):
                M[j][k] -= factor * M[i][k]
    x = [0, 0, 0]
    for i in reversed(range(3)):
        x[i] = M[i][3]
        for j in range(i + 1, 3):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]
    return x

def gsf_coeffs(q_peak, E_peak, E_one):
    """Return [a, b, c] for E(q) = a q^4 + b q^3 + c q^2 (d=0)."""
    A = [
        [1, 1, 1],
        [q_peak**4, q_peak**3, q_peak**2],
        [4 * q_peak**3, 3 * q_peak**2, 2 * q_peak],
    ]
    b = [E_one, E_peak, 0.0]
    return solve_linear3(A, b)

def evaluate_gsf(q, coeffs):
    a, b, c = coeffs
    return a * q**4 + b * q**3 + c * q**2

# --- Physical constants ---
PD_A0 = 3.8907          # Å
PT_A0 = 3.9239          # Å
PD_D111 = PD_A0 / math.sqrt(3)
PT_D111 = PT_A0 / math.sqrt(3)

# --- GSF curve parameters (paper Table I and text) ---
# Relaxed
PD_SFE_RELAXED = 225         # mJ/m²
PD_UNSTABLE_RELAXED = 383    # mJ/m²
PT_SFE_RELAXED = 339
PT_UNSTABLE_RELAXED = 432

# Unrelaxed (derived from reported percent reductions)
PD_SFE_UNRELAXED = PD_SFE_RELAXED / 0.95   # 5% reduction
PT_SFE_UNRELAXED = PT_SFE_RELAXED / 0.88   # 12% reduction

PD_UNSTABLE_UNRELAXED = 452  # mJ/m² (explicit in paper)
PT_UNSTABLE_UNRELAXED = 490  # mJ/m²

# Peak positions
PD_Q_PEAK_RELAXED = 0.5
PT_Q_PEAK_RELAXED = 0.6
# For unrelaxed we assume same peak positions
PD_Q_PEAK_UNRELAXED = 0.5
PT_Q_PEAK_UNRELAXED = 0.6

# Pre‑compute coefficients
PD_COEFF_REL = gsf_coeffs(PD_Q_PEAK_RELAXED, PD_UNSTABLE_RELAXED, PD_SFE_RELAXED)
PT_COEFF_REL = gsf_coeffs(PT_Q_PEAK_RELAXED, PT_UNSTABLE_RELAXED, PT_SFE_RELAXED)
PD_COEFF_UNREL = gsf_coeffs(PD_Q_PEAK_UNRELAXED, PD_UNSTABLE_UNRELAXED, PD_SFE_UNRELAXED)
PT_COEFF_UNREL = gsf_coeffs(PT_Q_PEAK_UNRELAXED, PT_UNSTABLE_UNRELAXED, PT_SFE_UNRELAXED)

# --- Interlayer spacing helpers (synthetic trends matching Fig. 2) ---
def pd_layer1(q):
    return PD_D111 - 0.06 * math.sin(math.pi * q)

def pd_layer2(q):
    return PD_D111 + 0.04 * (0.5 - q) * math.sin(math.pi * q)

def pd_layer3(q):
    return PD_D111 + 0.03 * math.sin(math.pi * q)

def pt_layer1(q):
    return PT_D111 - 0.05 * math.sin(math.pi * q)

def pt_layer2(q):
    return PT_D111 - 0.04 * math.sin(math.pi * q)

def pt_layer3(q):
    return PT_D111 + 0.03 * math.sin(math.pi * q)

# --- Main ---
def main():
    if len(sys.argv) < 2:
        print("Usage: generate_reference.py <output_path>")
        sys.exit(1)
    outpath = sys.argv[1]
    # Determine which file to produce
    if outpath.endswith("gsf_energy.csv"):
        write_gsf_energy(outpath)
    elif outpath.endswith("interlayer_spacings.csv"):
        write_interlayer(outpath)
    elif outpath.endswith("summary.csv"):
        write_summary(outpath)
    else:
        print(f"Unknown output file: {outpath}")
        sys.exit(1)

def write_gsf_energy(path):
    q_vals = [round(i * 0.1, 1) for i in range(11)]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metal", "q", "relaxed_energy", "unrelaxed_energy"])
        for q in q_vals:
            writer.writerow(["Pd", q,
                             round(evaluate_gsf(q, PD_COEFF_REL), 2),
                             round(evaluate_gsf(q, PD_COEFF_UNREL), 2)])
        for q in q_vals:
            writer.writerow(["Pt", q,
                             round(evaluate_gsf(q, PT_COEFF_REL), 2),
                             round(evaluate_gsf(q, PT_COEFF_UNREL), 2)])

def write_interlayer(path):
    q_vals = [round(i * 0.1, 1) for i in range(11)]
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metal", "q", "layer_number", "relaxed_spacing", "unrelaxed_spacing"])
        # Pd
        for q in q_vals:
            writer.writerow(["Pd", q, 1, round(pd_layer1(q), 5), round(PD_D111, 5)])
        for q in q_vals:
            writer.writerow(["Pd", q, 2, round(pd_layer2(q), 5), round(PD_D111, 5)])
        for q in q_vals:
            writer.writerow(["Pd", q, 3, round(pd_layer3(q), 5), round(PD_D111, 5)])
        # Pt
        for q in q_vals:
            writer.writerow(["Pt", q, 1, round(pt_layer1(q), 5), round(PT_D111, 5)])
        for q in q_vals:
            writer.writerow(["Pt", q, 2, round(pt_layer2(q), 5), round(PT_D111, 5)])
        for q in q_vals:
            writer.writerow(["Pt", q, 3, round(pt_layer3(q), 5), round(PT_D111, 5)])

def write_summary(path):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["metal", "SFE", "unstable_SFE", "c_over_a"])
        writer.writerow(["Pd", PD_SFE_RELAXED, PD_UNSTABLE_RELAXED, 1.632])
        writer.writerow(["Pt", PT_SFE_RELAXED, PT_UNSTABLE_RELAXED, 1.620])

if __name__ == "__main__":
    main()
