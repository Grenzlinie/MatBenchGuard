#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: absorption_vs_temperature.csv ===
# ------------------------------------------------------------
# absorption_vs_temperature.csv
# ------------------------------------------------------------
python3 <<'PYEOF'
import math
import csv

# KCl parameters from Table I
hbar_omega_max = 0.0342  # eV
k_min = 505
Ebar_l = 3.36           # normalized photon energy for 10.6 μm
k_B = 8.617333262145e-5  # eV/K

# Temperatures (K) to compute
temps = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]

# Helper to compute gamma ratio safely using log-gamma
def f_factor(k, m, Delta):
    """Compute f(k,m) from Eq. (39) using log-gamma to avoid overflow."""
    # prefactor
    numer = (k - 1 - 2*m) * (k - 1 - 2*m - 2*Delta)
    denom = (k - 1 - 2*m - Delta) ** 2
    pref = numer / denom
    # ratio of binomial coefficients = Gamma(m+Delta+1) * Gamma(k-m-Delta) / (Gamma(m+1) * Gamma(k-m))
    log_num = math.lgamma(m + Delta + 1) + math.lgamma(k - m - Delta)
    log_den = math.lgamma(m + 1) + math.lgamma(k - m)
    log_ratio = log_num - log_den
    # exp may underflow to 0.0 for very small values, that's fine
    ratio = math.exp(log_ratio) * pref
    return ratio

def compute_alpha(T):
    beta_bar = hbar_omega_max / (k_B * T)  # beta * hbar*omega_max
    total = 0.0
    max_Delta = 50  # safe cutoff; contributions decay rapidly
    for Delta in range(1, max_Delta + 1):
        y_val = Ebar_l / Delta
        if y_val <= 0:
            continue
        contrib_Delta = 0.0
        m = 0
        while True:
            A = (2*m + 1 + Delta) / k_min
            discriminant = 1 - 4*A*y_val
            if discriminant < 0:
                # For larger m, A increases, discriminant decreases, so no more roots
                break
            sqrtD = math.sqrt(discriminant)
            x_star = (1 - sqrtD) / (2*A)
            # only accept physically relevant root with 0 < x* < 1
            if 0 < x_star < 1:
                k = k_min * x_star
                # bound-state check: m <= (k-1)/2
                if m <= (k - 1) / 2:
                    # scaled energy Em from Eq. (41)
                    Ebar_m = (m + 0.5) * x_star - ((m + 0.5) ** 2) * x_star**2 / k_min
                    # Boltzmann factor
                    try:
                        exp_term = math.exp(-beta_bar * Ebar_m)
                    except OverflowError:
                        exp_term = 0.0
                    # f(k,m)
                    f_val = f_factor(k, m, Delta)
                    # denominator: (1 + 4/(k*beta_bar)) * (1 - 2*A*x_star)
                    denom = (1.0 + 4.0 / (k * beta_bar)) * (1.0 - 2.0 * A * x_star)
                    # Eq. (40) term (without outer constant)
                    term = x_star * exp_term * f_val / denom
                    contrib_Delta += term
            m += 1
        # outer Delta^{-3} factor
        total += Delta ** (-3) * contrib_Delta
    # Apply overall factor Ebar_l * beta_bar^2 (without arbitrary multiplicative constant)
    alpha = Ebar_l * (beta_bar ** 2) * total
    return alpha

# Compute and write CSV
output_path = "/app/outputs/absorption_vs_temperature.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["T_K", "alpha"])
    for T in temps:
        alpha = compute_alpha(T)
        writer.writerow([T, f"{alpha:.6e}"])

print("Done.")
PYEOF
