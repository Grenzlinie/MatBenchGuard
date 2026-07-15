#!/usr/bin/env python3
"""
Compute Faraday rotation noise spectrum S_FR(Ω) for:
  N=50, T=0 K, ω_ex/γ=5, Ω_L τ_s=20
in the adiabatic Gaussian limit.
Outputs /app/outputs/faraday_noise_spectrum.csv with columns: frequency, intensity.
"""

import csv
import numpy as np
from scipy.integrate import quad

# Parameters
N = 50
s = 2.5                     # Mn²⁺ spin quantum number
ws_ratio = 5.0              # ω_ex/γ
Omega_L = 1.0               # Larmor frequency (units)
tau_s = 20.0                # transverse relaxation time, scaled so Ω_L τ_s = 20

# Spin expectation values at T=0
Ix = N * s                  # ⟨I_x⟩
Iz2 = N / 2.0 * (s * (s + 1) - s**2)  # ⟨I_z^2⟩

# μ_− (μ_+ = 0 at T=0)
mu_minus = (ws_ratio**2 / 2.0) * (Iz2 + Ix / 2.0)

# Odd harmonics up to 21 (n_max = 21) – ample for range [-10,0]
n_max = 21
n_odds = np.arange(1, n_max + 2, 2, dtype=int)

# Compute amplitude J_n = ∫_0^∞ exp(-2k - μ_minus k^2) * (μ_minus k^2)^n / n! dk
def integrand(k, n, mu):
    from scipy.special import factorial
    term = (mu * k**2)**n / factorial(n)
    return np.exp(-2 * k - mu * k**2) * term

J = np.zeros(len(n_odds))
for i, n in enumerate(n_odds):
    J[i], _ = quad(integrand, 0, np.inf, args=(n, mu_minus), limit=200)

# Frequency grid (units of Ω_L): from -10 to 0 with step ≤ 0.05
freq_step = 0.05
freq = np.arange(-10.0, 0.0 + freq_step/2, freq_step)  # ensures endpoint 0.0 included

# Compute S_FR(Ω) = 0.5 * sum_n [ L_n(Ω) + L_n(-Ω) ]
# where L_n(Ω) = 2*(n/τ_s) / ((Ω - nΩ_L)^2 + (n/τ_s)^2)
S = np.zeros_like(freq)
for i, n in enumerate(n_odds):
    nOL = n * Omega_L
    gamma_n = n / tau_s
    denom_pos = (freq - nOL)**2 + gamma_n**2
    denom_neg = (freq + nOL)**2 + gamma_n**2
    L_pos = 2.0 * gamma_n / denom_pos
    L_neg = 2.0 * gamma_n / denom_neg
    S += J[i] * 0.5 * (L_pos + L_neg)

# Write CSV
output_path = "/app/outputs/faraday_noise_spectrum.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["frequency", "intensity"])
    for fv, sv in zip(freq, S):
        writer.writerow([f"{fv:.4f}", f"{sv:.10e}"])
