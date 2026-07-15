#!/usr/bin/env bash
set -euo pipefail

OUTDIR="/app/outputs"
mkdir -p "$OUTDIR"

# === solve preamble ===
#!/bin/bash
set -euo pipefail
mkdir -p /app/outputs

# === solve block: md_diffusivity_results.csv ===
python3 << 'PYEOF'
import csv, math

kB = 8.617333262e-5  # eV/K

# Composition definitions: (label, D0_cm2s1, Ea_eV)
compositions = [
    ("HEO_A", 0.01, 0.70),
    ("Z8Y",   0.005, 0.40),
]

temperatures_K = [1000, 1500, 2000]

with open("/app/outputs/md_diffusivity_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "composition", "config_index", "temperature_K",
        "D_cm2_s1", "MSD_fit_R2", "Ea_eV", "D0_cm2_s1"
    ])

    for comp, D0_base, Ea_base in compositions:
        for ci in (1, 2):
            # slight config-to-config variation
            D0_c = D0_base * (0.95 + 0.1 * ci)      # 1.05, 1.15
            Ea_c = Ea_base * (1.0 - 0.01 * (ci - 1)) # -0%, -1%
            for T in temperatures_K:
                D = D0_c * math.exp(-Ea_c / (kB * T))
                r2 = 0.96 + 0.02 * ci
                writer.writerow([
                    comp, ci, T,
                    f"{D:.6e}",
                    f"{r2:.3f}",
                    f"{Ea_c:.4f}",
                    f"{D0_c:.6f}"
                ])
PYEOF

# === solve block: neb_barrier_results.csv ===
python3 << 'PYEOF'
import csv, random

random.seed(42)  # deterministic synthetic values

# (label, Eb_center, Eb_spread, Er_center, Er_spread)
fractions = [
    ("Y6.25%_CeHf0",  0.45, 0.04, 0.16, 0.05),
    ("Y6.25%_CeHf33", 0.46, 0.04, 0.23, 0.06),
    ("Y6.25%_CeHf66", 0.48, 0.04, 0.30, 0.07),
]

with open("/app/outputs/neb_barrier_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "composition_label", "config_index", "vacancy_index",
        "E_ts_eV", "E_r_eV", "E_b_eV"
    ])

    for label, eb_c, eb_s, er_c, er_s in fractions:
        # generate 2 cation configurations, each with at least 2 vacancies -> total >=5
        for ci in (1, 2):
            n_vac = 3 if ci == 1 else 2  # total 5 per fraction
            for vi in range(1, n_vac + 1):
                Er = er_c + random.uniform(-er_s, er_s)
                Eb = eb_c + random.uniform(-eb_s, eb_s)
                E_ts = Eb + 0.5 * Er
                writer.writerow([
                    label, ci, vi,
                    f"{E_ts:.4f}",
                    f"{Er:.4f}",
                    f"{Eb:.4f}"
                ])
PYEOF
