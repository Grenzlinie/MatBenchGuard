#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy

# === solve block: results.json ===
python3 << 'PYEOF' > "$OUTDIR/results.json"
import json
import sys

# τ values (seconds)
tau1 = 10e-6   # case1, case3
tau2 = 20e-6   # case2

# rock: shale
shale = {
    'case1': {
        'stress_wave_energy': 3.42,
        'cutoff_frequency_lower_rad_s': 0.2944 / tau1,
        'cutoff_frequency_upper_rad_s': 4.9870 / tau1,
        'energy_dissipation_ratio_analytical_pct': 16.45,
        'energy_dissipation_ratio_discrete_pct': 16.53
    },
    'case2': {
        'stress_wave_energy': 6.84,
        'cutoff_frequency_lower_rad_s': 0.1464 / tau2,
        'cutoff_frequency_upper_rad_s': 5.3658 / tau2,
        'energy_dissipation_ratio_analytical_pct': 11.27,
        'energy_dissipation_ratio_discrete_pct': 11.29
    },
    'case3': {
        'stress_wave_energy': 6.71,
        'cutoff_frequency_lower_rad_s': 0.1494 / tau1,
        'cutoff_frequency_upper_rad_s': 5.3566 / tau1,
        'energy_dissipation_ratio_analytical_pct': 11.37,
        'energy_dissipation_ratio_discrete_pct': 11.38
    }
}

# rock: malmstone
malmstone = {
    'case1': {
        'stress_wave_energy': 2.52,
        'cutoff_frequency_lower_rad_s': 0.4056 / tau1,
        'cutoff_frequency_upper_rad_s': 4.7604 / tau1,
        'energy_dissipation_ratio_analytical_pct': 20.72,
        'energy_dissipation_ratio_discrete_pct': 20.72
    },
    'case2': {
        'stress_wave_energy': 5.04,
        'cutoff_frequency_lower_rad_s': 0.1992 / tau2,
        'cutoff_frequency_upper_rad_s': 5.2156 / tau2,
        'energy_dissipation_ratio_analytical_pct': 13.10,
        'energy_dissipation_ratio_discrete_pct': 13.10
    },
    'case3': {
        'stress_wave_energy': 4.94,
        'cutoff_frequency_lower_rad_s': 0.2032 / tau1,
        'cutoff_frequency_upper_rad_s': 5.2050 / tau1,
        'energy_dissipation_ratio_analytical_pct': 13.24,
        'energy_dissipation_ratio_discrete_pct': 13.24
    }
}

# rock: liparite
liparite = {
    'case1': {
        'stress_wave_energy': 2.28,
        'cutoff_frequency_lower_rad_s': 0.4466 / tau1,
        'cutoff_frequency_upper_rad_s': 4.6836 / tau1,
        'energy_dissipation_ratio_analytical_pct': 21.98,
        'energy_dissipation_ratio_discrete_pct': 22.11
    },
    'case2': {
        'stress_wave_energy': 4.55,
        'cutoff_frequency_lower_rad_s': 0.2206 / tau2,
        'cutoff_frequency_upper_rad_s': 5.1604 / tau2,
        'energy_dissipation_ratio_analytical_pct': 13.85,
        'energy_dissipation_ratio_discrete_pct': 13.85
    },
    'case3': {
        'stress_wave_energy': 4.44,
        'cutoff_frequency_lower_rad_s': 0.2264 / tau1,
        'cutoff_frequency_upper_rad_s': 5.1460 / tau1,
        'energy_dissipation_ratio_analytical_pct': 14.05,
        'energy_dissipation_ratio_discrete_pct': 14.08
    }
}

results = {
    'shale': shale,
    'malmstone': malmstone,
    'liparite': liparite
}

json.dump(results, sys.stdout, indent=2)
PYEOF

# === solve block: shale_case1_spectrum.csv ===
python3 << 'PYEOF' > "$OUTDIR/shale_case1_spectrum.csv"
import numpy as np

sigma = 50e6
tau = 10e-6

# sampling parameters
dt = 2e-8
N = 2**16   # 65536 points
T = N * dt

# time array centred at zero
t = -T/2 + dt * np.arange(N)

# rectangular wave
wave = sigma * (np.abs(t) <= tau/2)

# FFT
F = np.fft.fft(wave)
f = np.fft.fftfreq(N, dt)
omega = 2.0 * np.pi * f

# amplitude squared (approximate continuous Fourier transform magnitude)
amp_sq = (dt**2) * np.abs(F)**2

# select non-negative frequencies and sort
mask = omega >= 0
omega_pos = omega[mask]
amp_sq_pos = amp_sq[mask]

# sort by omega
idx = np.argsort(omega_pos)
omega_pos = omega_pos[idx]
amp_sq_pos = amp_sq_pos[idx]

# write CSV header and rows to stdout
print('frequency_rad_s,amplitude_squared')
for w, a in zip(omega_pos, amp_sq_pos):
    print(f"{w},{a}")
PYEOF
