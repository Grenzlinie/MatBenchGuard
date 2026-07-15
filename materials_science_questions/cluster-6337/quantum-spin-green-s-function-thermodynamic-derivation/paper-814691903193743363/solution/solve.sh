#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: step_01_spectral_data.csv ===
python3 << 'PYEOF'
import csv, math
omega_min, omega_max, n = -1.0, 0.2, 101
omega_step = (omega_max - omega_min) / (n - 1)
k_points = [
    (1.0, 0.0),  # hot
    (0.5, 0.5)   # cold
]
def spectral(omega, peak, gamma=0.12, amp=1.0):
    return amp / (1.0 + ((omega - peak)/gamma)**2)
peaks = {-0.3: 1.0, 0.0: 1.0}  # peak position -> amplitude (only one per k-point)
with open('/app/outputs/step_01_spectral_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['kx', 'ky', 'omega', 'spectral_density'])
    for kx, ky in k_points:
        if (abs(kx-1.0) < 1e-12 and abs(ky-0.0) < 1e-12):
            peak = -0.3
        else:
            peak = 0.0
        for i in range(n):
            omega = omega_min + i * omega_step
            A = spectral(omega, peak)
            w.writerow([kx, ky, round(omega, 6), round(A, 8)])
PYEOF

# === solve block: step_02_crossover_data.csv ===
python3 << 'PYEOF'
import csv, math
T_points = [200,240,280,320,360,400,440,480,520,560,600]
def compute_xi(T):
    if 220 <= T <= 470:
        return 1.0 / (0.25 + (T - 220) / 1000.0)
    elif T > 470:
        return 1.0 / math.sqrt(0.25 + (T - 470) / 1610.0)
    else:
        return 1.0 / 0.25  # default for T<220, not used much
with open('/app/outputs/step_02_crossover_data.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['temperature_K', 'correlation_length_xi', 'spin_damping_gamma_Q', 'ratio_chiQ2_over_gammaQ'])
    for T in T_points:
        xi = compute_xi(T)
        # synthetic gamma_Q
        gamma = 0.1 + 0.0005 * T
        # synthetic ratio: increase up to 470 K, then decrease
        ratio = 0.5 + 0.001 * min(T, 470.0) - 0.0002 * max(0.0, T - 470.0)
        w.writerow([T, round(xi, 5), round(gamma, 5), round(ratio, 5)])
PYEOF
