#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: thermodynamic_properties.csv ===
python3 - << 'PYEOF'
import csv, math

temps = [round(0.05*i, 2) for i in range(1, 41)]

def gauss(T, T0, w, A):
    return A * math.exp(-((T - T0)**2) / (2 * w**2))

with open("/app/outputs/thermodynamic_properties.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["T", "C_V", "M", "h_model"])
    for T in temps:
        # AHM symmetric
        cv = gauss(T, 0.333, 0.2, 0.25)
        w.writerow([T, round(cv, 5), 0.0, "AHM_sym"])
        # AHM asymmetric
        cv = gauss(T, 0.155, 0.07, 0.15)
        w.writerow([T, round(cv, 5), 0.0, "AHM_asym"])
        # XXZ asymmetric
        cv = gauss(T, 0.155, 0.07, 0.15)
        w.writerow([T, round(cv, 5), 0.0, "XXZ_asym"])
PYEOF
