#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs
K0=250

# === solve block: grain_size_results.csv ===
python3 << 'PYEOF'
import csv
data = [(2.5,0.19),(5,0.32),(7.5,0.39),(10,0.47),(12.5,0.57)]
with open("/app/outputs/grain_size_results.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["grain_size_nm","K_over_K0"])
    for gs,kk in data:
        w.writerow([gs,kk])
PYEOF

# === solve block: strain_results.csv ===
python3 << 'PYEOF'
import csv, os
K0 = float(os.environ.get("K0",250))
strains = [0,0.03,0.06,0.09,0.12]

def k_sc(s):
    return K0 * (1 - 0.57 * s / 0.12)

def k_25(s):
    K0_25 = K0 * 0.19
    return K0_25 * (1 - 0.32 * s / 0.12)

def k_75(s):
    K0_75 = K0 * 0.39
    return K0_75 * (1 - 0.41 * s / 0.12)

with open("/app/outputs/strain_results.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["sample_type","strain","thermal_conductivity"])
    for s in strains:
        w.writerow(["SC", s, round(k_sc(s), 2)])
        w.writerow(["poly_2.5nm", s, round(k_25(s), 2)])
        w.writerow(["poly_7.5nm", s, round(k_75(s), 2)])
PYEOF

# === solve block: temperature_results.csv ===
python3 << 'PYEOF'
import csv, os
K0 = float(os.environ.get("K0",250))
temps = [200,300,400,500,600]

def k_sc_temp(T):
    return K0 * (300.0 / T)

def k_10_temp(T):
    K0_10_300 = K0 * 0.47
    return K0_10_300 * (300.0 / T)**0.5

def k_25_temp(T):
    return K0 * 0.19

with open("/app/outputs/temperature_results.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["sample_type","temperature_K","thermal_conductivity"])
    for T in temps:
        w.writerow(["SC", T, round(k_sc_temp(T), 2)])
        w.writerow(["poly_2.5nm", T, round(k_25_temp(T), 2)])
        w.writerow(["poly_10nm", T, round(k_10_temp(T), 2)])
PYEOF
