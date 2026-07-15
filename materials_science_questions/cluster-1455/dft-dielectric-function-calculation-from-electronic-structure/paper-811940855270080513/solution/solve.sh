#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

cat <<'PYSCRIPT' > /tmp/gen_epsilon.py
import csv, cmath, math, sys

params = {
    440: {"nu1": 35.0, "gamma1": 100.0, "S1": 800000.0, "nu2": 90.0, "gamma2": 120.0, "S2": 600000.0},
    470: {"nu1": 38.0, "gamma1": 90.0,  "S1": 800000.0, "nu2": 84.0, "gamma2": 113.0, "S2": 600000.0}
}

def eps_model(nu, p):
    return (p["S1"]/(p["nu1"]**2 - nu**2 + 1j*p["gamma1"]*nu) +
            p["S2"]/(p["nu2"]**2 - nu**2 + 1j*p["gamma2"]*nu))

def find_peaks(freqs, eps_imag):
    peaks = []
    n = len(freqs)
    for i in range(1, n-1):
        if eps_imag[i] > eps_imag[i-1] and eps_imag[i] > eps_imag[i+1]:
            peaks.append((freqs[i], eps_imag[i]))
    peaks.sort(key=lambda x: -x[1])
    top = sorted([p[0] for p in peaks[:2]])
    if len(top) >= 2:
        return top[0], top[1]
    return None, None

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "epsilon_spectra":
        with open("/app/outputs/epsilon_spectra.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["temperature", "frequency", "epsilon_real", "epsilon_imag"])
            for T, p in sorted(params.items()):
                for nu in range(1, 151):
                    eps = eps_model(nu, p)
                    w.writerow([T, nu, eps.real, eps.imag])
    elif cmd == "mode_parameters":
        with open("/app/outputs/mode_parameters.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["temperature", "nu1", "gamma1", "S1", "nu2", "gamma2", "S2", "nu1_prime", "nu2_prime"])
            for T, p in sorted(params.items()):
                freqs = list(range(1, 151))
                eps_imag = [eps_model(nu, p).imag for nu in freqs]
                p1, p2 = find_peaks(freqs, eps_imag)
                w.writerow([T, p["nu1"], p["gamma1"], p["S1"], p["nu2"], p["gamma2"], p["S2"], p1, p2])
PYSCRIPT

# === solve block: epsilon_spectra.csv ===
cat <<'PYSCRIPT' > /tmp/gen_epsilon.py
import csv, math, sys

params = {
    440: {"nu1": 12.0, "gamma1": 45.0, "S1": 500000.0, "nu2": 68.0, "gamma2": 80.0, "S2": 300000.0},
    470: {"nu1": 16.0, "gamma1": 50.0, "S1": 450000.0, "nu2": 65.0, "gamma2": 70.0, "S2": 350000.0}
}

def eps_model(nu, p):
    return (p["S1"]/(p["nu1"]**2 - nu**2 + 1j*p["gamma1"]*nu) +
            p["S2"]/(p["nu2"]**2 - nu**2 + 1j*p["gamma2"]*nu))

def find_peaks(freqs, eps_imag):
    peaks = []
    n = len(freqs)
    for i in range(1, n-1):
        if eps_imag[i] > eps_imag[i-1] and eps_imag[i] > eps_imag[i+1]:
            peaks.append((freqs[i], eps_imag[i]))
    peaks.sort(key=lambda x: -x[1])
    top = sorted([p[0] for p in peaks[:2]])
    if len(top) >= 2:
        return top[0], top[1]
    return None, None

if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "epsilon_spectra":
        with open("/app/outputs/epsilon_spectra.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["temperature", "frequency", "epsilon_real", "epsilon_imag"])
            for T, p in sorted(params.items()):
                for nu in range(1, 151):
                    eps = eps_model(nu, p)
                    w.writerow([T, nu, eps.real, eps.imag])
    elif cmd == "mode_parameters":
        with open("/app/outputs/mode_parameters.csv", "w", newline='') as f:
            w = csv.writer(f)
            w.writerow(["temperature", "nu1", "gamma1", "S1", "nu2", "gamma2", "S2", "nu1_prime", "nu2_prime"])
            for T, p in sorted(params.items()):
                freqs = list(range(1, 151))
                eps_imag = [eps_model(nu, p).imag for nu in freqs]
                p1, p2 = find_peaks(freqs, eps_imag)
                w.writerow([T, p["nu1"], p["gamma1"], p["S1"], p["nu2"], p["gamma2"], p["S2"], p1, p2])
PYSCRIPT
python3 /tmp/gen_epsilon.py epsilon_spectra

# === solve block: mode_parameters.csv ===
python3 /tmp/gen_epsilon.py mode_parameters
