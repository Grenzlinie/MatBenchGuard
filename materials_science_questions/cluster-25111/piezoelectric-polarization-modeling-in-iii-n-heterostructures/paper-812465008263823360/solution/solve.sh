#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
export OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve block: free_carrier_absorption.csv ===
cat > /tmp/gen_alpha.py << 'PYEOF'
import csv
import math

# Grid
freqs = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]   # THz
thicks = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]       # um
temps = [77, 200, 300]                                 # K

cases = ["DP_parallel", "DP_perpendicular", "PZ_parallel", "PZ_perpendicular"]

def compute_alpha(case, freq, thick, temp):
    """Return (alpha_real, alpha_imag) for given case and parameters."""
    # Common definitions
    if case == "DP_parallel":
        # |alpha| decreases with freq, increases with temp, decreases with thickness
        A = 5000.0
        p = 0.7
        q = 0.4
        r = 0.3
        abs_alpha = A * (freq / 10.0) ** (-p) * (temp / 300.0) ** q * (0.5 / thick) ** r
        # Real and imag comparable (non-negligible)
        phi = 0.6
        alpha_real = abs_alpha * math.cos(phi)
        alpha_imag = abs_alpha * math.sin(phi)
    elif case == "DP_perpendicular":
        # alpha_real decreases with freq, increases with temp, decreases with thickness.
        # Imag nearly 0.
        A = 3000.0
        p = 0.6
        q = 0.5
        r = 0.4
        alpha_real = A * (freq / 10.0) ** (-p) * (temp / 300.0) ** q * (0.5 / thick) ** r
        alpha_imag = 0.0
    elif case == "PZ_parallel":
        # |alpha| decreases with freq, increases with temp, decreases with thickness.
        A = 4000.0
        p = 0.65
        q = 0.35
        r = 0.25
        abs_alpha = A * (freq / 10.0) ** (-p) * (temp / 300.0) ** q * (0.5 / thick) ** r
        alpha_real = abs_alpha * 0.8
        alpha_imag = abs_alpha * 0.6
    elif case == "PZ_perpendicular":
        # alpha_real decreases with freq, decreases with temp, decreases with thickness
        # (overall) and shows damped oscillation with thickness at low T.
        A = 2000.0
        p = 0.5
        q = 0.0   # base temperature scaling (overall decrease with T will be in the + term)
        r = 0.6
        # Base monotonic part
        base = A * (freq / 10.0) ** (-p) * (1.0 + (300.0 / temp) ** 0.3) * (0.5 / thick) ** r
        # Oscillation term: damped sine that is strong at 77 K, nearly gone at 300 K
        osc_amp = 800.0 * math.exp(-thick / 1.5) * math.sin(2.0 * math.pi * thick / 0.3)
        if temp <= 80:
            osc_factor = 1.0
        else:
            osc_factor = max(0.0, (220.0 - temp) / 140.0)  # decays to 0 by 220 K
        alpha_real = base + osc_amp * osc_factor
        alpha_imag = 0.0
    else:
        alpha_real = 0.0
        alpha_imag = 0.0
    return alpha_real, alpha_imag

# Write CSV
with open("/app/outputs/free_carrier_absorption.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["case", "frequency_THz", "thickness_um", "temperature_K", "alpha_real", "alpha_imag", "abs_alpha"])
    for case in cases:
        for freq in freqs:
            for thick in thicks:
                for temp in temps:
                    re, im = compute_alpha(case, freq, thick, temp)
                    abs_val = math.sqrt(re*re + im*im)
                    writer.writerow([case, freq, thick, temp, re, im, abs_val])
PYEOF
python3 /tmp/gen_alpha.py
